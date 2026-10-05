"""Tag 2 · Zufall & Modelle – Klausurtraining im Spiel-Stil."""
import os, subprocess

SRC = os.path.dirname(os.path.abspath(__file__))
SOL = []                       # Lösungen aller Checks (für den Lösungsteil)
HEAD = ("Statistik · Klausurtraining", "Tag 2 · Zufall &amp; Modelle")
LEVELS = [("lv1", "Level 1"), ("lv2", "Level 2"), ("lv3", "Level 3"), ("lv4", "Level 4"), ("fin", "Finale")]
P = []


def page(body, dark=False, level=None, nxt="Weiter auf der nächsten Seite", pid=None):
    """Seite merken; gerendert wird am Ende, wenn die Gesamtzahl feststeht."""
    P.append(dict(body=body, dark=dark, level=level, nxt=nxt, pid=pid))


def render_pages():
    total = len(P)
    out = []
    for i, d in enumerate(P):
        n = i + 1
        pct = round(100 * n / total)
        tabs = ""
        if not d["dark"] and d["level"]:
            li = [k for k, _ in LEVELS].index(d["level"])
            tabs = '<div class="tabs">' + "".join(
                '<a href="#%s" class="%s"><span>%s</span></a>' % (k, "on" if j == li else ("done" if j < li else ""), t)
                for j, (k, t) in enumerate(LEVELS)) + "</div>"
        nxt = '<a href="#p%d">%s →</a>' % (n + 1, d["nxt"]) if n < total else '<span>%s</span>' % d["nxt"]
        html = ('<section class="pg%s" id="%s">%s<div class="hd"><span>%s</span><span>%s</span><span class="pn">%02d / %d</span></div>'
                '%s<div class="ct">%s</div><div class="ft"><span class="bar"><span class="track"><span class="fill" style="display:block;width:%d%%"></span></span>'
                '<span class="pct">%d %%</span></span>%s</div></section>'
                % (" dark" if d["dark"] else "", d["pid"] or "p%d" % n, '<div class="frame"></div>' if d["dark"] else "",
                   HEAD[0], HEAD[1], n, total, tabs, d["body"].replace("@@TOTAL@@", str(total)), pct, pct, nxt))
        if d["pid"]:
            html = '<a id="p%d"></a>' % n + html
        out.append(html)
    return "\n".join(out)


def kick(sec, label, rel=3, xp=None):
    right = '<span class="xp">%s</span>' % xp if xp else '<span class="rel">Relevanz <b>%s</b></span>' % ("●" * rel + "○" * (3 - rel))
    return '<div class="kick"><span class="sec">%s</span><span class="rule"></span><span>%s</span>%s</div>' % (sec, label, right)


TR = lambda s: '<div class="tr">%s</div>' % s


STMAP = {"§2": (2, 2), "1": (1, 2), "2": (2, 3), "3": (2, 2), "4": (3, 3), "§5": (1, 2), "§6": (1, None), "§7a": (2, 2), "§7b": (3, 3),
         "§8a": (2, 3), "§8b": (2, 2), "§8c": (1, 1), "§9a": (2, 2), "§9b": (3, 3), "§10": (2, 3), "§12": (1, None), "§13a": (2, 4), "§13b": (3, 3),
         "§14": (2, 3), "§15a": (1, 3), "§15b": (2, 3), "§16a": (1, 3), "§16b": (2, 2), "§17": (3, 4), "§18a": (2, 3), "§18b": (2, 2),
         "§19a": (3, 3), "§19b": (1, 1), "§21a": (2, 4), "§21b": (1, 3), "§22": (3, 3)}
STUFE = {1: ("●○○", "leicht"), 2: ("●●○", "mittel"), 3: ("●●●", "Klausur")}


def chk(nr, q, lines=2, sol="", xp="+5 XP", st=2, pts=None):
    """Aufgabe im Probeklausur-Stil: Kopf mit Nummer, Stufe, Punkten; darunter ein Lösungskästchen."""
    if sol:
        SOL.append((str(nr), sol))
    st, pts = STMAP.get(str(nr), (st, pts))
    dots, name = STUFE[st]
    return ('<div class="aufg"><div class="ah"><span class="box"></span><b>Aufgabe %s</b><span class="stf s%d">%s %s</span>'
            '%s<span class="xp">%s</span></div><div class="q">%s</div><div class="lk" style="height:%.1fmm"><span>Lösung</span></div></div>'
            % (nr, st, dots, name, '<span class="pts">(%s P)</span>' % pts if pts else "", xp, q, 7.5 * lines))


def abschluss(nr, lvkey, a4, quiz, nxt, tr):
    """Level-Abschluss: Inhalt fürs handgeschriebene A4-Blatt + Wiederholungs-Quiz aus früheren Leveln."""
    body = kick("✓", "Level %s · Abschluss" % nr, xp="+5 XP Bonus") + \
        '<h1>Level %s <em>gesichert.</em></h1><p class="lead">Bevor du weitergehst: Schreib das Wichtigste auf dein A4-Blatt (das darfst du in die Klausur mitnehmen) und hol drei alte Sachen aus dem Gedächtnis – das verhindert, dass Formeln durcheinandergeraten.</p>' % nr + \
        '<div class="tr">%s</div>' % tr + \
        '<div class="a4"><div class="lab" style="margin-top:0">Auf dein A4-Blatt · mit der Hand abschreiben</div><ul style="margin:0;padding-left:4.5mm;font-size:9.2pt;line-height:1.6">%s</ul></div>' % "".join("<li>%s</li>" % x for x in a4) + \
        '<div class="lab" style="margin-top:3.4mm">Wiederholungs-Quiz · ohne Nachsehen</div>' + "".join(chk(*q[:2], lines=q[2], sol=q[3], st=q[4], pts=None, xp="+3 XP") for q in quiz)
    page(body, level=lvkey, nxt=nxt)


# ---------------------------------------------------------------- 1 Cover
page('''
<div class="lab" style="margin-top:4mm">Statistik und Data Science I &nbsp;——&nbsp; Klausur Teil A + B · Fr 09.10.2026</div>
<div style="margin-top:16mm;display:flex;align-items:flex-end;gap:6mm">
  <div style="border:1px solid #8a6f3e;padding:2mm 6mm 0 4mm"><div class="lab" style="margin:1mm 0 0">Tag</div><div class="bignum">2</div></div>
</div>
<div class="big" style="margin-top:9mm">Zufall &amp; <em>Modelle.</em></div>
<p class="lead" style="max-width:150mm">Heute lernst du alles, was nach der Wahrscheinlichkeitsrechnung kommt: stetige Zufallsvariablen, die sechs Verteilungen, Schätzer und Maximum-Likelihood. Am Abend wartet der Boss: eine Probeklausur mit drei Aufgaben – ohne Formelsammlung.</p>
''' + TR("Bugün olasılıktan sonraki her şeyi öğreniyorsun: sürekli rastgele değişkenler, altı dağılım, tahminciler ve Maximum-Likelihood. Akşam Boss seni bekliyor: üç soruluk bir deneme sınavı – formelsammlung'suz.") + '''
<div class="grid4" style="margin-top:7mm">
 <div class="stat"><div class="n">@@TOTAL@@</div><div class="t">Seiten</div></div>
 <div class="stat"><div class="n">≈ 8</div><div class="t">Stunden</div></div>
 <div class="stat"><div class="n">420</div><div class="t">XP möglich</div></div>
 <div class="stat"><div class="n">3</div><div class="t">Claude-Missionen</div></div>
</div>
<div style="margin-top:8mm;border-top:1px solid #4a3f2d;border-bottom:1px solid #4a3f2d;padding:4mm 0">
 <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:17pt;line-height:1.25">„Eine Dichte ist nur eine Fläche. Wer die Fläche ausrechnen kann, kann die halbe Klausur.“</div>
 <div class="lab" style="margin:2mm 0 0">Ziel bis Freitag · Note 1,x – schlechtestens 2,x</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:2mm"><div class="lab">Dein 5-Tage-Plan</div>
<div class="grid3" style="grid-template-columns:repeat(6,1fr);gap:2mm;font-size:7.6pt;line-height:1.35">
 <div><span class="chip f">✓</span><br><b>Fundament</b><br><span style="color:#a89c86">Tag 1 + Wahrscheinlichkeit · erledigt</span></div>
 <div><span class="chip f">2</span><br><b>Zufall &amp; Modelle</b><br><span style="color:#a89c86">heute · ZV, Verteilungen, Schätzer, ML</span></div>
 <div><span class="chip">3</span><br><b>Schätzen &amp; Testen</b><br><span style="color:#a89c86">morgen · KI, Tests, Regression</span></div>
 <div><span class="chip">4</span><br><b>Generalprobe</b><br><span style="color:#a89c86">Mi · Probeklausur A + B auf Zeit</span></div>
 <div><span class="chip">5</span><br><b>Feinschliff</b><br><span style="color:#a89c86">Do · A4-Blätter, Fehlerliste</span></div>
 <div><span class="chip">★</span><br><b>Klausur</b><br><span style="color:#a89c86">Fr 09.10 · 8:30 Teil A, 12:00 Teil B</span></div>
</div></div>
''', dark=True, nxt="Weiter: So funktioniert das Heft")

# ---------------------------------------------------------------- 2 Briefing
page('''
<div class="kick"><span class="sec">✦</span><span class="rule"></span><span>Briefing · lies das zuerst</span></div>
<h1>Dein Gehirn will <em>Punkte.</em> Gib sie ihm.</h1>
<p class="lead">Dieses Heft ist wie ein Spiel gebaut: Jede Seite bringt XP, jedes Level endet mit einer Belohnung, und am Ende wartet ein Boss – eine echte Klausuraufgabe. Du sammelst Punkte, indem du rechnest, nicht indem du liest.</p>
''' + TR("Bu defter bir oyun gibi: her sayfa XP verir, her level bir ödülle biter, sonda bir Boss var – gerçek bir sınav sorusu. Puanı okuyarak değil, hesaplayarak toplarsın.") + '''
<div class="lab">So liest du dieses Heft</div>
<div class="grid3">
 <div class="card"><b>Check</b> <span class="chip">+5 XP</span><div class="small">Kurze Rechenfrage auf der Seite. Erst rechnen, dann hinten (Lösungsteil) vergleichen.</div></div>
 <div class="card ink"><b>Claude-Mission</b> <span class="chip f">bis +40 XP</span><div class="small" style="color:#b9ae99">Ganze Klausuraufgabe auf Papier → Foto an Claude → Punkte wie in der Klausur + Fehleranalyse.</div></div>
 <div class="card"><b>Klausur-Falle</b><div class="small">Hier verlieren die meisten Punkte – auch du bisher (siehe Fehlerprofil, Level 1).</div></div>
 <div class="card"><b>Vorgemacht</b><div class="small">Eine Aufgabe komplett vorgerechnet, Zeile für Zeile so, wie sie ins Lösungskästchen gehört.</div></div>
 <div class="card"><b>Türkçe</b><div class="small">Unter jedem Block eine kurze türkische Zusammenfassung – nachschlagen, nicht übersetzen.</div></div>
 <div class="card"><b>Relevanz</b><div class="small"><span style="color:var(--gold)">●●●</span> kommt fast sicher · <span style="color:var(--gold)">●●○</span> häufig · <span style="color:var(--gold)">●○○</span> selten</div></div>
</div>
<div class="grid2" style="margin-top:4mm">
 <div>
  <div class="lab">4 Tricks für dein Gehirn</div>
  <ol class="num">
   <li><b>Abrufen statt lesen.</b> Formel zudecken, aus dem Kopf hinschreiben, dann vergleichen.</li>
   <li><b>Laut erklären.</b> Jede Regel einmal in einem deutschen Satz sagen – so wie im Antwortsatz.</li>
   <li><b>50 / 10.</b> 50 Minuten Fokus, Handy in einen anderen Raum, 10 Minuten Pause.</li>
   <li><b>Belohnung erst nach dem Level.</b> Snack, kurzer Spaziergang – erst wenn das Level geschafft ist.</li>
  </ol>
 </div>
 <div>
  <div class="lab">Deine Ränge heute</div>
  <table class="tb"><tr><td>Zufalls-Neuling</td><td style="text-align:right;color:var(--mute)">0–149 XP</td></tr>
  <tr><td>Dichte-Scout</td><td style="text-align:right;color:var(--mute)">150–249 XP</td></tr>
  <tr><td style="border:1px solid var(--gold)"><b>Likelihood-Profi</b></td><td style="text-align:right;border:1px solid var(--gold);color:var(--gold)">250–339 XP · Tagesziel</td></tr>
  <tr><td style="background:var(--dark2);color:#efe8da">Klausur-Maschine</td><td style="text-align:right;background:var(--dark2);color:var(--gold2)">340–420 XP</td></tr></table>
  <div class="lab" style="margin-top:4mm">Dein XP-Zähler</div>
  <div style="display:flex;gap:2mm;flex-wrap:wrap">''' + "".join('<span class="box" style="width:6mm;height:6mm;margin:0"></span>' for _ in range(16)) + '''</div>
  <div class="small" style="margin-top:1mm">Je Kästchen 20 XP – abhaken, sobald du sie hast.</div>
 </div>
</div>
<div class="grid2" style="margin-top:5mm">
 <div class="card gold"><div class="lab" style="margin-top:0">Mein Vertrag mit mir</div>
  <div style="font-size:9.4pt"><b>Heute ziehe ich Level 1–4 und das Finale durch.</b> Formelsammlung nur zum Nachschlagen – erst nach dem eigenen Versuch, nie davor.</div>
  <div style="border-bottom:1px solid #b8b0a0;height:9mm;margin-top:1mm"></div><div class="small">Unterschrift · Startzeit</div></div>
 <div class="card"><div class="lab" style="margin-top:0">Dein Streak</div>
  <div style="display:flex;gap:2.6mm;margin:1mm 0 2mm">''' + "".join(
    '<div style="text-align:center"><div style="width:8mm;height:8mm;border-radius:50%%;border:1.4px solid var(--gold);background:%s;color:%s;'
    'display:flex;align-items:center;justify-content:center;font-size:8pt">%s</div><div class="small" style="font-size:6.4pt">%s</div></div>' % x
    for x in [("var(--gold)", "#fff", "✓", "Tag 1"), ("#fbf8f1", "var(--gold)", "2", "heute"), ("#fbf8f1", "var(--gold)", "3", "Di"),
              ("#fbf8f1", "var(--gold)", "4", "Mi"), ("#fbf8f1", "var(--gold)", "5", "Do"), ("var(--dark2)", "var(--gold2)", "★", "Fr")]) + '''</div>
  <div style="font-size:8.8pt">Tag 1 ist geschafft. Lass die Kette heute nicht reißen.</div></div>
</div>
''' + TR("Sözleşmen: bugün Level 1–4 ve Finale'yi bitiriyorsun. Formelsammlung'a sadece kendi denemenden sonra bak. Tag 1 tamam – zinciri bugün koparma."), nxt="Weiter: Deine Route")

# ---------------------------------------------------------------- 3 Quest-Map
def node(t, s, gold=False):
    return ('<div style="text-align:center;width:18.6mm;position:relative;z-index:1"><div style="width:9mm;height:9mm;border-radius:50%%;margin:0 auto;border:1.4px solid var(--gold);'
            'background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-family:Cormorant Garamond,serif;font-size:11pt">%s</div>'
            '<div style="font-size:6.6pt;line-height:1.2;margin-top:1.2mm">%s</div></div>') % ("var(--gold)" if gold else "#fbf8f1", "#fff" if gold else "var(--gold)", t, s)


def route(lv, title, meta, nodes):
    w = (len(nodes) - 1) * 19.6
    return ('<div style="margin:4.6mm 0"><div style="display:flex;justify-content:space-between" class="lab"><span>%s · %s</span><span style="color:var(--mute)">%s</span></div>'
            '<div style="display:flex;align-items:flex-start;gap:1mm;position:relative;padding-top:1mm">'
            '<div style="position:absolute;left:12.5mm;width:%dmm;top:5.6mm;border-top:1.4px dashed var(--gold2)"></div>%s</div></div>') % (lv, title, meta, w, "".join(node(*n) for n in nodes))


page('''
<div class="kick"><span class="sec">✦</span><span class="rule"></span><span>Quest-Map</span></div>
<h1>Deine <em>Route</em> für heute.</h1>
<div class="grid4" style="margin:3mm 0 1mm">
 <div class="card"><div class="stat" style="border:0;padding:0"><div class="n">≈ 8:00</div><div class="t">Std. Lernzeit</div></div></div>
 <div class="card"><div class="stat" style="border:0;padding:0"><div class="n">5</div><div class="t">Pausen à 10 min</div></div></div>
 <div class="card"><div class="stat" style="border:0;padding:0"><div class="n">420</div><div class="t">XP möglich</div></div></div>
 <div class="card ink"><div class="stat" style="border:0;padding:0"><div class="n" style="color:#f3ead6">300</div><div class="t">XP Tagesziel</div></div></div>
</div>
''' + TR("Bu bugünkü haritan. Her durağı bitirince dairenin içini kalemle doldur. Altın daireler = Claude görevleri: kendin yaz, fotoğrafını çek, bana gönder.") +
route("Level 1", "Fehler-Detox", "40 min · 40 XP", [("§1", "Dein Fehlerprofil"), ("§2", "3 Retter-Regeln"), ("§3", "10-Sekunden-Kontrolle")]) +
route("Level 2", "Zufallsvariablen", "130 min · 100 XP", [("§4", "diskret: Wiederholung"), ("§5", "Dichte = Fläche"), ("§6", "Integral"), ("§7", "c bestimmen"), ("§8", "F(x), Median"), ("§9", "E(X), Var"), ("§10", "Rechenregeln"), ("§11", "zwei ZV, Cov"), ("M1", "Mission 1", True)]) +
route("Level 3", "Die Verteilungen", "100 min · 80 XP", [("§12", "Welche Verteilung?"), ("§13", "Binomial"), ("§14", "Poisson"), ("§15", "Gleich + Exponential"), ("§16", "Normal"), ("§17", "Summen + ZGWS")]) +
route("Level 4", "Schätzer &amp; Maximum-Likelihood", "140 min · 120 XP", [("§18", "Erwartungstreu?"), ("§19", "Varianz, MSE"), ("§20", "KDE, Gütekriterien"), ("§21", "ML-Rezept"), ("§22", "ML-Klassiker"), ("§23", "ML-Spezial"), ("M2", "Mission 2", True)]) +
route("Finale", "Training &amp; Boss", "70 min · 80 XP", [("§24", "Mini-Fälle"), ("★", "Boss-Probeklausur", True), ("✓", "Tagesabschluss")]) + '''
<div class="tip" style="margin-top:4mm"><b>Pausen</b>Nach jedem Level 10 Minuten Pause + 5 XP Level-Bonus. Erst abhaken, dann aufstehen.</div>
''', level="lv1", nxt="Los geht's: Level 1")

# ---------------------------------------------------------------- 4 Level 1 Start
page('''
<div class="lab" style="margin-top:6mm">Level</div>
<div class="lvbox"><div class="bignum">1</div></div>
<div class="big">Fehler-<em>Detox</em></div>
<p class="lead" style="max-width:150mm;color:#e2d9c6">Bevor du Neues lernst, räumst du auf. Ich habe alle deine Fragen und alle korrigierten Lösungen der letzten Tage ausgewertet. Es sind immer dieselben sieben Fehler – und drei davon kosten dich allein 10 Punkte.</p>
''' + TR("Yeni bir şey öğrenmeden önce temizlik. Son günlerdeki tüm sorularını ve düzeltilmiş çözümlerini inceledim. Hep aynı yedi hata – üçü tek başına 10 puan götürüyor.") + '''
<div style="margin:4mm 0"><span class="chip">3 Stationen</span><span class="chip">45 min</span><span class="chip f">40 XP</span></div>
<div class="lab" style="margin-top:6mm">Du schaltest frei</div>
<ul class="dia">
 <li><b>Dein Fehlerprofil</b><span class="d">· 7 Muster aus Fragen, Übungen und Probeklausur 2</span><span class="r">§ 1</span></li>
 <li><b>3 Retter-Regeln</b><span class="d">· Strich = ablesen · 1 − p · stetig = Fläche</span><span class="r">§ 2</span></li>
 <li><b>10-Sekunden-Kontrolle</b><span class="d">· nach jedem Kästchen + Drill</span><span class="r">§ 3</span></li>
</ul>
<div style="position:absolute;left:0;right:0;bottom:2mm">
 <div class="reward" style="position:static"><span style="font-size:15pt">☕</span><div><div class="lab">Belohnung</div>Nach Level 1: 10 Minuten Pause und +5 XP Level-Bonus.</div><span class="box" style="margin-left:auto;width:4.5mm;height:4.5mm"></span></div>
</div>
''', dark=True, pid="lv1", nxt="Level 1 · Start")

# ---------------------------------------------------------------- 5 §1 Fehlerprofil 1/2
cats = [("Formel verwechselt / nicht abrufbar", 5.5, "A3c Regression, A6d Binomial"),
        ("Teilaufgabe vergessen", 4.0, "A2c Mittelwert, A3d Prognose, A5e"),
        ("Stetig wie diskret gerechnet", 3.5, "A6a Integral, A6b E(X) als Summe"),
        ("Rechnen / Abschreiben", 3.5, "114 → 119, Ā ∪ B, 0.5 · 0.4"),
        ("Bedingt mit Schnitt verwechselt", 2.0, "A5a: 0.8 · 0.05 statt 0.05"),
        ("Grenzen, Runden, Form", 2.0, "x ≤ 2 statt x &lt; 2, 4.91, 13,5")]
bars = "".join(
    '<div style="display:grid;grid-template-columns:62mm 1fr 12mm;align-items:center;gap:2.4mm;margin:.5mm 0;font-size:8.4pt;line-height:1.3">'
    '<span>%s<br><span class="small" style="font-size:7.4pt">%s</span></span>'
    '<span style="height:4mm;background:#e3ded3;border-radius:1mm;position:relative;display:block"><span style="position:absolute;left:0;top:0;bottom:0;width:%d%%;background:%s;border-radius:1mm;display:block"></span></span>'
    '<span style="text-align:right;font-family:Cormorant Garamond,serif;font-size:13pt;color:var(--red)">−%s</span></div>'
    % (t, w, int(p / 5.5 * 100), "var(--red)" if p >= 3.5 else "var(--gold)", ("%g" % p).replace(".", ",")) for t, p, w in cats)
page(kick("§ 1", "Dein Fehlerprofil · Teil 1/2") + '''
<h1>Wo deine <em>Punkte</em> hingehen.</h1>
<p class="lead">Ausgewertet: 4 korrigierte Lösungen (Venn, Fitness, Glücksrad, Probeklausur 2) und über 25 Fragen, die du mir gestellt hast. Das Ergebnis ist eine gute Nachricht: Dir fehlt kaum Wissen – dir fehlen Routinen.</p>
''' + TR("4 düzeltilmiş çözüm ve bana sorduğun 25'ten fazla soru incelendi. İyi haber: bilgin eksik değil, rutinlerin eksik.") + '''
<div class="grid3" style="margin:3mm 0">
 <div class="card"><div class="stat" style="border:0;padding:0"><div class="n">31,5<span style="font-size:13pt;color:var(--mute)"> / 52</span></div><div class="t">Probeklausur 2 · A1–A6</div></div></div>
 <div class="card gold"><div class="stat" style="border:0;padding:0"><div class="n" style="color:var(--red)">20,5</div><div class="t">Punkte verloren</div></div></div>
 <div class="card ink"><div class="stat" style="border:0;padding:0"><div class="n" style="color:var(--gold2)">≈ 13</div><div class="t">davon ohne neues Wissen rettbar</div></div></div>
</div>
<div class="lab">Verlorene Punkte nach Fehlerart · Probeklausur 2</div>
''' + bars + '''
<div class="card note" style="margin-top:2mm;padding:2mm 3mm;font-size:9.4pt"><b>Das heißt für dich:</b> Teilaufgaben vergessen, Abschreib- und Formfehler (zusammen <b>9,5 P</b>) kosten dich mehr als jede Wissenslücke. Die Formel-Verwechslungen (<b>5,5 P</b>) löst du mit Abruf-Training – genau das macht dieses Heft.</div>
''' + TR("Unutulan alt sorular, kopyalama ve biçim hataları (toplam 9,5 puan) herhangi bir bilgi eksiğinden daha pahalı. Formül karıştırmayı (5,5 puan) hatırlama alıştırmasıyla çözeceğiz.") + '''
<div class="lab" style="margin-top:3mm">Deine Fragen der letzten Tage – was sie verraten</div>
<table class="tb"><tr><th>Thema</th><th>Deine Fragen (Auswahl)</th><th>Diagnose</th></tr>
<tr><td><b>Bedingte W'keit</b> <span class="small">· 4×</span></td><td>„Wie finden wir P(B|A)?“ · „P(A|B̄) verstehe ich nicht“ · Bayes Teil 2 „schaffe ich nicht“</td><td style="color:var(--red)">Kernlücke → Regel 1</td></tr>
<tr><td><b>Zufallsvariablen</b> <span class="small">· 4×</span></td><td>„Was ist Träger?“ · „Warum 0 sonst?“ · „E(X) verstehe ich nicht“ · „Woher kommt 18/7?“</td><td style="color:var(--red)">Begriffe neu → Level 2</td></tr>
<tr><td><b>Gegenereignis</b> <span class="small">· 2×</span></td><td>„Woher kommt 0.98?“ · Bayes mit \\(\\bar V\\)</td><td style="color:var(--gold)">Routine → Regel 2</td></tr>
<tr><td><b>Rechnen</b> <span class="small">· 1×</span></td><td>„E(log X) ist falsch – ich bekomme 0.2455“ (log₁₀ statt ln)</td><td style="color:var(--gold)">Taschenrechner → § 3</td></tr>
<tr><td><b>R-Grundlagen</b> <span class="small">· 6×</span></td><td>na.omit · read.csv/setwd · typeof vs. class · mean/sd/var · tapply · addmargins</td><td style="color:var(--green)">geklärt ✓</td></tr></table>
''' + TR("Soruların iki merkezi boşluğu gösteriyor: koşullu olasılık ve rastgele değişken kavramları. İkisi de bugün kapanıyor. R soruların tamamen çözüldü."),
     level="lv1", nxt="Weiter: Die 7 Muster")

# ---------------------------------------------------------------- 6 §1 Fehlerprofil 2/2
rows = [("1", "Gegenereignis vergessen", "Venn: Außenbereich 0.4 fehlte · „0.98 – woher?“ · Glücksrad: die 7 außen · \\(\\bar A\\cup B\\): B-Elemente vergessen · Bayes Teil 2 mit \\(\\bar V\\)", "§ 2 Regel 2"),
        ("2", "Bedingt ≠ Schnitt", "Fragen „Wie finde ich P(B|A)?“, „P(A|B̄) verstehe ich nicht“ · PK2 A5a: \\(P(C\\mid\\text{pünktl.})=0.8\\cdot0.05\\) statt 0.05", "§ 2 Regel 1"),
        ("3", "Stetig wie diskret", "Fragen zu Träger, „0 sonst“, E(X), „18/7 woher?“ · PK2 A6b: E(X) als Summe 0·¼ + 1·¼ + 2·¼", "Level 2"),
        ("4", "Formel nicht abrufbar", "PK2 A3c: Transformationsregel statt \\(b=s_{xy}/s_x^2\\) · A6d: \\(1-(1-\\pi)^n\\) statt \\(P(4)+P(5)\\)", "§ 3 + Abruf-Checks"),
        ("5", "Flüchtigkeit", "Fitness: 0.6 · 0.25 = 0.125 (richtig 0.15) · 114 → 119 · 0.5 · 0.4 = 0.25 · log₁₀ statt ln", "§ 3 Kontrolle"),
        ("6", "Teil/Satz vergessen", "Fitness (e) ohne Entscheidungssatz · PK2 A2c, A3d, A5e leer", "§ 3 Kontrolle"),
        ("7", "Form", "13,5 statt 13.5 · 4.91 statt 4.909 · Notation: erst Menge, dann P", "§ 3 Kontrolle")]
page(kick("§ 1", "Dein Fehlerprofil · Teil 2/2") + '''
<h1>Die sieben <em>Muster.</em></h1>
<p class="lead">Jede Zeile ist ein Fehler, den du mindestens zweimal gemacht hast – mit Beleg und dem Gegenmittel in diesem Heft.</p>
''' + TR("Her satır en az iki kez yaptığın bir hata: nerede olduğu ve bu defterdeki çaresi.") + '''
<table class="tb" style="margin-top:2mm"><tr><th>#</th><th>Muster</th><th>Wo es passiert ist</th><th>Gegenmittel</th></tr>''' +
"".join('<tr><td class="k">%s</td><td style="width:30mm"><b>%s</b></td><td>%s</td><td style="width:24mm;color:var(--gold)">%s</td></tr>' % r for r in rows) + '''</table>
<div class="grid2" style="margin-top:4mm">
 <div class="card"><div class="lab" style="margin-top:0;color:var(--green)">Das sitzt schon</div>
  <div style="font-size:8.8pt">Lage- und Streuungsmaße (A1: 8,5/9) · Verteilungsfunktion zeichnen · totale Wahrscheinlichkeit und Bayes (A5b–d voll) · Kausalität begründen · Skalenniveaus · R-Grundlagen (tapply, addmargins, typeof)</div></div>
 <div class="card ink"><div class="lab" style="margin-top:0">Deine Regel ab heute</div>
  <div style="font-size:9pt">Nach jedem Kästchen 10 Sekunden: <b>Alles beantwortet? Zahl plausibel? Abgeschrieben richtig? Form?</b></div></div>
</div>
''' + TR("Zaten oturmuş olanlar: konum ve dağılım ölçüleri, dağılım fonksiyonu çizimi, toplam olasılık ve Bayes, nedensellik, ölçek düzeyleri, R temelleri. Bugünden itibaren kuralın: her kutudan sonra 10 saniye kontrol.") + '''
<div class="lab" style="margin-top:3mm">Probeklausur 2 neu gerechnet – nur mit Routinen, ohne neues Wissen</div>
<div style="display:grid;grid-template-columns:22mm 1fr 18mm;gap:2.4mm;align-items:center;font-size:8.8pt">
 <span>vorher</span><span style="height:5mm;background:#e3ded3;border-radius:1mm;display:block;position:relative"><span style="position:absolute;left:0;top:0;bottom:0;width:60.6%;background:var(--gold);border-radius:1mm;display:block"></span></span><span style="font-family:Cormorant Garamond,serif;font-size:14pt">31,5</span>
 <span><b>nachher</b></span><span style="height:5mm;background:#e3ded3;border-radius:1mm;display:block;position:relative"><span style="position:absolute;left:0;top:0;bottom:0;width:85.6%;background:var(--green);border-radius:1mm;display:block"></span></span><span style="font-family:Cormorant Garamond,serif;font-size:14pt;color:var(--green)">44,5</span>
</div>
<div class="small" style="margin-top:1.4mm">+4 Teilaufgaben nicht vergessen · +3,5 sauber rechnen/abschreiben · +2 Form · +2 Regel 1 · +1,5 Regel 3 (Integral) = <b>+13 Punkte</b> – das entspricht etwa einer ganzen Notenstufe.</div>
''' + TR("Sadece rutinlerle (yeni bilgi olmadan) Probeklausur 2'den 44,5/52 alırdın: +13 puan, yaklaşık bir tam not basamağı."),
     level="lv1", nxt="Weiter: 3 Retter-Regeln")

# ---------------------------------------------------------------- 7 §2 Drei Regeln
tree = '''<svg viewBox="0 0 262 124" style="width:100%;height:auto">
<g stroke="#a8803a" stroke-width="1.2" fill="none"><path d="M18 60 L110 25"/><path d="M18 60 L110 95"/><path d="M135 25 L225 10"/><path d="M135 25 L225 40"/><path d="M135 95 L225 80"/><path d="M135 95 L225 110"/></g>
<g font-size="11" fill="#1d1b17"><text x="112" y="28">P</text><text x="112" y="98">V</text><text x="228" y="13">C</text><text x="228" y="43">A, B</text><text x="228" y="83">C</text><text x="228" y="113">A, B</text></g>
<g font-size="10" fill="#6b665c"><text x="52" y="33">0.8</text><text x="52" y="92">0.2</text><text x="160" y="12">0.05</text><text x="160" y="84">0.3</text></g>
<rect x="156" y="2" width="29" height="14" rx="2" fill="none" stroke="#a33a2a" stroke-width="1.2"/>
<text x="150" y="58" font-size="9.5" fill="#a33a2a">0.05 = P(C | P) → ablesen</text></svg>'''
page(kick("§ 2", "3 Retter-Regeln", rel=3) + '''
<h1>Drei Regeln, die dir <em>10 Punkte</em> retten.</h1>
<div class="grid2" style="grid-template-columns:1.05fr 1fr;align-items:start">
 <div>
  <h2><span style="color:var(--gold)">1</span> &nbsp;Strich heißt ablesen.</h2>
  <p style="margin:0">Steht in der Aufgabe <b>„von den pünktlichen … 5 %“</b>, ist das schon \\(P(C\\mid P)=0.05\\) – die Zahl am Ast. <b>Multipliziert</b> wird nur für den <b>Schnitt</b> (einen ganzen Pfad).</p>
  <div class="fm">\\(P(C\\mid P)=0.05\\qquad P(C\\cap P)=0.8\\cdot0.05=0.04\\)</div>
 </div>
 <div class="card" style="padding:2mm 3mm">''' + tree + '''</div>
</div>
''' + TR("„|“ işareti varsa: dalın üstündeki sayıyı oku, çarpma. Çarpma sadece kesişim (∩) için, yani bütün bir yol için.") + '''
<h2><span style="color:var(--gold)">2</span> &nbsp;Immer an 1 − p denken.</h2>
<table class="tb"><tr><th>Gegeben</th><th>Mitgedacht werden muss</th><th>Wo du es vergessen hast</th></tr>
<tr><td>Prävalenz 2 %</td><td>gesund: \\(1-0.02=0.98\\)</td><td>„0.98 – woher?“</td></tr>
<tr><td>Verspätung 10 %</td><td>pünktlich: \\(P(\\bar V\\mid A)=0.9\\)</td><td>Bayes Teil 2</td></tr>
<tr><td>Venn mit \\(P(A\\cup B)=0.6\\)</td><td>außen: \\(1-0.6=0.4\\)</td><td>Venn-Übung</td></tr>
<tr><td>\\(A\\), Ω = {1,…,10}</td><td>\\(\\bar A\\) komplett ausschreiben, dann \\(\\cup B\\)</td><td>PK2 A4a</td></tr></table>
''' + TR("Bir oran verildiyse tümleyenini (1 − p) hemen yanına yaz: hasta → sağlıklı, gecikme → zamanında, Venn içi → dışı.") + '''
<h2><span style="color:var(--gold)">3</span> &nbsp;Stetig heißt Fläche – also Integral.</h2>
<div class="grid2" style="align-items:center">
 <div class="fm" style="text-align:left">diskret: \\(E(X)=\\sum x\\,P(X=x)\\)<br>stetig: \\(E(X)=\\int x\\,f(x)\\,dx\\)</div>
 <div class="falle" style="margin:0"><b>Deine Falle (PK2 A6b)</b>\\(0\\cdot\\tfrac14+1\\cdot\\tfrac14+2\\cdot\\tfrac14\\) – bei einer Dichte gibt es keine Einzelwahrscheinlichkeiten.</div>
</div>
''' + TR("Yoğunluk f(x) verildiyse toplam yok, integral var. „Dichte“ kelimesini görünce ∫ yaz.") + '''
<div class="card gold" style="margin-top:2mm"><div class="lab" style="margin-top:0">Vorgemacht · alle drei Regeln in einer Aufgabe</div>
<div style="font-size:9.2pt">„10 % aller Kunden sind Neukunden (N). Von den Neukunden reklamieren 30 %, von den Stammkunden 5 %. Mit welcher Wahrscheinlichkeit ist ein reklamierender Kunde (R) ein Stammkunde?“</div>
<div class="fm">\\(\\underbrace{P(R\\mid N)=0.3,\\ P(R\\mid\\bar N)=0.05}_{\\text{Regel 1: ablesen}}\\quad \\underbrace{P(\\bar N)=1-0.1=0.9}_{\\text{Regel 2}}\\quad P(\\bar N\\mid R)=\\frac{0.05\\cdot0.9}{0.3\\cdot0.1+0.05\\cdot0.9}=\\frac{0.045}{0.075}=0.6\\)</div></div>
''' + chk("§2", "Gleiche Situation: Mit welcher Wahrscheinlichkeit reklamiert ein Neukunde <b>nicht</b>? Und wie groß ist \\(P(N\\cap\\bar R)\\)?", 1, sol="\\(P(\\bar R\\mid N)=1-0.3=0.7\\) (Regel 2: Gegenereignis) · \\(P(N\\cap\\bar R)=0.1\\cdot0.7=0.07\\) (ganzer Pfad → multiplizieren)"),
     level="lv1", nxt="Weiter: 10-Sekunden-Kontrolle")

# ---------------------------------------------------------------- 8 §3 Kontrolle + Drill
page(kick("§ 3", "10-Sekunden-Kontrolle · Drill", xp="4 × 5 XP") + '''
<h1>Zehn Sekunden pro <em>Kästchen.</em></h1>
<div class="grid4" style="margin:2mm 0 1mm">
 <div class="card"><b style="color:var(--gold)">1 · Alles?</b><div class="small">Jede Teilfrage, jedes „Begründen“, jeder Antwortsatz.</div></div>
 <div class="card"><b style="color:var(--gold)">2 · Plausibel?</b><div class="small">0 ≤ P ≤ 1 · Var ≥ 0 · |r| ≤ 1 · Summe = 1</div></div>
 <div class="card"><b style="color:var(--gold)">3 · Abgeschrieben?</b><div class="small">Zahl im Kästchen = Zahl aus der Nebenrechnung?</div></div>
 <div class="card"><b style="color:var(--gold)">4 · Form?</b><div class="small">Punkt statt Komma · 3 Stellen · ln statt log₁₀</div></div>
</div>
''' + TR("Her kutudan sonra 4 soru: hepsi cevaplandı mı? sayı mantıklı mı? doğru kopyalandı mı? biçim doğru mu? Şimdi tam senin hata kalıplarına göre 4 kısa soru.") + '''
<div class="lab">Drill · jede Frage zielt auf eines deiner Muster</div>
''' + chk(1, "Muster 2. Baum: \\(P(K)=0.1\\), \\(P(T\\mid K)=0.9\\), \\(P(T\\mid\\bar K)=0.2\\). Geben Sie \\(P(T\\mid\\bar K)\\) und \\(P(T\\cap\\bar K)\\) an.", 2, sol="\\(P(T\\mid\\bar K)=0.2\\) – nur ablesen · \\(P(T\\cap\\bar K)=P(\\bar K)\\cdot P(T\\mid\\bar K)=0.9\\cdot0.2=0.18\\)")
     + chk(2, "Muster 1 + 5. Ω = {1,…,6} (Laplace), A = {1, 2}, B = {2, 4, 6}. Bestimmen Sie \\(|\\bar A\\cup B|\\). Sind A und B unabhängig? Rechnerisch begründen.", 3, sol="\\(\\bar A=\\{3,4,5,6\\}\\), \\(\\bar A\\cup B=\\{2,3,4,5,6\\}\\Rightarrow|\\bar A\\cup B|=5\\) · \\(P(A\\cap B)=P(\\{2\\})=\\frac16\\), \\(P(A)P(B)=\\frac26\\cdot\\frac36=\\frac16\\) → unabhängig")
     + chk(3, "Muster 3. \\(f(x)=c\\) für \\(0\\le x\\le4\\), 0 sonst. Bestimmen Sie c und \\(P(X\\le1)\\).", 2, sol="\\(\\int_0^4c\\,dx=4c=1\\Rightarrow c=\\frac14\\) · \\(P(X\\le1)=\\int_0^1\\frac14dx=\\frac14\\)")
     + chk(4, "Muster 4 – Abruf ohne Nachsehen. Regressionsgerade: \\(b=\\ ?\\quad a=\\ ?\\) &nbsp;·&nbsp; Binomial: \\(P(Y\\ge4)\\) bei \\(n=5\\) als Summe = ?", 2, sol="\\(b=\\frac{s_{xy}}{s_x^2}\\), \\(a=\\bar y-b\\,\\bar x\\) · \\(P(Y\\ge4)=P(Y=4)+P(Y=5)=\\binom54\\pi^4(1-\\pi)+\\pi^5\\)") + '''
<div class="small" style="margin-top:1mm">Lösungen: Lösungsteil am Ende des Heftes. Alle vier richtig? Dann trag 20 XP ein und gönn dir die Level-Pause.</div>
''', level="lv1", nxt="Weiter: Level-1-Abschluss")

abschluss("1", "lv1",
    [r"Strich heißt ablesen: \(P(C\mid P)\) steht am Ast · multipliziert wird nur für den Schnitt \(P(C\cap P)=P(P)\,P(C\mid P)\)",
     r"Immer \(1-p\) mitdenken: Prävalenz → gesund, Verspätung → pünktlich, Venn innen → außen",
     r"Stetig = Fläche = Integral: \(E(X)=\int x f(x)\,dx\), nie \(\sum\) bei einer Dichte",
     r"Bayes: \(P(A_j\mid B)=\frac{P(B\mid A_j)P(A_j)}{\sum_i P(B\mid A_i)P(A_i)}\) · unabhängig \(\iff P(A\cap B)=P(A)P(B)\)",
     r"10-Sekunden-Kontrolle: alles beantwortet? plausibel? richtig abgeschrieben? Punkt, 3 Stellen, ln?"],
    [("W1", r"Tag 1: Bestimmen Sie den Median der Daten 7, 2, 9, 4, 3.", 1, r"sortiert 2, 3, 4, 7, 9 → \(x_{med}=4\)", 1),
     ("W2", r"\(P(A)=0.4,\ P(B)=0.5,\ P(A\cap B)=0.1\). Bestimmen Sie \(P(A\cup B)\) und \(P(A\mid B)\).", 1, r"\(0.4+0.5-0.1=0.8\) · \(\frac{0.1}{0.5}=0.2\)", 1),
     ("W3", r"Tag 1: Empirische Varianz \(s^2\) von 1, 2, 3, 4, 5?", 1, r"\(\bar x=3\), \(s^2=\frac{4+1+0+1+4}{5}=2\)", 2)],
    "Level 1 geschafft · Pause!", "A4 kâğıdına el yazınla geçir: sınava götürebileceğin tek yardımcı bu. Sonra üç eski soruyu bakmadan çöz – formüller karışmasın diye.")

# ---------------------------------------------------------------- 9 Level 2 Start
page('''
<div class="lab" style="margin-top:6mm">Level</div>
<div class="lvbox"><div class="bignum">2</div></div>
<div class="big">Stetige <em>Zufallsvariablen</em></div>
<p class="lead" style="max-width:150mm;color:#e2d9c6">Bei Wartezeiten, Gewichten oder Anteilen gibt es keine Liste von Werten mehr, sondern eine Kurve. Die Wahrscheinlichkeit ist die Fläche unter dieser Kurve. Mehr Idee steckt nicht dahinter – der Rest ist Integrieren nach Rezept.</p>
''' + TR("Bekleme süresi, ağırlık veya oran gibi değişkenlerde değer listesi yok, bir eğri var. Olasılık = eğrinin altındaki alan. Fikir bu kadar; gerisi tarifle integral almak.") + '''
<div style="margin:4mm 0"><span class="chip">8 Stationen + Mission</span><span class="chip">130 min</span><span class="chip f">100 XP</span></div>
<div class="lab" style="margin-top:5mm">Du schaltest frei</div>
<ul class="dia" style="font-size:9.4pt">
 <li><b>Diskret: Wiederholung</b><span class="d">· Träger, Treppe, E und Var als Summe – der leichte Einstieg</span><span class="r">§ 4</span></li>
 <li><b>Dichte = Fläche</b><span class="d">· diskret vs. stetig, die 3 Eigenschaften</span><span class="r">§ 5</span></li>
 <li><b>Integral-Crashkurs</b><span class="d">· Potenzregel, Grenzen einsetzen, 6er-Drill</span><span class="r">§ 6</span></li>
 <li><b>c bestimmen</b><span class="d">· Fläche = 1, auch stückweise</span><span class="r">§ 7</span></li>
 <li><b>F(x), Median, Quantile</b><span class="d">· Fläche bis x</span><span class="r">§ 8</span></li>
 <li><b>E(X) und Var(X) per Integral</b><span class="d">· Testat-4-Typ, PK2 A6</span><span class="r">§ 9</span></li>
 <li><b>Rechenregeln</b><span class="d">· \\(E(aX+b)\\), Summen, Unabhängigkeit</span><span class="r">§ 10</span></li>
 <li><b>Zwei Zufallsvariablen</b><span class="d">· gemeinsame Tabelle, Rand, bedingt, Kovarianz</span><span class="r">§ 11</span></li>
 <li><b>Mission 1</b><span class="d">· Testat-4-Aufgabe auf Papier → Foto an Claude</span><span class="r">30 XP</span></li>
</ul>
<div style="position:absolute;left:0;right:0;bottom:2mm">
 <div class="reward" style="position:static"><span style="font-size:15pt">☕</span><div><div class="lab">Belohnung</div>Nach Level 2: 10 Minuten Pause, etwas essen, +5 XP Level-Bonus.</div><span class="box" style="margin-left:auto;width:4.5mm;height:4.5mm"></span></div>
</div>
''', dark=True, pid="lv2", nxt="Level 2 · Start")

page(kick("§ 4", "Diskret: Wiederholung", rel=3) + r"""
<h1>Erst die Liste, dann die <em>Kurve.</em></h1>
<p class="lead">Bevor die Dichten kommen, holst du den diskreten Fall zurück – er ist der leichte Einstieg und kommt in Testat-Aufgaben genauso dran. Vier Begriffe: Träger, Wahrscheinlichkeitsfunktion, Verteilungsfunktion, Erwartungswert.</p>
""" + TR("Yoğunluklardan önce kesikli durumu hatırla: kolay giriş ve Testat'ta aynen çıkıyor. Dört kavram: Träger, olasılık fonksiyonu, dağılım fonksiyonu, beklenen değer.") + r"""
<table class="tb"><tr><th>Begriff</th><th>Was ist das?</th><th>Rechnung</th></tr>
<tr><td><b>Träger</b> T</td><td>alle Werte, die X annehmen kann</td><td>Liste, z. B. \(\{0,1,2\}\)</td></tr>
<tr><td><b>Wahrscheinlichkeitsfunktion</b></td><td>jeder Wert mit seiner Wahrscheinlichkeit, <b>„0 sonst“</b></td><td>\(\sum P(X=x)=1\)</td></tr>
<tr><td><b>Verteilungsfunktion</b> F</td><td>Treppe: Wahrscheinlichkeiten von links aufsummiert</td><td>\(F(x)=P(X\le x)\), Sprunghöhe = \(P(X=x)\)</td></tr>
<tr><td><b>Erwartungswert, Varianz</b></td><td>Wert × Wahrscheinlichkeit, aufsummiert</td><td>\(E(X)=\sum x\,P(X=x)\), \(Var=E(X^2)-E(X)^2\)</td></tr></table>
""" + '<div class="card gold" style="margin-top:2mm"><div class="lab" style="margin-top:0">Vorgemacht · Konstante c, E und Var</div>' + r"""
<div style="font-size:9.2pt">\(P(X=x)=c\,(x+1)\) für \(x\in\{0,1,2\}\), 0 sonst.</div>
<div class="fm">\(c(1+2+3)=6c=1\Rightarrow c=\frac16\quad E(X)=0\cdot\frac16+1\cdot\frac26+2\cdot\frac36=\frac43\quad E(X^2)=\frac{0+2+12}6=\frac73\quad Var(X)=\frac73-\frac{16}9=\frac59=0.556\)</div></div>
""" + chk("§4a", r"Eine faire Münze wird zweimal geworfen, X = Anzahl Kopf. Geben Sie Träger und Wahrscheinlichkeitsfunktion an und berechnen Sie \(E(X)\).", 2,
          sol=r"\(T=\{0,1,2\}\); \(P(X=0)=\frac14,\ P(X=1)=\frac12,\ P(X=2)=\frac14\), 0 sonst · \(E(X)=0+\frac12+\frac24=1\)", st=1, pts=3)
    + chk("§4b", r"\(P(X=1)=0.2,\ P(X=2)=0.5,\ P(X=4)=0.3\). Stellen Sie F(x) auf und bestimmen Sie \(P(X\le3)\), \(P(X&lt;2)\) und \(E(X)\).", 3,
          sol=r"\(F=0\ (x<1);\ 0.2\ (1\le x<2);\ 0.7\ (2\le x<4);\ 1\ (x\ge4)\) · \(P(X\le3)=0.7\) · \(P(X<2)=0.2\) · \(E(X)=0.2+1+1.2=2.4\)", st=2, pts=4),
    level="lv2", nxt="Weiter: Jetzt stetig – Dichte = Fläche")

# ---------------------------------------------------------------- 10 §5 Dichte = Fläche
dens = '''<svg viewBox="0 0 260 150" style="width:100%;height:auto">
<line x1="30" y1="125" x2="245" y2="125" stroke="#1d1b17" stroke-width="1"/><line x1="30" y1="125" x2="30" y2="10" stroke="#1d1b17" stroke-width="1"/>
<polygon points="30,125 115,125 115,72.5" fill="#f1dfb8" stroke="none"/>
<line x1="30" y1="125" x2="200" y2="20" stroke="#a8803a" stroke-width="2"/>
<line x1="200" y1="20" x2="200" y2="125" stroke="#a8803a" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="200" y1="125" x2="240" y2="125" stroke="#a8803a" stroke-width="2"/>
<g font-size="11" fill="#1d1b17"><text x="26" y="137">0</text><text x="111" y="137">1</text><text x="196" y="137">2</text><text x="236" y="138">x</text>
<text x="8" y="23">1</text><text x="2" y="76">0.5</text><text x="38" y="14">f(x)</text></g>
<line x1="27" y1="20" x2="33" y2="20" stroke="#1d1b17"/><line x1="27" y1="72.5" x2="33" y2="72.5" stroke="#1d1b17"/>
<text x="60" y="117" font-size="8.5" fill="#a33a2a">Fläche = ¼</text>
<text x="128" y="66" font-size="8.5" fill="#a8803a">f(x) = x/2</text></svg>'''
page(kick("§ 5", "Dichte = Fläche · Teil 1/2", rel=3) + '''
<h1>Die Fläche <em>ist</em> die Wahrscheinlichkeit.</h1>
<p class="lead">Eine diskrete Zufallsvariable hat eine Liste: jeder Wert mit seiner Wahrscheinlichkeit. Eine stetige hat eine <b>Dichte</b> \\(f(x)\\) – eine Kurve. Die Wahrscheinlichkeit für ein Intervall ist die Fläche darunter.</p>
''' + TR("Kesikli değişkenin bir listesi var: her değer ve olasılığı. Süreklinin bir yoğunluk eğrisi f(x) var. Bir aralığın olasılığı = altındaki alan.") + '''
<div class="grid2" style="margin-top:2mm">
 <div class="card"><div class="lab" style="margin-top:0">A · diskret</div><b>Wahrscheinlichkeitsfunktion</b>
  <div class="fm">\\(P(X=x)\\) für jeden Wert im Träger</div>
  <div style="font-size:9pt">Rechnen mit <b>Summen</b>: \\(\\sum P(X=x)=1\\), \\(E(X)=\\sum x\\,P(X=x)\\)<br>Beispiel: Anzahl Kopf, Anzahl Fehler</div></div>
 <div class="card gold"><div class="lab" style="margin-top:0">B · stetig</div><b>Dichtefunktion</b>
  <div class="fm">\\(P(a\\le X\\le b)=\\int_a^b f(x)\\,dx\\)</div>
  <div style="font-size:9pt">Rechnen mit <b>Integralen</b>: \\(\\int f=1\\), \\(E(X)=\\int x\\,f(x)\\,dx\\)<br>Beispiel: Wartezeit, Gewicht, Anteil</div></div>
</div>
<div class="grid2" style="grid-template-columns:1fr 1.05fr;margin-top:3mm;align-items:center">
 <div class="card" style="padding:2mm">''' + dens + '''</div>
 <div>
  <div class="lab" style="margin-top:0">Die 3 Eigenschaften jeder Dichte</div>
  <ol class="num" style="font-size:9.2pt">
   <li>\\(f(x)\\ge0\\) überall.</li>
   <li>Gesamtfläche \\(\\int_{-\\infty}^{\\infty}f(x)\\,dx=1\\).</li>
   <li>\\(P(X=x)=0\\) für jeden einzelnen Wert – also \\(P(X&lt;1)=P(X\\le1)\\).</li>
  </ol>
  <div class="small">Im Bild: \\(P(X\\le1)\\) ist das Dreieck: \\(\\frac{1\\cdot0.5}{2}=\\frac14\\). Das ist deine PK2-Aufgabe A6c.</div>
 </div>
</div>
''' + chk("§5", "Testat 4, Aufgabe 4: Welche Aussagen muss jede Dichte erfüllen? (a) \\(\\int f=1\\) &nbsp;(b) \\(f(x)\\ge0\\) &nbsp;(c) \\(f(x)\\le1\\) &nbsp;(d) \\(P(X=x)=f(x)\\) &nbsp;(e) f stetig und monoton", 1, sol="Richtig: (a) und (b). Falsch: (c) – Dichten dürfen größer als 1 sein; (d) – \\(P(X=x)=0\\); (e) – keine Bedingung")
     + '''<div class="card gold" style="margin-top:2mm"><div class="lab" style="margin-top:0">Vorgemacht · Wahrscheinlichkeit als Fläche</div>
<div style="font-size:9.2pt">„Berechnen Sie \\(P(0.5\\le X\\le1.5)\\) für \\(f(x)=\\frac x2\\) auf [0, 2].“</div>
<div class="fm">\\(P(0.5\\le X\\le1.5)=\\int_{0.5}^{1.5}\\frac x2\\,dx=\\left[\\frac{x^2}{4}\\right]_{0.5}^{1.5}=\\frac{2.25}{4}-\\frac{0.25}{4}=\\mathbf{0.5}\\)</div>
<div class="small">Kontrolle: Die Fläche liegt zwischen 0 und 1 ✓ · Antwortsatz: „Mit Wahrscheinlichkeit 0.5 dauert es zwischen 0.5 und 1.5 Stunden.“</div></div>'''
     + '<div class="falle" style="margin-top:1mm"><b>Klausur-Falle</b>\\(f(x)&gt;1\\) ist erlaubt (z. B. \\(f(x)=2\\) auf [0; 0.5]). Nur die Fläche muss 1 sein.</div>',
     level="lv2", nxt="Weiter: c bestimmen")

