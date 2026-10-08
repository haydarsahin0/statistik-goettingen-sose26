# Kochbuch 2 – Adım Adım: jede Aufgabe als Rezeptkarte (Türkçe açıklama + was man in der Klausur hinschreibt)
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'extra', 'kochbuch2_adim.html')

CSS = r'''<style>
.w{width:auto!important;padding:0!important}
@page{size:A4;margin:10mm 11mm}
body{font-size:12.5px!important;background:#fff!important;line-height:1.4!important}
h1{font-size:27px!important;margin:0 0 4px!important}
.pb{break-before:page}
.card{border:2px solid var(--c);border-radius:12px;margin:0 0 10px;break-inside:avoid}
.card>.hd{border-radius:9px 9px 0 0;background:var(--c);color:#fff;font:800 15px Inter;padding:6px 12px;display:flex;gap:10px;align-items:center;break-after:avoid}
.card>.hd .no{background:#fff;color:var(--c);border-radius:6px;padding:1px 8px;font-size:14px}
.card>.bd{padding:7px 11px 9px}
.erk{font-size:12px;margin:0 0 4px}.erk b{color:var(--c)}
.ne{background:#fff7e0;border-left:4px solid #e0a100;padding:4px 10px;margin:4px 0 6px;border-radius:0 6px 6px 0}
table.st{width:100%;border-collapse:collapse;margin:4px 0}
table.st th{background:#eef1f6;font:700 11px Inter;text-align:left;padding:4px 6px;border:1px solid #cfd6e0}
table.st td{border:1px solid #cfd6e0;padding:5px 7px;vertical-align:top;break-inside:avoid}
table.st tr{break-inside:avoid}
table.st td.n{width:26px;text-align:center;font:800 14px Inter;color:#fff;background:var(--c)}
table.st td.tr{width:44%;color:#0f3d38}
table.st td.de{background:#fbfcfe}
.falle{background:#fdecea;border-left:4px solid #b42318;padding:4px 10px;margin:6px 0 2px;border-radius:0 6px 6px 0}
.satz{background:#eaf6ec;border-left:4px solid #2e7d32;padding:4px 10px;margin:6px 0 2px;border-radius:0 6px 6px 0}
.mini{width:100%;border-collapse:collapse;margin:4px 0}
.mini th{background:var(--c);color:#fff;font:700 11px Inter;padding:3px 6px;text-align:left}
.mini td{border:1px solid #cfd6e0;padding:3px 6px}
.toc{columns:2;column-gap:18px;font-size:12.5px}
.toc div{break-inside:avoid;padding:2px 0;border-bottom:1px dotted #ccc}
.toc b{display:inline-block;min-width:34px}
.sec{font:800 19px Inter;color:#fff;border-radius:8px;padding:7px 14px;margin:0 0 8px}
.small{font-size:11px;color:#555}
</style>'''

def card(no, title, color, erk, ne, steps, falle='', satz='', extra=''):
    h = f'<div class="card" style="--c:{color}"><div class="hd"><span class="no">{no}</span>{title}</div><div class="bd">'
    h += f'<div class="erk"><b>Sınavda böyle görünür:</b> {erk}</div>'
    h += f'<div class="ne"><b>Ne yapıyorum?</b> {ne}</div>'
    h += '<table class="st"><tr><th></th><th>Türkçe: bu adımda ne yapıyorum</th><th>Kâğıda / sınava yaz (örnek sayılarla)</th></tr>'
    for i, (tr, de) in enumerate(steps, 1):
        de = de.replace('\\(', '\\(\\displaystyle ')
        tr, de = (x.replace(' · ', ' &nbsp;<b>|</b>&nbsp; ') for x in (tr, de))
        h += f'<tr><td class="n">{i}</td><td class="tr">{tr}</td><td class="de">{de}</td></tr>'
    h += '</table>' + extra
    if satz: h += f'<div class="satz"><b>✎ Kopyala (cevap cümlesi):</b> {satz}</div>'
    if falle: h += f'<div class="falle"><b>⚠ Dikkat:</b> {falle}</div>'
    return h + '</div></div>'

def sec(title, color):
    return f'<div class="pb"></div><div class="sec" style="background:{color}">{title}</div>'

RED, BLUE, PURP, ORNG, TEAL, GRN, BRN = '#b42318', '#1f4e79', '#7030a0', '#c55a11', '#00796b', '#2e7d32', '#6d4c41'

# ======================= Titel + Inhalt
toc = [
 ('T1', 'Hipotez kurmak (H₀ / H₁)', '„Hypothesenpaar“, „absichern“, „nachweisen“'),
 ('T2', 'Gauß-Test (σ biliniyor)', '„σ bekannt“, „Varianz bekannt“'),
 ('T3', 't-Test (σ bilinmiyor) + ham veriden', '„Varianz unbekannt“, Daten gegeben'),
 ('T4', 'Oran testi (yaklaşık)', '„Anteil“, „Prozent“, n groß'),
 ('T5', 'Kesin Binom testi + İşaret testi', 'n klein, „Median“, „ohne Verteilungsannahme“'),
 ('T6', 'χ²-Varyans testi', '„Varianz / Streuung“ testen'),
 ('T7', 'χ²-Bağımsızlık + Uyum testi', 'Kreuztabelle, „unabhängig“, „fair“'),
 ('T8', 'R çıktısı: hangi kod, hangi karar?', 't.test(...), „p-value“'),
 ('T9', 'Fehler 1./2. Art + β hesabı', '„Fehler 2. Art“, „Güte“'),
 ('K1', 'Güven aralığı μ için', '„Konfidenzintervall für μ“'),
 ('K2', 'Güven aralığı oran/varyans, gereken n', '„Anteil“, „Varianz“, „wie groß muss n“'),
 ('S1', 'Tahminci yansız mı? (lineer)', '„erwartungstreu“, „unverzerrt“'),
 ('S2', 'Tahmincinin varyansı + hangisi iyi?', '„Var(T)“, „vorzuziehen“, „MSE“'),
 ('S3', 'Zor tahminci (kesir, çarpım)', '∏, Brüche, „Testen Sie, ob … unverzerrt“'),
 ('S4', 'Kerndichteschätzer', '„Kerndichteschätzer“, „Bandweite“'),
 ('D1', 'Yoğunlukta c bulmak', '„Bestimmen Sie c“'),
 ('D2', 'E(X) ve Var(X)', '„Erwartungswert“, „Varianz“'),
 ('D3', 'F(x), olasılık, medyan', '„Verteilungsfunktion“, „P(X > …)“'),
 ('D4', 'Parçalı yoğunluk / F verilmiş', 'zwei Formeln, „F(x) gegeben“'),
 ('D5', 'Diskret tablo: c, E, Var, F', 'Tabelle P(X = x)'),
 ('V1', 'Normal dağılım: olasılık + kantil', '„normalverteilt“, „Quantil“'),
 ('V2', 'Toplam, ortalama, ZGWS', '„Summe“, „Mittelwert“, n ≥ 30'),
 ('V3', 'Binom / Poisson / Hipergeometrik', '„Anzahl“, „im Mittel pro“, „ohne Zurücklegen“'),
 ('V4', 'Üstel ve Düzgün dağılım', '„Wartezeit“, „gleichverteilt“'),
 ('B1', 'BONUS: Bayes / ağaç (Altklausur A3)', '„Wahrscheinlichkeit, dass … gegeben …“'),
 ('B2', 'BONUS: Kümeler (Altklausur A4)', '„Mächtigkeit“, Ā, ∪, ∩'),
]
p0 = r'''<div class="kick">Kochbuch 2 · Adım Adım · Türkçe açıklamalı · her soru tipi bir tarif kartı</div>
<h1>Soruyu tanı → kartı aç → adımları sırayla yap.</h1>
<div class="ne" style="font-size:13.5px"><b>Nasıl kullanılır?</b><br>
<b>1.</b> Sorudaki Almanca kelimeye bak, aşağıdaki listeden kart numarasını bul (ör. „σ bekannt“ → <b>T2</b>).<br>
<b>2.</b> Kartta adımları <b>sırayla</b> yap. Sol sütun: Türkçe ne yaptığını anlatır. Sağ sütun: sınav kâğıdına <b>aynen</b> yazacağın Almanca satır – sadece sayıları kendi sorunla değiştir.<br>
<b>3.</b> Yeşil kutudaki cümleyi kopyala (puan oradan gelir), kırmızı kutudaki tuzağa düşme.</div>
<div class="toc">''' + ''.join(f'<div><b>{a}</b> {b} <span class="small">– {c}</span></div>' for a, b, c in toc) + r'''</div>
<div class="satz" style="margin-top:10px"><b>Altın kurallar (her soruda):</b> Her adımı yaz (sadece sonuç = puan kaybı) · Sonuç 3 ondalık, ara sonuç 4 ondalık · „Interpretieren / Begründen“ varsa mutlaka <b>bir cümle</b> · σ² verilmişse önce <b>kökünü al</b> · \(\log\) = \(\ln\) (hesap makinesinde <b>ln</b>).</div>
<div class="mini" style="margin-top:8px"></div>
<table class="mini" style="--c:#1f4e79"><tr><th>Kantil tablosu (ezberleme, buradan bak)</th><th>α = 10 %</th><th>α = 5 %</th><th>α = 1 %</th></tr>
<tr><td>iki taraflı (≠): \(z_{1-\alpha/2}\)</td><td>1.645</td><td><b>1.960</b></td><td>2.576</td></tr>
<tr><td>tek taraflı (&gt; veya &lt;): \(z_{1-\alpha}\)</td><td>1.282</td><td><b>1.645</b></td><td>2.326</td></tr>
<tr><td>χ² (sağ, 95 %): df = 1 / 2 / 3 / 4 / 5</td><td colspan="3">3.841 / 5.991 / 7.815 / 9.488 / 11.070</td></tr></table>
'''

# ======================= TESTS
T1 = card('T1', 'Hipotez kurmak – \\(H_0\\) ve \\(H_1\\)', RED,
 '„Stellen Sie das passende Hypothesenpaar auf“, „statistisch absichern“, „nachweisen“, „vermutet“, „bezweifelt“',
 'Metinde <b>kanıtlanmak istenen</b> şey \\(H_1\\)\'e gider. \\(H_0\\) onun tersidir ve eşittir işaretini (=, ≤, ≥) taşır.',
 [(r'Metinde „absichern / nachweisen / vermuten / bezweifeln“ kelimesinin yanındaki cümleyi bul. <b>Bu cümle \(H_1\)</b>.',
   r'Altklausur A8: „… absichern, dass Stahlbichler <u>nicht weiter als 133.5 m</u> springt“ → \(H_1\) bu.'),
  (r'Yönü kelimeden oku:<br>„größer, mehr, übersteigt, länger, weiter“ → \(\gt\)<br>„kleiner, weniger, nicht weiter als, kürzer, zu wenig“ → \(\lt\)<br>„genau, weicht ab, ungleich, in beide Richtungen, verändert“ → \(\neq\)',
   r'„nicht weiter als 133.5“ → \(\mu\lt133.5\)<br>„genau 10 Stunden … in beide Richtungen bezweifelt“ → \(\mu\neq10\)<br>„Verbraucher vermutet, es sind weniger als 500 g“ → \(\mu\lt500\)'),
  (r'\(H_0\) = tam tersi, <b>eşittir işareti hep \(H_0\)\'da</b>. \(\lt\) ise \(H_0\): \(\ge\) · \(\gt\) ise \(H_0\): \(\le\) · \(\neq\) ise \(H_0\): \(=\).',
   r'\(H_0:\ \mu\ge133.5\quad\text{vs.}\quad H_1:\ \mu\lt133.5\)<br>\(H_0:\ \mu=10\quad\text{vs.}\quad H_1:\ \mu\neq10\)<br>\(H_0:\ \mu\ge500\quad\text{vs.}\quad H_1:\ \mu\lt500\)'),
  (r'Parametreyi doğru seç: ortalama → \(\mu\), oran/yüzde → \(\pi\), varyans → \(\sigma^2\), medyan → \(x_{0.5}\).',
   r'„Anteil der Kunden über 30 %“ → \(H_0:\pi\le0.3\) vs. \(H_1:\pi\gt0.3\)')],
 falle=r'\(H_1\)\'de asla „=, ≤, ≥“ olmaz. Üreticinin iddiası („mindestens 500 g“) genelde \(H_0\)\'dır; şüphelenen kişinin iddiası \(H_1\)\'dir.')

T2 = card('T2', 'Gauß-Test – ortalama, σ <b>biliniyor</b>', RED,
 '„σ = 4 bekannt“, „Varianz σ² = 16 bekannt“, „normalverteilt“, „Prüfgröße“, „Testentscheidung“, „p-Wert“',
 'Örnek ortalamasının \\(\\mu_0\\)\'dan kaç standart hata uzak olduğunu hesapla (\\(z\\)), tablodaki kritik değerle karşılaştır.',
 [(r'Verileri topla: \(\bar x\), \(\mu_0\) (hipotezdeki sayı), \(\sigma\), \(n\), \(\alpha\). <b>σ² verildiyse kökünü al!</b>',
   r'Beispiel: \(\bar x=52,\ \mu_0=50,\ \sigma=4,\ n=16,\ \alpha=0.05\), „weicht ab“'),
  (r'Hipotezi yaz (Kart T1).', r'\(H_0:\ \mu=50\quad\text{vs.}\quad H_1:\ \mu\neq50\)'),
  (r'Test istatistiğini hesapla: önce payda \(\sigma/\sqrt n\), sonra bölme. Dağılımını yaz – bu ayrı puan!',
   r'\(Z=\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}=\dfrac{52-50}{4/\sqrt{16}}=\dfrac21=2\)<br>Unter \(H_0\) gilt: \(Z\sim N(0,1)\).'),
  (r'Kritik değeri seç (sayfa 1 tablosu):<br>\(\neq\) → \(z_{1-\alpha/2}\) (5 %: 1.96)<br>\(\gt\) → \(z_{1-\alpha}\) (5 %: 1.645)<br>\(\lt\) → \(-z_{1-\alpha}\) (5 %: −1.645)',
   r'Ablehnungsbereich: \(|z|\gt z_{0.975}=1.96\)'),
  (r'Karşılaştır:<br>\(\neq\): \(|z|\) kritikten büyükse ret<br>\(\gt\): \(z\) kritikten büyükse ret<br>\(\lt\): \(z\) negatif kritikten küçükse ret',
   r'Da \(|z|=2\gt1.96\), wird \(H_0\) abgelehnt.'),
  (r'Bağlamla cümle kur (yeşil kutu).', r'Zum Niveau 5 % ist nachgewiesen, dass die mittlere Füllmenge von 50 ml abweicht.'),
  (r'p-değeri istenirse: \(\neq\): \(2(1-\Phi(|z|))\) · \(\gt\): \(1-\Phi(z)\) · \(\lt\): \(\Phi(z)\). <b>\(p\le\alpha\) → ret.</b>',
   r'\(p=2\,(1-\Phi(2))=2\,(1-0.9772)=0.0456\lt0.05\Rightarrow H_0\) ablehnen.')],
 satz=r'„Da \(|z|=\dots\gt\dots\), wird \(H_0\) zum Niveau \(\alpha=\dots\) abgelehnt. Es ist statistisch nachgewiesen, dass …“ — reddedilmezse: „\(H_0\) kann nicht abgelehnt werden; es kann nicht nachgewiesen werden, dass …“',
 falle=r'\(\sigma/\sqrt n\) – \(\sigma/n\) değil, \(\sigma^2\) değil. „\(H_0\) angenommen / bewiesen“ yazma → „nicht abgelehnt“. Sol taraflı testte \(z\) negatif, işareti koru.')

T3 = card('T3', 't-Test – ortalama, σ <b>bilinmiyor</b> (ham veriden de)', RED,
 '„Varianz unbekannt“, nur \\(s\\) oder \\(s_*\\) gegeben, Rohdaten \\(x_1,\\dots,x_n\\), „\\(t_{n-1;\\dots}\\)“ im Hinweis',
 'T2 ile aynı, sadece σ yerine \\(s_*\\) (düzeltilmiş std. sapma) ve normal tablo yerine \\(t_{n-1}\\) kantili.',
 [(r'Ham veri varsa: \(\bar x\) hesapla.', r'Daten \(12,15,11,14,13\): \(\bar x=\frac{65}{5}=13\)'),
  (r'\(s_*^2\) hesapla: sapmaların karesinin toplamı / \((n-1)\). Sadece empirik \(s^2\) verildiyse: \(s_*^2=\frac{n}{n-1}s^2\).',
   r'\(s_*^2=\frac{1}{4}\big((12-13)^2+(15-13)^2+\dots\big)=\frac{1+4+4+1+0}{4}=2.5\), \(s_*=1.581\)'),
  (r'Hipotez (T1).', r'\(H_0:\mu=12\) vs. \(H_1:\mu\neq12\)'),
  (r'Test istatistiği ve dağılımı (serbestlik derecesi \(n-1\)!).',
   r'\(T=\dfrac{\bar X-\mu_0}{S_*/\sqrt n}=\dfrac{13-12}{1.581/\sqrt5}=1.414\); unter \(H_0\): \(T\sim t_{4}\)'),
  (r'Kritik değer soruda verilir (Hinweis). \(\neq\): \(t_{n-1;1-\alpha/2}\), tek taraflı: \(t_{n-1;1-\alpha}\).',
   r'\(t_{4;0.975}=2.776\); \(|t|=1.414\lt2.776\Rightarrow H_0\) nicht ablehnen.')],
 satz=r'„\(H_0\) kann zum Niveau 5 % nicht abgelehnt werden. Es kann nicht nachgewiesen werden, dass der Mittelwert von 12 abweicht.“',
 falle=r'Paydada \(n-1\) (\(s_*\)) kullan, \(n\) değil. Serbestlik derecesi \(df=n-1\).')

T4 = card('T4', 'Oran testi (yaklaşık binom testi)', RED,
 '„Anteil“, „Prozent der …“, „Erfolgsquote“, n groß (z. B. 100)',
 'Gözlenen oran \\(\\hat\\pi\\), hipotezdeki oran \\(\\pi_0\\)\'dan anlamlı farklı mı? Gauß testinin aynısı, sadece standart hata farklı.',
 [(r'\(\hat\pi=\frac{\text{başarı sayısı}}{n}\) hesapla.', r'60 von 100: \(\hat\pi=0.6\); \(\pi_0=0.5\), „weicht ab“'),
  (r'Hipotez.', r'\(H_0:\pi=0.5\) vs. \(H_1:\pi\neq0.5\)'),
  (r'Test istatistiği – paydada \(\pi_0\) (hipotezdeki sayı)!',
   r'\(Z=\dfrac{\hat\pi-\pi_0}{\sqrt{\pi_0(1-\pi_0)/n}}=\dfrac{0.6-0.5}{\sqrt{0.25/100}}=\dfrac{0.1}{0.05}=2\), \(Z\overset{a}{\sim}N(0,1)\)'),
  (r'Kritik değer + karar + cümle: T2 adım 4–6 ile aynı.', r'\(|z|=2\gt1.96\Rightarrow H_0\) ablehnen.')],
 falle=r'Testte paydada \(\pi_0\), güven aralığında (K2) \(\hat\pi\) var – karıştırma.')

T5 = card('T5', 'Kesin binom testi ve işaret testi (Vorzeichentest)', RED,
 'kleines n (z. B. 10), „exakt“, „Median“, „ohne Verteilungsannahme“',
 'Başarı sayısı \\(X\\) \\(H_0\\) altında \\(B(n,\\pi_0)\\). p-değerini binom olasılıklarıyla doğrudan hesapla ve α ile karşılaştır.',
 [(r'\(X\) = başarı sayısı. İşaret testinde: \(Z\) = \(\theta_0\)\'a <b>eşit veya küçük</b> gözlem sayısı, \(\pi_0=0.5\).',
   r'\(n=10\), 9 Erfolge, \(H_1:\pi\gt0.5\) → unter \(H_0\): \(X\sim B(10;0.5)\)'),
  (r'p-değeri: sağ \(P(X\ge x)\) · sol \(P(X\le x)\) · iki taraflı \(2\cdot\) küçük taraf. Binom formülü: \(\binom nk\pi^k(1-\pi)^{n-k}\).',
   r'\(p=P(X\ge9)=P(9)+P(10)=\frac{10+1}{1024}=0.0107\)'),
  (r'Karar: \(p\le\alpha\) → ret.', r'\(0.0107\le0.05\Rightarrow H_0\) ablehnen.'),
  (r'Ret bölgesi istenirse: \(P(X\ge k)\le\alpha\) olan en küçük \(k\)\'yı ara.',
   r'\(P(X\ge9)=0.0107\le0.05\), \(P(X\ge8)=0.0547\gt0.05\Rightarrow\) Ablehnungsbereich \(\{9,10\}\)')],
 falle=r'\(P(X\ge k)=1-P(X\le k-1)\) – \(1-P(X\le k)\) değil!')

T6 = card('T6', 'χ²-Varyans testi', RED,
 '„Streuung zu groß“, „Varianz größer als …“, normalverteilt',
 'Örnek varyansını hipotezdeki varyansla oranla; χ² tablosuyla karşılaştır.',
 [(r'Hipotez (\(\sigma^2\) ile).', r'\(H_0:\sigma^2\le4\) vs. \(H_1:\sigma^2\gt4\); \(n=10\), \(s_*^2=8\)'),
  (r'Test istatistiği ve dağılımı.', r'\(\chi^2=\dfrac{(n-1)s_*^2}{\sigma_0^2}=\dfrac{9\cdot8}{4}=18\); unter \(H_0\): \(\chi^2\sim\chi^2_{9}\)'),
  (r'Kritik değer: sağ \(\chi^2_{n-1;1-\alpha}\) · sol \(\chi^2_{n-1;\alpha}\) · iki taraflı: iki ayrı sınır \(\chi^2_{n-1;\alpha/2}\) ve \(\chi^2_{n-1;1-\alpha/2}\).',
   r'\(\chi^2_{9;0.95}=16.919\); \(18\gt16.919\Rightarrow H_0\) ablehnen.')],
 falle=r'χ² simetrik değil – iki taraflıda alt ve üst sınırı ayrı ayrı tablodan al.')

T7 = card('T7', 'χ²-Bağımsızlık testi ve uyum testi', RED,
 'Kreuztabelle, „Sind die Merkmale unabhängig?“, „Ist der Würfel fair?“, „passt die Verteilung?“',
 'Gözlenen sayılar (\\(h\\)) ile \\(H_0\\) doğruysa beklenen sayılar (\\(e\\)) ne kadar farklı? Fark büyükse ret.',
 [(r'Hipotez yaz.', r'\(H_0\): Geschlecht und Antwort sind unabhängig vs. \(H_1\): abhängig'),
  (r'Beklenen sayılar. Bağımsızlık: \(e=\frac{\text{satır toplamı}\cdot\text{sütun toplamı}}{n}\). Uyum: \(e_j=n\cdot p_j\).',
   r'Männer ja 30 / nein 20, Frauen ja 20 / nein 30: \(e=\frac{50\cdot50}{100}=25\) (jede Zelle)'),
  (r'Her hücre için \(\frac{(h-e)^2}{e}\), hepsini topla.', r'\(\chi^2=\frac{(30-25)^2}{25}+\frac{(20-25)^2}{25}+\frac{(20-25)^2}{25}+\frac{(30-25)^2}{25}=4\)'),
  (r'Serbestlik: bağımsızlık \((k-1)(m-1)\), uyum \(k-1\). Kritik \(\chi^2_{df;1-\alpha}\) (hep sağ).',
   r'\(df=1\), \(\chi^2_{1;0.95}=3.841\); \(4\gt3.841\Rightarrow H_0\) ablehnen.')],
 satz=r'„Zum Niveau 5 % wird \(H_0\) abgelehnt; es besteht ein Zusammenhang zwischen Geschlecht und Antwort.“',
 falle=r'Uyum örneği (zar, 60 atış, gözlenen 5, 8, 9, 8, 10, 20): \(e_j=10\), \(\chi^2=\frac{25+4+1+4+0+100}{10}=13.4\gt\chi^2_{5;0.95}=11.07\) → zar adil değil.')

T8 = card('T8', 'R çıktısı: hangi kod doğru, karar ne? (Altklausur A8c)', RED,
 'mehrere <code>t.test(…)</code>-Codes, „Geben Sie die Nummer des R-Codes an“, „Treffen Sie anhand des R-Codes eine Testentscheidung“',
 'Doğru kodu 3 kontrolle bul (doğru veri, doğru mu, doğru alternative), sonra sadece <b>p-value</b> ile α\'yı karşılaştır.',
 [(r'Doğru veri mi? Hangi kişi/grup test ediliyor?', r'Test über Stahlbichler → <code>x &lt;- c(130, 134, 129.5, 132.5)</code> → Code (2) oder (3)'),
  (r'<code>mu=</code> hipotezdeki \(\mu_0\) mı?', r'<code>mu=133.5</code> ✓'),
  (r'<code>alternative</code> \(H_1\)\'e uyuyor mu? <code>"less"/"l"</code> ↔ \(\lt\) · <code>"greater"/"g"</code> ↔ \(\gt\) · <code>"two.sided"</code> (veya yok) ↔ \(\neq\)',
   r'\(H_1:\mu\lt133.5\) → <code>"l"</code> → <b>Code (2)</b>'),
  (r'Karar: p-value ≤ α → \(H_0\) ret.', r'\(p=0.07791\lt\alpha=0.1\Rightarrow H_0\) wird abgelehnt.')],
 satz=r'„Ich wähle Code (2), da die Daten von Stahlbichler verwendet werden und \(H_1:\mu\lt133.5\) linksseitig ist. Da \(p=0.078\lt0.1\), wird \(H_0\) abgelehnt: Zum Niveau 10 % springt Stahlbichler im Mittel nicht weiter als 133.5 m.“',
 falle=r'<code>conf.level=0.9</code> ↔ \(\alpha=0.1\). <code>t = ?</code> bilmen gerekmez – karar sadece p-değerinden.')

T9 = card('T9', 'Fehler 1./2. Art ve β (Güte) hesabı', RED,
 '„Beschreiben Sie den Fehler 1./2. Art im Sachzusammenhang“, „Wahrscheinlichkeit für einen Fehler 2. Art, wenn μ = …“',
 '1. tür hata = haksız yere reddetmek (olasılık α). 2. tür hata = reddetmemiz gerekirken reddetmemek (olasılık β).',
 [(r'Tanımları bağlama göre yaz.',
   r'<b>Fehler 1. Art:</b> \(H_0\) wird abgelehnt, obwohl \(H_0\) wahr ist. Hier: Wir schließen, dass die Füllmenge von 50 ml abweicht, obwohl sie in Wahrheit 50 ml beträgt.<br><b>Fehler 2. Art:</b> \(H_0\) wird nicht abgelehnt, obwohl \(H_1\) wahr ist.'),
  (r'β hesabı – önce ret bölgesini \(\bar x\) cinsinden yaz: \(\mu_0+z\cdot\sigma/\sqrt n\).',
   r'\(H_0:\mu\le50\), \(\sigma=4\), \(n=16\), α = 5 %: ablehnen, wenn \(\bar x\gt50+1.645\cdot1=51.645\)'),
  (r'Gerçek μ (soruda verilen) ile, ret bölgesine <b>düşmeme</b> olasılığı = β.',
   r'wahres \(\mu=53\): \(\beta=P(\bar X\le51.645)=\Phi\big(\frac{51.645-53}{1}\big)=\Phi(-1.36)=0.087\)'),
  (r'Güç (Güte) = \(1-\beta\).', r'Güte \(=1-0.087=0.913\)')],
 falle=r'Ret edildiyse sadece 1. tür hata mümkün; reddedilmediyse sadece 2. tür hata mümkün. α küçülürse β büyür.')

# ======================= KI
K1 = card('K1', 'Güven aralığı (Konfidenzintervall) μ için', PURP,
 '„Bestimmen Sie ein 95 %-Konfidenzintervall für μ“, „Interpretieren Sie das KI“',
 'Ortalama ± (kantil × standart hata). σ biliniyorsa \\(z\\), bilinmiyorsa \\(t_{n-1}\\).',
 [(r'Seviye → kantil: \(1-\alpha=0.95\) → \(z_{0.975}=1.96\) (σ biliniyor) veya \(t_{n-1;0.975}\) (bilinmiyor).',
   r'\(1-\alpha=0.95\Rightarrow z_{1-\alpha/2}=z_{0.975}=1.96\)'),
  (r'Standart hata: \(\sigma/\sqrt n\) (veya \(s_*/\sqrt n\)).', r'\(\sigma/\sqrt n=4/\sqrt{16}=1\)'),
  (r'Yarı genişlik \(e\) = kantil × standart hata.', r'\(e=1.96\cdot1=1.96\)'),
  (r'Sınırlar: \(\bar x-e\) ve \(\bar x+e\).', r'\(\big[\bar x-z_{0.975}\frac{\sigma}{\sqrt n};\ \bar x+z_{0.975}\frac{\sigma}{\sqrt n}\big]=[52-1.96;\ 52+1.96]=[50.04;\ 53.96]\)'),
  (r'σ bilinmiyorsa aynı adımlar \(t\) ile.', r'\(\bar x=32,\ s_*=4,\ n=16\): \(32\pm t_{15;0.975}\cdot\frac44=32\pm2.131=[29.869;\ 34.131]\)')],
 satz=r'„Bei wiederholter Stichprobenziehung überdecken etwa 95 % der so konstruierten Intervalle den wahren Mittelwert μ.“',
 falle=r'YANLIŞ: „μ liegt mit 95 % Wahrscheinlichkeit im Intervall“ (μ sabit). Seviye ↑ → aralık genişler; n ↑ → daralır. İki taraflı test ret ⇔ \(\mu_0\) aralığın dışında.')

K2 = card('K2', 'Güven aralığı oran ve varyans için + gereken n', PURP,
 '„KI für den Anteil“, „KI für die Varianz“, „Wie groß muss n mindestens sein, damit …“',
 'Oran: \\(\\hat\\pi\\) ± \\(z\\)·\\(\\sqrt{\\hat\\pi(1-\\hat\\pi)/n}\\). Varyans: χ² kantilleriyle. Gereken n: genişlik formülünü n için çöz, yukarı yuvarla.',
 [(r'<b>Oran:</b> \(\hat\pi\) hesapla, standart hatayı \(\hat\pi\) ile kur.',
   r'\(\hat\pi=0.6,\ n=100\): \(0.6\pm1.96\sqrt{\frac{0.6\cdot0.4}{100}}=0.6\pm0.096=[0.504;\ 0.696]\)'),
  (r'<b>Varyans:</b> pay \((n-1)s_*^2\); <b>büyük</b> kantil <b>alt</b> sınıra gider.',
   r'\(n=10,\ s_*^2=8\): \(\Big[\frac{72}{\chi^2_{9;0.975}};\frac{72}{\chi^2_{9;0.025}}\Big]=\Big[\frac{72}{19.023};\frac{72}{2.700}\Big]=[3.785;\ 26.663]\)'),
  (r'<b>Gereken n (ortalama):</b> \(e=z\frac{\sigma}{\sqrt n}\) → \(n\ge\big(\frac{z\sigma}{e}\big)^2\). Uzunluk \(L=2e\) verilirse önce \(e=L/2\).',
   r'\(\sigma=4,\ e=1\), 95 %: \(n\ge(1.96\cdot4)^2=61.47\Rightarrow n=62\)'),
  (r'<b>Gereken n (oran):</b> \(n\ge\frac{z^2\pi(1-\pi)}{e^2}\); bilgi yoksa \(\pi=0.5\).',
   r'\(e=0.03\): \(n\ge\frac{1.96^2\cdot0.25}{0.0009}=1067.1\Rightarrow n=1068\)'),
  (r'<b>Geriye:</b> aralık \([a;b]\) verilmişse \(\bar x=\frac{a+b}2\), \(e=\frac{b-a}2\). R kodundan: <code>qnorm(0.995)</code> → 99 %.',
   r'<code>3 + c(-1,1)*qnorm(0.995)*2/sqrt(100)</code> → \(\bar x=3\), 99 %, \(\sigma=2\), \(n=100\)')],
 falle=r'n her zaman <b>yukarı</b> yuvarlanır (61.47 → 62). σ için aralık: varyans aralığının iki sınırının karekökü.')

# ======================= Schätzer
S1 = card('S1', 'Tahminci yansız mı? (erwartungstreu / unverzerrt)', ORNG,
 '„Zeigen Sie, dass … erwartungstreu ist“, „Ist T ein unverzerrter Schätzer für μ?“, „Bias“',
 '\\(E(T)\\) hesapla. Parametreye eşitse yansız, değilse \\(\\text{Bias}=E(T)-\\theta\\).',
 [(r'Beklentiyi her terime dağıt, sabitleri dışarı al: \(E(aX_1+bX_2)=aE(X_1)+bE(X_2)\).',
   r'\(E(T_1)=E(0.5X_1+0.3X_2+0.2X_3)=0.5E(X_1)+0.3E(X_2)+0.2E(X_3)\)'),
  (r'Her \(E(X_i)\) yerine soruda verilen değeri koy (\(\mu\), \(\frac\alpha4\), \(\frac\theta2\) …).',
   r'\(=0.5\mu+0.3\mu+0.2\mu=(0.5+0.3+0.2)\mu=\mu\)'),
  (r'Parametreyle karşılaştır. <b>Kısa yol:</b> katsayıların toplamı 1 ise μ için yansız.',
   r'\(E(T_1)=\mu\Rightarrow T_1\) ist erwartungstreu. &nbsp; \(E(X_1-X_2+X_3)=\mu-\mu+\mu=\mu\) ✓'),
  (r'Yansız değilse sapmayı yaz.', r'\(T=\frac14(X_1+X_2+X_3)\): \(E(T)=\frac34\mu\neq\mu\); \(\text{Bias}=\frac34\mu-\mu=-\frac14\mu\)'),
  (r'\(E(X)=\frac\theta2\) gibi bir şey verilmişse: tahminciyi buna göre düzelt.', r'\(E(2\bar X)=2\cdot\frac\theta2=\theta\Rightarrow2\bar X\) ist erwartungstreu für θ.')],
 satz=r'„Da \(E(T)=\mu\) für alle μ gilt, ist T ein erwartungstreuer (unverzerrter) Schätzer für μ.“')

S2 = card('S2', 'Tahmincinin varyansı – hangisi daha iyi?', ORNG,
 '„Berechnen Sie Var(T₁) und Var(T₂)“, „Welcher Schätzer ist vorzuziehen?“, „Ist X̄ noch besser?“, „MSE“, „konsistent“',
 'Varyansta katsayıların <b>karesi</b> alınır. İkisi de yansızsa varyansı küçük olan daha iyi.',
 [(r'Varyans kuralı (bağımsız \(X_i\)): \(Var(aX_1+bX_2)=a^2\sigma^2+b^2\sigma^2\). Eksi işaret kareyle kaybolur!',
   r'\(Var(T_1)=0.5^2\sigma^2+0.3^2\sigma^2+0.2^2\sigma^2=(0.25+0.09+0.04)\sigma^2=0.38\sigma^2\)'),
  (r'İkinci tahminci için aynı.', r'\(Var(T_2)=1^2\sigma^2+(-1)^2\sigma^2+1^2\sigma^2=3\sigma^2\)'),
  (r'Karşılaştır (ikisi de yansızsa).', r'Da beide erwartungstreu und \(0.38\sigma^2\lt3\sigma^2\), ist \(T_1\) vorzuziehen.'),
  (r'\(\bar X\) ile karşılaştır: \(Var(\bar X)=\frac{\sigma^2}{n}\).', r'\(Var(\bar X)=\frac{\sigma^2}{3}\approx0.333\sigma^2\lt0.38\sigma^2\Rightarrow\bar X\) ist noch besser.'),
  (r'Biri yanlıysa MSE kullan: \(MSE=Var+\text{Bias}^2\), küçük olan iyi.', r'A: Bias 0, Var 4 → MSE 4 · B: Bias 1, Var 2 → MSE 3 → B besser.'),
  (r'Konsistenz: \(n\to\infty\) iken MSE → 0 mı?', r'\(Var(\bar X)=\frac{\sigma^2}n\to0\) → konsistent · \(Var(X_1)=\sigma^2\) → nicht konsistent')],
 falle=r'Varyansta katsayıyı karele, toplamda topla. \(Var(X_1-X_2)=2\sigma^2\) (eksi değil artı!).')

S3 = card('S3', 'Zor tahminci: kesir, çarpım (Altklausur A7)', ORNG,
 '„Testen Sie, ob der Schätzer \\(\\hat\\alpha=\\frac{\\prod_{i=2}^{n-1}X_i}{\\prod_{i=1}^{n-1}X_i}+\\frac{X_n}{\\alpha}-\\frac14\\) ein unverzerrter Schätzer für α ist“, \\(E(X)=\\frac\\alpha4\\)',
 'Önce sadeleştir (kesirde aynı \\(X\\)\'ler sadeleşir), sonra S1 gibi beklentiyi terim terim al.',
 [(r'Çarpımları aç: pay \(X_2\cdots X_{n-1}\), payda \(X_1X_2\cdots X_{n-1}\). Ortaklar sadeleşir.',
   r'\(\dfrac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}=\dfrac{X_2\cdots X_{n-1}}{X_1\cdot X_2\cdots X_{n-1}}=\dfrac1{X_1}\)'),
  (r'Beklentiyi her terime dağıt; α sabit → dışarı.',
   r'\(E(\hat\alpha)=E\Big(\frac1{X_1}\Big)+\frac{E(X_n)}{\alpha}-\frac14\)'),
  (r'Verileni yerine koy: \(E(X_n)=\frac\alpha4\). Resmî çözümde \(E(\frac1{X_1})=\frac1{E(X_1)}=\frac4\alpha\) alınıyor.',
   r'\(=\frac{4}{\alpha}+\frac{\alpha/4}{\alpha}-\frac14=\frac4\alpha+\frac14-\frac14=\frac4\alpha\)'),
  (r'Karşılaştır.', r'\(E(\hat\alpha)=\frac4\alpha\neq\alpha\Rightarrow\hat\alpha\) ist <b>verzerrt</b> (nicht erwartungstreu).'),
  (r'Çarpım kuralı (bağımsız): \(E(X_1X_2)=E(X_1)E(X_2)\). Kare: \(E(X^2)=Var(X)+E(X)^2\).',
   r'\(E(X_1X_2)=\frac\alpha4\cdot\frac\alpha4=\frac{\alpha^2}{16}\)')],
 falle=r'Aslında matematikte \(E(1/X)\neq1/E(X)\) – ama resmî çözüm böyle hesaplıyor; sonuç her iki yolda da „verzerrt“. Sadeleştirme adımını mutlaka yaz.')

S4 = card('S4', 'Kerndichteschätzer (bir noktada)', ORNG,
 '„Berechnen Sie den Kerndichteschätzer an der Stelle x = … mit Rechteckkern/Epanechnikov-Kern und Bandweite b“',
 'Her gözlem için \\(u=(x-x_i)/b\\), çekirdek değerini bul, topla, \\(n\\cdot b\\)\'ye böl.',
 [(r'Her \(x_i\) için \(u_i=\frac{x-x_i}{b}\).', r'Daten \(1,\,2,\,2.5,\,4\); \(x=2\); \(b=1\): \(u=1,\ 0,\ -0.5,\ -2\)'),
  (r'Sadece \(-1\le u\lt1\) olanlar sayılır (\(u=1\) sayılmaz!). Çekirdek: dikdörtgen \(\frac12\), Epanechnikov \(\frac34(1-u^2)\).',
   r'Rechteck: \(K=0,\ 0.5,\ 0.5,\ 0\) · Epanechnikov: \(0,\ 0.75,\ 0.5625,\ 0\)'),
  (r'Topla ve \(n\cdot b\)\'ye böl.', r'Rechteck: \(\hat f(2)=\frac{1}{4\cdot1}(0.5+0.5)=0.25\) · Epanechnikov: \(\frac{0.75+0.5625}{4}=0.328\)')],
 satz=r'„Größere Bandweite → glattere Schätzung (Approximationsfehler ↑, Schätzfehler ↓); kleinere Bandweite → zackiger.“')

# ======================= Dichte
D1 = card('D1', 'Yoğunlukta c bulmak', TEAL,
 '„Bestimmen Sie c derart, dass f eine gültige Dichtefunktion ist“',
 'Yoğunluğun altındaki toplam alan 1 olmalı: \\(\\int f(x)\\,dx=1\\) → c\'yi çöz.',
 [(r'İntegrali taşıyıcı üzerinde kur (sınırlar \(f\)\'nin tanımından).', r'\(\displaystyle\int_0^2 c\,(2-x)\,dx\overset{!}{=}1\)'),
  (r'c\'yi dışarı al, parantezi aç, her terimin integralini al: \(\int x^k=\frac{x^{k+1}}{k+1}\).', r'\(c\Big[2x-\frac{x^2}{2}\Big]_0^2\)'),
  (r'Sınırları yerleştir: üst − alt.', r'\(=c\,\big((4-2)-(0-0)\big)=2c\)'),
  (r'\(=1\) koy, c\'yi çöz.', r'\(2c=1\Rightarrow c=\frac12\)'),
  (r'İkinci şart: \(f(x)\ge0\) kontrol et (bir cümle).', r'Außerdem ist \(f(x)\ge0\) für alle \(x\), also ist f eine Dichte.')],
 falle=r'Diskret tabloda integral yok: olasılıkların toplamı = 1 (Kart D5). \(e^{-\lambda x}\) içeren yoğunlukta: \(\int_0^\infty x^ke^{-\lambda x}dx=\frac{k!}{\lambda^{k+1}}\) (örn. \(f=c\,x\,e^{-2x}\): \(c\cdot\frac14=1\Rightarrow c=4\)).')

D2 = card('D2', 'Beklenen değer E(X) ve varyans Var(X)', TEAL,
 '„Berechnen Sie den Erwartungswert E(X)“, „Berechnen Sie Var(X)“',
 '\\(E(X)=\\int x\\,f(x)\\,dx\\). Varyans için önce \\(E(X^2)=\\int x^2 f(x)\\,dx\\), sonra \\(Var=E(X^2)-E(X)^2\\).',
 [(r'\(f\)\'yi \(x\) ile çarp, parantezi aç.', r'\(x\cdot\frac12(2-x)=x-\frac{x^2}{2}\)'),
  (r'İntegral al, sınırları yerleştir.', r'\(E(X)=\int_0^2\Big(x-\frac{x^2}{2}\Big)dx=\Big[\frac{x^2}{2}-\frac{x^3}{6}\Big]_0^2=2-\frac86=\frac23\)'),
  (r'\(E(X^2)\): \(f\)\'yi \(x^2\) ile çarp ve aynı.', r'\(E(X^2)=\int_0^2\Big(x^2-\frac{x^3}{2}\Big)dx=\Big[\frac{x^3}{3}-\frac{x^4}{8}\Big]_0^2=\frac83-2=\frac23\)'),
  (r'Varyans formülü.', r'\(Var(X)=E(X^2)-E(X)^2=\frac23-\frac49=\frac29\approx0.222\)'),
  (r'Dönüşüm sorulursa: \(E(aX+b)=aE(X)+b\), \(Var(aX+b)=a^2Var(X)\).', r'\(E(3X+1)=3\cdot\frac23+1=3\), \(Var(3X+1)=9\cdot\frac29=2\)')],
 falle=r'Kesirlerle git, en sonda ondalığa çevir (yuvarlanmış \(E(X)\)\'in karesi hatalı sonuç verir). Varyans asla negatif olmaz.')

D3 = card('D3', 'Dağılım fonksiyonu F(x), olasılıklar, medyan', TEAL,
 '„Bestimmen Sie die Verteilungsfunktion F(x) (mit Fallunterscheidung)“, „Berechnen Sie P(X > 1)“, „Median“',
 '\\(F(x)=\\int_{\\text{alt}}^{x}f(t)\\,dt\\) – üst sınır \\(x\\). Sonra 3 durum yaz. Olasılıklar \\(F\\)\'den okunur.',
 [(r'Alt sınırdan \(x\)\'e kadar integral (değişkeni \(t\) yap).', r'\(\displaystyle\int_0^x\tfrac12(2-t)\,dt=\tfrac12\Big[2t-\tfrac{t^2}{2}\Big]_0^x=x-\frac{x^2}{4}\)'),
  (r'<b>3 durum</b> yaz: taşıyıcının solunda 0, içinde formül, sağında 1.',
   r'\(F(x)=\begin{cases}0,&x\lt0\\ x-\frac{x^2}4,&0\le x\le2\\1,&x\gt2\end{cases}\)'),
  (r'Olasılık: \(P(X\le a)=F(a)\) · \(P(X\gt a)=1-F(a)\) · \(P(a\lt X\le b)=F(b)-F(a)\).',
   r'\(P(X\gt1)=1-F(1)=1-\frac34=\frac14\) · \(P(0.5\le X\le1)=\frac34-\frac7{16}=\frac5{16}\)'),
  (r'Medyan / p-kantil: \(F(x)=0.5\) (veya \(p\)) koy, \(x\)\'i çöz; taşıyıcıdaki çözümü al.',
   r'\(x-\frac{x^2}4=\frac12\Leftrightarrow x^2-4x+2=0\Rightarrow x=2-\sqrt2=0.586\)')],
 falle=r'Fallunterscheidung olmadan F(x) eksik sayılır. Sürekli değişkende \(P(X=a)=0\), yani \(P(X\lt a)=P(X\le a)\). Kontrol: \(F\)(üst sınır) = 1 olmalı.')

D4 = card('D4', 'Parçalı yoğunluk · F verilmiş · „f bir yoğunluk mu?“', TEAL,
 'f mit zwei Formeln, „F(x) ist gegeben“, „Ist f eine Dichtefunktion? Begründen Sie“',
 'Parçalıda integrali kırılma noktasında böl. F verilmişse türev al. Yoğunluk kontrolü: \\(f\\ge0\\) ve integral 1.',
 [(r'<b>Parçalı:</b> her parçanın integralini ayrı al, topla.', r'\(f=x\) auf \([0,1]\), \(2-x\) auf \((1,2]\): \(\int_0^1x\,dx+\int_1^2(2-x)\,dx=\frac12+\frac12=1\) ✓'),
  (r'E(X) de aynı şekilde iki parça.', r'\(E(X)=\int_0^1x^2dx+\int_1^2x(2-x)dx=\frac13+\frac23=1\)'),
  (r'F(x): ikinci parçada önceki parçanın toplamı (\(F(1)\)) + yeni integral.', r'\(F(x)=\frac{x^2}2\) für \(0\le x\le1\); \(F(x)=1-\frac{(2-x)^2}{2}\) für \(1\lt x\le2\)'),
  (r'<b>F verilmiş:</b> \(f=F\,\'\) (türev al). Medyan: \(F(x)=0.5\).', r'\(F=\frac{x^3}{8}\) auf \([0,2]\): \(f=\frac{3x^2}{8}\); Median \(x=\sqrt[3]{4}=1.587\)'),
  (r'<b>Yoğunluk mu?</b> Bir yerde negatifse veya integral ≠ 1 ise hayır.', r'\(f=x-0.5\) auf \([0,2]\): \(\int=1\), aber \(f(0)=-0.5\lt0\Rightarrow\) keine Dichte.')],
 falle=r'Simetrik yoğunlukta (üçgen gibi) \(E(X)\) = medyan = simetri merkezi – hesaplamadan söyleyebilirsin.')

D5 = card('D5', 'Diskret tablo: c, E, Var, F(x) (basamak)', TEAL,
 'Tabelle mit \\(x\\) und \\(P(X=x)\\), „Träger“, „Wahrscheinlichkeitsfunktion“, „Verteilungsfunktion“',
 'İntegral yerine <b>toplam</b>. F(x) bir merdiven: her \\(x\\) değerinde \\(P(X=x)\\) kadar zıplar.',
 [(r'c: olasılıkların toplamı 1.', r'\(x\): 0, 1, 2, 3 mit \(0.1,\ 0.3,\ c,\ 0.2\): \(0.6+c=1\Rightarrow c=0.4\)'),
  (r'E(X): her \(x\) × olasılığı, topla.', r'\(E(X)=0\cdot0.1+1\cdot0.3+2\cdot0.4+3\cdot0.2=1.7\)'),
  (r'E(X²) ve Var.', r'\(E(X^2)=0+0.3+1.6+1.8=3.7\); \(Var=3.7-1.7^2=0.81\)'),
  (r'F(x): kümülatif toplamlar, aralıklar „\(\le x\lt\)“ şeklinde.', r'\(F(x)=\begin{cases}0,&x\lt0\\0.1,&0\le x\lt1\\0.4,&1\le x\lt2\\0.8,&2\le x\lt3\\1,&x\ge3\end{cases}\)'),
  (r'Olasılık: \(P(X\ge2)=1-F(1)\).', r'\(P(X\ge2)=1-0.4=0.6\)'),
  (r'İki değişken tablosu: marjinal = satır/sütun toplamı; \(Cov=E(XY)-E(X)E(Y)\); bağımsız ⇔ her hücre = marjinallerin çarpımı.',
   r'\(P(1,1)=0.4\), \(P(X=1)P(Y=1)=0.5\cdot0.6=0.3\neq0.4\Rightarrow\) abhängig')],
 falle=r'Merdivenin solu kapalı (●), sağı açık (○). Bağımsızlığı çürütmek için tek hücre yeter.')

# ======================= Verteilungen
V1 = card('V1', 'Normal dağılım: olasılık ve kantil', BLUE,
 '„X ~ N(70, 16)“, „Berechnen Sie P(X ≤ 76)“, „Welcher Wert wird nur von 10 % überschritten?“',
 'Standartlaştır: \\(z=\\frac{x-\\mu}{\\sigma}\\), tablodan \\(\\Phi(z)\\) oku. Kantil için ters yön: \\(x=\\mu+\\sigma z\\).',
 [(r'σ\'yı bul: \(N(\mu,\sigma^2)\)\'de ikinci sayı <b>varyans</b>, kökünü al.', r'\(N(70,16)\Rightarrow\sigma=4\)'),
  (r'\(z\) hesapla (2 ondalık).', r'\(P(X\le76)\): \(z=\frac{76-70}{4}=1.5\)'),
  (r'Tabloya bak: „≤“ → \(\Phi(z)\) · „&gt;“ → \(1-\Phi(z)\) · arasında → fark · negatif: \(\Phi(-z)=1-\Phi(z)\).',
   r'\(P(X\le76)=\Phi(1.5)=0.9332\) · \(P(X\gt66)=1-\Phi(-1)=\Phi(1)=0.8413\) · \(P(66\lt X\lt78)=\Phi(2)-\Phi(-1)=0.8185\)'),
  (r'<b>Kantil:</b> \(x_p=\mu+\sigma\,z_p\). „Sadece %10 aşar“ = %90 kantili.', r'\(x_{0.9}=70+4\cdot1.282=75.128\) · \(x_{0.05}=70-4\cdot1.645=63.42\)'),
  (r'<b>Geriye:</b> olasılık verilmiş, σ veya μ aranıyor → \(z\)\'yi tablodan bul, denklemi çöz.', r'\(P(X\le78)=0.9772\Rightarrow z=2\Rightarrow\frac{78-70}{\sigma}=2\Rightarrow\sigma=4\)')],
 falle=r'\(N(100,225)\): σ = 15, 225 değil! Simetrik aralık: \(P(|X-\mu|\le k\sigma)=2\Phi(k)-1\).')

V2 = card('V2', 'Toplam, ortalama, fark ve ZGWS', BLUE,
 '„10 unabhängige Packungen, Gesamtgewicht“, „Mittelwert von n = 36“, „approximativ“, „Zentraler Grenzwertsatz“, „P(X > Y)“',
 'Önce yeni değişkenin dağılımını yaz (beklenti ve varyans), sonra V1 gibi standartlaştır.',
 [(r'<b>Toplam</b> \(S=X_1+\dots+X_n\): \(E=n\mu\), \(Var=n\sigma^2\).', r'10 × \(N(70,16)\): \(S\sim N(700,160)\); \(P(S\gt720)=1-\Phi\big(\frac{20}{\sqrt{160}}\big)=1-\Phi(1.58)=0.057\)'),
  (r'<b>Ortalama</b> \(\bar X\): \(E=\mu\), \(Var=\frac{\sigma^2}{n}\).', r'\(n=16\): \(\bar X\sim N(70,1)\); \(P(\bar X\gt72)=1-\Phi(2)=0.0228\)'),
  (r'<b>Fark</b> \(X-Y\) (bağımsız): beklentiler çıkar, <b>varyanslar toplanır</b>.', r'\(X\sim N(10,4),\ Y\sim N(8,5)\): \(X-Y\sim N(2,9)\); \(P(X\gt Y)=1-\Phi\big(\frac{0-2}{3}\big)=\Phi(0.67)=0.749\)'),
  (r'<b>ZGWS:</b> dağılım normal olmasa bile n büyükse (≥ 30) \(\bar X\) yaklaşık normal.', r'\(n=36,\ \mu=50,\ \sigma=12\): \(\bar X\overset{a}{\sim}N(50,4)\); \(P(\bar X\gt53)\approx1-\Phi(1.5)=0.0668\)'),
  (r'Binom → normal: \(N(n\pi,\ n\pi(1-\pi))\).', r'\(B(100;0.5)\approx N(50,25)\); \(P(X\le60)\approx\Phi(2)=0.977\)')],
 satz=r'„Nach dem ZGWS ist \(\bar X\) für großes n approximativ \(N(\mu,\sigma^2/n)\)-verteilt, unabhängig von der Verteilung der \(X_i\).“',
 falle=r'\(2X\) ile \(X_1+X_2\) farklı: \(Var(2X)=4\sigma^2\), \(Var(X_1+X_2)=2\sigma^2\).')

V3 = card('V3', 'Binom, Poisson, hipergeometrik, geometrik', BLUE,
 '„genau k“, „mindestens einer“, „im Mittel 3 pro Stunde“, „ohne Zurücklegen“, „bis zum ersten Erfolg“',
 'Önce hangi dağılım olduğunu tanı (aşağıdaki 1. adım), sonra formüle koy.',
 [(r'Dağılımı seç: sabit n deneme, başarı sayısı → <b>Binom</b> · „ortalama … saatte“ → <b>Poisson</b> · geri koymadan çekiliş → <b>hipergeometrik</b> · ilk başarıya kadar → <b>geometrik</b>.',
   r'„10 Teile, je 20 % defekt“ → \(X\sim B(10;0.2)\)'),
  (r'<b>Binom:</b> \(P(X=k)=\binom nk\pi^k(1-\pi)^{n-k}\); \(E=n\pi\), \(Var=n\pi(1-\pi)\).', r'\(P(X=2)=\binom{10}{2}0.2^2\,0.8^8=45\cdot0.04\cdot0.1678=0.302\)'),
  (r'<b>„En az bir“</b> = 1 − „hiç“.', r'\(P(X\ge1)=1-0.8^{10}=0.893\) (Altklausur: \(1-0.7^{10}=0.972\))'),
  (r'<b>Poisson:</b> \(P(X=k)=\frac{\lambda^k}{k!}e^{-\lambda}\); zaman aralığı değişirse λ\'yı da çarp.', r'\(\lambda=3\): \(P(X=0)=e^{-3}=0.0498\) · 2 Stunden: \(\lambda=6\), \(e^{-6}=0.0025\)'),
  (r'<b>Hipergeometrik:</b> \(\frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom Nn}\).', r'10 Teile, 4 defekt, 3 gezogen: \(P(X=1)=\frac{4\cdot15}{120}=0.5\)'),
  (r'<b>Geometrik</b> (başarıdan önceki başarısızlık sayısı): \(P(X=x)=p(1-p)^x\), \(E=\frac{1-p}{p}\).', r'\(p=0.2\): \(P(X=3)=0.2\cdot0.8^3=0.1024\)')],
 falle=r'„en az bir“ sorusunda \(p^n\) değil \(1-(1-p)^n\). „Kaç deneme gerekli ki en az bir ≥ 0.95?“: \(n\ge\frac{\log0.05}{\log(1-p)}\), yukarı yuvarla.')

V4 = card('V4', 'Üstel (Exponential) ve düzgün (Gleich-) dağılım', BLUE,
 '„Wartezeit“, „im Mittel 4 Minuten“, „Zeit bis zum Defekt“, „gleichverteilt zwischen a und b“',
 'Üstel: \\(P(T\\gt t)=e^{-\\lambda t}\\), \\(\\lambda=1/\\text{ortalama}\\). Düzgün: olasılık = genişlik / toplam genişlik.',
 [(r'λ\'yı bul: ortalama verildiyse \(\lambda=\frac1{\text{ortalama}}\).', r'im Mittel 4 min → \(\lambda=0.25\)'),
  (r'\(P(T\gt t)=e^{-\lambda t}\) · \(P(T\le t)=1-e^{-\lambda t}\) · arasında: \(e^{-\lambda a}-e^{-\lambda b}\).', r'\(P(T\gt6)=e^{-1.5}=0.223\) · \(P(T\le2)=1-e^{-0.5}=0.393\) · \(P(2\lt T\lt6)=0.383\)'),
  (r'E, Var, medyan, kantil.', r'\(E=\frac1\lambda=4\), \(Var=\frac1{\lambda^2}=16\), Median \(\frac{\log2}{\lambda}=2.773\), \(x_p=-\frac{\log(1-p)}{\lambda}\)'),
  (r'Belleksizlik: \(P(T\gt s+t\mid T\gt s)=P(T\gt t)\).', r'\(P(T\gt8\mid T\gt2)=P(T\gt6)=0.223\)'),
  (r'<b>Düzgün</b> \(U(a,b)\): \(P=\frac{\text{genişlik}}{b-a}\), \(E=\frac{a+b}2\), \(Var=\frac{(b-a)^2}{12}\).', r'\(U(2,12)\): \(P(X\gt9)=\frac{3}{10}=0.3\); \(E=7\); \(Var=\frac{100}{12}=8.333\)')],
 falle=r'λ ortalama değil, ortalamanın tersidir („im Mittel 3 h“ → λ = 1/3).')

# ======================= Bonus
B1 = card('B1', 'BONUS: Bayes ve toplam olasılık – ağaç (Altklausur A3)', GRN,
 '„Mit einer Wahrscheinlichkeit von 80 % gehört ein Bestehender …“, „Wie groß ist die Wahrscheinlichkeit, dass sie besteht, wenn …“',
 'Ağaç çiz: önce ana olay (Bestehen / Nicht-Bestehen), sonra dallar. Yol = çarpım, toplam olasılık = yolların toplamı, Bayes = istenen yol / toplam.',
 [(r'Olayları adlandır ve verilenleri koşullu olarak yaz („Besteher\'lerin %80\'i …“ → \(P(\cdot\mid B)\)).',
   r'\(P(B)=0.7\), \(P(S_1\mid B)=0.8\), \(P(S_2\mid B)=0.15\), \(P(S_1\mid\bar B)=0.1\), \(P(S_2\mid\bar B)=0.2\)'),
  (r'Tümleyenleri hesapla (her dalın toplamı 1).', r'\(P(\bar B)=0.3\), \(P(S_3\mid B)=1-0.8-0.15=0.05\), \(P(S_3\mid\bar B)=1-0.1-0.2=0.7\)'),
  (r'<b>Toplam olasılık:</b> tüm yolları topla – her yolda <b>kendi</b> ana olasılığını kullan (0.7 ve <b>0.3</b>).', r'\(P(S_3)=0.05\cdot0.7+0.7\cdot0.3=0.035+0.21=0.245\)'),
  (r'<b>Bayes:</b> istenen yol / toplam olasılık.', r'\(P(B\mid S_2)=\frac{P(S_2\mid B)P(B)}{P(S_2)}=\frac{0.15\cdot0.7}{0.15\cdot0.7+0.2\cdot0.3}=\frac{0.105}{0.165}=0.636\)'),
  (r'„En az bir“: \(1-\)hiç.', r'\(P(\text{mind. 1 Nicht-Besteher unter 10})=1-0.7^{10}=0.972\)')],
 falle=r'Bayes\'te payda HER ZAMAN toplam olasılıktır – sadece payı yazmak puan kaybettirir (0.105 değil 0.636!).')

B2 = card('B2', 'BONUS: Kümeler ve Laplace (Altklausur A4)', GRN,
 '„Ω = {1, …, 9}“, „Berechnen Sie |A ∩ B̄|, |Ā ∪ B|“, „P(A | B̄)“',
 'Önce tümleyeni yaz, SONRA birleşim/kesişimi al. Laplace: olasılık = eleman sayısı / |Ω|.',
 [(r'Tümleyenleri tek tek yaz (Ω\'da olup kümede olmayanlar).', r'\(A=\{1,3,6,7\}\), \(B=\{1,3,6,9\}\): \(\bar A=\{2,4,5,8,9\}\), \(\bar B=\{2,4,5,7,8\}\)'),
  (r'Kesişim ∩ = <b>ikisinde de</b> olanlar.', r'\(A\cap\bar B=\{7\}\Rightarrow|A\cap\bar B|=1\)'),
  (r'Birleşim ∪ = <b>en az birinde</b> olanlar – tümleyeni yazdıktan sonra diğer kümeyi EKLE.', r'\(\bar A\cup B=\{2,4,5,8,9\}\cup\{1,3,6,9\}=\{1,2,3,4,5,6,8,9\}\Rightarrow8\)'),
  (r'Koşullu olasılık: \(P(A\mid B)=\frac{|A\cap B|}{|B|}\) (Laplace).', r'\(P(A\mid\bar B)=\frac{|A\cap\bar B|}{|\bar B|}=\frac15=0.2\)'),
  (r'Bağımsız mı? \(P(A\cap B)=P(A)P(B)\) kontrol et. Ayrık mı? \(A\cap B=\emptyset\) mi?', r'\(P(A\cap B)=\frac39\), \(P(A)P(B)=\frac49\cdot\frac49=\frac{16}{81}\neq\frac13\Rightarrow\) abhängig')],
 falle=r'De Morgan: \(\overline{A\cap B}=\bar A\cup\bar B\), \(\overline{A\cup B}=\bar A\cap\bar B\). Tümleyeni yazıp birleşimi unutma (PK4 ve Altklausur\'da iki kez puan kaybettin).')

html = CSS + p0
html += sec('TEST – Hipotez testleri (her sınavda ~8 puan)', RED) + T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9
html += sec('KI – Güven aralıkları', PURP) + K1 + K2
html += sec('SCHÄTZER – Tahminciler (her sınavda ~5 puan)', ORNG) + S1 + S2 + S3 + S4
html += sec('DICHTE – Yoğunluk ve dağılım fonksiyonu (~9 puan)', TEAL) + D1 + D2 + D3 + D4 + D5
html += sec('VERTEILUNGEN – Hazır dağılımlarla hesap', BLUE) + V1 + V2 + V3 + V4
html += sec('BONUS – Altklausur\'da puan kaybettiğin konular', GRN) + B1 + B2
html = html.replace("\\'", "'")  # r-Strings: \' -> '
open(OUT, 'w').write(html)
print(OUT)
