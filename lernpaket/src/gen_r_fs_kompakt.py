# R-Formelsammlung kompakt (Teil B): 2 Seiten, Karten-Layout, jeder Befehl mit türkischer Erklärung
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'extra', 'r_fs_kompakt.html')

# (Kartennummer, Titel, Farbe, [(Code, Türkisch)], Hinweis)
CARDS = [
 ('01', 'Start & Einlesen', '#2563eb', [
  ('setwd(path.expand("~"))', 'çalışma klasörünü ayarla (ilk satır)'),
  ('getwd(); list.files()', 'klasörü / dosyaları kontrol et'),
  ('d <- read.csv("D.csv")', 'CSV oku (sep="," dec=".")'),
  ('read.csv("D.csv", sep=";", dec=",")', 'Alman formatı ; ve 3,5'),
  ('read.csv2("D.csv")', 'aynısı, kısayol'),
  ('read.table("D.txt", header=TRUE)', 'txt dosyası, 1. satır başlık'),
  ('head(d); str(d); summary(d)', 'ilk satırlar · yapı/tipler · özet'),
  ('dim(d); nrow(d); names(d)', 'boyut · satır sayısı · sütun adları'),
 ], 'Sayılar <code>chr</code> çıkıyorsa → <code>dec=","</code> eksik.'),
 ('02', 'Datentypen', '#7c3aed', [
  ('class(x); typeof(x)', 'tip: numeric / integer / character / factor'),
  ('is.numeric(x); is.character(x)', 'tip kontrolü (TRUE/FALSE)'),
  ('as.numeric(x); as.character(x)', 'tip dönüştür'),
  ('factor(x); levels(f)', 'kategoriye çevir · kategoriler'),
  ('factor(x, levels=c(..), ordered=TRUE)', 'sıralı (ordinal) faktör'),
  ('data.frame(x=c(..), g=c(..))', 'kendi tablonu oluştur'),
 ], 'Cümle: „Die Variable … ist vom Typ …“'),
 ('03', 'Zugriff & Filtern', '#0891b2', [
  ('d$x;  d[i, ];  d[ , "x"]', 'sütun · satır i · sütun adıyla'),
  ('d$x[d$g == "A"]', 'koşullu seçim (== iki eşittir)'),
  ('subset(d, g=="A" & x>3)', 'koşula uyan satırlar (& ve, | veya)'),
  ('which(x > 3); which.max(x)', 'satır numaraları · en büyüğün yeri'),
  ('sort(x); d[order(d$x), ]', 'sırala · tabloyu sırala'),
  ('d$neu <- ifelse(x>30,"a","b")', 'yeni sütun, koşullu'),
  ('cut(x, breaks=c(..), right=FALSE)', 'sınıflara ayır [a,b)'),
  ('is.na(x); mean(x, na.rm=TRUE)', 'eksik değer bul · atla'),
  ('unique(x);  "A" %in% x', 'farklı değerler · içinde var mı'),
 ], ''),
 ('04', 'Rechnen & Mengen', '#0d9488', [
  ('c(); 1:5; seq(0,1,by=.25); rep(2,3)', 'vektör · dizi · adımlı dizi · tekrar'),
  ('sum(x); prod(x); length(x)', 'toplam · çarpım · eleman sayısı'),
  ('cumsum(x); max(x); min(x)', 'kümülatif toplam · en büyük · en küçük'),
  ('sqrt(x); exp(x); log(x)', 'kök · e üzeri · <b>log = ln</b>'),
  ('choose(n,k); factorial(n)', 'binom katsayısı · faktöriyel'),
  ('union(A,B); intersect(A,B)', 'birleşim ∪ · kesişim ∩'),
  ('setdiff(A,B); is.element(6,B)', 'fark A\\B · eleman mı'),
  ('matrix(v, nrow=2); colSums(M)', 'matris · sütun toplamları'),
  ('apply(M, 1, sum)', 'her satıra uygula (2 = sütun)'),
  ('for (i in 1:n) { … }', 'döngü: i = 1…n tekrar'),
 ], ''),
 ('05', 'Häufigkeiten', '#16a34a', [
  ('table(x)', 'mutlak frekans'),
  ('prop.table(table(x))', 'göreli frekans (toplam 1)'),
  ('cumsum(prop.table(table(x)))', 'kümülatif → EVF tablosu'),
  ('Fh <- ecdf(x); Fh(2)', '\\(\\hat F(2)\\) = „≤ 2“ oranı'),
  ('table(x, y); addmargins(t)', 'Kontingenztafel · toplamlarla'),
  ('prop.table(t, margin=1)', 'satır içi oranlar (2 = sütun)'),
 ], ''),
 ('06', 'Lage & Streuung', '#ca8a04', [
  ('mean(x); median(x)', 'ortalama · medyan'),
  ('names(which.max(table(x)))', 'modus (en sık değer)'),
  ('var(x); sd(x)', 'düzeltilmiş \\(s_*^2\\), \\(s_*\\) (<b>n−1</b>)'),
  ('var(x)*(n-1)/n', 'empirik varyans \\(s^2\\) (n ile)'),
  ('quantile(x, c(.25,.5,.75))', 'kantiller (ders: <code>type=2</code>)'),
  ('IQR(x); range(x)', 'çeyrekler açıklığı · min–max'),
  ('tapply(d$x, d$g, mean)', 'gruplara göre ortalama'),
  ('aggregate(x ~ g, data=d, mean)', 'aynısı, tablo olarak'),
 ], '<code>var</code>, <code>sd</code>, <code>cov</code> hep n−1 ile böler!'),
 ('07', 'Zusammenhang', '#ea580c', [
  ('cov(x, y); cor(x, y)', 'kovaryans (n−1) · Pearson r'),
  ('cor(x, y, method="spearman")', 'Spearman sıra korelasyonu'),
  ('chisq.test(t)$expected', 'bağımsızlıkta beklenen frekanslar'),
  ('chisq.test(t, correct=FALSE)$statistic', 'χ²-katsayısı'),
 ], ''),
 ('08', 'Grafiken', '#dc2626', [
  ('pdf("a.pdf") … dev.off()', 'grafiği PDF\'e kaydet (png() da olur)'),
  ('hist(x, breaks=c(..), right=FALSE, freq=FALSE)', 'histogram: sınırlar, sol kapalı, yoğunluk'),
  ('main=, xlab=, ylab=', 'başlık (Aufgabe + Matrikel + Platz), eksenler'),
  ('lines(density(x))', 'histograma çekirdek yoğunluğu ekle'),
  ('density(x, bw=2, kernel="epanechnikov")', 'KDE: bant genişliği, çekirdek'),
  ('boxplot(y ~ g, data=d)', 'gruplara göre boxplot'),
  ('plot(x, y); abline(lm(y ~ x))', 'saçılım + regresyon doğrusu'),
  ('barplot(table(x))', 'çubuk grafik'),
  ('plot(ecdf(x))', 'EVF çizimi'),
  ('curve(dexp(x, r), add=TRUE)', 'teorik eğri ekle'),
  ('par(mfrow=c(1,2))', 'yan yana 2 grafik'),
 ], ''),
 ('09', 'Verteilungen d · p · q · r', '#9333ea', [
  ('dbinom(k, n, p)', '\\(P(X=k)\\) binom'),
  ('pbinom(k, n, p)', '\\(P(X\\le k)\\)'),
  ('1 - pbinom(k-1, n, p)', '\\(P(X\\ge k)\\) (<b>k−1</b>!)'),
  ('dpois(k, λ); ppois(k, λ)', 'Poisson'),
  ('pnorm(x, μ, σ); qnorm(p, μ, σ)', 'Normal (σ = sd, varyans değil!)'),
  ('pexp(x, rate=λ); qexp(p, λ)', 'Üstel, λ = 1/ortalama'),
  ('punif(x, a, b); dgeom(k, p)', 'Düzgün · geometrik'),
  ('dgamma(x, shape, rate)', 'Gamma yoğunluğu'),
  ('qt(.975, df); qchisq(.95, df)', 't- ve χ²-kantilleri'),
  ('1 - pnorm(z); 1 - pt(t, df)', 'sağ kuyruk p-değeri'),
  ('rbinom(N,n,p); rnorm(N,μ,σ)', 'rastgele sayı üret'),
 ], 'd = olasılık/yoğunluk · p = ≤ · q = kantil · r = rastgele'),
 ('10', 'Simulation', '#db2777', [
  ('set.seed(123)', 'tekrarlanabilir rastgelelik'),
  ('sample(1:6, 5, replace=TRUE)', 'zar 5 kez (geri koyarak)'),
  ('mean(x == 3)', 'olayın göreli frekansı ≈ olasılık'),
 ], ''),
 ('11', 'Likelihood & ML', '#1d4ed8', [
  ('prod(dpois(x, λ))', '<b>Likelihood</b> = olasılıkların çarpımı'),
  ('sum(dpois(x, λ, log=TRUE))', '<b>Log-Likelihood</b> = log\'ların toplamı'),
  ('sum(log(dgamma(x, a, b)))', 'çarpım 0 çıkarsa (underflow) bunu kullan'),
  ('L <- function(l) prod(dpois(x, l))', 'L\'yi fonksiyon olarak tanımla'),
  ('for (l in 17:23) print(L(l))', 'grid: her λ için L (resmî çözüm)'),
  ('g <- 17:23; g[which.max(sapply(g, L))]', 'grid: en iyi λ tek satırda'),
  ('optimize(f, c(0.1,5), maximum=TRUE)', 'tek parametre sayısal max'),
  ('mean(x);  1/mean(x)', 'kontrol: Poisson \\(\\hat\\lambda=\\bar x\\) · Exp \\(1/\\bar x\\)'),
 ], 'Cümle: „Das Maximum der Likelihood liegt bei λ = …“'),
 ('11b', 'nlm (mehrere Parameter)', '#1e40af', [
  ('nl <- function(tp, x) -sum(log(dgamma(x, exp(tp[1]), exp(tp[2]))))', '<b>negatif</b> log-L, <code>exp()</code> parametreyi pozitif yapar'),
  ('m <- nlm(nl, p=c(0,0), x=x)', 'minimize et (başlangıç değerleri p)'),
  ('exp(m$estimate)', 'geri dönüştür → \\(\\hat\\alpha,\\hat\\beta\\)'),
  ('-m$minimum', 'maksimum log-Likelihood'),
 ], '„NA/Inf replaced“ uyarıları normal.'),
 ('12', 'Konfidenzintervalle', '#0f766e', [
  ('mean(x)+c(-1,1)*qnorm(.975)*σ/sqrt(n)', 'μ için KI, σ biliniyor'),
  ('mean(x)+c(-1,1)*qt(.975,n-1)*sd(x)/sqrt(n)', 'μ için KI, σ bilinmiyor'),
  ('t.test(x, conf.level=.95)$conf.int', 'aynısı hazır'),
  ('p+c(-1,1)*qnorm(.975)*sqrt(p*(1-p)/n)', 'oran için KI'),
  ('(n-1)*var(x)/qchisq(c(.975,.025), n-1)', 'varyans için KI'),
 ], ''),
 ('13', 'Hypothesentests', '#b91c1c', [
  ('t.test(x, mu=μ0, alternative="greater")', 't-Test, H₁: μ > μ0 ("less" <, "two.sided" ≠)'),
  ('t.test(...)$p.value; $statistic', 'p-değeri · test istatistiği'),
  ('(mean(x)-μ0)/(σ/sqrt(n))', 'Gauß z elle; p = 1-pnorm(z)'),
  ('chisq.test(table(x, y))', 'χ² bağımsızlık testi'),
  ('chisq.test(table(x), p=c(..))', 'χ² uyum testi'),
  ('binom.test(k, n, p=.5, alternative="greater")', 'kesin binom testi'),
  ('qt(.95, df)', 'ret bölgesi sınırı'),
 ], '<b>p ≤ α → H₀ ret.</b> „Da der p-Wert … kleiner als α ist, wird H₀ abgelehnt …“'),
 ('14', 'Regression', '#4f46e5', [
  ('m <- lm(y ~ x, data=d); coef(m)', 'a (Intercept) ve b (eğim)'),
  ('summary(m)$r.squared', 'R²'),
  ('summary(m)$coefficients', 'katsayılar + p-değerleri'),
  ('predict(m, data.frame(x=40))', 'x = 40 için tahmin'),
  ('resid(m)', 'artıklar \\(y-\\hat y\\)'),
 ], ''),
 ('15', 'Ausgabe & Runden', '#475569', [
  ('round(x, 3)', '3 ondalığa yuvarla (her sonuçta!)'),
  ('sprintf("%.20f", x)', 'sabit sayıda ondalık yazdır'),
  ('z <- "0."; for (i in 1:54) z <- paste0(z, i)', 'Yennefer-Zahl: 99 ondalık (Altklausur h)'),
  ('options(scipen=999)', 'e-131 gösterimini kapat'),
  ('paste("a", 1); cat("n =", n)', 'metin + sayı birleştir / yazdır'),
 ], ''),
]

FEHLER = [
 ('mehr Spalten als Spaltennamen', '<code>sep=";", dec=","</code> ekle'),
 ('cannot open file / Datei nicht gefunden', '<code>setwd</code> + <code>list.files()</code>'),
 ('object not found', 'yazım/büyük-küçük harf, nesne yok'),
 ('could not find function', 'komut adı yanlış'),
 ('Argument nicht numerisch → NA', 'sütun metin: <code>dec</code> / <code>as.numeric</code>'),
 ('Ergebnis NA', '<code>na.rm=TRUE</code>'),
]

SAETZE = [
 ('Typ', '„Die Variable <i>x</i> ist vom Typ <i>integer</i>.“'),
 ('Lage', '„Das arithmetische Mittel von <i>x</i> beträgt 30.637.“'),
 ('Likelihood', '„Die Likelihood unter λ = 20 beträgt 6.938 · 10⁻¹³¹.“'),
 ('ML', '„Das Maximum der Likelihood liegt bei λ = 22; der ML-Schätzer ist 22.“'),
 ('Test', '„Da der p-Wert 0.001 kleiner als α = 0.05 ist, wird H₀ abgelehnt. Es ist abgesichert, dass …“'),
 ('KI', '„Das 95 %-KI lautet [28.935; 32.340].“'),
]

CSS = r'''<style>
@page{size:A4;margin:7mm 7mm 8mm}
.w{width:auto!important;padding:0!important}
body{background:#f4f6fb!important;font-family:Inter,Arial,sans-serif;font-size:9.6px!important;line-height:1.36!important;color:#0f172a}
.hero{display:flex;justify-content:space-between;align-items:flex-end;background:linear-gradient(120deg,#0f172a,#1e3a8a 60%,#2563eb);color:#fff;border-radius:9px;padding:3mm 4mm;margin-bottom:2.2mm}
.hero h1{font:800 19px Inter;margin:0!important;color:#fff!important;letter-spacing:-.01em}
.hero .s{font-size:8.4px;opacity:.85;margin-top:.6mm}
.hero .chip{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);border-radius:20px;padding:.8mm 3mm;font-weight:700;font-size:8.4px;white-space:nowrap}
.flow{display:flex;gap:1.4mm;margin-bottom:2.2mm}
.flow div{flex:1;background:#fff;border-radius:6px;padding:1.2mm 1.8mm;border:1px solid #e2e8f0;font-size:8.6px}
.flow b.n{display:inline-block;width:12px;height:12px;border-radius:50%;background:#1e3a8a;color:#fff;text-align:center;line-height:12px;font-size:7px;margin-right:3px}
.grid{column-count:3;column-gap:2mm}
.card{break-inside:avoid;background:#fff;border-radius:7px;margin:0 0 2mm;border:1px solid #e2e8f0;box-shadow:0 .4mm 1mm rgba(15,23,42,.06);overflow:hidden}
.card .hd{display:flex;align-items:center;gap:1.6mm;padding:1.1mm 2mm;border-bottom:1px solid #eef2f7}
.card .no{background:var(--c);color:#fff;border-radius:4px;font:800 9px Inter;padding:.3mm 1.3mm}
.card .ti{font:800 10.6px Inter;color:var(--c)}
.card table{width:100%;border-collapse:collapse;table-layout:fixed}
.card td.t{word-break:break-word}
.card td{padding:.8mm 1.7mm;vertical-align:top;border-bottom:1px dotted #e5e7eb}
.card tr:last-child td{border-bottom:0}
.card td.k{width:56%}
.card code.c{display:inline-block;font:8.9px/1.36 "JetBrains Mono",monospace;font-variant-ligatures:none;background:#0f172a;color:#e2e8f0;border-radius:3px;padding:.25mm 1mm;white-space:pre-wrap;word-break:break-word}
.card td.t{color:#334155}
.card .ft{background:color-mix(in srgb,var(--c) 9%,#fff);color:#1e293b;padding:.8mm 2mm;font-size:8.6px;border-top:1px solid #eef2f7}
code{font-family:"JetBrains Mono",monospace;font-size:.95em;font-variant-ligatures:none;background:#eef2ff;border-radius:2px;padding:0 1px}
.katex{font-size:1.02em}
.mini td{font-size:7.2px}
</style>'''

def card(no, title, color, rows, foot):
    h = f'<div class="card" style="--c:{color}"><div class="hd"><span class="no">{no}</span><span class="ti">{title}</span></div><table>'
    for c, t in rows:
        h += f'<tr><td class="k"><code class="c">{html.escape(c)}</code></td><td class="t">{t}</td></tr>'
    h += '</table>'
    if foot: h += f'<div class="ft">{foot}</div>'
    return h + '</div>'

def build():
    h = [CSS, '<div class="hero"><div><h1>R-Formelsammlung · Teil B</h1><div class="s">Alle Befehle für die ILIAS-Klausur · jeder Befehl mit türkischer Erklärung · Details & echte Outputs: R_Befehle_TeilB.pdf</div></div><div class="chip">60 min · 45 Punkte</div></div>']
    h.append('<div class="flow">'
             '<div><b class="n">1</b>Kodu yaz, <b>Strg+Enter</b> ile çalıştır</div>'
             '<div><b class="n">2</b><b>Kod + çıktı</b> → ILIAS kutusu</div>'
             '<div><b class="n">3</b>Sonuç <code>round(…, 3)</code></div>'
             '<div><b class="n">4</b>2. kutu: <b>tam Almanca cümle</b></div>'
             '<div><b class="n">5</b>Scripti sık kaydet · grafikleri yükle</div></div>')
    h.append('<div class="grid">')
    for c in CARDS:
        h.append(card(*c))
    h.append(card('!', 'Fehlermeldungen', '#be123c', FEHLER, ''))
    h.append(card('✎', 'Antwortsätze (ILIAS)', '#15803d', [(k, v) for k, v in SAETZE], 'Sayısal olmayan her cevap <b>tam cümle</b>.').replace('<code class="c">', '<code class="c" style="background:#15803d">'))
    h.append('</div>')
    open(OUT, 'w').write('\n'.join(h))
    print(OUT)

if __name__ == '__main__':
    build()
