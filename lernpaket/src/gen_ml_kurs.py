# ML-Kurs: Lerneinheit -> passende Übungen (Klausurlayout) -> ... -> komplette Klausuraufgaben -> Lösungen
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_ml_klausur as K  # liefert A, aufgabe(), uniform()

CSS = r'''<style>
.lern{border:2px solid #1f4e79;border-radius:10px;margin:0 0 5mm;overflow:hidden;break-inside:auto}
.lern .lh1{background:#1f4e79;color:#fff;padding:2.5mm 4mm;font-weight:800;font-size:1.05rem;display:flex;justify-content:space-between}
.lern .lh1 small{font-weight:600;opacity:.85}
.lern .lb2{padding:2mm 4mm 3mm;font-size:.9rem;line-height:1.5}
.lern h4{margin:2.5mm 0 1mm;color:#1f4e79;font-size:.95rem}
.lern .tr{display:block;background:#e3f4f2;border-left:3px solid #00796b;padding:1.5mm 3mm;margin:2mm 0;font-style:italic;color:#0f4f47;border-radius:0 6px 6px 0}
.lern .vg{background:#f4f6fa;border-left:3px solid #1f4e79;padding:1.5mm 3mm;margin:2mm 0;border-radius:0 6px 6px 0}
.lern .vg b.t{display:block;color:#1f4e79;font-size:.75rem;letter-spacing:.1em;text-transform:uppercase}
.lern .fe{background:#fdeeec;border-left:3px solid #c62828;padding:1.5mm 3mm;margin:2mm 0;border-radius:0 6px 6px 0}
.lern table{border-collapse:collapse;width:100%;font-size:.86rem;margin:1.5mm 0}
.lern td,.lern th{border:1px solid #cfd6e0;padding:1mm 2mm;text-align:left}
.lern th{background:#e8eef6}
.ueb h2{border-bottom-color:#a8823a!important;color:#7a5d22!important}
.ueb .lk.s{height:13mm}
.unit-tag{display:inline-block;background:#a8823a;color:#fff;border-radius:4px;padding:0 6px;font-size:.7rem;margin-right:6px;vertical-align:middle}
.loesk h3{color:#2f6b3a}
</style>'''

def lern(nr, title, minutes, html):
    return f'<div class="lern kl-pb"><div class="lh1"><span>Lerneinheit {nr} · {title}</span><small>ca. {minutes} min</small></div><div class="lb2">{html}</div></div>'

def uebung(nr, title, items, pts_each=1):
    lis = ''.join(f'<li><span class="lb">({chr(97+k)})</span>{t} <span class="pt">({pts_each} P)</span><div class="lk s"></div></li>' for k, (t, _) in enumerate(items))
    return f'<div class="kl-auf ueb"><h2><span><span class="unit-tag">E{nr}</span>Übung {nr}: {title}</span><span>({pts_each*len(items)} Punkte)</span></h2><ol class="tl">{lis}</ol></div>'

U = {}
# ---------- Einheit 1: Likelihood = Produkt
L1 = r'''
<h4>Worum geht es?</h4>
Wir haben eine Dichte \(f(x;\theta)\) mit einem <b>unbekannten Parameter</b> \(\theta\) (oder \(\lambda\), \(\pi\), …) und Beobachtungen \(x_1,\dots,x_n\). Gesucht: der Wert von \(\theta\), der die Daten <b>am wahrscheinlichsten</b> macht.
<span class="tr">Elimizde bir formül var, içinde bilinmeyen bir sayı (θ) var. Hangi θ, elimizdeki verileri en olası yapar? Onu arıyoruz.</span>
<h4>Schritt ①: Die Likelihood ist ein PRODUKT</h4>
\[L(\theta)=\prod_{i=1}^n f(x_i;\theta)=f(x_1;\theta)\cdot f(x_2;\theta)\cdots f(x_n;\theta)\]
<span class="tr">Her gözlem için f'yi yaz (x yerine xᵢ) ve hepsini ÇARP. Bağımsız olayların olasılıkları çarpılır, zar gibi.</span>
<h4>Wie fasse ich das Produkt zusammen? Faktor für Faktor!</h4>
<table><tr><th>Faktor in \(f\)</th><th>wird im Produkt zu</th><th>Grund</th></tr>
<tr><td>\(\lambda\) (Parameter)</td><td>\(\lambda^n\)</td><td>\(n\)-mal derselbe Faktor</td></tr>
<tr><td>\(\lambda^2\), \(\lambda^3\)</td><td>\(\lambda^{2n}\), \(\lambda^{3n}\)</td><td>\((\lambda^2)^n=\lambda^{2n}\)</td></tr>
<tr><td>\(\frac1\theta\)</td><td>\(\theta^{-n}\)</td><td>\(\frac1\theta=\theta^{-1}\)</td></tr>
<tr><td>Zahl, z. B. \(2\)</td><td>\(2^n\)</td><td>\(n\)-mal</td></tr>
<tr><td>\(x\), \(x^2\)</td><td>\(\prod x_i\), \(\prod x_i^2\)</td><td>jedes \(x_i\) ist anders → stehen lassen</td></tr>
<tr><td>\(e^{-\lambda x}\)</td><td>\(e^{-\lambda\sum x_i}\)</td><td>\(e^a\cdot e^b=e^{a+b}\)</td></tr>
<tr><td>\(x^{\theta-1}\)</td><td>\(\big(\prod x_i\big)^{\theta-1}\)</td><td>gleicher Exponent</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(f(x;\lambda)=\lambda^2x\,e^{-\lambda x}\):&nbsp;&nbsp;&nbsp;\(L(\lambda)=\prod_{i=1}^n\lambda^2x_ie^{-\lambda x_i}=\lambda^{2n}\cdot\Big(\prod x_i\Big)\cdot e^{-\lambda\sum x_i}\)</div>
<div class="fe">⚠ Nie eine Summe \(\sum f(x_i)\) – immer das Produkt \(\prod\)!</div>'''
U[1] = [(r'\(f(x;\lambda)=\lambda e^{-\lambda x}\).&nbsp;&nbsp;&nbsp;\(L(\lambda)=\)', r'\lambda^n e^{-\lambda\sum x_i}'),
        (r'\(f(x;\theta)=\theta x^{\theta-1}\).&nbsp;&nbsp;&nbsp;\(L(\theta)=\)', r'\theta^n\big(\prod x_i\big)^{\theta-1}'),
        (r'\(f(x;\theta)=\frac1\theta e^{-x/\theta}\).&nbsp;&nbsp;&nbsp;\(L(\theta)=\)', r'\theta^{-n}e^{-\sum x_i/\theta}'),
        (r'\(f(x;\lambda)=3\lambda x^2e^{-\lambda x^3}\).&nbsp;&nbsp;&nbsp;\(L(\lambda)=\)', r'3^n\lambda^n\big(\prod x_i^2\big)e^{-\lambda\sum x_i^3}'),
        (r'\(P(X=x)=\pi^x(1-\pi)^{1-x}\).&nbsp;&nbsp;&nbsp;\(L(\pi)=\)', r'\pi^{\sum x_i}(1-\pi)^{n-\sum x_i}')]

L2 = r'''
<h4>Schritt ②: Logarithmus nehmen</h4>
Produkte lassen sich schwer ableiten. Der Logarithmus macht aus dem Produkt eine <b>Summe</b> – und das Maximum liegt an derselben Stelle.
<span class="tr">Log almak tepe noktasının yerini değiştirmez, sadece hesabı kolaylaştırır. Çarpım → toplam olur.</span>
<h4>Die vier Log-Regeln (mehr braucht man nicht)</h4>
\[\log(a\cdot b)=\log a+\log b\qquad\log(a^k)=k\log a\qquad\log(e^{z})=z\qquad\log\Big(\prod x_i\Big)=\sum\log x_i\]
<table><tr><th>in \(L\)</th><th>in \(l=\log L\)</th></tr>
<tr><td>\(\lambda^{2n}\)</td><td>\(2n\log\lambda\)</td></tr><tr><td>\(\theta^{-n}\)</td><td>\(-n\log\theta\)</td></tr><tr><td>\(2^n\)</td><td>\(n\log2\)</td></tr>
<tr><td>\(\prod x_i\)</td><td>\(\sum\log x_i\)</td></tr><tr><td>\(\prod x_i^2\)</td><td>\(2\sum\log x_i\)</td></tr><tr><td>\(\big(\prod x_i\big)^{\theta-1}\)</td><td>\((\theta-1)\sum\log x_i\)</td></tr>
<tr><td>\(e^{-\lambda\sum x_i}\)</td><td>\(-\lambda\sum x_i\)</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(L(\lambda)=\lambda^{2n}\big(\prod x_i\big)e^{-\lambda\sum x_i}\ \Rightarrow\ l(\lambda)=2n\log\lambda+\sum\log x_i-\lambda\sum x_i\)</div>
<div class="fe">⚠ \(\log(\lambda^{2n})\) ist \(2n\log\lambda\) – nicht \(\log(2n\lambda)\)! Jeder Faktor von \(L\) wird ein eigener Summand in \(l\).</div>
<span class="tr">L'deki her çarpan, l'de ayrı bir toplanan oluyor. Tabloya bak, tek tek çevir.</span>'''
U[2] = [(r'\(L(\lambda)=\lambda^ne^{-\lambda\sum x_i}\).&nbsp;&nbsp;&nbsp;\(l(\lambda)=\)', r'n\log\lambda-\lambda\sum x_i'),
        (r'\(L(\theta)=\theta^n\big(\prod x_i\big)^{\theta-1}\).&nbsp;&nbsp;&nbsp;\(l(\theta)=\)', r'n\log\theta+(\theta-1)\sum\log x_i'),
        (r'\(L(\theta)=\theta^{-n}e^{-\sum x_i/\theta}\).&nbsp;&nbsp;&nbsp;\(l(\theta)=\)', r'-n\log\theta-\frac{\sum x_i}{\theta}'),
        (r'\(L(\lambda)=3^n\lambda^n\big(\prod x_i^2\big)e^{-\lambda\sum x_i^3}\).&nbsp;&nbsp;&nbsp;\(l(\lambda)=\)', r'n\log3+n\log\lambda+2\sum\log x_i-\lambda\sum x_i^3')]

L3 = r'''
<h4>Schritt ③: Ableiten nach dem Parameter</h4>
Wir suchen den Gipfel von \(l\). Am Gipfel ist die Steigung null – also leiten wir ab. <b>Wichtig:</b> Abgeleitet wird nur nach dem Parameter. \(n\), \(\sum x_i\), \(\sum\log x_i\) sind einfach <b>Zahlen</b>.
<span class="tr">Türevi sadece θ'ya göre alıyorsun. n, Σxᵢ, Σlog xᵢ hepsi sabit sayı gibi. İçinde θ olmayan terimin türevi 0.</span>
<table><tr><th>Term in \(l(\theta)\)</th><th>Ableitung</th><th>Merkhilfe</th></tr>
<tr><td>\(c\cdot\log\theta\)</td><td>\(\dfrac{c}{\theta}\)</td><td>\((\log\theta)'=\frac1\theta\)</td></tr>
<tr><td>\(c\cdot\log(\theta+1)\)</td><td>\(\dfrac{c}{\theta+1}\)</td><td></td></tr>
<tr><td>\(c\cdot\log(1-\theta)\)</td><td>\(-\dfrac{c}{1-\theta}\)</td><td>innere Ableitung \(-1\)</td></tr>
<tr><td>\(-\theta\cdot S\) &nbsp;(\(S\) = Summe)</td><td>\(-S\)</td><td>wie \((5\theta)'=5\)</td></tr>
<tr><td>\(-\dfrac{S}{\theta}=-S\theta^{-1}\)</td><td>\(+\dfrac{S}{\theta^2}\)</td><td>Potenzregel</td></tr>
<tr><td>\(-\theta^2 S\)</td><td>\(-2\theta S\)</td><td></td></tr>
<tr><td>Term ohne \(\theta\) (\(\sum\log x_i\), \(n\log2\))</td><td>\(0\)</td><td>Konstante!</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(l(\lambda)=2n\log\lambda+\sum\log x_i-\lambda\sum x_i\ \Rightarrow\ l'(\lambda)=\dfrac{2n}{\lambda}+0-\sum x_i\)</div>
<div class="fe">⚠ \(\sum\log x_i\) wird beim Ableiten nach \(\lambda\) zu 0 – nicht zu \(\sum\frac1{x_i}\)!</div>'''
U[3] = [(r'\(l(\lambda)=n\log\lambda-\lambda\sum x_i\).&nbsp;&nbsp;&nbsp;\(l^{\prime}(\lambda)=\)', r"\frac n\lambda-\sum x_i"),
        (r'\(l(\lambda)=n\log3+n\log\lambda+2\sum\log x_i-\lambda\sum x_i^3\).&nbsp;&nbsp;&nbsp;\(l^{\prime}(\lambda)=\)', r"\frac n\lambda-\sum x_i^3"),
        (r'\(l(\theta)=-n\log\theta-\frac{\sum x_i}{\theta}\).&nbsp;&nbsp;&nbsp;\(l^{\prime}(\theta)=\)', r"-\frac n\theta+\frac{\sum x_i}{\theta^2}"),
        (r'\(l(\theta)=5n\log\theta+\theta\sum\log x_i\).&nbsp;&nbsp;&nbsp;\(l^{\prime}(\theta)=\)', r"\frac{5n}{\theta}+\sum\log x_i")]

L4 = r'''
<h4>Schritt ④: Null setzen und nach dem Parameter auflösen</h4>
\(l'(\hat\theta)=0\) setzen und \(\hat\theta\) allein auf eine Seite bringen. Das Dach \(\hat{\ }\) zeigt: Das ist jetzt der <b>Schätzer</b>.
<span class="tr">Türevi 0'a eşitle, θ'yı yalnız bırak. Hep aynı 4 kalıp çıkıyor.</span>
<table><tr><th>Gleichung</th><th>Rechenweg</th><th>Lösung</th></tr>
<tr><td>\(\frac{a}{\theta}-S=0\)</td><td>\(\frac a\theta=S\ \Rightarrow\ a=\theta S\)</td><td>\(\hat\theta=\frac{a}{S}\)</td></tr>
<tr><td>\(\frac{a}{\theta}+S=0\)</td><td>\(\frac a\theta=-S\)</td><td>\(\hat\theta=-\frac aS\)</td></tr>
<tr><td>\(-\frac a\theta+\frac{S}{\theta^2}=0\)</td><td>mal \(\theta^2\): \(-a\theta+S=0\)</td><td>\(\hat\theta=\frac Sa\)</td></tr>
<tr><td>\(\frac{a}{\theta+1}+S=0\)</td><td>\(\theta+1=-\frac aS\)</td><td>\(\hat\theta=-\frac aS-1\)</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(\frac{2n}{\lambda}-\sum x_i=0\ \Rightarrow\ \frac{2n}{\lambda}=\sum x_i\ \Rightarrow\ 2n=\lambda\sum x_i\ \Rightarrow\ \hat\lambda=\frac{2n}{\sum x_i}=\frac{2}{\bar x}\)</div>
<div class="fe">⚠ Nach dem Parameter auflösen, nicht nach \(x_i\)! Und \(\frac{n}{\sum x_i}=\frac1{\bar x}\), weil \(\bar x=\frac{\sum x_i}{n}\).</div>'''
U[4] = [(r'\(\frac n\lambda-\sum x_i^3=0\).&nbsp;&nbsp;&nbsp;\(\hat\lambda=\)', r'\frac{n}{\sum x_i^3}'),
        (r'\(\frac{5n}{\theta}+\sum\log x_i=0\).&nbsp;&nbsp;&nbsp;\(\hat\theta=\)', r'-\frac{5n}{\sum\log x_i}'),
        (r'\(-\frac n\theta+\frac{\sum x_i}{\theta^2}=0\).&nbsp;&nbsp;&nbsp;\(\hat\theta=\)', r'\frac{\sum x_i}{n}=\bar x'),
        (r'\(\frac{2n}{\theta+1}+\sum\log x_i=0\).&nbsp;&nbsp;&nbsp;\(\hat\theta=\)', r'-\frac{2n}{\sum\log x_i}-1')]

L5 = r'''
<h4>Schritt ⑤: Hinreichende Bedingung – ist es wirklich ein Maximum?</h4>
Leite \(l'(\theta)\) noch einmal ab. Ist \(l''\lt 0\), ist die Kurve nach unten gewölbt → <b>Maximum</b>. Die Begründung gehört dazu!
<span class="tr">İkinci türev negatifse tepe noktası. "neden negatif" cümlesini yazmazsan puan kaybedersin.</span>
<table><tr><th>\(l'(\theta)\) enthält</th><th>in \(l''(\theta)\)</th></tr>
<tr><td>\(\frac{a}{\theta}\)</td><td>\(-\frac{a}{\theta^2}\)</td></tr><tr><td>\(\frac{a}{\theta+1}\)</td><td>\(-\frac{a}{(\theta+1)^2}\)</td></tr><tr><td>\(-S\) (ohne \(\theta\))</td><td>\(0\)</td></tr><tr><td>\(\frac{S}{\theta^2}\)</td><td>\(-\frac{2S}{\theta^3}\)</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(l'(\lambda)=\frac{2n}{\lambda}-\sum x_i\ \Rightarrow\ l''(\lambda)=-\frac{2n}{\lambda^2}\lt 0\), da \(n\gt 0\) und \(\lambda^2\gt 0\). ⇒ Maximum.</div>
<div class="fe">⚠ Sonderfall \(-\frac n\theta+\frac{S}{\theta^2}\): \(l''=\frac n{\theta^2}-\frac{2S}{\theta^3}\) ist nicht sofort negativ – an der Stelle \(\hat\theta=\frac Sn\) einsetzen: \(\frac{n}{\hat\theta^2}-\frac{2n}{\hat\theta^2}=-\frac n{\hat\theta^2}\lt 0\).</div>'''
U[5] = [(r'\(l^{\prime}(\lambda)=\frac n\lambda-\sum x_i^3\).&nbsp;&nbsp;&nbsp;\(l^{\prime\prime}(\lambda)=\) … und Begründung', r"-\frac n{\lambda^2}\lt 0\text{, da }n\gt 0,\ \lambda^2\gt 0"),
        (r'\(l^{\prime}(\theta)=\frac{5n}{\theta}+\sum\log x_i\).&nbsp;&nbsp;&nbsp;\(l^{\prime\prime}(\theta)=\) … und Begründung', r"-\frac{5n}{\theta^2}\lt 0"),
        (r'\(l^{\prime}(\theta)=\frac{2n}{\theta+1}+\sum\log x_i\).&nbsp;&nbsp;&nbsp;\(l^{\prime\prime}(\theta)=\) … und Begründung', r"-\frac{2n}{(\theta+1)^2}\lt 0")]

L6 = r'''
<h4>Schritt ⑥: Schätzwert berechnen</h4>
Erst jetzt kommen die Zahlen! Bestimme aus der Stichprobe genau die Größen, die in deiner Formel stehen:
<table><tr><th>Größe</th><th>Bedeutung</th><th>Beispiel \(x=(1,\,2,\,3)\)</th></tr>
<tr><td>\(n\)</td><td>Anzahl der Werte</td><td>\(3\)</td></tr><tr><td>\(\sum x_i\)</td><td>Summe</td><td>\(6\)</td></tr><tr><td>\(\sum x_i^2\)</td><td>Summe der Quadrate</td><td>\(1+4+9=14\)</td></tr><tr><td>\(\sum\log x_i\)</td><td>Summe der ln-Werte</td><td>\(0+0.6931+1.0986=1.7918\)</td></tr></table>
<div class="fe">⚠ \(\log\) = natürlicher Logarithmus = Taste <b>ln</b> (nicht log!). Zwischenergebnisse mit 4 Nachkommastellen, Ergebnis mit 3.</div>
<span class="tr">(a)(b)(c)'de sayı yok! Sayılar sadece burada. n = kaç tane sayı, Σxᵢ = toplamları.</span>'''
U[6] = [(r'\(\hat\lambda=\frac{n}{\sum x_i^3}\), Stichprobe \(x=(1,\ 2)\).&nbsp;&nbsp;&nbsp;\(\hat\lambda=\)', r'\frac{2}{1+8}=\frac29=0.222'),
        (r'\(\hat\theta=-\frac{n}{\sum\log x_i}\), Stichprobe \(x=(0.2,\ 0.5)\).&nbsp;&nbsp;&nbsp;\(\hat\theta=\)', r'\sum\log x_i=-1.6094-0.6931=-2.3026\Rightarrow\hat\theta=\frac{2}{2.3026}=0.869'),
        (r'\(\hat\theta=\frac{\sum x_i^2}{2n}\), Stichprobe \(x=(2,\ 4)\).&nbsp;&nbsp;&nbsp;\(\hat\theta=\)', r'\frac{4+16}{4}=5')]

TITLES = {1: 'Likelihood = Produkt', 2: 'Log-Likelihood', 3: 'Ableiten', 4: 'Nullsetzen und Auflösen', 5: 'Hinreichende Bedingung', 6: 'Schätzwert berechnen'}
LERN = {1: L1, 2: L2, 3: L3, 4: L4, 5: L5, 6: L6}
MIN = {1: 8, 2: 6, 3: 8, 4: 6, 5: 5, 6: 4}

deck = r'''<section class="t0 kl">
<div class="kl-deck">
<h1>Maximum-Likelihood – Kurs mit Klausuraufgaben</h1>
<div class="sub">Statistik und Data Science I · erst lernen, dann sofort üben · Lerneinheiten 1–6, danach 13 komplette Klausuraufgaben<br><span class="small">Übungsheft zur Vorbereitung – keine offizielle Klausur</span></div>
<div class="kl-hin"><h3>So arbeitest du (ca. 2 Stunden)</h3><ul>
<li><b>Lerneinheit lesen</b> (blauer Kasten) → <b>direkt danach die Übung</b> zu genau diesem Schritt (Klausurlayout). Lösungen hinten.</li>
<li>Nach Einheit 6 kannst du alle sechs Schritte. Dann folgen die <b>kompletten Klausuraufgaben</b> mit Teilaufgaben (a)–(d) wie in der echten Klausur.</li>
<li>Zeitplan: Einheiten 1–6 mit Übungen ≈ 60 min · Klausuraufgaben 1–8 ≈ 60 min (7 min pro Aufgabe).</li>
<li>Mit \(\log\) ist stets der natürliche Logarithmus gemeint (Taschenrechner: <b>ln</b>).</li></ul>
<table class="kl-pt"><tr><th>Schritt</th><td>①</td><td>②</td><td>③</td><td>④</td><td>⑤</td><td>⑥</td></tr><tr><th>Inhalt</th><td>\(L=\prod f\)</td><td>\(l=\log L\)</td><td>\(l'\)</td><td>\(l'=0\)</td><td>\(l''\lt 0\)</td><td>Zahlen</td></tr><tr><th>Klausur</th><td colspan="2">(a) 4 P</td><td colspan="2">(b) 3 P</td><td>(c) 2 P</td><td>(d) 1 P</td></tr></table>
</div></div>
'''

out = [CSS, deck]
for k in range(1, 7):
    out.append(lern(k, TITLES[k], MIN[k], LERN[k]))
    out.append(uebung(k, TITLES[k], U[k]))
out.append('<div class="lern kl-pb"><div class="lh1"><span>Lerneinheit 7 · Alles zusammen: die komplette Klausuraufgabe</span><small>ab jetzt: Klausurmodus</small></div><div class="lb2">Jetzt kommen die sechs Schritte in einer Aufgabe – genau so ist die ML-Aufgabe der Klausur aufgebaut: (a) = ① + ②, (b) = ③ + ④, (c) = ⑤, (d) = ⑥.<span class="tr">Artık sınav modu: her Aufgabe 6 adımın hepsi. 7 dakika hedefle. Takılırsan ilgili Lerneinheit\'e geri dön.</span>'
           r'<div class="vg"><b class="t">Vorgemacht (Klausurmuster)</b>\(f(x;\lambda)=\lambda^2x\,e^{-\lambda x}\), Stichprobe \((1,3,2,0.5,3.5)\):<br>(a) \(L(\lambda)=\lambda^{2n}\big(\prod x_i\big)e^{-\lambda\sum x_i}\), \(l(\lambda)=2n\log\lambda+\sum\log x_i-\lambda\sum x_i\)<br>(b) \(l^{\prime}(\lambda)=\frac{2n}\lambda-\sum x_i=0\Rightarrow\hat\lambda=\frac{2n}{\sum x_i}\)<br>(c) \(l^{\prime\prime}(\lambda)=-\frac{2n}{\lambda^2}\lt 0\), da \(n\gt0,\lambda^2\gt0\) ⇒ Maximum<br>(d) \(n=5,\ \sum x_i=10\Rightarrow\hat\lambda=1\)</div></div></div>')
for i, a in enumerate(K.A, 1):
    h, _ = K.aufgabe(i, a); out.append(h)
h, _, usol = K.uniform(len(K.A) + 1); out.append(h)
out.append('</section>')

# Lösungen
S = ['<section class="t1 loes loesk" style="page-break-before:always"><h2>Lösungen</h2><p class="small">Erst selbst rechnen, dann vergleichen. Bei den Übungen gibt es je 1 Punkt pro Teilaufgabe; bei den Klausuraufgaben steht der Bewertungsschlüssel in eckigen Klammern.</p>']
for k in range(1, 7):
    S.append(f'<h3>Übung {k}: {TITLES[k]}</h3><p>' + '<br>'.join(f'({chr(97+j)}) \\({s}\\)' for j, (_, s) in enumerate(U[k])) + '</p>')
for i, a in enumerate(K.A, 1):
    S.append(f'<h3>Klausuraufgabe {i}</h3><p>' + '<br>'.join(a['sol']) + '</p>')
S.append(f'<h3>Klausuraufgabe {len(K.A)+1}</h3><p>' + '<br>'.join(usol) + '</p></section>')
open(os.path.join(HERE, 'content', 'mlkurs.html'), 'w').write('\n'.join(out) + '\n' + '\n'.join(S))
print('ok')
