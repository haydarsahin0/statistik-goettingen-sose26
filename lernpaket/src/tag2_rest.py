r"""Tag 2 · Seiten 11 bis Ende: Level 2 (Rest), Level 3, Level 4, Finale, Lösungsteil."""
from gen_tag2 import page, kick, TR, chk, SOL, P


def vg(title, body):
    return '<div class="card gold" style="margin-top:2mm"><div class="lab" style="margin-top:0">Vorgemacht · %s</div>%s</div>' % (title, body)


def ks(t):
    return '<div class="card note" style="margin-top:2mm;padding:2mm 3mm;font-size:9.2pt"><b style="color:var(--gold)">✎ Klausursatz</b> &nbsp;%s</div>' % t


def falle(t, title="Klausur-Falle"):
    return '<div class="falle"><b>%s</b>%s</div>' % (title, t)


def tip(t, title="Merke"):
    return '<div class="tip"><b>%s</b>%s</div>' % (title, t)


def fm(t):
    return '<div class="fm">%s</div>' % t


def lvl(num, title, lead, tr, chips, items, reward, pid, nxt):
    lis = "".join('<li><b>%s</b><span class="d">· %s</span><span class="r">%s</span></li>' % it for it in items)
    page(('<div class="lab" style="margin-top:6mm">%s</div><div class="lvbox"><div class="bignum">%s</div></div>'
          '<div class="big">%s</div><p class="lead" style="max-width:150mm;color:#e2d9c6">%s</p>%s'
          '<div style="margin:4mm 0">%s</div><div class="lab" style="margin-top:5mm">Du schaltest frei</div><ul class="dia">%s</ul>'
          '<div style="position:absolute;left:0;right:0;bottom:2mm"><div class="reward" style="position:static"><span style="font-size:15pt">☕</span>'
          '<div><div class="lab">Belohnung</div>%s</div><span class="box" style="margin-left:auto;width:4.5mm;height:4.5mm"></span></div></div>')
         % ("Finale" if num == "F" else "Level", num, title, lead, TR(tr), chips, lis, reward), dark=True, pid=pid, nxt=nxt)


def mission(nr, title, xp, intro, tr, task, send, lvlkey, nxt):
    page(kick("M%s" % nr, "Claude-Mission %s" % nr, xp="+%d XP" % xp) +
         '<h1>Mission %s · <em>%s</em></h1><p class="lead">%s</p>%s' % (nr, title, intro, TR(tr)) +
         '<div class="card ink" style="margin-top:3mm"><div class="lab" style="margin-top:0">Aufgabe · auf Papier, ohne Formelsammlung, Stoppuhr</div>'
         '<div style="font-size:9.6pt;line-height:1.55">%s</div></div>' % task +
         '<div class="grid2" style="margin-top:3mm"><div class="card"><div class="lab" style="margin-top:0">So bekommst du die XP</div>'
         '<ol class="num" style="font-size:9pt"><li>Lösen wie in der Klausur: Lösungsweg + Ergebnis eingerahmt.</li><li>Foto machen, an Claude schicken mit <b>„%s“</b>.</li>'
         '<li>Du bekommst Punkte wie in der Klausur, deine Fehler-Muster und die XP zurück.</li></ol></div>'
         '<div class="card gold"><div class="lab" style="margin-top:0">XP-Stufen</div><table class="tb">'
         '<tr><td>alles richtig</td><td style="text-align:right;color:var(--gold)">%d XP</td></tr><tr><td>≥ 75 %% der Punkte</td><td style="text-align:right;color:var(--gold)">%d XP</td></tr>'
         '<tr><td>≥ 50 %% der Punkte</td><td style="text-align:right;color:var(--gold)">%d XP</td></tr><tr><td>versucht</td><td style="text-align:right;color:var(--gold)">5 XP</td></tr></table></div></div>'
         % (send, xp, round(xp * .7), round(xp * .4)) +
         '<div class="lab" style="margin-top:4mm">Platz für Notizen / Skizze</div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div>',
         level=lvlkey, nxt=nxt)


# ======================================================================
# Level 2 · §5 Integral-Crashkurs
area = '''<svg viewBox="0 0 250 130" style="width:100%;height:auto">
<line x1="25" y1="110" x2="240" y2="110" stroke="#1d1b17"/><line x1="25" y1="110" x2="25" y2="8" stroke="#1d1b17"/>
<polygon points="70,110 70,86 180,42 180,110" fill="#f1dfb8"/>
<line x1="25" y1="104" x2="230" y2="22" stroke="#a8803a" stroke-width="2"/>
<line x1="70" y1="110" x2="70" y2="86" stroke="#a8803a" stroke-dasharray="3,3"/><line x1="180" y1="110" x2="180" y2="42" stroke="#a8803a" stroke-dasharray="3,3"/>
<g font-size="10" fill="#1d1b17"><text x="66" y="123">a</text><text x="176" y="123">b</text><text x="232" y="123">x</text><text x="30" y="16">f(x)</text></g>
<text x="96" y="94" font-size="10" fill="#a33a2a">∫ₐᵇ f(x) dx</text><text x="104" y="106" font-size="9" fill="#a33a2a">= F(b) − F(a)</text></svg>'''
page(kick("§ 5", "Integral-Crashkurs · Teil 1/2") + r'''
<h1>Integrieren in <em>fünf Minuten.</em></h1>
<p class="lead">In der Klausur brauchst du nur eine einzige Regel und zwei Handgriffe. Ein Integral ist eine Fläche – und eine Fläche unter einer Dichte ist eine Wahrscheinlichkeit.</p>
''' + TR("Sınavda tek bir kural ve iki el alışkanlığı yeter. İntegral = alan; yoğunluğun altındaki alan = olasılık. Bu sayfayı lise matematiğini hatırlamak için kullan.") + r'''
<div class="grid2" style="grid-template-columns:1.2fr 1fr;align-items:center;margin-top:2mm">
 <div class="card gold"><div class="lab" style="margin-top:0">Die eine Regel · Potenzregel</div>
  <div class="fm" style="font-size:12.5pt">\[\int x^n\,dx=\frac{x^{n+1}}{n+1}\]</div>
  <div style="font-size:9.4pt;text-align:center"><b>Exponent um 1 erhöhen – durch den neuen Exponenten teilen.</b></div></div>
 <div class="card" style="padding:2mm">''' + area + r'''</div>
</div>
''' + TR("Kuvvet kuralı: üssü 1 artır, yeni üsse böl. Grafikte a ile b arasındaki alan = F(b) − F(a).") + r'''
<div class="lab">Die Tabelle, die du auswendig kannst · f(x) → Stammfunktion F(x)</div>
<table class="tb"><tr><th>f(x)</th><td>\(c\)</td><td>\(x\)</td><td>\(x^2\)</td><td>\(x^3\)</td><td>\(\sqrt x=x^{1/2}\)</td><td>\(e^{-\lambda x}\)</td><td>\(\lambda e^{-\lambda x}\)</td></tr>
<tr><th>F(x)</th><td>\(c\,x\)</td><td>\(\frac{x^2}{2}\)</td><td>\(\frac{x^3}{3}\)</td><td>\(\frac{x^4}{4}\)</td><td>\(\frac23x^{3/2}\)</td><td>\(-\frac1\lambda e^{-\lambda x}\)</td><td>\(-e^{-\lambda x}\)</td></tr></table>
<div class="grid3" style="margin-top:3mm">
 <div class="card"><b style="color:var(--gold)">Handgriff 1 · Konstanten raus</b><div style="font-size:9pt">\(\int 5x^2dx=5\cdot\frac{x^3}{3}\) · \(\int\frac{x}{2}dx=\frac12\cdot\frac{x^2}2=\frac{x^2}4\)</div></div>
 <div class="card"><b style="color:var(--gold)">Handgriff 2 · Summen einzeln</b><div style="font-size:9pt">\(\int(x^2-2x)\,dx=\frac{x^3}3-x^2\)</div></div>
 <div class="card"><b style="color:var(--gold)">Grenzen · oben minus unten</b><div style="font-size:9pt">\(\big[F(x)\big]_a^b=F(b)-F(a)\)</div></div>
</div>
''' + vg("Schritt für Schritt", r'''<div style="font-size:9.3pt">\(\int_1^3(2x+1)\,dx\):&nbsp; ① Stammfunktion: \(2\cdot\frac{x^2}{2}+x=x^2+x\) &nbsp;② oben: \(F(3)=9+3=12\) &nbsp;③ unten: \(F(1)=1+1=2\) &nbsp;④ \(12-2=\mathbf{10}\)</div>
<div class="small">Kontrolle: Ableitung von \(x^2+x\) ist \(2x+1\) ✓ – so prüfst du jede Stammfunktion in 5 Sekunden.</div>''') +
     falle(r"Untere Grenze vergessen: \(\int_1^3\) ist nicht einfach \(F(3)\). Nur wenn die untere Grenze 0 ist und \(F(0)=0\), fällt der zweite Teil weg."),
     level="lv2", nxt="Weiter: Integral-Drill")

page(kick("§ 5", "Integral-Crashkurs · Teil 2/2", xp="6 × 2 XP") + r'''
<h1>Die drei Integrale, die in der <em>Klausur</em> kommen.</h1>
''' + TR("Sınavda gelen üç integral tipi: c bulmak (alan = 1), olasılık (a'dan b'ye alan) ve beklenen değer (x·f(x)). Hepsi aynı kuralla.") +
     vg("Typ A · ganze Fläche (für c)", r'''<div style="font-size:9.3pt">\(\int_0^2 c\,x\,dx=c\left[\frac{x^2}{2}\right]_0^2=c\cdot\frac{4}{2}=2c\overset!=1\Rightarrow c=\frac12\) &nbsp;<span class="small">(deine PK2-A6a: hier fehlte das „durch 2“)</span></div>''') +
     vg("Typ B · Erwartungswert: erst x · f(x) ausmultiplizieren", r'''<div style="font-size:9.3pt">\(\int_0^2 x\cdot\frac x2\,dx=\int_0^2\frac{x^2}{2}dx=\left[\frac{x^3}{6}\right]_0^2=\frac86=\frac43=1.333\)</div>''') +
     vg("Typ C · Klammer ausmultiplizieren, Grenzen nicht bei 0", r'''<div style="font-size:9.3pt">\(\int_2^3x(x-2)\,dx=\int_2^3(x^2-2x)\,dx=\left[\frac{x^3}3-x^2\right]_2^3=(9-9)-\left(\frac83-4\right)=0-\left(-\frac43\right)=\frac43\)</div>''') +
     falle(r"\(\int x\cdot x\,dx\ne\int x\,dx\cdot\int x\,dx\). Produkte immer zuerst ausmultiplizieren, dann gliedweise integrieren. Und bei negativer unterer Hälfte: Klammer setzen – \(-(-\frac43)=+\frac43\).") +
     chk("§5", r'''Integral-Drill – je 2 XP. Rechne alle sechs, Kontrolle hinten.<div class="grid3" style="margin-top:1.4mm;font-weight:400">
<div>(a) \(\int_0^1 3x^2\,dx\)</div><div>(b) \(\int_0^4\frac14\,dx\)</div><div>(c) \(\int_1^2(x+1)\,dx\)</div>
<div>(d) \(\int_0^3\frac{x^2}{9}\,dx\)</div><div>(e) \(\int_0^2x^3\,dx\)</div><div>(f) \(\int_0^{\infty}0.5\,e^{-0.5x}\,dx\)</div></div>''', 4,
         sol=r"(a) \([x^3]_0^1=1\) · (b) \(\frac14\cdot4=1\) · (c) \(\left[\frac{x^2}2+x\right]_1^2=4-1.5=2.5\) · (d) \(\left[\frac{x^3}{27}\right]_0^3=1\) · (e) \(\left[\frac{x^4}4\right]_0^2=4\) · (f) \(\left[-e^{-0.5x}\right]_0^\infty=0-(-1)=1\). (a), (b), (d), (f) haben Fläche 1 – das sind gültige Dichten!", xp="12 XP"),
     level="lv2", nxt="Weiter: c bestimmen")

# §6 c bestimmen
page(kick("§ 6", "c bestimmen · Teil 1/2") + r'''
<h1>Gesamtfläche = 1. <em>Immer.</em></h1>
<p class="lead">„Bestimmen Sie c derart, dass f eine gültige Dichtefunktion ist“ – diese Aufgabe kommt in fast jedem Testat. Du schreibst eine einzige Gleichung: Integral über den Träger = 1.</p>
''' + TR("„c'yi f geçerli bir yoğunluk olacak şekilde belirleyin“: tek denklem – taşıyıcı üzerindeki integral = 1. Sonra c'yi çöz ve f ≥ 0 olduğunu kontrol et.") + r'''
<div class="card" style="margin-top:2mm"><div class="lab" style="margin-top:0">Rezept · 4 Zeilen</div>
<ol class="num" style="font-size:9.4pt"><li>Integral über den <b>Träger</b> (die Grenzen aus der Aufgabe) hinschreiben und \(\overset!=1\) setzen.</li>
<li>c vor das Integral ziehen, Stammfunktion bilden (§ 5).</li><li>Grenzen einsetzen: oben minus unten → Zahl · c = 1.</li>
<li>Nach c auflösen und prüfen: Ist \(f(x)\ge0\) auf dem ganzen Träger? Sonst „nicht lösbar“.</li></ol></div>
''' + vg("Testat 4, Aufgabe 5.1", r'''<div style="font-size:9.3pt">\(f(x)=c\,(x-2)\) für \(2\le x\le3\), 0 sonst.</div>
<div class="fm">\(\int_2^3c\,(x-2)\,dx=c\left[\frac{x^2}{2}-2x\right]_2^3=c\big[(4.5-6)-(2-4)\big]=c\,(-1.5+2)=0.5\,c\overset!=1\ \Rightarrow\ \mathbf{c=2}\)</div>
<div class="small">Prüfen: \(f(x)=2(x-2)\ge0\) für \(2\le x\le3\) ✓</div>''') +
     ks("„Damit f eine gültige Dichte ist, muss \\(\\int_2^3 c(x-2)\\,dx=1\\) gelten. Es folgt \\(0.5c=1\\), also \\(c=2\\); außerdem ist \\(f(x)\\ge0\\) auf [2, 3].“") +
     falle("Die Klammer \\((4.5-6)-(2-4)\\) ohne Klammern rechnen ergibt Vorzeichenfehler. Erst beide Werte einzeln ausrechnen: −1.5 und −2, dann subtrahieren.") +
     chk("§6a", r"\(f(x)=c\,(4-x)\) für \(0\le x\le4\), 0 sonst. Bestimmen Sie c.", 2, sol=r"\(c\left[4x-\frac{x^2}2\right]_0^4=c(16-8)=8c=1\Rightarrow c=\frac18\); \(f(x)=\frac{4-x}{8}\ge0\) auf [0, 4] ✓"),
     level="lv2", nxt="Weiter: stückweise Dichten")

page(kick("§ 6", "c bestimmen · Teil 2/2", rel=2) + r'''
<h1>Stückweise Dichten und der <em>„nicht lösbar“</em>-Fall.</h1>
<p class="lead">Hat die Dichte mehrere Stücke, integrierst du jedes Stück über <b>sein</b> Intervall und addierst. Die Summe muss wieder 1 sein.</p>
''' + TR("Yoğunluk birkaç parçadan oluşuyorsa her parçayı kendi aralığında integralle ve topla. Toplam yine 1 olmalı.") +
     vg("Testat 4, Aufgabe 6 · Kontrolle der Fläche", r'''<div style="font-size:9.3pt">\(f(y)=\frac y6\) für \(0\le y\le2\); \(\ f(y)=\frac{6-y}{12}\) für \(2&lt;y\le6\); 0 sonst.</div>
<div class="fm">\(\int_0^2\frac y6\,dy=\left[\frac{y^2}{12}\right]_0^2=\frac4{12}=\frac13\qquad\int_2^6\frac{6-y}{12}\,dy=\frac1{12}\left[6y-\frac{y^2}2\right]_2^6=\frac{(36-18)-(12-2)}{12}=\frac8{12}=\frac23\)</div>
<div class="small">Summe \(\frac13+\frac23=1\) ✓ – eine gültige Dichte. Den Erwartungswert dazu rechnest du in § 8.</div>''') +
     chk("§6b", r"\(f(x)=c\) für \(0\le x&lt;1\) und \(f(x)=2c\) für \(1\le x\le2\), 0 sonst. Bestimmen Sie c und \(P(X\ge1)\).", 2,
         sol=r"\(\int_0^1c\,dx+\int_1^22c\,dx=c+2c=3c=1\Rightarrow c=\frac13\) · \(P(X\ge1)=2c\cdot1=\frac23=0.667\)") + r'''
<div class="grid2" style="margin-top:2mm">
 <div class="card ink"><div class="lab" style="margin-top:0">Wann ist eine Aufgabe „nicht lösbar“?</div>
  <div style="font-size:9pt">\(f(x)=c\,x\) für \(-1\le x\le1\): \(\int_{-1}^1c\,x\,dx=c\left[\frac{x^2}{2}\right]_{-1}^1=c\cdot0=0\ne1\) – <b>kein c möglich</b>. Außerdem wäre f links oder rechts negativ.</div></div>
 <div class="card"><div class="lab" style="margin-top:0">Und dann?</div><div style="font-size:9pt">„nicht lösbar“ ins Kästchen, Begründung in die Box am Ende der Klausur: „Das Integral ist für jedes c gleich 0, daher kann die Fläche nicht 1 sein.“</div></div>
</div>
''' + TR("Hiçbir c alanı 1 yapamıyorsa veya f bir yerde negatif oluyorsa: kutuya „nicht lösbar“, gerekçeyi sondaki kutuya yaz.") +
     tip("Wahrscheinlichkeiten bei stückweisen Dichten: Rechteck = Breite × Höhe, Dreieck = ½ · Breite × Höhe. Oft schneller als integrieren – und eine super Kontrolle.", "Abkürzung"),
     level="lv2", nxt="Weiter: Verteilungsfunktion")

# §7 F(x), Median
fcurve = '''<svg viewBox="0 0 250 120" style="width:100%;height:auto">
<line x1="25" y1="100" x2="240" y2="100" stroke="#1d1b17"/><line x1="25" y1="100" x2="25" y2="8" stroke="#1d1b17"/>
<line x1="10" y1="100" x2="25" y2="100" stroke="#a8803a" stroke-width="2"/>
<path d="M25 100 Q 105 100 185 20" stroke="#a8803a" stroke-width="2" fill="none"/>
<line x1="185" y1="20" x2="240" y2="20" stroke="#a8803a" stroke-width="2"/>
<line x1="25" y1="60" x2="138" y2="60" stroke="#a33a2a" stroke-dasharray="3,3"/><line x1="138" y1="60" x2="138" y2="100" stroke="#a33a2a" stroke-dasharray="3,3"/>
<g font-size="10" fill="#1d1b17"><text x="21" y="113">0</text><text x="181" y="113">2</text><text x="232" y="113">x</text><text x="12" y="24">1</text><text x="2" y="64">0.5</text><text x="30" y="14">F(x)</text></g>
<text x="124" y="113" font-size="9" fill="#a33a2a">√2</text><text x="60" y="54" font-size="9" fill="#a33a2a">Median</text></svg>'''
page(kick("§ 7", "Verteilungsfunktion F(x) · Teil 1/2") + r'''
<h1>F(x) ist die Fläche <em>bis x.</em></h1>
<p class="lead">\(F(x)=P(X\le x)\) – wie bei der empirischen Verteilungsfunktion von Tag 1, nur ohne Treppe: Bei stetigen Zufallsvariablen ist F eine glatte Kurve, die von 0 auf 1 steigt.</p>
''' + TR("F(x) = x'e kadar olan alan. Tag 1'deki ampirik dağılım fonksiyonu gibi, ama merdiven değil, 0'dan 1'e yükselen düzgün bir eğri.") +
     fm(r"\[F(x)=\int_{-\infty}^{x}f(t)\,dt\qquad P(X\le b)=F(b)\qquad P(X>a)=1-F(a)\qquad P(a<X\le b)=F(b)-F(a)\]") + r'''
<div class="grid2" style="grid-template-columns:1.15fr 1fr;align-items:start">
''' + vg("F(x) für \\(f(x)=\\frac x2\\) auf [0, 2]", r'''<div style="font-size:9.2pt">Im Träger: \(F(x)=\int_0^x\frac t2\,dt=\left[\frac{t^2}{4}\right]_0^x=\frac{x^2}{4}\)</div>
<div class="fm">\(F(x)=\begin{cases}0 & x<0\\ \frac{x^2}{4} & 0\le x\le2\\ 1 & x>2\end{cases}\)</div>
<div style="font-size:9pt">\(P(X\le1)=\frac14\) · \(P(X>1.5)=1-\frac{2.25}{4}=0.438\) · \(P(0.5<X\le1.5)=\frac{2.25-0.25}{4}=0.5\)</div>''') + '''
 <div class="card" style="padding:2mm;margin-top:2mm">''' + fcurve + r'''</div></div>
''' + falle(r"F vollständig angeben: auch „0 für \(x&lt;\) Träger“ und „1 für \(x&gt;\) Träger“. Und die untere Integrationsgrenze ist der Anfang des Trägers, nicht immer 0.") +
     chk("§7a", r"\(f(x)=2(x-2)\) auf [2, 3] (Testat 4). Bestimmen Sie F(x) vollständig und \(P(X\le2.5)\).", 2,
         sol=r"\(F(x)=\int_2^x2(t-2)\,dt=\big[(t-2)^2\big]_2^x=(x-2)^2\) für \(2\le x\le3\); 0 für \(x<2\); 1 für \(x>3\) · \(P(X\le2.5)=0.5^2=0.25\)"),
     level="lv2", nxt="Weiter: Median und Quantile")

page(kick("§ 7", "Median und Quantile · Teil 2/2", rel=2) + r'''
<h1>Median: Wo ist die Fläche <em>halb voll?</em></h1>
<p class="lead">Der Median einer stetigen Zufallsvariable ist die Stelle, links von der genau die Hälfte der Fläche liegt. Du setzt F(x) gleich 0.5 und löst nach x auf. Für jedes andere Quantil genauso mit α.</p>
''' + TR("Medyan: solunda alanın tam yarısı olan nokta. F(x) = 0.5 denklemini x için çöz. Her kantil için aynı: F(x) = α.") +
     fm(r"\[F(x_{med})=0.5\qquad F(x_\alpha)=\alpha\]") +
     vg("Median und 90 %-Quantil für \\(F(x)=\\frac{x^2}{4}\\)", r'''<div class="fm">\(\frac{x^2}{4}=0.5\Rightarrow x^2=2\Rightarrow x_{med}=\sqrt2=\mathbf{1.414}\)&nbsp;(\(-\sqrt2\) liegt nicht im Träger) &nbsp;·&nbsp; \(\frac{x^2}{4}=0.9\Rightarrow x_{0.9}=\sqrt{3.6}=\mathbf{1.897}\)</div>''') +
     vg("Exponentialverteilung (kommt in Level 3 wieder)", r'''<div class="fm">\(F(x)=1-e^{-\lambda x}=0.5\Rightarrow e^{-\lambda x}=0.5\Rightarrow-\lambda x=\log0.5\Rightarrow x_{med}=\frac{\log2}{\lambda}\)</div>''') +
     falle("Von zwei Lösungen der Gleichung gilt nur die, die im Träger liegt. Und: Median ≠ Erwartungswert, außer die Dichte ist symmetrisch.") +
     chk("§7b", r"Für \(F(x)=(x-2)^2\) auf [2, 3]: Bestimmen Sie den Median und das 25 %-Quantil.", 2,
         sol=r"\((x-2)^2=0.5\Rightarrow x=2+\sqrt{0.5}=2.707\) · \((x-2)^2=0.25\Rightarrow x=2.5\)") +
     chk("§7c", r"Wie groß ist \(P(X=1.5)\) für die Dichte \(f(x)=\frac x2\)? Ein Satz Begründung.", 1,
         sol=r"0 – bei stetigen Zufallsvariablen hat jeder einzelne Wert die Wahrscheinlichkeit 0 (die Fläche über einem Punkt ist 0)."),
     level="lv2", nxt="Weiter: Erwartungswert per Integral")

# §8 E(X), Var
page(kick("§ 8", "E(X) per Integral · Teil 1/2") + r'''
<h1>Erwartungswert: <em>x mal f(x)</em> integrieren.</h1>
<p class="lead">Die Idee ist dieselbe wie im diskreten Fall – „Wert mal Wahrscheinlichkeit, aufsummieren“ –, nur dass aus der Summe ein Integral wird und aus \(P(X=x)\) die Dichte \(f(x)\).</p>
''' + TR("Fikir kesikli durumla aynı: değer × olasılık, topla. Sadece toplam integrale, P(X = x) de f(x)'e dönüşüyor.") + r'''
<div class="grid2"><div class="card"><div class="lab" style="margin-top:0">diskret</div><div class="fm">\(E(X)=\sum x\cdot P(X=x)\)</div></div>
<div class="card gold"><div class="lab" style="margin-top:0">stetig</div><div class="fm">\(E(X)=\int x\cdot f(x)\,dx\)</div></div></div>
<div class="card" style="margin-top:2mm"><div class="lab" style="margin-top:0">Rezept</div><ol class="num" style="font-size:9.3pt"><li>\(x\cdot f(x)\) hinschreiben und <b>ausmultiplizieren</b>.</li><li>Über den Träger integrieren (§ 5).</li><li>Plausibel? E(X) muss <b>im Träger</b> liegen.</li></ol></div>
''' + vg("PK2 A6b – so hätte es aussehen müssen", r'''<div class="fm">\(E(X)=\int_0^2x\cdot\frac x2\,dx=\int_0^2\frac{x^2}{2}\,dx=\left[\frac{x^3}{6}\right]_0^2=\frac86=\frac43=\mathbf{1.333}\)</div>''') +
     vg("Testat 4, Aufgabe 5.2", r'''<div class="fm">\(E(X)=\int_2^3x\cdot2(x-2)\,dx=2\int_2^3(x^2-2x)\,dx=2\cdot\frac43=\frac83=\mathbf{2.667}\)</div><div class="small">Das Integral \(\int_2^3(x^2-2x)dx=\frac43\) kennst du aus § 5 (Typ C). 2.667 liegt in [2, 3] ✓</div>''') +
     chk("§8a", r"\(f(x)=\frac{4-x}{8}\) auf [0, 4] (aus § 6). Berechnen Sie \(E(X)\).", 2,
         sol=r"\(\frac18\int_0^4(4x-x^2)\,dx=\frac18\left[2x^2-\frac{x^3}3\right]_0^4=\frac18\left(32-\frac{64}3\right)=\frac18\cdot\frac{32}3=\frac43=1.333\)"),
     level="lv2", nxt="Weiter: Varianz per Integral")

page(kick("§ 8", "E(X²) und Var(X) · Teil 2/2") + r'''
<h1>Varianz: zweimal integrieren, <em>einmal abziehen.</em></h1>
<p class="lead">Die Varianz rechnest du wie im diskreten Fall mit dem Verschiebungssatz. Neu ist nur: \(E(X^2)\) ist wieder ein Integral – diesmal mit \(x^2\cdot f(x)\).</p>
''' + TR("Varyans kesikli durumdaki gibi: Var = E(X²) − E(X)². Yeni olan: E(X²) de bir integral, bu sefer x²·f(x) ile. Kesirlerle git!") +
     fm(r"\[E(X^2)=\int x^2f(x)\,dx\qquad Var(X)=E(X^2)-\big(E(X)\big)^2\qquad E(g(X))=\int g(x)f(x)\,dx\]") +
     vg("\\(f(x)=\\frac x2\\) auf [0, 2]", r'''<div class="fm">\(E(X^2)=\int_0^2x^2\cdot\frac x2\,dx=\left[\frac{x^4}{8}\right]_0^2=2\qquad Var(X)=2-\left(\frac43\right)^2=\frac{18}9-\frac{16}9=\frac29=\mathbf{0.222}\)</div>''') +
     vg("Testat 4, Aufgabe 5.3 · \\(E(Y)\\) für \\(Y=X^2\\)", r'''<div class="fm">\(E(X^2)=2\int_2^3(x^3-2x^2)\,dx=2\left[\frac{x^4}4-\frac{2x^3}3\right]_2^3=2\left[\left(\frac{81}4-18\right)-\left(4-\frac{16}3\right)\right]=\frac{43}6=\mathbf{7.167}\)</div><div class="small">Damit \(Var(X)=\frac{43}6-\left(\frac83\right)^2=\frac{129-128}{18}=\frac1{18}=0.056\)</div>''') +
     vg("Testat 4, Aufgabe 6 · stückweise", r'''<div class="fm">\(E(Y)=\int_0^2y\cdot\frac y6\,dy+\int_2^6y\cdot\frac{6-y}{12}\,dy=\left[\frac{y^3}{18}\right]_0^2+\frac1{12}\left[3y^2-\frac{y^3}3\right]_2^6=\frac49+\frac{20}9=\frac83=\mathbf{2.667}\)</div>''') +
     chk("§8b", r"\(f(x)=\frac{4-x}{8}\) auf [0, 4]: Berechnen Sie \(E(X^2)\) und \(Var(X)\) (E(X) aus § 8a).", 2,
         sol=r"\(E(X^2)=\frac18\int_0^4(4x^2-x^3)dx=\frac18\left[\frac{4x^3}3-\frac{x^4}4\right]_0^4=\frac18\cdot\frac{64}3=\frac83\) · \(Var(X)=\frac83-\frac{16}9=\frac89=0.889\)"),
     level="lv2", nxt="Weiter: Rechenregeln")

# §9 Rechenregeln
page(kick("§ 9", "Rechenregeln für E und Var") + r'''
<h1>Rechnen <em>ohne</em> Integral.</h1>
<p class="lead">Oft fragt die Klausur nicht nach X, sondern nach einer Umrechnung wie \(Y=3X-1\) oder einer Summe. Dann musst du nicht neu integrieren – die Regeln erledigen das in einer Zeile.</p>
''' + TR("Sınav çoğu zaman X'i değil, Y = 3X − 1 gibi bir dönüşümü veya bir toplamı sorar. Yeniden integral almana gerek yok; kurallar tek satırda çözer.") + r'''
<table class="tb" style="margin-top:2mm"><tr><th>Regel</th><th>Formel</th><th>Merksatz</th></tr>
<tr><td>linear</td><td>\(E(aX+b)=a\,E(X)+b\)</td><td>alles wird mitgerechnet</td></tr>
<tr><td>linear</td><td>\(Var(aX+b)=a^2\,Var(X)\)</td><td>+b verschiebt nur, a zählt im Quadrat</td></tr>
<tr><td>Summe</td><td>\(E(X+Y)=E(X)+E(Y)\)</td><td>gilt <b>immer</b></td></tr>
<tr><td>Summe/Differenz, unabhängig</td><td>\(Var(X\pm Y)=Var(X)+Var(Y)\)</td><td>auch bei minus: <b>plus</b>!</td></tr>
<tr><td>allgemein</td><td>\(Var(aX+bY)=a^2Var(X)+b^2Var(Y)+2ab\,Cov(X,Y)\)</td><td>Cov = 0 bei Unabhängigkeit</td></tr>
<tr><td>Produkt, unabhängig</td><td>\(E(XY)=E(X)\,E(Y)\)</td><td>braucht man für Schätzer (Level 4)</td></tr></table>
''' + vg("Rückwärts rechnen (Tutorium-Typ)", r'''<div style="font-size:9.2pt">\(E(X)=3,\ Var(X)=1\); \(Z=0.5X+Y\) mit X, Y unabhängig; \(E(Z)=8.5\), \(Var(Y)=1\). Gesucht \(E(Y)\), \(Var(Z)\).</div>
<div class="fm">\(8.5=0.5\cdot3+E(Y)\Rightarrow E(Y)=\mathbf7\qquad Var(Z)=0.5^2\cdot1+1=\mathbf{1.25}\qquad\text{mit }Cov=0.4:\ 1.25+2\cdot0.5\cdot0.4=\mathbf{1.65}\)</div>''') +
     falle(r"\(Var(2X)=4\,Var(X)\), aber \(Var(X_1+X_2)=2\,Var(X)\) für zwei unabhängige Kopien – das ist nicht dasselbe!") +
     chk("§9", r"Für \(f(x)=\frac x2\) gilt \(E(X)=\frac43\), \(Var(X)=\frac29\). Bestimmen Sie \(E(Y)\) und \(Var(Y)\) für \(Y=3X-1\). Und \(Var(X_1-X_2)\) für zwei unabhängige Kopien von X.", 2,
         sol=r"\(E(Y)=3\cdot\frac43-1=3\) · \(Var(Y)=9\cdot\frac29=2\) · \(Var(X_1-X_2)=\frac29+\frac29=\frac49=0.444\)"),
     level="lv2", nxt="Weiter: Mission 1")

mission(1, "Die komplette Dichte-Aufgabe", 30,
        "Jetzt alles aus Level 2 in einer Testat-Aufgabe – so, wie sie am Freitag aussehen kann. Ziel: 15 Minuten.",
        "Level 2'nin tamamı tek bir Testat sorusunda. Cuma günü böyle gelebilir. Hedef: 15 dakika.",
        r'''Die Bearbeitungszeit X (in Stunden) einer Aufgabe habe die Dichte \(f(x)=c\cdot x^2\) für \(0\le x\le3\), 0 sonst.<br>
(a) Bestimmen Sie c. <b>(2 P)</b><br>(b) Bestimmen Sie die Verteilungsfunktion F(x) vollständig und \(P(X&gt;2)\). <b>(3 P)</b><br>
(c) Bestimmen Sie den Median. <b>(2 P)</b><br>(d) Berechnen Sie \(E(X)\) und \(Var(X)\). <b>(4 P)</b><br>(e) Berechnen Sie \(E(2X+1)\) und \(Var(2X+1)\). <b>(2 P)</b>''',
        "Tag 2 · Mission 1", "lv2", "Level 2 geschafft · Pause!")

# ======================================================================
# Level 3 · Verteilungen
lvl("3", "Die <em>Verteilungen</em>",
    "Sechs Modelle beschreiben fast jede Zufallsvariable der Klausur. Wer am Text erkennt, welches Modell gemeint ist, hat schon die Hälfte der Punkte – der Rest ist Einsetzen.",
    "Altı model sınavdaki neredeyse her rastgele değişkeni tanımlar. Metinden hangi modelin kastedildiğini tanırsan puanın yarısını aldın; gerisi yerine koymak.",
    '<span class="chip">6 Stationen</span><span class="chip">100 min</span><span class="chip f">80 XP</span>',
    [("Welche Verteilung?", "Erkennungs-Schlüssel + 6 Erkennungs-Checks", "§ 10"), ("Binomial", "„mindestens“, „höchstens“, E und Var", "§ 11"),
     ("Poisson", "λ an den Zeitraum anpassen", "§ 12"), ("Gleich + Exponential", "Rechteck und Wartezeit", "§ 13"),
     ("Normalverteilung", "standardisieren, Φ ablesen, Quantile", "§ 14"), ("Summen + ZGWS", "Verteilung von \\(\\bar X\\)", "§ 15")],
    "Nach Level 3: 10 Minuten an die frische Luft, +5 XP Level-Bonus.", "lv3", "Level 3 · Start")

page(kick("§ 10", "Welche Verteilung? · Erkennen", xp="6 × 3 XP") + r'''
<h1>Der Text <em>verrät</em> die Verteilung.</h1>
<p class="lead">Lies die Aufgabe und suche das Signalwort. Dann schreibst du sofort das Modell mit Parametern hin – dafür gibt es in der Klausur schon den ersten Punkt.</p>
''' + TR("Soruyu oku, ipucu kelimeyi bul, modeli parametreleriyle hemen yaz – sınavda ilk puan bunun için verilir.") + r'''
<table class="tb" style="margin-top:2mm"><tr><th>Signal im Text</th><th>Modell</th><th>Parameter</th><th>E · Var</th></tr>
<tr><td>n unabhängige Versuche, Anzahl Erfolge, „mit Zurücklegen“, „rät“</td><td><b>Binomial</b> \(B(n,\pi)\)</td><td>n, π</td><td>\(n\pi\) · \(n\pi(1-\pi)\)</td></tr>
<tr><td>Anzahl pro Zeitraum, „im Durchschnitt … pro Monat“, ohne Obergrenze</td><td><b>Poisson</b> \(Po(\lambda)\)</td><td>λ = Mittel im gefragten Zeitraum</td><td>λ · λ</td></tr>
<tr><td>„jeder Wert zwischen a und b gleich wahrscheinlich“</td><td><b>Gleich</b> \(U(a,b)\)</td><td>a, b</td><td>\(\frac{a+b}2\) · \(\frac{(b-a)^2}{12}\)</td></tr>
<tr><td>Wartezeit, Dauer bis zum Ereignis, „im Mittel 3 Stunden“</td><td><b>Exponential</b> \(Exp(\lambda)\)</td><td>λ = 1 / Mittel</td><td>\(\frac1\lambda\) · \(\frac1{\lambda^2}\)</td></tr>
<tr><td>Messwerte (Gewicht, Größe, Füllmenge), Mittelwerte vieler Werte</td><td><b>Normal</b> \(N(\mu,\sigma^2)\)</td><td>μ, σ²</td><td>μ · σ²</td></tr>
<tr><td>ein einzelner Ja/Nein-Versuch</td><td><b>Bernoulli</b> \(Be(\pi)\)</td><td>π</td><td>π · \(\pi(1-\pi)\)</td></tr></table>
''' + chk("§10", r'''Welches Modell (mit Parametern)? – je 3 XP<div class="grid2" style="margin-top:1.2mm;font-weight:400;font-size:9.2pt">
<div>(1) Anzahl Sechsen bei 10 Würfen eines fairen Würfels</div><div>(2) Anrufe pro Stunde, im Mittel 4</div>
<div>(3) Wartezeit auf den Bus, im Mittel 8 Minuten</div><div>(4) Körpergröße von Studierenden</div>
<div>(5) Ankunftszeit zwischen 8:00 und 8:20, jede Minute gleich wahrscheinlich</div><div>(6) Gewittertage pro Monat, im Mittel zwei (Testat 4)</div></div>''', 3,
         sol=r"(1) \(B(10;\frac16)\) · (2) \(Po(4)\) · (3) \(Exp(\frac18)\) · (4) \(N(\mu,\sigma^2)\) · (5) \(U(0;20)\) (in Minuten nach 8:00) · (6) \(Po(2)\)", xp="18 XP") +
     falle("Poisson-λ immer auf den gefragten Zeitraum umrechnen: im Mittel 2 pro Monat → in 3 Monaten λ = 6. Und Exponential-λ ist der <b>Kehrwert</b> des Mittels."),
     level="lv3", nxt="Weiter: Binomialverteilung")

page(kick("§ 11", "Binomialverteilung · Teil 1/2") + r'''
<h1>n Versuche, k <em>Treffer.</em></h1>
<p class="lead">Die Binomialverteilung zählt Erfolge in n unabhängigen, gleichen Versuchen. Die Formel hat drei Teile: wie viele Anordnungen, Wahrscheinlichkeit der Treffer, Wahrscheinlichkeit der Nieten.</p>
''' + TR("Binom dağılımı n bağımsız, aynı denemedeki başarıları sayar. Formülün üç parçası var: kaç farklı sıralama, başarıların olasılığı, başarısızlıkların olasılığı.") +
     fm(r"\[P(X=k)=\binom nk\,\pi^k\,(1-\pi)^{n-k}\qquad E(X)=n\pi\qquad Var(X)=n\pi(1-\pi)\]") + r'''
<table class="tb"><tr><th>Text</th><th>Rechnung</th><th>Text</th><th>Rechnung</th></tr>
<tr><td>genau k</td><td>\(P(X=k)\)</td><td>mindestens 1</td><td>\(1-P(X=0)=1-(1-\pi)^n\)</td></tr>
<tr><td>höchstens k</td><td>\(P(0)+\dots+P(k)\)</td><td>mindestens k</td><td>\(1-P(X\le k-1)\) oder \(P(k)+\dots+P(n)\)</td></tr>
<tr><td>mehr als k</td><td>\(1-P(X\le k)\)</td><td>weniger als k</td><td>\(P(X\le k-1)\)</td></tr></table>
''' + vg("Testat 4, Aufgabe 2", r'''<div style="font-size:9.2pt">60 schwarze und 20 gelbe Kugeln, 5 Züge <b>mit</b> Zurücklegen, X = Anzahl gelber Kugeln.</div>
<div class="fm">\(X\sim B\!\left(5;\ \frac{20}{80}=0.25\right)\qquad P(X&gt;4)=P(X=5)=0.25^5=\mathbf{0.001}\qquad P(X\ge1)=1-0.75^5=\mathbf{0.763}\)</div>
<div class="small">R-Lückentext dazu: <code>x &lt;- rbinom(10000, size = 5, prob = 0.25)</code></div>''') +
     tip(r"Wähle die kürzere Seite: Für „mindestens 4 von 5“ rechnest du \(P(4)+P(5)\) (2 Terme), für „mindestens 1 von 5“ lieber \(1-P(0)\) (1 Term).", "Abkürzung") +
     falle(r"\(1-(1-\pi)^n\) ist nur „mindestens 1“ – nicht „mindestens 4“ (dein PK2-A6d-Fehler)."),
     level="lv3", nxt="Weiter: Binomial üben")

page(kick("§ 11", "Binomialverteilung · Teil 2/2", xp="2 × 5 XP") + r'''
<h1>Binomial: zwei <em>Klausur-Klassiker.</em></h1>
''' + TR("Sınavın iki klasiği: „en az k“ ve parametrelerle dağılımı yazma.") +
     vg("Multiple-Choice-Test, Student rät", r'''<div style="font-size:9.2pt">10 Fragen, je 4 Antworten, genau eine richtig. Y = Anzahl richtiger Antworten. Wie wahrscheinlich sind mindestens 2 richtige?</div>
<div class="fm">\(Y\sim B(10;\ 0.25)\qquad P(Y\ge2)=1-P(0)-P(1)=1-0.75^{10}-10\cdot0.25\cdot0.75^9=1-0.0563-0.1877=\mathbf{0.756}\)</div>''') +
     ks("„Y ist binomialverteilt mit n = 10 und π = 0.25. Die Wahrscheinlichkeit für mindestens zwei richtige Antworten beträgt 0.756.“") +
     chk("§11a", r"\(X\sim B(8;\ 0.3)\). Berechnen Sie \(P(X=2)\), \(P(X\le1)\), \(E(X)\) und \(Var(X)\).", 3,
         sol=r"\(P(X=2)=28\cdot0.09\cdot0.7^6=0.296\) · \(P(X\le1)=0.7^8+8\cdot0.3\cdot0.7^7=0.058+0.198=0.255\) · \(E=2.4\) · \(Var=1.68\)") +
     chk("§11b", r"Eine Maschine produziert 5 % Ausschuss. In einer Kiste liegen 20 Teile. Wie wahrscheinlich ist mindestens ein Ausschussteil? Welches Modell, welche Annahme?", 3,
         sol=r"\(X\sim B(20;\ 0.05)\), Annahme: Teile unabhängig · \(P(X\ge1)=1-0.95^{20}=1-0.358=0.642\)") +
     tip(r"Taschenrechner: \(\binom{10}{2}\) = 10 nCr 2 = 45. Potenzen mit großen Exponenten (\(0.75^9\)) direkt eintippen, nicht schrittweise runden.", "Taschenrechner"),
     level="lv3", nxt="Weiter: Poisson")

page(kick("§ 12", "Poissonverteilung") + r'''
<h1>Wie oft pro <em>Zeitraum?</em></h1>
<p class="lead">Die Poissonverteilung zählt Ereignisse in einem festen Zeitraum (oder auf einer Fläche), wenn es keine feste Obergrenze gibt: Anrufe pro Stunde, Tore pro Spiel, Gewittertage pro Monat.</p>
''' + TR("Poisson belirli bir zamanda olayları sayar, üst sınır yok: saatteki aramalar, maçtaki goller, aydaki fırtınalı günler. λ = o zamandaki ortalama.") +
     fm(r"\[P(X=k)=\frac{\lambda^k}{k!}\,e^{-\lambda}\qquad E(X)=Var(X)=\lambda\qquad P(X=0)=e^{-\lambda}\qquad\text{Zeitraum}\times t\ \Rightarrow\ \lambda\times t\]") +
     vg("Testat 4, Aufgabe 3", r'''<div style="font-size:9.2pt">Im Mittel 2 Gewittertage pro Monat. Wahrscheinlichkeit für mehr als 2 Gewittertage?</div>
<div class="fm">\(Y\sim Po(2)\qquad P(Y&gt;2)=1-P(0)-P(1)-P(2)=1-e^{-2}\left(1+2+\frac{2^2}{2}\right)=1-5e^{-2}=\mathbf{0.323}\)</div>
<div class="small">R: richtig sind <code>1 - ppois(2, 2)</code> und <code>1 - dpois(0, 2) - dpois(1, 2) - dpois(2, 2)</code> – nicht <code>1 - ppois(3, 2)</code>.</div>''') +
     chk("§12", r"Im Mittel 3 Anrufe pro Stunde. Berechnen Sie (a) \(P(X=0)\), (b) \(P(X\ge2)\) in einer Stunde, (c) die Wahrscheinlichkeit für keinen Anruf in 2 Stunden.", 3,
         sol=r"(a) \(e^{-3}=0.050\) · (b) \(1-e^{-3}(1+3)=0.801\) · (c) \(\lambda=6\): \(e^{-6}=0.002\)") +
     falle(r"\(Z=2X+4\) ist nicht mehr poissonverteilt: \(E(Z)=2\lambda+4\) ≠ \(Var(Z)=4\lambda\). Poisson verlangt E = Var.") +
     tip(r"Achtung: \(e^{-2}\) mit der Taste \(e^x\) und −2, nicht \(e\cdot(-2)\). Kontrolle: \(e^{-2}=0.1353\).", "Taschenrechner"),
     level="lv3", nxt="Weiter: Gleich- und Exponentialverteilung")

page(kick("§ 13", "Stetige Gleichverteilung · Teil 1/2", rel=2) + r'''
<h1>Das <em>Rechteck.</em></h1>
<p class="lead">Wenn jeder Wert zwischen a und b gleich wahrscheinlich ist, ist die Dichte ein Rechteck der Höhe \(\frac1{b-a}\). Jede Wahrscheinlichkeit ist dann einfach Breite mal Höhe – ohne Integral.</p>
''' + TR("a ile b arasındaki her değer eşit olasılıklıysa yoğunluk 1/(b − a) yüksekliğinde bir dikdörtgen. Her olasılık = genişlik × yükseklik, integrale gerek yok.") +
     fm(r"\[f(x)=\frac1{b-a}\ (a\le x\le b)\qquad F(x)=\frac{x-a}{b-a}\qquad E(X)=\frac{a+b}2\qquad Var(X)=\frac{(b-a)^2}{12}\qquad x_\alpha=a+\alpha(b-a)\]") +
     vg("Wartezeit \\(X\\sim U(2,10)\\) in Minuten", r'''<div class="fm">\(f(x)=\frac18\) auf [2, 10] · \(P(X&gt;7)=\frac{10-7}{8}=\mathbf{0.375}\) · \(E(X)=\mathbf6\) · \(Var(X)=\frac{8^2}{12}=\mathbf{5.333}\) · \(x_{0.9}=2+0.9\cdot8=\mathbf{9.2}\)</div>''') +
     chk("§13a", r"Der Bus kommt zu einem zufälligen Zeitpunkt in den nächsten 30 Minuten. Berechnen Sie \(P(X\le10)\), \(E(X)\), \(Var(X)\) und \(P(5\le X\le20)\).", 3,
         sol=r"\(U(0,30)\): \(P(X\le10)=\frac13\) · \(E=15\) · \(Var=\frac{900}{12}=75\) · \(P(5\le X\le20)=\frac{15}{30}=0.5\)") +
     tip("Testat 4, Aufgabe 7 fragt nach dem Mittelwert vieler gleichverteilter Werte – das ist kein Rechteck mehr, sondern ZGWS (§ 15).", "Verknüpfung"),
     level="lv3", nxt="Weiter: Exponentialverteilung")

page(kick("§ 13", "Exponentialverteilung · Teil 2/2") + r'''
<h1>Warten auf <em>das Ereignis.</em></h1>
<p class="lead">Die Exponentialverteilung beschreibt Wartezeiten: bis zum Defekt, bis zum nächsten Kunden, bis der Fuchs eine Gans fängt. Die wichtigste Formel ist die für „länger als“.</p>
''' + TR("Üstel dağılım bekleme sürelerini anlatır. En önemli formül „x'ten uzun sürer“ için: P(X > x) = e^(−λx). λ = 1/ortalama.") +
     fm(r"\[f(x)=\lambda e^{-\lambda x}\ (x\ge0)\qquad P(X\le x)=1-e^{-\lambda x}\qquad P(X>x)=e^{-\lambda x}\qquad E(X)=\frac1\lambda\qquad Var(X)=\frac1{\lambda^2}\]") +
     vg("Testat 4, Aufgabe 8 · der Fuchs", r'''<div style="font-size:9.2pt">Der Fuchs jagt im Mittel 3 Stunden, bis er eine Gans fängt. Wahrscheinlichkeit, länger als 10 Stunden zu jagen?</div>
<div class="fm">\(X\sim Exp\!\left(\lambda=\frac13\right)\qquad P(X&gt;10)=e^{-10/3}=\mathbf{0.036}\qquad x_{med}=\frac{\log2}{1/3}=3\log2=\mathbf{2.079}\)</div>''') +
     ks("„Die Jagdzeit wird durch eine Exponentialverteilung mit λ = 1/3 modelliert. Mit Wahrscheinlichkeit 0.036 jagt der Fuchs länger als zehn Stunden.“") +
     chk("§13b", r"Die Lebensdauer einer Batterie ist exponentialverteilt mit Mittelwert 5 Jahren. Berechnen Sie \(P(X\le2)\), \(P(X&gt;5)\) und \(Var(X)\).", 3,
         sol=r"\(\lambda=0.2\): \(P(X\le2)=1-e^{-0.4}=0.330\) · \(P(X>5)=e^{-1}=0.368\) · \(Var=\frac1{0.04}=25\)") +
     falle(r"Weibull mit r = 1 ist die Exponentialverteilung: \(r\lambda(\lambda x)^{r-1}e^{-(\lambda x)^r}\) wird zu \(\lambda e^{-\lambda x}\). Das stand in der Probeklausur 2022!"),
     level="lv3", nxt="Weiter: Normalverteilung")

normal = '''<svg viewBox="0 0 260 110" style="width:100%;height:auto">
<path d="M10 95 C 70 95, 90 15, 130 15 C 170 15, 190 95, 250 95" stroke="#a8803a" stroke-width="2" fill="none"/>
<path d="M10 95 C 70 95, 90 15, 130 15 C 150 15, 160 35, 170 50 L170 95 Z" fill="#f1dfb8"/>
<path d="M10 95 C 70 95, 90 15, 130 15 C 170 15, 190 95, 250 95" stroke="#a8803a" stroke-width="2" fill="none"/>
<line x1="5" y1="95" x2="255" y2="95" stroke="#1d1b17"/><line x1="130" y1="95" x2="130" y2="15" stroke="#6b665c" stroke-dasharray="3,3"/>
<g font-size="10" fill="#1d1b17"><text x="125" y="107">μ</text><text x="166" y="107">x</text></g>
<text x="80" y="80" font-size="9.5" fill="#a33a2a">Φ(z) = P(X ≤ x)</text><text x="176" y="40" font-size="9" fill="#6b665c">z = (x − μ)/σ</text></svg>'''
page(kick("§ 14", "Normalverteilung · Teil 1/2") + r'''
<h1>Standardisieren, dann <em>ablesen.</em></h1>
<p class="lead">Für die Normalverteilung gibt es keine Stammfunktion zum Hinschreiben. Stattdessen verwandelst du jedes x in ein z und liest die Fläche in der Φ-Tabelle ab.</p>
''' + TR("Normal dağılımın yazılabilir bir integrali yok. Her x'i bir z'ye çevirip alanı Φ tablosundan okursun. σ = varyansın karekökü!") +
     '<div class="grid2" style="grid-template-columns:1fr 1fr;align-items:center"><div>' +
     fm(r"\[Z=\frac{X-\mu}{\sigma}\sim N(0,1)\]") + fm(r"\(P(X\le x)=\Phi(z)\qquad P(X>x)=1-\Phi(z)\)") + fm(r"\(\Phi(-z)=1-\Phi(z)\)") +
     '</div><div class="card" style="padding:2mm">' + normal + '</div></div>' + r'''
<div class="lab">Φ-Werte, die du ständig brauchst</div>
<table class="tb"><tr><th>z</th><td>0</td><td>0.5</td><td>1</td><td>1.28</td><td>1.5</td><td>1.645</td><td>1.96</td><td>2</td><td>2.33</td><td>2.5</td></tr>
<tr><th>Φ(z)</th><td>0.5</td><td>0.6915</td><td>0.8413</td><td>0.90</td><td>0.9332</td><td>0.95</td><td>0.975</td><td>0.9772</td><td>0.99</td><td>0.9938</td></tr></table>
''' + vg("Körpergröße \\(X\\sim N(170,\\,100)\\)", r'''<div class="fm">\(\sigma=\sqrt{100}=10\quad P(X\le185)=\Phi(1.5)=\mathbf{0.933}\quad P(X&gt;160)=1-\Phi(-1)=\Phi(1)=\mathbf{0.841}\quad P(160&lt;X&lt;180)=2\Phi(1)-1=\mathbf{0.683}\)</div>''') +
     chk("§14a", r"\(X\sim N(50,\,16)\). Berechnen Sie \(P(X\le56)\), \(P(X&gt;46)\) und \(P(X&lt;44)\).", 2,
         sol=r"\(\sigma=4\): \(\Phi(1.5)=0.933\) · \(\Phi(1)=0.841\) · \(1-\Phi(1.5)=0.067\)") +
     falle(r"\(N(170,\,100)\): 100 ist die <b>Varianz</b>. Durch 100 teilen statt durch 10 ist der häufigste Fehler überhaupt."),
     level="lv3", nxt="Weiter: Quantile der Normalverteilung")

page(kick("§ 14", "Quantile und σ-Regeln · Teil 2/2", rel=2) + r'''
<h1>Rückwärts: Welcher Wert gehört zur <em>Fläche?</em></h1>
<p class="lead">Ist die Wahrscheinlichkeit gegeben und der Wert gesucht, gehst du den Weg rückwärts: z aus der Tabelle suchen, dann \(x=\mu+z\,\sigma\).</p>
''' + TR("Olasılık verilip değer aranıyorsa ters git: tablodan z'yi bul, sonra x = μ + z·σ. Alt kantillerde z negatif.") +
     fm(r"\[x_\alpha=\mu+z_\alpha\,\sigma\qquad z_{1-\alpha}=-z_\alpha\qquad z_{0.9}=1.282\quad z_{0.95}=1.645\quad z_{0.975}=1.96\quad z_{0.99}=2.326\]") +
     vg("95 %-Quantil der Körpergröße \\(N(170,100)\\)", r'''<div class="fm">\(x_{0.95}=170+1.645\cdot10=\mathbf{186.45}\) cm – nur 5 % sind größer.</div>''') +
     vg("Abfüllung: Welche Menge wird nur von 10 % unterschritten?", r'''<div class="fm">\(X\sim N(500,16)\): \(x_{0.1}=500-1.282\cdot4=\mathbf{494.872}\) g</div>''') + r'''
<div class="card" style="margin-top:2mm"><div class="lab" style="margin-top:0">σ-Regeln zum Schätzen und Kontrollieren</div>
<div style="font-size:9.2pt">\(P(\mu-\sigma\le X\le\mu+\sigma)\approx0.683\) · \(P(\mu-2\sigma\le X\le\mu+2\sigma)\approx0.954\) · \(P(\mu-3\sigma\le X\le\mu+3\sigma)\approx0.997\) → „mehr als 2σ vom Mittel entfernt“ ≈ 0.046</div></div>
''' + chk("§14b", r"IQ-Werte sind \(N(100,\,225)\). Ab welchem IQ gehört man zu den besten 2.5 %? Wie groß ist der Anteil zwischen 85 und 115?", 2,
          sol=r"\(\sigma=15\): \(x_{0.975}=100+1.96\cdot15=129.4\) · \(P(85<X<115)=2\Phi(1)-1=0.683\)") +
     tip("Die Quantile \\(z_{0.95}\\) und \\(z_{0.975}\\) brauchst du morgen bei Konfidenzintervallen und Tests ständig – heute schon einprägen!", "Vorschau Tag 3"),
     level="lv3", nxt="Weiter: Summen und ZGWS")

page(kick("§ 15", "Summen und Zentraler Grenzwertsatz") + r'''
<h1>Viele Werte <em>zusammen.</em></h1>
<p class="lead">Summen und Mittelwerte vieler unabhängiger Zufallsvariablen sind (annähernd) normalverteilt – egal, wie die einzelnen Werte verteilt sind. Das ist der Zentrale Grenzwertsatz, und er ist die Brücke zu den Tests von morgen.</p>
''' + TR("Çok sayıda bağımsız değişkenin toplamı ve ortalaması (yaklaşık) normal dağılır – tek tek nasıl dağıldıklarından bağımsız. Merkezi limit teoremi yarınki testlerin köprüsü.") +
     fm(r"\[\bar X\overset{a}{\sim}N\!\left(\mu,\ \frac{\sigma^2}{n}\right)\qquad\sum_{i=1}^nX_i\overset{a}{\sim}N(n\mu,\ n\sigma^2)\qquad aX+b\sim N(a\mu+b,\ a^2\sigma^2)\]") +
     vg("Testat 4, Aufgabe 7", r'''<div style="font-size:9.2pt">\(X\sim U(a,b)\) mit \(E(X)=\mu\), \(Var(X)=\sigma^2\); Mittelwert aus n = 100 Werten.</div><div class="fm">\(\bar X\overset{a}{\sim}N\!\left(\mu,\frac{\sigma^2}{100}\right)\qquad\text{mit }E(X)=4:\ P(\bar X&lt;4)\approx\Phi(0)=\mathbf{0.5}\)</div>''') +
     vg("Mittelwert mit Zahlen", r'''<div class="fm">\(n=36,\ \mu=50,\ \sigma=12:\quad\bar X\overset a\sim N(50,\ 4)\quad P(\bar X&gt;53)\approx1-\Phi\!\left(\frac{3}{2}\right)=1-0.9332=\mathbf{0.067}\)</div>''') +
     chk("§15", r"(a) n = 25, μ = 100, σ = 10: Wie ist \(\bar X\) verteilt, und wie groß ist \(P(\bar X&gt;103)\)? (b) \(X_1,\dots,X_4\) unabhängig \(N(10,9)\): Verteilung von \(S=\sum X_i\) und \(P(S&gt;46)\)?", 3,
         sol=r"(a) \(\bar X\sim N(100,\,4)\), \(P(\bar X>103)=1-\Phi(1.5)=0.067\) · (b) \(S\sim N(40,\,36)\), \(P(S>46)=1-\Phi(1)=0.159\)") +
     falle(r"Standardabweichung von \(\bar X\) ist \(\frac{\sigma}{\sqrt n}\) (hier 2), nicht σ (12) und nicht \(\frac{\sigma^2}{n}\) (4)."),
     level="lv3", nxt="Level 3 geschafft · Pause!")

# ======================================================================
# Level 4 · Schätzer & ML
lvl("4", "Schätzer &amp; <em>Likelihood</em>",
    "Bisher kanntest du die Parameter. Jetzt drehst du den Spieß um: Aus Daten schätzt du μ, λ oder θ – und prüfst, ob dein Schätzer gut ist. Probeklausur 2022: 15 Punkte allein aus diesem Level.",
    "Şimdiye kadar parametreler biliniyordu. Şimdi tersine: veriden μ, λ veya θ'yı tahmin ediyorsun ve tahmincinin iyi olup olmadığını kontrol ediyorsun. Probeklausur 2022: sadece bu level'dan 15 puan.",
    '<span class="chip">4 Stationen + Mission</span><span class="chip">110 min</span><span class="chip f">100 XP</span>',
    [("Erwartungstreu?", "E auf den Schätzer anwenden, Bias", "§ 16"), ("Varianz, MSE, Konsistenz", "Schätzer vergleichen", "§ 17"),
     ("ML-Rezept", "6 Schritte, Log-Regeln, Ableiten", "§ 18"), ("ML-Klassiker", "Poisson, Exponential, geometrisch, spezielle Dichten", "§ 19"),
     ("Mission 2", "ML-Aufgabe auf Papier → Foto an Claude", "40 XP")],
    "Nach Level 4: richtige Pause, etwas essen. +5 XP Level-Bonus – du hast das Schwerste geschafft.", "lv4", "Level 4 · Start")

page(kick("§ 16", "Erwartungstreue · Teil 1/2") + r'''
<h1>Trifft der Schätzer <em>im Mittel?</em></h1>
<p class="lead">Ein Schätzer ist eine Formel aus den Daten, zum Beispiel \(\bar X\). Er heißt <b>erwartungstreu</b> (unverzerrt), wenn er im Durchschnitt über viele Stichproben genau den wahren Parameter trifft.</p>
''' + TR("Tahminci verilerden bir formül, örn. X̄. Çok sayıda örneklemde ortalama olarak gerçek parametreyi tam tutturuyorsa „erwartungstreu“ (yansız) denir.") +
     fm(r"\[\text{erwartungstreu}\iff E(\hat\vartheta)=\vartheta\qquad Bias(\hat\vartheta)=E(\hat\vartheta)-\vartheta\]") + r'''
<div class="card"><div class="lab" style="margin-top:0">Rezept · immer gleich</div><ol class="num" style="font-size:9.3pt">
<li>Schätzer vereinfachen (kürzen, Produkte auflösen).</li><li>E auf jeden Summanden anwenden, Konstanten herausziehen (§ 9).</li>
<li>\(E(X_i)\) aus der Aufgabe einsetzen.</li><li>Mit dem Parameter vergleichen → „erwartungstreu“ oder Bias angeben.</li></ol></div>
''' + vg("\\(E(X)=\\frac\\theta2\\): zwei Kandidaten", r'''<div class="fm">\(\hat\theta_1=2\bar X:\ E(\hat\theta_1)=2\cdot\frac\theta2=\theta\) ✓ erwartungstreu &nbsp;&nbsp; \(\hat\theta_2=\bar X+1:\ E(\hat\theta_2)=\frac\theta2+1\), \(Bias=1-\frac\theta2\)</div>''') +
     vg("Testat-Typ mit Teilsumme", r'''<div style="font-size:9.2pt">\(E(X)=\frac\kappa2\), \(\tilde\kappa=X_1+\frac1{2n}\sum_{i=2}^nX_i\)</div>
<div class="fm">\(E(\tilde\kappa)=\frac\kappa2+\frac1{2n}(n-1)\frac\kappa2=\frac{(3n-1)\kappa}{4n}\qquad Bias=\frac{(3n-1)\kappa}{4n}-\kappa=-\frac{(n+1)\kappa}{4n}\ne0\)</div>
<div class="small">Die Summe läuft von 2 bis n → das sind n − 1 Summanden, nicht n.</div>''') +
     ks("„Da \\(E(\\hat\\theta)=\\theta\\) für alle θ gilt, ist \\(\\hat\\theta\\) ein unverzerrter Schätzer für θ.“"),
     level="lv4", nxt="Weiter: Erwartungstreue üben")

page(kick("§ 16", "Erwartungstreue · Teil 2/2", xp="2 × 5 XP") + r'''
<h1>Die zwei <em>Fallen</em> beim Erwartungswert.</h1>
''' + TR("Beklenen değerdeki iki tuzak: çarpımlar ve kareler. Bağımsızlıkta E(X₁X₂) = E(X₁)E(X₂), ama E(X²) ≠ E(X)².") + r'''
<div class="grid2" style="margin-top:2mm">
 <div class="card"><div class="lab" style="margin-top:0">Produkte</div><div style="font-size:9.2pt">Unabhängig: \(E(X_1X_2)=E(X_1)\,E(X_2)=\mu^2\).<br>Kürzen vor dem Rechnen: \(\frac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}=\frac1{X_1}\) (PK 2022, A7).</div></div>
 <div class="card"><div class="lab" style="margin-top:0">Quadrate</div><div style="font-size:9.2pt">\(E(X^2)=Var(X)+E(X)^2=\sigma^2+\mu^2\ne\mu^2\).<br>Ist nur \(E(X_i^2)\) gegeben: \(Var(X_i)=E(X_i^2)-E(X_i)^2\).</div></div>
</div>
''' + vg("Probeklausur 2022, Aufgabe 7 (offizielle Lösung)", r'''<div style="font-size:9.2pt">\(E(X)=\frac\alpha4\), \(\hat\alpha=\frac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}+\frac{X_n}\alpha-\frac14=\frac1{X_1}+\frac{X_n}{\alpha}-\frac14\)</div>
<div class="fm">\(E(\hat\alpha)=E\!\left(\frac1{X_1}\right)+\frac{1}{\alpha}\cdot\frac\alpha4-\frac14=E\!\left(\frac1{X_1}\right)\overset{\text{Lösung}}{=}\frac4\alpha\ne\alpha\ \Rightarrow\ \text{verzerrt}\)</div>
<div class="small">Mathematisch gilt \(E(\frac1X)\ne\frac1{E(X)}\) – das Ergebnis „verzerrt“ bleibt aber richtig.</div>''') +
     chk("§16a", r"\(E(X_i)=\mu\). Prüfen Sie \(\hat\mu=\frac{2X_1+X_2+X_3}{4}\) und \(\tilde\mu=\frac{X_1+X_2}{3}\) auf Erwartungstreue; ggf. Bias angeben.", 3,
         sol=r"\(E(\hat\mu)=\frac{2\mu+\mu+\mu}4=\mu\) → erwartungstreu · \(E(\tilde\mu)=\frac{2\mu}3\), \(Bias=-\frac\mu3\) → verzerrt") +
     chk("§16b", r"\(E(X_i)=\mu\), \(Var(X_i)=\sigma^2\), unabhängig. Ist \(X_1\cdot X_2\) erwartungstreu für \(\mu^2\)? Ist \(X_1^2\) erwartungstreu für \(\mu^2\)?", 2,
         sol=r"\(E(X_1X_2)=\mu\cdot\mu=\mu^2\) → ja · \(E(X_1^2)=\sigma^2+\mu^2\) → nein, Bias \(\sigma^2\)"),
     level="lv4", nxt="Weiter: Varianz und MSE")

page(kick("§ 17", "Varianz, MSE, Konsistenz", rel=2) + r'''
<h1>Welcher Schätzer ist <em>besser?</em></h1>
<p class="lead">Zwei erwartungstreue Schätzer vergleichst du über die Varianz: kleiner ist besser (effizienter). Ist einer verzerrt, entscheidet der MSE, der Bias und Varianz zusammenfasst.</p>
''' + TR("İki yansız tahminciyi varyansla karşılaştır: küçük olan daha iyi. Biri yanlıysa MSE karar verir: Bias² + Varyans. Tutarlı: n büyüdükçe MSE → 0.") +
     fm(r"\[Var\Big(\sum a_iX_i\Big)=\sum a_i^2\,\sigma^2\ \text{(unabh.)}\qquad Var(\bar X)=\frac{\sigma^2}n\qquad MSE=Bias^2+Var\qquad\text{konsistent: }MSE\to0\]") +
     vg("\\(\\bar X\\) gegen \\(\\frac{X_1+X_2}{2}\\)", r'''<div class="fm">\(Var(\bar X)=\frac{\sigma^2}n\to0\) → konsistent · \(Var\left(\frac{X_1+X_2}2\right)=\frac14(\sigma^2+\sigma^2)=\frac{\sigma^2}2\) – hängt nicht von n ab → nicht konsistent; für n > 2 ist \(\bar X\) besser.</div>''') +
     vg("MSE mit Zahlen", r'''<div class="fm">A: Bias 0, Var 4 → MSE = 4 &nbsp;·&nbsp; B: Bias 1, Var 2 → MSE = 1 + 2 = 3 → <b>B ist besser</b>, obwohl verzerrt.</div>''') +
     chk("§17a", r"\(\hat\mu=\frac{3X_1+X_2}{4}\): Ist er erwartungstreu? Berechnen Sie \(Var(\hat\mu)\) und vergleichen Sie mit \(\frac{X_1+X_2}{2}\).", 3,
         sol=r"\(E=\frac{3\mu+\mu}4=\mu\) ✓ · \(Var=\frac{9+1}{16}\sigma^2=0.625\sigma^2\) · \(Var\left(\frac{X_1+X_2}2\right)=0.5\sigma^2\) → der Mittelwert ist effizienter") +
     chk("§17b", r"Schätzer C: Bias 2, Varianz 0.5. Schätzer D: Bias 0, Varianz 5. Welcher hat den kleineren MSE?", 1,
         sol=r"MSE(C) = 4 + 0.5 = 4.5 < MSE(D) = 5 → C") +
     falle("„Ein erwartungstreuer Schätzer hat immer den kleineren MSE“ ist falsch (beliebte Multiple-Choice-Aussage)."),
     level="lv4", nxt="Weiter: Maximum-Likelihood")

page(kick("§ 18", "ML-Rezept · Teil 1/2") + r'''
<h1>Welcher Parameter macht die Daten <em>am wahrscheinlichsten?</em></h1>
<p class="lead">Maximum-Likelihood ist in jeder Klausur ~10 Punkte wert und läuft immer nach demselben Rezept. Du brauchst nur Log-Regeln (Tag-2-Werkzeug) und eine Ableitung.</p>
''' + TR("ML her sınavda yaklaşık 10 puan ve hep aynı tarifle çözülür. Sadece log kuralları ve bir türev lazım. log = ln!") + r'''
<div class="grid2" style="grid-template-columns:1.1fr 1fr;margin-top:2mm">
 <div class="card gold"><div class="lab" style="margin-top:0">Die 6 Schritte</div><ol class="num" style="font-size:9.2pt">
  <li><b>Likelihood:</b> \(L(\vartheta)=\prod_{i=1}^n f(x_i;\vartheta)\) – vereinfachen.</li><li><b>Log:</b> \(\ell(\vartheta)=\log L\) – Produkt wird Summe.</li>
  <li><b>Ableiten</b> nach dem Parameter.</li><li><b>Null setzen:</b> \(\ell'(\hat\vartheta)\overset!=0\).</li><li><b>Auflösen</b> → \(\hat\vartheta\) (mit Dach, mit \(\bar x\)).</li>
  <li><b>2. Ableitung</b> \(&lt;0\) → Maximum.</li></ol></div>
 <div class="card"><div class="lab" style="margin-top:0">Werkzeug</div><div style="font-size:9pt">
  \(\prod c=c^n\) · \(\prod a^{x_i}=a^{\sum x_i}\) · \(\prod e^{-\lambda x_i}=e^{-\lambda\sum x_i}\)<br>\(\log(ab)=\log a+\log b\) · \(\log a^b=b\log a\) · \(\log e^x=x\)<br>
  \((\log\vartheta)'=\frac1\vartheta\) · \((\log(1-\vartheta))'=\frac{-1}{1-\vartheta}\) · \(\left(\frac n\vartheta\right)'=-\frac n{\vartheta^2}\)<br>Terme ohne Parameter → Ableitung 0</div></div>
</div>
''' + vg("Poisson, allgemein", r'''<div class="fm">\(L(\lambda)=\prod\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}=\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}\qquad\ell(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log(x_i!)\)</div>
<div class="fm">\(\ell'(\lambda)=\frac{\sum x_i}{\lambda}-n\overset!=0\ \Rightarrow\ \hat\lambda=\frac{\sum x_i}{n}=\bar x\qquad\ell''(\lambda)=-\frac{\sum x_i}{\lambda^2}&lt;0\ \Rightarrow\ \text{Maximum}\)</div>''') +
     falle(r"\(\prod_{i=1}^n\lambda=\lambda^n\), nicht \(n\lambda\). Und \(\log(\lambda^n)=n\log\lambda\) – genau hier verlieren die meisten den ersten Punkt."),
     level="lv4", nxt="Weiter: ML mit Zahlen")

page(kick("§ 18", "ML mit Zahlen · Teil 2/2", xp="2 × 5 XP") + r'''
<h1>Vom Rezept zur <em>Zahl.</em></h1>
''' + TR("Somut verilerle: önce genel tahminciyi bul, sonra sayıları yerine koy. Kontrol: Poisson'da λ̂ = x̄, üstelde λ̂ = 1/x̄.") +
     vg("Exponentialverteilung (= Weibull mit r = 1), Daten 2, 4, 6", r'''<div class="fm">\(L(\lambda)=\prod\lambda e^{-\lambda x_i}=\lambda^ne^{-\lambda\sum x_i}\qquad\ell(\lambda)=n\log\lambda-\lambda\sum x_i\)</div>
<div class="fm">\(\ell'(\lambda)=\frac n\lambda-\sum x_i\overset!=0\Rightarrow\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}=\frac{3}{12}=\mathbf{0.25}\qquad\ell''=-\frac{n}{\lambda^2}&lt;0\)</div>''') +
     vg("Likelihood für konkrete Werte (Poisson, Daten 2, 0, 3, 1)", r'''<div class="fm">\(L(\lambda)=\frac{\lambda^2e^{-\lambda}}{2!}\cdot\frac{e^{-\lambda}}{0!}\cdot\frac{\lambda^3e^{-\lambda}}{3!}\cdot\frac{\lambda e^{-\lambda}}{1!}=\frac{\lambda^6e^{-4\lambda}}{12}\Rightarrow\ell'=\frac6\lambda-4=0\Rightarrow\hat\lambda=\mathbf{1.5}\)</div>''') +
     ks("„Der Maximum-Likelihood-Schätzer ist \\(\\hat\\lambda=1/\\bar x\\); für die Stichprobe ergibt sich \\(\\hat\\lambda=0.25\\). Da \\(\\ell''(\\lambda)=-n/\\lambda^2&lt;0\\), liegt ein Maximum vor.“") +
     chk("§18a", r"Bernoulli: Daten 1, 0, 1, 1, 0 mit \(P(X=1)=\pi\). Stellen Sie \(\ell(\pi)\) auf und bestimmen Sie \(\hat\pi\).", 3,
         sol=r"\(L=\pi^3(1-\pi)^2\), \(\ell=3\log\pi+2\log(1-\pi)\), \(\ell'=\frac3\pi-\frac2{1-\pi}=0\Rightarrow3(1-\pi)=2\pi\Rightarrow\hat\pi=0.6\)") +
     chk("§18b", r"Bringen Sie in die richtige Reihenfolge (Testat 5): (A) Maximum prüfen (B) Likelihood aufstellen (C) ableiten und null setzen (D) Verteilungsmodell wählen (E) auflösen (F) logarithmieren.", 1,
         sol=r"D → B → F → C → E → A"),
     level="lv4", nxt="Weiter: ML-Klassiker")

page(kick("§ 19", "ML-Klassiker · Teil 1/2") + r'''
<h1>Die Ergebnisse, die du <em>wiedererkennst.</em></h1>
<p class="lead">Viele ML-Aufgaben sind Varianten derselben Familien. Kennst du das Endergebnis, kannst du deine Rechnung sofort kontrollieren.</p>
''' + TR("ML sorularının çoğu aynı ailelerin varyasyonları. Sonucu bilirsen hesabını hemen kontrol edersin.") + r'''
<table class="tb" style="margin-top:2mm"><tr><th>Modell</th><th>Log-Likelihood</th><th>ML-Schätzer</th></tr>
<tr><td>Poisson \(Po(\lambda)\)</td><td>\(\sum x_i\log\lambda-n\lambda+\text{const}\)</td><td>\(\hat\lambda=\bar x\)</td></tr>
<tr><td>Bernoulli \(Be(\pi)\)</td><td>\(k\log\pi+(n-k)\log(1-\pi)\)</td><td>\(\hat\pi=\frac kn=\bar x\)</td></tr>
<tr><td>Exponential / Weibull r = 1</td><td>\(n\log\lambda-\lambda\sum x_i\)</td><td>\(\hat\lambda=\frac1{\bar x}\)</td></tr>
<tr><td>geometrisch \(\theta(1-\theta)^x\)</td><td>\(n\log\theta+\sum x_i\log(1-\theta)\)</td><td>\(\hat\theta=\frac1{1+\bar x}\)</td></tr>
<tr><td>Normal, μ (σ bekannt)</td><td>\(-\frac1{2\sigma^2}\sum(x_i-\mu)^2+\text{const}\)</td><td>\(\hat\mu=\bar x\)</td></tr>
<tr><td>Normal, σ² (μ bekannt)</td><td>\(-\frac n2\log\sigma^2-\frac{\sum(x_i-\mu)^2}{2\sigma^2}+\text{const}\)</td><td>\(\hat\sigma^2=\frac1n\sum(x_i-\mu)^2\)</td></tr></table>
''' + vg("Geometrisch, Testat 5 · Daten 3, 0, 5, 2", r'''<div class="fm">\(L(\theta)=\theta^4(1-\theta)^{3+0+5+2}=\theta^4(1-\theta)^{10}\qquad\ell'=\frac4\theta-\frac{10}{1-\theta}\overset!=0\)</div>
<div class="fm">\(4(1-\hat\theta)=10\hat\theta\Rightarrow\hat\theta=\frac4{14}=\frac27=\mathbf{0.286}\qquad\text{Kontrolle: }\frac1{1+\bar x}=\frac1{1+2.5}=0.286\ ✓\)</div>''') +
     tip(r"Bei \((1-\theta)\) im Nenner: über Kreuz multiplizieren, alle θ auf eine Seite, ausklammern. So vermeidest du Bruch-Chaos.", "Auflösen"),
     level="lv4", nxt="Weiter: spezielle Dichten")

page(kick("§ 19", "Spezielle Dichten · Teil 2/2", xp="+5 XP") + r'''
<h1>Unbekannte Dichte? <em>Gleiches Rezept.</em></h1>
<p class="lead">In der Klausur steht oft eine Dichte, die du nie gesehen hast. Kein Problem: Du brauchst sie nicht zu kennen – Rezept anwenden, Log-Regeln nutzen, fertig.</p>
''' + TR("Sınavda hiç görmediğin bir yoğunluk olabilir. Tanıman gerekmiyor: tarifi uygula, log kurallarını kullan, bitti.") +
     vg("\\(f(x;\\theta)=\\theta^2x\\,e^{-\\theta x}\\) für x > 0 · Daten 1, 2, 3", r'''<div class="fm">\(L(\theta)=\theta^{2n}\prod x_i\,e^{-\theta\sum x_i}\qquad\ell(\theta)=2n\log\theta+\sum\log x_i-\theta\sum x_i\)</div>
<div class="fm">\(\ell'(\theta)=\frac{2n}\theta-\sum x_i\overset!=0\Rightarrow\hat\theta=\frac{2n}{\sum x_i}=\frac2{\bar x}=\frac22=\mathbf1\qquad\ell''=-\frac{2n}{\theta^2}&lt;0\)</div>
<div class="small">\(\sum\log x_i\) enthält kein θ → in der Log-Likelihood hinschreiben, beim Ableiten fällt es weg.</div>''') +
     vg("Übungsklausur ML, Aufgabe 3 · \\(f(x)=\\frac{\\beta\\log2}{2^{x\\beta}}\\)", r'''<div class="fm">\(\ell(\beta)=n\log(\log2)+n\log\beta-\beta\log2\sum x_i\qquad\ell'=\frac n\beta-\log2\sum x_i\overset!=0\Rightarrow\hat\beta=\frac{1}{\log(2)\,\bar x}\)</div>''') +
     chk("§19", r"Für die Dichte aus Übungsklausur A3 und die Daten 0.5, 1, 1.5, 3: Berechnen Sie \(\hat\beta\). Prüfen Sie auch die 2. Ableitung.", 2,
         sol=r"\(\bar x=1.5\): \(\hat\beta=\frac1{0.6931\cdot1.5}=0.962\) · \(\ell''(\beta)=-\frac n{\beta^2}<0\) → Maximum") +
     falle(r"Mit dem Taschenrechner <b>ln</b> benutzen: \(\log2=0.6931\). Mit log₁₀ (0.3010) wird jedes Ergebnis falsch – dein E(log X)-Fehler.") +
     tip(r"\(\log(2^{-x\beta})=-x\beta\log2\) – der Exponent wandert nach vorne. Das ist der Trick bei allen „Parameter im Exponenten“-Dichten.", "Log-Trick"),
     level="lv4", nxt="Weiter: Mission 2")

mission(2, "Maximum-Likelihood komplett", 40,
        "Eine ML-Aufgabe wie in der Probeklausur – mit Likelihood, Log-Likelihood, Schätzer, 2. Ableitung und Zahlenwert. Ziel: 12 Minuten.",
        "Probeklausur'daki gibi bir ML sorusu: likelihood, log-likelihood, tahminci, ikinci türev ve sayısal değer. Hedef: 12 dakika.",
        r'''Die Dichte einer Zufallsvariable X sei \(f(x;a)=a\,x^{-(a+1)}\) für \(x\ge1\), 0 sonst, mit \(a&gt;0\). Gegeben ist eine iid-Stichprobe \(X_1,\dots,X_n\).<br>
(a) Stellen Sie die Likelihood und die Log-Likelihood auf und vereinfachen Sie. <b>(4 P)</b><br>(b) Bestimmen Sie den ML-Schätzer \(\hat a\). <b>(3 P)</b><br>
(c) Prüfen Sie die Bedingung zweiter Ordnung. <b>(2 P)</b><br>(d) Berechnen Sie den Schätzwert für die Stichprobe 2, 4, 8. <b>(1 P)</b>''',
        "Tag 2 · Mission 2", "lv4", "Level 4 geschafft · Pause!")

# ======================================================================
# Finale
lvl("F", "Training &amp; <em>Boss</em>",
    "Jetzt wird gemischt – wie in der Klausur, wo kein Kapitel angekündigt wird. Erst acht schnelle Mini-Fälle, dann der Boss: die Aufgaben 6–8 deiner Probeklausur 2.",
    "Şimdi karışık – sınavda hangi konunun geleceği söylenmez. Önce sekiz hızlı mini vaka, sonra Boss: Probeklausur 2'nin 6–8. soruları.",
    '<span class="chip">3 Stationen</span><span class="chip">60 min</span><span class="chip f">70 XP</span>',
    [("Mini-Fälle", "8 gemischte Aufgaben, je 2 Minuten", "§ 20"), ("Boss · Probeklausur 2 A6–A8", "23 Punkte, 30 Minuten, ohne Hilfe", "40 XP"),
     ("Tagesabschluss", "Medaillen, XP-Bilanz, Vorschau Tag 3", "✓")],
    "Nach dem Boss: Der Abend gehört dir. Fotos an Claude schicken nicht vergessen!", "fin", "Finale · Start")

minis = [
    (r"\(f(x)=c\) auf [1, 5]. Bestimmen Sie c und \(E(X)\).", r"\(4c=1\Rightarrow c=\frac14\) · \(E(X)=3\) (Mitte des Rechtecks)"),
    (r"\(X\sim Po(1.5)\). \(P(X\ge1)=\,?\)", r"\(1-e^{-1.5}=0.777\)"),
    (r"\(X\sim B(4;\ 0.5)\). \(P(X=2)=\,?\)", r"\(\binom42\cdot0.5^4=\frac6{16}=0.375\)"),
    (r"\(X\sim N(20,\,25)\). \(P(X&gt;30)=\,?\)", r"\(\sigma=5\): \(1-\Phi(2)=0.023\)"),
    (r"Wartezeit exponentialverteilt, Mittel 10 Minuten. \(P(X&gt;10)=\,?\)", r"\(e^{-1}=0.368\)"),
    (r"\(E(X)=2,\ Var(X)=3\). \(E(4-2X)\) und \(Var(4-2X)\)?", r"\(4-4=0\) · \((-2)^2\cdot3=12\)"),
    (r"\(E(X_i)=\mu\). Bias von \(\hat\mu=\frac{X_1+X_2+X_3}{3}+1\)?", r"\(E(\hat\mu)=\mu+1\) → Bias = 1"),
    (r"Poisson-Daten 1, 3, 2. ML-Schätzwert \(\hat\lambda\)?", r"\(\hat\lambda=\bar x=2\)")]
for part in (0, 1):
    body = kick("§ 20", "Mini-Fälle · Teil %d/2" % (part + 1), xp="4 × 5 XP")
    if part == 0:
        body += r'''<h1>Acht Fälle, je <em>zwei Minuten.</em></h1><p class="lead">Stoppuhr an. Erst das Modell oder die Regel erkennen, dann rechnen, dann 10-Sekunden-Kontrolle. Lösungen im Lösungsteil.</p>''' + \
            TR("Kronometreyi başlat. Önce modeli veya kuralı tanı, sonra hesapla, sonra 10 saniye kontrol. Çözümler en sonda.")
    else:
        body += r'''<h1>Halbzeit – <em>weiter so.</em></h1>''' + TR("Dört vaka daha. Her doğru cevap 5 XP.")
    for i in range(4):
        k = part * 4 + i
        body += chk("M%d" % (k + 1), minis[k][0], 2, sol=minis[k][1])
    if part == 1:
        body += tip("Alle acht richtig in unter 16 Minuten? Dann bist du bereit für den Boss. Weniger als sechs? Die falschen Paragraphen noch einmal kurz lesen – das ist kein Rückschritt, das ist Training.", "Bereit für den Boss?")
    page(body, level="fin", nxt="Weiter: Mini-Fälle" if part == 0 else "Weiter: Der Boss")

page(kick("★", "Boss-Kampf", xp="bis +40 XP") + r'''
<h1>Der <em>Boss:</em> Probeklausur 2, Aufgaben 6–8.</h1>
<p class="lead">Du kennst Aufgabe 6 schon – damals 2 von 8 Punkten. Heute zeigst du, was sich verändert hat. Dazu kommen Aufgabe 7 (Maximum-Likelihood) und Aufgabe 8 (Schätzer), die du gestern noch nicht konntest.</p>
''' + TR("6. soruyu biliyorsun – o zaman 8'de 2 puan. Bugün neyin değiştiğini gösteriyorsun. Üstüne 7 (ML) ve 8 (tahminci) geliyor; dün bunları bilmiyordun.") + r'''
<div class="grid3" style="margin-top:3mm">
 <div class="card"><div class="stat" style="border:0;padding:0"><div class="n">23</div><div class="t">Punkte · A6 8 · A7 10 · A8 5</div></div></div>
 <div class="card"><div class="stat" style="border:0;padding:0"><div class="n">30′</div><div class="t">Zeit · Stoppuhr</div></div></div>
 <div class="card ink"><div class="stat" style="border:0;padding:0"><div class="n" style="color:var(--gold2)">0</div><div class="t">Hilfsmittel außer Taschenrechner</div></div></div>
</div>
<div class="card ink" style="margin-top:3mm"><div class="lab" style="margin-top:0">Regeln des Boss-Kampfs</div>
<ol class="num" style="font-size:9.4pt;color:#efe8da"><li>Druck die Seiten 7–9 von <b>Probeklausur2_TeilA.pdf</b> aus (oder nimm ein leeres Blatt).</li>
<li>Kein Blick in dieses Heft, keine Formelsammlung. Nur Taschenrechner.</li><li>Nach 30 Minuten: Stift weg. Was nicht fertig ist, bleibt offen.</li>
<li>Fotos an Claude mit <b>„Tag 2 · Boss“</b>. Du bekommst Punkte wie in der Klausur und die Fehler-Muster im Vergleich zu gestern.</li></ol></div>
<div class="lab" style="margin-top:4mm">Boss-Belohnung</div>
<table class="tb"><tr><td>≥ 20 von 23 Punkten</td><td>Boss besiegt · <b>40 XP</b> + Medaille „Boss besiegt“</td></tr>
<tr><td>15–19 Punkte</td><td>Boss angeschlagen · <b>28 XP</b></td></tr><tr><td>10–14 Punkte</td><td>Boss verwundet · <b>16 XP</b></td></tr>
<tr><td>unter 10 Punkte</td><td>Revanche morgen früh · <b>5 XP</b> fürs Antreten</td></tr></table>
''' + tip("Bei jeder Teilaufgabe zuerst die Formel allgemein hinschreiben – das bringt fast immer schon den ersten Punkt, auch wenn die Rechnung danach hakt.", "Taktik"),
     level="fin", nxt="Weiter: Tagesabschluss")

medals = [("Fehler-Detox", "Level 1 geschafft"), ("Integral-Ass", "Integral-Drill 6/6"), ("Dichte-Profi", "Mission 1 ≥ 75 %"), ("Modell-Detektiv", "§ 10: 6/6 erkannt"),
          ("Normal-Navigator", "§ 14 ohne Fehler"), ("Schätzer-Prüfer", "§ 16 beide Checks"), ("Likelihood-Profi", "Mission 2 ≥ 75 %"), ("Boss besiegt", "≥ 20/23 Punkte")]
page(kick("✓", "Tagesabschluss") + r'''
<h1>Tag 2 <em>geschafft.</em></h1>
<p class="lead">Zähl deine XP, kreuz deine Medaillen an und schick die drei Fotos an Claude. Morgen früh beginnt Tag 3 mit deinem Feedback.</p>
''' + TR("XP'lerini say, madalyalarını işaretle ve üç fotoğrafı Claude'a gönder. Yarın sabah Tag 3 senin geri bildiriminle başlıyor.") +
     '<div class="lab">Medaillen · Tag 2</div><div class="grid4">' + "".join(
         '<div class="card" style="text-align:center;padding:2.4mm"><div style="width:11mm;height:11mm;border-radius:50%%;border:1.6px solid var(--gold);margin:0 auto 1.4mm;'
         'display:flex;align-items:center;justify-content:center;font-size:12pt;color:var(--gold)">★</div><b style="font-size:8.8pt">%s</b><div class="small" style="font-size:7.2pt">%s</div>'
         '<div class="small" style="font-size:7.2pt;margin-top:1mm"><span class="box"></span>freigeschaltet</div></div>' % m for m in medals) + '</div>' + r'''
<div class="grid2" style="margin-top:4mm">
 <div class="card ink"><div class="lab" style="margin-top:0">Heute Abend an Claude senden</div>
  <div style="font-size:9.2pt"><span class="box"></span>Mission 1 · „Tag 2 · Mission 1“<br><span class="box"></span>Mission 2 · „Tag 2 · Mission 2“<br><span class="box"></span>Boss · „Tag 2 · Boss“</div>
  <div class="small" style="color:#b9ae99;margin-top:1.4mm">Du bekommst Punkte, Notentendenz und deine Fehler-Muster im Vergleich zu gestern.</div></div>
 <div class="card"><div class="lab" style="margin-top:0">Deine XP heute</div>
  <div style="display:flex;align-items:flex-end;gap:3mm"><div style="border-bottom:1px solid #b8b0a0;width:28mm;height:12mm"></div><div style="font-family:Cormorant Garamond,serif;font-size:18pt">/ 370 XP</div></div>
  <div class="small" style="margin-top:1.4mm">Rang: <span class="box"></span>Zufalls-Neuling <span class="box"></span>Dichte-Scout <span class="box"></span>Likelihood-Profi <span class="box"></span>Klausur-Maschine</div></div>
</div>
<div class="card gold" style="margin-top:3mm"><div class="lab" style="margin-top:0">Morgen · Tag 3 · Schätzen &amp; Testen</div>
<div style="font-size:9.2pt">Konfidenzintervalle (μ, Anteil, Varianz) · Hypothesen aus dem Text · Gauß-, t-, Binomial-, χ²-Tests · lineare Regression (dein PK2-A3c) · Probeklausur 2 A9 als Boss. Danach kennst du den <b>gesamten</b> Klausurstoff.</div></div>
<div class="tip"><b>Morgen früh · 10 Minuten</b>Formeln aus Level 2–4 auf ein leeres Blatt schreiben, ohne nachzusehen. Was fehlt, kommt auf dein A4-Blatt.</div>
''', level="fin", nxt="Weiter: Lösungsteil")

# ======================================================================
# Lösungsteil (automatisch aus allen Checks)
MISSION_SOL = [
    ("Mission 1", r"(a) \(9c=1\Rightarrow c=\frac19\) · (b) \(F(x)=\frac{x^3}{27}\) auf [0, 3], 0 links, 1 rechts; \(P(X>2)=1-\frac8{27}=\frac{19}{27}=0.704\) · (c) \(x^3=13.5\Rightarrow x_{med}=2.381\) · (d) \(E(X)=\frac94=2.25\), \(E(X^2)=\frac{27}{5}=5.4\), \(Var(X)=5.4-5.0625=0.338\) · (e) \(E(2X+1)=5.5\), \(Var(2X+1)=4\cdot0.3375=1.35\)"),
    ("Mission 2", r"(a) \(L(a)=a^n\prod x_i^{-(a+1)}\), \(\ell(a)=n\log a-(a+1)\sum\log x_i\) · (b) \(\ell'(a)=\frac na-\sum\log x_i=0\Rightarrow\hat a=\frac n{\sum\log x_i}\) · (c) \(\ell''(a)=-\frac n{a^2}<0\) → Maximum · (d) \(\sum\log x_i=\log2+\log4+\log8=6\log2=4.159\Rightarrow\hat a=\frac3{4.159}=0.721\)"),
    ("Boss", "Die Lösungen zu Probeklausur 2 A6–A8 bekommst du von Claude zusammen mit deiner Bewertung – damit du sie vorher nicht siehst.")]
items = SOL + MISSION_SOL
per = 15
chunks = [items[i:i + per] for i in range(0, len(items), per)]
for ci, ch in enumerate(chunks):
    body = kick("✓", "Lösungsteil · %d/%d" % (ci + 1, len(chunks)))
    if ci == 0:
        body += '<h1>Alle <em>Lösungen.</em></h1>' + TR("Önce kendin çöz, sonra burada karşılaştır. Yanlış mı? İlgili paragrafa dön ve hatanın hangi kalıba ait olduğunu not et.")
    body += '<table class="tb">' + "".join('<tr><td class="k" style="width:16mm">%s</td><td style="font-size:8.8pt">%s</td></tr>' % (n, s) for n, s in ch) + '</table>'
    page(body, level="fin", nxt="Weiter" if ci < len(chunks) - 1 else "Ende · Viel Erfolg morgen!")
