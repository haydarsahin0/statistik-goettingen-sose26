"""Statistik-Komplettkurs (Teil A nach Tag 1) im Klausurformat, Farbwelt lila.
Baut content/skurs.html aus sk1.py, sk2.py, sk3.py. Alle Zahlen werden dort berechnet."""
import os, re
from scipy.stats import norm
from skcommon import C, LOG
from sk_erkl import LERN, VERST, CHECK
from sk_tr import LERN_TR, VERST_TR
import sk1, sk2, sk3  # noqa: F401  (füllen C)

SRC = os.path.dirname(os.path.abspath(__file__))

H = ['<section class="t6">',
     '<div class="fs-kopf"><h1>Statistik-Komplettkurs</h1><div class="sub">Teil A · alles nach Tag 1 – von null bis Klausurniveau</div>',
     '<p>In der Probeklausur 2022 kamen <b>40 der 75 Punkte</b> aus diesem Stoff: Bayes 11 · Mengen 6 · Maximum-Likelihood 10 · Schätzer 5 · Hypothesentest 8. '
     'Jede Karte ist eine echte Klausuraufgabe: erst <b>Aufgabe</b>, dann <b>So löst du es</b>, dann das <b>Lösungskästchen</b> – genau das schreibst du in der Klausur hin.</p></div>',
     '<div class="legend"><b>Prozent</b> = Wahrscheinlichkeit, dass der Aufgabentyp drankommt (aus Probeklausur, Testaten 3–6, Tutorien 4–13): '
     '<span class="ol hi">≥ 70 %</span> fast sicher · <span class="ol mid">30–69 %</span> häufig · <span class="ol lo">&lt; 30 %</span> selten = Kür. '
     '<b>Lernweg:</b> Lösungskästchen abdecken → selbst rechnen → vergleichen → den Fehler in einem Satz notieren. Alle Zahlen sind mit Python/R nachgerechnet.</div>']

LFIG = {"1": ["sk_bedingt.svg"], "2": ["sk_diskstet.svg"], "3": ["sk_baum_vert.svg", "sk_norm2.svg", "sk_zgws.svg"], "4": ["sk_ziel.svg"],
        "5": ["sk_lik.svg"], "6": ["sk_kibau.svg"], "7": ["sk_pwert.svg"], "8": ["sk_baum_test.svg"]}
used = {f for v in LFIG.values() for f in v}
cur = None; ALLCHK = []

def flush_check():
    if cur in CHECK:
        qs = CHECK[cur]
        H.append('<div class="kcheck"><div class="wt">Kurz-Check Abschnitt %s – ohne Nachsehen lösen (Lösungen im Anhang)</div><ol>%s</ol></div>'
                 % (cur, "".join("<li>%s</li>" % q for q, a in qs)))
        ALLCHK.append((cur, qs))

nk = 0
for c in C:
    if c["kind"] == "sec":
        flush_check()
        cur = c["t"].split(" ")[0]
        H.append('<h2 class="rzh">%s</h2>' % c["t"])
        if c["intro"]:
            H.append('<p class="small" style="margin:.2em 0 .5em">%s</p>' % c["intro"])
        if cur in LERN:
            figs = "".join('<div class="lfig"><img src="fig/%s"></div>' % f for f in LFIG.get(cur, []))
            H.append('<div class="lern"><div class="wt">Erklärt von null</div>%s%s</div>' % (LERN[cur], figs))
        if cur in LERN_TR:
            H.append('<div class="tr"><div class="wt">Türkçe açıklama</div>%s</div>' % LERN_TR[cur])
        if c["wissen"]:
            H.append('<div class="wissen"><div class="wt">Das musst du wissen</div><ul>%s</ul></div>'
                     % "".join("<li>%s</li>" % w for w in c["wissen"]))
        continue
    nk += 1
    p = c["p"]; cl = "hi" if p >= 70 else "mid" if p >= 30 else "lo"
    kuer = ' <span class="kuer">Kür – nur wenn Zeit</span>' if p < 30 else ''
    s = ['<div class="rz"><div class="q"><span>%s%s</span><span class="ol %s">~%d %%</span></div><div class="b">' % (c["title"], kuer, cl, p)]
    s.append('<div class="auf"><b>Aufgabe.</b> %s</div>' % c["auf"])
    s.append('<div class="yap" style="grid-column:1/-1"><b class="l">So löst du es</b><ol>%s</ol></div>'
             % "".join("<li>%s</li>" % x for x in c["steps"]))
    loes = re.sub(r'\\t?frac', r'\\dfrac', c["loes"])
    s.append('<div class="lk2" style="grid-column:1/-1">%s</div>' % loes)
    if c["title"] in VERST:
        s.append('<div class="verst"><b>Verstehen:</b> %s</div>' % VERST[c["title"]])
    if c["title"] in VERST_TR:
        s.append('<div class="trk"><b>Türkçe:</b> %s</div>' % VERST_TR[c["title"]])
    if c["warn"]:
        s.append('<div class="dikkat">%s</div>' % c["warn"])
    if c["fig"]:
        f, w = c["fig"]
        s.append('<div class="fig"><img src="fig/%s" style="width:%d%%"></div>' % (f, w))
    s.append('</div></div>')
    H.append("\n".join(s))
flush_check()
H.append('<h2 class="rzh" style="page-break-before:always">Anhang · Lösungen der Kurz-Checks</h2>')
for sc, qs in ALLCHK:
    H.append('<div class="kloes"><b>Abschnitt %s:</b><ol>%s</ol></div>' % (sc, "".join("<li>%s</li>" % a for q, a in qs)))
# Anhang: Φ-Tabelle
rows = ['<tr><th>z</th>' + ''.join('<th>%.2f</th>' % (j / 100) for j in range(10)) + '</tr>']
for i in range(31):
    rows.append('<tr><th>%.1f</th>' % (i / 10) + ''.join('<td>%.4f</td>' % norm.cdf(i / 10 + j / 100) for j in range(10)) + '</tr>')
H.append('<h2 class="rzh" style="page-break-before:always">Anhang · Verteilungsfunktion Φ(z) der Standardnormalverteilung</h2>'
         '<p class="small">Ablesen: Zeile = z bis zur 1. Nachkommastelle, Spalte = 2. Nachkommastelle. Beispiel: Φ(1.64) = Zeile 1.6, Spalte 0.04 = 0.9495. '
         'Negative z: Φ(−z) = 1 − Φ(z). Quantile rückwärts suchen: z₀.₉₅ ≈ 1.645 liegt zwischen 0.9495 und 0.9505.</p>'
         '<table class="tab phi">' + ''.join(rows) + '</table>')
H.append("</section>")
open(os.path.join(SRC, "content", "skurs.html"), "w", encoding="utf-8").write("\n".join(H))
print(nk, "Karten")
for k, v in LOG:
    print("  ", k, "=", v)
