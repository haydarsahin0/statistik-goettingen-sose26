/* ================= TAG 2 · Zusammenhänge & Wahrscheinlichkeit ================= */

L({id:"2.1",day:2,no:1,title:"Kontingenztafel & χ²-Koeffizient",min:55,rel:2,
src:["V03","Tutorium 3","Testat 2","R-Skript 03"],
goal:"Du füllst eine Kontingenztafel aus Text aus, bildest Rand- und bedingte Verteilungen und misst den Zusammenhang mit dem χ²-Koeffizienten.",
blocks:[
{t:"idea",h:"Zwei Merkmale gleichzeitig",de:r`
<p>Beobachten wir an denselben Einheiten zwei Merkmale \(X\) und \(Y\), zählen wir Paare: \(h_{jk}\) = Anzahl mit \(X=a_j\) <b>und</b> \(Y=b_k\). Die Tabelle heißt <b>Kontingenztafel</b>. Zeilen- und Spaltensummen sind die <b>Randverteilungen</b> \(h_{j\bullet}\) und \(h_{\bullet k}\).</p>
<p>Die gemeinsame Verteilung bestimmt die Ränder — aber die Ränder bestimmen die gemeinsame Verteilung <b>nur bei Unabhängigkeit</b>.</p>`,
tr:r`Çapraz tablo (Kontingenztafel): iki değişkenin birlikte frekansları. Satır/sütun toplamları marjinal (Rand) dağılımlardır.`},
{t:"ex",h:"Tafel aus einem Text bauen (Tutorium 3, Aufgabe 2)",q:r`Von 1000 Verkehrsunfällen waren 380 tödlich. Bei 160 tödlichen Unfällen war der Fahrer alkoholisiert. Bei insgesamt 720 Unfällen war der Fahrer nicht alkoholisiert. (\(T\) = tödlich, \(A\) = alkoholisiert)`,
steps:[r`Gegebene Zahlen eintragen: \(n=1000\), Zeilensumme \(T\): 380, Zelle \(T\cap A\): 160, Spaltensumme \(\bar A\): 720.`,
r`Rest durch Differenzen: \(T\cap\bar A=380-160=220\); Spalte \(A\): \(1000-720=280\); \(\bar T\cap A=280-160=120\); \(\bar T\cap\bar A=720-220=500\).`,
r`<div class="tbl"><table><tr><th></th><th>\(A\)</th><th>\(\bar A\)</th><th>Σ</th></tr><tr><th>\(T\)</th><td>160</td><td>220</td><td>380</td></tr><tr><th>\(\bar T\)</th><td>120</td><td>500</td><td>620</td></tr><tr><th>Σ</th><td>280</td><td>720</td><td>1000</td></tr></table></div>`,
r`Anteil der nicht tödlichen Unfälle: \(620/1000=0.62\). Tödlich und nicht alkoholisiert: \(220/1000=0.22\).`]},
{t:"formula",h:"Bedingte Verteilung",tex:r`f(Y=b_k\mid X=a_j)=\frac{h_{jk}}{h_{j\bullet}}`,note:r`Zeilenweise normieren: jede Zeile durch ihre Zeilensumme teilen → jede Zeile summiert sich zu 1. Sind alle Zeilen gleich, gibt es <b>keinen</b> Zusammenhang.`,tr:r`Koşullu dağılım: hücreyi kendi satır toplamına böl. Bütün satırlar aynıysa ilişki yok.`},
{t:"num",q:r`Unfall-Tafel: Wie groß ist der Anteil tödlicher Unfälle <b>unter den alkoholisierten</b> Fahrern, und unter den nicht alkoholisierten?`,f:[{l:"f(T | A) =",a:160/280},{l:r`f(T | \(\bar A\)) =`,a:220/720}],why:r`\(160/280=0.571\) gegenüber \(220/720=0.306\). Die bedingten Verteilungen unterscheiden sich stark → Zusammenhang.`},
{t:"formula",h:"Erwartete Häufigkeit bei Unabhängigkeit & χ²-Koeffizient",tex:r`\tilde h_{jk}=\frac{h_{j\bullet}\,h_{\bullet k}}{n}\qquad \chi^2=\sum_{j=1}^{J}\sum_{k=1}^{K}\frac{(h_{jk}-\tilde h_{jk})^2}{\tilde h_{jk}}`,
parts:[[r`\tilde h_{jk}`,"„Zeilensumme mal Spaltensumme durch n“"],[r`\chi^2\approx0`,"(fast) unabhängig"],[r`\chi^2\ \text{groß}`,"starker Zusammenhang"]],
tr:r`Beklenen frekans = satır toplamı × sütun toplamı / n. χ² gözlenen ile beklenen arasındaki farkı ölçer.`},
{t:"ex",h:"χ² für die Unfall-Tafel",q:r`Berechne die erwarteten Häufigkeiten und \(\chi^2\).`,
steps:[r`\(\tilde h_{T,A}=\frac{380\cdot280}{1000}=106.4\), \(\tilde h_{T,\bar A}=\frac{380\cdot720}{1000}=273.6\), \(\tilde h_{\bar T,A}=\frac{620\cdot 280}{1000}=173.6\), \(\tilde h_{\bar T,\bar A}=\frac{620\cdot720}{1000}=446.4\).`,
r`Jede Abweichung ist hier \(\pm53.6\) (bei 2×2-Tafeln immer gleich groß!).`,
r`\(\chi^2=\frac{53.6^2}{106.4}+\frac{53.6^2}{273.6}+\frac{53.6^2}{173.6}+\frac{53.6^2}{446.4}=27.0015+10.5006+16.5493+6.4358\)`],a:r`\(\chi^2\approx 60.487\) → deutlicher Zusammenhang`},
{t:"num",q:r`V03: 447 Arbeitslose, Zeile „keine Ausbildung“ hat 123 Personen, Spalte „Kurzzeitarbeitslosigkeit“ 324 Personen. Wie groß ist \(\tilde h_{11}\)?`,f:[{l:r`\(\tilde h_{11}\) =`,a:123*324/447,tol:.005}],why:r`\(\frac{123\cdot324}{447}=89.154\). (Der χ²-Koeffizient der ganzen Tafel ist ≈ 4.82 — auf der Folie steht 4.51, aber nachgerechnet ergeben die Tabellenwerte 4.82.)`},
{t:"r",h:"In R",code:r`
tafel <- matrix(c(160, 120, 220, 500), nrow = 2,
                dimnames = list(c("T", "nicht T"), c("A", "nicht A")))
addmargins(tafel)                      # mit Randsummen
prop.table(tafel, margin = 1)          # bedingt: zeilenweise
erw <- outer(rowSums(tafel), colSums(tafel)) / sum(tafel)
sum((tafel - erw)^2 / erw)             # chi^2-Koeffizient`,
out:r`
[1] 60.48724`,
notes:[[1,"<code>matrix</code> füllt <b>spaltenweise</b>: erst 160, 120 (Spalte A), dann 220, 500.","matrix() sütun sütun doldurur."],[4,"<code>margin = 1</code> = Zeilen normieren, <code>margin = 2</code> = Spalten.",""],[5,"Erwartete Häufigkeiten: Zeilensumme × Spaltensumme / n für alle Zellen.",""]]},
{t:"trap",items:[r`Zeilen und Spalten vertauscht beim bedingten Anteil (Nenner = Summe der <b>Bedingung</b>).`,r`\(\chi^2\) mit relativen statt absoluten Häufigkeiten gerechnet.`,r`Aus dem Text die „insgesamt“-Zahl als Zelle statt als Randsumme eingetragen.`]}
]});

L({id:"2.2",day:2,no:2,title:"Kovarianz, Korrelation & Kausalität",min:65,rel:3,
src:["V03","Tutorium 3","Testat 2","Probeklausur A5"],
goal:"Du rechnest Kovarianz und Pearson-Korrelation mit dem Verschiebungssatz, rechnest Spearman mit Rängen, interpretierst das Ergebnis in Worten und begründest, warum Korrelation keine Kausalität ist.",
blocks:[
{t:"formula",h:"Empirische Kovarianz",tex:r`\operatorname{Cov}(X,Y)=s_{XY}=\frac1n\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)=\frac1n\sum_{i=1}^n x_iy_i-\bar x\,\bar y`,
note:r`Positiv: große \(x\) gehen mit großen \(y\) einher (konkordant). Negativ: gegenläufig. Die <b>Höhe</b> ist nicht interpretierbar — sie hängt von den Einheiten ab (cm vs. m, Tutorium 3).`,
tr:r`Kovaryansın işareti yönü gösterir; büyüklüğü birime bağlı olduğu için yorumlanamaz.`},
{t:"formula",h:"Korrelationskoeffizient nach Bravais-Pearson",tex:r`\rho_{XY}=\frac{s_{XY}}{s_X\,s_Y}=\frac{s_{XY}}{\sqrt{s_X^2\,s_Y^2}}\,,\qquad -1\le\rho\le 1`,
parts:[["|\\rho|\\lt 0.3","schwach"],["0.3\\le|\\rho|\\lt0.7","mittel"],["|\\rho|\\ge 0.7","stark"]],note:r`Misst nur den <b>linearen</b> Zusammenhang. \(\rho=0\) heißt „kein linearer“, nicht „kein“ Zusammenhang.`,
tr:r`Korelasyon: normlanmış kovaryans, −1 ile 1 arası, birimsiz. Sadece doğrusal ilişkiyi ölçer.`},
{t:"fig",kind:"scatter",h:"Konkordant und diskordant",x:[68,108],y:[155,205],xl:"Gewicht (kg)",yl:"Größe (cm)",pts:[[93,198],[72,160],[83,167],[104,199],[76,182]],means:[85.6,181.2],cap:"Tutorium 3: Durch den Schwerpunkt (x̄, ȳ) = (85.6, 181.2) entstehen 4 Quadranten. Punkte oben rechts / unten links: (xᵢ−x̄)(yᵢ−ȳ) > 0 → positiver Beitrag."},
{t:"ex",h:"Gewicht und Größe (Tutorium 3, Aufgabe 3)",q:r`Gewicht 93, 72, 83, 104, 76 (kg) und Größe 198, 160, 167, 199, 182 (cm).`,
steps:[r`Mittelwerte: \(\bar x=85.6\), \(\bar y=181.2\).`,r`Kovarianz: \(\frac15[(7.4)(16.8)+(-13.6)(-21.2)+(-2.6)(-14.2)+(18.4)(17.8)+(-9.6)(0.8)]=153.88\).`,r`Varianzen (Verschiebungssatz): \(s_X^2=\frac15(93^2+\dots+76^2)-85.6^2=135.44\), \(s_Y^2=250.16\).`,r`\(\rho=\frac{153.88}{\sqrt{135.44}\sqrt{250.16}}=0.836\).`],a:r`\(\rho=0.836\): starker positiver linearer Zusammenhang`},
{t:"num",q:r`Testat 2: \(n=50\), \(\sum x=2019\), \(\sum y=3733\), \(\sum x^2=87611\), \(\sum y^2=301695\), \(\sum xy=160064\). Berechne die (unkorrigierte) Kovarianz und \(\rho\).`,
f:[{l:"Cov =",a:186.5092,tol:.002},{l:"ρ =",a:.7885357,tol:.0006}],why:r`\(\bar x=40.38\), \(\bar y=74.66\). \(s_{XY}=\frac{160064}{50}-40.38\cdot74.66=3201.28-3014.7708=186.509\). \(s_X^2=\frac{87611}{50}-40.38^2=121.6756\), \(s_Y^2=\frac{301695}{50}-74.66^2=459.7844\). \(\rho=\frac{186.5092}{\sqrt{121.6756\cdot459.7844}}=0.789\).`},
{t:"idea",h:"Rangkorrelation nach Spearman",de:r`
<p>Für <b>ordinale</b> Merkmale (oder monotone, nicht-lineare Zusammenhänge): ersetze jeden Wert durch seinen <b>Rang</b> (kleinster = 1) und rechne dann Pearson mit den Rängen. Gleiche Werte (Bindungen) bekommen den <b>Durchschnittsrang</b>: Teilen sich zwei Werte die Plätze 4 und 5, bekommen beide 4.5.</p>`,
tr:r`Spearman: değerlerin yerine sıralarını (Rang) koy, sonra Pearson formülünü uygula. Eşit değerler ortalama sırayı alır.`},
{t:"ex",h:"Film-Bewertungen (Tutorium 3, Aufgabe 4)",q:r`Metacritic: 6.5, 7.1, 8.1, 9.3, 7.8, 8.1, 8.6, 9.3, 9.4, 9.0 · Rotten Tomatoes: 8.5, 8.6, 9.4, 9.2, 9.8, 9.2, 9.4, 9.6, 9.8, 9.7`,
steps:[r`Ränge Metacritic: 1, 2, 4.5, 8.5, 3, 4.5, 6, 8.5, 10, 7 (8.1 kommt zweimal auf Platz 4 und 5 → 4.5).`,r`Ränge Rotten: 1, 2, 5.5, 3.5, 9.5, 3.5, 5.5, 7, 9.5, 8.`,r`Mittlerer Rang \(=\frac{n+1}{2}=5.5\). \(\sum rk_x rk_y=347.25\), \(\sum rk_x^2=384\), \(\sum rk_y^2=383.5\), \(n\cdot5.5^2=302.5\).`,r`\(\rho_S=\frac{347.25-302.5}{\sqrt{(384-302.5)(383.5-302.5)}}=\frac{44.75}{\sqrt{81.5\cdot81}}=0.551\).`],a:r`Spearman 0.551, Pearson 0.752`},
{t:"idea",h:"Korrelation ≠ Kausalität",de:r`
<p><b>Kausalität</b> heißt: eine Änderung von \(X\) <i>verursacht</i> eine Änderung von \(Y\). Um das zu zeigen, bräuchte man eine gezielte Manipulation von \(X\) und die Kontrolle aller anderen Einflüsse (z. B. durch Randomisierung). Eine normale statistische Analyse zeigt nur einen <b>statistischen Zusammenhang</b>.</p>
<ul><li><b>Scheinkorrelation</b>: Margarineverbrauch und Scheidungsrate in Maine korrelieren mit 0.99 — eine dritte Variable (z. B. wirtschaftliche Lage) oder Zufall steckt dahinter.</li>
<li><b>Ökologischer Fehlschluss</b>: von Gruppendaten (Stadtbezirke mit vielen Grünen-Wählern haben mehr EHEC-Fälle) unzulässig auf Personen schließen.</li></ul>`,
tr:r`Korelasyon nedensellik değildir. Üçüncü bir değişken ilişkiyi yaratabilir. Grup verisinden bireye sonuç çıkarmak „ökologischer Fehlschluss“tur.`},
{t:"rule",k:"Musterformulierung · 2 Punkte",de:r`„Nein. Statistische Analysen liefern keinen Nachweis einer Kausalität; der Zusammenhang könnte auch durch dritte Variablen entstehen.“`,tr:r`Sınavda bu cümleyi aynen kullanabilirsin.`},
{t:"mc",q:r`Welche Aussagen sind korrekt? (Testat 2, Aufgabe 2)`,o:[r`Wenn \(\rho_{XY}\ne0\), sind \(X\) und \(Y\) niemals unabhängig.`,r`Wenn \(Y=-X^2\), kann \(\rho_{XY}\) annähernd 0 sein.`,r`Wenn \(X=Y\), gilt immer \(\rho_{XY}=1\).`,r`Wenn \(\rho_{XY}\ne0\), besteht stets ein kausaler Zusammenhang.`,r`Wenn \(\operatorname{Cov}(X,Y)\ge0.8\), liegt immer ein starker Zusammenhang vor.`],k:[0,1,2],why:r`(a) Unabhängig ⇒ unkorreliert, also: korreliert ⇒ abhängig. (b) Quadratischer Zusammenhang, symmetrisch um 0 → linear kaum sichtbar. (c) Perfekter linearer Zusammenhang (sofern Varianz &gt; 0). (d) Korrelation ≠ Kausalität. (e) Die Kovarianz ist nicht normiert.`},
{t:"r",h:"In R",code:r`
x <- c(93, 72, 83, 104, 76); y <- c(198, 160, 167, 199, 182)
mean(x * y) - mean(x) * mean(y)     # Kovarianz mit 1/n
cov(x, y)                           # ACHTUNG: mit 1/(n-1)
cor(x, y)                           # Pearson (Standard)
cor(x, y, method = "spearman")      # Spearman
plot(x, y, xlab = "Gewicht", ylab = "Größe")`,
out:r`
[1] 153.88
[1] 192.35
[1] 0.8359875
[1] 0.9`,
notes:[[3,"<code>cov()</code> teilt wie <code>var()</code> durch \\(n-1\\). Für die Korrelation ist das egal — der Faktor kürzt sich weg.","cor() sonucu n veya n−1 fark etmez."]]},
{t:"exam",h:"Probeklausur Aufgabe 5 — Biathlon",src:"Probeklausur A-Teil",q:r`Schießfehler \(x\): 3, 2, 5, 1, 3, 4. Laufzeit \(y\) (min): 18, 20, 26, 24, 25, 19.`,
parts:[{q:r`(a) Berechnen Sie die empirische Varianz der Schießfehler. Geben Sie den Lösungsweg an.`,p:2,s:r`\(\bar x=18/6=3\), \(\overline{x^2}=\frac{9+4+25+1+9+16}{6}=\frac{64}{6}=10.6667\). \(s_x^2=10.6667-9=1.667\).`},
{q:r`(b) Ermitteln Sie \(\rho_{xy}\). Verwenden Sie \(s_y^2=10\), \(s_x^2=1.6\), \(\bar y=22\), \(\sum x_\nu y_\nu=399\). Lösungsweg + Interpretation.`,p:5,s:r`\(s_{xy}=\frac{399}{6}-3\cdot22=66.5-66=0.5\). \(\rho=\frac{0.5}{\sqrt{1.6\cdot10}}=\frac{0.5}{4}=0.125\).<br>Interpretation: „Es handelt sich um die normierte Kovarianz. Der Koeffizient gibt den Grad des linearen Zusammenhangs von X und Y an und liegt zwischen −1 und +1. Hier kann man von einer <b>niedrigen positiven Korrelation</b> ausgehen.“`},
{q:r`(c) Der Trainer behauptet, eine hohe Korrelation bedeute, dass Schießfehler die schwache Laufleistung verursachen. Stimmen Sie zu? Begründen Sie in 1–2 Sätzen.`,p:2,s:r`Nein, statistische Analysen liefern keinen Nachweis einer Kausalität; der Zusammenhang könnte auch durch dritte Variablen entstehen.`},
{q:r`(d) Skizzieren Sie ein mögliches Streudiagramm für \(\rho_{xy}=0\).`,p:2,s:r`Punktwolke ohne erkennbaren linearen Trend (z. B. gleichmäßig verstreut oder U-förmig). <b>Achsen beschriften</b>: x = Schießfehler, y = Laufzeit in min.`}]}
]});

L({id:"2.3",day:2,no:3,title:"Ereignisse & Rechenregeln",min:50,rel:3,
src:["V04","Tutorium 1, 4","Testat 0, 3","Probeklausur A4"],
goal:"Du übersetzt Ereignisse in Mengen (∩, ∪, Komplement, Differenz), rechnest Laplace-Wahrscheinlichkeiten und nutzt die Axiome von Kolmogorov für Lücken-Aufgaben.",
blocks:[
{t:"terms",h:"Sprache der Mengen",items:[
["Ergebnisraum Ω","örnek uzay","Menge aller möglichen Ergebnisse, z. B. Würfel: {1,…,6}."],
["Ereignis A ⊆ Ω","olay","Teilmenge, z. B. „gerade Zahl“ = {2,4,6}."],
[r`\(A\cap B\) · Durchschnitt`,"kesişim","A <b>und</b> B treten ein."],
[r`\(A\cup B\) · Vereinigung`,"birleşim","A <b>oder</b> B (oder beide)."],
[r`\(\bar A = A^c\) · Komplement`,"tümleyen",r`A tritt <b>nicht</b> ein: \(\Omega\setminus A\).`],
[r`\(A\setminus B=A\cap\bar B\)`,"fark","A, aber nicht B."],
["disjunkt","ayrık",r`\(A\cap B=\emptyset\): schließen sich aus.`],
[r`\(|A|\) · Mächtigkeit`,"eleman sayısı","Anzahl der Elemente."]]},
{t:"num",q:r`\(\Omega=\{1,\dots,9\}\), \(A=\{1,3,6,7\}\), \(B=\{1,3,6,9\}\) (Probeklausur A4). Bestimme \(|A\cap\bar B|\), \(|\bar A\cup B|\) und \(P(A\mid\bar B)\) (Laplace).`,
f:[{l:r`\(|A\cap\bar B|\) =`,a:1,tol:0},{l:r`\(|\bar A\cup B|\) =`,a:8,tol:0},{l:r`\(P(A\mid\bar B)\) =`,a:.2}],
why:r`\(\bar B=\{2,4,5,7,8\}\) → \(A\cap\bar B=\{7\}\), also 1. \(\bar A=\{2,4,5,8,9\}\), vereinigt mit \(B\): \(\{1,2,3,4,5,6,8,9\}\) → 8. \(P(A\mid\bar B)=\frac{|A\cap\bar B|}{|\bar B|}=\frac15\). In die Lücken gehört die Notation \(P(A\mid \bar B)\).`},
{t:"formula",h:"Laplace & Kolmogorov",tex:r`P(A)=\frac{|A|}{|\Omega|}\quad\text{(alle gleich wahrscheinlich)}\qquad (K1)\ P(A)\ge0\quad (K2)\ P(\Omega)=1\quad (K3)\ P(A\cup B)=P(A)+P(B)\ \text{falls}\ A\cap B=\emptyset`},
{t:"formula",h:"Rechenregeln, die daraus folgen",tex:r`P(\bar A)=1-P(A)\qquad P(A\cup B)=P(A)+P(B)-P(A\cap B)\qquad P(A)=P(A\cap B)+P(A\setminus B)`,note:r`Male bei Lücken-Aufgaben immer ein Venn-Diagramm mit drei Feldern: \(A\setminus B\), \(A\cap B\), \(B\setminus A\).`,tr:r`Boşluk doldurma sorularında Venn şeması çiz: A\B, A∩B, B\A.`},
{t:"num",q:r`Tutorium 4, Aufgabe 1: (i) \(P(A)\), wenn \(P(B)=0.5\), \(P(B\setminus A)=0.4\), \(P(A\setminus B)=0.2\). (ii) \(P(A)\), wenn \(P(A\cup B)=0.8\), \(P(B)=0.5\), \(P(A\cap B)=0.2\). (iii) \(P(A\cap B)\), wenn \(P(A\cup B)=0.8\) und \(P(A\setminus B)=P(B\setminus A)=0.2\).`,
f:[{l:"(i) P(A) =",a:.3},{l:"(ii) P(A) =",a:.5},{l:"(iii) P(A∩B) =",a:.4}],
why:r`(i) \(P(A\cap B)=0.5-0.4=0.1\) → \(P(A)=0.1+0.2=0.3\). (ii) \(P(A)=0.8-0.5+0.2=0.5\). (iii) \(0.8-0.2-0.2=0.4\).`},
{t:"ex",h:"Ereignis C rekonstruieren (Tutorium 4, Aufgabe 2)",q:r`Laplace mit \(\Omega=\{1,\dots,10\}\), \(A=\{3,5,7\}\), \(B=\{1,2,4,5,6,9,10\}\). Gesucht \(C\) mit \(P(A\cup C)=0.4\), \(P(A\cap B\cap C)=0.1\), \(P(B\cup C)=0.8\), \(P(C)=0.2\).`,
steps:[r`\(P(C)=0.2\) → \(C\) hat 2 Elemente.`,r`\(P(A\cap B\cap C)=0.1\) → ein gemeinsames Element; \(A\cap B=\{5\}\) → \(5\in C\).`,r`\(B\cup C\) hat 8 Elemente, \(B\) hat 7 → das zweite Element liegt nicht in \(B\). \(A\cup C\) hat 4, \(A\) hat 3 → es liegt auch nicht in \(A\).`,r`Weder in \(A\) noch in \(B\): nur 8 bleibt.`],a:r`\(C=\{5,8\}\)`},
{t:"num",q:r`Glücksrad mit \(\Omega=\{1,\dots,10\}\) (Testat 3): \(A=\{1,\dots,5\}\), \(B=\{2,4,6,8,10\}\), \(C=\{1,4,7,10\}\). Berechne \(P(A\cup C)\) und \(P(A\mid B)\).`,f:[{l:"P(A∪C) =",a:.7},{l:"P(A|B) =",a:.4}],why:r`\(A\cup C=\{1,2,3,4,5,7,10\}\) → 0.7. \(A\cap B=\{2,4\}\) → \(P(A\mid B)=\frac{2/10}{5/10}=0.4\). Da \(P(A)=0.5\ne0.4=P(A\mid B)\), sind \(A\) und \(B\) <b>abhängig</b>.`},
{t:"r",h:"Mengen in R",code:r`
Omega <- 1:9; A <- c(1,3,6,7); B <- c(1,3,6,9)
Bq <- setdiff(Omega, B)          # Komplement von B
intersect(A, Bq)                 # A ∩ B-quer
length(union(setdiff(Omega, A), B))
length(intersect(A, Bq)) / length(Bq)`,out:r`
[1] 7
[1] 8
[1] 0.2`}
]});

L({id:"2.4",day:2,no:4,title:"Bedingte Wahrscheinlichkeit & Unabhängigkeit",min:50,rel:3,
src:["V04","Tutorium 4","Testat 3"],
goal:r`Du rechnest mit \(P(A\mid B)\), dem Produktsatz und prüfst Unabhängigkeit sauber — auch beim Ziehen ohne Zurücklegen.`,
blocks:[
{t:"formula",h:"Bedingte Wahrscheinlichkeit & Produktsatz",tex:r`P(A\mid B)=\frac{P(A\cap B)}{P(B)}\qquad P(A\cap B)=P(A\mid B)\,P(B)=P(B\mid A)\,P(A)`,note:r`Idee: Wir wissen, dass \(B\) passiert ist → \(\Omega\) schrumpft auf \(B\) und wird neu normiert.`,tr:r`B olduğunu biliyorsak örnek uzay B'ye küçülür. P(A|B) = P(A∩B)/P(B).`},
{t:"ex",h:"Würfel (V04)",q:r`Fairer Würfel. \(A\) = „gerade“ = {2,4,6}, \(B\) = „höchstens 3“ = {1,2,3}. Wie ändert sich \(P(A)\), wenn man \(B\) kennt?`,
steps:[r`Ohne Information: \(P(A)=\frac36=\frac12\).`,r`\(A\cap B=\{2\}\) → \(P(A\cap B)=\frac16\), \(P(B)=\frac36\).`,r`\(P(A\mid B)=\frac{1/6}{3/6}=\frac13\), und \(P(\bar A\mid B)=\frac23=1-P(A\mid B)\).`],a:r`\(P(A\mid B)=1/3 \lt 1/2\) — das Wissen über \(B\) macht \(A\) unwahrscheinlicher.`},
{t:"formula",h:"Stochastische Unabhängigkeit",tex:r`A,B\ \text{unabhängig}\iff P(A\cap B)=P(A)\,P(B)\iff P(A\mid B)=P(A)`,note:r`Mit Zurücklegen ziehen → unabhängig. Ohne Zurücklegen → abhängig. (Urne 1,2,3,4: „erst 1, dann 2“ hat mit Zurücklegen \(\frac1{16}=\frac14\cdot\frac14\), ohne Zurücklegen \(\frac1{12}\ne\frac1{16}\).)`,tr:r`Bağımsızlık: P(A∩B)=P(A)·P(B). İadeli çekilişte bağımsız, iadesizde bağımlı.`},
{t:"num",q:r`Testat 3, Aufgabe 1: \(P(A)=0.2\), \(P(B)=0.6\), \(P(A\mid B)=0.3\). Berechne \(P(A\cup B)\) und \(P(A\mid\bar B)\).`,f:[{l:"P(A∪B) =",a:.62},{l:r`\(P(A\mid\bar B)\) =`,a:.05}],why:r`\(P(A\cap B)=0.3\cdot0.6=0.18\). \(P(A\cup B)=0.2+0.6-0.18=0.62\). \(P(A\cap\bar B)=0.2-0.18=0.02\), \(P(\bar B)=0.4\) → \(0.02/0.4=0.05\).`},
{t:"num",q:r`Softeis-Maschine (Testat 3, Aufgabe 7): \(P(A)=0.05\), \(P(A\mid B)=0.2\), \(P(A\cap B)=0.02\). Berechne \(P(B)\) und \(P(B\mid A)\).`,f:[{l:"P(B) =",a:.1},{l:"P(B|A) =",a:.4}],why:r`\(P(B)=\frac{P(A\cap B)}{P(A\mid B)}=\frac{0.02}{0.2}=0.1\). \(P(B\mid A)=\frac{0.02}{0.05}=0.4\).`},
{t:"num",q:r`Tutorium 4, Aufgabe 1 (iv) und (v): (iv) \(P(B\mid A)\), wenn \(P(A)=\tfrac12\), \(P(B)=\tfrac14\), \(P(A\mid B)=\tfrac12\). (v) \(A,B\) unabhängig, \(P(A\cap B)=\tfrac25\), \(P(B\setminus A)=\tfrac15\): gesucht \(P(A)\) und \(P(A\cup B)\).`,
f:[{l:"(iv) P(B|A) =",a:.25},{l:"(v) P(A) =",a:2/3},{l:"(v) P(A∪B) =",a:13/15}],
why:r`(iv) \(P(A\cap B)=\frac12\cdot\frac14=\frac18\) → \(P(B\mid A)=\frac{1/8}{1/2}=\frac14\). (Schneller: \(P(A\mid B)=P(A)\) → unabhängig → \(P(B\mid A)=P(B)\).)<br>(v) \(P(B)=\frac25+\frac15=\frac35\); unabhängig → \(P(A)=\frac{2/5}{3/5}=\frac23\); \(P(A\cup B)=\frac23+\frac35-\frac25=\frac{13}{15}=0.867\).`},
{t:"num",q:r`Testat 3: Faire Münze dreimal, \(Z_i\) = Anzahl Kopf bis Wurf \(i\). Berechne \(P(Z_3=3)\) und \(P(Z_3=3\mid Z_2=2)\). Außerdem: zweimal würfeln, \(P(\text{Summe}=8)\).`,f:[{l:"P(Z₃=3) =",a:.125},{l:"P(Z₃=3 | Z₂=2) =",a:.5},{l:"P(Summe=8) =",a:5/36}],why:r`\((\frac12)^3=\frac18\). Wenn die ersten beiden schon Kopf sind, fehlt nur noch der dritte: \(\frac12\). Summe 8: (2,6),(3,5),(4,4),(5,3),(6,2) → \(\frac{5}{36}=0.139\).`},
{t:"num",q:r`Kiste ohne Zurücklegen (Testat 3, Aufgabe 6): 15 rot, 5 blau, 5 gelb. Rot = verloren, Blau = gewonnen, Gelb = nochmal ziehen. (a) \(P\)(verliert im ersten Zug), (b) \(P\)(gewinnt im zweiten Zug).`,f:[{l:"(a) =",a:.6},{l:"(b) =",a:25/600}],why:r`(a) \(\frac{15}{25}=0.6\). (b) Erst gelb, dann blau: \(\frac{5}{25}\cdot\frac{5}{24}=\frac{25}{600}=0.042\). Achtung: Nach dem ersten Zug sind nur noch <b>24</b> Kugeln drin.`},
{t:"r",h:"Simulation in R (Testat 3)",code:r`
set.seed(123)
n <- 1000
wuerfe <- replicate(n, sample(c(0, 1), 3, replace = TRUE))
kopfzahlen <- colSums(wuerfe)
mean(kopfzahlen == 3)          # relative Häufigkeit ~ 1/8`,notes:[[3,"<code>replicate(n, …)</code> wiederholt das Experiment n-mal; <code>sample(c(0,1), 3, replace = TRUE)</code> = dreimal Münze werfen.","replicate: deneyi n kez tekrarlar; sample(..., replace=TRUE): iadeli çekiliş."],[5,"Anteil der Experimente mit drei Köpfen → nähert sich 0.125.",""]]}
]});

L({id:"2.5",day:2,no:5,title:"Totale Wahrscheinlichkeit & Satz von Bayes",min:70,rel:3,
src:["V04","Tutorium 4","Testat 3","Probeklausur A3"],
goal:r`Du erkennst Bayes-Aufgaben sofort, baust eine saubere Tabelle der gegebenen Wahrscheinlichkeiten und rechnest \(P(B)\) und \(P(A_j\mid B)\) ohne Verwechslung.`,
blocks:[
{t:"formula",h:"Satz der totalen Wahrscheinlichkeit",tex:r`P(B)=\sum_{i=1}^{k}P(B\mid A_i)\,P(A_i)`,parts:[["A_1,\\dots,A_k","disjunkte Zerlegung von Ω (jede Person gehört genau zu einer Gruppe)"]],tr:r`Toplam olasılık: B'nin olasılığı = her gruptaki B olasılığı × grubun olasılığı, toplamı.`},
{t:"formula",h:"Satz von Bayes",tex:r`P(A_j\mid B)=\frac{P(B\mid A_j)\,P(A_j)}{\sum_{i=1}^{k}P(B\mid A_i)\,P(A_i)}=\frac{P(B\mid A_j)\,P(A_j)}{P(B)}`,note:r`Bayes „dreht die Bedingung um“: gegeben ist \(P(B\mid A)\), gefragt ist \(P(A\mid B)\).`,tr:r`Bayes koşulu ters çevirir: P(B|A) biliniyor, P(A|B) soruluyor.`},
{t:"rule",de:r`Bayes-Rezept: <b>1.</b> Ereignisse benennen · <b>2.</b> alle gegebenen Zahlen als \(P(\cdot)\) oder \(P(\cdot\mid\cdot)\) aufschreiben · <b>3.</b> fehlende per Gegenwahrscheinlichkeit ergänzen · <b>4.</b> Nenner mit totaler Wahrscheinlichkeit · <b>5.</b> Bayes.`,tr:r`Önce olayları adlandır, verilenleri P(·|·) olarak yaz, eksikleri 1−… ile tamamla, paydayı toplam olasılıkla hesapla.`},
{t:"ex",h:"Medizinischer Test (V04)",q:r`Prävalenz 0.1 %, Sensitivität 90 % (Kranke werden erkannt), Spezifität 90 % (Gesunde sind negativ). Wie wahrscheinlich ist man krank, wenn der Test positiv ist?`,
steps:[r`\(A\) = krank, \(B\) = positiv. \(P(A)=0.001\), \(P(B\mid A)=0.9\), \(P(\bar B\mid\bar A)=0.9\Rightarrow P(B\mid\bar A)=0.1\).`,r`Totale W.: \(P(B)=0.9\cdot0.001+0.1\cdot0.999=0.0009+0.0999=0.1008\).`,r`Bayes: \(P(A\mid B)=\frac{0.0009}{0.1008}=0.0089\).`],a:r`Nur ≈ 0.9 % der positiv Getesteten sind krank — wegen der kleinen Prävalenz.`},
{t:"num",q:r`Blutgruppen (Tutorium 4, Aufgabe 3): \(P(A)=0.42\), \(P(B)=0.10\), \(P(AB)=0.04\), \(P(0)=0.44\). \(P(R^+\mid A)=P(R^+\mid0)=0.85\), \(P(R^+\mid B)=0.8\), \(P(R^+\mid AB)=0.75\). Berechne \(P(R^+)\) und \(P(AB\mid R^+)\).`,
f:[{l:"P(R⁺) =",a:.841},{l:"P(AB | R⁺) =",a:.03/.841}],why:r`\(P(R^+)=0.85\cdot0.42+0.8\cdot0.1+0.75\cdot0.04+0.85\cdot0.44=0.841\). \(P(AB\mid R^+)=\frac{0.75\cdot0.04}{0.841}=\frac{0.03}{0.841}=0.036\).`},
{t:"num",q:r`Befristete Verträge (Tutorium 4, Aufgabe 4): \(P(E_2)=0.7\); \(P(\text{Bef}\mid E_1)=0.3\), \(P(\text{Bef}\mid E_2)=0.1\), \(P(\text{Bef}\mid E_3)=0.05\); außerdem \(P(\text{Bef}\cap E_1)=0.06\). Berechne \(P(E_1)\), \(P(\text{Bef})\), \(P(E_3\mid\text{Bef})\).`,
f:[{l:"P(E₁) =",a:.2},{l:"P(Bef) =",a:.135},{l:"P(E₃ | Bef) =",a:.005/.135}],why:r`\(P(E_1)=\frac{0.06}{0.3}=0.2\), \(P(E_3)=1-0.2-0.7=0.1\). \(P(\text{Bef})=0.3\cdot0.2+0.1\cdot0.7+0.05\cdot0.1=0.135\). \(P(E_3\mid\text{Bef})=\frac{0.005}{0.135}=0.037\).`},
{t:"num",q:r`Wasserbomben (Testat 3, Aufgabe 5): Wurfrichtung rechts/mitte/links mit 0.4/0.25/0.35; Abfangwahrscheinlichkeit 0.5/0.2/0.2. (1) \(P\)(Zielscheibe getroffen)? (2) \(P\)(mitte | getroffen)?`,
f:[{l:"P(trifft) =",a:.68},{l:"P(Mitte | trifft) =",a:.2/.68}],why:r`Treffen = <b>nicht</b> abgefangen: \(0.4\cdot0.5+0.25\cdot0.8+0.35\cdot0.8=0.2+0.2+0.28=0.68\). Bayes: \(\frac{0.25\cdot0.8}{0.68}=0.294\). Falle: mit der Abfang- statt der Durchkomm-Wahrscheinlichkeit rechnen.`},
{t:"num",q:r`Sonnenbrand (Testat 3, Aufgabe 8): \(P(A_2)=0.2\), \(P(A_3)=0.2\); \(P(\text{Brennen}\mid A_1)=0.1\), \(\mid A_2)=0.6\), \(\mid A_3)=0.9\). Gesucht \(P(A_1)\), \(P(\text{Brennen})\), \(P(A_3\mid\text{Brennen})\).`,
f:[{l:"P(A₁) =",a:.6},{l:"P(Brennen) =",a:.36},{l:"P(A₃ | Brennen) =",a:.5}],why:r`\(P(A_1)=1-0.2-0.2=0.6\). \(0.1\cdot0.6+0.6\cdot0.2+0.9\cdot0.2=0.06+0.12+0.18=0.36\). \(\frac{0.18}{0.36}=0.5\).`},
{t:"idea",h:"Warum man Bedingungen nicht verwechseln darf (Tutorium 4, Aufgabe 5)",de:r`
<p>60 % der Infizierten über 60 waren geimpft — also schützt die Impfung nicht? <b>Falsch gedacht.</b> Das ist \(P(G\mid I)\). Die Schutzwirkung zeigt \(P(I\mid G)\) im Vergleich zu \(P(I\mid\bar G)\). Mit 22 Mio. Menschen, 91 % geimpft, 1 Mio. Infizierten:</p>
<p>\(P(I\mid G)=\frac{600\,000}{20\,020\,000}=0.030\) und \(P(I\mid\bar G)=\frac{400\,000}{1\,980\,000}=0.200\). Geimpfte infizieren sich also viel seltener. Bei nur 50 % Impfquote wären es 0.055 gegenüber 0.036 — dann spräche das gegen einen Schutz.</p>`,
tr:r`P(G|I) ile P(I|G) aynı şey değildir! Aşının koruyup korumadığını görmek için P(I|G) ile P(I|Ḡ) karşılaştırılır.`},
{t:"ex",h:"Ziegenproblem (Tutorium 4, Aufgabe 6) — zum Merken",q:r`Drei Tore, ein Auto. Du wählst Tor 1. Der Moderator öffnet immer ein Ziegen-Tor — hier Tor 2. Wechseln auf Tor 3?`,
steps:[r`\(P(M_2\mid T_1)=\frac12\), \(P(M_2\mid T_2)=0\), \(P(M_2\mid T_3)=1\); jeweils \(P(T_i)=\frac13\).`,r`Totale W.: \(P(M_2)=\frac12\cdot\frac13+0+1\cdot\frac13=\frac12\).`,r`Bayes: \(P(T_3\mid M_2)=\frac{1\cdot\frac13}{\frac12}=\frac23\).`],a:r`Wechseln gewinnt mit 2/3, Bleiben nur mit 1/3.`},
{t:"exam",h:"Probeklausur Aufgabe 3 — Lernstrategien",src:"Probeklausur A-Teil",q:r`\(P(\text{Bestehen})=0.7\). Unter den Bestehern: Strategie 1 mit 80 %, Strategie 2 mit 15 %. Unter den Nicht-Bestehern: Strategie 1 mit 10 %, Strategie 2 mit 20 %. Strategie 3 = gar nicht lernen.`,
parts:[{q:r`(a) Berechnen Sie \(P(\bar B)\), \(P(A_3\mid B)\), \(P(A_3\mid\bar B)\) und \(P(A_3)\).`,p:7,s:r`\(P(\bar B)=0.3\). \(P(A_3\mid B)=1-0.8-0.15=0.05\). \(P(A_3\mid\bar B)=1-0.1-0.2=0.7\).<br>\(P(A_3)=0.05\cdot0.7+0.7\cdot0.3=0.035+0.21=0.245\).`},
{q:r`(b) Franziska wählt Strategie 2. Mit welcher Wahrscheinlichkeit besteht sie? Lösungsweg angeben.`,p:2,s:r`Gesucht \(P(B\mid A_2)\). \(P(A_2)=0.15\cdot0.7+0.2\cdot0.3=0.165\). \(P(B\mid A_2)=\frac{0.15\cdot0.7}{0.165}=\frac{0.105}{0.165}=0.636\) (Musterlösung: 0.6364).`},
{q:r`(c) Wahrscheinlichkeit, dass unter 10 unabhängig befragten Studierenden mindestens eine Person nicht bestanden hat? So weit wie möglich vereinfachen.`,p:2,s:r`\(X\sim B(10,\,0.3)\) = Anzahl Nicht-Besteher. \(P(X\ge1)=1-P(X=0)=1-0.7^{10}=0.972\). (Binomialverteilung → Tag 3.)`}]}
]});
