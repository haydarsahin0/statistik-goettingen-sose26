# Kochbuch 2: Tests, Konfidenzintervalle, Schätzer, Dichten – fertige Lösungswege zum Abschreiben
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'extra', 'kochbuch2.html')

CSS = r'''<style>
.w{width:auto!important;padding:0!important}
@page{size:A4 landscape;margin:9mm 10mm}
body{font-size:12.5px!important;background:#fff!important;line-height:1.35!important}
h1{font-size:28px!important;margin:0 0 2px!important}
.pb{break-before:page}
table.k{width:100%;border-collapse:collapse;margin:4px 0 8px}
table.k th{background:#1f4e79;color:#fff;font-family:Inter;font-size:11px;padding:4px 6px;text-align:left}
table.k td{border:1px solid #cfd6e0;padding:4px 5px;vertical-align:middle;font-size:11.5px}
table.k td.nw{white-space:nowrap}
table.k tr:nth-child(even) td{background:#f6f8fb}
table.k td.nr{font:800 12px Inter;color:#1f4e79;text-align:center;width:22px}
table.k td.res{background:#eaf6ec!important;font-weight:700}
.fam{font:800 15px Inter;color:#fff;border-radius:7px;padding:5px 12px;margin:6px 0 3px;break-after:avoid}
.form{border:2px solid #1f1d1a;border-radius:10px;padding:6px 12px;margin:6px 0;break-inside:avoid}
.form h3{margin:0 0 3px;font-family:Inter;font-size:14px}
.how{display:flex;gap:10px}.how>div{flex:1;border:1.5px solid #1f4e79;border-radius:10px;padding:6px 10px}
.how b.n{display:inline-block;width:22px;height:22px;border-radius:50%;background:#1f4e79;color:#fff;text-align:center;line-height:22px;font-family:Inter;margin-right:6px}
.tr{border-left:3px solid #00796b;background:#e3f4f2;padding:3px 9px;font-style:italic;color:#0f4f47;margin:4px 0;border-radius:0 6px 6px 0}
.tpl{border:2px dashed #a8823a;border-radius:10px;padding:6px 14px;background:#fffaf0;font-size:13.5px;line-height:1.65;break-inside:avoid}
.two{display:flex;gap:10px}.two>div{flex:1}
.small{font-size:11px;color:#555}
</style>'''

def table(head, rows, res_col=None, nw=(), ds=False):
    h = '<table class="k"><tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>'
    for r in rows:
        h += '<tr>'
        for i, c in enumerate(r):
            if ds: c = str(c).replace('\\(', '\\(\\displaystyle ')
            cls = []
            if i == 0 and str(c).isdigit(): cls.append('nr')
            if i == res_col: cls.append('res')
            if i in nw: cls.append('nw')
            h += f'<td class="{" ".join(cls)}">{c}</td>' if cls else f'<td>{c}</td>'
        h += '</tr>'
    return h + '</table>'

PB = '<div class="pb"></div>'

# ================= Seite 1: Übersicht + Quantile
p1 = r'''
<div class="kick">Kochbuch 2 · Test · Konfidenzintervall · Schätzer · Dichte · zum Abschreiben aufs A4-Blatt</div>
<h1>Aufgabe erkennen → <em>Zeile finden</em> → Lösungsweg abschreiben.</h1>
<div class="tr">Kullanım: Sorudaki kelimeye bak (sol sütun) → hangi sayfa/satır olduğunu bul → şablondaki cümleleri aynen yaz, sadece sayıları değiştir. ML için ayrı ML-Kochbuch var.</div>
''' + table(['In der Aufgabe steht …', 'Ne istiyor', 'Rezept', 'Seite'], [
 ['„Hypothesenpaar“, „Prüfgröße“, „Testentscheidung“, „kritischer Wert“, „p-Wert“', 'hipotez testi', 'Test-Schablone + Katalog', '2–4'],
 ['„σ bekannt“ / „Standardabweichung … bekannt“', 'Gauß-Test', 'Test-Katalog Nr. 1', '3'],
 ['„Varianz unbekannt“, \\(s\\) oder \\(s_*\\) gegeben, t.test-Output', 't-Test', 'Test-Katalog Nr. 2', '3'],
 ['„Anteil“, „Prozent der …“, „Erfolgswahrscheinlichkeit“', 'oran testi', 'Test-Katalog Nr. 3/4', '3'],
 ['„Varianz“ / „Streuung“ testen', 'χ²-Varianztest', 'Test-Katalog Nr. 5', '3'],
 ['„ohne Verteilungsannahme“, „Median“', 'işaret testi', 'Test-Katalog Nr. 6', '3'],
 ['Kreuztabelle, „unabhängig?“ / „Gleichverteilung?“, „Würfel fair?“', 'χ²-Test', 'Test-Katalog Nr. 7/8', '3'],
 ['„Fehler 1./2. Art“', 'hata türleri', 'Fehler-Kasten', '4'],
 ['„Konfidenzintervall“, „Vertrauensintervall“, „Wie groß muss n sein?“', 'güven aralığı', 'KI-Katalog', '5'],
 ['„erwartungstreu“, „unverzerrt“, „Bias“, „Var(T)“, „vorzuziehen“, „MSE“, „konsistent“', 'tahminci kalitesi', 'Schätzer-Schablone + Katalog', '6'],
 ['„Bestimmen Sie c“, „Dichte“, „Verteilungsfunktion F(x)“, „E(X)“, „Var(X)“, „Median“', 'yoğunluk', 'Dichte-Schablone + Katalog', '7–8'],
 ['„exponentialverteilt“, „gleichverteilt“, „normalverteilt“', 'hazır dağılım', 'Verteilungs-Kasten', '8'],
], nw=(3,)) + r'''
<div class="two"><div>
<div class="form"><h3>Quantile der Standardnormalverteilung \(z_p\)</h3>
\(z_{0.90}=1.282\) · \(z_{0.95}=1.645\) · \(z_{0.975}=1.960\) · \(z_{0.99}=2.326\) · \(z_{0.995}=2.576\)<br>
<span class="small">\(\alpha=0.05\): zweiseitig \(1.96\), einseitig \(1.645\) · \(\alpha=0.01\): zweiseitig \(2.576\), einseitig \(2.326\) · Symmetrie: \(\Phi(-z)=1-\Phi(z)\), \(z_{0.05}=-1.645\)</span></div>
</div><div>
<div class="form"><h3>Quantile \(\chi^2_{df;\,0.95}\) (rechts, für χ²-Tests)</h3>
\(df=1{:}\ 3.841\) · \(2{:}\ 5.991\) · \(3{:}\ 7.815\) · \(4{:}\ 9.488\) · \(5{:}\ 11.070\) · \(6{:}\ 12.592\)<br>
<span class="small">t-Quantile stehen in der Aufgabe (Hinweis) oder in der Tabelle der Formelsammlung (15.2), z. B. \(t_{15;0.975}=2.131\), \(t_{15;0.95}=1.753\).</span></div>
</div></div>
'''

# ================= Seite 2: Test-Schablone
p2 = PB + r'''<div class="fam" style="background:#b42318">Test-Schablone – genau so aufschreiben (4 Schritte = 8 Punkte)</div>
<div class="tpl"><b>Aufgabe:</b> Hersteller: Füllmenge im Mittel <b>genau</b> 50 ml. Gemessen: \(n=16\), \(\bar x=52\). Normalverteilt, \(\sigma=4\) bekannt, \(\alpha=0.05\).<br>
<b>(a) Hypothesen:</b> \(H_0:\ \mu=50\quad\text{vs.}\quad H_1:\ \mu\neq50\)<br>
<b>(b) Prüfgröße:</b> \(Z=\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}=\dfrac{52-50}{4/\sqrt{16}}=\dfrac{2}{1}=2\) &nbsp;&nbsp; Unter \(H_0\) gilt: \(Z\sim N(0,1)\).<br>
<b>(c) Entscheidung:</b> Ablehnungsbereich \(|z|\gt z_{1-\alpha/2}=z_{0.975}=1.96\). Da \(|z|=2\gt1.96\), wird \(H_0\) <b>abgelehnt</b>.<br>
<b>Antwortsatz:</b> Zum Signifikanzniveau \(\alpha=0.05\) kann nachgewiesen werden, dass die mittlere Füllmenge von 50 ml abweicht.<br>
<b>(d) p-Wert:</b> \(p=2\,(1-\Phi(|z|))=2\,(1-\Phi(2))=2\,(1-0.9772)=0.0456\lt\alpha=0.05\ \Rightarrow H_0\) ablehnen.</div>
<div class="tr">Kendi sorunda sadece sayıları ve bağlamı (Füllmenge → Laufzeit, Wartezeit …) değiştir. 4 adımın hepsini YAZ: hipotez, test istatistiği + dağılımı, karar + cümle, p-değeri.</div>
<div class="two"><div>
<div class="form"><h3>Schritt 1: Hypothesen aus dem Text</h3>
Was <b>nachgewiesen</b> / vermutet / behauptet werden soll → kommt in \(H_1\). Das Gleichheitszeichen steht immer in \(H_0\).<br>
„mehr als“, „größer“, „übersteigt“, „länger“ → \(H_1:\mu\gt\mu_0\) (rechtsseitig)<br>
„weniger als“, „kleiner“, „unterschreitet“, „kürzer“ → \(H_1:\mu\lt\mu_0\) (linksseitig)<br>
„genau“, „weicht ab“, „ungleich“, „in beide Richtungen“ → \(H_1:\mu\neq\mu_0\) (zweiseitig)<br>
<span class="small">Hersteller sagt „mindestens 500 g“, Verbraucher vermutet weniger → \(H_0:\mu\ge500\) vs. \(H_1:\mu\lt500\).</span></div>
</div><div>
<div class="form"><h3>Schritt 3: Ablehnungsbereich (Niveau \(\alpha\))</h3>
\(H_1:\mu\neq\mu_0\): ablehnen, wenn \(|z|\gt z_{1-\alpha/2}\) &nbsp;(5 %: \(1.96\))<br>
\(H_1:\mu\gt\mu_0\): ablehnen, wenn \(z\gt z_{1-\alpha}\) &nbsp;(5 %: \(1.645\))<br>
\(H_1:\mu\lt\mu_0\): ablehnen, wenn \(z\lt -z_{1-\alpha}\) &nbsp;(5 %: \(-1.645\))<br>
Beim t-Test genauso, nur \(t_{n-1;\,1-\alpha/2}\) bzw. \(t_{n-1;\,1-\alpha}\) statt \(z\).</div>
<div class="form"><h3>Schritt 4: p-Wert</h3>
zweiseitig \(p=2\,(1-\Phi(|z|))\) · rechts \(p=1-\Phi(z)\) · links \(p=\Phi(z)\)<br>
<b>Regel: \(p\le\alpha\Rightarrow H_0\) ablehnen; \(p\gt\alpha\Rightarrow H_0\) nicht ablehnen.</b></div>
</div></div>
<div class="form"><h3>Antwortsätze (passend einsetzen)</h3>
<b>abgelehnt:</b> „Zum Niveau \(\alpha=\dots\) wird \(H_0\) abgelehnt. Es kann nachgewiesen werden, dass [Größe] [größer als / kleiner als / ungleich] [\(\mu_0\)] ist.“<br>
<b>nicht abgelehnt:</b> „\(H_0\) kann zum Niveau \(\alpha=\dots\) nicht abgelehnt werden. Es kann <u>nicht</u> nachgewiesen werden, dass … (\(H_0\) ist damit <u>nicht</u> bewiesen).“</div>
'''

# ================= Seite 3: Test-Katalog
p3 = PB + '<div class="fam" style="background:#1f4e79">Test-Katalog – Prüfgröße, Verteilung unter \\(H_0\\), wann ablehnen?</div>' + table(
 ['#', 'Test · wann?', 'Hypothesen', 'Prüfgröße', 'unter \\(H_0\\)', 'ablehnen, wenn … (zweiseitig / rechts / links)'], [
 ['1', '<b>Gauß-Test</b> · μ, σ <b>bekannt</b> (oder n groß)', '\\(H_0:\\mu=\\mu_0\\)', '\\(Z=\\dfrac{\\bar x-\\mu_0}{\\sigma/\\sqrt n}\\)', '\\(N(0,1)\\)', '\\(|z|\\gt z_{1-\\alpha/2}\\) / \\(z\\gt z_{1-\\alpha}\\) / \\(z\\lt-z_{1-\\alpha}\\)'],
 ['2', '<b>t-Test</b> · μ, σ <b>unbekannt</b>, normalverteilt', '\\(H_0:\\mu=\\mu_0\\)', '\\(T=\\dfrac{\\bar x-\\mu_0}{s_*/\\sqrt n}\\)', '\\(t_{n-1}\\)', '\\(|t|\\gt t_{n-1;1-\\alpha/2}\\) / \\(t\\gt t_{n-1;1-\\alpha}\\) / \\(t\\lt-t_{n-1;1-\\alpha}\\)'],
 ['3', '<b>Approx. Binomialtest</b> · Anteil π, n groß', '\\(H_0:\\pi=\\pi_0\\)', '\\(Z=\\dfrac{\\hat\\pi-\\pi_0}{\\sqrt{\\pi_0(1-\\pi_0)/n}}\\)', '\\(\\approx N(0,1)\\)', 'wie Gauß-Test'],
 ['4', '<b>Exakter Binomialtest</b> · Anteil, n klein', '\\(H_0:\\pi=\\pi_0\\)', '\\(X\\)= Anzahl Erfolge', '\\(B(n,\\pi_0)\\)', 'p-Wert: rechts \\(P(X\\ge x)\\) / links \\(P(X\\le x)\\) / zweis. \\(2\\cdot\\)kleinere Seite; \\(p\\le\\alpha\\)'],
 ['5', '<b>χ²-Varianztest</b> · σ² testen, normalverteilt', '\\(H_0:\\sigma^2=\\sigma_0^2\\)', '\\(\\chi^2=\\dfrac{(n-1)s_*^2}{\\sigma_0^2}\\)', '\\(\\chi^2_{n-1}\\)', 'außerhalb \\([\\chi^2_{n-1;\\alpha/2};\\chi^2_{n-1;1-\\alpha/2}]\\) / \\(\\gt\\chi^2_{n-1;1-\\alpha}\\) / \\(\\lt\\chi^2_{n-1;\\alpha}\\)'],
 ['6', '<b>Vorzeichentest</b> · Median, ohne Verteilungsannahme', '\\(H_0:x_{0.5}=\\theta_0\\)', '\\(Z\\)= Anzahl \\(x_i\\le\\theta_0\\)', '\\(B(n;0.5)\\)', 'p-Wert über Binomialverteilung wie Nr. 4; \\(p\\le\\alpha\\)'],
 ['7', '<b>χ²-Unabhängigkeitstest</b> · Kreuztabelle', '\\(H_0\\): X, Y unabhängig', '\\(\\chi^2=\\sum\\dfrac{(h_{ij}-e_{ij})^2}{e_{ij}}\\), \\(e_{ij}=\\dfrac{h_{i\\cdot}h_{\\cdot j}}{n}\\)', '\\(\\chi^2_{(k-1)(m-1)}\\)', '\\(\\chi^2\\gt\\chi^2_{df;1-\\alpha}\\) (immer rechts)'],
 ['8', '<b>χ²-Anpassungstest</b> · „folgt Verteilung …?“, „Würfel fair?“', '\\(H_0\\): \\(P(X=j)=p_j\\)', '\\(\\chi^2=\\sum\\dfrac{(h_j-np_j)^2}{np_j}\\)', '\\(\\chi^2_{k-1}\\)', '\\(\\chi^2\\gt\\chi^2_{k-1;1-\\alpha}\\) (immer rechts)'],
]) + r'''
<div class="tr">Hangi test? σ veriliyor ve "bekannt" deniyorsa → 1 (Gauß). Sadece s veya s* varsa → 2 (t). Yüzde/oran → 3. Varyans → 5. "Verteilungsannahme yok" + medyan → 6. Tablo + "unabhängig" → 7. "Verteilung/fair" → 8.</div>
<div class="two"><div>
<div class="form"><h3>\(s_*\) aus \(s\) (Aufgabe gibt empirische \(s\))</h3>
\(s_*^2=\dfrac{n}{n-1}\,s^2\) · \(s_*^2=\dfrac{1}{n-1}\Big(\sum x_i^2-n\bar x^2\Big)\)</div>
<div class="form"><h3>Test ↔ Konfidenzintervall</h3>
Zweiseitiger Test zum Niveau \(\alpha\) lehnt \(H_0:\mu=\mu_0\) genau dann ab, wenn \(\mu_0\) <b>nicht</b> im \((1-\alpha)\)-KI liegt.</div>
</div><div>
<div class="form"><h3>Fehler 1. und 2. Art</h3>
<b>Fehler 1. Art:</b> \(H_0\) wird abgelehnt, obwohl \(H_0\) wahr ist. \(P=\alpha\).<br>
<b>Fehler 2. Art:</b> \(H_0\) wird nicht abgelehnt, obwohl \(H_1\) wahr ist. \(P=\beta\).<br>
<span class="small">Satz im Kontext: „Ein Fehler 1. Art läge vor, wenn wir schließen, dass die Füllmenge von 50 ml abweicht, obwohl sie in Wahrheit 50 ml beträgt.“ Abgelehnt → nur Fehler 1. Art möglich; nicht abgelehnt → nur Fehler 2. Art möglich.</span></div>
</div></div>
'''

# ================= Seite 4: Test-Rechenbeispiele
p4 = PB + '<div class="fam" style="background:#2e7d32">Test-Rechenbeispiele – jede Variante einmal komplett durchgerechnet</div>' + table(
 ['#', 'Aufgabe (kurz)', '\\(H_0\\) vs. \\(H_1\\)', 'Prüfgröße', 'kritischer Wert', 'Entscheidung · p-Wert'], [
 ['1', 'μ0=50, σ=4, n=16, x̄=52, „weicht ab“', '\\(\\mu=50\\) vs. \\(\\mu\\neq50\\)', '\\(z=\\frac{52-50}{4/4}=2\\)', '\\(1.96\\)', '\\(2\\gt1.96\\): ablehnen · \\(p=2(1-0.9772)=0.0456\\)'],
 ['1', 'gleiche Daten, „mehr als 50“', '\\(\\mu\\le50\\) vs. \\(\\mu\\gt50\\)', '\\(z=2\\)', '\\(1.645\\)', '\\(2\\gt1.645\\): ablehnen · \\(p=1-0.9772=0.0228\\)'],
 ['1', 'μ0=500, σ=10, n=25, x̄=497, „weniger als 500“', '\\(\\mu\\ge500\\) vs. \\(\\mu\\lt500\\)', '\\(z=\\frac{497-500}{10/5}=-1.5\\)', '\\(-1.645\\)', '\\(-1.5\\gt-1.645\\): nicht ablehnen · \\(p=\\Phi(-1.5)=1-0.9332=0.0668\\)'],
 ['2', 'μ0=30, n=16, x̄=32, s*=4, „weicht ab“', '\\(\\mu=30\\) vs. \\(\\mu\\neq30\\)', '\\(t=\\frac{32-30}{4/4}=2\\), \\(df=15\\)', '\\(t_{15;0.975}=2.131\\)', '\\(2\\lt2.131\\): nicht ablehnen'],
 ['2', 'gleiche Daten, „größer als 30“', '\\(\\mu\\le30\\) vs. \\(\\mu\\gt30\\)', '\\(t=2\\), \\(df=15\\)', '\\(t_{15;0.95}=1.753\\)', '\\(2\\gt1.753\\): ablehnen'],
 ['3', 'π0=0.5, n=100, 60 Erfolge, „weicht ab“', '\\(\\pi=0.5\\) vs. \\(\\pi\\neq0.5\\)', '\\(z=\\frac{0.6-0.5}{\\sqrt{0.25/100}}=\\frac{0.1}{0.05}=2\\)', '\\(1.96\\)', '\\(2\\gt1.96\\): ablehnen · \\(p=0.0456\\)'],
 ['4', 'n=10, π0=0.5, 9 Erfolge, „größer“', '\\(\\pi\\le0.5\\) vs. \\(\\pi\\gt0.5\\)', '\\(x=9\\), \\(X\\sim B(10;0.5)\\)', '—', '\\(p=P(X\\ge9)=\\frac{10+1}{1024}=0.0107\\le0.05\\): ablehnen'],
 ['5', 'σ0²=4, n=10, s*²=8, „größer“', '\\(\\sigma^2\\le4\\) vs. \\(\\sigma^2\\gt4\\)', '\\(\\chi^2=\\frac{9\\cdot8}{4}=18\\)', '\\(\\chi^2_{9;0.95}=16.919\\)', '\\(18\\gt16.919\\): ablehnen'],
 ['5', 'gleiche Daten, „weicht ab“', '\\(\\sigma^2=4\\) vs. \\(\\sigma^2\\neq4\\)', '\\(\\chi^2=18\\)', '\\([2.700;\\,19.023]\\)', '\\(18\\) liegt innerhalb: nicht ablehnen'],
 ['6', 'n=10, θ0=10, 2 Werte ≤ 10, zweiseitig', '\\(x_{0.5}=10\\) vs. \\(x_{0.5}\\neq10\\)', '\\(z=2\\), \\(Z\\sim B(10;0.5)\\)', '—', '\\(P(Z\\le2)=\\frac{1+10+45}{1024}=0.0547\\); \\(p=0.109\\gt0.05\\): nicht abl.'],
 ['7', '2×2: Männer ja 30/nein 20, Frauen ja 20/nein 30', 'unabhängig vs. abhängig', '\\(e_{ij}=\\frac{50\\cdot50}{100}=25\\); \\(\\chi^2=4\\cdot\\frac{5^2}{25}=4\\)', '\\(\\chi^2_{1;0.95}=3.841\\)', '\\(4\\gt3.841\\): ablehnen → Zusammenhang'],
 ['8', 'Würfel 60×: 5, 8, 9, 8, 10, 20', 'fair (\\(p_j=\\frac16\\)) vs. nicht fair', '\\(e_j=10\\); \\(\\chi^2=\\frac{25+4+1+4+0+100}{10}=13.4\\)', '\\(\\chi^2_{5;0.95}=11.070\\)', '\\(13.4\\gt11.07\\): ablehnen → nicht fair'],
], res_col=5, ds=True) + r'''
<div class="two"><div>
<div class="form"><h3>R-Output lesen (auch Teil B!)</h3>
<code>t = 2.874, df = 24, p-value = 0.0042</code> → \(p\lt0.05\Rightarrow H_0\) ablehnen.<br>
<code>X-squared = 5.120, df = 3, p-value = 0.163</code> → \(p\gt0.05\Rightarrow H_0\) nicht ablehnen.<br>
<code>alternative = "greater"</code> ↔ \(H_1:\mu\gt\mu_0\) · <code>"less"</code> ↔ \(H_1:\mu\lt\mu_0\) · <code>"two.sided"</code> ↔ \(\neq\)</div>
</div><div>
<div class="form"><h3>Typische Fallen</h3>
• \(\sigma/\sqrt n\) – nicht \(\sigma/n\) und nicht \(\sigma^2\)!<br>
• Zweiseitig: \(\alpha/2\) → \(1.96\); einseitig: \(\alpha\) → \(1.645\).<br>
• „\(H_0\) wird angenommen / bewiesen“ ist <b>falsch</b> → „nicht abgelehnt“.<br>
• Linksseitig ist \(z\) meist negativ – Vorzeichen behalten!</div>
</div></div>
'''

# ================= Seite 5: Konfidenzintervalle
p5 = PB + '<div class="fam" style="background:#7030a0">Konfidenzintervall-Katalog – Formel, Beispiel, Interpretation</div>' + table(
 ['#', 'wann?', 'Formel \\((1-\\alpha)\\)-KI', 'Beispiel (95 %)', 'Ergebnis'], [
 ['1', 'μ, σ <b>bekannt</b>', '\\(\\Big[\\bar x\\pm z_{1-\\alpha/2}\\dfrac{\\sigma}{\\sqrt n}\\Big]\\)', '\\(\\bar x=52,\\ \\sigma=4,\\ n=16\\): \\(52\\pm1.96\\cdot\\frac44\\)', '\\([50.04;\\ 53.96]\\)'],
 ['2', 'μ, σ <b>unbekannt</b>', '\\(\\Big[\\bar x\\pm t_{n-1;1-\\alpha/2}\\dfrac{s_*}{\\sqrt n}\\Big]\\)', '\\(\\bar x=32,\\ s_*=4,\\ n=16\\): \\(32\\pm2.131\\cdot\\frac44\\)', '\\([29.869;\\ 34.131]\\)'],
 ['3', 'Anteil π, n groß', '\\(\\Big[\\hat\\pi\\pm z_{1-\\alpha/2}\\sqrt{\\dfrac{\\hat\\pi(1-\\hat\\pi)}{n}}\\Big]\\)', '\\(\\hat\\pi=0.6,\\ n=100\\): \\(0.6\\pm1.96\\cdot0.049\\)', '\\([0.504;\\ 0.696]\\)'],
 ['4', 'Varianz σ²', '\\(\\Big[\\dfrac{(n-1)s_*^2}{\\chi^2_{n-1;1-\\alpha/2}};\\ \\dfrac{(n-1)s_*^2}{\\chi^2_{n-1;\\alpha/2}}\\Big]\\)', '\\(n=10,\\ s_*^2=8\\): \\(\\frac{72}{19.023};\\ \\frac{72}{2.700}\\)', '\\([3.785;\\ 26.663]\\)'],
], res_col=4) + r'''
<div class="tpl"><b>Schablone:</b> Gesucht: 95 %-KI für μ, \(\sigma=4\) bekannt, \(n=16\), \(\bar x=52\).<br>
\(1-\alpha=0.95\Rightarrow z_{1-\alpha/2}=z_{0.975}=1.96\). &nbsp; \(\Big[\bar x-z_{0.975}\frac{\sigma}{\sqrt n};\ \bar x+z_{0.975}\frac{\sigma}{\sqrt n}\Big]=\Big[52-1.96\cdot\frac{4}{4};\ 52+1.96\cdot\frac44\Big]=[50.04;\ 53.96]\)<br>
<b>Interpretation:</b> Bei wiederholter Stichprobenziehung überdecken etwa 95 % der so konstruierten Intervalle den wahren Mittelwert μ.</div>
<div class="two"><div>
<div class="form"><h3>Richtig / falsch (Multiple Choice)</h3>
✗ „μ liegt mit 95 % Wahrscheinlichkeit in [50.04; 53.96].“ (μ ist fest, kein Zufall)<br>
✗ „95 % der Daten liegen im KI.“<br>
✓ „95 % der so konstruierten Intervalle enthalten μ.“<br>
✓ Höheres Niveau (99 %) → <b>breiteres</b> KI · größeres n → <b>schmaleres</b> KI · größeres σ → breiter.</div>
</div><div>
<div class="form"><h3>Länge und nötiges n</h3>
Länge \(L=2\,z_{1-\alpha/2}\dfrac{\sigma}{\sqrt n}\) · halbe Breite \(e=z_{1-\alpha/2}\dfrac{\sigma}{\sqrt n}\)<br>
\(n\ge\Big(\dfrac{z_{1-\alpha/2}\,\sigma}{e}\Big)^2=\Big(\dfrac{2z_{1-\alpha/2}\,\sigma}{L}\Big)^2\) → <b>immer aufrunden</b><br>
<span class="small">Beispiel: σ=4, e=1, 95 %: \(n\ge(1.96\cdot4)^2=61.47\Rightarrow n=62\). Halbe Breite halbieren → n vervierfachen.</span><br>
<span class="small">Rückwärts: KI \([a;b]\) gegeben → \(\bar x=\frac{a+b}2\), \(e=\frac{b-a}2\).</span></div>
</div></div>
'''

# ================= Seite 6: Schätzer
p6 = PB + '<div class="fam" style="background:#c55a11">Schätzer-Schablone – erwartungstreu, Varianz, welcher ist besser?</div>' + r'''
<div class="how">
<div><b class="n">1</b><b>Erwartungswert</b><br>\(E\big(\sum a_iX_i\big)=\big(\sum a_i\big)\,\mu\)<br><b>Summe der Koeffizienten \(=1\)</b> ⇔ erwartungstreu für μ.<br>\(\text{Bias}(T)=E(T)-\theta\)</div>
<div><b class="n">2</b><b>Varianz</b> (unabhängig)<br>\(Var\big(\sum a_iX_i\big)=\big(\sum a_i^2\big)\,\sigma^2\)<br><b>Koeffizienten quadrieren!</b> Minus wird plus.<br>\(Var(\bar X)=\dfrac{\sigma^2}{n}\)</div>
<div><b class="n">3</b><b>Vergleichen</b><br>Beide erwartungstreu → <b>kleinere Varianz</b> ist besser (effizienter).<br>Sonst: \(MSE=Var(T)+\text{Bias}^2\) → kleiner ist besser.<br>Konsistent: \(MSE\to0\) für \(n\to\infty\).</div></div>
<div class="tpl"><b>Aufgabe:</b> \(T_1=0.5X_1+0.3X_2+0.2X_3\), \(T_2=X_1-X_2+X_3\), \(E(X_i)=\mu\), \(Var(X_i)=\sigma^2\), unabhängig.<br>
<b>(a)</b> \(E(T_1)=0.5E(X_1)+0.3E(X_2)+0.2E(X_3)=(0.5+0.3+0.2)\mu=\mu\ \Rightarrow T_1\) ist erwartungstreu.<br>
\(\phantom{(a)}\ E(T_2)=E(X_1)-E(X_2)+E(X_3)=\mu-\mu+\mu=\mu\ \Rightarrow T_2\) ist erwartungstreu.<br>
<b>(b)</b> \(Var(T_1)=0.5^2\sigma^2+0.3^2\sigma^2+0.2^2\sigma^2=(0.25+0.09+0.04)\sigma^2=0.38\sigma^2\)<br>
\(\phantom{(b)}\ Var(T_2)=1^2\sigma^2+(-1)^2\sigma^2+1^2\sigma^2=3\sigma^2\)<br>
\(\phantom{(b)}\ \) Da beide erwartungstreu sind und \(0.38\sigma^2\lt3\sigma^2\), ist \(T_1\) vorzuziehen. \(Var(\bar X)=\frac{\sigma^2}{3}\approx0.333\sigma^2\lt0.38\sigma^2\Rightarrow \bar X\) ist noch besser.</div>
''' + table(['#', 'Schätzer \\(T\\)', '\\(E(T)\\)', 'Bias', '\\(Var(T)\\)', 'Bemerkung'], [
 ['1', '\\(\\bar X=\\frac1n\\sum X_i\\)', '\\(\\mu\\)', '0', '\\(\\frac{\\sigma^2}{n}\\)', 'erwartungstreu, konsistent, bester linearer'],
 ['2', '\\(X_1\\)', '\\(\\mu\\)', '0', '\\(\\sigma^2\\)', 'erwartungstreu, aber <b>nicht konsistent</b> (Var hängt nicht von n ab)'],
 ['3', '\\(aX_1+(1-a)X_2\\)', '\\(\\mu\\)', '0', '\\((a^2+(1-a)^2)\\sigma^2\\)', 'minimal bei \\(a=0.5\\) → \\(\\frac{\\sigma^2}2\\)'],
 ['4', '\\(2X_1-X_2\\)', '\\(\\mu\\)', '0', '\\(5\\sigma^2\\)', 'erwartungstreu, aber große Varianz'],
 ['5', '\\(\\frac14(X_1+X_2+X_3)\\)', '\\(\\frac34\\mu\\)', '\\(-\\frac14\\mu\\)', '\\(\\frac{3}{16}\\sigma^2\\)', 'verzerrt; \\(MSE=\\frac3{16}\\sigma^2+\\frac1{16}\\mu^2\\)'],
 ['6', '\\(\\frac1{n+1}\\sum X_i\\)', '\\(\\frac{n}{n+1}\\mu\\)', '\\(-\\frac{\\mu}{n+1}\\)', '\\(\\frac{n\\sigma^2}{(n+1)^2}\\)', 'verzerrt, aber asympt. erwartungstreu und konsistent'],
 ['7', '\\(c\\sum X_i\\) – c gesucht', '\\(cn\\mu\\)', '—', '\\(c^2n\\sigma^2\\)', 'erwartungstreu ⇔ \\(cn=1\\Rightarrow c=\\frac1n\\)'],
 ['8', '\\(s^2=\\frac1n\\sum(X_i-\\bar X)^2\\)', '\\(\\frac{n-1}{n}\\sigma^2\\)', '\\(-\\frac{\\sigma^2}n\\)', '—', 'verzerrt → deshalb \\(s_*^2=\\frac1{n-1}\\sum(X_i-\\bar X)^2\\) (erwartungstreu)'],
 ['9', '\\(2\\bar X\\) bei \\(U(0,\\theta)\\)', '\\(2\\cdot\\frac\\theta2=\\theta\\)', '0', '\\(4\\cdot\\frac{\\theta^2}{12n}=\\frac{\\theta^2}{3n}\\)', 'erwartungstreu für θ'],
 ['10', '\\(\\bar X\\) bei Poisson / Bernoulli', '\\(\\lambda\\) / \\(\\pi\\)', '0', '\\(\\frac\\lambda n\\) / \\(\\frac{\\pi(1-\\pi)}n\\)', 'erwartungstreu, konsistent'],
], nw=(1,2,3,4), ds=True) + r'''
<div class="tr">Kural: E için katsayıları TOPLA (1 ise yansız). Var için katsayıların KARESİNİ topla (eksi işareti kaybolur). İkisi de yansızsa küçük varyans kazanır.</div>
'''

# ================= Seite 7: Dichte-Schablone
p7 = PB + '<div class="fam" style="background:#00796b">Dichte-Schablone – c, E(X), Var(X), F(x), Wahrscheinlichkeiten, Median</div>' + r'''
<div class="tpl"><b>Aufgabe:</b> \(f(x)=c\,(2-x)\) für \(0\le x\le2\), sonst \(0\).<br>
<b>c:</b> \(\displaystyle\int_0^2 c(2-x)\,dx=c\Big[2x-\frac{x^2}{2}\Big]_0^2=c\,(4-2)=2c\overset{!}{=}1\ \Rightarrow\ c=\frac12\). Außerdem \(f(x)\ge0\) für alle x ✓.<br>
<b>E(X):</b> \(\displaystyle E(X)=\int_0^2 x\cdot\tfrac12(2-x)\,dx=\frac12\Big[x^2-\frac{x^3}{3}\Big]_0^2=\frac12\Big(4-\frac83\Big)=\frac23\)<br>
<b>Var(X):</b> \(\displaystyle E(X^2)=\int_0^2 x^2\cdot\tfrac12(2-x)\,dx=\frac12\Big[\frac{2x^3}{3}-\frac{x^4}{4}\Big]_0^2=\frac12\Big(\frac{16}3-4\Big)=\frac23\); &nbsp; \(Var(X)=E(X^2)-E(X)^2=\frac23-\frac49=\frac29\)<br>
<b>F(x):</b> \(\displaystyle\int_0^x\tfrac12(2-t)\,dt=x-\frac{x^2}{4}\) &nbsp;⇒&nbsp; \(F(x)=\begin{cases}0,&x\lt0\\[2pt] x-\frac{x^2}{4},&0\le x\le2\\[2pt]1,&x\gt2\end{cases}\)<br>
<b>P:</b> \(P(X\gt1)=1-F(1)=1-\frac34=\frac14\) · \(P(0.5\le X\le1)=F(1)-F(0.5)=\frac34-\frac{7}{16}=\frac5{16}\)<br>
<b>Median:</b> \(F(x)=0.5\Leftrightarrow x-\frac{x^2}4=\frac12\Leftrightarrow x^2-4x+2=0\Rightarrow x=2-\sqrt2=0.586\) (die Lösung im Träger nehmen)</div>
<div class="two"><div>
<div class="form"><h3>Integrieren – das reicht für jede Klausur</h3>
\(\int x^k\,dx=\dfrac{x^{k+1}}{k+1}\) · \(\int c\,dx=cx\) · \(\int e^{-\lambda x}dx=-\frac1\lambda e^{-\lambda x}\)<br>
Klammern <b>vorher ausmultiplizieren</b>: \(x(2-x)=2x-x^2\)<br>
Grenzen: \([G(x)]_a^b=G(b)-G(a)\) — bei \(a=0\) fällt meist alles weg.</div>
</div><div>
<div class="form"><h3>Eigenschaften einer Dichte (Satz)</h3>
„\(f\) ist eine Dichte, da \(f(x)\ge0\) für alle \(x\) und \(\int_{-\infty}^{\infty}f(x)\,dx=1\).“<br>
\(P(X=a)=0\) bei stetigen ZV ⇒ \(P(X\lt a)=P(X\le a)\). \(f(x)\) darf größer als 1 sein.<br>
\(F'(x)=f(x)\) · \(P(a\lt X\le b)=F(b)-F(a)\)</div>
</div></div>
<div class="tr">Sıra hep aynı: (1) ∫f=1 → c, (2) E = ∫x·f, (3) E(X²)=∫x²·f → Var = E(X²) − E(X)², (4) F: 0 / formül / 1 olmak üzere 3 durum, (5) P(X&gt;a)=1−F(a), (6) medyan: F(x)=0.5 çöz.</div>
'''

# ================= Seite 8: Dichte-Katalog + Verteilungen + Bedava-Liste
p8 = PB + '<div class="fam" style="background:#1f4e79">Dichte-Katalog – Ergebnisse zum Vergleichen</div>' + table(
 ['#', 'Dichte (sonst 0)', 'c', '\\(E(X)\\)', '\\(E(X^2)\\)', '\\(Var(X)\\)', '\\(F(x)\\) im Träger', 'Median'], [
 ['1', '\\(c\\,x,\\ 0\\le x\\le2\\)', '\\(\\frac12\\)', '\\(\\frac43\\)', '\\(2\\)', '\\(\\frac29\\)', '\\(\\frac{x^2}4\\)', '\\(\\sqrt2=1.414\\)'],
 ['2', '\\(c\\,x^2,\\ 0\\le x\\le3\\)', '\\(\\frac19\\)', '\\(\\frac94\\)', '\\(\\frac{27}5\\)', '\\(\\frac{27}{80}\\)', '\\(\\frac{x^3}{27}\\)', '\\(\\sqrt[3]{13.5}=2.381\\)'],
 ['3', '\\(c\\,(2-x),\\ 0\\le x\\le2\\)', '\\(\\frac12\\)', '\\(\\frac23\\)', '\\(\\frac23\\)', '\\(\\frac29\\)', '\\(x-\\frac{x^2}4\\)', '\\(2-\\sqrt2=0.586\\)'],
 ['4', '\\(c\\,(x+1),\\ 0\\le x\\le2\\)', '\\(\\frac14\\)', '\\(\\frac76\\)', '\\(\\frac53\\)', '\\(\\frac{11}{36}\\)', '\\(\\frac{x^2}8+\\frac x4\\)', '\\(\\sqrt5-1=1.236\\)'],
 ['5', '\\(c\\,x(1-x),\\ 0\\le x\\le1\\)', '\\(6\\)', '\\(\\frac12\\)', '\\(\\frac3{10}\\)', '\\(\\frac1{20}\\)', '\\(3x^2-2x^3\\)', '\\(0.5\\)'],
 ['6', '\\(c\\sqrt x,\\ 0\\le x\\le1\\)', '\\(\\frac32\\)', '\\(\\frac35\\)', '\\(\\frac37\\)', '\\(\\frac{12}{175}\\)', '\\(x^{3/2}\\)', '\\(0.5^{2/3}=0.630\\)'],
 ['7', '\\(c\\,x^{-4},\\ x\\ge1\\)', '\\(3\\)', '\\(\\frac32\\)', '\\(3\\)', '\\(\\frac34\\)', '\\(1-x^{-3}\\)', '\\(\\sqrt[3]2=1.260\\)'],
 ['8', '\\(c\\,e^{-2x},\\ x\\ge0\\)', '\\(2\\)', '\\(\\frac12\\)', '\\(\\frac12\\)', '\\(\\frac14\\)', '\\(1-e^{-2x}\\)', '\\(\\frac{\\log2}{2}=0.347\\)'],
 ['9', '\\(c,\\ 2\\le x\\le6\\)', '\\(\\frac14\\)', '\\(4\\)', '\\(\\frac{52}3\\)', '\\(\\frac43\\)', '\\(\\frac{x-2}4\\)', '\\(4\\)'],
], nw=(1,2,3,4,5,6,7), ds=True) + r'''
<div class="two"><div>
<div class="form"><h3>Diskret: \(P(X=x)=c\,x\) für \(x=1,2,3,4\)</h3>
\(c(1+2+3+4)=10c=1\Rightarrow c=\frac1{10}\) · \(E(X)=\sum x\,P(X=x)=\frac{1+4+9+16}{10}=3\)<br>
\(E(X^2)=\frac{1+8+27+64}{10}=10\) · \(Var(X)=10-9=1\) · \(F\): Treppe, springt bei jedem \(x\).</div>
<div class="form"><h3>Fertige Verteilungen (nicht integrieren!)</h3>
<b>Exp(λ):</b> \(F(t)=1-e^{-\lambda t}\), \(P(T\gt t)=e^{-\lambda t}\), \(E=\frac1\lambda\), \(Var=\frac1{\lambda^2}\)<br>
<b>U(a,b):</b> \(f=\frac1{b-a}\), \(E=\frac{a+b}2\), \(Var=\frac{(b-a)^2}{12}\), \(P=\frac{\text{Breite}}{b-a}\)<br>
<b>N(μ,σ²):</b> \(P(X\le x)=\Phi\big(\frac{x-\mu}{\sigma}\big)\) · <b>Bin(n,π):</b> \(E=n\pi\), \(Var=n\pi(1-\pi)\) · <b>Poi(λ):</b> \(E=Var=\lambda\)<br>
\(E(aX+b)=aE(X)+b\) · \(Var(aX+b)=a^2Var(X)\)</div>
</div><div>
<div class="form" style="border-color:#b42318"><h3>Bedava-Punkte-Liste (PK3/PK4-Fehler)</h3>
• \(y=a+bx\): \(\bar y=a+b\bar x\), \(s_y=|b|\,s_x\) — <b>Multiplizieren ändert s!</b><br>
• Modus nicht eindeutig, wenn zwei Werte gleich oft am häufigsten.<br>
• \(r\)-Interpretation: Stärke + <b>Richtung</b> + linear + Variablen.<br>
• \(R^2=r^2\): „… % der Varianz von Y werden durch X erklärt.“<br>
• Prognose außerhalb \([x_{\min};x_{\max}]\) → „Extrapolation, unsicher“.<br>
• \(\overline{A\cap B}=\bar A\cup\bar B\), \(\overline{A\cup B}=\bar A\cap\bar B\); erst einzeln bilden, dann vereinigen.<br>
• \(P(A\mid B)=\frac{P(A\cap B)}{P(B)}\) · unabhängig ⇔ \(P(A\cap B)=P(A)P(B)\) · disjunkt ⇔ \(A\cap B=\emptyset\).<br>
• „keiner von n“: \(p^n\) · „mindestens einer“: \(1-(1-p)^n\).<br>
• ML (c): \(l''\lt0\Rightarrow\) Maximum — immer hinschreiben.<br>
• 3 Nachkommastellen im Ergebnis, 4 in Zwischenschritten; jede „Interpretieren/Begründen“-Frage mit Satz.</div>
</div></div>
'''

open(OUT, 'w').write(CSS + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8)
print(OUT)
