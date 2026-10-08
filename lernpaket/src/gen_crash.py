# Crashkurse (persönlich): Schätzer erwartungstreu · Bayes/totale W'keit · Hypothesentests
# Aufbau je Heft: Deckblatt -> (Lerneinheit -> Übung im Klausurlayout) x k -> komplette Klausuraufgaben -> Lösungen
import os
HERE = os.path.dirname(os.path.abspath(__file__))

CSS = r'''<style>
.lern{border:2px solid var(--c,#1f4e79);border-radius:10px;margin:0 0 5mm;overflow:hidden}
.lern .lh1{background:var(--c,#1f4e79);color:#fff;padding:2.5mm 4mm;font-weight:800;font-size:1.05rem;display:flex;justify-content:space-between}
.lern .lh1 small{font-weight:600;opacity:.85}
.lern .lb2{padding:2mm 4mm 3mm;font-size:.92rem;line-height:1.55}
.lern h4{margin:2.5mm 0 1mm;color:var(--c,#1f4e79);font-size:.97rem}
.tr{display:block;background:#e3f4f2;border-left:3px solid #00796b;padding:1.5mm 3mm;margin:2mm 0;color:#0f4f47;border-radius:0 6px 6px 0}
.vg{background:#f4f6fa;border-left:3px solid var(--c,#1f4e79);padding:1.5mm 3mm;margin:2mm 0;border-radius:0 6px 6px 0}
.vg b.t{display:block;color:var(--c,#1f4e79);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase}
.fe{background:#fdeeec;border-left:3px solid #c62828;padding:1.5mm 3mm;margin:2mm 0;border-radius:0 6px 6px 0}
.du{background:#fff7e0;border-left:3px solid #e0a100;padding:1.5mm 3mm;margin:2mm 0;border-radius:0 6px 6px 0}
.lern table{border-collapse:collapse;width:100%;font-size:.88rem;margin:1.5mm 0}
.lern td,.lern th{border:1px solid #cfd6e0;padding:1mm 2mm;text-align:left;vertical-align:top}
.lern th{background:#eef1f6}
.ueb h2{border-bottom-color:#a8823a!important;color:#7a5d22!important}
.unit-tag{display:inline-block;background:#a8823a;color:#fff;border-radius:4px;padding:0 6px;font-size:.7rem;margin-right:6px;vertical-align:middle}
.loesk h3{color:#2f6b3a;margin-top:4mm}
.loesk p{line-height:1.6}
.tree{display:block;margin:2mm auto}
</style>'''

def lern(nr, title, minutes, html, color):
    return f'<div class="lern kl-pb" style="--c:{color}"><div class="lh1"><span>Lerneinheit {nr} · {title}</span><small>ca. {minutes} min</small></div><div class="lb2">{html}</div></div>'

def uebung(nr, title, items):
    lis = ''.join(f'<li><span class="lb">({chr(97+k)})</span>{q} <span class="pt">(1 P)</span><div class="lk {sz}"></div></li>'
                  for k, (q, _, sz) in enumerate(items))
    return f'<div class="kl-auf ueb"><h2><span><span class="unit-tag">E{nr}</span>Übung {nr}: {title}</span><span>({len(items)} Punkte)</span></h2><ol class="tl">{lis}</ol></div>'

def klausur(i, title, pts, ctx, parts):
    h = f'<div class="kl-auf kl-pb"><h2><span>Klausuraufgabe {i} · {title}</span><span>({pts} Punkte)</span></h2><p>{ctx}</p><ol class="tl">'
    for k, (q, p, sz, _) in enumerate(parts):
        h += f'<li><span class="lb">({chr(97+k)})</span>{q} <span class="pt">({p} P)</span><div class="lk {sz}"></div></li>'
    return h + '</ol></div>'

def deck(title, sub, plan_rows, tip):
    rows = ''.join(f'<li>{r}</li>' for r in plan_rows)
    return f'''<section class="t0 kl"><div class="kl-deck"><h1>{title}</h1>
<div class="sub">{sub}<br><span class="small">Persönliches Übungsheft – keine offizielle Klausur</span></div>
<div class="kl-hin"><h3>So arbeitest du</h3><ul>{rows}</ul>
<div class="tr">{tip}</div></div></div>'''

def build(name, color, d, units, klaus):
    out = [CSS, d]
    for k, (title, mins, html, items) in enumerate(units, 1):
        out.append(lern(k, title, mins, html, color))
        out.append(uebung(k, title, items))
    for i, (t, pts, ctx, parts) in enumerate(klaus, 1):
        out.append(klausur(i, t, pts, ctx, parts))
    out.append('</section>')
    S = ['<section class="t1 loes loesk" style="page-break-before:always"><h2>Lösungen</h2><p class="small">Erst selbst lösen, dann vergleichen. Bei den Klausuraufgaben steht in eckigen Klammern, wofür es Punkte gibt.</p>']
    for k, (title, _, _, items) in enumerate(units, 1):
        S.append(f'<h3>Übung {k}: {title}</h3><p>' + '<br>'.join(f'({chr(97+j)}) {s}' for j, (_, s, _) in enumerate(items)) + '</p>')
    for i, (t, _, _, parts) in enumerate(klaus, 1):
        S.append(f'<h3>Klausuraufgabe {i} · {t}</h3><p>' + '<br>'.join(f'({chr(97+j)}) {s}' for j, (_, _, _, s) in enumerate(parts)) + '</p>')
    S.append('</section>')
    html = '\n'.join(out) + '\n' + '\n'.join(S)
    html = html.replace("\\'", "'")
    open(os.path.join(HERE, 'content', 'extra', name), 'w').write(html)

# =====================================================================================
# HEFT 1: SCHÄTZER – ERWARTUNGSTREU
# =====================================================================================
C1 = '#c55a11'
S_units = []
S_units.append(('Was bedeutet \\(E(X)\\) und \\(X_i\\)?', 8, r'''
<h4>Die Situation in der Klausur</h4>
In der Aufgabe steht z. B.: <i>„Sei \(X\) eine Zufallsvariable mit \(E(X)=\frac{\alpha}{4}\). Sie ziehen eine Stichprobe \(X_1,\dots,X_n\). Testen Sie, ob der Schätzer \(\hat\alpha=\dots\) unverzerrt ist.“</i>
<span class="tr">Korkma: bu soruda integral yok, türev yok. Sadece 3 basit kural var (Lerneinheit 2–3). Bu sorunun tamamı ~5 puan ve sen bunu 5 dakikada çözebileceksin.</span>
<h4>\(X_1,\dots,X_n\) ne demek?</h4>
\(X_i\) = \(i\)-inci kişinin / ölçümün değeri. Daha ölçmediğimiz için <b>rastgele</b>. Hepsi aynı dağılımdan geliyor, yani <b>hepsinin beklenen değeri aynı</b>:
\[E(X_1)=E(X_2)=\dots=E(X_n)=E(X)\]
<span class="tr">Sınıftan rastgele 5 öğrenci seçip boyunu ölçüyoruz: X₁ = 1. öğrencinin boyu, X₂ = 2. öğrencinin boyu… Hangisi olursa olsun, "ortalama beklenen boy" aynıdır.</span>
<h4>\(E(X)\) ne demek?</h4>
\(E(X)\) = <b>uzun vadede ortalama</b> (Erwartungswert). Adil zar: \(E(X)=3.5\).
<div class="vg"><b class="t">Wichtig</b>Wenn in der Aufgabe \(E(X)=\frac\alpha4\) steht, dann gilt <b>für jedes</b> \(X_i\): \(E(X_1)=\frac\alpha4\), \(E(X_n)=\frac\alpha4\), \(E(X_7)=\frac\alpha4\).</div>
<h4>Die griechischen Buchstaben</h4>
\(\mu\) (mü), \(\theta\) (theta), \(\alpha\) (alpha), \(\kappa\) (kappa), \(\lambda\) (lambda) sind <b>einfach unbekannte Zahlen</b> (Parameter). Du rechnest mit ihnen wie mit \(a\) oder \(b\).
<span class="tr">θ'yı "a" gibi düşün. "E(X) = θ/2" → "ortalama, a'nın yarısı". Bu harfler sabit sayılar; rastgele olan sadece X'ler.</span>
<h4>Was ist ein Schätzer?</h4>
Eine Formel aus den Daten, die einen unbekannten Parameter schätzen soll, z. B. \(\bar X=\frac1n\sum X_i\) für \(\mu\).<br>
<b>Erwartungstreu (= unverzerrt)</b> heißt: <b>im Mittel trifft der Schätzer genau</b>, d. h.
\[E(\text{Schätzer})=\text{Parameter}\]
<span class="tr">Ok atıcı benzetmesi: erwartungstreu = oklar hedefin etrafına dağılıyor ama ORTALAMASI tam merkezde. Verzerrt = hep sola kayıyor.</span>''',
 [(r'\(E(X)=\mu\). Was ist \(E(X_4)\)?', r'\(\mu\) (jedes \(X_i\) hat denselben Erwartungswert)', 's'),
  (r'\(E(X)=\frac\theta2\). Was ist \(E(X_1)\) und \(E(X_n)\)?', r'beide \(\frac\theta2\)', 's'),
  (r'Was muss gelten, damit \(T\) ein erwartungstreuer Schätzer für \(\kappa\) ist?', r'\(E(T)=\kappa\)', 's')]))

S_units.append(('Regel 1: Konstanten herausziehen', 8, r'''
<h4>Die drei Mini-Regeln</h4>
<table><tr><th>Regel</th><th>Beispiel mit \(E(X)=\mu\)</th><th>Türkçe</th></tr>
<tr><td>\(E(a\cdot X)=a\cdot E(X)\)</td><td>\(E(3X_1)=3\mu\)</td><td>önündeki sayı dışarı çıkar</td></tr>
<tr><td>\(E\big(\frac{X}{a}\big)=\frac{E(X)}{a}\)</td><td>\(E\big(\frac{X_n}{\alpha}\big)=\frac{\mu}{\alpha}\)</td><td>bölen sabitse o da dışarı (α sabit!)</td></tr>
<tr><td>\(E(b)=b\) für eine Konstante</td><td>\(E\big(\frac14\big)=\frac14\), \(E(-2)=-2\)</td><td>sabit sayının beklentisi kendisi</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(E(X)=\frac\alpha4\):&nbsp;&nbsp; \(E\Big(\frac{X_n}{\alpha}\Big)=\frac{E(X_n)}{\alpha}=\frac{\alpha/4}{\alpha}=\frac14\)</div>
<span class="tr">"α/4 bölü α": α'lar sadeleşir, 1/4 kalır. Kesir içinde kesir görünce korkma: (α/4)/α = α/(4α) = 1/4.</span>
<div class="fe">⚠ Nur Konstanten (Zahlen, \(\alpha\), \(\theta\), \(n\)) darf man herausziehen – niemals ein \(X\)!</div>''',
 [(r'\(E(X)=\theta\). \(E(5X_2)=\)', r'\(5\theta\)', 's'),
  (r'\(E(X)=\frac\theta3\). \(E(6X_1)=\)', r'\(6\cdot\frac\theta3=2\theta\)', 's'),
  (r'\(E(X)=\frac\alpha2\). \(E\big(\frac{X_n}{\alpha}\big)=\)', r'\(\frac{\alpha/2}{\alpha}=\frac12\)', 's'),
  (r'\(E\big(\frac14\big)=\) und \(E(7)=\)', r'\(\frac14\) und \(7\)', 's')]))

S_units.append(('Regel 2: Summen auseinanderziehen', 10, r'''
<h4>Erwartungswert einer Summe = Summe der Erwartungswerte</h4>
\[E(X_1+X_2)=E(X_1)+E(X_2)\qquad E(aX_1+bX_2+c)=aE(X_1)+bE(X_2)+c\]
<span class="tr">Toplamın beklentisi = beklentilerin toplamı. Her terimi ayrı ayrı hesapla, sonra topla. Bu kural HER ZAMAN geçerli.</span>
<h4>Summenzeichen</h4>
\[E\Big(\sum_{i=1}^n X_i\Big)=\sum_{i=1}^n E(X_i)=n\cdot E(X)\]
<span class="tr">n tane aynı beklenti toplanıyor → n çarpı beklenti. Dikkat: toplam i=2'den başlıyorsa terim sayısı n−1'dir!</span>
<table><tr><th>Summe</th><th>Anzahl Terme</th><th>Erwartungswert (\(E(X)=\mu\))</th></tr>
<tr><td>\(\sum_{i=1}^n X_i\)</td><td>\(n\)</td><td>\(n\mu\)</td></tr>
<tr><td>\(\sum_{i=2}^n X_i\)</td><td>\(n-1\)</td><td>\((n-1)\mu\)</td></tr>
<tr><td>\(\sum_{i=2}^{n-1} X_i\)</td><td>\(n-2\)</td><td>\((n-2)\mu\)</td></tr></table>
<h4>Der Mittelwert</h4>
\[E(\bar X)=E\Big(\frac1n\sum X_i\Big)=\frac1n\cdot n\mu=\mu\]
<div class="vg"><b class="t">Vorgemacht</b>\(E(X)=\frac\theta2\), \(T=2\bar X\): \(E(T)=2E(\bar X)=2\cdot\frac\theta2=\theta\Rightarrow\) erwartungstreu für \(\theta\).</div>''',
 [(r'\(E(X)=\mu\). \(E(X_1+X_2+X_3)=\)', r'\(3\mu\)', 's'),
  (r'\(E(X)=\mu\). \(E(2X_1-X_2)=\)', r'\(2\mu-\mu=\mu\)', 's'),
  (r'\(E(X)=\theta\). \(E\big(\sum_{i=2}^n X_i\big)=\)', r'\((n-1)\theta\)', 's'),
  (r'\(E(X)=\frac\kappa2\). \(E\big(\frac{1}{2n}\sum_{i=1}^{n}X_i\big)=\)', r'\(\frac1{2n}\cdot n\cdot\frac\kappa2=\frac\kappa4\)', 's')]))

S_units.append(('Das Rezept: erwartungstreu prüfen', 10, r'''
<h4>4 Schritte – immer gleich</h4>
<table><tr><th>#</th><th>Was tun?</th><th>Was hinschreiben?</th></tr>
<tr><td>①</td><td>Erwartungswert über den <b>ganzen</b> Schätzer setzen</td><td>\(E(\hat\theta)=E(\dots)\)</td></tr>
<tr><td>②</td><td>Summen auseinanderziehen, Konstanten raus (Regel 1+2)</td><td>\(=aE(X_1)+bE(X_2)+\dots\)</td></tr>
<tr><td>③</td><td>\(E(X_i)\) aus der Aufgabe einsetzen, vereinfachen</td><td>\(=\dots=\) Ergebnis</td></tr>
<tr><td>④</td><td>Mit dem Parameter vergleichen + <b>Satz</b></td><td>„Da \(E(\hat\theta)=\theta\), ist \(\hat\theta\) erwartungstreu.“ / „Da \(E(\hat\theta)\neq\theta\), ist \(\hat\theta\) verzerrt; Bias \(=E(\hat\theta)-\theta\).“</td></tr></table>
<div class="vg"><b class="t">Vorgemacht</b>\(E(X)=\mu\), \(T=\frac14(X_1+2X_2+X_3)\):<br>
① \(E(T)=E\big(\frac14(X_1+2X_2+X_3)\big)\)<br>
② \(=\frac14\big(E(X_1)+2E(X_2)+E(X_3)\big)\)<br>
③ \(=\frac14(\mu+2\mu+\mu)=\frac{4\mu}{4}=\mu\)<br>
④ Da \(E(T)=\mu\), ist \(T\) ein erwartungstreuer Schätzer für \(\mu\).</div>
<span class="tr">Kısa yol (lineer tahmincilerde): katsayıları topla. 1/4 + 2/4 + 1/4 = 1 → yansız. Ama sınavda yine 4 adımı yaz, puan oradan geliyor.</span>
<h4>Bias und „asymptotisch erwartungstreu“</h4>
\(\text{Bias}=E(\hat\theta)-\theta\). Wenn der Bias von \(n\) abhängt und für \(n\to\infty\) gegen 0 geht → <b>asymptotisch erwartungstreu</b>.
<div class="fe">⚠ Immer den Satz am Ende schreiben – ohne Satz fehlt ein Punkt.</div>''',
 [(r'\(E(X)=\mu\), \(T=\frac13(X_1+X_2+X_3)\). Erwartungstreu?', r'\(E(T)=\frac13\cdot3\mu=\mu\) → ja', 's'),
  (r'\(E(X)=\mu\), \(T=X_1+X_2-X_3\). Erwartungstreu?', r'\(\mu+\mu-\mu=\mu\) → ja', 's'),
  (r'\(E(X)=\mu\), \(T=\frac12(X_1+X_2+X_3)\). Erwartungstreu? Bias?', r'\(E(T)=\frac32\mu\neq\mu\) → verzerrt, Bias \(=\frac12\mu\)', 'm'),
  (r'\(E(X)=\frac\theta2\), \(T=\bar X\). Ist \(T\) erwartungstreu für \(\theta\)?', r'\(E(\bar X)=\frac\theta2\neq\theta\) → verzerrt (Bias \(-\frac\theta2\)); \(2\bar X\) wäre erwartungstreu', 'm')]))

S_units.append(('Die Altklausur-Falle: Produkte und Brüche', 10, r'''
<h4>Schritt 0: erst kürzen!</h4>
In der Altklausur stand: \(\dfrac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}\). Schreib die Produkte aus:
\[\frac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}=\frac{X_2\cdot X_3\cdots X_{n-1}}{X_1\cdot X_2\cdot X_3\cdots X_{n-1}}=\frac{1}{X_1}\]
<span class="tr">Pay ve paydada aynı X'ler var → sadeleşir. Hangi X'in fazladan olduğuna bak: payda X₁'den başlıyor, pay X₂'den → paydada X₁ fazla → sonuç 1/X₁.</span>
<table><tr><th>Bruch</th><th>gekürzt</th><th>Warum</th></tr>
<tr><td>\(\frac{\prod_{i=1}^{n}X_i}{\prod_{i=1}^{n-1}X_i}\)</td><td>\(X_n\)</td><td>oben ein \(X_n\) mehr</td></tr>
<tr><td>\(\frac{\prod_{i=1}^{n}X_i}{\prod_{i=2}^{n}X_i}\)</td><td>\(X_1\)</td><td>oben ein \(X_1\) mehr</td></tr>
<tr><td>\(\frac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}\)</td><td>\(\frac1{X_1}\)</td><td>unten ein \(X_1\) mehr</td></tr></table>
<h4>Produkt unabhängiger ZV</h4>
\(E(X_1\cdot X_2)=E(X_1)\cdot E(X_2)\) (unabhängig). Für \(E\big(\frac1{X_1}\big)\) rechnet die offizielle Lösung \(\frac{1}{E(X_1)}\).
<div class="vg"><b class="t">Vorgemacht (Altklausur A7)</b>\(E(X)=\frac\alpha4\), \(\hat\alpha=\frac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}+\frac{X_n}{\alpha}-\frac14\)<br>
⓪ kürzen: \(\hat\alpha=\frac1{X_1}+\frac{X_n}\alpha-\frac14\)<br>
①② \(E(\hat\alpha)=E\big(\frac1{X_1}\big)+\frac{E(X_n)}{\alpha}-\frac14\)<br>
③ \(=\frac{4}{\alpha}+\frac{\alpha/4}{\alpha}-\frac14=\frac4\alpha+\frac14-\frac14=\frac4\alpha\)<br>
④ Da \(E(\hat\alpha)=\frac4\alpha\neq\alpha\), ist \(\hat\alpha\) verzerrt.</div>''',
 [(r'Kürzen: \(\frac{\prod_{i=1}^{n}X_i}{\prod_{i=1}^{n-1}X_i}=\)', r'\(X_n\)', 's'),
  (r'Kürzen: \(\frac{\prod_{i=1}^{n}X_i}{\prod_{i=2}^{n}X_i}=\)', r'\(X_1\)', 's'),
  (r'\(E(X)=\frac\theta3\), unabhängig. \(E(X_1X_2)=\)', r'\(\frac\theta3\cdot\frac\theta3=\frac{\theta^2}9\)', 's')]))

S_klaus = [
 ('Zwei lineare Schätzer vergleichen', 6,
  r'Sei \(X\) eine Zufallsvariable mit \(E(X)=\mu\) und \(Var(X)=\sigma^2\). Sie ziehen eine 3-fache, unabhängige Stichprobe und betrachten \[T_1=\frac{X_1+2X_2+X_3}{4}\qquad\text{und}\qquad T_2=X_1+X_2-X_3.\]',
  [(r'Zeigen Sie, dass beide Schätzer erwartungstreu für \(\mu\) sind.', 2, 'm', r'\(E(T_1)=\frac14(\mu+2\mu+\mu)=\mu\) [1]; \(E(T_2)=\mu+\mu-\mu=\mu\) [1]'),
   (r'Berechnen Sie \(Var(T_1)\) und \(Var(T_2)\). (Hinweis: \(Var(aX_1+bX_2)=a^2\sigma^2+b^2\sigma^2\) bei Unabhängigkeit)', 2, 'm', r'\(Var(T_1)=\frac{1+4+1}{16}\sigma^2=0.375\sigma^2\) [1]; \(Var(T_2)=(1+1+1)\sigma^2=3\sigma^2\) [1]'),
   (r'Welcher Schätzer ist vorzuziehen? Ist \(\bar X\) noch besser? Begründen Sie.', 2, 'm', r'Beide e.t., \(0.375\sigma^2<3\sigma^2\) → \(T_1\) [1]; \(Var(\bar X)=\frac{\sigma^2}{3}=0.333\sigma^2<0.375\sigma^2\) → \(\bar X\) noch besser [1]')]),
 ('Produkte kürzen (Altklausur-Typ)', 5,
  r'Sei \(X\) eine Zufallsvariable mit \(E(X)=\frac{\theta}{2}\) mit \(\theta\in\mathbb R\). Sie ziehen eine \(n\)-fache, unabhängige Zufallsstichprobe \(\{X_1,\dots,X_n\}\). Testen Sie, ob der Schätzer \[\hat\theta=\frac{\prod_{i=1}^{n}X_i}{\prod_{i=1}^{n-1}X_i}+\frac1n\sum_{i=1}^nX_i\] ein unverzerrter Schätzer für \(\theta\) ist.',
  [(r'Vereinfachen Sie den Schätzer so weit wie möglich.', 1, 's', r'\(\hat\theta=X_n+\bar X\) [1]'),
   (r'Berechnen Sie \(E(\hat\theta)\) und entscheiden Sie (mit Satz).', 4, 'l', r'\(E(\hat\theta)=E(X_n)+E(\bar X)\) [1] \(=\frac\theta2+\frac\theta2\) [1] \(=\theta\) [1]; Da \(E(\hat\theta)=\theta\), ist \(\hat\theta\) unverzerrt [1]')]),
 ('Bias, der von n abhängt (Testat-Typ)', 5,
  r'Betrachten Sie eine Zufallsvariable \(X\) mit \(E(X)=\frac{\kappa}{2}\). Ein Schätzer für \(\kappa\) sei \[\tilde\kappa=X_1+\frac{1}{2n}\sum_{i=2}^{n}X_i.\]',
  [(r'Berechnen Sie \(E(\tilde\kappa)\). Achten Sie auf die Anzahl der Summanden!', 2, 'm', r'\(E(\tilde\kappa)=\frac\kappa2+\frac1{2n}(n-1)\frac\kappa2=\frac\kappa2+\frac{(n-1)\kappa}{4n}\) [2]'),
   (r'Berechnen Sie den Bias. Ist \(\tilde\kappa\) erwartungstreu?', 2, 'm', r'Bias \(=\frac\kappa2+\frac{(n-1)\kappa}{4n}-\kappa=\frac{(n-1)\kappa-2n\kappa}{4n}=-\frac{(n+1)\kappa}{4n}\neq0\) → verzerrt [2]'),
   (r'Hängt der Bias von \(n\) ab?', 1, 's', r'Ja, Bias \(=-\frac{(n+1)\kappa}{4n}\) hängt von \(n\) ab (geht gegen \(-\frac\kappa4\), nicht gegen 0) [1]')]),
 ('Die Konstante kürzt sich weg', 5,
  r'Sei \(X\) eine Zufallsvariable mit \(E(X)=\frac{\alpha}{4}\). Sie ziehen eine \(n\)-fache, unabhängige Zufallsstichprobe. Testen Sie, ob \[\hat\alpha=4\bar X+\frac{X_1}{\alpha}-\frac14\] ein unverzerrter Schätzer für \(\alpha\) ist.',
  [(r'Berechnen Sie \(E(\hat\alpha)\) Schritt für Schritt.', 4, 'l', r'\(E(\hat\alpha)=4E(\bar X)+\frac{E(X_1)}{\alpha}-\frac14\) [1] \(=4\cdot\frac\alpha4+\frac{\alpha/4}{\alpha}-\frac14\) [1] \(=\alpha+\frac14-\frac14=\alpha\) [2]'),
   (r'Entscheiden Sie mit einem Satz.', 1, 's', r'Da \(E(\hat\alpha)=\alpha\), ist \(\hat\alpha\) unverzerrt [1]')]),
]

# =====================================================================================
# HEFT 2: BAYES & TOTALE WAHRSCHEINLICHKEIT
# =====================================================================================
C2 = '#2e7d32'
TREE = r'''<svg class="tree" width="520" height="190" viewBox="0 0 520 190" font-family="Inter,Arial" font-size="13">
<circle cx="30" cy="95" r="5" fill="#2e7d32"/>
<line x1="30" y1="95" x2="190" y2="45" stroke="#2e7d32" stroke-width="2"/><line x1="30" y1="95" x2="190" y2="145" stroke="#2e7d32" stroke-width="2"/>
<text x="85" y="55" fill="#2e7d32">P(B) = 0.7</text><text x="85" y="150" fill="#c62828">P(B̄) = 0.3</text>
<text x="195" y="50" font-weight="700">B (besteht)</text><text x="195" y="150" font-weight="700">B̄ (nicht)</text>
<line x1="280" y1="45" x2="400" y2="15" stroke="#555"/><line x1="280" y1="45" x2="400" y2="45" stroke="#555"/><line x1="280" y1="45" x2="400" y2="75" stroke="#555"/>
<line x1="280" y1="145" x2="400" y2="115" stroke="#555"/><line x1="280" y1="145" x2="400" y2="145" stroke="#555"/><line x1="280" y1="145" x2="400" y2="175" stroke="#555"/>
<text x="300" y="22">0.8</text><text x="320" y="42">0.15</text><text x="300" y="72">0.05</text>
<text x="300" y="122">0.1</text><text x="320" y="142">0.2</text><text x="300" y="172">0.7</text>
<text x="405" y="19">S₁ → 0.7·0.8</text><text x="405" y="49">S₂ → 0.7·0.15</text><text x="405" y="79">S₃ → 0.7·0.05</text>
<text x="405" y="119">S₁ → 0.3·0.1</text><text x="405" y="149">S₂ → 0.3·0.2</text><text x="405" y="179">S₃ → 0.3·0.7</text></svg>'''

B_units = []
B_units.append(('Sätze in Wahrscheinlichkeiten übersetzen', 10, r'''
<h4>Das Wichtigste zuerst: „von wem“ ist die Rede?</h4>
Jede Prozentangabe in diesen Aufgaben bezieht sich auf eine <b>Gruppe</b>. Diese Gruppe steht <b>rechts</b> vom Strich \(\mid\).
<table><tr><th>Satz in der Aufgabe</th><th>Notation</th><th>Türkçe</th></tr>
<tr><td>„70 % bestehen die Klausur.“</td><td>\(P(B)=0.7\)</td><td>herkes içinde → koşulsuz</td></tr>
<tr><td>„Mit 80 % gehört ein <u>Besteher</u> zu Strategie 1.“</td><td>\(P(S_1\mid B)=0.8\)</td><td>bilinen grup (Besteher) sağa</td></tr>
<tr><td>„Unter den <u>Nicht-Bestehern</u> lernen 10 % regelmäßig.“</td><td>\(P(S_1\mid\bar B)=0.1\)</td><td>„unter den …“ → sağa</td></tr>
<tr><td>„Der Test erkennt 95 % der <u>Kranken</u>.“</td><td>\(P(+\mid K)=0.95\)</td><td>hastalar arasında → K sağda</td></tr>
<tr><td>„Eine Person ist positiv. Wie wahrscheinlich ist sie krank?“</td><td>\(P(K\mid +)\) = <b>gesucht</b></td><td>bildiğimiz şey (+) sağda</td></tr></table>
<span class="tr">Kural: "… arasında / … olan biri / bilindiğine göre" denen grup HER ZAMAN çizginin SAĞINA yazılır. Soruyu okurken önce o grubun altını çiz.</span>
<div class="fe">⚠ \(P(A\mid B)\) und \(P(B\mid A)\) sind verschiedene Dinge! „Kranke, die positiv sind“ ≠ „Positive, die krank sind“.</div>''',
 [(r'„40 % aller Nutzer haben ein Premium-Abo (\(P\)).“', r'\(P(P)=0.4\)', 's'),
  (r'„Unter den Premium-Nutzern schauen 50 % hauptsächlich Serien (\(S\)).“', r'\(P(S\mid P)=0.5\)', 's'),
  (r'„Von den Nicht-Premium-Nutzern schauen 25 % Serien.“', r'\(P(S\mid\bar P)=0.25\)', 's'),
  (r'„Jemand schaut Serien. Wie wahrscheinlich hat er Premium?“ (gesucht)', r'\(P(P\mid S)\)', 's')]))

B_units.append(('Den Baum zeichnen und vervollständigen', 10, r'''
<h4>Regel: Die Gruppe hinter „unter den …“ kommt in die ERSTE Stufe</h4>
In der Altklausur A3: „Mit 80 % gehört ein <u>Besteher</u> zu Kategorie 1“ → erste Stufe = Bestehen / Nicht-Bestehen, zweite Stufe = Strategie.
''' + TREE + r'''
<h4>Fehlende Äste ergänzen: jede Gabel ergibt zusammen 1</h4>
\(P(\bar B)=1-0.7=0.3\) · \(P(S_3\mid B)=1-0.8-0.15=0.05\) · \(P(S_3\mid\bar B)=1-0.1-0.2=0.7\)
<span class="tr">Her çatalda dallar toplamı 1. Eksik dalı "1 eksi diğerleri" ile bul. İlk iş olarak ağacı çiz ve tüm sayıları yerleştir – puanların yarısı zaten bu kutularda.</span>
<div class="fe">⚠ Unten am Baum stehen die Wahrscheinlichkeiten <b>bedingt</b>: Die 0.1 gilt nur <b>innerhalb</b> von \(\bar B\).</div>''',
 [(r'\(P(K)=0.02\). \(P(\bar K)=\)', r'\(0.98\)', 's'),
  (r'\(P(+\mid K)=0.95\). \(P(-\mid K)=\)', r'\(0.05\)', 's'),
  (r'Drei Gruppen: \(P(S_1\mid A)=0.5\), \(P(S_2\mid A)=0.3\). \(P(S_3\mid A)=\)', r'\(1-0.5-0.3=0.2\)', 's')]))

B_units.append(('Pfadregel: entlang des Pfades multiplizieren', 6, r'''
<h4>„A und B“ = Pfad entlang gehen = multiplizieren</h4>
\[P(B\cap S_2)=P(B)\cdot P(S_2\mid B)=0.7\cdot0.15=0.105\]
<span class="tr">"Hem geçti hem S₂" = ağaçta B dalından S₂'ye giden YOL. Yol boyunca sayıları çarp.</span>
<div class="vg"><b class="t">Vorgemacht</b>\(P(\bar B\cap S_3)=P(\bar B)\cdot P(S_3\mid\bar B)=0.3\cdot0.7=0.21\)</div>
<div class="fe">⚠ Auf dem \(\bar B\)-Ast mit \(0.3\) multiplizieren, nicht mit \(0.7\)! (Genau das war dein Fehler in der Altklausur.)</div>''',
 [(r'\(P(B)=0.7\), \(P(S_1\mid B)=0.8\). \(P(B\cap S_1)=\)', r'\(0.56\)', 's'),
  (r'\(P(\bar B)=0.3\), \(P(S_2\mid\bar B)=0.2\). \(P(\bar B\cap S_2)=\)', r'\(0.06\)', 's'),
  (r'\(P(K)=0.02\), \(P(+\mid K)=0.95\). \(P(K\cap +)=\)', r'\(0.019\)', 's')]))

B_units.append(('Totale Wahrscheinlichkeit: alle Pfade zum Ergebnis addieren', 8, r'''
<h4>„Wie wahrscheinlich ist \(S_3\) insgesamt?“</h4>
Zu \(S_3\) führen <b>zwei</b> Pfade: über \(B\) und über \(\bar B\). Beide multiplizieren, dann addieren:
\[P(S_3)=P(B)\,P(S_3\mid B)+P(\bar B)\,P(S_3\mid\bar B)=0.7\cdot0.05+0.3\cdot0.7=0.035+0.21=0.245\]
<span class="tr">"Toplam olasılık" = o sonuca giden BÜTÜN yolları bul, her yolu çarp, sonra yolları TOPLA. Her yolda o yolun kendi ilk sayısını kullan (0.7 ve 0.3).</span>
<div class="vg"><b class="t">Muster zum Abschreiben</b>\(P(\text{Ergebnis})=P(A)\cdot P(\text{Erg.}\mid A)+P(\bar A)\cdot P(\text{Erg.}\mid\bar A)\)</div>''',
 [(r'\(P(B)=0.7\), \(P(S_2\mid B)=0.15\), \(P(S_2\mid\bar B)=0.2\). \(P(S_2)=\)', r'\(0.105+0.06=0.165\)', 's'),
  (r'\(P(K)=0.02\), \(P(+\mid K)=0.95\), \(P(+\mid\bar K)=0.1\). \(P(+)=\)', r'\(0.019+0.098=0.117\)', 's'),
  (r'\(P(P)=0.4\), \(P(F\mid P)=0.3\), \(P(F\mid\bar P)=0.6\). \(P(F)=\)', r'\(0.12+0.36=0.48\)', 's')]))

B_units.append(('Bayes: rückwärts fragen', 10, r'''
<h4>„Jemand ist in \(S_2\). Wie wahrscheinlich hat er bestanden?“ → \(P(B\mid S_2)\)</h4>
\[P(B\mid S_2)=\frac{\text{der eine Pfad über }B}{\text{alle Pfade zu }S_2}=\frac{P(B)\,P(S_2\mid B)}{P(S_2)}=\frac{0.105}{0.165}=0.636\]
<span class="tr">Bayes = İSTENEN YOL / TOPLAM. Pay: sadece istenen yol (B → S₂). Payda: S₂'ye giden bütün yollar (Lerneinheit 4'teki toplam). Paydayı yazmazsan cevap yanlış olur (Altklausur'da 0.105 yazmıştın – o sadece paydı).</span>
<div class="vg"><b class="t">Rezept</b>① Was ist bekannt? (rechts vom Strich) → das ist das Ergebnis am Ende des Baums<br>
② Nenner: totale Wahrscheinlichkeit dieses Ergebnisses<br>③ Zähler: der eine Pfad, nach dem gefragt ist<br>④ teilen</div>
<div class="fe">⚠ Kontrolle: Das Ergebnis muss zwischen 0 und 1 liegen und der Zähler muss kleiner als der Nenner sein.</div>''',
 [(r'\(P(K\cap +)=0.019\), \(P(+)=0.117\). \(P(K\mid +)=\)', r'\(\frac{0.019}{0.117}=0.162\)', 's'),
  (r'\(P(P\cap F)=0.12\), \(P(F)=0.48\). \(P(P\mid F)=\)', r'\(0.25\)', 's'),
  (r'\(P(B)=0.7\), \(P(S_1\mid B)=0.8\), \(P(S_1\mid\bar B)=0.1\). \(P(B\mid S_1)=\)', r'\(\frac{0.56}{0.56+0.03}=\frac{0.56}{0.59}=0.949\)', 'm')]))

B_units.append(('Trick: mit 1000 Personen rechnen', 8, r'''
<h4>Wenn der Baum verwirrt: stell dir 1000 Personen vor</h4>
Medizinischer Test: \(P(K)=0.02\), \(P(+\mid K)=0.95\), \(P(+\mid\bar K)=0.1\).
<table><tr><th></th><th>positiv</th><th>negativ</th><th>Σ</th></tr>
<tr><td>krank</td><td>\(20\cdot0.95=19\)</td><td>1</td><td>\(1000\cdot0.02=20\)</td></tr>
<tr><td>gesund</td><td>\(980\cdot0.1=98\)</td><td>882</td><td>980</td></tr>
<tr><td>Σ</td><td><b>117</b></td><td>883</td><td>1000</td></tr></table>
\(P(+)=\frac{117}{1000}=0.117\) · \(P(K\mid +)=\frac{19}{117}=0.162\) · \(P(\bar K\mid -)=\frac{882}{883}=0.999\)
<span class="tr">1000 kişi düşün, sayıları tabloya yaz. "Pozitiflerin içinde kaç hasta var?" → 19/117. Bu yöntem Bayes formülüyle AYNI sonucu verir ama kafada daha kolay. Sınavda formülü de yaz.</span>''',
 [(r'1000 Studierende, \(P(M)=0.6\), \(P(V\mid M)=0.5\), \(P(V\mid\bar M)=0.2\). Wie viele sind vegetarisch (\(V\))?', r'\(600\cdot0.5+400\cdot0.2=300+80=380\)', 's'),
  (r'… und wie viele davon gehen in die Mensa? \(P(M\mid V)=\)', r'\(\frac{300}{380}=0.789\)', 's')]))

B_units.append(('„Mindestens einer“ bei unabhängigen Wiederholungen', 6, r'''
<h4>Immer über das Gegenereignis</h4>
\[P(\text{mindestens einer})=1-P(\text{keiner})=1-(1-p)^n\]
<span class="tr">"En az bir" = 1 − "hiç yok". "Hiç yok" = her seferinde olmaması → (1−p) üssü n.</span>
<div class="vg"><b class="t">Vorgemacht (Altklausur A3c)</b>Bestehensquote 0.7, 10 Personen, mindestens ein Nicht-Besteher:<br>\(p=P(\bar B)=0.3\) → \(1-(1-0.3)^{10}=1-0.7^{10}=1-0.0282=0.972\)</div>
<div class="fe">⚠ \(0.3^{10}\) wäre „<b>alle</b> zehn bestehen nicht“ – das ist eine andere Frage!</div>''',
 [(r'\(P(\text{Premium})=0.4\), 8 Personen: mindestens eine mit Premium?', r'\(1-0.6^8=0.983\)', 's'),
  (r'Fehlerquote 5 %, 20 Teile: mindestens ein fehlerhaftes?', r'\(1-0.95^{20}=0.642\)', 's'),
  (r'Fehlerquote 5 %, 20 Teile: kein fehlerhaftes?', r'\(0.95^{20}=0.358\)', 's')]))

B_klaus = [
 ('Medizinischer Test', 9,
  r'Eine Krankheit tritt bei 2 % der Bevölkerung auf. Ein Schnelltest erkennt 95 % der Kranken (positives Ergebnis). Bei Gesunden zeigt der Test in 10 % der Fälle fälschlicherweise ein positives Ergebnis.',
  [(r'Berechnen Sie die Wahrscheinlichkeit, dass eine zufällig getestete Person positiv getestet wird.', 2, 'm', r'\(P(+)=0.95\cdot0.02+0.1\cdot0.98=0.019+0.098=0.117\) [2]'),
   (r'Eine Person wurde positiv getestet. Mit welcher Wahrscheinlichkeit ist sie tatsächlich krank? Geben Sie Ihren Lösungsweg an.', 3, 'm', r'\(P(K\mid +)=\frac{0.019}{0.117}=0.162\) [Zähler 1, Nenner 1, Ergebnis 1]'),
   (r'Eine Person wurde negativ getestet. Mit welcher Wahrscheinlichkeit ist sie gesund?', 2, 'm', r'\(P(\bar K\mid -)=\frac{0.9\cdot0.98}{1-0.117}=\frac{0.882}{0.883}=0.999\) [2]'),
   (r'Es werden 5 Personen unabhängig getestet. Mit welcher Wahrscheinlichkeit ist mindestens ein Test positiv?', 2, 's', r'\(1-(1-0.117)^5=1-0.883^5=0.463\) [2]')]),
 ('Drei Maschinen', 7,
  r'Ein Betrieb fertigt Schrauben auf drei Maschinen: A stellt 50 %, B 30 % und C 20 % der Produktion her. Die Ausschussquoten betragen bei A 2 %, bei B 3 % und bei C 5 %.',
  [(r'Wie groß ist die Wahrscheinlichkeit, dass eine zufällig gewählte Schraube Ausschuss ist?', 3, 'm', r'\(P(D)=0.5\cdot0.02+0.3\cdot0.03+0.2\cdot0.05=0.01+0.009+0.01=0.029\) [3]'),
   (r'Eine Schraube ist Ausschuss. Mit welcher Wahrscheinlichkeit stammt sie von Maschine C?', 2, 'm', r'\(P(C\mid D)=\frac{0.01}{0.029}=0.345\) [2]'),
   (r'Eine Schraube ist <b>kein</b> Ausschuss. Mit welcher Wahrscheinlichkeit stammt sie von Maschine A?', 2, 'm', r'\(P(A\mid\bar D)=\frac{0.5\cdot0.98}{1-0.029}=\frac{0.49}{0.971}=0.505\) [2]')]),
 ('Altklausur-Typ: Mensa', 11,
  r'60 % der Studierenden essen regelmäßig in der Mensa (\(M\)). Unter den Mensa-Gästen essen 50 % vegetarisch, 30 % Fleisch und der Rest Fisch. Unter den Studierenden, die nicht in der Mensa essen, ernähren sich 20 % vegetarisch und 70 % essen Fleisch; der Rest isst Fisch.',
  [(r'Berechnen Sie \(P(\bar M)\), \(P(\text{Fisch}\mid M)\) und \(P(\text{Fisch}\mid\bar M)\).', 3, 'm', r'\(0.4\) [1]; \(1-0.5-0.3=0.2\) [1]; \(1-0.2-0.7=0.1\) [1]'),
   (r'Berechnen Sie die Wahrscheinlichkeit, dass eine zufällig ausgewählte Person Fisch isst.', 3, 'm', r'\(P(\text{Fisch})=0.2\cdot0.6+0.1\cdot0.4=0.12+0.04=0.16\) [3]'),
   (r'Eine Person isst vegetarisch. Wie wahrscheinlich isst sie in der Mensa? Lösungsweg!', 3, 'm', r'\(P(V)=0.5\cdot0.6+0.2\cdot0.4=0.38\); \(P(M\mid V)=\frac{0.3}{0.38}=0.789\) [3]'),
   (r'Sie befragen 6 Personen unabhängig. Wie groß ist die Wahrscheinlichkeit, dass mindestens eine nicht in der Mensa isst? Vereinfachen Sie so weit wie möglich.', 2, 's', r'\(1-0.6^6=0.953\) [2]')]),
]

# =====================================================================================
# HEFT 3: HYPOTHESENTESTS
# =====================================================================================
C3 = '#b42318'
T_units = []
T_units.append(('Die Idee: wie ein Gerichtsverfahren', 6, r'''
<h4>Unschuldsvermutung</h4>
\(H_0\) = der „Normalzustand“ / die Behauptung, die wir angreifen. \(H_1\) = das, was wir <b>beweisen</b> wollen.<br>
Wir lehnen \(H_0\) nur ab, wenn die Daten <b>sehr</b> unwahrscheinlich wären, falls \(H_0\) stimmt (Wahrscheinlichkeit \(\le\alpha\)).
<span class="tr">Mahkeme gibi: sanık suçsuz kabul edilir (H₀). Ancak güçlü kanıt varsa "suçlu" denir (H₀ reddedilir). Kanıt yetersizse "suçsuz" denmez, sadece "suçluluğu kanıtlanamadı" denir → "H₀ kann nicht abgelehnt werden", ASLA "H₀ angenommen".</span>
<h4>Der Ablauf – immer gleich (8 Punkte)</h4>
<table><tr><th>Teil</th><th>Was</th><th>Punkte typisch</th></tr>
<tr><td>(a)</td><td>Hypothesenpaar</td><td>2</td></tr><tr><td>(b)</td><td>Prüfgröße berechnen + <b>Verteilung unter \(H_0\)</b></td><td>2–3</td></tr>
<tr><td>(c)</td><td>Ablehnungsbereich / kritischer Wert oder R-Code</td><td>1–2</td></tr><tr><td>(d)</td><td>Entscheidung + Satz im Sachzusammenhang</td><td>2</td></tr></table>''',
 [(r'Was bedeutet „\(H_0\) wird abgelehnt“ in einem Satz?', r'Die Daten sprechen so stark gegen \(H_0\), dass wir \(H_1\) als statistisch nachgewiesen ansehen.', 's'),
  (r'Darf man schreiben „\(H_0\) wird angenommen“?', r'Nein → „\(H_0\) kann nicht abgelehnt werden“', 's')]))

T_units.append(('Hypothesen aus dem Text', 12, r'''
<h4>Drei Fragen</h4>
<b>1. Welcher Parameter?</b> Mittelwert → \(\mu\) · Anteil/Prozent → \(\pi\) · Varianz → \(\sigma^2\)<br>
<b>2. Was soll nachgewiesen / abgesichert werden?</b> → das ist \(H_1\)<br>
<b>3. Welche Richtung?</b>
<table><tr><th>Wort im Text</th><th>\(H_1\)</th></tr>
<tr><td>mehr als, größer, übersteigt, länger, besser, erhöht</td><td>\(\mu>\mu_0\)</td></tr>
<tr><td>weniger als, kleiner, unterschreitet, kürzer, <b>nicht weiter als</b>, zu wenig</td><td>\(\mu<\mu_0\)</td></tr>
<tr><td>weicht ab, ungleich, <b>genau</b> … bezweifelt, verändert, in beide Richtungen</td><td>\(\mu\neq\mu_0\)</td></tr></table>
\(H_0\) ist das Gegenteil und enthält immer das Gleichheitszeichen (\(=,\le,\ge\)).
<div class="vg"><b class="t">Vorgemacht</b>„Hersteller: Brötchen wiegen <i>mindestens</i> 60 g. Verbraucherschutz vermutet <i>weniger</i>.“ → nachweisen will man „weniger“: \(H_0:\mu\ge60\) vs. \(H_1:\mu<60\)</div>
<div class="fe">⚠ Immer den Parameter schreiben: „\(H_0:\ \mu\ge133.5\)“ – nicht nur „\(H_0\ge133.5\)“.</div>''',
 [(r'„Eine Firma will absichern, dass ihre Akkus <i>länger</i> als 10 h halten.“', r'\(H_0:\mu\le10\) vs. \(H_1:\mu>10\)', 's'),
  (r'„Ein Magazin bezweifelt die Angabe <i>genau</i> 500 ml – in beide Richtungen.“', r'\(H_0:\mu=500\) vs. \(H_1:\mu\neq500\)', 's'),
  (r'„Absichern, dass ein Springer <i>nicht weiter als</i> 133.5 m springt.“', r'\(H_0:\mu\ge133.5\) vs. \(H_1:\mu<133.5\)', 's'),
  (r'„Eine Partei will zeigen, dass <i>mehr als 40 %</i> sie unterstützen.“', r'\(H_0:\pi\le0.4\) vs. \(H_1:\pi>0.4\)', 's')]))

T_units.append(('Welcher Test? Prüfgröße und Verteilung', 12, r'''
<table><tr><th>Situation</th><th>Prüfgröße</th><th>Verteilung unter \(H_0\)</th></tr>
<tr><td>Mittelwert, <b>σ bekannt</b> (σ oder σ² steht in der Aufgabe als „bekannt“)</td><td>\(Z=\dfrac{\bar x-\mu_0}{\sigma/\sqrt n}\)</td><td>\(N(0,1)\)</td></tr>
<tr><td>Mittelwert, <b>σ unbekannt</b> (nur \(s_*\) aus den Daten)</td><td>\(T=\dfrac{\bar x-\mu_0}{s_*/\sqrt n}\)</td><td>\(t_{n-1}\)</td></tr>
<tr><td>Anteil \(\pi\) (n groß)</td><td>\(Z=\dfrac{\hat\pi-\pi_0}{\sqrt{\pi_0(1-\pi_0)/n}}\)</td><td>\(\approx N(0,1)\)</td></tr></table>
<span class="tr">Hep aynı mantık: (gözlenen − hipotezdeki) / standart hata. Sonra MUTLAKA dağılımı yaz: "Unter H₀ gilt Z ~ N(0,1)" – bu tek başına 1 puan.</span>
<div class="vg"><b class="t">Vorgemacht</b>\(\bar x=48.2\), \(\mu_0=50\), \(\sigma^2=9\), \(n=25\): erst \(\sigma=\sqrt9=3\)!<br>\(Z=\frac{48.2-50}{3/\sqrt{25}}=\frac{-1.8}{0.6}=-3\); unter \(H_0\): \(Z\sim N(0,1)\).</div>
<div class="fe">⚠ σ² gegeben → Wurzel ziehen! Nenner ist \(\sigma/\sqrt n\), nicht \(\sigma/n\).</div>''',
 [(r'\(\bar x=103\), \(\mu_0=100\), \(\sigma=9\), \(n=36\). \(Z=\)? Verteilung?', r'\(\frac{3}{1.5}=2\), \(N(0,1)\)', 's'),
  (r'\(\bar x=12.6\), \(\mu_0=12\), \(s_*=1.2\), \(n=16\), σ unbekannt. \(T=\)? Verteilung?', r'\(\frac{0.6}{0.3}=2\), \(t_{15}\)', 's'),
  (r'230 von 400 stimmen zu, \(\pi_0=0.5\). \(Z=\)?', r'\(\hat\pi=0.575\), \(\sqrt{0.25/400}=0.025\), \(Z=3\)', 's'),
  (r'\(\bar x=131.5\), \(\mu_0=133.5\), \(\sigma^2=16\), \(n=4\). \(Z=\)?', r'\(\frac{-2}{4/2}=-1\)', 's')]))

T_units.append(('Ablehnungsbereich und kritischer Wert', 10, r'''
<table><tr><th>\(H_1\)</th><th>ablehnen, wenn</th><th>α = 10 %</th><th>α = 5 %</th><th>α = 1 %</th></tr>
<tr><td>\(\neq\) (zweiseitig)</td><td>\(|z|>z_{1-\alpha/2}\)</td><td>1.645</td><td>1.960</td><td>2.576</td></tr>
<tr><td>\(>\) (rechts)</td><td>\(z>z_{1-\alpha}\)</td><td>1.282</td><td>1.645</td><td>2.326</td></tr>
<tr><td>\(<\) (links)</td><td>\(z<-z_{1-\alpha}\)</td><td>−1.282</td><td>−1.645</td><td>−2.326</td></tr></table>
Beim t-Test genauso, nur mit \(t_{n-1;1-\alpha}\) bzw. \(t_{n-1;1-\alpha/2}\) (steht in der Aufgabe).
<span class="tr">Ret bölgesi H₁'in gösterdiği taraftadır: H₁ "<" ise sol kuyruk (negatif sayılar), ">" ise sağ kuyruk, "≠" ise iki taraf.</span>
<div class="vg"><b class="t">Ablehnungsbereich hinschreiben</b>links, α = 5 %: \(A=(-\infty;\ -1.645]\) · rechts, t-Test \(df=7\): \(A=[1.895;\ \infty)\) · zweiseitig: \(A=(-\infty;-1.96]\cup[1.96;\infty)\)</div>''',
 [(r'Gauß-Test, \(H_1:\mu\neq\mu_0\), α = 5 %. Ablehnen, wenn …', r'\(|z|>1.96\)', 's'),
  (r'Gauß-Test, \(H_1:\mu>\mu_0\), α = 1 %. Ablehnen, wenn …', r'\(z>2.326\)', 's'),
  (r'Gauß-Test, \(H_1:\mu<\mu_0\), α = 10 %. \(A=\)', r'\((-\infty;-1.282]\)', 's'),
  (r't-Test, \(H_1:\mu>\mu_0\), \(n=16\), α = 5 % (\(t_{15;0.95}=1.753\)). \(A=\)', r'\([1.753;\infty)\)', 's')]))

T_units.append(('Entscheidung und Antwortsatz', 8, r'''
<h4>Prüfgröße im Ablehnungsbereich? → \(H_0\) ablehnen</h4>
<div class="vg"><b class="t">Satz-Bausteine (abschreiben!)</b>
<b>abgelehnt:</b> „Da \(z=\dots\in A\), wird \(H_0\) zum Niveau \(\alpha=\dots\) abgelehnt. Es ist statistisch abgesichert, dass [Kontext + Richtung aus \(H_1\)].“<br>
<b>nicht abgelehnt:</b> „Da \(z=\dots\notin A\), kann \(H_0\) zum Niveau \(\alpha=\dots\) nicht abgelehnt werden. Es kann nicht nachgewiesen werden, dass [Kontext].“</div>
<span class="tr">Cümlede bağlamı yaz (Brötchen, Akku, Springer…) ve H₁'in yönünü tekrar et. "H₀ reddedildi" tek başına yarım puan.</span>''',
 [(r'\(H_1:\mu<60\) (Brötchen in g), \(z=-1.5\), α = 5 %. Entscheidung + Satz.', r'\(-1.5>-1.645\) → nicht ablehnen; es kann nicht nachgewiesen werden, dass die Brötchen im Mittel weniger als 60 g wiegen.', 'm'),
  (r'\(H_1:\mu>10\) (Akku in h), \(z=2.4\), α = 5 %. Entscheidung + Satz.', r'\(2.4>1.645\) → ablehnen; abgesichert, dass die Akkus im Mittel länger als 10 h halten.', 'm')]))

T_units.append(('p-Wert', 8, r'''
<table><tr><th>\(H_1\)</th><th>p-Wert</th><th>Beispiel</th></tr>
<tr><td>\(\neq\)</td><td>\(2\,(1-\Phi(|z|))\)</td><td>\(z=2\): \(2(1-0.9772)=0.0456\)</td></tr>
<tr><td>\(>\)</td><td>\(1-\Phi(z)\)</td><td>\(z=2.5\): \(1-0.9938=0.0062\)</td></tr>
<tr><td>\(<\)</td><td>\(\Phi(z)\)</td><td>\(z=-1.5\): \(\Phi(-1.5)=1-0.9332=0.0668\)</td></tr></table>
<div class="vg"><b class="t">Die eine Regel</b>\(p\le\alpha\Rightarrow H_0\) ablehnen · \(p>\alpha\Rightarrow\) nicht ablehnen</div>
<span class="tr">p-değeri küçükse H₀ reddedilir. "Birden fazla α için karar ver" sorusunda: p'den büyük veya eşit bütün α'lar için ret.</span>''',
 [(r'\(p=0.0456\). Entscheidung für α = 1 %, 5 %, 10 %?', r'nicht ablehnen / ablehnen / ablehnen', 's'),
  (r'\(p=0.0668\). Entscheidung für α = 5 % und 10 %?', r'nicht ablehnen / ablehnen', 's'),
  (r'\(H_1:\mu<\mu_0\), \(z=-2\), \(\Phi(2)=0.9772\). \(p=\)', r'\(\Phi(-2)=0.0228\)', 's')]))

T_units.append(('R-Output: welcher Code? welche Entscheidung?', 10, r'''
<h4>Drei Kontrollen in dieser Reihenfolge</h4>
<table><tr><th>#</th><th>prüfen</th><th>Beispiel Altklausur A8</th></tr>
<tr><td>1</td><td><b>Richtige Daten?</b> Über wen/was ist der Test?</td><td>Test über Stahlbichler → seine Weiten <code>c(130, 134, 129.5, 132.5)</code> → Code (1) fällt weg</td></tr>
<tr><td>2</td><td><code>mu=</code> = \(\mu_0\) aus \(H_0\)?</td><td><code>mu=133.5</code> ✓</td></tr>
<tr><td>3</td><td><code>alternative</code> passt zu \(H_1\)? <code>"l"</code>=less=\(<\) · <code>"g"</code>=greater=\(>\) · nichts/"two.sided"=\(\neq\)</td><td>\(H_1:\mu<133.5\) → <code>"l"</code> → <b>Code (2)</b></td></tr></table>
Dann nur noch: <b>p-value mit α vergleichen</b>. Den Wert <code>t = ?</code> brauchst du nicht.
<span class="tr">Kendini kandırma: üç kodun da sayıları birbirine benzer. Önce verinin KİME ait olduğuna bak – Altklausur'da Fiedler'in verisini seçmiştin.</span>
<div class="fe">⚠ <code>conf.level=0.9</code> bedeutet α = 0.1.</div>''',
 [(r'\(H_1:\mu>5\). Code A: <code>t.test(x, mu=5, alternative="l")</code>, Code B: <code>t.test(x, mu=5, alternative="g")</code>. Welcher?', r'B', 's'),
  (r'Gewählter Code liefert <code>p-value = 0.0023</code>, α = 5 %. Entscheidung?', r'\(0.0023<0.05\) → \(H_0\) ablehnen', 's')]))

T_units.append(('Fehler 1. und 2. Art im Sachzusammenhang', 6, r'''
<table><tr><th></th><th>\(H_0\) ist wahr</th><th>\(H_1\) ist wahr</th></tr>
<tr><td>\(H_0\) abgelehnt</td><td><b>Fehler 1. Art</b> (W'keit α)</td><td>richtig</td></tr>
<tr><td>\(H_0\) nicht abgelehnt</td><td>richtig</td><td><b>Fehler 2. Art</b> (β)</td></tr></table>
<div class="vg"><b class="t">Satzmuster</b>„Ein Fehler 1. Art liegt vor, wenn wir schließen, dass [\(H_1\) im Kontext], obwohl in Wahrheit [\(H_0\) im Kontext] gilt.“</div>
<span class="tr">1. tür = haksız mahkumiyet (masumu suçlu ilan etmek). 2. tür = suçluyu serbest bırakmak.</span>''',
 [(r'Brötchen: \(H_0:\mu\ge60\), \(H_1:\mu<60\). Fehler 1. Art im Kontext?', r'Man schließt, dass die Brötchen im Mittel weniger als 60 g wiegen, obwohl sie in Wahrheit mindestens 60 g wiegen.', 'm'),
  (r'Gleicher Test, \(H_0\) wurde <b>nicht</b> abgelehnt. Welcher Fehler ist möglich?', r'nur Fehler 2. Art', 's')]))

T_klaus = [
 ('Gauß-Test linksseitig', 10,
  r'Eine Bäckerei gibt an, dass ihre Brötchen im Mittel <b>mindestens</b> 60 g wiegen. Der Verbraucherschutz vermutet, dass sie im Mittel <b>weniger</b> wiegen, und wiegt \(n=16\) zufällig ausgewählte Brötchen: \(\bar x=58.5\) g. Das Gewicht sei normalverteilt mit bekannter Varianz \(\sigma^2=16\). Signifikanzniveau \(\alpha=0.05\). (Hinweis: \(\Phi(1.5)=0.9332\), \(z_{0.95}=1.645\))',
  [(r'Stellen Sie das passende Hypothesenpaar auf.', 2, 's', r'\(H_0:\mu\ge60\) vs. \(H_1:\mu<60\) [2]'),
   (r'Berechnen Sie die Prüfgröße und geben Sie ihre Verteilung unter \(H_0\) an.', 3, 'm', r'\(\sigma=4\); \(Z=\frac{58.5-60}{4/\sqrt{16}}=-1.5\) [2]; \(Z\sim N(0,1)\) [1]'),
   (r'Geben Sie den Ablehnungsbereich an und treffen Sie die Testentscheidung im Sachzusammenhang.', 3, 'm', r'\(A=(-\infty;-1.645]\) [1]; \(-1.5\notin A\) → \(H_0\) nicht ablehnen [1]; Es kann nicht nachgewiesen werden, dass die Brötchen im Mittel weniger als 60 g wiegen [1]'),
   (r'Berechnen Sie den p-Wert. Welcher Fehler könnte hier vorliegen? Beschreiben Sie ihn im Sachzusammenhang.', 2, 'm', r'\(p=\Phi(-1.5)=0.0668\) [1]; Fehler 2. Art: Die Brötchen wiegen in Wahrheit weniger als 60 g, aber wir lehnen \(H_0\) nicht ab [1]')]),
 ('t-Test mit R-Output (Testat-/Altklausur-Typ)', 9,
  r'Eine Hotline gibt an, dass die mittlere Wartezeit 5 Minuten beträgt. Kund*innen vermuten, dass sie im Mittel <b>länger</b> warten müssen. Es werden 8 Wartezeiten gemessen (normalverteilt, Varianz unbekannt), α = 5 %. Eine Kommilitonin probiert drei R-Befehle:<br>'
  r'(1) <code>t.test(wz, mu=5, alternative="l")</code> → <code>t = ?, df = 7, p-value = 0.9977</code><br>'
  r'(2) <code>t.test(wz, mu=5, alternative="g")</code> → <code>t = 4.106, df = 7, p-value = 0.002269</code><br>'
  r'(3) <code>t.test(wz, mu=6, alternative="g")</code> → <code>t = ?, df = 7, p-value = 0.864</code><br>Hinweis: \(t_{7;0.95}=1.895\), \(t_{7;0.975}=2.365\).',
  [(r'Stellen Sie das Hypothesenpaar auf.', 2, 's', r'\(H_0:\mu\le5\) vs. \(H_1:\mu>5\) [2]'),
   (r'Welcher R-Code ist der richtige? Begründen Sie kurz.', 2, 's', r'Code (2): <code>mu=5</code> = \(\mu_0\) und <code>"g"</code> passt zu \(H_1:\mu>5\) [2]'),
   (r'Geben Sie die Verteilung der Prüfgröße unter \(H_0\) und den Ablehnungsbereich an.', 2, 's', r'\(T\sim t_7\) [1]; \(A=[1.895;\infty)\) [1]'),
   (r'Treffen Sie die Testentscheidung (über Prüfgröße <b>oder</b> p-Wert) und formulieren Sie das Ergebnis.', 3, 'm', r'\(t=4.106\in A\) bzw. \(p=0.0023<0.05\) → \(H_0\) ablehnen [2]; Zum Niveau 5 % ist abgesichert, dass die mittlere Wartezeit länger als 5 Minuten ist [1]')]),
 ('Anteilstest zweiseitig', 8,
  r'Eine Partei behauptet, dass genau 40 % der Wahlberechtigten sie unterstützen. Eine Zeitung bezweifelt diese Angabe (in beide Richtungen) und befragt 600 zufällig ausgewählte Personen; 216 davon unterstützen die Partei. α = 5 %. (Hinweis: \(\Phi(2)=0.9772\))',
  [(r'Stellen Sie das Hypothesenpaar auf.', 2, 's', r'\(H_0:\pi=0.4\) vs. \(H_1:\pi\neq0.4\) [2]'),
   (r'Berechnen Sie die Prüfgröße und geben Sie ihre (approximative) Verteilung unter \(H_0\) an.', 3, 'm', r'\(\hat\pi=\frac{216}{600}=0.36\); \(\sqrt{\frac{0.4\cdot0.6}{600}}=0.02\); \(Z=\frac{0.36-0.4}{0.02}=-2\) [2]; \(Z\overset{a}{\sim}N(0,1)\) [1]'),
   (r'Treffen Sie die Testentscheidung mithilfe des p-Werts und formulieren Sie das Ergebnis.', 3, 'm', r'\(p=2(1-\Phi(2))=0.0456\) [1]; \(0.0456<0.05\) → \(H_0\) ablehnen [1]; Der Anteil der Unterstützer weicht signifikant von 40 % ab [1]')]),
]

HEFTE = [
 ('crash_schaetzer.html', C1,
  deck('Schätzer: erwartungstreu oder nicht?', 'Crashkurs für die Klausur · von null bis zur Klausuraufgabe (ca. 5 Punkte) · ca. 60 Minuten',
       ['<b>Lerneinheit lesen</b> → sofort die <b>Übung</b> dazu lösen (Klausurlayout).', 'Danach 4 komplette <b>Klausuraufgaben</b>. Lösungen hinten – erst selbst rechnen!',
        'Ziel: Jede Aufgabe der Form „Testen Sie, ob … unverzerrt ist“ in 5 Minuten lösen.'],
       'Bu konuda integral ya da türev yok. Sadece 3 kural: sabitler dışarı, toplamlar ayrılır, E(Xᵢ) yerine verileni koy. Sonra parametreyle karşılaştır ve cümle yaz.'),
  S_units, S_klaus, 'Crashkurs_Schaetzer.pdf'),
 ('crash_bayes.html', C2,
  deck('Bayes &amp; totale Wahrscheinlichkeit', 'Crashkurs für die Klausur · Baum zeichnen → Pfade → Summe → Bayes · ca. 60 Minuten',
       ['<b>Lerneinheit lesen</b> → sofort die <b>Übung</b> dazu lösen.', 'Danach 3 komplette <b>Klausuraufgaben</b> (wie Altklausur A3). Lösungen hinten.',
        'Ziel: Die 11-Punkte-Aufgabe der Altklausur komplett lösen.'],
       'Senin iki hatan vardı: (1) ikinci yolda 0.3 yerine 0.7 kullanmak, (2) Bayes\'te paydayı (toplam olasılığı) yazmamak. Bu defter tam bu iki şeyi oturtuyor.'),
  B_units, B_klaus, 'Crashkurs_Bayes.pdf'),
 ('crash_tests.html', C3,
  deck('Hypothesentests', 'Crashkurs für die Klausur · Hypothesen → Prüfgröße → Entscheidung → Satz · R-Output · ca. 75 Minuten',
       ['<b>Lerneinheit lesen</b> → sofort die <b>Übung</b> dazu lösen.', 'Danach 3 komplette <b>Klausuraufgaben</b> (Gauß, t-Test mit R, Anteil). Lösungen hinten.',
        'Ziel: Die 8-Punkte-Testaufgabe vollständig – inkl. „Verteilung angeben“ und Antwortsatz.'],
       'Test sorusu her zaman aynı 4 parçadan oluşur. Altklausur\'da kaybettiğin puanlar: dağılımı yazmamak (1 P), yanlış R kodu (1 P), karar kutusunu boş bırakmak (2 P). Bunların hepsi bu defterde.'),
  T_units, T_klaus, 'Crashkurs_Tests.pdf'),
]

if __name__ == '__main__':
    for name, color, d, units, klaus, pdf in HEFTE:
        build(name, color, d, units, klaus)
        print(name, pdf)
