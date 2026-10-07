# Erzeugt das ML-Trainingsheft (HTML mit KaTeX) -> ML_Training.pdf
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'extra', 'ml_training.html')

CSS = r'''<style>
.w{width:auto!important;padding:0!important}
@page{size:A4;margin:11mm 12mm}
body{font-size:14px!important;background:#fff!important}
h1{font-size:32px!important}
.pb{break-before:page}
.step,.ok,.task,.sol,.warn{break-inside:avoid}
.n{display:inline-block;width:21px;height:21px;border-radius:50%;background:#7c5cd6;color:#fff;font:800 11px Inter;text-align:center;line-height:21px;margin-right:7px}
.ln{margin:5px 0}
.warn{background:#fdeeec;border-left:4px solid #c62828;border-radius:8px;padding:8px 14px;margin:10px 0}
.lvl{font:800 12px Inter;letter-spacing:.14em;text-transform:uppercase;color:#fff;border-radius:8px;padding:7px 14px;margin:14px 0 8px;break-after:avoid}
.task{border:1.6px solid #1f1d1a;border-radius:10px;padding:7px 13px 9px;margin:9px 0;background:#fff}
.th{display:flex;justify-content:space-between;align-items:center;font-family:Inter;font-weight:800;border-bottom:1.4px solid #1f1d1a;padding-bottom:3px;margin-bottom:5px}
.th .tag{font-size:11px;border-radius:99px;padding:1px 10px;border:1.4px solid}
.box{border:1.3px solid #1f1d1a;border-radius:6px;margin-top:6px;position:relative}
.box::before{content:"Lösung";position:absolute;left:6px;top:2px;font:10px Inter;color:#888}
.sol{border-left:4px solid #2f6b3a;background:#f2f8f2;border-radius:0 8px 8px 0;padding:6px 12px;margin:8px 0;font-size:13px}
.sol b.h{color:#2f6b3a}
.timer{float:right;font:700 11px Inter;color:#a8823a}
table.mini td,table.mini th{padding:4px 9px;font-size:13px}
</style>'''

def lvl(text, color):
    return f'<div class="lvl" style="background:{color}">{text}</div>'

# (Nr, Stufe, Punkte, Aufgabentext, Daten, Lösungszeilen, Ergebnis, Boxhöhe mm)
P = [
 (1, 1, 6, r'\(f(x;\lambda)=\lambda e^{-\lambda x}\), \(x\gt 0\)', r'\(1,\ 2,\ 3\)',
  [r'L(\lambda)=\lambda^n e^{-\lambda\sum x_i}', r'l(\lambda)=n\log\lambda-\lambda\sum x_i', r"l'(\lambda)=\frac n\lambda-\sum x_i=0\Rightarrow\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}", r"l''(\lambda)=-\frac n{\lambda^2}\lt 0"], r'\hat\lambda=3/6=0.5', 38),
 (2, 1, 6, r'Poisson: \(P(X=x)=\dfrac{\lambda^x e^{-\lambda}}{x!}\), \(x=0,1,2,\dots\)', r'\(2,\ 3,\ 1,\ 2\)',
  [r'L(\lambda)=\dfrac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}', r'l(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log(x_i!)', r"l'(\lambda)=\frac{\sum x_i}{\lambda}-n=0\Rightarrow\hat\lambda=\bar x", r"l''(\lambda)=-\frac{\sum x_i}{\lambda^2}\lt 0"], r'\hat\lambda=8/4=2', 38),
 (3, 1, 6, r'Bernoulli: \(P(X=x)=\pi^x(1-\pi)^{1-x}\), \(x\in\{0,1\}\)', r'\(1,\ 0,\ 1,\ 1,\ 1\)',
  [r'L(\pi)=\pi^{\sum x_i}(1-\pi)^{n-\sum x_i}', r'l(\pi)=\sum x_i\log\pi+(n-\sum x_i)\log(1-\pi)', r"l'(\pi)=\frac{\sum x_i}{\pi}-\frac{n-\sum x_i}{1-\pi}=0\Rightarrow\hat\pi=\frac{\sum x_i}{n}=\bar x", r"l''(\pi)=-\frac{\sum x_i}{\pi^2}-\frac{n-\sum x_i}{(1-\pi)^2}\lt 0"], r'\hat\pi=4/5=0.8', 42),
 (4, 1, 6, r'Normalverteilung mit bekanntem \(\sigma^2\): \(f(x;\mu)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}\)', r'\(4,\ 6,\ 8\)',
  [r'L(\mu)=(2\pi\sigma^2)^{-n/2}\,e^{-\sum(x_i-\mu)^2/(2\sigma^2)}', r'l(\mu)=-\frac n2\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2', r"l'(\mu)=\frac{1}{\sigma^2}\sum(x_i-\mu)=0\Rightarrow\sum x_i=n\mu\Rightarrow\hat\mu=\bar x", r"l''(\mu)=-\frac{n}{\sigma^2}\lt 0"], r'\hat\mu=18/3=6', 42),
 (5, 2, 8, r'\(f(x;\lambda)=\tfrac12\lambda^3x^2e^{-\lambda x}\), \(x\gt 0\)', r'\(2,\ 4\)',
  [r'L(\lambda)=\frac{1}{2^n}\lambda^{3n}\Big(\prod x_i^2\Big)e^{-\lambda\sum x_i}', r'l(\lambda)=-n\log2+3n\log\lambda+2\sum\log x_i-\lambda\sum x_i', r"l'(\lambda)=\frac{3n}{\lambda}-\sum x_i=0\Rightarrow\hat\lambda=\frac{3n}{\sum x_i}=\frac3{\bar x}", r"l''(\lambda)=-\frac{3n}{\lambda^2}\lt 0"], r'\hat\lambda=6/6=1', 48),
 (6, 2, 8, r'\(f(x;\theta)=\theta x^{\theta-1}\), \(0\lt x\lt 1\), \(\theta\gt 0\)', r'\(0.5,\ 0.5\)',
  [r'L(\theta)=\theta^n\Big(\prod x_i\Big)^{\theta-1}', r'l(\theta)=n\log\theta+(\theta-1)\sum\log x_i', r"l'(\theta)=\frac n\theta+\sum\log x_i=0\Rightarrow\hat\theta=-\frac{n}{\sum\log x_i}", r"l''(\theta)=-\frac{n}{\theta^2}\lt 0"], r'\hat\theta=-2/(2\log0.5)=1.443', 48),
 (7, 2, 8, r'\(f(x;\theta)=(\theta+1)x^{\theta}\), \(0\lt x\lt 1\), \(\theta\gt -1\)', r'\(0.2,\ 0.4\)',
  [r'L(\theta)=(\theta+1)^n\Big(\prod x_i\Big)^{\theta}', r'l(\theta)=n\log(\theta+1)+\theta\sum\log x_i', r"l'(\theta)=\frac{n}{\theta+1}+\sum\log x_i=0\Rightarrow\hat\theta=-\frac{n}{\sum\log x_i}-1", r"l''(\theta)=-\frac{n}{(\theta+1)^2}\lt 0"], r'\sum\log x_i=-2.5257\Rightarrow\hat\theta=0.7919-1=-0.208', 48),
 (8, 2, 8, r'\(f(x;\theta)=2\theta x e^{-\theta x^2}\), \(x\gt 0\)', r'\(0.5,\ 1,\ 1.5\)',
  [r'L(\theta)=2^n\theta^n\Big(\prod x_i\Big)e^{-\theta\sum x_i^2}', r'l(\theta)=n\log2+n\log\theta+\sum\log x_i-\theta\sum x_i^2', r"l'(\theta)=\frac n\theta-\sum x_i^2=0\Rightarrow\hat\theta=\frac{n}{\sum x_i^2}", r"l''(\theta)=-\frac n{\theta^2}\lt 0"], r'\sum x_i^2=3.5\Rightarrow\hat\theta=3/3.5=0.857', 48),
 (9, 2, 8, r'Pareto: \(f(x;\beta)=\dfrac{\beta}{x^{\beta+1}}\), \(x\gt 1\)', r'\(3,\ 3\)',
  [r'L(\beta)=\beta^n\Big(\prod x_i\Big)^{-(\beta+1)}', r'l(\beta)=n\log\beta-(\beta+1)\sum\log x_i', r"l'(\beta)=\frac n\beta-\sum\log x_i=0\Rightarrow\hat\beta=\frac{n}{\sum\log x_i}", r"l''(\beta)=-\frac n{\beta^2}\lt 0"], r'\hat\beta=2/(2\log3)=0.910', 48),
 (10, 2, 8, r'\(f(x;\theta)=\dfrac{1}{\theta}e^{-x/\theta}\), \(x\gt 0\) (Parameter im Nenner!)', r'\(2,\ 5,\ 8\)',
  [r'L(\theta)=\theta^{-n}e^{-\sum x_i/\theta}', r'l(\theta)=-n\log\theta-\frac{\sum x_i}{\theta}', r"l'(\theta)=-\frac n\theta+\frac{\sum x_i}{\theta^2}=0\;\big|\cdot\theta^2\Rightarrow -n\theta+\sum x_i=0\Rightarrow\hat\theta=\bar x", r"l''(\theta)=\frac n{\theta^2}-\frac{2\sum x_i}{\theta^3};\ \text{bei }\hat\theta:\ \frac n{\hat\theta^2}-\frac{2n}{\hat\theta^2}=-\frac n{\hat\theta^2}\lt 0"], r'\hat\theta=15/3=5', 52),
 (11, 2, 8, r'Rayleigh: \(f(x;\theta)=\dfrac{x}{\theta}e^{-x^2/(2\theta)}\), \(x\gt 0\)', r'\(1,\ 2,\ 3\)',
  [r'L(\theta)=\theta^{-n}\Big(\prod x_i\Big)e^{-\sum x_i^2/(2\theta)}', r'l(\theta)=-n\log\theta+\sum\log x_i-\frac{\sum x_i^2}{2\theta}', r"l'(\theta)=-\frac n\theta+\frac{\sum x_i^2}{2\theta^2}=0\Rightarrow\hat\theta=\frac{\sum x_i^2}{2n}", r"l''(\hat\theta)=\frac n{\hat\theta^2}-\frac{\sum x_i^2}{\hat\theta^3}=\frac n{\hat\theta^2}-\frac{2n}{\hat\theta^2}=-\frac n{\hat\theta^2}\lt 0"], r'\hat\theta=14/6=2.333', 52),
 (12, 2, 8, r'Verschobene Exponentialverteilung: \(f(x;\theta)=\theta e^{-\theta(x-1)}\), \(x\gt 1\)', r'\(2,\ 3,\ 4\)',
  [r'L(\theta)=\theta^n e^{-\theta\sum(x_i-1)}', r'l(\theta)=n\log\theta-\theta\sum(x_i-1)', r"l'(\theta)=\frac n\theta-\sum(x_i-1)=0\Rightarrow\hat\theta=\frac{n}{\sum(x_i-1)}=\frac{1}{\bar x-1}", r"l''(\theta)=-\frac n{\theta^2}\lt 0"], r'\hat\theta=3/6=0.5', 48),
 (13, 3, 10, r'Weibull mit \(r=2\): \(f(x;\lambda)=r\lambda(\lambda x)^{r-1}e^{-(\lambda x)^r}\). Vereinfachen Sie zuerst!', r'\(1,\ 1\)',
  [r'r=2:\ f(x;\lambda)=2\lambda^2x\,e^{-\lambda^2x^2}', r'L(\lambda)=2^n\lambda^{2n}\Big(\prod x_i\Big)e^{-\lambda^2\sum x_i^2}', r'l(\lambda)=n\log2+2n\log\lambda+\sum\log x_i-\lambda^2\sum x_i^2', r"l'(\lambda)=\frac{2n}{\lambda}-2\lambda\sum x_i^2=0\Rightarrow\lambda^2=\frac{n}{\sum x_i^2}\Rightarrow\hat\lambda=\sqrt{\frac{n}{\sum x_i^2}}", r"l''(\lambda)=-\frac{2n}{\lambda^2}-2\sum x_i^2\lt 0"], r'\hat\lambda=\sqrt{2/2}=1', 62),
 (14, 3, 10, r'Diskret: \(P(X=x)=p(1-p)^{x}\), \(x=0,1,2,\dots\)', r'\(0,\ 1,\ 2,\ 1\)',
  [r'L(p)=p^n(1-p)^{\sum x_i}', r'l(p)=n\log p+\sum x_i\log(1-p)', r"l'(p)=\frac np-\frac{\sum x_i}{1-p}=0\Rightarrow n(1-p)=p\sum x_i\Rightarrow\hat p=\frac{n}{n+\sum x_i}=\frac1{1+\bar x}", r"l''(p)=-\frac n{p^2}-\frac{\sum x_i}{(1-p)^2}\lt 0"], r'\hat p=4/(4+4)=0.5', 62),
 (15, 3, 10, r'Binomial mit bekanntem \(m=10\): \(P(X=x)=\binom{10}{x}\pi^x(1-\pi)^{10-x}\)', r'\(3,\ 5,\ 4\)',
  [r'L(\pi)=\Big(\prod\binom{10}{x_i}\Big)\pi^{\sum x_i}(1-\pi)^{10n-\sum x_i}', r'l(\pi)=\sum\log\binom{10}{x_i}+\sum x_i\log\pi+(10n-\sum x_i)\log(1-\pi)', r"l'(\pi)=\frac{\sum x_i}{\pi}-\frac{10n-\sum x_i}{1-\pi}=0\Rightarrow\hat\pi=\frac{\sum x_i}{10n}", r"l''(\pi)=-\frac{\sum x_i}{\pi^2}-\frac{10n-\sum x_i}{(1-\pi)^2}\lt 0"], r'\hat\pi=12/30=0.4', 62),
 (16, 3, 10, r'Normalverteilung mit \(\mu=0\), gesucht ist \(v=\sigma^2\): \(f(x;v)=\frac{1}{\sqrt{2\pi v}}e^{-x^2/(2v)}\)', r'\(-1,\ 2,\ -2,\ 1\)',
  [r'L(v)=(2\pi v)^{-n/2}e^{-\sum x_i^2/(2v)}', r'l(v)=-\frac n2\log(2\pi)-\frac n2\log v-\frac{\sum x_i^2}{2v}', r"l'(v)=-\frac{n}{2v}+\frac{\sum x_i^2}{2v^2}=0\Rightarrow\hat v=\frac{\sum x_i^2}{n}", r"l''(\hat v)=\frac n{2\hat v^2}-\frac{\sum x_i^2}{\hat v^3}=\frac{n}{2\hat v^2}-\frac{n}{\hat v^2}=-\frac{n}{2\hat v^2}\lt 0"], r'\hat\sigma^2=10/4=2.5', 62),
 (17, 3, 6, r'Gleichverteilung \(U(0,\theta)\): \(f(x;\theta)=\dfrac1\theta\) für \(0\le x\le\theta\). <b>Achtung, Falle!</b>', r'\(2,\ 7,\ 4\)',
  [r'L(\theta)=\theta^{-n}\ \text{falls alle } x_i\le\theta,\ \text{sonst } 0', r"\text{Ableiten hilft nicht: }\theta^{-n}\text{ fällt in }\theta\text{, also }\theta\text{ so klein wie möglich, aber }\theta\ge\max x_i", r'\Rightarrow\hat\theta=\max(x_1,\dots,x_n)'], r'\hat\theta=7', 48),
 (18, 3, 10, r'Lomax: \(f(x;\theta)=\dfrac{\theta}{(1+x)^{\theta+1}}\), \(x\gt 0\)', r'\(1,\ 3\)',
  [r'L(\theta)=\theta^n\prod(1+x_i)^{-(\theta+1)}', r'l(\theta)=n\log\theta-(\theta+1)\sum\log(1+x_i)', r"l'(\theta)=\frac n\theta-\sum\log(1+x_i)=0\Rightarrow\hat\theta=\frac{n}{\sum\log(1+x_i)}", r"l''(\theta)=-\frac n{\theta^2}\lt 0"], r'\hat\theta=2/(\log2+\log4)=0.962', 62),
 (19, 3, 10, r'Gamma mit Form 4: \(f(x;\lambda)=\dfrac{\lambda^4x^3e^{-\lambda x}}{6}\), \(x\gt 0\)', r'\(2,\ 6\)',
  [r'L(\lambda)=6^{-n}\lambda^{4n}\Big(\prod x_i^3\Big)e^{-\lambda\sum x_i}', r'l(\lambda)=-n\log6+4n\log\lambda+3\sum\log x_i-\lambda\sum x_i', r"l'(\lambda)=\frac{4n}{\lambda}-\sum x_i=0\Rightarrow\hat\lambda=\frac{4n}{\sum x_i}=\frac4{\bar x}", r"l''(\lambda)=-\frac{4n}{\lambda^2}\lt 0"], r'\hat\lambda=8/8=1', 62),
]

def task(p):
    nr, st, pts, txt, data, sol, res, h = p
    tagcol = {1: '#2f6b3a', 2: '#a8823a', 3: '#b42318'}[st]
    tagtxt = {1: '●○○ leicht', 2: '●●○ mittel', 3: '●●● Klausur'}[st]
    return (f'<div class="task"><div class="th"><span>Aufgabe {nr}</span><span class="tag" style="color:{tagcol};border-color:{tagcol}">{tagtxt} · {pts} P</span></div>'
            f'{txt}. Bestimmen Sie \\(L\\), \\(l\\), den ML-Schätzer und prüfen Sie die hinreichende Bedingung. Schätzwert für die Stichprobe {data}.'
            f'<div class="box" style="height:{h}mm"></div></div>')

def solution(p):
    nr, st, pts, txt, data, sol, res, h = p
    lines = ''.join(f'<div class="ln">\\(\\displaystyle {s}\\)</div>' for s in sol)
    return f'<div class="sol"><b class="h">Aufgabe {nr}</b> {lines}<div class="ln"><b>Schätzwert:</b> \\({res}\\)</div></div>'

teach = r'''
<div class="kick">Trainingsheft · Maximum-Likelihood · in 60 Minuten klausurfest</div>
<h1>ML: erst <em>verstehen</em>, dann <em>19-mal</em> üben.</h1>
<div class="tr">Plan: 10 dk öğren (sayfa 1–2) → 10 dk Stufe 1 → 20 dk Stufe 2 → 15 dk Stufe 3 → 5 dk Fehlersuche. Çözümler en sonda. Her soruyu önce kendin çöz, sonra kontrol et.</div>

<div class="step"><h2><span>1</span>Die Idee in einem Satz</h2>
Welcher Parameter macht die beobachteten Daten <b>am wahrscheinlichsten</b>? Dazu schreiben wir die Wahrscheinlichkeit der Daten als Funktion des Parameters, \(L(\theta)\), und suchen ihr Maximum: <b>ableiten, null setzen</b>.
<div class="tr">L = verinin olasılığı (parametreye bağlı). En büyük olduğu yer = tepe = türev sıfır.</div></div>

<div class="step"><h2><span>2</span>Das Rezept – jede Aufgabe gleich</h2>
<div class="ln"><span class="n">1</span><b>Likelihood:</b> \(L(\theta)=\prod_{i=1}^n f(x_i;\theta)\) – Produkt hinschreiben und zusammenfassen</div>
<div class="ln"><span class="n">2</span><b>Log-Likelihood:</b> \(l(\theta)=\log L(\theta)\) – Log-Regeln anwenden</div>
<div class="ln"><span class="n">3</span><b>Ableiten</b> nach \(\theta\): Terme ohne \(\theta\) → 0</div>
<div class="ln"><span class="n">4</span><b>Null setzen</b> und nach \(\hat\theta\) auflösen</div>
<div class="ln"><span class="n">5</span><b>2. Ableitung</b> \(\lt 0\) ⇒ Maximum (mit Begründung)</div>
<div class="ln"><span class="n">6</span><b>Zahlen einsetzen:</b> \(n\) = Anzahl der Werte, \(\sum x_i\) = Summe</div>
<div class="tr">(a)(b)(c)'de harflerle çalış (x_i, n, Σ). Sayıları SADECE en son adımda koy.</div></div>

<div class="step"><h2><span>3</span>So zerlegst du jede Dichte – der wichtigste Trick</h2>
Schau jeden Faktor von \(f(x;\theta)\) an und frag: <b>Was passiert, wenn ich ihn \(n\)-mal multipliziere?</b>
<table class="mini" style="width:100%"><tr><th>Faktor in \(f\)</th><th>im Produkt \(L\)</th><th>nach dem Log in \(l\)</th><th>abgeleitet</th></tr>
<tr><td>\(\theta\)</td><td>\(\theta^n\)</td><td>\(n\log\theta\)</td><td>\(\frac n\theta\)</td></tr>
<tr><td>\(\theta^2\)</td><td>\(\theta^{2n}\)</td><td>\(2n\log\theta\)</td><td>\(\frac{2n}\theta\)</td></tr>
<tr><td>\(\frac1\theta\)</td><td>\(\theta^{-n}\)</td><td>\(-n\log\theta\)</td><td>\(-\frac n\theta\)</td></tr>
<tr><td>\(e^{-\theta x}\)</td><td>\(e^{-\theta\sum x_i}\)</td><td>\(-\theta\sum x_i\)</td><td>\(-\sum x_i\)</td></tr>
<tr><td>\(e^{-x/\theta}\)</td><td>\(e^{-\sum x_i/\theta}\)</td><td>\(-\frac{\sum x_i}{\theta}\)</td><td>\(+\frac{\sum x_i}{\theta^2}\)</td></tr>
<tr><td>\(x^{\theta}\)</td><td>\((\prod x_i)^{\theta}\)</td><td>\(\theta\sum\log x_i\)</td><td>\(\sum\log x_i\)</td></tr>
<tr><td>\(x\), \(x^2\), Zahl wie \(2\) (ohne \(\theta\))</td><td>\(\prod x_i\), \(2^n\) …</td><td>\(\sum\log x_i\), \(n\log2\)</td><td><b>0</b></td></tr></table>
<div class="tr">Her parçayı ayrı ayrı düşün: n kere çarp → log al → türev al. Sonra parçaları topla. Hepsi bu!</div></div>

<div class="step pb"><h2><span>4</span>Durchgerechnet: das Klausurmuster in Zeitlupe</h2>
\(f(x;\lambda)=\lambda^2\,x\,e^{-\lambda x}\), Daten \(1,3,2,0.5,3.5\)
<div class="ln"><span class="n">1</span>\(L(\lambda)=\prod\lambda^2x_ie^{-\lambda x_i}=\lambda^{2n}\cdot\prod x_i\cdot e^{-\lambda\sum x_i}\) <span class="timer">Faktor für Faktor aus der Tabelle!</span></div>
<div class="ln"><span class="n">2</span>\(l(\lambda)=2n\log\lambda+\sum\log x_i-\lambda\sum x_i\)</div>
<div class="ln"><span class="n">3</span>\(l'(\lambda)=\dfrac{2n}{\lambda}+0-\sum x_i\)</div>
<div class="ln"><span class="n">4</span>\(\dfrac{2n}{\hat\lambda}=\sum x_i\Rightarrow\hat\lambda=\dfrac{2n}{\sum x_i}\)</div>
<div class="ln"><span class="n">5</span>\(l''(\lambda)=-\dfrac{2n}{\lambda^2}\lt 0\), da \(n\gt 0\) und \(\lambda^2\gt 0\) ⇒ Maximum</div>
<div class="ln"><span class="n">6</span>\(n=5,\ \sum x_i=10\Rightarrow\hat\lambda=\frac{10}{10}=1\)</div></div>

<div class="step"><h2><span>5</span>Auflösen – die 3 Grundmuster für Schritt ④</h2>
<table class="mini" style="width:100%"><tr><th>Gleichung</th><th>Lösung</th></tr>
<tr><td>\(\frac{a}{\theta}-b=0\)</td><td>\(\theta=\frac ab\)</td></tr>
<tr><td>\(\frac{a}{\theta}+b=0\) (z. B. \(b=\sum\log x_i\lt 0\))</td><td>\(\theta=-\frac ab\)</td></tr>
<tr><td>\(-\frac{a}{\theta}+\frac{b}{\theta^2}=0\) &nbsp;(mal \(\theta^2\))</td><td>\(-a\theta+b=0\Rightarrow\theta=\frac ba\)</td></tr>
<tr><td>\(\frac{a}{\theta+1}+b=0\)</td><td>\(\theta+1=-\frac ab\Rightarrow\theta=-\frac ab-1\)</td></tr></table></div>

<div class="warn"><b>⚠ Die 6 Punktekiller</b><br>① Summe statt Produkt in \(L\) · ② \(\log(\theta^{2n})\) nicht zu \(2n\log\theta\) · ③ Konstanten (ohne \(\theta\)) nicht 0 gesetzt · ④ nach \(x_i\) statt \(\theta\) aufgelöst · ⑤ 2. Ableitung ohne Begründung · ⑥ Taschenrechner: <b>log = ln</b></div>

<div class="ok"><b>Punkte-Retter:</b> Schritt ① und ② gehen IMMER – das sind schon ca. 4 von 10 Punkten. Nie leer lassen!</div>
'''

fehler = r'''
<div class="lvl pb" style="background:#6a1b9a">Fehlersuche – finde den Fehler (5 Minuten)</div>
<div class="task"><div class="th"><span>F1</span></div>\(f(x;\lambda)=\lambda e^{-\lambda x}\). Ein Student schreibt: \(L(\lambda)=\sum_{i=1}^n\lambda e^{-\lambda x_i}\). Was ist falsch?<div class="box" style="height:14mm"></div></div>
<div class="task"><div class="th"><span>F2</span></div>\(l(\lambda)=2n\log\lambda+\sum\log x_i-\lambda\sum x_i\). Ein Student leitet ab: \(l'(\lambda)=\frac{2n}{\lambda}+\sum\frac{1}{x_i}-\sum x_i\). Was ist falsch?<div class="box" style="height:14mm"></div></div>
<div class="task"><div class="th"><span>F3</span></div>\(f(x;\theta)=\theta x^{\theta-1}\), Daten \(0.5,0.5\). Eine Studentin erhält \(\hat\theta=3.322\). Wo liegt der Fehler?<div class="box" style="height:14mm"></div></div>
<div class="task"><div class="th"><span>F4</span></div>\(L(\lambda)=\lambda^{3n}e^{-\lambda\sum x_i}\). Ein Student schreibt: \(l(\lambda)=\log(3n\lambda)-\lambda\sum x_i\). Was ist falsch?<div class="box" style="height:14mm"></div></div>
'''
fehler_sol = r'''<div class="sol"><b class="h">Fehlersuche</b>
<div class="ln"><b>F1:</b> Produkt statt Summe: \(L(\lambda)=\prod\lambda e^{-\lambda x_i}=\lambda^ne^{-\lambda\sum x_i}\).</div>
<div class="ln"><b>F2:</b> \(\sum\log x_i\) enthält kein \(\lambda\) → Ableitung 0, nicht \(\sum\frac1{x_i}\). Richtig: \(l'=\frac{2n}{\lambda}-\sum x_i\).</div>
<div class="ln"><b>F3:</b> \(\log_{10}\) statt \(\ln\) benutzt: \(-2/(2\cdot(-0.301))=3.322\). Richtig mit ln: \(-2/(2\cdot(-0.6931))=1.443\).</div>
<div class="ln"><b>F4:</b> \(\log(\lambda^{3n})=3n\log\lambda\), nicht \(\log(3n\lambda)\). Richtig: \(l=3n\log\lambda-\lambda\sum x_i\).</div></div>'''

body = [CSS, teach]
body.append('<div class="pb"></div>' + lvl('Stufe 1 · Aufwärmen · bekannte Verteilungen (10 Minuten)', '#2f6b3a'))
body += [task(p) for p in P if p[1] == 1]
body.append(lvl('Stufe 2 · Klausurtypen · Faktoren zerlegen (20 Minuten)', '#a8823a'))
body += [task(p) for p in P if p[1] == 2]
body.append(lvl('Stufe 3 · Klausur+ · Fallen und Umformungen (15 Minuten)', '#b42318'))
body += [task(p) for p in P if p[1] == 3]
body.append(fehler)
body.append('<div class="lvl pb" style="background:#1f4e79">Lösungen – erst nach dem eigenen Versuch ansehen!</div>')
body += [solution(p) for p in P]
body.append(fehler_sol)
body.append('<div class="ok"><b>Selbsttest:</b> Schaffst du eine Aufgabe aus Stufe 3 in unter 10 Minuten ohne Nachsehen? Dann bist du klausurfest. ✓<div class="tr">Stufe 3\'ten bir soruyu 10 dakikada bakmadan çözebiliyorsan hazırsın.</div></div>')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write('\n'.join(body))
print(OUT)
