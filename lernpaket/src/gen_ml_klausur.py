# ML-Klausurtraining im Probeklausur-Layout (Aufgaben + Musterlösung mit Bewertungsschlüssel)
import os
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, 'content')

STD = [  # Standard-Teilaufgaben (10 P)
    ('Stellen Sie zunächst die Likelihood- und die Log-Likelihood-Funktion auf. Geben Sie Ihren vollständigen Lösungsweg an und vereinfachen Sie Ihr Endresultat so weit wie möglich.', 4, 'l'),
    ('Bestimmen Sie auf Grundlage Ihres Ergebnisses aus (a) den Maximum-Likelihood-Schätzer. Geben Sie Ihren vollständigen Lösungsweg an.', 3, 'l'),
    ('Prüfen Sie die hinreichende Bedingung (Bedingung zweiter Ordnung).', 2, 'm'),
]

# (Titel/Kontext, Dichte-HTML, Parametertext, Daten, extra Teilaufgaben, Lösung: Liste (Teil, Text mit Punkten))
A = [
 dict(ctx=r'Die Wartezeit \(X\) (in Minuten) an der Kasse der Zentralmensa werde durch eine Zufallsvariable mit der Dichte', f=r'f(x;\lambda)=\begin{cases}\lambda\,e^{-\lambda x}, & x&gt;0\\ 0, & \text{sonst}\end{cases}\qquad\lambda&gt;0', par=r'\lambda', data=r'x=(1,\ 2,\ 3)',
      extra=[('Schätzen Sie mithilfe Ihres Schätzwertes die Wahrscheinlichkeit, länger als 2 Minuten zu warten. (Hinweis: \\(P(X&gt;x)=e^{-\\lambda x}\\))', 1, 's')],
      sol=[r'(a) \(L(\lambda)=\prod_{i=1}^n\lambda e^{-\lambda x_i}=\lambda^n e^{-\lambda\sum x_i}\) [2] · \(l(\lambda)=n\log\lambda-\lambda\sum x_i\) [2]',
           r"(b) \(l'(\lambda)=\frac n\lambda-\sum x_i\) [1] · \(=0\Rightarrow\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}\) [2]",
           r"(c) \(l''(\lambda)=-\frac{n}{\lambda^2}&lt;0\), da \(n&gt;0,\ \lambda^2&gt;0\) ⇒ Maximum [2]",
           r'(d) \(\hat\lambda=\frac36=0.5\) [1]', r'(e) \(P(X&gt;2)\approx e^{-0.5\cdot2}=e^{-1}=0.368\) [1]']),
 dict(ctx=r'Die Anzahl \(X\) der E-Mails, die eine Studentin pro Stunde in ihrem Uni-Postfach erhält, sei poissonverteilt mit der Wahrscheinlichkeitsfunktion', f=r'P(X=x)=\frac{\lambda^{x}e^{-\lambda}}{x!},\qquad x=0,1,2,\dots,\quad\lambda&gt;0', par=r'\lambda', data=r'x=(2,\ 3,\ 1,\ 2)',
      extra=[('Berechnen Sie mit Ihrem Schätzwert die Wahrscheinlichkeit, dass in einer Stunde keine E-Mail eintrifft.', 1, 's')],
      sol=[r'(a) \(L(\lambda)=\prod\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}=\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}\) [2] · \(l(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log(x_i!)\) [2]',
           r"(b) \(l'(\lambda)=\frac{\sum x_i}{\lambda}-n\) [1] · \(=0\Rightarrow\hat\lambda=\frac{\sum x_i}{n}=\bar x\) [2]",
           r"(c) \(l''(\lambda)=-\frac{\sum x_i}{\lambda^2}&lt;0\) (da \(x_i\ge0\), nicht alle 0) [2]",
           r'(d) \(\hat\lambda=\frac84=2\) [1]', r'(e) \(P(X=0)=e^{-2}=0.135\) [1]']),
 dict(ctx=r'Die Bearbeitungszeit \(X\) (in Stunden) eines Statistik-Übungsblattes werde durch die Dichte', f=r'f(x;\lambda)=\begin{cases}\tfrac12\lambda^3x^2e^{-\lambda x}, & x&gt;0\\ 0, & \text{sonst}\end{cases}\qquad\lambda&gt;0', par=r'\lambda', data=r'x=(2,\ 4)', extra=[],
      sol=[r'(a) \(L(\lambda)=\prod\tfrac12\lambda^3x_i^2e^{-\lambda x_i}=2^{-n}\lambda^{3n}\big(\prod x_i^2\big)e^{-\lambda\sum x_i}\) [2] · \(l(\lambda)=-n\log2+3n\log\lambda+2\sum\log x_i-\lambda\sum x_i\) [2]',
           r"(b) \(l'(\lambda)=\frac{3n}{\lambda}-\sum x_i\) [1] · \(\hat\lambda=\frac{3n}{\sum x_i}=\frac3{\bar x}\) [2]", r"(c) \(l''(\lambda)=-\frac{3n}{\lambda^2}&lt;0\) [2]", r'(d) \(\hat\lambda=\frac{6}{6}=1\) [1]']),
 dict(ctx=r'Der Anteil \(X\) richtig beantworteter Fragen in einem Online-Quiz werde durch die Dichte', f=r'f(x;\theta)=\begin{cases}\theta\,x^{\theta-1}, & 0&lt;x&lt;1\\ 0, & \text{sonst}\end{cases}\qquad\theta&gt;0', par=r'\theta', data=r'x=(0.5,\ 0.5)', extra=[],
      sol=[r'(a) \(L(\theta)=\theta^n\big(\prod x_i\big)^{\theta-1}\) [2] · \(l(\theta)=n\log\theta+(\theta-1)\sum\log x_i\) [2]',
           r"(b) \(l'(\theta)=\frac n\theta+\sum\log x_i\) [1] · \(\hat\theta=-\frac{n}{\sum\log x_i}\) [2]", r"(c) \(l''(\theta)=-\frac n{\theta^2}&lt;0\) [2]",
           r'(d) \(\sum\log x_i=2\log0.5=-1.3863\Rightarrow\hat\theta=\frac{2}{1.3863}=1.443\) [1] (Taschenrechner: ln!)']),
 dict(ctx=r'Der Abstand \(X\) (in km) zwischen Wohnung und nächster Bushaltestelle werde durch die Dichte', f=r'f(x;\theta)=\begin{cases}2\theta\,x\,e^{-\theta x^2}, & x&gt;0\\ 0, & \text{sonst}\end{cases}\qquad\theta&gt;0', par=r'\theta', data=r'x=(0.5,\ 1,\ 1.5)', extra=[],
      sol=[r'(a) \(L(\theta)=2^n\theta^n\big(\prod x_i\big)e^{-\theta\sum x_i^2}\) [2] · \(l(\theta)=n\log2+n\log\theta+\sum\log x_i-\theta\sum x_i^2\) [2]',
           r"(b) \(l'(\theta)=\frac n\theta-\sum x_i^2\) [1] · \(\hat\theta=\frac{n}{\sum x_i^2}\) [2]", r"(c) \(l''(\theta)=-\frac n{\theta^2}&lt;0\) [2]",
           r'(d) \(\sum x_i^2=0.25+1+2.25=3.5\Rightarrow\hat\theta=\frac{3}{3.5}=0.857\) [1]']),
 dict(ctx=r'Die Schadenshöhe \(X\) (in Tausend Euro) bei einer Fahrradversicherung werde durch die Pareto-Dichte', f=r'f(x;\beta)=\begin{cases}\dfrac{\beta}{x^{\beta+1}}, & x&gt;1\\ 0, & \text{sonst}\end{cases}\qquad\beta&gt;0', par=r'\beta', data=r'x=(3,\ 3)', extra=[],
      sol=[r'(a) \(L(\beta)=\beta^n\big(\prod x_i\big)^{-(\beta+1)}\) [2] · \(l(\beta)=n\log\beta-(\beta+1)\sum\log x_i\) [2]',
           r"(b) \(l'(\beta)=\frac n\beta-\sum\log x_i\) [1] · \(\hat\beta=\frac{n}{\sum\log x_i}\) [2]", r"(c) \(l''(\beta)=-\frac n{\beta^2}&lt;0\) [2]",
           r'(d) \(\hat\beta=\frac{2}{2\log3}=\frac{1}{1.0986}=0.910\) [1]']),
 dict(ctx=r'Die Lebensdauer \(X\) (in Jahren) eines Laptop-Akkus werde durch die Dichte', f=r'f(x;\theta)=\begin{cases}\dfrac{1}{\theta}\,e^{-x/\theta}, & x&gt;0\\ 0, & \text{sonst}\end{cases}\qquad\theta&gt;0', par=r'\theta', data=r'x=(2,\ 5,\ 8)',
      extra=[('Interpretieren Sie den Parameter \\(\\theta\\) (Hinweis: \\(E(X)=\\theta\\)).', 1, 's')],
      sol=[r'(a) \(L(\theta)=\theta^{-n}e^{-\sum x_i/\theta}\) [2] · \(l(\theta)=-n\log\theta-\frac{\sum x_i}{\theta}\) [2]',
           r"(b) \(l'(\theta)=-\frac n\theta+\frac{\sum x_i}{\theta^2}\) [1] · \(\cdot\theta^2:\ -n\theta+\sum x_i=0\Rightarrow\hat\theta=\bar x\) [2]",
           r"(c) \(l''(\theta)=\frac n{\theta^2}-\frac{2\sum x_i}{\theta^3}\); an \(\hat\theta=\frac{\sum x_i}{n}\): \(\frac{n}{\hat\theta^2}-\frac{2n}{\hat\theta^2}=-\frac{n}{\hat\theta^2}&lt;0\) [2]",
           r'(d) \(\hat\theta=\frac{15}{3}=5\) [1]', r'(e) \(\theta\) ist die erwartete Lebensdauer; geschätzt hält ein Akku im Mittel 5 Jahre [1]']),
 dict(ctx=r'Die Windgeschwindigkeit \(X\) (in m/s) an der Wetterstation Göttingen werde durch die Rayleigh-Dichte', f=r'f(x;\theta)=\begin{cases}\dfrac{x}{\theta}\,e^{-x^2/(2\theta)}, & x&gt;0\\ 0, & \text{sonst}\end{cases}\qquad\theta&gt;0', par=r'\theta', data=r'x=(1,\ 2,\ 3)', extra=[],
      sol=[r'(a) \(L(\theta)=\theta^{-n}\big(\prod x_i\big)e^{-\sum x_i^2/(2\theta)}\) [2] · \(l(\theta)=-n\log\theta+\sum\log x_i-\frac{\sum x_i^2}{2\theta}\) [2]',
           r"(b) \(l'(\theta)=-\frac n\theta+\frac{\sum x_i^2}{2\theta^2}\) [1] · \(\hat\theta=\frac{\sum x_i^2}{2n}\) [2]",
           r"(c) \(l''(\hat\theta)=\frac n{\hat\theta^2}-\frac{\sum x_i^2}{\hat\theta^3}=\frac n{\hat\theta^2}-\frac{2n}{\hat\theta^2}=-\frac n{\hat\theta^2}&lt;0\) [2]",
           r'(d) \(\hat\theta=\frac{1+4+9}{6}=\frac{7}{3}=2.333\) [1]']),
 dict(ctx=r'Die Zeit \(X\) (in Monaten) bis zum Ausfall eines Kaffeeautomaten sei Weibull-verteilt mit Dichte \(f(x;\lambda,r)=r\lambda(\lambda x)^{r-1}\exp(-(\lambda x)^r)\) für \(x&gt;0\). Nehmen Sie im Folgenden \(r=2\) an. Damit ist die Dichte', f=r'f(x;\lambda)=\;?\qquad\lambda&gt;0', par=r'\lambda', data=r'x=(1,\ 1)',
      pre=[('Vereinfachen Sie die Dichte für \\(r=2\\).', 1, 's')], extra=[],
      sol=[r'(a) \(f(x;\lambda)=2\lambda(\lambda x)e^{-(\lambda x)^2}=2\lambda^2x\,e^{-\lambda^2x^2}\) [1]',
           r'(b) \(L(\lambda)=2^n\lambda^{2n}\big(\prod x_i\big)e^{-\lambda^2\sum x_i^2}\) [2] · \(l(\lambda)=n\log2+2n\log\lambda+\sum\log x_i-\lambda^2\sum x_i^2\) [2]',
           r"(c) \(l'(\lambda)=\frac{2n}{\lambda}-2\lambda\sum x_i^2\) [1] · \(=0\Rightarrow\lambda^2=\frac{n}{\sum x_i^2}\Rightarrow\hat\lambda=\sqrt{\frac{n}{\sum x_i^2}}\) [2]",
           r"(d) \(l''(\lambda)=-\frac{2n}{\lambda^2}-2\sum x_i^2&lt;0\) [2]", r'(e) \(\hat\lambda=\sqrt{2/2}=1\) [1]']),
 dict(ctx=r'Beim Basketball-Training zählt eine Spielerin die Anzahl \(X\) der Fehlwürfe vor dem ersten Treffer. \(X\) habe die Wahrscheinlichkeitsfunktion', f=r'P(X=x)=p\,(1-p)^{x},\qquad x=0,1,2,\dots,\quad 0&lt;p&lt;1', par=r'p', data=r'x=(0,\ 1,\ 2,\ 1)', extra=[],
      sol=[r'(a) \(L(p)=p^n(1-p)^{\sum x_i}\) [2] · \(l(p)=n\log p+\sum x_i\log(1-p)\) [2]',
           r"(b) \(l'(p)=\frac np-\frac{\sum x_i}{1-p}\) [1] · \(n(1-p)=p\sum x_i\Rightarrow\hat p=\frac{n}{n+\sum x_i}=\frac1{1+\bar x}\) [2]",
           r"(c) \(l''(p)=-\frac{n}{p^2}-\frac{\sum x_i}{(1-p)^2}&lt;0\) [2]", r'(d) \(\hat p=\frac{4}{4+4}=0.5\) [1]']),
 dict(ctx=r'Der Messfehler \(X\) (in Gramm) einer Laborwaage sei normalverteilt mit Erwartungswert \(0\) und unbekannter Varianz \(v=\sigma^2\), also', f=r'f(x;v)=\frac{1}{\sqrt{2\pi v}}\exp\!\Big(-\frac{x^2}{2v}\Big),\qquad v&gt;0', par=r'v=\sigma^2', data=r'x=(-1,\ 2,\ -2,\ 1)', extra=[],
      sol=[r'(a) \(L(v)=(2\pi v)^{-n/2}e^{-\sum x_i^2/(2v)}\) [2] · \(l(v)=-\frac n2\log(2\pi)-\frac n2\log v-\frac{\sum x_i^2}{2v}\) [2]',
           r"(b) \(l'(v)=-\frac{n}{2v}+\frac{\sum x_i^2}{2v^2}\) [1] · \(\hat v=\frac{\sum x_i^2}{n}\) [2]",
           r"(c) \(l''(\hat v)=\frac{n}{2\hat v^2}-\frac{\sum x_i^2}{\hat v^3}=\frac{n}{2\hat v^2}-\frac{n}{\hat v^2}=-\frac{n}{2\hat v^2}&lt;0\) [2]", r'(d) \(\hat\sigma^2=\frac{1+4+4+1}{4}=2.5\) [1]']),
 dict(ctx=r'Die Gesamtdauer \(X\) (in Minuten) von vier aufeinanderfolgenden Telefonaten im Studierendenservice werde durch die Dichte', f=r'f(x;\lambda)=\begin{cases}\dfrac{\lambda^4x^3e^{-\lambda x}}{6}, & x&gt;0\\ 0, & \text{sonst}\end{cases}\qquad\lambda&gt;0', par=r'\lambda', data=r'x=(2,\ 6)', extra=[],
      sol=[r'(a) \(L(\lambda)=6^{-n}\lambda^{4n}\big(\prod x_i^3\big)e^{-\lambda\sum x_i}\) [2] · \(l(\lambda)=-n\log6+4n\log\lambda+3\sum\log x_i-\lambda\sum x_i\) [2]',
           r"(b) \(l'(\lambda)=\frac{4n}{\lambda}-\sum x_i\) [1] · \(\hat\lambda=\frac{4n}{\sum x_i}=\frac4{\bar x}\) [2]", r"(c) \(l''(\lambda)=-\frac{4n}{\lambda^2}&lt;0\) [2]", r'(d) \(\hat\lambda=\frac{8}{8}=1\) [1]']),
]

def letters():
    return 'abcdefg'

def aufgabe(i, a):
    parts = list(a.get('pre', [])) + STD + [(f'Berechnen Sie den Schätzwert für die Stichprobe \\({a["data"]}\\).', 1, 's')] + a['extra']
    pts = sum(p for _, p, _ in parts)
    pb = ' kl-pb' if i > 1 else ''
    h = f'<div class="kl-auf{pb}"><h2><span>Aufgabe {i}</span><span>({pts:g} Punkte)</span></h2>'
    h += f'<p>{a["ctx"]}</p><p style="text-align:center">\\({a["f"]}\\)</p>'
    if 'pre' not in a:
        h += f'<p>beschrieben. Bestimmen Sie den Maximum-Likelihood-Schätzer für \\({a["par"]}\\) basierend auf einer Stichprobe von \\(n\\) Beobachtungen \\(X_1,\\dots,X_n\\), die unabhängig und identisch verteilt sind.</p>'
    else:
        h += f'<p>Bestimmen Sie den Maximum-Likelihood-Schätzer für \\({a["par"]}\\) basierend auf einer iid-Stichprobe \\(X_1,\\dots,X_n\\).</p>'
    h += '<ol class="tl">'
    for k, (txt, p, size) in enumerate(parts):
        h += f'<li><span class="lb">({letters()[k]})</span>{txt} <span class="pt">({p:g} P)</span><div class="lk {size}"></div></li>'
    h += '</ol></div>'
    return h, pts

def uniform(i):
    h = f'''<div class="kl-auf kl-pb"><h2><span>Aufgabe {i} (Sonderfall)</span><span>(5 Punkte)</span></h2>
<p>Die Verspätung \\(X\\) (in Minuten) der Straßenbahn sei gleichverteilt auf \\([0,\\theta]\\) mit unbekanntem \\(\\theta&gt;0\\), d. h. \\(f(x;\\theta)=\\frac1\\theta\\) für \\(0\\le x\\le\\theta\\) und \\(0\\) sonst.</p>
<ol class="tl"><li><span class="lb">(a)</span>Stellen Sie die Likelihood-Funktion auf. Beachten Sie, für welche \\(\\theta\\) sie positiv ist. <span class="pt">(2 P)</span><div class="lk m"></div></li>
<li><span class="lb">(b)</span>Warum führt Ableiten und Nullsetzen hier nicht zum Ziel? Bestimmen Sie den ML-Schätzer. <span class="pt">(2 P)</span><div class="lk m"></div></li>
<li><span class="lb">(c)</span>Berechnen Sie den Schätzwert für \\(x=(2,\\ 7,\\ 4)\\). <span class="pt">(1 P)</span><div class="lk s"></div></li></ol></div>'''
    sol = [r'(a) \(L(\theta)=\prod\frac1\theta=\theta^{-n}\), falls \(\theta\ge\max x_i\), sonst \(L(\theta)=0\) [2]',
           r"(b) \(L(\theta)=\theta^{-n}\) ist streng fallend, \(l'(\theta)=-\frac n\theta\ne0\) hat keine Nullstelle; \(L\) wird maximal für das kleinste zulässige \(\theta\): \(\hat\theta=\max(x_1,\dots,x_n)\) [2]",
           r'(c) \(\hat\theta=7\) [1]']
    return h, 5, sol

deck = r'''<section class="t0 kl">
<div class="kl-deck">
<h1>ML-Klausurtraining (Teil A)</h1>
<div class="sub">Statistik und Data Science I · Aufgabentyp „Maximum-Likelihood“ · 13 Aufgaben im Originalformat<br><span class="small">Übungsheft zur Vorbereitung – keine offizielle Klausur</span></div>
<div class="kl-fields"><div>Name, Vorname</div><div>Matrikel-Nr.</div><div>Startzeit</div><div>Endzeit</div></div>
<p><b>Empfohlene Bearbeitungszeit:</b> 60 Minuten für Aufgaben 1–8 (ca. 7 Minuten pro Aufgabe, wie in der Klausur) · Aufgaben 9–13 als Zusatztraining · <b>Gesamtpunktzahl:</b> @@SUM@@</p>
<table class="kl-pt"><tr><th>Aufgabe</th>@@NRS@@<th>Σ</th></tr><tr><th>Punkte</th>@@PTS@@<th>@@SUM@@</th></tr><tr><th>erreicht</th>@@EMPTY@@<th></th></tr></table>
<div class="kl-hin">
<h3>Hinweise</h3>
<ul>
<li>Jede Aufgabe ist wie die ML-Aufgabe der echten Klausur aufgebaut: (a) Likelihood und Log-Likelihood, (b) ML-Schätzer, (c) hinreichende Bedingung, (d) Schätzwert.</li>
<li>Rechnen Sie in (a)–(c) <b>allgemein</b> mit \(x_1,\dots,x_n\). Zahlen werden erst in (d) eingesetzt.</li>
<li>Mit \(\log\) ist stets der natürliche Logarithmus gemeint (Taschenrechner: <b>ln</b>). Ergebnisse auf drei Nachkommastellen.</li>
<li>Geben Sie bei jeder Teilaufgabe Ihren vollständigen Lösungsweg an – die Punkte gibt es für die Zwischenschritte.</li>
<li>Die Musterlösung mit Bewertungsschlüssel liegt separat bei. Erst selbst rechnen, dann vergleichen!</li>
</ul>
<p><i>Selbsttest: Schaffst du eine Aufgabe in unter 8 Minuten ohne Formelsammlung, bist du klausurfest.</i></p>
</div>
</div>
'''

body, pts_list, sols = [], [], []
for i, a in enumerate(A, 1):
    h, p = aufgabe(i, a); body.append(h); pts_list.append(p); sols.append((i, p, a['sol']))
h, p, s = uniform(len(A) + 1); body.append(h); pts_list.append(p); sols.append((len(A) + 1, p, s))
tot = sum(pts_list)
d = deck.replace('@@SUM@@', f'{tot:g}').replace('@@NRS@@', ''.join(f'<td>{i}</td>' for i in range(1, len(pts_list) + 1)))
d = d.replace('@@PTS@@', ''.join(f'<td>{p:g}</td>' for p in pts_list)).replace('@@EMPTY@@', '<td></td>' * len(pts_list))
open(os.path.join(C, 'mlk_a.html'), 'w').write(d + '\n'.join(body) + '\n</section>\n')

L = ['<section class="t1 loes"><h2>Musterlösung · ML-Klausurtraining</h2>',
     '<p class="small">Punkte in eckigen Klammern = Bewertungsschlüssel wie in der Klausur. Alle Schätzwerte sind nachgerechnet. Folgefehler werden berücksichtigt.</p>']
for i, p, s in sols:
    L.append(f'<h3>Aufgabe {i} ({p:g} P)</h3><p>' + '<br>'.join(s) + '</p>')
L.append('</section>')
open(os.path.join(C, 'mlk_loes.html'), 'w').write('\n'.join(L))
print('ok', tot)
