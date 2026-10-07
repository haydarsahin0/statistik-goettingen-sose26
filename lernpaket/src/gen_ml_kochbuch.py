# ML-Kochbuch: alle Dichtetypen mit fertigem Lösungsweg + A4-Spickzettel (Formen) + Klausur-Schablone
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'extra', 'ml_kochbuch.html')

CSS = r'''<style>
.w{width:auto!important;padding:0!important}
@page{size:A4 landscape;margin:9mm 10mm}
body{font-size:12.5px!important;background:#fff!important;line-height:1.35!important}
h1{font-size:30px!important;margin:0 0 2px!important}
.pb{break-before:page}
table.k{width:100%;border-collapse:collapse;margin:4px 0 8px}
table.k th{background:#1f4e79;color:#fff;font-family:Inter;font-size:11px;padding:4px 6px;text-align:left}
table.k td{border:1px solid #cfd6e0;padding:4px 5px;vertical-align:middle;white-space:nowrap;font-size:11.5px}
table.k td.wr{white-space:normal}
table.k tr:nth-child(even) td{background:#f6f8fb}
table.k td.nr{font:800 12px Inter;color:#1f4e79;text-align:center;width:22px}
table.k td.res{background:#eaf6ec!important;font-weight:700}
.fam{font:800 15px Inter;color:#fff;border-radius:7px;padding:5px 12px;margin:6px 0 3px;break-after:avoid}
.form{border:2px solid #1f1d1a;border-radius:10px;padding:6px 12px;margin:6px 0;break-inside:avoid}
.form h3{margin:0 0 3px;font-family:Inter;font-size:14px}
.how{display:flex;gap:10px}.how>div{flex:1;border:1.5px solid #1f4e79;border-radius:10px;padding:6px 10px}
.how b.n{display:inline-block;width:22px;height:22px;border-radius:50%;background:#1f4e79;color:#fff;text-align:center;line-height:22px;font-family:Inter;margin-right:6px}
.tr{border-left:3px solid #00796b;background:#e3f4f2;padding:3px 9px;font-style:italic;color:#0f4f47;margin:4px 0;border-radius:0 6px 6px 0}
.tpl{border:2px dashed #a8823a;border-radius:10px;padding:6px 14px;background:#fffaf0;font-size:13.5px;line-height:1.6}
.small{font-size:11px;color:#555}
</style>'''

def M(s):  # inline math, displaystyle
    return r'\(\displaystyle ' + s + r'\)'

# ---------------- Seite 1: Anleitung
p1 = r'''
<div class="kick">ML-Kochbuch · alle Aufgabentypen mit fertigem Lösungsweg · zum Abschreiben aufs A4-Blatt</div>
<h1>Maximum-Likelihood: <em>Muster erkennen</em> → Lösung abschreiben.</h1>
<div class="tr">Kullanım: Sınavdaki f'yi aşağıdaki kataloğa benzet → aynı satırı kendi f'ne uyarla. Ya da 3 adımlı kısa yolla l(θ)'yı yaz ve sayfa 2'deki "Form" tablosundan sonucu oku.</div>
<div class="how">
<div><b class="n">1</b><b>\(\log f(x;\theta)\) schreiben</b><br>Log-Regeln: \(\log(ab)=\log a+\log b\), \(\log a^k=k\log a\), \(\log e^z=z\).<br><i>Beispiel:</i> \(f=3\lambda x^2e^{-\lambda x^3}\Rightarrow\log f=\log3+\log\lambda+2\log x-\lambda x^3\)</div>
<div><b class="n">2</b><b>\(\log f\) → \(l(\theta)\)</b><br>Term <b>ohne \(x\)</b> → mal \(n\).<br>Term <b>mit \(x\)</b> → \(x\) durch \(\sum x_i\) ersetzen (\(\log x\to\sum\log x_i\), \(x^3\to\sum x_i^3\)).<br><i>Beispiel:</i> \(l=n\log3+n\log\lambda+2\sum\log x_i-\lambda\sum x_i^3\)</div>
<div><b class="n">3</b><b>Form erkennen → \(\hat\theta\) ablesen</b><br>Steht \(l=A\log\lambda-B\lambda+\dots\) da, ist \(\hat\lambda=\frac AB\).<br><i>Beispiel:</i> \(A=n,\ B=\sum x_i^3\Rightarrow\hat\lambda=\frac{n}{\sum x_i^3}\)<br>Dann Lösungsweg mit der Schablone (Seite 3) aufschreiben.</div></div>
<div class="form" style="margin-top:8px"><h3>L für Teil (a) ebenso schnell – aus \(f\) direkt:</h3>
Faktor <b>ohne \(x\)</b> (\(\lambda\), \(3\), \(\frac1\theta\)) → <b>hoch \(n\)</b> (\(\lambda^n\), \(3^n\), \(\theta^{-n}\)) · Faktor <b>\(x\), \(x^2\), \(g(x)\)</b> → <b>\(\prod\)</b> (\(\prod x_i^2\)) · \(x\) <b>im Exponenten</b> (\(e^{-\lambda x}\), \(\pi^x\), \(x^{\theta-1}\)) → <b>\(\sum\) in den Exponenten</b> bzw. \(\big(\prod x_i\big)^{\theta-1}\)
<div class="small">Beispiel: \(f=3\lambda x^2e^{-\lambda x^3}\Rightarrow L(\lambda)=3^n\lambda^n\big(\prod x_i^2\big)e^{-\lambda\sum x_i^3}\)</div></div>
'''

# ---------------- Seite 2: die Formen (A4-Spickzettel)
forms = [
 ('I', r'l(\theta)=A\log\theta-B\,\theta+K', r"l'=\frac A\theta-B", r'\hat\theta=\frac AB', r"l''=-\frac A{\theta^2}\lt 0", r'Exponential, Gamma, Poisson, \(x^{\theta-1}\), Pareto … (Achtung: \(B\) kann \(-\sum\log x_i\) sein!)'),
 ('II', r'l(\theta)=-A\log\theta-\frac B\theta+K', r"l'=-\frac A\theta+\frac B{\theta^2}", r'\hat\theta=\frac BA', r"l''(\hat\theta)=\frac{A}{\hat\theta^2}-\frac{2B}{\hat\theta^3}=-\frac{A}{\hat\theta^2}\lt 0", r'Parameter im Nenner: \(\frac1\theta e^{-x/\theta}\), Rayleigh, Normal-\(\sigma^2\)'),
 ('III', r'l(p)=A\log p+B\log(1-p)+K', r"l'=\frac Ap-\frac B{1-p}", r'\hat p=\frac{A}{A+B}', r"l''=-\frac A{p^2}-\frac B{(1-p)^2}\lt 0", r'Bernoulli, Binomial, Geometrisch'),
 ('IV', r'l(\theta)=A\log(\theta+1)+C\,\theta+K', r"l'=\frac A{\theta+1}+C", r'\hat\theta=-\frac AC-1', r"l''=-\frac{A}{(\theta+1)^2}\lt 0", r'\((\theta+1)x^\theta\) mit \(C=\sum\log x_i\)'),
 ('V', r'l(\lambda)=rn\log\lambda-\lambda^r S+K', r"l'=\frac{rn}\lambda-r\lambda^{r-1}S", r'\hat\lambda=\Big(\frac nS\Big)^{1/r}', r"l''=-\frac{rn}{\lambda^2}-r(r-1)\lambda^{r-2}S\lt 0", r'Weibull mit festem \(r\), \(S=\sum x_i^r\)'),
 ('VI', r'L(\theta)=\theta^{-n}\text{ für }\theta\ge\max x_i', r'\text{nicht ableiten!}', r'\hat\theta=\max(x_1,\dots,x_n)', r'—', r'Gleichverteilung \(U(0,\theta)\)'),
 ('VII', r'l(\mu)=-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2+K', r"l'=\frac1{\sigma^2}\sum(x_i-\mu)", r'\hat\mu=\bar x', r"l''=-\frac n{\sigma^2}\lt 0", r'Normalverteilung, \(\mu\) gesucht'),
]
p2 = '<div class="pb"></div><div class="fam" style="background:#b42318">A4-Spickzettel: die 7 Formen – \\(l\\) aufstellen, Form erkennen, \\(\\hat\\theta\\) ablesen (\\(K\\) = alles ohne Parameter, Ableitung 0)</div>'
p2 += '<table class="k"><tr><th>Form</th><th>so sieht \\(l\\) aus</th><th>Ableitung \\(l\'\\)</th><th>ML-Schätzer</th><th>2. Ableitung</th><th>typische Dichten</th></tr>'
for f in forms:
    p2 += f'<tr><td class="nr">{f[0]}</td><td>{M(f[1])}</td><td>{M(f[2])}</td><td class="res">{M(f[3])}</td><td>{M(f[4])}</td><td class="wr">{f[5]}</td></tr>'
p2 += '</table>'
p2 += r'''<div class="form"><h3>Typische \(A\), \(B\) – direkt aus \(l\) ablesen</h3>
\(\lambda e^{-\lambda x}\): \(A=n,\ B=\sum x_i\) · \(\lambda^2xe^{-\lambda x}\): \(A=2n,\ B=\sum x_i\) · \(2\theta xe^{-\theta x^2}\): \(A=n,\ B=\sum x_i^2\) · Poisson: \(A=\sum x_i,\ B=n\) · \(\theta x^{\theta-1}\): \(A=n,\ B=-\sum\log x_i\) · Pareto \(\beta x^{-\beta-1}\): \(A=n,\ B=\sum\log x_i\) · Bernoulli: \(A=\sum x_i,\ B=n-\sum x_i\) · Geometrisch \(p(1-p)^x\): \(A=n,\ B=\sum x_i\)</div>
<div class="tr">Sınavda: önce l'yi yaz (kısa yol), sonra hangi Form olduğunu bul, θ̂'yı oku. Ama türevi ve =0 adımını yine YAZ – puan oradan geliyor. Sayfa 3'teki şablonu kullan.</div>
<div class="form"><h3>Schätzwert & Funktionen davon (Invarianz)</h3>\(n\) = Anzahl Werte · \(\sum x_i\) = Summe · \(\sum x_i^2\) = Summe der Quadrate · \(\sum\log x_i\) mit <b>ln</b>! · Ist \(\hat\lambda\) bekannt, schätzt man z. B. \(P(X\gt t)=e^{-\hat\lambda t}\), \(E(X)=1/\hat\lambda\), \(P(X=0)=e^{-\hat\lambda}\) einfach durch Einsetzen.</div>
'''

# ---------------- Seite 3: Klausur-Schablone
p3 = r'''<div class="pb"></div><div class="fam" style="background:#a8823a">Klausur-Schablone – genau so aufschreiben (Beispiel \(f(x;\lambda)=\lambda^2xe^{-\lambda x}\), Daten \(1,3,2,0.5,3.5\))</div>
<div class="tpl">
<b>(a)</b> \(L(\lambda)=\prod_{i=1}^n f(x_i;\lambda)=\prod_{i=1}^n\lambda^2x_ie^{-\lambda x_i}=\lambda^{2n}\Big(\prod_{i=1}^n x_i\Big)e^{-\lambda\sum_{i=1}^n x_i}\)<br>
\(\phantom{(a)}\ l(\lambda)=\log L(\lambda)=2n\log\lambda+\sum_{i=1}^n\log x_i-\lambda\sum_{i=1}^n x_i\)<br>
<b>(b)</b> \(l'(\lambda)=\dfrac{2n}{\lambda}-\sum_{i=1}^n x_i\overset{!}{=}0\ \Leftrightarrow\ \dfrac{2n}{\lambda}=\sum x_i\ \Leftrightarrow\ \hat\lambda=\dfrac{2n}{\sum_{i=1}^n x_i}=\dfrac{2}{\bar x}\)<br>
<b>(c)</b> \(l''(\lambda)=-\dfrac{2n}{\lambda^2}\lt 0\) für alle \(\lambda\gt 0\), da \(n\gt 0\) und \(\lambda^2\gt 0\). \(\Rightarrow\ \hat\lambda\) ist ein Maximum.<br>
<b>(d)</b> \(n=5,\ \sum x_i=1+3+2+0.5+3.5=10\ \Rightarrow\ \hat\lambda=\dfrac{2\cdot5}{10}=1\)</div>
<div class="tr">Kendi sorunda sadece f'yi, l'yi ve sonucu değiştir; cümleler ve semboller aynı kalıyor. Bu şablonu A4'e yaz.</div>
<div class="form"><h3>Satzbausteine</h3>„Da \(n\gt0\) und \(\theta^2\gt0\), ist \(l''(\theta)\lt0\) für alle \(\theta\gt0\); somit liegt ein Maximum vor.“ · „Die Terme ohne \(\theta\) fallen beim Ableiten weg.“ · „Mit \(\log\) ist der natürliche Logarithmus gemeint.“</div>
'''

# ---------------- Katalog
def row(nr, f, L, l, d1, est, d2):
    return f'<tr><td class="nr">{nr}</td><td>{M(f)}</td><td>{M(L)}</td><td>{M(l)}</td><td>{M(d1)}</td><td class="res">{M(est)}</td><td>{M(d2)}</td></tr>'

HEAD = "<table class=\"k\"><tr><th>#</th><th>Dichte \\(f\\)</th><th>(a) Likelihood \\(L\\)</th><th>(a) Log-Likelihood \\(l\\)</th><th>(b) \\(l'\\)</th><th>(b) ML-Schätzer</th><th>(c) \\(l''\\)</th></tr>"

fam1 = [
 (1, r'\lambda e^{-\lambda x}', r'\lambda^ne^{-\lambda\sum x_i}', r'n\log\lambda-\lambda\sum x_i', r'\frac n\lambda-\sum x_i', r'\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}', r'-\frac n{\lambda^2}\lt0'),
 (2, r'\lambda^2xe^{-\lambda x}', r'\lambda^{2n}\big(\prod x_i\big)e^{-\lambda\sum x_i}', r'2n\log\lambda+\sum\log x_i-\lambda\sum x_i', r'\frac{2n}\lambda-\sum x_i', r'\hat\lambda=\frac{2n}{\sum x_i}', r'-\frac{2n}{\lambda^2}\lt0'),
 (3, r'\tfrac12\lambda^3x^2e^{-\lambda x}', r'2^{-n}\lambda^{3n}\big(\prod x_i^2\big)e^{-\lambda\sum x_i}', r'-n\log2+3n\log\lambda+2\sum\log x_i-\lambda\sum x_i', r'\frac{3n}\lambda-\sum x_i', r'\hat\lambda=\frac{3n}{\sum x_i}', r'-\frac{3n}{\lambda^2}\lt0'),
 (4, r'\tfrac16\lambda^4x^3e^{-\lambda x}', r'6^{-n}\lambda^{4n}\big(\prod x_i^3\big)e^{-\lambda\sum x_i}', r'-n\log6+4n\log\lambda+3\sum\log x_i-\lambda\sum x_i', r'\frac{4n}\lambda-\sum x_i', r'\hat\lambda=\frac{4n}{\sum x_i}', r'-\frac{4n}{\lambda^2}\lt0'),
 (5, r'2\theta xe^{-\theta x^2}', r'2^n\theta^n\big(\prod x_i\big)e^{-\theta\sum x_i^2}', r'n\log2+n\log\theta+\sum\log x_i-\theta\sum x_i^2', r'\frac n\theta-\sum x_i^2', r'\hat\theta=\frac{n}{\sum x_i^2}', r'-\frac n{\theta^2}\lt0'),
 (6, r'3\lambda x^2e^{-\lambda x^3}', r'3^n\lambda^n\big(\prod x_i^2\big)e^{-\lambda\sum x_i^3}', r'n\log3+n\log\lambda+2\sum\log x_i-\lambda\sum x_i^3', r'\frac n\lambda-\sum x_i^3', r'\hat\lambda=\frac{n}{\sum x_i^3}', r'-\frac n{\lambda^2}\lt0'),
 (7, r'\theta e^{-\theta(x-1)},\,x\gt1', r'\theta^ne^{-\theta\sum(x_i-1)}', r'n\log\theta-\theta\sum(x_i-1)', r'\frac n\theta-\sum(x_i-1)', r'\hat\theta=\frac{n}{\sum x_i-n}=\frac1{\bar x-1}', r'-\frac n{\theta^2}\lt0'),
 (8, r'\text{Poisson }\frac{\lambda^xe^{-\lambda}}{x!}', r'\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}', r'\sum x_i\log\lambda-n\lambda-\sum\log x_i!', r'\frac{\sum x_i}\lambda-n', r'\hat\lambda=\bar x', r'-\frac{\sum x_i}{\lambda^2}\lt0'),
]
fam2 = [
 (9, r'\theta x^{\theta-1},\,0\lt x\lt1', r'\theta^n\big(\prod x_i\big)^{\theta-1}', r'n\log\theta+(\theta-1)\sum\log x_i', r'\frac n\theta+\sum\log x_i', r'\hat\theta=-\frac{n}{\sum\log x_i}', r'-\frac n{\theta^2}\lt0'),
 (10, r'(\theta+1)x^{\theta},\,0\lt x\lt1', r'(\theta+1)^n\big(\prod x_i\big)^{\theta}', r'n\log(\theta+1)+\theta\sum\log x_i', r'\frac n{\theta+1}+\sum\log x_i', r'\hat\theta=-\frac{n}{\sum\log x_i}-1', r'-\frac n{(\theta+1)^2}\lt0'),
 (11, r'2\theta x^{2\theta-1},\,0\lt x\lt1', r'2^n\theta^n\big(\prod x_i\big)^{2\theta-1}', r'n\log2+n\log\theta+(2\theta-1)\sum\log x_i', r'\frac n\theta+2\sum\log x_i', r'\hat\theta=-\frac{n}{2\sum\log x_i}', r'-\frac n{\theta^2}\lt0'),
 (12, r'\theta(1-x)^{\theta-1},\,0\lt x\lt1', r'\theta^n\big(\prod(1-x_i)\big)^{\theta-1}', r'n\log\theta+(\theta-1)\sum\log(1-x_i)', r'\frac n\theta+\sum\log(1-x_i)', r'\hat\theta=-\frac{n}{\sum\log(1-x_i)}', r'-\frac n{\theta^2}\lt0'),
 (13, r'\text{Pareto }\frac{\beta}{x^{\beta+1}},\,x\gt1', r'\beta^n\big(\prod x_i\big)^{-(\beta+1)}', r'n\log\beta-(\beta+1)\sum\log x_i', r'\frac n\beta-\sum\log x_i', r'\hat\beta=\frac{n}{\sum\log x_i}', r'-\frac n{\beta^2}\lt0'),
 (14, r'\frac{\beta\,2^\beta}{x^{\beta+1}},\,x\gt2', r'\beta^n2^{n\beta}\big(\prod x_i\big)^{-(\beta+1)}', r'n\log\beta+n\beta\log2-(\beta+1)\sum\log x_i', r'\frac n\beta+n\log2-\sum\log x_i', r'\hat\beta=\frac{n}{\sum\log x_i-n\log2}', r'-\frac n{\beta^2}\lt0'),
 (15, r'\frac{\theta}{(1+x)^{\theta+1}},\,x\gt0', r'\theta^n\prod(1+x_i)^{-(\theta+1)}', r'n\log\theta-(\theta+1)\sum\log(1+x_i)', r'\frac n\theta-\sum\log(1+x_i)', r'\hat\theta=\frac{n}{\sum\log(1+x_i)}', r'-\frac n{\theta^2}\lt0'),
]
fam3 = [
 (16, r'\frac1\theta e^{-x/\theta}', r'\theta^{-n}e^{-\sum x_i/\theta}', r'-n\log\theta-\frac{\sum x_i}\theta', r'-\frac n\theta+\frac{\sum x_i}{\theta^2}', r'\hat\theta=\bar x', r'\text{bei }\hat\theta:\,-\frac n{\hat\theta^2}\lt0'),
 (17, r'\frac{x}{\theta^2}e^{-x/\theta}', r'\theta^{-2n}\big(\prod x_i\big)e^{-\sum x_i/\theta}', r'-2n\log\theta+\sum\log x_i-\frac{\sum x_i}\theta', r'-\frac{2n}\theta+\frac{\sum x_i}{\theta^2}', r'\hat\theta=\frac{\sum x_i}{2n}=\frac{\bar x}2', r'\text{bei }\hat\theta:\,-\frac{2n}{\hat\theta^2}\lt0'),
 (18, r'\text{Rayleigh }\frac{x}{\theta}e^{-\frac{x^2}{2\theta}}', r'\theta^{-n}\big(\prod x_i\big)e^{-\sum x_i^2/(2\theta)}', r'-n\log\theta+\sum\log x_i-\frac{\sum x_i^2}{2\theta}', r'-\frac n\theta+\frac{\sum x_i^2}{2\theta^2}', r'\hat\theta=\frac{\sum x_i^2}{2n}', r'\text{bei }\hat\theta:\,-\frac n{\hat\theta^2}\lt0'),
 (19, r'\text{Laplace }\frac1{2\theta}e^{-|x|/\theta}', r'2^{-n}\theta^{-n}e^{-\sum|x_i|/\theta}', r'-n\log2-n\log\theta-\frac{\sum|x_i|}\theta', r'-\frac n\theta+\frac{\sum|x_i|}{\theta^2}', r'\hat\theta=\frac{\sum|x_i|}{n}', r'\text{bei }\hat\theta:\,-\frac n{\hat\theta^2}\lt0'),
 (20, r'N(\mu_0,v),\ v=\sigma^2\text{ ges.}', r'(2\pi v)^{-n/2}e^{-\sum(x_i-\mu_0)^2/(2v)}', r'-\frac n2\log(2\pi)-\frac n2\log v-\frac{\sum(x_i-\mu_0)^2}{2v}', r'-\frac n{2v}+\frac{\sum(x_i-\mu_0)^2}{2v^2}', r'\hat v=\frac1n\sum(x_i-\mu_0)^2', r'\text{bei }\hat v:\,-\frac n{2\hat v^2}\lt0'),
]
fam4 = [
 (21, r'\text{Bernoulli }\pi^x(1-\pi)^{1-x}', r'\pi^{\sum x_i}(1-\pi)^{n-\sum x_i}', r'\sum x_i\log\pi+(n-\sum x_i)\log(1-\pi)', r'\frac{\sum x_i}\pi-\frac{n-\sum x_i}{1-\pi}', r'\hat\pi=\bar x', r'-\frac{\sum x_i}{\pi^2}-\frac{n-\sum x_i}{(1-\pi)^2}\lt0'),
 (22, r'\text{Binomial }B(m,\pi),\,m\text{ bekannt}', r'\Big(\prod\tbinom{m}{x_i}\Big)\pi^{\sum x_i}(1-\pi)^{mn-\sum x_i}', r'K+\sum x_i\log\pi+(mn-\sum x_i)\log(1-\pi)', r'\frac{\sum x_i}\pi-\frac{mn-\sum x_i}{1-\pi}', r'\hat\pi=\frac{\sum x_i}{mn}=\frac{\bar x}m', r'-\frac{\sum x_i}{\pi^2}-\frac{mn-\sum x_i}{(1-\pi)^2}\lt0'),
 (23, r'p(1-p)^x,\ x=0,1,\dots', r'p^n(1-p)^{\sum x_i}', r'n\log p+\sum x_i\log(1-p)', r'\frac np-\frac{\sum x_i}{1-p}', r'\hat p=\frac{n}{n+\sum x_i}', r'-\frac n{p^2}-\frac{\sum x_i}{(1-p)^2}\lt0'),
 (24, r'p(1-p)^{x-1},\ x=1,2,\dots', r'p^n(1-p)^{\sum x_i-n}', r'n\log p+(\sum x_i-n)\log(1-p)', r'\frac np-\frac{\sum x_i-n}{1-p}', r'\hat p=\frac{n}{\sum x_i}=\frac1{\bar x}', r'-\frac n{p^2}-\frac{\sum x_i-n}{(1-p)^2}\lt0'),
]
fam5 = [
 (25, r'\text{Weibull }r\lambda(\lambda x)^{r-1}e^{-(\lambda x)^r},\ r=2', r'2^n\lambda^{2n}\big(\prod x_i\big)e^{-\lambda^2\sum x_i^2}', r'n\log2+2n\log\lambda+\sum\log x_i-\lambda^2\sum x_i^2', r'\frac{2n}\lambda-2\lambda\sum x_i^2', r'\hat\lambda=\sqrt{\frac{n}{\sum x_i^2}}', r'-\frac{2n}{\lambda^2}-2\sum x_i^2\lt0'),
 (26, r'\text{Weibull mit }r=1\ (=\lambda e^{-\lambda x})', r'\lambda^ne^{-\lambda\sum x_i}', r'n\log\lambda-\lambda\sum x_i', r'\frac n\lambda-\sum x_i', r'\hat\lambda=\frac1{\bar x}', r'-\frac n{\lambda^2}\lt0'),
 (27, r'N(\mu,\sigma^2),\ \sigma^2\text{ bekannt}', r'(2\pi\sigma^2)^{-n/2}e^{-\sum(x_i-\mu)^2/(2\sigma^2)}', r'K-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2', r'\frac1{\sigma^2}\sum(x_i-\mu)', r'\hat\mu=\bar x', r'-\frac n{\sigma^2}\lt0'),
 (28, r'U(0,\theta):\ \frac1\theta,\ 0\le x\le\theta', r'\theta^{-n}\ (\theta\ge\max x_i),\ \text{sonst }0', r'\text{—}', r'\text{keine Nullstelle}', r'\hat\theta=\max x_i', r'\text{—}'),
]

def fam(title, color, rows, note=''):
    h = f'<div class="fam" style="background:{color}">{title}</div>'
    if note: h += f'<div class="tr">{note}</div>'
    return h + HEAD + ''.join(row(*r) for r in rows) + '</table>'

cat = '<div class="pb"></div>' + fam('Familie 1 · Parameter als Faktor und in \\(e^{-\\theta\\,h(x)}\\) → Form I: \\(\\hat\\theta=\\frac{A}{\\sum h(x_i)}\\)', '#1f4e79', fam1, 'Kalıp: f = (sayı)·θ^a·(x ile ilgili çarpan)·e^(−θ·h(x)) ⇒ θ̂ = a·n / Σh(xᵢ). a = θ\'nın üssü, h = e\'nin üstünde θ\'yla çarpılan şey.')
cat += '<div class="pb"></div>' + fam('Familie 2 · Parameter im Exponenten von \\(x\\) → Form I mit \\(B=-\\sum\\log x_i\\) bzw. Form IV', '#7030a0', fam2, 'Kalıp: θ, x\'in üssünde ⇒ l\'de θ·Σlog xᵢ çıkar. Sonuçta hep Σlog xᵢ var. 0<x<1 ise log xᵢ negatif → θ̂ pozitif çıkar. Hesap makinesinde ln!')
cat += '<div class="pb"></div>' + fam('Familie 3 · Parameter im Nenner (\\(\\frac1\\theta\\), \\(e^{-h(x)/\\theta}\\)) → Form II: \\(\\hat\\theta=\\frac{\\sum h(x_i)}{a\\,n}\\)', '#2e7d32', fam3, 'Kalıp: θ paydada ⇒ türevde −a·n/θ + Σh/θ² çıkar → θ² ile çarp → θ̂ = Σh/(a·n). 2. türevi θ̂ noktasında hesapla.')
cat += fam('Familie 4 · Diskret mit \\(p\\) bzw. \\(\\pi\\) → Form III: \\(\\hat p=\\frac{A}{A+B}\\)', '#c55a11', fam4, 'Kalıp: l = A·log p + B·log(1−p) ⇒ p̂ = A/(A+B). A = p\'nin üssündeki toplam, B = (1−p)\'nin üssündeki toplam.')
cat += '<div class="pb"></div>' + fam('Familie 5 · Sonderfälle: Weibull, Normal, Gleichverteilung', '#b42318', fam5, 'Weibull: önce r\'yi yerine koyup f\'yi sadeleştir (sınavda ayrı puan!). Gleichverteilung: türev alma, θ̂ = en büyük gözlem.')
cat += r'''<div class="form"><h3>Rechenbeispiele für Teil (d) – Zahlen einsetzen</h3>
#1 mit \(1,2,3\): \(\hat\lambda=\frac{3}{6}=0.5\) · #2 mit \(1,3,2,0.5,3.5\): \(\frac{10}{10}=1\) · #5 mit \(0.5,1,1.5\): \(\frac{3}{3.5}=0.857\) · #9 mit \(0.5,0.5\): \(-\frac{2}{2\cdot(-0.6931)}=1.443\) · #13 mit \(3,3\): \(\frac{2}{2.1972}=0.910\) · #18 mit \(1,2,3\): \(\frac{14}{6}=2.333\) · #23 mit \(0,1,2,1\): \(\frac{4}{4+4}=0.5\) · #25 mit \(1,1\): \(\sqrt{2/2}=1\)</div>'''

open(OUT, 'w').write(CSS + p1 + p2 + p3 + cat)
print(OUT)
