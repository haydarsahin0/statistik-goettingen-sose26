"""Gemeinsames Gerüst für die Formelsammlungen (Statistik + R).
Einträge werden gesammelt, gerendert und in zwei Durchgängen gebaut:
1. Durchgang ohne Seitenzahlen → PDF → Linkziele auslesen; 2. Durchgang mit Seitenzahlen."""
import os, re, subprocess
import pymupdf

SRC = os.path.dirname(os.path.abspath(__file__))


def eid(no):
    return "e-" + no.replace(".", "-")


class Doc:
    def __init__(self, key, cls, title, sub, chip, intro, howto, foot, outname):
        self.key, self.cls, self.title, self.sub, self.chip = key, cls, title, sub, chip
        self.intro, self.howto, self.foot, self.outname = intro, howto, foot, outname
        self.secs, self.finder, self.tail = [], [], ""

    # ---------- Inhalte sammeln ----------
    def S(self, no, title, intro=""):
        self.secs.append(dict(no=no, title=title, intro=intro, entries=[]))

    def E(self, no, title, sig="", ne="", fm="", st=None, bsp="", fa="", ks="", extra="", long=False, **kw):
        self.secs[-1]["entries"].append(dict(no=no, title=title, sig=sig, ne=ne, fm=fm, st=st or [],
                                             bsp=bsp, fa=fa, ks=ks, extra=extra, long=long, **kw))

    def F(self, *row):
        """Finder-Zeile: F('Gruppe') oder F(signal_de, tr, nr)."""
        self.finder.append(row)

    # ---------- Rendern ----------
    def _p(self, pages, key):
        return str(pages[key]) if pages and key in pages else "00"

    def render(self, pages=None):
        H = ['<section class="%s">' % self.cls]
        H.append('<div class="fs-hero"><div class="chip">%s</div><h1>%s</h1><div class="sub">%s</div>%s</div>'
                 % (self.chip, self.title, self.sub, self.intro))
        H.append('<div class="howto">%s</div>' % self.howto.replace(
            "{FINDER}", '<a href="#finder" style="color:inherit">Aufgaben-Finder (Seite %s)</a>' % self._p(pages, "finder")))
        # Inhaltsverzeichnis
        H.append('<h2 class="toc-h">Inhaltsverzeichnis</h2><div class="toc">')
        for s in self.secs:
            sid = "s-" + s["no"]
            H.append('<div class="ts"><a href="#%s"><div class="tsh"><span class="x">%s · %s</span><span class="p">%s</span></div></a>'
                     % (sid, s["no"], s["title"], self._p(pages, sid)))
            for e in s["entries"]:
                k = eid(e["no"])
                H.append('<a href="#%s"><div class="tl"><span class="n">%s</span><span class="x">%s</span><span class="dots"></span><span class="p">%s</span></div></a>'
                         % (k, e["no"], e["title"], self._p(pages, k)))
            H.append('</div>')
        H.append('</div>')
        # Aufgaben-Finder
        if self.finder:
            H.append('<h2 class="toc-h pb" id="finder">Aufgaben-Finder: Was steht in der Aufgabe? → Wo ist das Rezept?</h2>'
                     '<p class="small">Links steht der typische Wortlaut aus Klausur, Testat oder Tutorium, in der Mitte die türkische Bedeutung, rechts die Nummer des Rezepts (mit Seite). Nummer anklicken springt direkt hin.</p>'
                     '<table class="finder"><tr><th style="width:44%">In der Aufgabe steht …</th><th>Ne demek / ne isteniyor</th><th style="width:15%">Rezept</th></tr>')
            for row in self.finder:
                if len(row) == 1:
                    H.append('<tr class="grp"><td colspan="3">%s</td></tr>' % row[0])
                else:
                    sig, tr, nos = row
                    links = ", ".join('<a href="#%s">%s <span style="color:#6b7280;font-weight:600">S.%s</span></a>'
                                      % (eid(n), n, self._p(pages, eid(n))) for n in nos.split(","))
                    H.append('<tr><td>%s</td><td>%s</td><td class="go">%s</td></tr>' % (sig, tr, links))
            H.append('</table>')
        # Abschnitte
        first = True
        for s in self.secs:
            # Überschrift + Einleitung + erster Eintrag bleiben zusammen (kein Waisenkind am Seitenende)
            head = ['<h2 class="sec" id="s-%s"><span class="sn">%s</span> %s</h2>' % (s["no"], s["no"], s["title"])]
            if s["intro"]:
                head.append('<p class="secintro">%s</p>' % s["intro"])
            ents = s["entries"]
            keep = ents and not ents[0]["long"]
            if keep:
                head.append(self.entry(ents[0]))
            H.append('<div class="sechead%s">%s</div>' % (" pb" if first else "", "\n".join(head)))
            first = False
            for e in (ents[1:] if keep else ents):
                H.append(self.entry(e))
        H.append(self.tail)
        H.append('</section>')
        return "\n".join(H)

    def entry(self, e):
        # inline-Brüche in Text, Beispielen und Tabellen groß setzen (lesbar auf dem Handy)
        big = lambda x: re.sub(r'\\t?frac(?![a-z])', r'\\dfrac', x) if isinstance(x, str) else [big(y) for y in x]
        e = dict(e, **{k: big(e[k]) for k in ("ne", "st", "bsp", "fa", "ks", "extra")})
        o = ['<div class="e%s" id="%s"><div class="eh"><span class="no">%s</span><span class="ti">%s</span></div>'
             % (" long" if e["long"] else "", eid(e["no"]), e["no"], e["title"])]
        if e["sig"]:
            o.append('<span class="sig"><b>Erkennen:</b> %s</span>' % e["sig"])
        if e["ne"]:
            o.append('<div class="ne">%s</div>' % e["ne"])
        if e["fm"]:
            o.append('<div class="fm">%s</div>' % e["fm"])
        if e["st"]:
            o.append('<ol class="st">%s</ol>' % "".join("<li>%s</li>" % x for x in e["st"]))
        if e.get("rhtml"):
            o.append(e["rhtml"])
        if e.get("img"):
            o.append('<div class="imgs">%s</div>' % "".join('<img src="fig/%s">' % f for f in e["img"]))
        if e["extra"]:
            o.append(e["extra"])
        if e["bsp"]:
            o.append('<div class="bsp"><b>Beispiel.</b> %s</div>' % e["bsp"])
        if e["fa"]:
            o.append('<div class="fa">%s</div>' % e["fa"])
        if e["ks"]:
            o.append('<div class="ks">%s</div>' % e["ks"])
        o.append('</div>')
        return "\n".join(o)

    # ---------- Bauen ----------
    def _make(self, html):
        fn = "fs_%s.html" % self.key
        open(os.path.join(SRC, "content", fn), "w", encoding="utf-8").write(html)
        env = dict(os.environ, THEME="fs", FOOT=self.foot, PARTS=fn, OUTNAME=self.outname)
        r = subprocess.run(["./make.sh"], cwd=SRC, env=env, capture_output=True, text=True)
        if "PDF fertig" not in r.stdout:
            print(r.stdout[-3000:], r.stderr[-3000:])
            raise SystemExit("Build fehlgeschlagen")
        err = open(os.path.join(SRC, "buch.html"), encoding="utf-8").read().count("katex-error")
        if err:
            raise SystemExit("KaTeX-Fehler: %d" % err)

    def _pages(self):
        d = pymupdf.open(os.path.join(SRC, "..", self.outname))
        pages = {}
        for pno in range(min(len(d), 12)):
            for l in d[pno].get_links():
                nd = l.get("nameddest")
                if nd and "page" in l:
                    pages[nd] = l["page"] + 1
        return pages, len(d)

    def build(self):
        self._make(self.render(None))
        p1, n1 = self._pages()
        self._make(self.render(p1))
        p2, n2 = self._pages()
        if p1 != p2:  # Seitenzahlen haben sich verschoben → noch einmal
            self._make(self.render(p2))
            p3, n2 = self._pages()
            assert p3 == p2, "Seitenzahlen instabil"
        nent = sum(len(s["entries"]) for s in self.secs)
        missing = [eid(e["no"]) for s in self.secs for e in s["entries"] if eid(e["no"]) not in p2]
        print("%s: %d Seiten, %d Abschnitte, %d Einträge, fehlende Linkziele: %s"
              % (self.outname, n2, len(self.secs), nent, missing or "keine"))
