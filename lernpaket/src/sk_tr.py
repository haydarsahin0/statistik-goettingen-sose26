r"""Türkische Erklärschicht: LERN_TR (Abschnitt → HTML), VERST_TR (Kartentitel → HTML)."""
LERN_TR = {}
VERST_TR = {}

LERN_TR["1"] = r"""
<p><b>Olasılık nedir?</b> 0 ile 1 arasında bir sayı: Bir şeyin <i>uzun vadede</i> ne sıklıkla olduğunu söyler. P = 0.25 → çok kez tekrar edersen yaklaşık her 4 denemede bir.</p>
<p><b>Olaylar = kümeler.</b> Ω (Ergebnisraum) olabilecek her şeyin listesidir (zar: {1,…,6}). Bir olay bu listenin bir parçasıdır: „çift“ = {2, 4, 6}.</p>
<table class="tab trtab"><tr><th>İşaret</th><th>Türkçe</th><th>Sınavdaki Almanca</th></tr>
<tr><td>\(A\cap B\)</td><td>A <b>ve</b> B (ikisi birden)</td><td>und, sowohl … als auch</td></tr>
<tr><td>\(A\cup B\)</td><td>A <b>veya</b> B (en az biri)</td><td>oder, mindestens eines</td></tr>
<tr><td>\(\bar A\)</td><td>A <b>değil</b></td><td>nicht, Gegenereignis, Komplement</td></tr>
<tr><td>\(A\setminus B=A\cap\bar B\)</td><td>A <b>ama B değil</b></td><td>A, aber nicht B</td></tr>
<tr><td>\(\bar A\cap\bar B\)</td><td><b>hiçbiri</b></td><td>weder … noch</td></tr>
<tr><td>\(|A|\)</td><td>A'nın <b>eleman sayısı</b></td><td>Mächtigkeit</td></tr>
<tr><td>\(P(A|B)\)</td><td>B olduğunu <b>bilerek</b> A'nın olasılığı</td><td>A, wenn/gegeben B</td></tr></table>
<p><b>Koşullu olasılık = dünya küçülür.</b> B'nin olduğunu biliyorsan artık sadece B'deki sonuçlar vardır. Zar örneği: B = {1, 2, 3}, A = çift → küçük dünyada sadece 2 çift → \(P(A|B)=\frac13\).</p>
<p><b>Bağımsız</b> = B'yi bilmek A'nın olasılığını değiştirmiyor: \(P(A\cap B)=P(A)\cdot P(B)\) ise bağımsızdır. <b>Dikkat:</b> „ayrık“ (disjunkt, kesişimi boş) ile „bağımsız“ aynı şey değil!</p>
<p><b>Ağaç diyagramı:</b> 1. basamak = grup/neden (\(A_1, A_2,\dots\)), 2. basamak = sonuç (B / \(\bar B\)). <b>Yol üstünde çarp, yolları topla.</b>
Toplam olasılık = B'ye giden bütün yolların toplamı. Bayes = „benim yolum ÷ B'ye giden bütün yollar“.</p>"""

VERST_TR.update({
"Ein Lösungskästchen richtig füllen": r"Puan şöyle verilir: <b>formül → sayıları yerleştir → sonuç</b>. Sadece „0.6“ yazar ve yanlış hesaplarsan 0 puan alırsın. Formülü yazarsan hesap hatasında bile kısmi puan gelir.",
"Text in Mengen-Sprache übersetzen": r"Önce Venn'in 4 bölgesini doldur: ikisi birden 0.15 → sadece A = 0.5 − 0.15 = 0.35 → sadece B = 0.4 − 0.15 = 0.25 → hiçbiri = 1 − 0.35 − 0.25 − 0.15 = 0.25. Sonra her soru bir toplama işlemi: „weder…noch“ = hiçbiri, „genau eines“ = sadece A + sadece B, „Kaffee aber kein Kuchen“ = sadece A.",
"Mengen und Mächtigkeiten im Laplace-Experiment": r"Laplace = her sayı eşit olasılıklı → olasılık = <b>saymak</b>. 1) Tümleyenleri yaz: B̄ = B'de olmayanlar. 2) Kesişim = iki listede de olanlar; birleşim = ikisini birleştir, tekrarı bir kez yaz. 3) |…| = eleman sayısı. 4) P(A|B̄): yeni dünya B̄ (6 sayı), bunların 3'ü A'da → 3/6.",
"Zwei Würfel: Abzählen mit 36 Paaren": r"İki zar → 6 × 6 = 36 <b>sıralı</b> çift. (2,6) „birinci zar 2, ikinci 6“ demek; (6,2) başka bir sonuç. Toplamı 8 olanları tek tek yaz: (2,6), (3,5), (4,4), (5,3), (6,2) → 5/36. 6×6'lık tablo çizip işaretlemek en güvenli yol.",
"Rechenregeln: fehlende Wahrscheinlichkeiten finden": r"Toplama kuralı \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\): Kesişim hem P(A)'da hem P(B)'de var, iki kez sayılmasın diye bir kez çıkarılır. Üçünü biliyorsan dördüncüyü yalnız bırak. Sonra bağımsızlığı çarpımla test et: \(P(A)\cdot P(B)=0.2=P(A\cap B)\) → bağımsız.",
"Bedingte Wahrscheinlichkeit und Komplement": r"Hemen her koşullu olasılık sorusu <b>kesişimle</b> başlar: \(P(A\cap B)=P(A|B)\cdot P(B)=0.4\cdot0.5=0.2\). \(P(A|\bar B)\) için A'nın B <i>dışındaki</i> kısmı: 0.3 − 0.2 = 0.1, bunu yeni dünyaya \(P(\bar B)=0.5\) böl → 0.2. \(P(B|A)\) farklı bir soru: payda P(A) olur.",
"Unabhängigkeit von Ereignissen prüfen": r"Bağımsızlık gözle görülmez, <b>hesaplanır</b>: \(P(A\cap B)\) ile \(P(A)\cdot P(B)\)'yi bulup karşılaştır. A = {1,2,3,4} içinde çiftlerin oranı 2/4 = 1/2, Ω'daki oranla aynı → „çift“ bilgisi A'yı değiştirmez → bağımsız. C ile A için 0.1 ≠ 0.12 → bağımlı.",
"Satz der totalen Wahrscheinlichkeit (mit fehlendem Anteil)": r"Gecikme üç yoldan gelir (Fahrer 1, 2, 3). Her yol: „şoförün payı × şoförün gecikme oranı“. Önce eksik payı bul: 1 − 0.5 − 0.3 = 0.2. Sonra topla: 0.05 + 0.06 + 0.01 = 0.12. Kontrol: sonuç en küçük (0.05) ile en büyük (0.2) oran arasında olmalı.",
"Satz von Bayes: Rückschluss auf die Ursache": r"Bayes şu soruya cevap verir: Sonucu gördük (gecikti), <b>nereden</b> geldi? „Gecikti“de biten tüm yollar 0.12. Bunlardan Fahrer 2 yolu 0.06 → 0.06 / 0.12 = 0.5. Kısaca: <b>benim yolum ÷ bütün uygun yollar</b>.",
"Bayes im Probeklausur-Format (Lernstrategien)": r"Dikkat, yön: „Geçenlerin %70'i düzenli çalışıyor“ = \(P(S_1|B)=0.7\) (\(P(B|S_1)\) değil!). Aynı koşul içinde kalan pay: \(P(S_3|B)=1-0.7-0.2=0.1\). \(P(S_3)\): iki yol (B ve B̄ üzerinden) toplanır. (c) „en az biri“ → her zaman 1 − „hiçbiri“ = \(1-0.6^8\).",
"Medizinischer Test: Sensitivität, Spezifität, Prävalenz": r"Sensitivität = hastaysa testin pozitif çıkması \(P(T|K)\). Spezifität = sağlıklıysa negatif \(P(\bar T|\bar K)\). Prävalenz = hastalık oranı \(P(K)\). 10 000 kişiyle düşün: 200 hasta → 190 pozitif; 9 800 sağlıklı → 980 yanlış pozitif. Pozitif olan 1 170 kişinin sadece 190'ı hasta → %16. Hastalık nadir olduğu için yanlış pozitif çok olur.",
"Ziehen ohne Zurücklegen (Kugeln)": r"„İkinci çekişte kazanmak“ = önce sarı, <b>sonra</b> mavi. Çarpım kuralı: P(sarı) · P(mavi | sarı çekildi). Geri koymadan → ikinci çekişte 19 top kalır (6 mavi). Geri koysaydın yine 20 top olurdu ve çekişler bağımsız olurdu.",
"„Mindestens einer“ über das Gegenereignis": r"„En az biri bozulur“ 12 ayrı durum demek (1, 2, …, 12 bozuk). Tersi „hiçbiri bozulmaz“ tek bir durum: \(0.95^{12}\). Kural: <b>en az biri = 1 − hiçbiri</b>. „Tam olarak biri“ için hangi parçanın bozulduğu önemsiz → 12 olasılık × \(0.05\cdot0.95^{11}\).",
"Fehlinterpretation: P(A|B) mit P(B|A) verwechselt": r"„Enfekte olanların yarısı aşılı“ = \(P(G|I)\). Aşılı birinin riski ise \(P(I|G)\): bambaşka bir referans grubu. Nüfusun %80'i aşılı olduğu için aşılılar sayıca çok enfekte olur. Asıl karşılaştırma: aşılılarda %3.1, aşısızlarda %12.5 → aşı koruyor.",
})

# ======================================================================
LERN_TR["2"] = r"""
<p><b>Rastgele değişken (Zufallsvariable) = şansa bağlı bir sayı.</b> Örnek: X = zarın sonucu, X = kazanç (€), X = bekleme süresi. Soru: X hangi değerleri alabilir ve her birinin olasılığı ne?</p>
<p><b>Kesikli (diskret):</b> sayılabilen değerler (0, 1, 2, …). Bir <b>tablo</b> verilir: her değerin olasılığı (Wahrscheinlichkeitsfunktion). Hepsi ≥ 0 ve toplamları tam 1.<br>
<b>Sürekli (stetig):</b> ölçülen değerler (2.371 dakika). Tek bir değerin olasılığı 0'dır. X bir <b>yoğunluk</b> (Dichte) f(x) ile tanımlanır: <b>olasılık = eğrinin altındaki alan</b>. 1 kg kum düşün, x ekseni üzerine yayılmış: [a, b] üzerindeki kum miktarı \(P(a\le X\le b)\).</p>
<p><b>Dağılım fonksiyonu</b> \(F(x)=P(X\le x)\) = „x'e kadar her şeyi topla“. 0'dan 1'e yükselir. Kesiklide merdiven (her basamak = o değerin olasılığı), süreklide yumuşak eğri (yoğunluğun integrali).</p>
<p><b>Beklenen değer E(X)</b> = uzun vadedeki ortalama. Zar: 3.5 (hiç 3.5 gelmez ama ortalama budur). Hesap: <b>her değer × olasılığı, hepsini topla</b> (süreklide integral).<br>
<b>Varyans Var(X)</b> = ortalamadan ne kadar saçıldığı (risk). Pratikte: \(Var(X)=E(X^2)-E(X)^2\) (Verschiebungssatz).</p>
<p><b>Kurallar:</b> X'e sabit eklersen (+5 €) ortalama kayar, saçılım değişmez. X'i a ile çarparsan ortalama a ile, <b>varyans a² ile</b> çarpılır (varyansın birimi karedir). Bağımsız X, Y için \(Var(X+Y)=Var(X)+Var(Y)\); \(Var(X-Y)\) de <b>toplanır</b>.</p>
<p><b>İntegral hatırlatma:</b> \(\int x^n dx=\frac{x^{n+1}}{n+1}\); \(\int_a^b g\,dx=G(b)-G(a)\). Örnek: \(\int_0^2 3x^2dx=[x^3]_0^2=8\). G(a) negatifse parantez koy!</p>
<p><b>Sık hatalar:</b> ① \(E(X^2)\)'de olasılıkları da karelemek (sadece x karelenir). ② \(Var(aX)=a\,Var(X)\) yazmak (doğrusu a²). ③ Kesiklide \(P(X<2)\) ile \(P(X\le2)\)'yi aynı sanmak.</p>"""

VERST_TR.update({
"Wahrscheinlichkeitsfunktion und Träger aufstellen": r"Zar 1…6 gelir, her biri 1/6. Kazanç = çıkan sayı − 2 € → 1 → −1 €, 2 → 0 €, …, 6 → 4 €. Olasılıklar aynen taşınır. Träger = olası kazançların listesi {−1,…,4}. Fonksiyonu yazarken „0 sonst“ (diğer durumlarda 0) eklemeyi unutma. E(X) = 3.5 − 2 = 1.5.",
"Konstante c bestimmen, dann E(X) und Var(X)": r"Olasılıkların toplamı 1 olmalı, çünkü X mutlaka bir değer alır: c·1 + c·4 + c·9 = 14c = 1 → c = 1/14. Sonra normal tablo: P(1) = 1/14, P(2) = 4/14, P(3) = 9/14. E(X) = Σ x·P, E(X²) = Σ x²·P, Var = E(X²) − E(X)². Kesirlerle çalışmak sonucu kesin tutar.",
"Erwartungswert und Varianz aus einer Tabelle": r"Sütunları x, P, x·P, x²·P olan bir tablo kur. 3. sütunun toplamı E(X) = 1.9, 4. sütunun toplamı E(X²) = 5.1. Var = 5.1 − 1.9² = 1.49, sd = √1.49 = 1.221. Kontrol: varyans asla negatif olmaz.",
"Wahrscheinlichkeiten mit der Verteilungsfunktion (diskret)": r"F(x) = x dahil o noktaya kadar olan olasılıkların toplamı: 0.1, 0.4, 0.8, 1. F sadece taşıyıcı noktalarında (Träger) atlar; 2 ile 4 arasında sabit kalır. Her soruyu „≤“ şekline çevir: „< 2“ = „≤ 1“ → 0.4; „≥ 2“ = 1 − F(1) = 0.6; „1 < X ≤ 4“ = F(4) − F(1) = 0.6. 3 taşıyıcıda olmadığı için P(X = 3) = 0.",
"Verteilungsfunktion lesen und E(g(X)) berechnen": r"Merdivenin basamak yükseklikleri tek tek olasılıklardır: 1'de 0.3, 2'de 0.5, 3'te kalan 0.2 → „?“ = 0.3 + 0.5 = 0.8. E(log X) için E(X)'i log'a koymazsın: <b>her değer için</b> log(x)·P(X = x) hesaplayıp toplarsın. log1 = 0 olduğu için ilk terim düşer.",
"Stetige Dichte: c bestimmen und prüfen": r"Kesiklideki „toplam = 1“ kuralının sürekli karşılığı „alan = 1“. f sadece [2, 3]'te sıfırdan farklı, o yüzden integrali yalnızca orada al: ∫c(x − 2)dx = c/2 = 1 → c = 2. Kontrol: genişliği 1, yüksekliği c olan bir üçgenin alanı c/2.",
"Stetige Zufallsvariable: E(X) und Var(X) per Integral": r"Toplam yerine integral: E(X) = ∫x·f(x)dx = ∫(2x² − 4x)dx. Önce çarp, sonra integral al: [⅔x³ − 2x²] → 3'te 0, 2'de −8/3 → 0 − (−8/3) = 8/3. E(X²) için x²·f(x)'in integrali alınır. Var = 43/6 − (8/3)² = 1/18. Eksi işaretli terimlerde parantez kullan!",
"Verteilungsfunktion herleiten, Wahrscheinlichkeiten, Median": r"F(x) = en soldan x'e kadar olan alan. 2'nin solunda 0, 3'ün sağında 1. Arada: ∫₂ˣ 2(t − 2)dt = (x − 2)². İntegral değişkenine t diyoruz çünkü x üst sınır. Olasılıklar: P(X > 2.5) = 1 − F(2.5). Medyan: F(x) = 0.5 → x = 2 + √0.5.",
"Stückweise definierte Dichte: Erwartungswert": r"Yoğunluk iki formülden oluşuyorsa integrali kırılma noktasından (y = 2) ikiye böl. Her parçada kendi formülünü kullan, sonuçları topla: 4/9 + 20/9 = 8/3. Önce toplam alanın 1 olduğunu kontrol et (1/3 + 2/3).",
"Rechenregeln: lineare Transformation und Summen": r"Beklenen değer: çarpanlar ve toplamlar doğrudan geçer → 3·4 − 2·1 + 5 = 15. Varyans: sabit (+5) düşer, çarpanlar <b>karesiyle</b> çıkar → 9·2 + 4·3 = 30. (−2)² = 4 olduğu için eksi de pozitife döner. sd = √30.",
"Rückwärts rechnen mit den Rechenregeln (Tutorium-Typ)": r"Kuralı tek bilinmeyenli bir denklem olarak yaz: 8.5 = 0.5·3 + E(Y) → E(Y) = 7. Varyansta bağımsızlık sayesinde kovaryans terimi düşer: 0.25·1 + 1 = 1.25. Kovaryans verilirse 2·a·b·Cov eklenir (2·0.5·1·0.4 = 0.4 → 1.65).",
"Gemeinsame Wahrscheinlichkeitsfunktion: Rand und bedingte Verteilung": r"Bu tablo Tag 1'deki çapraz tabloyla aynı mantıkta, sadece sıklık yerine olasılık var. Marjinal (Rand) = satır ve sütun toplamları. Koşullu = ilgili satırı/sütunu al ve kenar toplamına bölerek toplamını 1 yap. Bağımsızlık için <b>her hücre</b> = satır toplamı × sütun toplamı olmalı; tek bir hücre tutmazsa bağımlıdır.",
"Kovarianz und Korrelation zweier Zufallsvariablen": r"Kovaryans, büyük X değerlerinin büyük Y değerleriyle birlikte gelip gelmediğini ölçer. E(XY) = Σ x·y·P: sadece x ≠ 0 ve y ≠ 0 olan hücreler katkı yapar → 0.25 + 2·0.2 = 0.65. Cov = 0.65 − 0.6·1.05 = 0.02. Korelasyon = Cov / (sd(X)·sd(Y)) ve −1 ile 1 arasında olur.",
"Gemeinsame Dichte: Randdichten und Unabhängigkeit": r"Marjinal yoğunluk = diğer değişkeni integralle yok et. f_X(x) için y üzerinden integral al (x sabit gibi davranır). f(x, y), sadece x'li bir fonksiyon ile sadece y'li bir fonksiyonun çarpımıysa X ve Y bağımsızdır → ρ = 0. (Kür konusu: zaman kalırsa çalış.)",
"Erwarteter Gewinn und fairer Einsatz": r"Adil oyun = uzun vadede kimse kazanmaz → beklenen net kazanç 0. Önce beklenen <b>ödemeyi</b> hesapla: 0.1·10 + 0.2·3 = 1.6 €. Adil fiyat bu. Bilet 2 € olduğu için bilet başına ortalama 0.40 € kaybedersin.",
})

# ======================================================================
LERN_TR["3"] = r"""
<p><b>Dağılımlar hazır modellerdir.</b> Durumu tanı, doğru formülü seç. Sırayla sor:</p>
<ol><li><b>Bir şey mi sayılıyor?</b> Sabit n deneme ve her biri evet/hayır → <b>Binom</b> (n = 1: Bernoulli). Üst sınır yok, „saatte/günde kaç tane“ → <b>Poisson</b>.</li>
<li><b>Bir süre mi ölçülüyor?</b> (bekleme, ömür) → <b>Üstel (Exponential)</b>.</li>
<li><b>Bir ortalama etrafında simetrik ölçüm?</b> → <b>Normal</b>. „a ile b arasında her değer eşit olasılıklı“ → <b>Düzgün (Gleichverteilung)</b>.</li></ol>
<p><b>Binom formülünü anlamak:</b> \(\binom nx\pi^x(1-\pi)^{n-x}\). 3 atış, π = 0.5, tam 2 isabet: Sıralamalar İİK, İKİ, Kİİ → \(\binom32=3\) tane. Her sıralamanın olasılığı \(0.5^3=0.125\). Toplam 0.375. \(\binom nx\) sıralamaları sayar, kalan kısım tek bir sıralamanın olasılığıdır.</p>
<p><b>Poisson:</b> λ = o zaman dilimindeki ortalama sayı; E = Var = λ. <b>Üstel:</b> bir sonraki olaya kadar geçen süre; ortalama süre 1/λ → <b>λ = 1/ortalama</b>.</p>
<p><b>Normal:</b> μ etrafında çan eğrisi, genişliği σ. Değerlerin ~%68'i μ ± σ, ~%95'i μ ± 2σ içinde. F için formül yok → <b>standartlaştır</b>: \(z=\frac{x-\mu}{\sigma}\) („ortalamadan kaç standart sapma uzakta?“), sonra Φ(z)'yi tablodan oku. Negatif z için: Φ(−z) = 1 − Φ(z).</p>
<p><b>Merkezi limit teoremi (ZGWS):</b> Birçok bağımsız gözlemin ortalaması yaklaşık normal dağılır; tek tek değerlerin dağılımı ne olursa olsun. Ortalamanın standart sapması \(\sigma/\sqrt n\)'dir.</p>
<p><b>Sık hatalar:</b> ① N(μ, σ²) yazımında <b>varyans</b>, R'da ise <b>standart sapma</b> kullanılır. ② Üstelde λ yerine ortalamayı koymak. ③ Kesiklide „4'ten fazla“ = ≥ 5 (≥ 4 değil).</p>"""

VERST_TR.update({
"Welche Verteilung passt? (Erkennen + Parameter)": r"Soru zincirini uygula: sayılıyor mu ölçülüyor mu? Deneme sayısı sabit mi, yoksa zaman başına açık uçlu mu? Parametreler metinde yazar: Binomda n ve π, Poisson'da „ortalama 4“ = λ, Normalde „ortalama 500, sd 3“ → N(500, 9) (varyans yazılır!). Üstelde ortalama 1/4 saat → λ = 4.",
"Bernoulliverteilung": r"Bernoulli en küçük yapı taşıdır: tek deneme, başarı (1) veya başarısızlık (0). E(X) = π, Var = π(1 − π). Asıl iş π'yi saymak: Toplamı 3'e bölünebilen 12 çift var (3: 2, 6: 5, 9: 4, 12: 1) → 12/36 = 1/3.",
"Binomialverteilung per Hand": r"Her terimi ayrı hesapla ve yaz. P(Y = 1): tek isabet 8 farklı yerde olabilir, her biri ⅓·(⅔)⁷. P(Y ≤ 2) = „0 veya 1 veya 2 isabet“ → üç ayrı durum, topla. E = nπ = 8/3, Var = nπ(1 − π) = 16/9. Ara sonuçları 4 ondalıkla tut, sadece sonucu 3 ondalığa yuvarla.",
"Binomial: „mindestens“, „mehr als“, „zwischen“ umschreiben": r"0, 1, …, 10 sayı doğrusunu çiz ve istenen değerleri işaretle. pbinom(k) her zaman 0'dan k'ya kadar olanları verir. „5'ten fazla“ = 6…10 = 1 − (0…5) = 1 − pbinom(5). „2 ile 6 arası (sınırlar hariç)“ = 3, 4, 5 = pbinom(5) − pbinom(2). Simülasyon (rastgele sayı) için <b>r</b>binom kullanılır.",
"Poissonverteilung per Hand": r"Formül \(\frac{\lambda^x}{x!}e^{-\lambda}\). x = 0 için λ⁰ = 1 ve 0! = 1 → sadece e^(−λ) kalır. „En az 2“ → yine tersinden: 1 − P(0) − P(1). Süre iki katına çıkarsa ortalama sayı da iki katına çıkar: 2 dakika için λ = 5.",
"Ist die transformierte Variable noch poissonverteilt?": r"Poisson'ın imzası: E = Var. Dönüşümden sonra E(Z) = 2·3 + 4 = 10, Var(Z) = 4·3 = 12 → eşit değil → Poisson olamaz. Ayrıca Z sadece 4, 6, 8, … değerlerini alıyor.",
"Gleichverteilung U(a, b)": r"Yoğunluk bir dikdörtgen: genişlik b − a = 8, alanın 1 olması için yükseklik 1/8. Her olasılık = „istenen genişlik / toplam genişlik“: P(X > 7) = 3/8. Ortalama tam ortada: (2 + 10)/2 = 6. Varyans (b − a)²/12. %90 çeyreği: 2 + 0.9·8 = 9.2.",
"Exponentialverteilung: λ aus dem Mittelwert": r"Süre → üstel. Ortalama 3 saat → λ = 1/3 (3 değil!). P(X > x) = e^(−λx) („hayatta kalma“ formülü) → P(X > 10) = e^(−10/3) = 0.036. P(X ≤ 1) = 1 − e^(−1/3). Medyan = ln2/λ. Kontrol: ortalama 3 saatken 10 saatten uzun sürmesi nadir olmalı → küçük sayı ✓.",
"Normalverteilung: standardisieren": r"σ = √9 = 3 (9 değil!). z = (x − μ)/σ: 505 ortalamanın 1.667 standart sapma üstünde. Aralık için: Φ(z_üst) − Φ(z_alt). Negatif z için tabloda simetri kullan: Φ(−1.333) = 1 − Φ(1.333). P(X > 500) = 0.5, çünkü μ tam ortada.",
"Normalverteilung: Quantile und „um mehr als 2σ“": r"Çeyreklik (Quantil) tersten sorulan sorudur: „x'in olasılığı ne?“ değil, „hangi x'in altında %95 var?“. Tablonun içinde 0.95'i ara → z ≈ 1.645 → geri dön: x = μ + σz = 175 + 1.645·9.5. „Ortalamayı 2σ'dan fazla aşmak“ = 1 − Φ(2) = 0.023, μ ve σ'dan bağımsızdır.",
"Summen und lineare Transformation normalverteilter ZV": r"<b>Bağımsız</b> büyüklüklerin toplamında standart sapmalar değil, varyanslar toplanır: koli N(5000, 90), sd = √90 = 9.49 (30 değil). Tek tek dalgalanmalar kısmen birbirini götürür. Aynı paketi 10 kez saymak (10X) ise varyansı 100 katına çıkarır.",
"Zentraler Grenzwertsatz: Verteilung des Mittelwerts": r"Ortalama, tek değerlerden çok daha az dalgalanır: ortalamanın sd'si σ/√n = 4/8 = 0.5. Bu yüzden 13'lük bir ortalama (μ'den sadece 1 dakika fazla) bile nadir: z = 2 → 0.023. ZGWS sayesinde tek tek süreler normal olmasa bile normal dağılım kullanılabilir.",
"Bivariate Normalverteilung: Rand und bedingte Verteilung": r"X'i bilmek Y'yi daha iyi tahmin etmeni sağlar. Koşullu ortalama ilişki yönünde kayar (ρ > 0 → daha büyük): 70 + 0.6·(12/10)·10 = 77.2. Belirsizlik (1 − ρ²) çarpanıyla küçülür: 144·0.64 = 92.16. Olasılık için <b>koşullu</b> μ ve σ ile standartlaştır. (Kür konusu.)",
"Ziehen ohne Zurücklegen: Lotto-Formel": r"Olasılıkları say: 4 kırmızıdan 2'sini seçme yolu \(\binom42=6\), diğer 6 toptan 1'ini seçme yolu 6 → 36 uygun kombinasyon. Toplam \(\binom{10}3=120\). Laplace: uygun / olası = 0.3. Geri koymadan çekildiği için Binom kullanılamaz. (Kür konusu.)",
})

# ======================================================================
LERN_TR["4"] = r"""
<p><b>Tahmin edici (Schätzer) bir tariftir:</b> Veriden tek bir sayı üretir, örneğin μ için \(\bar X\). Veri rastgele olduğu için sonuç da rastgeledir: Yeni bir örneklemle başka bir sayı çıkar.</p>
<p><b>Hedef tahtası resmi:</b> Tahtanın ortası gerçek parametre, her örneklem bir atış.
<b>Bias (yanlılık)</b> = atışların <i>sistematik olarak</i> kayması (nişangâh bozuk). <b>Varyans</b> = atışların ne kadar dağıldığı (titreyen el).
<b>MSE</b> = merkeze ortalama karesel uzaklık = Bias² + Varyans. <b>Tutarlı (konsistent)</b> = veri arttıkça atışların merkeze yaklaşması (MSE → 0).</p>
<p><b>Yansızlığı kontrol etmenin 4 adımı:</b> ① Tahmin edicinin tamamının beklenen değerini yaz. ② E'yi toplamın içine sok, sabitleri öne al. ③ \(E(X_i)=\mu\) yerine koy. ④ μ ile karşılaştır ve bir cümle yaz: „\(E(\hat\mu)=\mu\), also erwartungstreu“.
Varyans için (iid): \(Var(\sum a_iX_i)=\sum a_i^2Var(X_i)\). Çarpan <b>karesiyle</b> dışarı çıkar.</p>
<p><b>Çekirdek yoğunluk tahmini (KDE):</b> Histogram yoğunluğu basamaklarla tahmin eder. KDE ise her veri noktasının üzerine küçük bir „tepe“ (çekirdek) koyar ve hepsini toplar. Bant genişliği b = tepelerin genişliği: dar → tırtıklı, geniş → çok düz.</p>
<p><b>Sık hatalar:</b> ① Var'da 1/n çarpanını karelememek. ② Toplamdaki terim sayısını yanlış saymak (i = 2'den başlayan toplamda n − 1 terim var). ③ „Yansız = her zaman daha iyi“ sanmak; karar MSE'ye göre verilir.</p>"""

VERST_TR.update({
"Erwartungstreue prüfen und Bias berechnen": r"Taktik hep aynı: E ile toplamın yeri değişebilir, sabitler öne çıkar. E((2/n)ΣXᵢ) = (2/n)·n·μ = 2μ ≠ μ → yanlı, Bias = 2μ − μ = μ. (X₁ + Xₙ)/2'nin beklenen değeri μ → yansız ama sadece 2 değer kullanıyor (büyük varyans). X̄ yansızdır.",
"Schätzer mit Teilsummen (Testat-Typ) und Multiple Choice": r"Terimleri say: Σ i = 2'den n'ye gidiyor → n − 1 terim, her birinin beklenen değeri κ/2. E = κ/2 + (n − 1)κ/(4n) → paydayı 4n yap → κ(3n − 1)/(4n). Bias = −κ(n + 1)/(4n) ≠ 0 ve n'ye bağlı → (2) ve (3) doğru. (4) yanlış: Çok küçük varyanslı yanlı bir tahmin edicinin MSE'si daha küçük olabilir.",
"Varianz, MSE und Konsistenz von Schätzern": r"X̄ neden tutarlı? Her yeni gözlemle rastlantı biraz daha ortalanıp gider: Var = θ²/n → 0. (X₁ + X₂)/2 diğer verileri yok sayıyor, varyansı n ne kadar büyük olursa olsun θ²/2'de kalıyor → tutarlı değil. Bias = 0 olunca MSE = Var.",
"Verzerrter Schätzer mit Varianzberechnung (Tutorium 9)": r"İki yapı taşı: (1) Tek gözlemin varyansı E(X²) − E(X)²; kesirleri γ² paydasında topla → (γ² + 2γ − 1)/γ². (2) Ortalamanın varyansı = tek varyans / n. Tahmin edici yanlı, çünkü γ'yı değil 1/γ'yı tahmin ediyor.",
"Produkte im Schätzer kürzen (Probeklausur 2022, Aufgabe 7)": r"Korkutucu görünüyor ama bir sadeleştirme hilesi: Payda X₂…Xₙ₋₁, paydada X₁…Xₙ₋₁ var → X₁ dışındaki her şey sadeleşir → 1/X₁ kalır. E(Xₙ/α) = 1/4, −1/4 ile birbirini götürür. Resmî çözüm: E(1/X₁) = 4/α ≠ α → yanlı. Ders: önce sadeleştir, sonra E al.",
"MSE-Vergleich mit Zahlen": r"Hedef tahtası: A ortalamada tam isabet ama çok dağınık (Var 4). B biraz kaymış (Bias 1) ama az dağınık (Var 2). MSE(A) = 0 + 4 = 4, MSE(B) = 1 + 2 = 3 → B merkeze ortalamada daha yakın, yani daha iyi.",
"Gütekriterien von ML-Schätzern und Fehlerarten": r"ML'nin üç özelliği: <b>asimptotik yansız</b> (n → ∞'da Bias → 0), <b>tutarlı</b> (MSE → 0), <b>asimptotik normal</b>. 10 sınıflı histogramın 9 serbest parametresi var (alan 1 olmak zorunda). Daha çok sınıf: yaklaşım hatası ↓, tahmin hatası ↑. Daha büyük n: tahmin hatası ↓.",
"Kerndichteschätzer per Hand an einer Stelle": r"x = 3'te her veri noktasına „ne kadar yakınsın?“ diye sor: u = (3 − xᵢ)/b. Bir bant genişliğinden uzak olan noktalar katkı yapmaz (K = 0). Dikdörtgen çekirdekte u = 1 sayılmaz (−1 ≤ u < 1). Yakın noktalar katkı yapar; Epanechnikov'da ne kadar yakınsa o kadar çok. Sonunda n·b'ye böl, böylece alan 1 olur.",
})

# ======================================================================
LERN_TR["5"] = r"""
<p><b>Fikir:</b> Elimizde veri ve bilinmeyen bir parametreli model var (örneğin λ). Bütün λ değerlerini aklımızda deneyip şunu soruyoruz: <b>Hangi λ ile tam bu verileri görmek en olasıdır?</b> O λ, ML tahmin edicisidir. Örnek: 20 atışta 6 yazı → P(yazı) = 0.3 en iyi uyar.</p>
<p><b>Neden logaritma?</b> Likelihood uzun bir çarpımdır, çarpımın türevini almak zahmetlidir. Logaritma çarpımı <b>toplama</b> çevirir, toplamın türevi terim terim alınır. log her zaman arttığı için maksimum aynı yerde kalır.</p>
<p><b>Tarif (6 adım):</b> ① Likelihood: her gözlem için bir olasılık/yoğunluk, hepsini çarp \(L(\vartheta)=\prod f(x_i)\). ② log al: \(\ell=\sum\log f(x_i)\). ③ ϑ'ya göre türev al. ④ 0'a eşitle. ⑤ \(\hat\vartheta\)'yı çöz. ⑥ (istenirse) 2. türev < 0 → maksimum.</p>
<p><b>Log kuralları:</b> log(a·b) = log a + log b · log(aᵇ) = b·log a · log(eˣ) = x · log(1/a) = −log a. <b>Dikkat:</b> log(a + b) ≠ log a + log b!<br>
<b>Çarpım kuralları:</b> \(\prod_{i=1}^nc=c^n\) · \(\prod a^{x_i}=a^{\sum x_i}\) · \(\prod e^{-\lambda x_i}=e^{-\lambda\sum x_i}\).<br>
<b>Türevler:</b> (log ϑ)' = 1/ϑ · (log(1 − ϑ))' = −1/(1 − ϑ) · (c·ϑ)' = c · ϑ içermeyen terimler → 0.</p>
<p><b>Puan taktiği:</b> Çözüm adımında takılsan bile likelihood'u kurmak, log-likelihood'u sadeleştirmek ve „türev = 0“ yazmak puanların çoğunu getirir.</p>
<p><b>Standart sonuçlar (kontrol için):</b> Poisson λ̂ = x̄ · Bernoulli π̂ = x̄ · Üstel λ̂ = 1/x̄ · Normal μ̂ = x̄ · Geometrik p̂ = 1/(1 + x̄).</p>"""

VERST_TR.update({
"Likelihood für eine konkrete Stichprobe (geometrische Verteilung)": r"Her gözlem bir çarpan verir: (1 − p)^x·p. Çarparken üsler toplanır: p dört kez geçer (4 gözlem) → p⁴; (1 − p)'nin üssü 3 + 0 + 5 + 2 = 10. log: 4 log p + 10 log(1 − p). Türev: 4/p − 10/(1 − p) = 0 → 4(1 − p) = 10p → p̂ = 4/14 = 0.286. 10 log(1 − p)'nin türevinde iç türev −1 olduğu için eksi gelir.",
"ML allgemein: Poissonverteilung mit 2. Ableitung": r"Örnek tarif: ℓ = Σxᵢ·log λ − nλ − Σlog(xᵢ!). Son terim λ içermiyor → türevde düşer (bunu yazarsan puan alırsın). Türev: Σxᵢ/λ − n = 0 → λ̂ = x̄. 2. türev −Σxᵢ/λ² < 0 → maksimum. Örneklem: 12/6 = 2.",
"ML: Exponentialverteilung (auch Weibull mit r = 1)": r"∏λe^(−λxᵢ): e'nin önündeki λ n kez geçer → λⁿ; e'lerin üsleri toplanır → e^(−λΣxᵢ). log: n log λ − λΣxᵢ. Türev: n/λ − Σxᵢ = 0 → λ̂ = 1/x̄. Mantıklı: kısa bekleme süreleri yüksek oran demek. PK 2022'deki Weibull'da önce r = 1 koy, aynı şey çıkar.",
"ML: Bernoulli / Anteilswert": r"Bernoulli formülü π^x(1 − π)^(1 − x) bir hile: x = 1 için π, x = 0 için 1 − π kalır. L = π^k(1 − π)^(n − k), k = başarı sayısı. Türev: k/π − (n − k)/(1 − π) = 0 → π̂ = k/n = 6/20 = 0.3. Sonuç, formülsüz de tahmin edeceğin „başarı / deneme“ oranıdır.",
"ML: allgemeine geometrische Verteilung (Testat 5)": r"Somut örneklemdekiyle aynı akış, sadece sayı yerine Σxᵢ var: L = θⁿ(1 − θ)^(Σxᵢ). Türev = 0 → n(1 − θ) = θΣxᵢ → çarpımı aç → θ'ları bir tarafa topla → θ(n + Σxᵢ) = n → n'ye bölünce θ̂ = 1/(1 + x̄).",
"ML: Dichte mit Parameter im Exponenten (Übungsklausur ML, Aufgabe 1)": r"Parametre üsteyse log(x^b) = b·log x kullan: parametre bir sabitin önündeki çarpan olur. ℓ = n log(b + 1) + b·Σlog xᵢ. Σlog xᵢ veriden gelen bir sayıdır (0 ile 1 arasındaki x'ler için negatif). Türev: n/(b + 1) + Σlog xᵢ = 0 → b̂ = −1 − n/Σlog xᵢ. (a) ve (b) puanların çoğunu getirir.",
"ML: Normal- und Log-Normalverteilung, μ (σ bekannt)": r"Log-likelihood'u „μ'süz kısım“ ve „μ'lü kısım“ diye ayır. Sadece −1/(2σ²)·Σ(log xᵢ − μ)² μ'ye bağlı. Karenin türevi (zincir kuralı): 2(log xᵢ − μ)·(−1). Sonuç: μ̂ = logaritması alınmış verilerin ortalaması. Normal dağılımda (log ve 1/x olmadan) aynı şekilde μ̂ = x̄ çıkar.",
"ML: Parameter mit log(2) (Übungsklausur ML, Aufgabe 3)": r"log(2)'den korkma: o sadece bir sayı (≈ 0.693). 2^(−xβ)'nin logu −xβ·log2. ℓ = n log(log2) + n log β − β·log2·Σxᵢ. log(log2) sabit → türevde düşer. Türev: n/β − log2·Σxᵢ = 0 → β̂ = 1/(log(2)·x̄). Aslında üstel dağılımla aynı yapı.",
"ML aus einer Wahrscheinlichkeitstabelle (quadratische Gleichung)": r"Her gözlem için tablodaki değeri koy: 1 → α, 3 → 1 − α − α², 2 → α², 1 → α → L = α⁴(1 − α − α²). Türevden sonra çapraz çarp, her şeyi bir tarafa topla → 6α² + 5α − 4 = 0 → formül: (−5 ± 11)/12. Sadece izin verilen aralıktaki çözüm (0.5) geçerli; −4/3 olmaz.",
"ML für die Varianz der Normalverteilung (μ bekannt)": r"Hile: σ² yerine v yaz, doğru büyüklüğe göre türev al. −1/(2v)'nin türevi +1/(2v²). ℓ'(v) = −n/(2v) + Σxᵢ²/(2v²) = 0 → 2v² ile çarp → v̂ = Σxᵢ²/n. Sonuç: μ'den karesel uzaklıkların ortalaması. (Kür konusu.)",
"Reihenfolge der ML-Schritte (Testat 5)": r"Yemek tarifi gibi düşün: tarifi seç (model, D) → malzemeleri topla (likelihood, B) → sadeleştir (log, F) → ocağı aç (türev = 0, C) → sonucu al (çöz, E) → tadına bak (2. türev, A). Sıra: D → B → F → C → E → A.",
})

# ======================================================================
LERN_TR["6"] = r"""
<p><b>Neden aralık?</b> x̄ = 52.3 gibi bir tahmin neredeyse hiçbir zaman tam doğru değildir. Daha dürüst olan: „μ <i>büyük ihtimalle</i> 50.3 ile 54.3 arasında.“ Güven aralığının (Konfidenzintervall, KI) yapısı hep aynıdır:</p>
<p style="text-align:center;font-size:1.05rem">\(\text{Tahmin}\ \pm\ \text{Çeyreklik}\times\text{Standart hata}\)</p>
<ul><li><b>Tahmin:</b> x̄ (μ için) veya π̂ (oran için).</li>
<li><b>Çeyreklik (Quantil):</b> Ne kadar emin olmak istiyorsun? %95 → iki uçtan %2.5'er kes → 0.975 çeyrekliği → z = 1.96. σ bilinmiyorsa biraz daha büyük olan t çeyrekliği kullanılır (df = n − 1), çünkü σ'yı tahmin etmek ek belirsizlik getirir.</li>
<li><b>Standart hata:</b> Tahmin ne kadar dalgalanıyor? x̄ için σ/√n (veya s*/√n); oran için √(π̂(1 − π̂)/n).</li></ul>
<p><b>Hangi formül?</b> σ biliniyor → z · σ bilinmiyor → t (df = n − 1) · oran → z ve √(π̂(1 − π̂)/n) · varyans → χ² (bölme ile, ± ile değil).</p>
<p><b>Yorum:</b> Yöntem, örneklemlerin %95'inde gerçek μ'yü yakalar. Hesaplanmış <i>tek</i> bir aralık için „μ %95 olasılıkla içinde“ denmez, çünkü μ sabittir: ya içindedir ya değildir.</p>
<p><b>Sık hatalar:</b> ① %95 için 0.975 yerine 0.95 çeyrekliğini almak. ② df = n − 1 yerine n. ③ σ yerine σ² koymak. ④ Varyans aralığında çeyreklikleri karıştırmak.</p>"""

VERST_TR.update({
"KI für μ bei bekannter Varianz": r"Yapı: tahmin 52.3 ± çeyreklik 1.96 × standart hata 4/√16 = 1. %90 için daha az güvence gerekir → daha küçük çeyreklik (1.645) → daha dar aralık. Kontrol: tahmin aralığın tam ortasında olmalı.",
"KI für μ bei unbekannter Varianz (t-Quantil aus R-Output)": r"Hesaplamadan önce iki karar ver: (1) Hangi satır? σ bilinmiyor → t, df = n − 1 = 14. (2) Hangi sütun? %95 çift taraflı → 0.975. Değer: 2.145. 15'lik satırı ya da 0.95 sütununu alan puan kaybeder; soru tam bunun için hazırlanmış. Sonra: 180.5 ± 2.145·7/√15.",
"KI für einen Anteilswert": r"Oran, 0/1 değerlerinin ortalaması gibidir → yapı aynı. Bernoulli varyansı π(1 − π); π bilinmediği için π̂ = 0.8 kullanılır. Standart hata √(0.8·0.2/100) = 0.04 → 0.8 ± 1.96·0.04. Soru 4 ondalık istediği için cevap 4 ondalıkla verilir.",
"KI für die Varianz (χ²-Quantile aus R-Output)": r"Burada yapı farklı: ± yerine bölme var. Pay: (n − 1)·s*² = var·29 = 27.91232. Kural: <b>büyük</b> çeyrekliğe bölmek <b>küçük</b> sınırı verir → 27.91/45.72 ve 27.91/16.05. df = 29 (30 değil). Kontrol: s*² = 0.962 aralığın içinde ama tam ortasında değil, çünkü χ² dağılımı çarpık.",
"Rückwärts: Was steckt in diesem R-Befehl?": r"x̄ ± z·σ/√n formülünü R komutunun yanına koy ve parça parça eşleştir: ±'den önceki sayı x̄ = 3; qnorm(0.995) çeyreklik → 1 − α/2 = 0.995 → α = 0.01 → %99; 2 = σ; sqrt(100) = √n → n = 100.",
"Konfidenzintervalle richtig interpretieren": r"Benzetme: Aralık bir ağ, μ hareketsiz duran bir balık. „%95“, ağı çok kez attığında ne kadar iyi tuttuğunu anlatır. Atılmış tek bir ağ balığı ya yakalamıştır ya yakalamamıştır → (1) yanlış. (2) doğru. (3) doğru: daha çok veri = daha dar ağ. (4) yanlış: %99 daha geniş. (5) yanlış: 180 aralığın içinde → H₀ reddedilmez.",
})

# ======================================================================
LERN_TR["7"] = r"""
<p><b>Mahkeme benzetmesi:</b> Mahkemede „suçu kanıtlanana kadar masumdur“ ilkesi geçerlidir. <b>H₀ = masum</b> (sıkıcı normal durum), <b>H₁ = suçlu</b> (kanıtlamak istediğin şey). Kanıtlar (veri) H₀'a karşı çok güçlüyse mahkûmiyet olur (H₀ reddedilir). Beraat „masum olduğu kanıtlandı“ demek değildir, sadece „yeterli kanıt yok“ demektir. Reddedilmeyen bir H₀ da <b>kanıtlanmış sayılmaz</b>.</p>
<ul><li><b>1. tür hata</b> = masumu mahkûm etmek (H₀ doğru ama reddedildi). Olasılığı en fazla α (örn. %5).</li>
<li><b>2. tür hata</b> = suçluyu serbest bırakmak (H₁ doğru ama H₀ korundu).</li></ul>
<p><b>Test istatistiği</b> = „Veri H₀'dan kaç standart hata uzakta?“ Gauß testinde: \(z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}\). z büyükse (pozitif ya da negatif) veri H₀'a karşı konuşur.</p>
<p><b>Ret bölgesi (Ablehnungsbereich)</b> = H₀ altında olası değerlerin en uç %α'sı. Nerede olduğunu H₁ söyler: H₁ „&lt;“ → sol, „&gt;“ → sağ, „≠“ → iki tarafta α/2'şer.<br>
<b>p-değeri</b> = „H₀ doğruysa verim ne kadar şaşırtıcı?“ Küçükse (≤ α), o kadar şaşırtıcıdır ki H₀'a artık inanmayız.</p>
<p><b>Her testte 5 adım:</b> ① Hipotezler (göstermek istediğin H₁'e). ② Test istatistiği: formül + sayı. ③ H₀ altındaki dağılım. ④ Ret bölgesi veya p-değeri. ⑤ Konu bağlamında karar cümlesi.</p>
<p><b>Sık hatalar:</b> ① Göstermek istediğin iddiayı H₀'a yazmak. ② „H₀ kanıtlandı“ demek. ③ Çift taraflı testte 1 − α/2 yerine 1 − α çeyrekliğini almak.</p>"""

VERST_TR.update({
"Hypothesenpaar aus dem Text aufstellen": r"Metinde „absichern / zeigen / nachweisen / belegen“ (güvenceye almak, göstermek, kanıtlamak) kelimesini ara. Ondan sonra gelen kısım H₁ olur, eşittir işareti olmadan. H₀ onun tersidir ve eşittir işaretini alır (=, ≤, ≥). „unterscheidet sich / weicht ab“ (farklıdır) → çift taraflı (≠). „Daha yavaş“ gibi ifadelerde önce sayının büyüyüp büyümediğini düşün: yavaş = daha çok ms.",
"Fehler 1. und 2. Art im Sachkontext": r"Her zaman günlük dile çevir: „H₀ reddedilir“ = alarm çalar. 1. tür hata = yangın yokken alarm; 2. tür hata = yangın varken alarm yok. α ile hassasiyeti ayarlarsın: daha küçük α → daha az yanlış alarm, ama gerçek bir yangını kaçırma olasılığı artar.",
"Ablehnungsbereiche bestimmen": r"H₀ altındaki yoğunluğu çiz ve en uç %α'yı kes. Tek taraflıda alanın tamamı tek tarafta (çeyreklik 1 − α), çift taraflıda iki tarafta α/2'şer (çeyreklik 1 − α/2). t ve χ² testlerinde df = n − 1. χ²'de negatif değer yoktur: Sol taraf için „eksi bir şey“ değil, küçük çeyreklik χ²_α kullanılır.",
"p-Wert berechnen und interpretieren": r"p-değeri = H₁'in gösterdiği yönde „benim değerimden daha uç“ olan alan. Sağ taraflı: z'nin sağındaki alan, 1 − Φ(z). Sol taraflı: solundaki alan, Φ(z). Çift taraflı: küçük alanın iki katı. p-değeri, H₀'ın doğru olma olasılığı <b>değildir</b>.",
"Testentscheidung zu mehreren Niveaus": r"Bir p-değeri bütün α'lar için tek seferde karar verir: H₀, α ≥ p olan her düzeyde reddedilir. p = 0.014 → %10 ve %5'te ret, %1'de ret yok. Ret bölgesiyle çalışırsan her α için kritik değeri yeniden bulmalısın. Büyük α → büyük bölge → reddetmek daha kolay.",
"Exakter Binomialtest mit Tabelle": r"H₀ altında (π = 0.2) 10 bilette 2 boş beklenir. Gözlenen 5: tesadüf olabilir mi? p-değeri P(Z ≥ 5) = 1 − 0.9672 = 0.033: π = 0.2 olsaydı bu kadar ya da daha fazla boşu sadece %3.3 ihtimalle görürdük. Bu, α = %5'ten küçük → H₀ reddedilir.",
})

# ======================================================================
LERN_TR["8"] = r"""
<p><b>Bütün testler aynı şekilde işler</b>, sadece test istatistiği değişir. Öğrenmen gereken iki şey var: (1) <b>hangi test</b> uygun, (2) ona ait <b>formül ve dağılım</b> ne. Gerisi Abschnitt 7'deki 5 adım.</p>
<ul><li><b>Ortalama</b> μ: σ biliniyor → <b>Gauß testi</b> (N(0, 1)); σ bilinmiyor → <b>t testi</b> (t(n − 1)).</li>
<li><b>Oran</b> π: büyük n → <b>yaklaşık Binom testi</b> (N(0, 1)); küçük n → Binom dağılımıyla tam test.</li>
<li><b>Saçılım</b> σ²: <b>χ² varyans testi</b> (χ²(n − 1)).</li>
<li><b>Medyan</b>, dağılım varsayımı olmadan: <b>işaret testi</b> (Vorzeichentest, B(n; 0.5)).</li>
<li><b>İki kategorik özellik</b> (çapraz tablo): <b>χ² bağımsızlık testi</b>. Verilen bir dağılıma uyuyor mu: <b>χ² uyum testi</b>.</li></ul>
<p><b>χ² testlerini anlamak:</b> „Gözlediğim“ ile „H₀ doğru olsaydı beklediğim“ karşılaştırılır. Büyük sapma → büyük χ² → H₀ reddedilir. Bu yüzden bağımsızlık ve uyum testleri hep <b>sağ taraflıdır</b>.</p>
<p><b>Karar cümlesi kalıpları:</b> „H₀ wird verworfen; [iddia] ist zum Niveau α statistisch abgesichert.“ (H₀ reddedilir; iddia α düzeyinde istatistiksel olarak güvence altında.) · „H₀ kann nicht verworfen werden; [iddia] ist nicht nachweisbar.“ (H₀ reddedilemez; iddia kanıtlanamaz.)</p>"""

VERST_TR.update({
"Gauß-Test (σ bekannt) vollständig": r"Test istatistiği, x̄'nin iddia edilen değerin kaç standart hata altında olduğunu ölçer: 247.6 → 2.4 ml eksik, bir standart hata 4/3 = 1.33 ml → z = −1.8. H₀ altında böyle bir değer nadir (%3.6). „Az dolduruyor“ göstermek istediğimiz için H₁: μ < 250, sol taraflı → ret bölgesi (−∞; −1.645]. 5 adımın her biri genelde bir puan getirir.",
"t-Test per Hand (σ unbekannt)": r"Gauß testinden farkı: σ veriden tahmin edilir (s*, paydada n − 1) ve test istatistiği t dağılımına uyar. t dağılımının kuyrukları daha kalındır, kritik değerler daha büyüktür (4.604 > 2.576): σ tam bilinmediği için daha güçlü kanıt gerekir. |2.187| < 4.604 → reddedilmez.",
"t.test-Output: richtigen Code wählen und entscheiden": r"Üç şeyi kontrol et: doğru veri vektörü, doğru mu, doğru alternative. alternative = H₁'in yönü: \"less\" = &lt;, \"greater\" = &gt;, hiçbir şey yazılmamışsa ≠. Üç varyantta da t değeri aynı; sadece p-değeri değişir çünkü farklı bir alan kastediliyor. Burada H₁: μ > 30 → (2), p = 0.0296 < 0.05 → ret.",
"Approximativer Binomialtest für einen Anteil": r"H₀ altında nπ₀ = 200 onay beklenir, standart sapma √(nπ₀(1 − π₀)) = 10.95. Gözlenen 182 → 1.643 standart sapma eksik. Z'de X sayıdır (oran değil!). −1.643, %5 sınırının (−1.645) çok az önünde → reddedilmez; %10'da reddedilir. Ders: en sonda yuvarla, yoksa karar değişebilir.",
"Varianztest (χ²) vollständig": r"Test istatistiği gözlenen saçılımı iddia edilenle karşılaştırır: (n − 1)s*²/σ₀². Saçılım gerçekten küçükse değer küçük çıkar → sol taraflı test. Dikkat: soruda σ = 0.08 verilmiş, paydaya σ² = 0.0064 yazılır. 0.231 ∈ [0; 0.297] → ret.",
"p-Wert und Ablehnungsbereich in die χ²-Dichte einzeichnen": r"Çizim, „p < α“nın resimli hâli: İki alan da soldan 0'dan başlar. α alanı kritik değere (5.578), p alanı test istatistiğine (4.930) kadar uzanır. Test istatistiği kritik değerin solundaysa p alanı daha küçüktür → reddet.",
"Vorzeichentest für den Median": r"50 gerçekten medyan olsaydı her değer 0.5 olasılıkla altında kalırdı, yazı-tura gibi. 10 değerden 7'sinin 50 veya altında olması olağandışı değil (p = 0.344 > 0.05) → reddedilmez. Çift taraflıda iki taraftaki „en az bu kadar uç“ değerler sayılır: 7 ve fazlası, 3 ve azı.",
"χ²-Unabhängigkeitstest per Hand": r"Bağımsızlık altında beklenen sıklık: Tüm öğrencilerin 90/140'ı geçtiyse 80 BWL öğrencisinin de 90/140'ı geçmeli → 80·90/140 = 51.43. Gözlenen sayılar bundan ne kadar saparsa χ² o kadar büyür. Tag 1'den biliyorsun; yeni olan sadece çeyreklikle (3.841) karşılaştırmak: 9.333 ≥ 3.841 → bağımlı.",
"χ²-Anpassungstest (Würfel fair?)": r"Adil bir zarda 60 atışta her sayı için 10 beklenir. Sapmalar (−2, −1, 2, −3, 0, 4) karelenir, 10'a bölünür, toplanır → 3.4. df = kategori − 1 = 5, çünkü son sıklık diğerleri tarafından belirlenir (toplam = 60). 3.4 < 11.07 → zarın hileli olduğu kanıtlanamaz.",
"Test mit einer einzigen Beobachtung (Cappuccino-Typ)": r"Tek gözlemde n = 1 → standart hata = σ. Soru: 4.10 € Göttingen için olağandışı pahalı <i>veya</i> ucuz mu? → çift taraflı. z = (4.10 − 3.20)/0.40 = 2.25 → p = 0.024 < 0.05 → ret. Test ve güven aralığı aynı kararı verir: 4.10 etrafındaki aralık [3.316; 4.884], 3.20'yi dışarıda bırakır.",
"Welcher Test passt? (Entscheidungsbaum)": r"İlk soru her zaman: <b>Hangi parametre hakkında</b> bir şey gösterilecek (μ, π, σ², medyan, ilişki, dağılım)? İkinci soru: Ne biliniyor (σ?) ve n ne kadar büyük? İlk soruyu doğru cevaplayan testi neredeyse her zaman bulur.",
})

# ======================================================================
LERN_TR["9"] = r"""
<p><b>Fikir:</b> Nokta bulutunun içinden „en iyi uyan“ doğru çizilir. En iyi = noktaların doğruya dikey uzaklıkları (<b>artıklar, Residuen</b>) toplamda olabildiğince küçük olsun. Artıkların karesi alınır, böylece artılar ve eksiler birbirini götürmez ve büyük hatalar daha ağır sayılır → <b>en küçük kareler yöntemi (KQ)</b>.</p>
<p><b>Eğim</b> \(\hat\beta_1=\frac{s_{xy}}{s_x^2}\) = kovaryans / x'in varyansı (Tag 1!). <b>Kesişim</b> \(\hat\beta_0=\bar y-\hat\beta_1\bar x\): Doğru her zaman ağırlık merkezinden \((\bar x,\bar y)\) geçer.</p>
<p><b>Tahmin</b> ŷ = β̂₀ + β̂₁x; <b>artık</b> = gözlenen − tahmin edilen (pozitif → nokta doğrunun üstünde). <b>R²</b> = y'nin saçılımının doğruyla açıklanan payı (0 = hiç, 1 = mükemmel).</p>
<p><b>Yorum kalıbı:</b> „x bir birim artarsa y <b>ortalamada</b> β̂ birim değişir, <b>ceteris paribus</b> (diğer her şey sabitken).“ Birimleri unutma!</p>
<p><b>lm çıktısı:</b> Estimate = β̂ · Std. Error = standart hata · t value = Estimate / Std. Error · Pr(>|t|) = H₀: β = 0 testinin p-değeri · df = n − p − 1. (Bu bölüm Kür ağırlıklı; önce 1–8'i bitir.)</p>"""

VERST_TR.update({
"KQ-Gerade per Hand": r"En güvenli yol tablo: xᵢ − x̄, yᵢ − ȳ, çarpımları ve (xᵢ − x̄)². Çarpımların toplamı 14, karelerin toplamı 10 → β̂₁ = 1.4. β̂₀ = 5.6 − 1.4·3 = 1.4. Kontrol: (x̄, ȳ) = (3; 5.6) doğrunun üzerinde olmalı (1.4 + 1.4·3 = 5.6 ✓). Yorum: Reklam 1 000 € artarsa ciro ortalamada 1 400 € artar.",
"Prognose, Residuen und R²": r"Her x'i doğruya koy → ŷ. Artık = y − ŷ; pozitif = nokta doğrunun üstünde. KQ'da artıkların toplamı her zaman 0 olur, iyi bir kontrol (0.2 + 0.8 − 1.6 + 0 + 0.6 = 0 ✓). R² = 1 − (artık kareleri toplamı / y'nin toplam saçılımı) = 1 − 3.6/23.2 = 0.845 → saçılımın %84.5'i açıklanıyor.",
"lm-Output lesen: Interpretation, Prognose, Signifikanz": r"Çıktıyı tablo gibi oku: her satır bir katsayı. Tahmin için değerleri denklemde yerine koy; kukla değişkene (0/1) 0 veya 1 yazılır. Anlamlılık testi: H₀: β = 0, T = Estimate / Std. Error ~ t(df), p-değeri Pr(>|t|) sütununda. n = df + değişken sayısı + 1. Güven aralığı: β̂ ± t_{0.975; df}·SE.",
})

LERN_TR["10"] = r"""
<p><b>Sınav günü taktiği:</b> Önce bütün soruları 3 dakikada gözden geçir. Sonra emin olduğun puanları topla: hipotezler, dağılımı tanıma, E/Var, Bayes. Uzun integralleri ve ML türetmelerini sona bırak. 100 dakikada 75 puan ≈ puan başına 1.3 dakika. 5 dakikadan fazla takılırsan geç, sonra dön.</p>
<p><b>Kısmi puan:</b> Formülü yaz → sayıları koy → sonucu işaretle. Kutuyu asla boş bırakma: <b>Folgefehler</b> (önceki hatadan doğan hata) dikkate alınır, kendi (yanlış) ara sonucunla devam et.</p>
<p><b>Kontrol soruları:</b> Olasılık 0 ile 1 arasında mı? Varyans ≥ 0 mı? |ρ| ≤ 1 mi? Güven aralığı tahmini içeriyor mu? Doğru çeyreklik mi (çift taraflıda 1 − α/2)? df = n − 1 mi?</p>"""

VERST_TR.update({
"Was auf dein A4-Blatt (Seite 2) gehört": r"Kağıda sadece kafanda emin olmadığın şeyleri yaz. Uzun metin yerine formül + küçük örnek. Kendi elinle yaz, fotokopi yasak. En çok işe yarayanlar: dağılım tablosu (E, Var, R kısaltması), güven aralığı tablosu, test tablosu (istatistik + ret bölgesi + p-değeri) ve 5 adımlı test şeması.",
"Lernplan bis zur Klausur (9. Oktober)": r"Her gün: yeni bölümler + önceki günü 20 dakika tekrar (kartları bakmadan çöz). Akşamları 1–1.5 saat R. Sınavdan 2 gün önce Probeklausur A ve ML'yi süre tutarak çöz; hatalarını not et ve A4 kağıdına ekle.",
})
