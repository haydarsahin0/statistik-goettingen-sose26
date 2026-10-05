r"""Tag 2 · neue Seiten der Überarbeitung: zwei ZV, Level-Abschlüsse, KDE/Gütekriterien, ML-Spezialfälle, Boss-Probeklausur."""
from gen_tag2 import page, kick, TR, chk, abschluss


def vg(title, body):
    return '<div class="card gold" style="margin-top:2mm"><div class="lab" style="margin-top:0">Vorgemacht · %s</div>%s</div>' % (title, body)


def fm(t):
    return '<div class="fm">%s</div>' % t


def falle(t, title="Klausur-Falle"):
    return '<div class="falle"><b>%s</b>%s</div>' % (title, t)


def tip(t, title="Merke"):
    return '<div class="tip"><b>%s</b>%s</div>' % (title, t)


def trbox(lines, title="Adım adım · Türkçe"):
    return '<div class="trbox"><div class="lab">%s</div><ol style="margin:0;padding-left:4.5mm">%s</ol></div>' % (title, "".join("<li>%s</li>" % l for l in lines))


def rbox(code_out, title="Dasselbe in R · für Teil B"):
    out = []
    for ln in code_out.strip("\n").split("\n"):
        out.append('<span class="o">%s</span>' % ln if not ln.startswith(">") else ln.replace("<", "&lt;"))
    return '<div class="rbox"><div class="lab">%s</div><pre>%s</pre></div>' % (title, "\n".join(out))


# ---------------------------------------------------------------- §11 zwei Zufallsvariablen
def p_cov():
    page(kick("§ 11", "Zwei Zufallsvariablen · gemeinsame Verteilung", rel=2) + r'''
<h1>Zwei Variablen, <em>eine Tabelle.</em></h1>
<p class="lead">Manchmal ist eine Tabelle mit \(P(X=x,\,Y=y)\) gegeben – wie die Kontingenztafel von Tag 1, nur mit Wahrscheinlichkeiten. Daraus liest du Randverteilungen, bedingte Wahrscheinlichkeiten und die Kovarianz ab.</p>
''' + TR("Bazen P(X = x, Y = y) tablosu verilir – Tag 1'deki kontenjans tablosu gibi, ama olasılıklarla. Marjinal dağılımlar, koşullu olasılıklar ve kovaryans buradan okunur.") +
         fm(r"\[P(X=x)=\sum_yP(X=x,Y=y)\qquad P(Y=y\mid X=x)=\frac{P(X=x,Y=y)}{P(X=x)}\qquad Cov(X,Y)=E(XY)-E(X)E(Y)\qquad\rho=\frac{Cov}{sd(X)\,sd(Y)}\]") +
         vg("gemeinsame Tabelle auswerten", r'''<div style="display:grid;grid-template-columns:44mm 1fr;gap:4mm;align-items:center">
<table class="tb" style="font-size:9pt;text-align:center"><tr><th></th><th>Y=0</th><th>Y=1</th><th>Σ</th></tr><tr><th>X=0</th><td>0.3</td><td>0.2</td><td><b>0.5</b></td></tr>
<tr><th>X=1</th><td>0.1</td><td>0.4</td><td><b>0.5</b></td></tr><tr><th>Σ</th><td><b>0.4</b></td><td><b>0.6</b></td><td>1</td></tr></table>
<div style="font-size:9.1pt;line-height:1.7">Rand: \(E(X)=0.5\), \(E(Y)=0.6\) · bedingt: \(P(Y=1\mid X=1)=\frac{0.4}{0.5}=0.8\)<br>
\(E(XY)=1\cdot1\cdot0.4=0.4\) (nur die Zelle mit x = y = 1 zählt) · \(Cov=0.4-0.5\cdot0.6=\mathbf{0.1}\)<br>
\(\rho=\frac{0.1}{\sqrt{0.25}\cdot\sqrt{0.24}}=\mathbf{0.408}\) · unabhängig? \(0.3\ne0.5\cdot0.4\) → <b>abhängig</b></div></div>''') +
         falle(r"Unabhängig ⇒ Cov = 0, aber Cov = 0 ⇏ unabhängig. Für Unabhängigkeit muss <b>jede</b> Zelle gleich Zeilen- mal Spaltensumme sein.") +
         chk("§11a", r"\(P(0,0)=0.2,\ P(0,1)=0.3,\ P(1,0)=0.2,\ P(1,1)=0.3\). Bestimmen Sie die Randverteilungen. Sind X und Y unabhängig? Wie groß ist \(Cov(X,Y)\)?", 2,
             sol=r"X: 0.5 / 0.5; Y: 0.4 / 0.6 · jede Zelle = Produkt der Ränder (z. B. 0.2 = 0.5 · 0.4) → unabhängig · \(Cov=E(XY)-E(X)E(Y)=0.3-0.5\cdot0.6=0\)", st=2, pts=4) +
         chk("§11b", r"Für die Tabelle im Beispiel oben: Berechnen Sie \(Var(X+Y)\).", 2,
             sol=r"\(Var(X)=0.25\), \(Var(Y)=0.6\cdot0.4=0.24\), \(Cov=0.1\) → \(Var(X+Y)=0.25+0.24+2\cdot0.1=0.69\)", st=3, pts=3),
         level="lv2", nxt="Weiter: Mission 1")


def ab2():
    abschluss("2", "lv2",
              [r"Dichte: \(f\ge0\), \(\int f=1\), \(P(X=x)=0\), \(P(a\le X\le b)=\int_a^bf(x)\,dx\)",
               r"Potenzregel \(\int x^n=\frac{x^{n+1}}{n+1}\) · Grenzen: oben minus unten · Produkte erst ausmultiplizieren",
               r"c: \(\int_{\text{Träger}}f=1\) · \(F(x)=\int_{-\infty}^xf\) (0 links, 1 rechts) · Median: \(F(x)=0.5\)",
               r"\(E(X)=\int xf\), \(E(X^2)=\int x^2f\), \(Var=E(X^2)-E(X)^2\) · diskret: Summen statt Integrale",
               r"\(E(aX+b)=aE(X)+b\), \(Var(aX+b)=a^2Var(X)\), \(Var(X\pm Y)=Var(X)+Var(Y)\pm2Cov\) · \(Cov=E(XY)-E(X)E(Y)\)"],
              [("W4", r"Level 1: \(P(A)=0.3\), \(P(B\mid A)=0.6\). Geben Sie \(P(B\mid A)\) und \(P(A\cap B)\) an.", 1, r"\(P(B\mid A)=0.6\) (ablesen) · \(P(A\cap B)=0.3\cdot0.6=0.18\)", 1),
               ("W5", r"Tag 1: \(s_{xy}=-2\), \(s_x=2\), \(s_y=4\). Berechnen und interpretieren Sie r.", 1, r"\(r=\frac{-2}{2\cdot4}=-0.25\): schwacher negativer linearer Zusammenhang", 2),
               ("W6", r"§ 7: \(f(x)=c\,x^3\) auf [0, 2]. Bestimmen Sie c.", 1, r"\(c\left[\frac{x^4}4\right]_0^2=4c=1\Rightarrow c=\frac14\)", 2)],
              "Level 2 geschafft · Pause!", "Yoğunlukla ilgili her şey A4'üne. Sonra Level 1, Tag 1 ve § 7'den birer soru – karışmasın diye.")


def ab3():
    abschluss("3", "lv3",
              [r"Binomial \(\binom nk\pi^k(1-\pi)^{n-k}\), \(E=n\pi\), \(Var=n\pi(1-\pi)\) · „mindestens 1“ = \(1-(1-\pi)^n\)",
               r"Poisson \(\frac{\lambda^k}{k!}e^{-\lambda}\), \(E=Var=\lambda\), λ auf den Zeitraum umrechnen",
               r"Gleich \(U(a,b)\): \(\frac1{b-a}\), \(E=\frac{a+b}2\), \(Var=\frac{(b-a)^2}{12}\) · Exponential: \(P(X>x)=e^{-\lambda x}\), \(E=\frac1\lambda\), Median \(\frac{\log2}\lambda\)",
               r"Normal: \(z=\frac{x-\mu}{\sigma}\) (σ = √Varianz!), \(\Phi(-z)=1-\Phi(z)\), \(x_\alpha=\mu+z_\alpha\sigma\); \(z_{0.95}=1.645\), \(z_{0.975}=1.96\)",
               r"ZGWS: \(\bar X\overset a\sim N(\mu,\frac{\sigma^2}n)\), \(\sum X_i\overset a\sim N(n\mu,n\sigma^2)\)"],
              [("W7", r"§ 9: \(f(x)=3x^2\) auf [0, 1]. Berechnen Sie \(E(X)\).", 1, r"\(\int_0^13x^3dx=\left[\frac{3x^4}4\right]_0^1=\frac34\)", 2),
               ("W8", r"Level 1: Prävalenz 5 %, Sensitivität 0.8, Spezifität 0.9. Berechnen Sie \(P(K\mid T)\).", 1, r"\(P(T)=0.8\cdot0.05+0.1\cdot0.95=0.135\) · \(P(K\mid T)=\frac{0.04}{0.135}=0.296\)", 3),
               ("W9", r"§ 10: X, Y unabhängig, \(Var(X)=1\), \(Var(Y)=2\). \(Var(2X-Y)=\,?\)", 1, r"\(4\cdot1+2=6\)", 2)],
              "Level 3 geschafft · Pause!", "Dağılım tablosu ve normal dağılım kuralları A4'üne. Sonra yoğunluk, Bayes ve varyans kuralından birer soru.")


# ---------------------------------------------------------------- §20 KDE + Gütekriterien
def p_kde():
    page(kick("§ 20", "Kerndichteschätzer · Teil 1/2", rel=2) + r'''
<h1>Die Dichte aus den <em>Daten</em> schätzen.</h1>
<p class="lead">Ein Kerndichteschätzer (KDE) ist ein „fließendes Histogramm“: Um jeden Datenpunkt legst du einen kleinen Hügel (den Kern) und addierst alle Hügel. In der Klausur rechnest du ihn an <b>einer</b> Stelle x aus.</p>
''' + TR("Çekirdek yoğunluk tahmini „kayan histogram“ gibidir: her veri noktasına küçük bir tepe koyup hepsini toplarsın. Sınavda sadece tek bir x noktasında hesaplanır.") +
         fm(r"\[\hat f(x)=\frac1{n\,b}\sum_{i=1}^nK\!\left(\frac{x-x_i}{b}\right)\qquad\text{Rechteck: }K(u)=\tfrac12\qquad\text{Epanechnikov: }K(u)=\tfrac34(1-u^2)\qquad(-1\le u<1,\ \text{sonst }0)\]") + r'''
<div class="card"><div class="lab" style="margin-top:0">Rezept</div><ol class="num" style="font-size:9.2pt"><li>Für jede Beobachtung \(u_i=\frac{x-x_i}{b}\) ausrechnen (Tabelle!).</li>
<li>Nur wenn \(-1\le u_i&lt;1\): Kern einsetzen, sonst 0. Achtung: \(u=1\) zählt <b>nicht</b>.</li><li>Alles addieren und durch \(n\cdot b\) teilen.</li></ol></div>
''' + vg("Daten 1, 2, 2.5, 4 · Stelle x = 2 · Bandweite b = 1", r'''<table class="tb" style="font-size:8.8pt;text-align:center"><tr><th>\(x_i\)</th><td>1</td><td>2</td><td>2.5</td><td>4</td></tr><tr><th>\(u_i=\frac{2-x_i}{1}\)</th><td>1</td><td>0</td><td>−0.5</td><td>−2</td></tr>
<tr><th>Rechteck K</th><td>0 (u = 1!)</td><td>0.5</td><td>0.5</td><td>0</td></tr><tr><th>Epanechnikov K</th><td>0</td><td>0.75</td><td>0.5625</td><td>0</td></tr></table>
<div class="fm">Rechteck: \(\hat f(2)=\frac{0.5+0.5}{4\cdot1}=\mathbf{0.25}\)&nbsp;&nbsp;·&nbsp;&nbsp;Epanechnikov: \(\hat f(2)=\frac{0.75+0.5625}{4\cdot1}=\mathbf{0.328}\)</div>''') +
         chk("§20a", r"Daten 2, 3, 3.5, 6, 7. Berechnen Sie den KDE an der Stelle x = 3 mit Rechteckkern und b = 1.", 2, sol=r"\(u=1,\ 0,\ -0.5,\ -3,\ -4\) → nur 3 und 3.5 zählen: \(\hat f(3)=\frac{0.5+0.5}{5\cdot1}=0.2\)", st=2, pts=3) +
         chk("§20b", r"Gleiche Daten, Stelle x = 3, Epanechnikov-Kern mit b = 1.5.", 2, sol=r"\(u=0.667,\ 0,\ -0.333,\ -2,\ -2.667\); \(K=0.417,\ 0.75,\ 0.667,\ 0,\ 0\) → \(\hat f(3)=\frac{1.833}{5\cdot1.5}=0.244\)", st=3, pts=4),
         level="lv4", nxt="Weiter: Gütekriterien")

    page(kick("§ 20", "Gütekriterien und Bias-Varianz · Teil 2/2", rel=2) + r'''
<h1>Glatt oder genau? Der <em>Trade-off.</em></h1>
<p class="lead">Histogramm und KDE haben eine Stellschraube: Klassenzahl bzw. Bandweite. Mehr Flexibilität passt sich den Daten besser an, schwankt aber stärker. Das ist der Bias-Varianz-Trade-off – und er wird gern als Lückentext oder Multiple Choice gefragt.</p>
''' + TR("Histogram ve KDE'nin bir ayarı var: sınıf sayısı veya bant genişliği. Esneklik arttıkça veriye daha iyi uyar ama daha çok dalgalanır. Bu bias-varyans dengesidir; boşluk doldurma veya çoktan seçmeli sorulur.") + r'''
<table class="tb" style="margin-top:2mm"><tr><th>Änderung</th><th>Approximationsfehler (Bias)</th><th>Schätzfehler (Varianz)</th><th>Bild</th></tr>
<tr><td>mehr Klassen / kleinere Bandweite</td><td>↓ kleiner</td><td>↑ größer</td><td>zackig, unruhig</td></tr>
<tr><td>weniger Klassen / größere Bandweite</td><td>↑ größer</td><td>↓ kleiner</td><td>glatt, Details verschwinden</td></tr>
<tr><td>mehr Daten n</td><td>unverändert</td><td>↓ kleiner</td><td>Gesamtfehler ↓</td></tr></table>
<div class="grid2" style="margin-top:3mm">
 <div class="card"><div class="lab" style="margin-top:0">Histogramm mit J Klassen</div><div style="font-size:9.2pt">hat <b>J − 1</b> freie Parameter: J Höhen, aber die Gesamtfläche muss 1 sein.</div></div>
 <div class="card"><div class="lab" style="margin-top:0">ML-Schätzer (unter Annahmen)</div><div style="font-size:9.2pt"><b>asymptotisch erwartungstreu</b> (Bias → 0) · <b>konsistent</b> (MSE → 0) · <b>asymptotisch normalverteilt</b> – aber nicht immer erwartungstreu.</div></div>
</div>
''' + chk("§20c", r"Ergänzen Sie: Für iid-Daten sind ML-Schätzer (unter Zusatzannahmen) ______ (Bias → 0 für n → ∞), ______ (MSE → 0) und ______. Wie viele freie Parameter hat ein Histogramm mit 10 Klassen?", 2,
          sol=r"asymptotisch erwartungstreu, konsistent, asymptotisch normalverteilt · 10 − 1 = 9", st=1, pts=4) +
         chk("§20d", r"Richtig oder falsch? (1) Ein erwartungstreuer Schätzer hat immer den kleineren MSE. (2) ML-Schätzer sind immer erwartungstreu. (3) \(\bar X\) ist konsistent für μ. (4) Eine größere Bandweite macht den KDE glatter.", 2,
             sol=r"(1) falsch – MSE = Bias² + Var · (2) falsch – nur asymptotisch · (3) richtig – \(Var(\bar X)=\frac{\sigma^2}n\to0\) · (4) richtig", st=2, pts=4),
         level="lv4", nxt="Weiter: Maximum-Likelihood")


# ---------------------------------------------------------------- §23 ML-Spezialfälle
def p_mlspez():
    page(kick("§ 23", "ML-Spezialfälle: σ² und Tabellen", rel=2) + r'''
<h1>Die zwei <em>Sonderfälle.</em></h1>
<p class="lead">Zwei Varianten tauchen in Tutorien und Übungsklausuren auf: ML für die Varianz einer Normalverteilung und ML, wenn die Wahrscheinlichkeiten in einer Tabelle stehen. Das Rezept bleibt dasselbe.</p>
''' + TR("Tutorial ve alıştırma sınavlarında iki varyant çıkıyor: normal dağılımın varyansı için ML ve olasılıkların bir tabloda verildiği ML. Tarif aynı kalıyor.") +
         vg("Varianz σ², μ bekannt · Trick: v = σ² als <i>einen</i> Parameter behandeln", r'''<div class="fm">\(\ell(v)=-\frac n2\log(2\pi v)-\frac{\sum(x_i-\mu)^2}{2v}\qquad\ell'(v)=-\frac n{2v}+\frac{\sum(x_i-\mu)^2}{2v^2}\overset!=0\ \Rightarrow\ \hat\sigma^2=\frac1n\sum(x_i-\mu)^2\)</div>
<div class="small">Log-Renditen \(N(0,\sigma^2)\), Daten 0.02, −0.01, 0.03, −0.02: \(\hat\sigma^2=\frac{0.0004+0.0001+0.0009+0.0004}{4}=0.00045\)</div>''') +
         vg("Wahrscheinlichkeitstabelle · \\(P(1)=\\alpha,\\ P(2)=\\alpha^2,\\ P(3)=1-\\alpha-\\alpha^2\\), Daten 1, 3, 2, 1", r'''<div class="fm">\(L=\alpha\cdot(1-\alpha-\alpha^2)\cdot\alpha^2\cdot\alpha=\alpha^4(1-\alpha-\alpha^2)\qquad\ell'=\frac4\alpha-\frac{1+2\alpha}{1-\alpha-\alpha^2}\overset!=0\)</div>
<div class="fm">\(4-4\alpha-4\alpha^2=\alpha+2\alpha^2\Rightarrow6\alpha^2+5\alpha-4=0\Rightarrow\alpha=\frac{-5\pm11}{12}\Rightarrow\hat\alpha=\mathbf{0.5}\ (\text{−}\tfrac43\text{ unmöglich})\)</div>''') +
         chk("§23a", r"\(X_i\sim N(0,\sigma^2)\), Daten 1, −1, 2, −2. Berechnen Sie den ML-Schätzwert für σ².", 1, sol=r"\(\hat\sigma^2=\frac{1+1+4+4}{4}=2.5\)", st=2, pts=2) +
         chk("§23b", r"\(P(1)=\theta,\ P(2)=2\theta,\ P(3)=1-3\theta\); Daten 1, 2, 2, 3. Stellen Sie L(θ) auf und bestimmen Sie \(\hat\theta\).", 3,
             sol=r"\(L=\theta\cdot(2\theta)^2\cdot(1-3\theta)=4\theta^3(1-3\theta)\) · \(\ell'=\frac3\theta-\frac3{1-3\theta}=0\Rightarrow1-3\theta=\theta\Rightarrow\hat\theta=\frac14\) (P(3) = 0.25 ≥ 0 ✓)", st=3, pts=5),
         level="lv4", nxt="Weiter: Mission 2")


def ab4():
    abschluss("4", "lv4",
              [r"\(Bias=E(\hat\vartheta)-\vartheta\), erwartungstreu ⇔ \(E(\hat\vartheta)=\vartheta\) · \(E(\sum a_iX_i)=\sum a_iE(X_i)\), \(E(X_1X_2)=E(X_1)E(X_2)\)",
               r"\(Var(\sum a_iX_i)=\sum a_i^2\sigma^2\), \(Var(\bar X)=\frac{\sigma^2}n\), \(MSE=Bias^2+Var\), konsistent: MSE → 0",
               r"KDE \(\hat f(x)=\frac1{nb}\sum K(\frac{x-x_i}b)\), Rechteck ½, Epanechnikov \(\frac34(1-u^2)\) auf \([-1,1)\)",
               r"ML: L → log → ableiten → 0 → auflösen → \(\ell''&lt;0\) · \(\prod c=c^n\), \(\log a^b=b\log a\)",
               r"Ergebnisse: Poisson \(\bar x\) · Bernoulli \(\bar x\) · Exponential \(\frac1{\bar x}\) · geometrisch \(\frac1{1+\bar x}\) · Normal-σ² \(\frac1n\sum(x_i-\mu)^2\)"],
              [("W10", r"§ 16: \(X\sim N(60,\,9)\). \(P(X&gt;66)=\,?\)", 1, r"\(\sigma=3\): \(1-\Phi(2)=0.023\)", 2),
               ("W11", r"§ 13: \(X\sim B(5;\ 0.2)\). \(P(X=0)=\,?\)", 1, r"\(0.8^5=0.328\)", 1),
               ("W12", r"§ 8: \(F(x)=x^2\) auf [0, 1]. Median?", 1, r"\(x^2=0.5\Rightarrow x=\sqrt{0.5}=0.707\)", 2)],
              "Level 4 geschafft · Pause!", "Tahminci ve ML kuralları A4'üne. Sonra normal dağılım, binom ve medyandan birer soru.")


# ---------------------------------------------------------------- Boss-Probeklausur (im Klausurformat)
def task(nr, pts, intro, parts):
    o = ['<div class="aufg" style="margin-top:3mm"><div class="ah"><b>Aufgabe %s</b><span class="pts">(%d Punkte)</span></div><div class="q">%s</div>' % (nr, pts, intro)]
    for lab, txt, p, h in parts:
        o.append('<div class="q" style="margin-top:1.6mm"><b>(%s)</b> %s <b style="float:right">(%d P)</b></div><div class="lk" style="height:%dmm"><span>Lösung</span></div>' % (lab, txt, p, h))
    o.append('</div>')
    return "".join(o)


def boss():
    page(kick("★", "Boss-Probeklausur · Teil 1/2", xp="bis +40 XP") + r'''
<h1>Der <em>Boss</em> – im echten Klausurformat.</h1>
<p class="lead">Drei Aufgaben, 23 Punkte, 30 Minuten, nur Taschenrechner. Aufgabe B1 ist neu (die Lösung von PK2-A6 kennst du schon), B2 und B3 sind die Aufgaben 7 und 8 deiner Probeklausur 2.</p>
''' + TR("Üç soru, 23 puan, 30 dakika, sadece hesap makinesi. B1 yeni (PK2-A6'nın çözümünü zaten biliyorsun), B2 ve B3 Probeklausur 2'nin 7. ve 8. soruları. Çözümler defterde yok – Claude'dan gelecek.") +
         r'''<div class="card ink" style="padding:2.4mm 3.4mm"><div style="font-size:9pt;color:#efe8da">Regeln: kein Blick ins Heft · Stoppuhr 30 Minuten · Lösungsweg in die Kästchen · danach Fotos an Claude mit <b>„Tag 2 · Boss“</b>. Belohnung: ≥ 20 P → 40 XP + Medaille · 15–19 → 28 XP · 10–14 → 16 XP · darunter → Revanche morgen früh.</div></div>''' +
         task("B1", 8, r"Die Zeit X (in Stunden), die ein Kurier für eine Tour braucht, sei eine stetige Zufallsvariable mit der Dichte \(f(x)=c\,(2-x)\) für \(0\le x\le2\), 0 sonst.",
              [("a", r"Bestimmen Sie c derart, dass f eine gültige Dichtefunktion ist. Geben Sie Ihren Lösungsweg an.", 2, 18),
               ("b", r"Berechnen Sie den Erwartungswert \(E(X)\).", 2, 18), ("c", r"Berechnen Sie \(P(X\le1)\).", 1, 12),
               ("d", r"Ein Quiz hat 6 Fragen mit je 3 Antwortmöglichkeiten (genau eine richtig); ein Student rät. Wie lautet die Verteilung der Anzahl Y richtiger Antworten (mit Parametern)? Berechnen Sie \(P(Y\ge5)\).", 3, 22)]),
         level="fin", nxt="Weiter: Boss · Teil 2")

    page(kick("★", "Boss-Probeklausur · Teil 2/2") +
         task("B2", 10, r"Der Anteil X einer Vorlesung, den eine zufällig ausgewählte Person tatsächlich mitschreibt, werde durch eine Zufallsvariable mit der Dichte \(f(x;\theta)=\theta\,x^{\theta-1}\) für \(0&lt;x&lt;1\) (0 sonst) mit \(\theta&gt;0\) beschrieben. Bestimmen Sie den ML-Schätzer für θ basierend auf einer iid-Stichprobe \(X_1,\dots,X_n\). <span class='small'>(= PK2, Aufgabe 7)</span>",
              [("a", r"Stellen Sie die Likelihood- und die Log-Likelihood-Funktion auf und vereinfachen Sie so weit wie möglich.", 4, 26),
               ("b", r"Bestimmen Sie den ML-Schätzer \(\hat\theta\).", 3, 20), ("c", r"Prüfen Sie die Bedingung zweiter Ordnung.", 2, 12),
               ("d", r"Berechnen Sie den Schätzwert für die Stichprobe \(x=(0.5,\ 0.8,\ 0.9,\ 0.6)\).", 1, 10)]) +
         task("B3", 5, r"Sei \(E(X)=\mu\), \(Var(X)=\sigma^2\); \(X_1,X_2,X_3\) unabhängig. \(\hat\mu_1=\frac{X_1+2X_2+X_3}{4}\), \(\hat\mu_2=\frac{X_1+X_2+X_3}{2}\). <span class='small'>(= PK2, Aufgabe 8)</span>",
              [("a", r"Prüfen Sie, ob \(\hat\mu_1\) und \(\hat\mu_2\) erwartungstreu sind; geben Sie ggf. den Bias an.", 3, 20),
               ("b", r"Berechnen Sie \(Var(\hat\mu_1)\). Ist \(\hat\mu_1\) oder \(\bar X\) vorzuziehen? Begründen Sie.", 2, 16)]),
         level="fin", nxt="Weiter: Tagesabschluss")


# ---------------------------------------------------------------- Ergänzungen für freie Flächen
import math


def svg_bars(vals, labels, title, hl=None):
    W, H, x0, y0 = 250, 120, 28, 100
    mx = max(vals); bw = (W - x0 - 10) / len(vals)
    o = ['<svg viewBox="0 0 %d %d" style="width:100%%;height:auto">' % (W, H + 6),
         '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#1d1b17"/>' % (x0, y0, W - 5, y0)]
    for i, v in enumerate(vals):
        h = (y0 - 14) * v / mx; x = x0 + i * bw + bw * .18
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x, y0 - h, bw * .64, h, "#a33a2a" if hl and i in hl else "#d9b56a"))
        o.append('<text x="%.1f" y="%d" font-size="9" fill="#1d1b17" text-anchor="middle">%s</text>' % (x + bw * .32, y0 + 11, labels[i]))
        o.append('<text x="%.1f" y="%.1f" font-size="7.5" fill="#6b665c" text-anchor="middle">%.3f</text>' % (x + bw * .32, y0 - h - 2, v))
    o.append('<text x="%d" y="10" font-size="9" fill="#a8803a">%s</text></svg>' % (x0, title))
    return "".join(o)


def svg_curve(f, a, b, title, shade=None, ymax=None, xlab="x", ticks=()):
    W, H, x0, y0 = 250, 120, 28, 100
    n = 120; xs = [a + (b - a) * i / n for i in range(n + 1)]; ys = [f(x) for x in xs]
    ym = ymax or max(ys) * 1.1
    X = lambda x: x0 + (W - x0 - 10) * (x - a) / (b - a)
    Y = lambda y: y0 - (y0 - 14) * y / ym
    pts = " ".join("%.1f,%.1f" % (X(x), Y(y)) for x, y in zip(xs, ys))
    o = ['<svg viewBox="0 0 %d %d" style="width:100%%;height:auto">' % (W, H + 6)]
    if shade:
        sx = [x for x in xs if shade[0] <= x <= shade[1]]
        poly = "%.1f,%d " % (X(sx[0]), y0) + " ".join("%.1f,%.1f" % (X(x), Y(f(x))) for x in sx) + " %.1f,%d" % (X(sx[-1]), y0)
        o.append('<polygon points="%s" fill="#f1dfb8"/>' % poly)
    o.append('<polyline points="%s" fill="none" stroke="#a8803a" stroke-width="2"/>' % pts)
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#1d1b17"/><line x1="%d" y1="%d" x2="%d" y2="8" stroke="#1d1b17"/>' % (x0, y0, W - 5, y0, x0, y0, x0))
    for t in ticks:
        o.append('<text x="%.1f" y="%d" font-size="9" fill="#1d1b17" text-anchor="middle">%s</text>' % (X(t), y0 + 11, ("%g" % t)))
    o.append('<text x="%d" y="%d" font-size="9" fill="#1d1b17">%s</text><text x="%d" y="10" font-size="9" fill="#a8803a">%s</text></svg>' % (W - 12, y0 + 11, xlab, x0 + 6, title))
    return "".join(o)


def two(left, right, w="1fr 1fr"):
    return '<div style="display:grid;grid-template-columns:%s;gap:3mm;align-items:start">%s%s</div>' % (w, left, right)


def card(svg):
    return '<div class="card" style="padding:2mm">%s</div>' % svg


def x_f():
    return chk("§8d", r"\(f(x)=\frac14\) für \(0\le x\le2\) und \(f(x)=\frac12\) für \(2&lt;x\le3\), 0 sonst. Prüfen Sie, dass f eine Dichte ist, und bestimmen Sie \(F(2.5)\) sowie den Median.", 2,
               sol=r"Fläche \(2\cdot\frac14+1\cdot\frac12=1\) ✓ · \(F(2.5)=\frac12+0.5\cdot\frac12=0.75\) · Median: \(F(2)=0.5\) → \(x_{med}=2\)", st=3, pts=4)


def x_e():
    return rbox("""> integrate(function(x) x * x/2, lower = 0, upper = 2)   # E(X) für f(x) = x/2
1.333333 with absolute error < 1.5e-14
> integrate(function(x) x/2, 0, 1)                         # P(X <= 1)
0.25 with absolute error < 2.8e-15""", "Kontrolle mit R · integrate()") + \
        chk("§9c", r"\(f(x)=\frac14\) auf [0, 4] (Gleichverteilung). Berechnen Sie \(E(X)\) per Integral.", 1, sol=r"\(\int_0^4\frac x4dx=\left[\frac{x^2}8\right]_0^4=2\) – die Mitte, wie erwartet", st=1, pts=2)


def x_var():
    return trbox([r"Önce \(E(X)\)'i bul (§ 9 sayfa 1) – sonucu kesir olarak sakla, örn. \(\frac43\).",
                  r"\(E(X^2)\): integralin içine \(x^2\cdot f(x)\) yaz, çarp, integral al.",
                  r"\(Var=E(X^2)-E(X)^2\): \(\left(\frac43\right)^2=\frac{16}9\) – ondalığa ancak en sonda çevir.",
                  r"Kontrol: Var her zaman ≥ 0. Negatif çıktıysa \(E(X^2)\)'de x'i bir kez fazla/az çarpmışsın."])


def x_binom():
    return rbox("""> dbinom(2, size = 8, prob = 0.3)        # P(X = 2)
[1] 0.2964755
> pbinom(1, size = 8, prob = 0.3)        # P(X <= 1)
[1] 0.2552983
> 1 - pbinom(4, size = 5, prob = 0.25)   # P(X > 4) = P(X = 5)
[1] 0.0009765625""")


def x_pois():
    vals = [math.exp(-2) * 2 ** k / math.factorial(k) for k in range(8)]
    return two(card(svg_bars(vals, [str(k) for k in range(8)], "Po(2): P(X = k) · rot = P(X > 2)", hl={3, 4, 5, 6, 7})),
               rbox("""> dpois(0:3, lambda = 2)
[1] 0.1353353 0.2706706 0.2706706 0.1804470
> 1 - ppois(2, lambda = 2)    # P(X > 2)
[1] 0.3233236"""), "1fr 1.05fr")


def x_unif():
    return chk("§15c", r"\(X\sim U(a,b)\) mit \(E(X)=6\) und \(Var(X)=3\). Bestimmen Sie a und b.", 2,
               sol=r"\(\frac{a+b}2=6\), \(\frac{(b-a)^2}{12}=3\Rightarrow b-a=6\) → \(a=3\), \(b=9\)", st=3, pts=3)


def x_exp():
    lam = 1 / 3
    return two(card(svg_curve(lambda x: lam * math.exp(-lam * x), 0, 14, "Exp(1/3): Fläche ab 10 = 0.036", shade=(10, 14), ticks=(0, 3, 6, 10, 14))),
               rbox("""> 1 - pexp(10, rate = 1/3)    # P(X > 10)
[1] 0.03567399
> qexp(0.5, rate = 1/3)       # Median
[1] 2.079442"""), "1fr 1.05fr")


def x_norm1():
    return rbox("""> pnorm(185, mean = 170, sd = 10)   # sd = Wurzel der Varianz!
[1] 0.9331928
> 1 - pnorm(160, 170, 10)
[1] 0.8413447
> qnorm(0.95, mean = 170, sd = 10)   # Quantil rückwärts (Teil 2)
[1] 186.4485""")


def x_norm2():
    return chk("§16c", r"Eine Anlage füllt \(N(\mu,\,16)\) ab. Wie groß muss μ sein, damit 95 % der Packungen mindestens 500 g enthalten?", 2,
               sol=r"\(P(X\ge500)=0.95\Rightarrow500=\mu-1.645\cdot4\Rightarrow\mu=506.58\)", st=3, pts=3)


def x_zgws():
    return rbox("""> set.seed(1)
> m <- replicate(1000, mean(runif(100, 0, 8)))   # 1000 Mittelwerte aus U(0, 8), n = 100
> round(mean(m), 3)                               # ≈ E(X) = 4
[1] 3.997
> hist(m, freq = FALSE)                           # Glockenform = ZGWS""", "Simulation in R · Testat-4-Typ")


def x_et():
    return chk("§18c", r"\(E(X_i)=\mu\). Sind \(\bar X\) und \(\frac{X_1+X_2}2\) erwartungstreu für μ?", 1,
               sol=r"\(E(\bar X)=\mu\) ✓ und \(E\left(\frac{X_1+X_2}2\right)=\frac{2\mu}2=\mu\) ✓ – beide erwartungstreu (Unterschied erst bei der Varianz, § 19)", st=1, pts=2)


def x_ml1():
    return trbox([r"\(L(\lambda)\): her gözlemin olasılığını çarp. \(\lambda\) n kez çarpılır → \(\lambda^{\sum x_i}\), \(e^{-\lambda}\) n kez → \(e^{-n\lambda}\).",
                  r"log al: çarpım → toplam, üs öne iner: \(\log\lambda^{\sum x_i}=\sum x_i\log\lambda\), \(\log e^{-n\lambda}=-n\lambda\).",
                  r"λ'ya göre türev: \(\sum x_i\cdot\frac1\lambda\); \(-n\lambda\) → \(-n\); \(\log(x_i!)\) λ içermez → 0.",
                  r"0'a eşitle, λ'yı yalnız bırak: \(\hat\lambda=\frac{\sum x_i}n=\bar x\). Şapkayı unutma!",
                  r"İkinci türev \(-\frac{\sum x_i}{\lambda^2}&lt;0\) → maksimum. Gerekçe cümlesi: „da \(\sum x_i&gt;0\) und \(\lambda^2&gt;0\)“."], "Poisson-ML satır satır · Türkçe")


def x_ml2():
    L = lambda l: l ** 6 * math.exp(-4 * l) / 12
    return two(card(svg_curve(L, 0.01, 4, "L(λ) für Daten 2, 0, 3, 1 · Maximum bei 1.5", ticks=(0, 1, 1.5, 2, 3, 4), xlab="λ")),
               rbox("""> x <- c(2, 0, 3, 1)
> logL <- function(l) sum(dpois(x, l, log = TRUE))
> optimise(logL, c(0.1, 10), maximum = TRUE)$maximum
[1] 1.500005"""), "1fr 1.05fr")


def x_ml3():
    return chk("§22b", r"Exponentialverteilung, Daten 1, 2, 3. Bestimmen Sie den ML-Schätzwert \(\hat\lambda\) (Tabelle oben benutzen, dann zur Kontrolle herleiten).", 2,
               sol=r"\(\hat\lambda=\frac1{\bar x}=\frac12=0.5\) · Herleitung: \(\ell=3\log\lambda-6\lambda\), \(\ell'=\frac3\lambda-6=0\Rightarrow\hat\lambda=0.5\)", st=2, pts=3)
