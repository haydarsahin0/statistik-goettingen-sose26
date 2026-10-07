# Fügt die Lernhilfe-Kästen in Probeklausur 3 ein (einmalig, idempotent)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def H(t):
    return '<div class="lh">' + t + '</div>'

def before(s, marker, html):
    assert marker in s, marker[:60]
    return s.replace(marker, html + marker, 1)

p = 'content/pk3_a.html'
s = open(p).read()
if 'class="lh"' not in s:
    s = before(s, '<li><span class="lb">(c)</span>Bestimmen Sie das untere Quartil',
        H(r'<b>Quartil:</b> \(n\cdot\alpha\) berechnen. Ganze Zahl → Mittelwert aus \(x_{(n\alpha)}\) und \(x_{(n\alpha+1)}\); keine ganze Zahl → aufrunden. Hier: \(12\cdot0.25=3\) → \((x_{(3)}+x_{(4)})/2\). <b>Interquartilsabstand</b> \(d_Q=x_{0.75}-x_{0.25}\). <b>Ausreißer</b>, wenn Wert \(&gt; x_{0.75}+1.5\,d_Q\). <b>Varianz:</b> \(s^2=\frac1n\sum x_i^2-\bar x^2\), \(s_*^2=\frac{n}{n-1}s^2\).<span class="tr">Önce n·α hesapla; tam sayıysa iki değerin ortalaması.</span>'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Berechnen Sie die relativen Häufigkeiten',
        H(r'<b>Relative Häufigkeit</b> \(f_j=h_j/n\). <b>Säulenhöhe</b> \(=f_j/\text{Klassenbreite}\) (Fläche = Anteil!). <b>Klassiertes Mittel</b> \(\bar x\approx\sum f_j\cdot m_j\) mit Klassenmitte \(m_j\). <b>Modalklasse</b> = höchste Säule. <b>Anteil ab 30:</b> Gleichverteilung in der Klasse annehmen → Säulenhöhe × Breite des Stücks \([30,40)\) + ganze Klasse \([40,60]\).<span class="tr">Sütun yüksekliği = oran / genişlik. Alan = oran.</span>'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Berechnen Sie die empirische Kovarianz',
        H(r'<b>Kovarianz:</b> \(s_{xy}=\frac1n\sum x_\nu y_\nu-\bar x\bar y\). <b>Korrelation:</b> \(r_{xy}=\dfrac{s_{xy}}{\sqrt{s_x^2\,s_y^2}}\) mit \(s_x^2=\frac1n\sum x_\nu^2-\bar x^2\). Interpretation: Vorzeichen (positiv/negativ) + Stärke (schwach/mittel/stark) + „linear“. <b>Regression:</b> \(b=s_{xy}/s_x^2\), \(a=\bar y-b\bar x\), Prognose \(\hat y=a+b\cdot22\). <b>Spearman:</b> Ränge von x und y vergleichen – steigen beide in derselben Reihenfolge, ist \(r_{SP}=1\).<span class="tr">Önce ortalamalar, sonra s_xy ve s_x², sonra b, en son a.</span>'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Berechnen Sie die folgenden Wahrscheinlichkeiten. <span class="pt">(3 P)</span>\n<div class="lk s"><span class="lkl">P(„keine Panne“)',
        H(r'Baum: 1. Stufe Panne / keine Panne (danach wird „zunächst“ unterschieden), 2. Stufe Radtyp. Fehlender Ast: Stadtrad \(=1-\text{E-Bike}-\text{Lastenrad}\). <b>(b)</b> totale Wahrscheinlichkeit: Pfade addieren. <b>(c)</b> Bayes: Pfad „Panne ∩ Stadtrad“ / Ergebnis aus (b). <b>(d)</b> „mindestens eine“ \(=1-P(\text{keine})^{10}\).'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Bestimmen Sie \\(c\\) derart',
        H(r'<b>(a)</b> Gesamtfläche = 1: \(\int_0^3 c\,x^2\,dx=c\big[\tfrac{x^3}{3}\big]_0^3=1\) → nach \(c\) auflösen. <b>(b)</b> \(E(X)=\int_0^3 x\cdot f(x)\,dx\) (Potenzregel: Exponent +1, durch neuen Exponenten). <b>(c)</b> \(F(x)=\int_0^x f(t)\,dt\) mit drei Fällen: \(0\) für \(x&lt;0\), Formel für \(0\le x\le3\), \(1\) für \(x&gt;3\); dann \(P(1\le X\le2)=F(2)-F(1)\). <b>(d)</b> \(N(30,16)\): 16 ist die <i>Varianz</i> → \(\sigma=4\). Standardisieren \(z=(36-30)/4\), dann \(P(Y&gt;36)=1-\Phi(z)\).<span class="tr">Dichte görünce: toplam yok, integral var. F(x) her zaman üç satır.</span>'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Stellen Sie zunächst die Likelihood- und die Log-Likelihood-Funktion auf.',
        H(r'<b>Rezept:</b> ① \(L(\lambda)=\prod_{i=1}^n f(x_i;\lambda)\) ② \(l(\lambda)=\log L(\lambda)\) mit Log-Regeln vereinfachen ③ Ableitung \(l^{\prime}(\lambda)\) ④ \(=0\) setzen, nach \(\hat\lambda\) auflösen ⑤ \(l^{\prime\prime}(\lambda)&lt;0\)? ⑥ Daten einsetzen. <b>Helfer:</b> \(\prod\lambda^2=\lambda^{2n}\), \(\prod e^{-\lambda x_i}=e^{-\lambda\sum x_i}\), \(\log(\lambda^{2n})=2n\log\lambda\), \(\frac{d}{d\lambda}\,2n\log\lambda=\frac{2n}{\lambda}\), Terme ohne \(\lambda\) (z. B. \(\sum\log x_i\)) haben Ableitung 0.<span class="tr">① ve ② her zaman yapılabilir: çarpımı yaz, log al. Bu bile 3–4 puan.</span>'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Prüfen Sie für alle drei Schätzer',
        H(r'<b>Erwartungstreu</b> heißt \(E(T)=\mu\). Rechenregel: \(E(aX_1+bX_2)=a\mu+b\mu\). <b>Bias</b> \(=E(T)-\mu\). <b>Varianz</b> (unabhängig): \(Var(aX_1+bX_2)=a^2\sigma^2+b^2\sigma^2\). <b>MSE</b> \(=Var+\text{Bias}^2\); der Schätzer mit kleinerem MSE ist besser.<span class="tr">Sabit dışarı: beklenen değerde a, varyansta a².</span>'))
    s = before(s, '<ol class="tl">\n<li><span class="lb">(a)</span>Stellen Sie das passende Hypothesenpaar auf.',
        H(r'<b>Hypothesen:</b> Was abgesichert werden soll („zu wenig“) kommt in \(H_1\): \(H_0:\mu\ge\mu_0\) vs. \(H_1:\mu&lt;\mu_0\). <b>Varianz unbekannt → t-Test:</b> \(T=\dfrac{\bar x-\mu_0}{s^*/\sqrt n}\sim t(n-1)\) unter \(H_0\). <b>Linksseitig:</b> \(H_0\) ablehnen, wenn \(T&lt;-t_{n-1;\,1-\alpha}\). <b>KI:</b> \(\bar x\pm t_{n-1;\,0.975}\cdot s^*/\sqrt n\). <b>Satz:</b> „\(H_0\) wird (nicht) abgelehnt; es kann (nicht) statistisch abgesichert werden, dass …“<span class="tr">İspatlamak istediğin şey H₁ tarafına gider. Eşitlik işareti hep H₀ tarafında.</span>'))
    s = s.replace('Probeklausur 3 Statistik (Teil A)</h1>', 'Probeklausur 3 Statistik (Teil A)</h1>' + H('Diese Übungsversion enthält bei den Themen, die du noch nicht (fertig) gelernt hast, gelbe Lernhilfe-Kästen mit dem Lösungsweg – ohne die Ergebnisse. Erst ohne Kasten versuchen, dann nachsehen!<span class="tr">Sarı kutular sadece çözüm yolunu gösterir, sonucu değil. Önce kutuya bakmadan dene.</span>'), 1)
    assert s.count('class="lh"') == 9, s.count('class="lh"')
    open(p, 'w').write(s)

p = 'content/pk3_b.html'
s = open(p).read()
if 'class="lh"' not in s:
    def hint(s, label, html):
        key = '<li><span class="lb">(' + label + ')</span>'
        i = s.index(key); j = s.index('</li>', i)
        return s[:j] + H(html) + s[j:]
    s = hint(s, 'b', r'<code>d &lt;- read.csv("Fitness.csv", sep = ",", dec = ".", header = TRUE)</code> und <code>head(d)</code>. Vorher die CSV ansehen: Trennzeichen „,“ oder „;“?')
    s = hint(s, 'c', r'<code>class(d$Studio)</code>, <code>class(d$Besuche)</code> (oder <code>typeof()</code>, <code>str(d)</code>). Antwortsatz: „… ist vom Typ character / integer (ganze Zahlen).“')
    s = hint(s, 'd', r'<code>round(median(d$Minuten), 3)</code>, <code>round(IQR(d$Minuten), 3)</code>. Antwortsatz mit beiden Zahlen.')
    s = hint(s, 'e', r'Gerüst: <code>pdf("Boxplot.pdf")</code> → <code>boxplot(Minuten ~ Studio, data = d, main = "Sitz …, Matr.Nr. …, Aufgabenteil e)", xlab = "Studio", ylab = "Trainingsdauer in Minuten")</code> → <code>dev.off()</code>. Mediane je Studio: <code>tapply(d$Minuten, d$Studio, median)</code>.<span class="tr">dev.off() unutursan PDF boş kalır.</span>')
    s = hint(s, 'f', r'<code>tab &lt;- table(d$Studio, d$Abo)</code>, dann zeilenweise Anteile: <code>round(prop.table(tab, margin = 1), 3)</code> → Spalte „Premium“ vergleichen.')
    s = hint(s, 'g', r'Exponentialdichte in R: <code>dexp(x, rate = λ)</code>. <code>d$iL04 &lt;- dexp(d$Wartezeit, rate = 0.4)</code>, Likelihood = Produkt: <code>prod(d$iL04)</code>. Aus <code>8.3e-64</code> wird \(8.3\times10^{-64}\).')
    s = hint(s, 'h', r'<code>Likelihood.exp &lt;- function(lambda, x) { return(prod(dexp(x, rate = lambda))) }</code>; Gitter: <code>lam &lt;- seq(0.30, 0.60, by = 0.05)</code>; <code>Ls &lt;- sapply(lam, Likelihood.exp, x = d$Wartezeit)</code>; ML: <code>lam[which.max(Ls)]</code>; Vergleich: <code>1/mean(d$Wartezeit)</code>.')
    s = hint(s, 'i', r'Behauptung „weniger als 70“ → \(H_1:\mu&lt;70\), \(H_0:\mu\ge70\). <code>t.test(d$Minuten, mu = 70, alternative = "less")</code>. Entscheidung: p-Wert &lt; 0.05 → \(H_0\) ablehnen, sonst nicht ablehnen. Satz im Sachzusammenhang!<span class="tr">p &lt; α ise H₀ reddedilir.</span>')
    s = s.replace('Probeklausur 3 Statistik (Teil B)</h1>', 'Probeklausur 3 Statistik (Teil B)</h1>' + H('Diese Übungsversion enthält gelbe Lernhilfe-Kästen mit den passenden R-Befehlen – ohne Ergebnisse. Erst selbst versuchen, dann nachsehen!'), 1)
    open(p, 'w').write(s)
print('ok')
