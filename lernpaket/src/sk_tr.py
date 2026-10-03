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
