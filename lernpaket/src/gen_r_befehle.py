# R-Befehlsliste für Teil B: jeder Befehl mit türkischer Erklärung, Beispiel und echtem R-Output
import os, re, shutil, subprocess, html
HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.join(HERE, 'rwork', 'befehle')
OUT = os.path.join(HERE, 'content', 'extra', 'r_befehle.html')

# (Befehl/Code, türkische Erklärung, run?)  – Code wird in EINER R-Sitzung nacheinander ausgeführt
S = []
def sec(title, intro): S.append([title, intro, []])
def r(code, tr, run=True): S[-1][2].append((code.strip('\n'), tr, run))

# ------------------------------------------------------------------ 0
sec('0 · Start, Arbeitsordner, Hilfe', 'Sınavda ilk 2 dakika: klasörü ayarla, dosyanın orada olduğunu kontrol et, scripti kaydet.')
r('setwd(path.expand("~"))', '<b>Çalışma klasörünü</b> ayarlar (ev klasörü). Sınavda soru tam olarak bunu ister – <b>ilk satır</b>.', False)
r('getwd()\n# [1] "/home/IhrName"', 'Şu an hangi klasörde olduğunu gösterir. Kontrol için.', False)
r('list.files()\n# [1] "Daten.csv" "Klausur.R"', 'Klasördeki dosyaları listeler. CSV dosyası listede yoksa okuyamazsın → yanlış klasör.', False)
r('# Das ist ein Kommentar', '<code>#</code> ile başlayan satır <b>yorum</b>dur, çalışmaz. Kodunu açıklamak için kullan.')
r('?mean      # oder help(mean)', 'Bir komutun <b>yardım sayfasını</b> açar (argümanları unutursan).', False)
r('rm(list = ls())', 'Bellekteki <b>bütün nesneleri siler</b> (temiz başlangıç).', False)

# ------------------------------------------------------------------ 1
sec('1 · Daten einlesen', 'Önce dosyanın ilk satırına bak: ayraç virgül mü noktalı virgül mü? Ondalık nokta mı virgül mü?')
r('d <- read.csv("Beispiel_Mensa.csv")', 'CSV dosyasını okur ve <code>d</code> adlı <b>data frame</b> olarak kaydeder. Varsayılan: <code>sep=","</code>, <code>dec="."</code>, <code>header=TRUE</code>.')
r('# Alman formatı (3,5 ; 2,1):\n# d <- read.csv("Datei.csv", sep = ";", dec = ",")', 'Dosyada <b>; ayraç</b> ve <b>virgüllü ondalık</b> varsa (Almanya formatı) bu iki argümanı mutlaka yaz. Yoksa hata: „mehr Spalten als Spaltennamen“.', False)
r('# d <- read.csv2("Datei.csv")', '<code>read.csv2</code> = <code>sep=";", dec=","</code> varsayılan olan kısayol.', False)
r('# d <- read.table("Datei.txt", header = TRUE, sep = "\\t")', '<code>.txt</code> veya sekmeyle ayrılmış dosyalar için. <code>header=TRUE</code>: ilk satır sütun adları.', False)
r('head(d, 3)', 'İlk satırları gösterir (varsayılan 6). Okumanın doğru olduğunu <b>kontrol et</b>.')
r('str(d)', '<b>Yapı</b>: kaç satır/sütun, her sütunun tipi (num, int, chr). Sayılar <code>chr</code> görünüyorsa <code>dec</code> yanlış!')
r('dim(d); nrow(d); ncol(d)', 'Boyut: (satır, sütun) · satır sayısı · sütun sayısı.')
r('names(d)', 'Sütun (değişken) adları.')
r('summary(d$Dauer)', 'Min, 1. çeyrek, medyan, ortalama, 3. çeyrek, max – tek seferde.')

# ------------------------------------------------------------------ 2
sec('2 · Datentypen und Umwandlung', '„Welchen Datentyp hat die Variable?“ sorusu için. Cevap cümlesi: „Die Variable … ist vom Typ …“.')
r('class(d$Mensa); class(d$Dauer); class(d$Wartezeit)', 'R\'deki <b>sınıf</b>: character (metin), integer (tam sayı), numeric (ondalıklı), factor (kategori).')
r('typeof(d$Dauer)', '<b>Depolama tipi</b> (integer/double/character). Altklausur\'da <code>typeof</code> soruldu.')
r('is.numeric(d$Dauer); is.character(d$Mensa)', 'Tip kontrolü: TRUE/FALSE döner.')
r('as.numeric("3.5"); as.character(12)', 'Tip <b>dönüştürme</b>. Sayı metin olarak okunduysa <code>as.numeric</code>.')
r('d$Mensa <- factor(d$Mensa)\nlevels(d$Mensa)', 'Metni <b>kategorik değişkene (factor)</b> çevirir; <code>levels</code> kategorileri gösterir.')
r('z <- factor(c("gut","schlecht","gut"), levels = c("schlecht","gut"), ordered = TRUE)\nz', '<b>Ordinal</b> değişken: sıralı faktör (<code>ordered=TRUE</code>, sıra <code>levels</code> ile).')

# ------------------------------------------------------------------ 3
sec('3 · Auf Daten zugreifen, filtern, sortieren', 'Bir sütunu veya belirli satırları seçmek – neredeyse her soruda lazım.')
r('d$Dauer[1:5]', '<code>$</code> ile <b>bir sütunu</b> seç; <code>[1:5]</code> ile ilk 5 değer.')
r('d[2, ]; d[1:2, c("Mensa", "Dauer")]', '<code>d[satır, sütun]</code>: virgülden önce satır, sonra sütun. Boş = hepsi.')
r('nord <- d$Dauer[d$Mensa == "Nord"]\nlength(nord); mean(nord)', 'Koşulla seçme: sadece Mensa = „Nord“ olanların Dauer değerleri. <code>==</code> (iki eşittir!).')
r('t1 <- subset(d, Mensa == "Nord" & Dauer > 40)\nnrow(t1)', '<code>subset</code>: koşula uyan <b>satırlar</b>. <code>&</code> = ve, <code>|</code> = veya.')
r('which(d$Wartezeit > 15)', 'Koşulu sağlayan <b>satır numaraları</b>.')
r('which.max(d$Dauer); d$Person[which.max(d$Dauer)]', 'En büyük değerin <b>konumu</b> (ve o kişinin adı). <code>which.min</code> en küçük.')
r('sort(d$Gerichte)[1:10]; sort(d$Dauer, decreasing = TRUE)[1:3]', 'Sıralar (küçükten büyüğe; <code>decreasing=TRUE</code> tersten).')
r('head(d[order(d$Dauer), ], 3)', 'Bütün tabloyu bir sütuna göre sıralar.')
r('d$lang <- ifelse(d$Dauer > 30, "lang", "kurz")\ntable(d$lang)', '<b>Yeni sütun</b> oluştur; <code>ifelse(koşul, evet, hayır)</code>.')
r('d$Klasse <- cut(d$Dauer, breaks = c(10, 20, 30, 40, 50), right = FALSE)\ntable(d$Klasse)', 'Sayıları <b>sınıflara</b> ayırır. <code>right=FALSE</code> → [10,20) sol kapalı.')
r('x <- c(2, NA, 5)\nis.na(x); sum(is.na(x)); mean(x, na.rm = TRUE)', 'Eksik değer (NA): bul, say, hesaplarda <code>na.rm=TRUE</code> ile atla.')
r('unique(d$Mensa); "Nord" %in% d$Mensa', 'Farklı değerler · bir değer içinde var mı?')

# ------------------------------------------------------------------ 4
sec('4 · Vektoren, Rechnen, Mengen', 'Temel hesaplar. log = doğal logaritma (ln)!')
r('x <- c(4, 1, 3); y <- 1:5; seq(0, 1, by = 0.25); rep(2, 3)', '<code>c()</code> vektör kurar · <code>1:5</code> ardışık sayılar · <code>seq</code> adımlı dizi · <code>rep</code> tekrar.')
r('sum(x); prod(x); length(x); cumsum(x)', 'Toplam · <b>çarpım</b> (Likelihood!) · eleman sayısı · kümülatif toplam.')
r('max(x); min(x); range(x)', 'En büyük · en küçük · ikisi birden.')
r('sqrt(16); exp(1); log(exp(2)); log(100, base = 10); abs(-3)', 'Karekök · e üzeri · <b>log = ln</b> · 10 tabanlı log · mutlak değer.')
r('choose(10, 2); factorial(4)', 'Binom katsayısı \\(\\binom{10}{2}\\) · faktöriyel 4!.')
r('A <- 3:6; B <- c(2, 4, 6)\nunion(A, B); intersect(A, B); setdiff(A, B); is.element(6, B)', 'Kümeler: birleşim ∪ · kesişim ∩ · fark A\\B · eleman mı? (Testat 0).')

# ------------------------------------------------------------------ 5
sec('5 · Häufigkeiten und Kontingenztafeln', 'Kategorik değişkenler için.')
r('table(d$Mensa)', '<b>Mutlak frekanslar</b> (kaç kez).')
r('round(prop.table(table(d$Mensa)), 3)', '<b>Göreli frekanslar</b> (oranlar, toplamı 1).')
r('tab <- table(d$Mensa, d$Typ)\ntab', 'İki değişkenli <b>Kontingenztafel</b> (satır × sütun).')
r('addmargins(tab)', 'Satır ve sütun <b>toplamlarını</b> ekler.')
r('round(prop.table(tab, margin = 1), 3)', '<b>Satır içi oranlar</b> (koşullu): her Mensa\'da Student/Mitarbeiter oranı. <code>margin=2</code> sütun içi.')

# ------------------------------------------------------------------ 6
sec('6 · Lage- und Streuungsmaße', 'Dikkat: <code>var()</code> ve <code>sd()</code> \\(n-1\\) ile böler (düzeltilmiş). Empirik varyans istenirse çevir!')
r('mean(d$Dauer); median(d$Dauer)', 'Aritmetik ortalama · medyan.')
r('names(which.max(table(d$Gerichte)))', '<b>Modus</b> (en sık değer) – R\'de hazır komut yok, böyle bulunur.')
r('var(d$Dauer); sd(d$Dauer)', '<b>Düzeltilmiş</b> (unverzerrte) varyans \\(s_*^2\\) ve std. sapma (\\(n-1\\) ile).')
r('n <- length(d$Dauer)\nvar(d$Dauer) * (n - 1) / n\nmean((d$Dauer - mean(d$Dauer))^2)', '<b>Empirik</b> varyans \\(s^2\\) (\\(n\\) ile böler) – iki yol, aynı sonuç.')
r('quantile(d$Dauer, probs = c(0.25, 0.5, 0.75))', 'Kantiller (çeyrekler). Derslerdeki tanım için <code>type = 2</code> eklenebilir.')
r('quantile(d$Dauer, 0.9, type = 2)', '<code>type=2</code>: ders tanımı (nα tam sayıysa iki değerin ortalaması).')
r('IQR(d$Dauer); diff(range(d$Dauer))', 'Çeyrekler açıklığı · değişim aralığı (Spannweite).')
r('tapply(d$Dauer, d$Mensa, mean)', '<b>Gruplara göre</b> ortalama (her Mensa için). Başka fonksiyon da olur (median, sd…).')
r('aggregate(Dauer ~ Mensa, data = d, FUN = mean)', 'Aynısı, tablo hâlinde.')

# ------------------------------------------------------------------ 7
sec('7 · Zusammenhang zweier Merkmale', 'Kovaryans ve korelasyon; R\'nin <code>cov</code>\'u da \\(n-1\\) ile böler.')
r('cov(d$Dauer, d$Wartezeit); cor(d$Dauer, d$Wartezeit)', 'Kovaryans (\\(n-1\\)) · <b>Bravais-Pearson korelasyonu</b> r (−1…1).')
r('cor(d$Dauer, d$Wartezeit, method = "spearman")', '<b>Spearman sıra korelasyonu</b>.')
r('n <- nrow(d); cov(d$Dauer, d$Wartezeit) * (n - 1) / n', 'Empirik kovaryans (\\(n\\) ile).')
r('chisq.test(tab, correct = FALSE)$statistic\nchisq.test(tab)$expected', 'Kontingenztafel için \\(\\chi^2\\) değeri ve bağımsızlıkta <b>beklenen frekanslar</b>.')

# ------------------------------------------------------------------ 8
sec('8 · Grafiken (speichern und hochladen)', 'Başlıkta (<code>main</code>) görev harfi, Matrikelnummer ve Platznummer olmalı; eksenleri adlandır.')
r('pdf("Histogramm.pdf")\nhist(d$Dauer, breaks = c(10, 20, 30, 40, 50), right = FALSE, freq = FALSE,\n     main = "Aufgabe e) 12345678 Platz 7", xlab = "Dauer (min)", ylab = "Dichte")\nlines(density(d$Dauer))\ndev.off()', '<b>Histogram</b>: <code>breaks</code> sınıf sınırları, <code>right=FALSE</code> sol kapalı, <code>freq=FALSE</code> yoğunluk (alan = 1). <code>lines(density())</code> çekirdek yoğunluğu ekler. <code>pdf()</code>…<code>dev.off()</code> dosyaya kaydeder.')
r('png("Boxplot.png")\nboxplot(Dauer ~ Mensa, data = d, main = "Aufgabe f)", ylab = "Dauer")\ndev.off()', '<b>Boxplot</b>, gruplara göre (<code>y ~ grup</code>). <code>png()</code> PNG olarak kaydeder.')
r('pdf("Scatter.pdf")\nplot(d$Dauer, d$Wartezeit, xlab = "Dauer", ylab = "Wartezeit", main = "Streudiagramm", pch = 16)\nabline(lm(Wartezeit ~ Dauer, data = d), col = "red")\ndev.off()', '<b>Saçılım grafiği</b> + regresyon doğrusu (<code>abline(lm(...))</code>).')
r('pdf("Balken.pdf")\nbarplot(table(d$Mensa), main = "Mensa", ylab = "Anzahl")\ndev.off()', '<b>Çubuk grafik</b> (kategorik veri).')
r('pdf("ECDF.pdf")\nplot(ecdf(d$Gerichte), main = "Empirische Verteilungsfunktion")\ndev.off()', '<b>Empirik dağılım fonksiyonu</b> \\(\\hat F(x)\\) çizimi.')
r('pdf("Dichte.pdf")\nhist(d$Wartezeit, freq = FALSE, main = "Wartezeit")\ncurve(dexp(x, rate = 1 / mean(d$Wartezeit)), add = TRUE, col = "blue")\ndev.off()', 'Histogram üstüne <b>teorik yoğunluk eğrisi</b> (<code>curve(..., add=TRUE)</code>).')

# ------------------------------------------------------------------ 9
sec('9 · Verteilungen: d / p / q / r', '<b>d</b> = yoğunluk/olasılık \\(P(X=k)\\) · <b>p</b> = \\(P(X\\le x)\\) · <b>q</b> = kantil · <b>r</b> = rastgele sayı.')
r('dbinom(2, size = 10, prob = 0.2)', 'Binom: \\(P(X=2)\\), \\(X\\sim B(10;0.2)\\).')
r('pbinom(1, 10, 0.2); 1 - pbinom(1, 10, 0.2)', '\\(P(X\\le1)\\) · \\(P(X\\ge2)=1-P(X\\le1)\\) (<b>k−1</b>!).')
r('dpois(0, lambda = 3); ppois(2, 3); 1 - ppois(2, 3)', 'Poisson: \\(P(X=0)\\) · \\(P(X\\le2)\\) · \\(P(X>2)\\).')
r('pnorm(76, mean = 70, sd = 4); 1 - pnorm(66, 70, 4); qnorm(0.975)', 'Normal: \\(P(X\\le76)\\) · \\(P(X>66)\\) · \\(z_{0.975}=1.96\\). <b>sd</b> = σ (varyans değil!).')
r('pexp(2, rate = 0.25); 1 - pexp(6, 0.25); qexp(0.5, 0.25)', 'Üstel: \\(P(T\\le2)\\) · \\(P(T>6)\\) · medyan. <code>rate</code> = λ = 1/ortalama.')
r('punif(9, min = 2, max = 12); qt(0.95, df = 15); qchisq(0.95, df = 1)', 'Düzgün · t kantili \\(t_{15;0.95}\\) · χ² kantili.')
r('1 - pt(2, df = 15); 2 * (1 - pnorm(2))', 't için sağ kuyruk · iki taraflı p-değeri (z = 2).')

# ------------------------------------------------------------------ 10
sec('10 · Simulation', 'Rastgele deney; <code>set.seed</code> ile sonuç tekrarlanabilir olur.')
r('set.seed(123)\nsample(1:6, 5, replace = TRUE)', 'Zar 5 kez (<b>geri koyarak</b>). <code>set.seed</code> her seferinde aynı sonucu verir.')
r('set.seed(123)\nw <- matrix(sample(c(0, 1), 3 * 1000, replace = TRUE), nrow = 3)\nmean(colSums(w) == 3)', '1000 deneyde 3 yazı tura; „3 tura“ oranı ≈ 1/8 (Testat 3).')
r('set.seed(1)\nx <- rbinom(10000, size = 5, prob = 0.25)\nmean(x == 2)', 'Binom\'dan 10000 sayı, \\(P(X=2)\\) tahmini (Testat 4).')

# ------------------------------------------------------------------ 11
sec('11 · Likelihood und Maximum-Likelihood (Teil-B-Klassiker)', 'Altklausur B: Poisson-Likelihood (λ = 20) ve λ = 17…23 arasında en iyisini bulmak.')
r('x <- d$Gerichte\nL <- prod(dpois(x, lambda = 1.5)); L', '<b>Likelihood</b> = tüm gözlemlerin olasılıklarının <b>çarpımı</b>.')
r('logL <- sum(dpois(x, lambda = 1.5, log = TRUE)); logL', '<b>Log-Likelihood</b> = log-olasılıkların <b>toplamı</b> (çok küçük sayılarda daha iyi).')
r('Lfun <- function(lambda) prod(dpois(x, lambda))\nLfun(1.5)', 'Likelihood\'u <b>fonksiyon</b> olarak tanımla.')
r('grid <- seq(1, 2, by = 0.1)\nwerte <- sapply(grid, Lfun)\ngrid[which.max(werte)]', '<b>Grid arama</b>: her λ için L hesapla, en büyüğün λ\'sı = ML tahmini.')
r('optimize(function(l) sum(dpois(x, l, log = TRUE)), interval = c(0.1, 5), maximum = TRUE)$maximum\nmean(x)', '<code>optimize(..., maximum=TRUE)</code>: sayısal maksimum. Poisson\'da kontrol: \\(\\hat\\lambda=\\bar x\\).')
r('1 / mean(d$Wartezeit)', 'Üstel dağılım ML: \\(\\hat\\lambda=1/\\bar x\\) (kontrol için).')

# ------------------------------------------------------------------ 12
sec('12 · Konfidenzintervalle', 'Elle formül ya da <code>t.test()$conf.int</code>.')
r('x <- d$Dauer; n <- length(x)\nmean(x) + c(-1, 1) * qnorm(0.975) * 6 / sqrt(n)', 'σ <b>biliniyor</b> (örn. σ = 6): \\(\\bar x\\pm z_{0.975}\\,\\sigma/\\sqrt n\\).')
r('mean(x) + c(-1, 1) * qt(0.975, df = n - 1) * sd(x) / sqrt(n)', 'σ <b>bilinmiyor</b>: t kantili ve <code>sd</code>.')
r('t.test(x, conf.level = 0.95)$conf.int', 'Aynısı hazır: <code>t.test</code>\'in güven aralığı.')
r('p <- mean(d$Typ == "Student"); n <- nrow(d)\np + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / n)', '<b>Oran</b> için güven aralığı (Testat 6).')
r('s2 <- var(x)\nc((n - 1) * s2 / qchisq(0.975, n - 1), (n - 1) * s2 / qchisq(0.025, n - 1))', '<b>Varyans</b> için güven aralığı (χ²).')

# ------------------------------------------------------------------ 13
sec('13 · Hypothesentests', 'Karar her zaman: <b>p-value ≤ α → H₀ ret</b>. Cümle: „Da der p-Wert … kleiner als α = … ist, wird H₀ abgelehnt …“.')
r('t.test(d$Dauer, mu = 28, alternative = "greater")', '<b>t-Test</b>: \\(H_1:\\mu>28\\). <code>"less"</code> → <, <code>"two.sided"</code> (varsayılan) → ≠. Çıktıda t, df, <b>p-value</b>.')
r('tt <- t.test(d$Dauer, mu = 28, alternative = "greater")\nround(tt$p.value, 3); round(tt$statistic, 3)', 'Sadece p-değerini / test istatistiğini çekmek.')
r('qt(0.95, df = 79)', 'Ret bölgesi için kritik değer: \\(t\\ge t_{79;0.95}\\).')
r('z <- (mean(d$Dauer) - 28) / (6 / sqrt(80)); z; 1 - pnorm(z)', '<b>Gauß testi</b> elle (σ = 6 biliniyor): z ve sağ taraflı p-değeri.')
r('chisq.test(table(d$Mensa, d$Typ))', '<b>χ² bağımsızlık testi</b> (Kontingenztafel). p > 0.05 → bağımsızlık reddedilmez.')
r('chisq.test(table(d$Mensa), p = c(1/3, 1/3, 1/3))', '<b>χ² uyum testi</b>: gözlenen frekanslar verilen oranlara uyuyor mu?')
r('binom.test(9, 10, p = 0.5, alternative = "greater")', '<b>Kesin binom testi</b>: 10 denemede 9 başarı.')

# ------------------------------------------------------------------ 14
sec('14 · Lineare Regression', 'y ~ x: önce bağımlı değişken (y), sonra açıklayıcı (x).')
r('m <- lm(Wartezeit ~ Dauer, data = d)\ncoef(m)', 'KQ doğrusu: <b>a</b> (Intercept) ve <b>b</b> (eğim).')
r('summary(m)$r.squared', '<b>R²</b> (açıklanan varyans payı).')
r('summary(m)$coefficients', 'Katsayılar, std. hata, t değeri, <b>p-değeri</b> (eğim anlamlı mı?).')
r('predict(m, newdata = data.frame(Dauer = 40))', 'x = 40 için <b>tahmin</b> \\(\\hat y\\).')
r('head(resid(m), 3)', '<b>Artıklar</b> \\(e_i=y_i-\\hat y_i\\).')

# ------------------------------------------------------------------ 15
sec('15 · Runden und Ausgeben', 'Sınav: sonuçları <code>round(…, 3)</code> ile yuvarla ve tam cümle yaz.')
r('round(pi, 3); signif(123456, 2)', '3 ondalığa yuvarla · anlamlı basamak.')
r('format(1/3, nsmall = 5); sprintf("%.10f", pi)', 'Sabit sayıda ondalık gösterme.')
r('sprintf("%.99f", pi)', '<b>99 ondalık</b> (Altklausur B, „Yennefer-Zahl“) – <code>sprintf("%.99f", x)</code>.')
r('options(scipen = 999); 6.938e-131 > 0', 'Bilimsel gösterimi kapatır (<code>e-131</code> = \\(\\times10^{-131}\\)).')
r('paste("Mittelwert:", round(mean(d$Dauer), 3)); cat("n =", nrow(d), "\\n")', 'Metin + sayı birleştirme / yazdırma.')

# ------------------------------------------------------------------ 16
sec('16 · Fehlermeldungen und was zu tun ist', 'Hata alırsan panik yok – çoğu bu listede.')
r('# Fehler: mehr Spalten als Spaltennamen', '→ Ayraç yanlış: <code>read.csv(..., sep=";", dec=",")</code>.', False)
r('# Fehler: Datei kann nicht geöffnet werden / cannot open file', '→ Yanlış klasör: <code>setwd(path.expand("~"))</code>, <code>list.files()</code> ile kontrol.', False)
r('# Fehler: Objekt nicht gefunden / object not found', '→ Yazım hatası (büyük/küçük harf!) veya nesneyi henüz oluşturmadın.', False)
r('# Fehler: konnte Funktion nicht finden', '→ Komut adı yanlış yazıldı.', False)
r('# Warnung: Argument ist weder numerisch noch logisch: gebe NA zurück', '→ Sütun metin olarak okundu: <code>dec=","</code> unuttun ya da <code>as.numeric</code>.', False)
r('# Ergebnis NA', '→ Veride eksik değer: <code>mean(x, na.rm = TRUE)</code>.', False)


# ------------------------------------------------------------------ 17
sec('17 · Antwortsätze für ILIAS (abschreiben, Zahlen ersetzen)', 'Sayısal olmayan her cevap <b>tam cümle</b> olmalı. Sayılar 3 ondalık.')
r('# Datentyp', '„Die Variable <i>Mensa</i> ist vom Typ <i>character</i>, die Variable <i>Dauer</i> vom Typ <i>integer</i> (ganzzahlig numerisch).“', False)
r('# Mittelwert / Standardabweichung', '„Das arithmetische Mittel der Variable <i>Dauer</i> beträgt 30.637. Die (unverzerrte) Standardabweichung beträgt 7.651.“', False)
r('# Gruppenvergleich (tapply)', '„Die mittlere Dauer ist in der Mensa <i>Zentral</i> mit 31.903 Minuten am höchsten.“', False)
r('# Likelihood', '„Die Likelihood aller Beobachtungen unter der Annahme λ = 20 beträgt L(λ = 20) = 6.938 · 10⁻¹³¹.“', False)
r('# ML-Schätzer (Grid / optimize)', '„Das Maximum der Likelihood liegt bei λ = 22; dies ist der ML-Schätzer im betrachteten Bereich.“', False)
r('# Test abgelehnt', '„Da der p-Wert (0.001) kleiner als α = 0.05 ist, wird H₀ abgelehnt. Es ist statistisch abgesichert, dass die mittlere Dauer größer als 28 Minuten ist.“', False)
r('# Test nicht abgelehnt', '„Da der p-Wert (0.094) größer als α = 0.05 ist, kann H₀ nicht abgelehnt werden. Ein Zusammenhang zwischen Mensa und Typ kann nicht nachgewiesen werden.“', False)
r('# Konfidenzintervall', '„Das 95 %-Konfidenzintervall für den Erwartungswert lautet [28.935; 32.340]. Bei wiederholter Ziehung überdecken ca. 95 % solcher Intervalle den wahren Mittelwert.“', False)
r('# Regression', '„Steigt die Dauer um eine Minute, steigt die Wartezeit im Mittel um 0.048 Minuten. R² = 0.008: Das Modell erklärt kaum Varianz.“', False)

# ------------------------------------------------------------------ 18
sec('18 · Altklausur Teil B (04.03.2022) → welcher Abschnitt?', 'Gerçek sınavın her alt sorusu bu listenin hangi bölümüne denk geliyor.')
r('# a) Arbeitsverzeichnis setzen', '→ Abschnitt 0: <code>setwd(path.expand("~"))</code>, <code>getwd()</code>', False)
r('# b) Datensatz einlesen', '→ Abschnitt 1: <code>d &lt;- read.csv("WitcherData1.csv", sep=",", dec=".", header=TRUE)</code>, <code>head(d)</code>', False)
r('# c) Datentyp von Variablen', '→ Abschnitt 2: <code>typeof()</code> / <code>class()</code> + Satz', False)
r('# d) Mittelwert, Standardabweichung', '→ Abschnitt 6: <code>round(mean(d$x), 3)</code>, <code>round(sd(d$x), 3)</code>', False)
r('# e) Histogramm mit Klassen, links geschlossen', '→ Abschnitt 8: <code>hist(..., breaks=c(...), right=FALSE, freq=FALSE, main=..., xlab=...)</code> in <code>pdf()</code>…<code>dev.off()</code>', False)
r('# f) Likelihood für λ = 20 (Poisson)', '→ Abschnitt 11: <code>prod(dpois(d$x, 20))</code>', False)
r('# g) ML-Schätzer auf einem Gitter (17 … 23)', '→ Abschnitt 11: <code>grid &lt;- 17:23; werte &lt;- sapply(grid, Lfun); grid[which.max(werte)]</code>', False)
r('# h) Zahl mit 99 Nachkommastellen', '→ Abschnitt 15: <code>sprintf("%.99f", x)</code>', False)

# ======================================================================= R ausführen
def run_all():
    os.makedirs(WD, exist_ok=True)
    shutil.copy(os.path.join(HERE, '..', 'uebungsdaten', 'Beispiel_Mensa.csv'), WD)
    L = ['invisible(Sys.setlocale("LC_ALL", "C.UTF-8"))', 'options(width = 72, warn = 1)', 'sink(stdout(), type = "message")']
    k = 0; idx = []
    for si, (t, intro, rows) in enumerate(S):
        for ri, (code, tr, run) in enumerate(rows):
            if not run: continue
            L.append('cat("@@B%d@@\\n")' % k)
            L.append('try(source(textConnection(r"---(%s)---"), echo = TRUE, max.deparse.length = Inf, prompt.echo = "> ", continue.echo = "+ ", spaced = FALSE, keep.source = TRUE))' % code)
            L.append('cat("@@E%d@@\\n")' % k)
            idx.append((si, ri, k)); k += 1
    open(os.path.join(WD, 'run.R'), 'w').write('\n'.join(L) + '\n')
    res = subprocess.run(['Rscript', 'run.R'], cwd=WD, capture_output=True, text=True)
    outs = {}
    for si, ri, k in idx:
        seg = res.stdout.split('@@B%d@@\n' % k, 1)[1].split('@@E%d@@' % k, 1)[0]
        if re.search(r'(^|\n)(Error|Fehler)', seg):
            raise SystemExit('R-Fehler in Abschnitt %s:\n%s' % (S[si][0], seg))
        outs[(si, ri)] = seg
    return outs

def esc_code(ln):
    i = ln.find('#')
    if i >= 0 and ln.count('"', 0, i) % 2 == 0:
        return html.escape(ln[:i]) + '<span class="c">' + html.escape(ln[i:]) + '</span>'
    return html.escape(ln)

def fmt(code, out):
    lines = []
    if out is None:
        lines = [esc_code(l) for l in code.split('\n')]
    else:
        for ln in out.rstrip('\n').split('\n'):
            if ln.startswith('> ') or ln.startswith('+ '):
                lines.append(esc_code(ln))
            else:
                lines.append('<span class="o">%s</span>' % html.escape(ln))
    return '<pre class="rb">%s</pre>' % '\n'.join(lines)

CSS = r'''<style>
@page{size:A4;margin:9mm 9mm 11mm}
.w{width:auto!important;padding:0!important}
body{background:#fff!important;font-size:10.6px!important;line-height:1.38!important}
h1{font-size:23px!important;color:#1e3a8a;margin:0 0 1mm!important}
.sub{color:#334155;margin-bottom:2mm}
.sec{background:#1e3a8a;color:#fff;font:800 13px Inter;padding:1.4mm 3mm;border-radius:6px 6px 0 0;margin-top:3mm;break-after:avoid}
.si{background:#e6ecf8;color:#0f1f4d;padding:1mm 3mm;font-size:10.3px;border:1px solid #c3cfeb;border-top:0;break-after:avoid}
table.cmd{width:100%;border-collapse:collapse;margin-bottom:1mm}
table.cmd td{border:1px solid #c3cfeb;padding:1mm 1.6mm;vertical-align:top}
table.cmd td.c{width:60%}
table.cmd td.t{background:#fbfcfe;color:#1d1d1f;font-family:Inter,Arial,sans-serif;font-size:10.4px}
table.cmd tr{break-inside:avoid}
pre.rb{margin:0;font:10px/1.32 "JetBrains Mono",monospace;white-space:pre-wrap;word-break:break-word;font-variant-ligatures:none;background:#0f1f4d;color:#fff;padding:1.2mm 2mm;border-radius:4px}
pre.rb .o{color:#bfdbfe}
pre.rb .c{color:#9ca3af}
code{font-family:"JetBrains Mono",monospace;font-size:.95em;background:#eef2fb;padding:0 2px;border-radius:2px;font-variant-ligatures:none}
.box{border:2px solid #1e3a8a;border-radius:8px;padding:2mm 3mm;margin:2mm 0}
.box h3{margin:0 0 1mm;color:#1e3a8a;font:800 13px Inter}
.toc{columns:2;font-size:10.5px}
</style>'''

def build():
    outs = run_all()
    h = [CSS, '<h1>R-Befehle für Teil B – komplett</h1><div class="sub">Jeder Befehl mit <b>türkischer Erklärung</b>, Beispiel und <b>echtem R-Output</b> (Datensatz <code>Beispiel_Mensa.csv</code>: 80 Personen, Variablen Person, Mensa, Typ, Dauer, Gerichte, Wartezeit). Dunkle Zeilen: was du tippst · hellblau: was R antwortet · grau: Kommentar.</div>']
    h.append('<div class="box"><h3>Sınav akışı (60 dk, 45 P) – her alt soruda</h3>1) Kodu yaz, Strg+Enter ile çalıştır · 2) <b>Kod + çıktıyı</b> ILIAS\'taki kutuya kopyala · 3) Sonucu <code>round(…, 3)</code> ile yuvarla · 4) İkinci kutuya <b>tam Almanca cümle</b> („Der Mittelwert der Variable … beträgt …“) · 5) Scripti sık sık kaydet · Grafikleri <code>pdf()</code>/<code>png()</code> + <code>dev.off()</code> ile kaydet ve yükle.</div>')
    h.append('<div class="box"><h3>Inhalt</h3><div class="toc">' + ''.join(f'<div>{t}</div>' for t, _, _ in S) + '</div></div>')
    for si, (t, intro, rows) in enumerate(S):
        h.append(f'<div class="sec">{t}</div><div class="si">{intro}</div><table class="cmd">')
        for ri, (code, tr, run) in enumerate(rows):
            h.append(f'<tr><td class="c">{fmt(code, outs.get((si, ri)) if run else None)}</td><td class="t">{tr}</td></tr>')
        h.append('</table>')
    open(OUT, 'w').write('\n'.join(h))
    print(OUT)

if __name__ == '__main__':
    build()
