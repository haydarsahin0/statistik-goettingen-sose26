/* ================= TAG 1 · Daten beschreiben ================= */

L({id:"1.1",day:1,no:1,title:"Spielregeln & Mathe-Werkzeug",min:50,rel:3,
src:["Probeklausur-Hinweise","Abschlusssitzung","Testat 0","Tutorium 1"],
goal:"Du kennst die Regeln der Klausur (Runden, Form der Lösung) und beherrschst die Rechenwerkzeuge, die später bei Maximum-Likelihood immer wieder kommen: Summen, Produkte, Logarithmus, Ableiten.",
blocks:[
{t:"idea",h:"Wie die Klausur bewertet wird",de:r`
<p>Die Klausur hat zwei Teile. Im <b>A-Teil</b> (75 Punkte, 100 Minuten) rechnest du auf Papier. Im <b>B-Teil</b> (45 Punkte, 60 Minuten) arbeitest du mit R am Computer. Inhalt sind <b>Vorlesungen, Tutorien und Übungen</b> — also alles in diesem Plan.</p>
<ul>
<li>Nur das <b>Endergebnis</b> kommt ins Lösungskästchen — außer die Aufgabe sagt „Geben Sie Ihren Lösungsweg an“. Dann zählt der Weg!</li>
<li><b>Nie zwei Lösungen</b> hinschreiben. Falsches durchstreichen.</li>
<li>Findest du eine Aufgabe widersprüchlich: „<i>nicht lösbar</i>“ ins Kästchen + Begründung ins Feld am Ende.</li>
<li>Kugelschreiber oder Tinte. Bleistift, Grün und Rot werden <b>nicht</b> gewertet.</li>
</ul>`,
tr:r`Sınav iki bölüm: A (kâğıt üzerinde hesap, 75 puan) ve B (R ile bilgisayarda, 45 puan). Kutuya sadece sonucu yaz; soru „Lösungsweg“ istiyorsa yolu da yaz. Asla iki farklı cevap bırakma.`},
{t:"rule",k:"Rundungsregel · kostet sonst Punkte",de:r`Zwischenergebnisse mit <b>mindestens 4</b> Nachkommastellen, Endergebnis <b>kaufmännisch auf 3</b> Nachkommastellen. Erlaubt sind auch vollständig gekürzte Brüche (z. B. 1/5) oder Ausdrücke wie \(\log 4\) oder \(\sqrt 2\).`,
tr:r`Ara sonuçlarda en az 4 ondalık, son sonuçta 3 ondalık (5 ve üstü yukarı yuvarlanır). Tam sadeleşmiş kesir de kabul edilir.`},
{t:"mc",q:r`Du rechnest \(P = 0.021/0.033\). Was schreibst du ins Lösungskästchen?`,o:["0.63","0.636","0.6364","0.64"],k:1,why:r`\(0.021/0.033 = 0.636363\ldots\) → auf 3 Nachkommastellen: <b>0.636</b>. (0.6364 wäre ein Zwischenergebnis, als Endergebnis aber „zu genau“ — sicher ist genau das verlangte Format.) Alternativ ginge der gekürzte Bruch 7/11.`},
{t:"idea",h:"Summenzeichen: die Regeln, die du wirklich brauchst",de:r`
<p>Das Summenzeichen ist nur eine Abkürzung: \(\sum_{i=1}^{n} x_i = x_1 + x_2 + \dots + x_n\). Drei Regeln reichen für fast alles:</p>`},
{t:"formula",h:"Rechenregeln Summe",tex:r`\sum_{i=1}^{n} c = n\cdot c \qquad \sum_{i=1}^{n} c\,x_i = c\sum_{i=1}^{n} x_i \qquad \sum_{i=1}^{n}(x_i+y_i)=\sum x_i+\sum y_i`,
note:r`Nur Dinge <b>ohne Index i</b> dürfen vor das Summenzeichen. \(\sum \frac{x}{i^2} \neq \frac{1}{i^2}\sum x\)!`,
tr:r`Sabit sayı (i indeksi olmayan) toplamın dışına çıkar; i'ye bağlı olan çıkamaz.`},
{t:"ex",h:"Warum ist die Summe der Abweichungen immer 0?",q:r`Zeige: \(\sum_{i=1}^{n}(x_i-\bar x)=0\), wobei \(\bar x=\frac1n\sum x_i\). (Testat 0, Tutorium 1)`,
steps:[r`Summe aufteilen: \(\sum (x_i-\bar x) = \sum x_i - \sum \bar x\).`,
r`\(\bar x\) hat keinen Index → \(\sum_{i=1}^n \bar x = n\bar x\).`,
r`\(n\bar x = n\cdot \frac1n\sum x_i = \sum x_i\).`,
r`Also \(\sum x_i - \sum x_i = 0\).`],a:r`\(\sum_{i=1}^{n}(x_i-\bar x)=0\) — die Abweichungen nach links und rechts heben sich auf.`},
{t:"formula",h:"Produktzeichen",tex:r`\prod_{i=1}^{n} c = c^{\,n} \qquad \prod_{i=1}^{n} a^{x_i} = a^{\sum_{i=1}^n x_i} \qquad \prod_{i=1}^{n} (a_i b_i) = \prod a_i \cdot \prod b_i`,
note:r`Diese drei Regeln brauchst du bei <b>jeder</b> Likelihood-Funktion (Tag 4).`,
tr:r`Çarpımda sabit sayı n. kuvvete çıkar; aynı tabanın üsleri toplanır. Likelihood'da her zaman lazım.`},
{t:"num",q:r`Gegeben \(x_1=1,\ x_2=2,\ x_3=3\) und \(f(x_i,\theta)=\theta^{x_i}e^{-\theta}\). Es gilt \(\prod_{i=1}^3 f(x_i,\theta)=\theta^{a}\,e^{-b\theta}\). Bestimme \(a\) und \(b\). (Testat 0)`,
f:[{l:"a =",a:6,tol:0},{l:"b =",a:3,tol:0}],why:r`\(\prod \theta^{x_i} = \theta^{1+2+3}=\theta^6\) und \(\prod e^{-\theta} = (e^{-\theta})^3 = e^{-3\theta}\). Ergebnis: \(\theta^6 e^{-3\theta}\).`},
{t:"formula",h:"Logarithmus-Regeln (log = ln)",tex:r`\log(ab)=\log a+\log b \quad \log\tfrac ab=\log a-\log b \quad \log a^k = k\log a \quad \log e^{x}=x \quad \log\prod_{i} x_i=\sum_i \log x_i`,
note:r`In dieser Veranstaltung ist \(\log\) immer der <b>natürliche</b> Logarithmus (R: <code>log()</code>).`,
tr:r`Logaritma çarpımı toplama, üssü çarpana çevirir. Bu yüzden likelihood'un logaritmasını alırız: çarpım → toplam.`},
{t:"mc",q:r`Vereinfache \(\log \sqrt[3]{\dfrac{q^5}{s^2}}\). (Testat 0)`,o:[r`\(3\log q^5 - 3\log s^2\)`,r`\(\tfrac53\log q-\tfrac23\log s\)`,r`\(\tfrac35\log q-\tfrac32\log s\)`],k:1,why:r`\(\sqrt[3]{\cdot}=(\cdot)^{1/3}\) → \(\tfrac13(\log q^5-\log s^2)=\tfrac13(5\log q-2\log s)=\tfrac53\log q-\tfrac23\log s\).`},
{t:"mc",q:r`Fasse zusammen: \(3\log a^2+\log a^2-\log a^5-\log 27-\log b^3\). (Testat 0)`,o:[r`\(\log\frac{4}{(3ab)^3}\)`,r`\(\log(a^6+a^2-a^5-27-b^3)\)`,r`\(3\log\frac{a}{3b}\)`],k:2,why:r`\(6\log a+2\log a-5\log a = 3\log a\). \(\log 27=3\log 3\), \(\log b^3=3\log b\). Also \(3(\log a-\log 3-\log b)=3\log\frac{a}{3b}\).`},
{t:"formula",h:"Ableitungsregeln",tex:r`(x^k)'=kx^{k-1}\quad (\log x)'=\tfrac1x\quad (e^{cx})'=c\,e^{cx}\quad (\log(1-p))'=\tfrac{-1}{1-p}\quad (uv)'=u'v+uv'`,
note:r`Kettenregel: \((g(h(x)))' = g'(h(x))\cdot h'(x)\). Beispiel: \(\frac{d}{d\mu}(\log x_i-\mu)^2 = 2(\log x_i-\mu)\cdot(-1)\).`},
{t:"ex",h:"Das wichtigste Muster der ganzen Klausur",q:r`Gegeben \(\ell(\lambda)=\Big(\sum_{i=1}^n x_i\Big)\log\lambda-n\lambda-\sum_{i=1}^n\log(x_i!)\). Leite ab und finde die Extremstelle \(\lambda^*\). (Testat 0, Aufgabe 11)`,
steps:[r`Nur \(\lambda\) ist variabel. \(\sum x_i\) und \(\sum\log(x_i!)\) sind Konstanten.`,
r`\(\frac{\partial \ell}{\partial\lambda} = \frac{1}{\lambda}\sum x_i - n - 0\).`,
r`Nullsetzen: \(\frac{1}{\lambda^*}\sum x_i - n = 0 \iff \frac{1}{\lambda^*}\sum x_i = n\).`,
r`Auflösen: \(\lambda^* = \frac1n\sum x_i = \bar x\).`],a:r`\(\lambda^*=\bar x\) — das ist schon der ML-Schätzer der Poissonverteilung (Tag 4).`,
tr:r`Log-likelihood türevini al, sıfıra eşitle, parametreyi yalnız bırak. Bu kalıp sınavda hep çıkar.`},
{t:"mc",q:r`Berechne \(\int \frac{1}{\sqrt[3]{x^2}}\,dx\) für \(x\neq0\). (Testat 0)`,o:[r`\(\frac{1}{\sqrt{x^2}}+C\)`,r`\(2\sqrt[3]{x}+C\)`,r`\(3\sqrt[3]{x}+C\)`],k:2,why:r`\(\frac{1}{\sqrt[3]{x^2}}=x^{-2/3}\). Stammfunktion: \(\frac{x^{1/3}}{1/3}=3x^{1/3}=3\sqrt[3]{x}\).`},
{t:"ex",h:"Doppelintegral (kommt bei gemeinsamen Dichten)",q:r`Berechne \(\int_1^3\int_0^1 (x^2-axy)\,dy\,dx\). (Testat 0)`,
steps:[r`Innen nach \(y\) integrieren, \(x\) ist konstant: \(\int_0^1 (x^2-axy)\,dy=\big[x^2y-\tfrac{a x y^2}{2}\big]_0^1 = x^2-\tfrac{ax}{2}\).`,
r`Außen nach \(x\): \(\int_1^3\big(x^2-\tfrac{ax}{2}\big)dx=\big[\tfrac{x^3}{3}-\tfrac{ax^2}{4}\big]_1^3\).`,
r`Einsetzen: \(\big(9-\tfrac{9a}{4}\big)-\big(\tfrac13-\tfrac a4\big)=\tfrac{26}{3}-2a\).`],a:r`\(\frac{26}{3}-2a\)`},
{t:"trap",items:[r`Ergebnis auf 2 statt 3 Nachkommastellen gerundet → Punktabzug.`,r`Zu früh gerundet (z. B. mit 0.64 statt 0.6364 weitergerechnet) → Folgefehler.`,r`Eine Teilaufgabe übersehen — lies am Ende jede Aufgabe noch einmal von (a) bis zum letzten Buchstaben.`,r`„Begründen Sie“ mit einem Zirkelschluss beantwortet („weil es so ist“). Eine Begründung nennt immer die <b>Regel</b> oder die <b>Zahl</b>, aus der es folgt.`],
tr:r`En sık puan kaybı: yanlış yuvarlama, alt soruyu atlamak, „Begründen“ sorusunda gerçek bir gerekçe (kural veya sayı) yazmamak.`}
]});

L({id:"1.2",day:1,no:2,title:"Grundbegriffe & Skalenniveaus",min:50,rel:3,
src:["V01","Tutorium 1","Testat 1","Probeklausur A1, A2"],
goal:"Du kannst für jedes Merkmal sagen: diskret oder stetig? nominal, ordinal oder kardinal? — und du weißt, welches Stichprobenverfahren passt.",
blocks:[
{t:"terms",h:"Die Grundwörter",items:[
["Statistische Einheit","istatistik birimi","Das Objekt, an dem gemessen wird (Person, Firma, Wohnung …)."],
["Grundgesamtheit / Population","ana kütle","Menge <b>aller</b> Einheiten, die für die Frage relevant sind."],
["Stichprobe","örneklem","Teilmenge der Grundgesamtheit, die wirklich untersucht wird."],
["Merkmal","değişken / özellik",r`Eigenschaft der Einheit, z. B. Alter. Schreibweise: Großbuchstabe \(X\).`],
["Merkmalsausprägung","değer",r`Konkreter Wert bei einer Einheit, z. B. 21 Jahre. Schreibweise: Kleinbuchstabe \(x\).`]]},
{t:"ex",h:"Einmal durchspielen",q:r`Wahlumfrage vor der Bundestagswahl: 1000 Personen werden nach ihrer Partei gefragt.`,
steps:[r`Einheit: eine wahlberechtigte Person.`,r`Grundgesamtheit: alle Wahlberechtigten der nächsten Bundestagswahl.`,r`Stichprobe: die 1000 befragten Personen.`,r`Merkmal: Parteipräferenz — Ausprägungen: CDU/CSU, SPD, Grüne, …`]},
{t:"idea",h:"Diskret oder stetig?",de:r`
<p><b>Diskret</b>: endlich viele oder <i>abzählbar unendlich</i> viele Werte (0, 1, 2, …). Beispiel: Anzahl Likes, Parteipräferenz.</p>
<p><b>Stetig</b> (auch „metrisch“): jeder Wert in einem Intervall ist möglich (reelle Zahlen). Beispiel: Körpergröße, Gewinn, Liter Bier.</p>
<p>In der Praxis wird Stetiges gerundet gemessen (170 cm) und trotzdem als stetig behandelt („quasi-stetig“).</p>`,
tr:r`Kesikli (diskret): sayılabilir değerler (0,1,2,… veya kategoriler). Sürekli (stetig): bir aralıktaki her reel değer mümkün (boy, kilo, litre).`},
{t:"idea",h:"Die drei Skalenniveaus",de:r`
<div class="tbl"><table><thead><tr><th class="l">Skala</th><th>Häufigkeiten</th><th>Rangordnung</th><th>Abstände / Quotienten</th><th class="l">Beispiele</th></tr></thead><tbody>
<tr><td class="l"><b>nominal</b></td><td>ja</td><td>nein</td><td>nein</td><td class="l">Partei, Nationalität, Mensa-Standort</td></tr>
<tr><td class="l"><b>ordinal</b></td><td>ja</td><td>ja</td><td>nein</td><td class="l">Schulnote, Zufriedenheit 1–7, Rang</td></tr>
<tr><td class="l"><b>kardinal</b> (metrisch)</td><td>ja</td><td>ja</td><td>ja</td><td class="l">Alter, Einkommen, Körpergröße</td></tr></tbody></table></div>`,
tr:r`Nominal: sadece isim/kategori. Ordinal: sıralanabilir ama aralıklar anlamsız. Kardinal (metrik): aralıklar ve oranlar anlamlı.`},
{t:"rule",de:r`Frag dich zwei Dinge: <b>Kann ich die Werte sinnvoll ordnen?</b> Nein → nominal. Ja → <b>Sind die Abstände sinnvoll interpretierbar?</b> Nein → ordinal. Ja → kardinal.`,tr:r`İki soru sor: Sıralanabiliyor mu? Aralıklar anlamlı mı?`},
{t:"mc",q:r`„Zufriedenheit mit dem Essensangebot auf einer ganzzahligen Skala von 1 (gar nicht) bis 7 (sehr zufrieden)“. Skalenniveau und Typ? (Testat 1)`,o:["nominal, diskret","ordinal, diskret","kardinal, stetig","kardinal, diskret"],k:1,why:r`Man kann ordnen (7 &gt; 6), aber der Abstand „zwischen 2 und 3“ bedeutet nicht dasselbe wie „zwischen 6 und 7“. Zahlen als Kategorien verleiten zu „kardinal“ — das ist die typische Falle (Tutorium 1, Aufgabe 13).`},
{t:"mc",q:r`„Monatseinkommen in Euro“? (Testat 1)`,o:["ordinal, diskret","kardinal, stetig (quasi-stetig)","nominal, stetig"],k:1,why:r`Abstände und Verhältnisse sind sinnvoll (2000 € ist doppelt so viel wie 1000 €) → kardinal. Sehr viele mögliche Werte → wird als stetig behandelt.`},
{t:"mc",q:r`„Präferierter Mensastandort (Zentralmensa, Nordmensa, Mensa am Turm)“ — welche Lagemaße sind sinnvoll? (Testat 1, Aufgabe 3)`,o:["nur der Modus","Modus und Median","Modus, Median und arithmetisches Mittel"],k:0,why:r`Nominal → keine Ordnung → nur der Modus (häufigster Wert). Für die Zufriedenheit 1–7 (ordinal) wären Modus <b>und</b> Median sinnvoll.`},
{t:"idea",h:"Wie zieht man eine Stichprobe?",de:r`
<p>Eine Stichprobe soll <span class="hl">repräsentativ</span> sein: keine systematischen Unterschiede zur Grundgesamtheit.</p>
<ul>
<li><b>Einfache Zufallsstichprobe</b>: Ziehen ohne Zurücklegen, jedes Element hat die gleiche Chance, jede Stichprobe ist gleich wahrscheinlich.</li>
<li><b>Geschichtete Stichprobe</b>: Grundgesamtheit in Gruppen (Schichten) teilen, z. B. nach Studiengang, und <i>in jeder Schicht</i> zufällig ziehen. Voraussetzung: Anteile der Gruppen bekannt.</li>
<li><b>Klumpenstichprobe</b>: Man zieht zufällig ganze Klumpen (Schulklassen, Städte, Familien) und untersucht diese. Günstiger. Klumpen sollen untereinander ähnlich, innen aber vielfältig sein.</li>
<li><b>Bewusste Auswahl (Quotenverfahren)</b>: Vorab festgelegte Quoten müssen erfüllt sein.</li></ul>`,
tr:r`Tabakalı (geschichtet): her gruptan ayrı rastgele seçim. Küme (Klumpen): rastgele bütün gruplar (sınıflar, şehirler) seçilir. Kota: önceden belirlenen oranlar doldurulur.`},
{t:"mc",q:r`Der Anteil der Befragten aus jedem Studiengang soll dem Anteil an der gesamten Studierendenschaft entsprechen. Welche Methode? (Testat 1, Aufgabe 2)`,o:["Einfache Zufallsstichprobe","Geschichtete Stichprobe / Quotenverfahren","Klumpenstichprobe","Keines davon"],k:1,why:r`Die Gruppenanteile sind vorgegeben → Schichtung bzw. Quoten. Beim Vergleichstest „nur Schulen in Göttingen“ für ganz Deutschland wäre es dagegen eine <b>Klumpenstichprobe</b> (Tutorium 1).`},
{t:"idea",h:"Störvariablen kontrollieren",de:r`
<p>Eine <b>Störvariable</b> beeinflusst das Ergebnis, interessiert uns aber nicht (z. B. Vorwissen, wenn wir eine Lehrmethode testen). Drei Wege, sie zu kontrollieren:</p>
<ul><li><b>Homogenisierung</b>: in Teilgruppen mit gleicher Störvariable zerlegen.</li><li><b>Randomisierung</b>: zufällig in Gruppe mit/ohne Maßnahme einteilen.</li><li><b>Statistische Modellierung</b>: Störvariable im Modell berücksichtigen.</li></ul>`},
{t:"mc",q:r`Welche Aussagen sind richtig? (Tutorium 1, Aufgabe 14 — dort sollten falsche Sätze korrigiert werden)`,o:[r`Ein diskretes Merkmal kann nur endlich viele Werte annehmen.`,r`Ein Merkmal mit endlich vielen Ausprägungen ist diskret.`,r`Quantitative Merkmale sind stets stetig.`,r`Ein Modell ist eine vereinfachte Beschreibung der Realität.`],k:[1,3],why:r`Diskret heißt endlich <b>oder abzählbar unendlich</b> (Autos an der Autobahn zählen). Quantitative Merkmale können diskret (Anzahl) oder stetig (Gewicht) sein.`},
{t:"exam",h:"Probeklausur Aufgabe 2 (a) und 1 (a)",src:"Probeklausur A-Teil",q:r`Bar „BierWirdGeschafft“: \(X\) = getrunkene Biermenge in Litern, \(Y\) = Herkunft der Gäste (BY oder NRW). Außerdem: 20 Vorhersagen einer Wahrsagerin, kodiert 1 = korrekt, 0 = falsch.`,
parts:[{q:r`(a) Geben Sie für \(X\) und \(Y\) an, ob ein diskretes oder stetiges Merkmal vorliegt und welches Skalenniveau zugrunde liegt.`,p:4,s:r`\(X\): <b>stetig</b>, metrisch skaliert (Verhältnisskala).<br>\(Y\): <b>diskret</b>, nominal skaliert.`},
{q:r`(b) Geben Sie das Skalenniveau des Merkmals „Korrektheit der Vorhersagen“ (0/1) an.`,p:1,s:r`<b>Ordinalskaliert / binär</b> (Musterlösung). Ein 0/1-Merkmal ist ein Sonderfall: man kann es als binär bezeichnen.`}]}
]});

L({id:"1.3",day:1,no:3,title:"Häufigkeiten, Verteilungsfunktion & Histogramm",min:65,rel:3,
src:["V02","Tutorium 2","Testat 1","Probeklausur A2"],
goal:"Du kannst Häufigkeitstabellen ausfüllen, die empirische Verteilungsfunktion zeichnen und aus einem Histogramm Anteile ablesen — auch für halbe Klassen.",
blocks:[
{t:"formula",h:"Häufigkeiten",tex:r`h_j=\text{Anzahl der }x_i=a_j \qquad f_j=\frac{h_j}{n} \qquad H_j=h_1+\dots+h_j \qquad F_j=\frac{H_j}{n}`,
parts:[["h_j","absolute Häufigkeit"],["f_j","relative Häufigkeit (Anteil)"],["H_j","absolute Summenhäufigkeit (kumuliert)"],["F_j","relative Summenhäufigkeit"]],
tr:r`h: mutlak frekans, f: göreli frekans (oran), H ve F: birikimli (kümülatif) frekanslar.`},
{t:"ex",h:"Tabelle vervollständigen (Tutorium 2, Aufgabe 2)",q:r`Semesterzahlen von \(n=23\) Klausurteilnehmern:
<div class="tbl"><table><tr><th>Semester</th><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><th>\(h_j\)</th><td>1</td><td>7</td><td>5</td><td>5</td><td>1</td><td>4</td></tr></table></div>`,
steps:[r`\(n = 1+7+5+5+1+4 = 23\).`,r`\(f_j=h_j/23\): 1/23, 7/23, 5/23, 5/23, 1/23, 4/23.`,r`Kumulieren: \(H_j\) = 1, 8, 13, 18, 19, 23.`,r`\(F_j = H_j/23\): 1/23, 8/23, 13/23, 18/23, 19/23, 1.`]},
{t:"num",q:r`Mit der Tabelle oben: Anteil der Studierenden mit Semesterzahl (i) <b>größer als 3</b>, (ii) <b>mindestens 3</b>, (iii) <b>kleiner als 4</b>, (iv) <b>nicht größer als 5</b>. Brüche wie 15/23 sind erlaubt.`,
f:[{l:"(i) =",a:15/23},{l:"(ii) =",a:22/23},{l:"(iii) =",a:8/23},{l:"(iv) =",a:18/23}],
why:r`(i) „größer als 3“ = 4,5,6,7: \(1-F(3)=1-\tfrac{8}{23}=\tfrac{15}{23}\). (ii) „mindestens 3“ = \(\ge 3\): \(1-\tfrac1{23}=\tfrac{22}{23}\). (iii) „kleiner als 4“ = \(\le 3\): \(\tfrac{8}{23}\). (iv) „nicht größer als 5“ = \(\le5\): \(\tfrac{18}{23}\).<br><b>Das ist die Off-by-one-Falle:</b> Bei diskreten Werten ist „&gt; 3“ nicht dasselbe wie „≥ 3“.`},
{t:"idea",h:"Die empirische Verteilungsfunktion",de:r`
<p>\(\hat F(x)\) = Anteil der Beobachtungen, die <b>kleiner oder gleich</b> \(x\) sind. Sie ist eine <b>Treppenfunktion</b>: links 0, rechts 1, und sie springt an jedem beobachteten Wert um dessen relative Häufigkeit nach oben.</p>`,
tr:r`Ampirik dağılım fonksiyonu: x'e eşit veya küçük gözlemlerin oranı. Merdiven şeklinde; her gözlem değerinde göreli frekansı kadar zıplar.`},
{t:"fig",kind:"ecdf",h:"Beispiel: Biermengen aus der Probeklausur",x:[0,20],xt:[0,4,8.5,12,15.7,20],xl:"Biermenge in Litern",pts:[[4,.3],[8.5,.7],[12,.9],[15.7,1]],lab:["0.3","0.7","0.9","1"],
cap:"Werte: 4.0 (3×), 8.5 (4×), 12.0 (2×), 15.7 (1×), n = 10. Voller Punkt = der Wert gehört dazu (rechtsstetig), leerer Punkt = gehört nicht dazu."},
{t:"formula",h:"Empirische Verteilungsfunktion (Probeklausur A2)",tex:r`\hat F(x)=\begin{cases}0 & x\lt 4\\ 0.3 & 4\le x\lt 8.5\\ 0.7 & 8.5\le x\lt 12\\ 0.9 & 12\le x\lt 15.7\\ 1 & x\ge 15.7\end{cases}`,sheet:false},
{t:"trap",h:"So verlierst du beim Zeichnen Punkte",items:[r`Treppenstufen senkrecht verbinden — <b>nicht</b> machen.`,r`Den vollen Punkt links an jeder Stufe vergessen (der Wert gehört zur oberen Stufe: \(\hat F(4)=0.3\)).`,r`Den Anfang bei 0 (links) und die 1 (rechts, bis unendlich) nicht andeuten.`,r`Achsen nicht beschriften.`]},
{t:"idea",h:"Histogramm: die Fläche zählt, nicht die Höhe",de:r`
<p>Für stetige Merkmale teilt man in Klassen \((c_{j-1},c_j]\) ein. Im <b>Histogramm</b> ist die <span class="hl">Fläche</span> jeder Säule gleich der relativen Häufigkeit. Die Gesamtfläche ist 1.</p>
<p>Darum ist die Höhe die <b>Dichte</b>:</p>`,
tr:r`Histogramda sütunun ALANI göreli frekansa eşittir. Yükseklik = yoğunluk = göreli frekans / sınıf genişliği. Toplam alan 1.`},
{t:"formula",h:"Höhe im Histogramm",tex:r`\text{Dichte}_j=\frac{f_j}{c_j-c_{j-1}}=\frac{h_j}{n\cdot(c_j-c_{j-1})}`,parts:[["f_j","relative Häufigkeit der Klasse"],["c_j-c_{j-1}","Klassenbreite"]],note:r`Säulendiagramm (Höhe = Häufigkeit) ist bei <b>ungleichen</b> Klassenbreiten verzerrt. In dieser Veranstaltung ist das normierte Histogramm der Goldstandard.`},
{t:"fig",kind:"hist",h:"Körpergrößen von 20 Personen (Tutorium 2, Aufgabe 1)",x:[155,190],y:[0,.08],xt:[160,165,170,175,180,185],yt:[0,.02,.04,.06,.08],xl:"Körpergröße in cm",
bars:[[160,165,.01,"1"],[165,170,.03,"3"],[170,175,.05,"5"],[175,180,.07,"7"],[180,185,.04,"4"]],shade:[[170,172,.05]],
cap:"Über den Säulen: absolute Häufigkeit. Höhe = h / (n · 5), z. B. 7/(20·5) = 0.07. Gelb: der Teil (170, 172] der dritten Klasse."},
{t:"ex",h:"Anteil in einem Intervall, das eine Klasse schneidet",q:r`Schätze mit dem Histogramm den Anteil der Personen in \([160,172]\).`,
steps:[r`Annahme: Innerhalb einer Klasse sind die Werte <b>gleichmäßig verteilt</b>.`,r`Klasse [160,165] liegt ganz drin: \(\tfrac{1}{20}\). Klasse (165,170] ganz drin: \(\tfrac{3}{20}\).`,r`Von (170,175] nur 2 von 5 cm: \(\tfrac25\cdot\tfrac{5}{20}\). Gleichwertig: Fläche = Breite · Höhe = \(2\cdot 0.05=0.10\).`,r`Summe: \(0.05+0.15+0.10=0.30\).`],a:r`Anteil ≈ 0.30`},
{t:"num",q:r`Gleiches Histogramm: Schätze den Anteil in \((173,184]\).`,f:[{l:"Anteil =",a:.61}],why:r`(173,175]: \(2\cdot0.05=0.10\). (175,180]: \(5\cdot 0.07=0.35\). (180,184]: \(4\cdot 0.04=0.16\). Summe \(0.61\).`},
{t:"idea",h:"Mittelwert aus klassierten Daten",de:r`
<p>Kennst du nur die Klassen, nimm die <b>Klassenmitte</b> \(m_j\) als Stellvertreter:</p>`},
{t:"formula",h:"Klassierte Daten",tex:r`\bar x_K=\sum_{j} f_j\,m_j \qquad s_K^2=\sum_j f_j\,(m_j-\bar x_K)^2`,parts:[["m_j","Klassenmitte, z. B. (0+10)/2 = 5"],["f_j","relative Häufigkeit der Klasse"]]},
{t:"num",q:r`Arbeitszeit pro Woche (Tutorium 2, Aufgabe 5): [0,4]: 40.2 %, (4,8]: 19.6 %, (8,12]: 21.9 %, (12,16]: 18.3 %. Berechne den Mittelwert mit Klassenmitten.`,f:[{l:r`\(\bar x_K\) =`,a:6.732}],why:r`Mitten 2, 6, 10, 14: \(0.402\cdot2+0.196\cdot6+0.219\cdot10+0.183\cdot14=6.732\). Die Varianz wäre \(s_K^2=21.112\).`},
{t:"r",h:"Dasselbe in R",code:r`
x <- c(8.5, 8.5, 4, 4, 12, 12, 8.5, 15.7, 4, 8.5)
table(x)                       # absolute Häufigkeiten
prop.table(table(x))           # relative Häufigkeiten
cumsum(prop.table(table(x)))   # F an den Sprungstellen
plot(ecdf(x))                  # empirische Verteilungsfunktion
hist(x, breaks = c(0, 10, 20), freq = FALSE, right = FALSE)`,
out:r`
x
   4  8.5   12 15.7
   3    4    2    1
   4  8.5   12 15.7
 0.3  0.7  0.9  1.0`,
notes:[[2,"<code>table()</code> zählt, wie oft jeder Wert vorkommt.","Her değerin kaç kez geçtiğini sayar."],[4,"<code>cumsum()</code> bildet die kumulierte Summe — genau die Stufenhöhen von \\(\\hat F\\).",""],[6,"<code>freq = FALSE</code> macht ein <b>normiertes</b> Histogramm (Dichte auf der y-Achse). <code>right = FALSE</code> heißt: Klassen sind links geschlossen, [0,10).","freq=FALSE → y ekseninde yoğunluk. right=FALSE → aralıklar [a,b) şeklinde."]]},
{t:"exam",h:"Probeklausur Aufgabe 2 (b), (c) — Bier",src:"Probeklausur A-Teil",q:r`Werte \(x_i\) (Liter): 8.5, 8.5, 4.0, 4.0, 12.0, 12.0, 8.5, 15.7, 4.0, 8.5. Hinweis: \(\sum x_i=85.7\), \(\sum x_i^2=871.49\).`,
parts:[{q:r`(b) Zeichnen Sie die empirische Verteilungsfunktion für \(X\).`,p:6,s:r`Sprünge bei 4 (auf 0.3), 8.5 (auf 0.7), 12 (auf 0.9), 15.7 (auf 1). Links davon 0. Voller Punkt jeweils am linken Ende der Stufe, Achsen beschriften (x: Biermenge in l, y: \(\hat F(x)\)).`},
{q:r`(c) Klassieren Sie in \(K_1=[0,10)\) und \(K_2=[10,20]\) und bestimmen Sie den Mittelwert für die klassierten Daten.`,p:4,s:r`\(n(K_1)=7\) (dreimal 4.0, viermal 8.5), \(n(K_2)=3\). Klassenmitten \(m_1=5\), \(m_2=15\).<br>\(\bar x_K=\frac1{10}(7\cdot5+3\cdot15)=\frac{80}{10}=8\).`},
{q:r`(Zusatz) Berechnen Sie \(\bar x\) und die empirische Varianz \(\tilde s^2\) der Originaldaten.`,p:0,s:r`\(\bar x=85.7/10=8.570\). \(\tilde s^2=\frac{871.49}{10}-8.57^2=87.149-73.4449=13.704\).`}]}
]});

L({id:"1.4",day:1,no:4,title:"Lagemaße & Quantile",min:55,rel:3,
src:["V02","Tutorium 2, 3","Testat 1","Probeklausur A1"],
goal:"Du bestimmst Modus, Median, Mittelwert und beliebige Quantile ohne Positionsfehler — und weißt, welches Maß zu welcher Skala passt.",
blocks:[
{t:"formula",h:"Arithmetisches Mittel",tex:r`\bar x=\frac1n\sum_{i=1}^n x_i=\sum_{j=1}^J a_j f_j`,note:r`Mit Häufigkeitstabelle: jede Ausprägung \(a_j\) mal ihre relative Häufigkeit \(f_j\).`},
{t:"formula",h:"Median (Daten erst sortieren!)",tex:r`x_{med}=\begin{cases}x_{(\frac{n+1}{2})} & n\text{ ungerade}\\[2pt] \tfrac12\big(x_{(\frac n2)}+x_{(\frac n2+1)}\big) & n\text{ gerade}\end{cases}`,parts:[["x_{(k)}","k-ter Wert der <b>sortierten</b> Liste"]],note:r`Bei geradem \(n\) ist eigentlich jeder Wert im Intervall \([x_{(n/2)},x_{(n/2+1)}]\) ein Median; üblich (und in R) ist der Mittelwert der beiden.`,
tr:r`Medyan: önce sırala! n tekse ortadaki değer, n çiftse ortadaki iki değerin ortalaması.`},
{t:"formula",h:"α-Quantil",tex:r`x_\alpha=\begin{cases}x_{(\lfloor n\alpha\rfloor+1)} & n\alpha \text{ nicht ganzzahlig (aufrunden)}\\[2pt] \in[x_{(n\alpha)},\,x_{(n\alpha+1)}] & n\alpha\text{ ganzzahlig (Mitte nehmen)}\end{cases}`,note:r`Median = \(x_{0.5}\), Quartile = \(x_{0.25}, x_{0.75}\). Voraussetzung: mindestens ordinal.`},
{t:"rule",de:r`Quantil-Rezept: <b>1.</b> sortieren · <b>2.</b> \(n\cdot\alpha\) rechnen · <b>3.</b> keine ganze Zahl → aufrunden und diesen Platz nehmen; ganze Zahl → Mittel aus Platz \(n\alpha\) und \(n\alpha+1\).`,tr:r`Önce sırala, n·α hesapla; tam sayı değilse yukarı yuvarla, tam sayıysa o sıradaki ve bir sonraki değerin ortalamasını al.`},
{t:"ex",h:"Quartile im Mietspiegel (V02)",q:r`26 sortierte Nettomieten: 77.31, 104.14, 116.48, 132.24, 158.91, 163.17, <b>170.04</b>, 181.98, 183.09, 200.84, 210.55, 227.91, <b>243.44, 255.75</b>, 261.98, 263.21, 269.84, 276.60, 281.21, <b>311.87</b>, 343.30, 359.17, 361.60, 362.00, 400.05, 533.92.`,
steps:[r`\(x_{0.25}\): \(26\cdot0.25=6.5\) → nicht ganzzahlig → aufrunden auf 7 → \(x_{(7)}=170.04\).`,r`\(x_{0.5}\): \(26\cdot0.5=13\) → ganzzahlig → Mitte aus Platz 13 und 14: \(\frac{243.44+255.75}{2}=249.6\).`,r`\(x_{0.75}\): \(26\cdot0.75=19.5\) → aufrunden auf 20 → \(x_{(20)}=311.87\).`],a:r`\(x_{0.25}=170.04,\ x_{med}=249.6,\ x_{0.75}=311.87\)`},
{t:"num",q:r`Pilotstudie (Testat 1, Aufgabe 4): Mensabesuche \(a_i\) = 1, 3, 4, 5, 10 mit \(h_i\) = 1, 2, 5, 3, 1. Bestimme \(n\), Modus, Median und Mittelwert.`,
f:[{l:"n =",a:12,tol:0},{l:"x_mod =",a:4,tol:0},{l:"x_med =",a:4,tol:0},{l:"x̄ =",a:52/12}],
why:r`\(n=12\). Modus: 4 (fünfmal). Sortiert: 1, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 10 → \(n\) gerade → Mittel aus Platz 6 und 7 = \((4+4)/2=4\). \(\bar x=\frac{1+6+20+15+10}{12}=\frac{52}{12}=4.333\).`},
{t:"num",q:r`Monatseinkommen (Testat 1, Aufgabe 5): 1400, 750, 900, 1100, 900, 550, 800, 1600, 900, 7500, 1000, 600. Bestimme Modus, Median und Mittelwert.`,
f:[{l:"x_mod =",a:900,tol:0},{l:"x_med =",a:900,tol:0},{l:"x̄ =",a:1500,tol:0}],
why:r`Sortiert: 550, 600, 750, 800, 900, 900, 900, 1000, 1100, 1400, 1600, 7500. Modus 900. Median: Platz 6 und 7 → 900. Summe 18000 → \(\bar x=1500\).<br>Der eine Ausreißer 7500 zieht den Mittelwert nach oben, der Median bleibt stabil: <span class="hl">Der Median ist robust gegenüber Ausreißern.</span>`},
{t:"idea",h:"Welches Lagemaß wann?",de:r`
<ul><li><b>Modus</b>: jede Skala (auch nominal). Bei stetigen Daten meist nicht sinnvoll.</li>
<li><b>Median</b>: ab ordinal.</li>
<li><b>Arithmetisches Mittel</b>: kardinal. Auch sinnvoll für binäre 0/1-Daten (dann = Anteil der Einsen).</li></ul>
<p><b>Form der Verteilung:</b> symmetrisch: \(\bar x\approx x_{med}\approx x_{mod}\). <b>Rechtsschief</b> (= linkssteil, langer Schwanz nach rechts): \(\bar x \gt x_{med}\gt x_{mod}\). <b>Linksschief</b> (= rechtssteil): \(\bar x\lt x_{med}\lt x_{mod}\).</p>`,
tr:r`Mod her ölçekte; medyan en az sıralı; ortalama metrik (ve 0/1) verilerde. Sağa çarpık dağılımda ortalama > medyan > mod.`},
{t:"fig",kind:"density",h:"Rechtsschief = linkssteil",dist:"chisq",p:{df:4},x:[0,16],y:[0,.2],xl:"x",yl:"Dichte",marks:[[2,"Modus"],[3.36,"Median"],[4,"Mittel"]],cap:"Der lange Schwanz nach rechts zieht das Mittel am weitesten mit. Merke: „schief“ zeigt auf den Schwanz, „steil“ auf die steile Seite."},
{t:"mc",q:r`Für eine Verteilung gilt \(\bar x=5.1\), \(x_{med}=4.2\), \(x_{mod}=3.5\). Wie ist sie?`,o:["symmetrisch","rechtsschief / linkssteil","linksschief / rechtssteil"],k:1,why:r`\(\bar x\gt x_{med}\gt x_{mod}\) → langer Schwanz rechts → rechtsschief (= linkssteil).`},
{t:"formula",h:"Transformation & Schichten",tex:r`y_i=a+bx_i\Rightarrow \bar y=a+b\bar x \qquad y_i=g(x_i),\ g\text{ monoton}\Rightarrow y_{med}=g(x_{med}) \qquad \bar x=\frac1n\sum_{j=1}^r n_j\bar x_j`,note:r`Letzte Formel: Gesamtmittel aus Schichtmitteln = gewichteter Durchschnitt (Mietspiegel-Beispiel V02).`},
{t:"exam",h:"Probeklausur Aufgabe 1 — Wahrsagerin",src:"Probeklausur A-Teil",q:r`Harry befragt 20 Schüler*innen, ob die Vorhersagen eingetroffen sind (1 = korrekt, 0 = falsch):
<pre class="mono" style="margin:0;white-space:pre-wrap">&gt; sort(Vorhersagen)
[1] 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1</pre>`,
parts:[{q:r`(b) Berechnen Sie \(x_{mod}\), \(x_{med}\), \(\bar x\) und \(s_x^2\). Falls ein Parameter nicht sinnvoll ist, begründen Sie kurz.`,p:9,s:r`11 Nullen, 9 Einsen, \(n=20\).<br>\(x_{mod}=0\) (häufigster Wert).<br>\(x_{med}\): \(n\) gerade → Platz 10 und 11 → beide 0 → \(x_{med}=0\).<br>\(\bar x=9/20=0.45\) (= Anteil korrekter Vorhersagen).<br>\(s_x^2=\overline{x^2}-\bar x^2=0.45-0.45^2=0.2475\approx0.248\) — <b>oder</b> „NA: Weil die Daten ordinalskaliert sind, ist die Varianz nicht sinnvoll zu interpretieren.“ Beide Antworten gibt die Musterlösung als richtig an.`}]}
]});

L({id:"1.5",day:1,no:5,title:"Streuung & Boxplot",min:55,rel:3,
src:["V02","Tutorium 2, 3","Testat 1"],
goal:r`Du rechnest Varianz und Standardabweichung schnell mit dem Verschiebungssatz, kennst den Unterschied \(S^2\) vs. \(S^2_*\) (Achtung R!) und liest und baust Boxplots.`,
blocks:[
{t:"formula",h:"Varianz — zwei Versionen",tex:r`S^2=\frac1n\sum_{i=1}^n(x_i-\bar x)^2 \qquad S_*^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2 \qquad S^2=\frac{n-1}{n}S_*^2`,
parts:[["S^2","empirische Varianz (mittlere quadratische Abweichung), per Hand Standard"],["S_*^2","„unverzerrte“ Stichprobenvarianz — das rechnet R mit <code>var()</code>"]],
tr:r`S² paydası n, S*² paydası n−1. R'daki var() her zaman S*² verir! Elle hesaplarken soru özel olarak istemedikçe S² kullan.`},
{t:"formula",h:"Verschiebungssatz (spart Zeit)",tex:r`S^2=\frac1n\sum_{i=1}^n x_i^2-\bar x^2 \qquad S=\sqrt{S^2}`,note:r`Standardabweichung \(S\) hat dieselbe Einheit wie das Merkmal — das ist ihr Vorteil gegenüber der Varianz (Testat 1).`},
{t:"ex",h:"Semesterzahlen (Tutorium 2, Aufgabe 4)",q:r`Semester 2,3,4,5,6,7 mit \(h\) = 1,7,5,5,1,4 (\(n=23\)).`,
steps:[r`\(\bar x=\frac{1\cdot2+7\cdot3+5\cdot4+5\cdot5+1\cdot6+4\cdot7}{23}=\frac{102}{23}=4.4348\).`,r`\(\frac1n\sum x_i^2=\frac{1\cdot4+7\cdot9+5\cdot16+5\cdot25+1\cdot36+4\cdot49}{23}=\frac{504}{23}=21.9130\).`,r`\(S^2=21.9130-4.4348^2=21.9130-19.6675=2.2455\).`,r`\(S=\sqrt{2.2455}=1.4985\).`],a:r`\(\bar x=4.435\), \(S^2=2.246\), \(S=1.498\) (Median 4, Modus 3)`},
{t:"formula",h:"Lineare Transformation",tex:r`x_i\mapsto a+bx_i:\quad S^2\mapsto b^2S^2,\quad S\mapsto |b|\,S,\quad IQR\mapsto |b|\,IQR`,note:r`Die Verschiebung \(a\) ändert die Streuung nicht.`},
{t:"num",q:r`Datensatz II: 7, 9, 5, 8, 6. Datensatz III = 2 · Datensatz II. Berechne \(S^2\) für II und III (Tutorium 2, Aufgabe 6).`,f:[{l:"S² (II) =",a:2},{l:"S² (III) =",a:8}],why:r`II: \(\bar x=7\), \(\frac15(25+36+49+64+81)-49=51-49=2\). III: Faktor 2 → Varianz mal \(2^2=4\) → 8.`},
{t:"idea",h:"Interquartilsabstand & Boxplot",de:r`
<p>\(IQR=x_{0.75}-x_{0.25}\) — die Breite der mittleren 50 %. Der <b>Boxplot</b> zeigt die Fünf-Punkte-Zusammenfassung: Minimum, \(x_{0.25}\), Median, \(x_{0.75}\), Maximum. Ausreißer (mehr als \(1.5\cdot IQR\) von der Box entfernt) werden als Punkte gezeichnet; der Whisker endet dann beim extremsten Wert <i>innerhalb</i> der Grenze.</p>`,
tr:r`Kutu grafiği: min, Q1, medyan, Q3, max. Kutudan 1.5·IQR'den uzak değerler aykırı değer (nokta) olarak çizilir; bıyık sınırın içindeki en uç değerde biter.`},
{t:"ex",h:"Whisker wie R sie baut (Tutorium 2, Aufgabe 7)",q:r`20 sortierte Semesterzahlen: 1,1,1,1,2,2,3,3,3,4,4,5,6,6,6,6,7,9,13,14.`,
steps:[r`\(x_{0.25}\): \(20\cdot0.25=5\) ganzzahlig → Mittel aus Platz 5 und 6 = (2+2)/2 = 2. \(x_{0.75}\): \(20\cdot 0.75 = 15\) → Platz 15 und 16 = 6. Median: Platz 10 und 11 → (4+4)/2 = 4.`,r`\(IQR=6-2=4\).`,r`Obere Grenze: \(6+1.5\cdot4=12\). Größter Wert ≤ 12 ist 9 → oberer Whisker bei 9. Die Werte 13 und 14 sind Ausreißer.`,r`Untere Grenze: \(2-1.5\cdot4=-4\). Kleinster Wert ≥ −4 ist 1 → unterer Whisker = Minimum 1.`],a:r`Box von 2 bis 6, Median 4, Whisker 1 und 9, Ausreißer 13 und 14`},
{t:"fig",kind:"box",x:[0,15],xt:[0,2,4,6,9,12,14],xl:"Anzahl Semester",five:[1,2,4,6,9],out:[13,14],ann:[[1,"1","d"],[2,"x₀.₂₅","u"],[4,"Median","d"],[6,"x₀.₇₅","u"],[9,"9","d"],[13.5,"Ausreißer","u"]],cap:"Boxplot zu Tutorium 2, Aufgabe 7. Die Lage des Medians genau in der Mitte ist hier Zufall — kein Muss."},
{t:"mc",q:r`Boxplot eines ordinalen Merkmals „Zufriedenheit 1–7“: Es sind keine Punkte außerhalb der Whisker eingezeichnet. Liegen Ausreißer vor? (Testat 1, Aufgabe 6)`,o:["Ja, ein langer Whisker zeigt einen Ausreißer.","Nein, es sind keine Ausreißer eingezeichnet.","Ja, der Median „reißt aus“.","Nein, bei ordinalen Variablen kann es keine Ausreißer geben."],k:1,why:r`Ausreißer werden als einzelne Punkte gezeichnet. Ein langer Whisker ist kein Ausreißer.`},
{t:"r",h:"Streuung in R",code:r`
x <- c(1,1,1,1,2,2,3,3,3,4,4,5,6,6,6,6,7,9,13,14)
var(x)                      # ACHTUNG: S*^2 (Nenner n-1)
var(x) * (length(x)-1) / length(x)   # S^2 (Nenner n)
sd(x)                       # s* = sqrt(var(x))
quantile(x, c(0.25, 0.75))
IQR(x)
boxplot(x, range = 1.5, horizontal = TRUE, main = "Boxplot")
boxplot(x, plot = FALSE)$stats   # Whisker/Box-Werte ohne Grafik`,
out:r`
[1] 13.92368
[1] 13.2275
[1] 3.731445
25% 75%
  2   6
[1] 4`,
notes:[[2,"<code>var()</code> teilt durch \\(n-1\\). Das ist der häufigste R-Fehler im A-Teil-Vergleich.","R'daki var() n−1'e böler."],[3,"So kommst du von \\(S_*^2\\) auf \\(S^2\\).",""],[7,"<code>range = 1.5</code> ist die 1.5·IQR-Regel (Standard).",""]]},
{t:"trap",items:[r`\(S^2\) und \(S^2_*\) verwechselt (Tutorium 3: „Warum erhalten Sie mit R eine andere Varianz?“ → weil R \(S_*^2\) rechnet).`,r`Beim Verschiebungssatz \(\bar x^2\) mit \(\overline{x^2}\) verwechselt.`,r`Beim Quantil vergessen zu sortieren oder bei ganzzahligem \(n\alpha\) nicht gemittelt.`,r`Varianz statt Standardabweichung eingesetzt (oder umgekehrt).`]}
]});

L({id:"1.6",day:1,no:6,title:"R-Grundlagen für den B-Teil",min:70,rel:3,
src:["R-Skript 01, 02","Testat 0, 2","Probeklausur B (Witcher)","Tutorium 1–3"],
goal:"Du kannst im B-Teil ohne Nachdenken: Arbeitsverzeichnis setzen, CSV einlesen, Objekttypen bestimmen, Kennzahlen runden, ein beschriftetes Histogramm als PDF speichern und neue Variablen mit cut() bauen.",
blocks:[
{t:"idea",h:"Wie eine B-Teil-Antwort aussieht",de:r`
<p>Pro Teilaufgabe gibt es in ILIAS meist <b>zwei Kästchen</b>: eines für R-Code <b>mit</b> Output, eines für den <b>Antwortsatz</b> in einem vollen Satz. Zahlen immer mit einem R-Befehl runden (<code>round(…, 3)</code>). Grafiken: Titel mit Aufgabenteil, Sitzplatz und Matrikelnummer, Achsen beschriften, als PDF speichern und hochladen.</p>
<p><b>Folgefehler werden berücksichtigt:</b> Wenn (b) nicht klappt, schreibe trotzdem den Code für (c), (d), …</p>`,
tr:r`B bölümünde her alt soru için: 1) R kodu + çıktısı, 2) tam cümleyle cevap. Sayıları round(…,3) ile yuvarla. Grafiklerde başlık, eksen adları ve PDF olarak kaydetme şart.`},
{t:"r",h:"Einlesen: der Start jeder B-Klausur",code:r`
setwd(path.expand("~"))     # Arbeitsverzeichnis = Ordner Dokumente
d <- read.csv("WitcherData1.csv", sep = ",", dec = ".", header = TRUE)
head(d)                     # die ersten 6 Zeilen
str(d)                      # Struktur: Variablen und ihre Typen
typeof(d$Tal)               # Objekttyp einer Variable
typeof(d$Muenzen)`,
out:r`
[1] "character"
[1] "integer"`,
notes:[[1,"Genau so steht es in der Klausur-Anweisung.","Sınavda bu satır aynen verilir."],[2,"<code>sep</code> = Spaltentrenner, <code>dec</code> = Dezimalzeichen, <code>header = TRUE</code> = erste Zeile enthält Namen. Mit <code>d &lt;-</code> speicherst du als Data Frame.","sep: sütun ayırıcı, dec: ondalık işareti, header: ilk satır başlık mı."],[5,"Mögliche Antworten: <code>character</code> (Text), <code>integer</code> (ganze Zahlen), <code>double</code> (Kommazahlen, „numeric“), <code>logical</code>. Alternativ: <code>class()</code>.",""]]},
{t:"idea",h:"Antwortsätze wie in der Musterlösung",de:r`
<ul><li>(c) „Bei der Variable Tal handelt es sich um ein character-Objekt, bei der Variable Muenzen um ein numerisches Objekt des Typs integer, d. h. es enthält nur ganze Zahlen.“</li>
<li>(d) „Der Schätzer für das arithmetische Mittel der Variable Muenzen beträgt 22.454. Der unverzerrte Schätzer für die Standardabweichung beträgt 4.610.“</li></ul>`},
{t:"num",q:r`Testat 0, Aufgabe 2 — ergänze die R-Ausgaben:
<pre class="mono" style="margin:6px 0;white-space:pre-wrap">&gt; A &lt;- 3:6;  B &lt;- 4:2;  C &lt;- seq(2, 8, by = 2)
&gt; union(A, B)        [1] 3 4 5 6 ?
&gt; intersect(A, C)    [1] ? 6
&gt; setdiff(B, C)      [1] ?</pre>`,
f:[{l:"union: ? =",a:2,tol:0},{l:"intersect: ? =",a:4,tol:0},{l:"setdiff: ? =",a:3,tol:0}],
why:r`A = 3 4 5 6, B = 4 3 2, C = 2 4 6 8. Vereinigung: neu dazu kommt nur 2. Schnitt A∩C = 4, 6. B ohne C = 3. Und <code>is.element(6, C)</code> liefert <code>TRUE</code>.`},
{t:"r",h:"Kennzahlen und Rundung",code:r`
round(mean(d$Muenzen), 3)
round(sd(d$Muenzen), 3)       # s* (unverzerrt, Nenner n-1)
round(var(d$Muenzen), 2)
round(range(d$Muenzen), 2)    # Minimum und Maximum
median(d$Kampfzeit); IQR(d$Kampfzeit)
summary(d$Kampfzeit)          # Min, Quartile, Median, Mittel, Max`,
out:r`
[1] 22.454
[1] 4.61`,
notes:[[2,"R zeigt 4.61 — im Antwortsatz schreibst du 4.610 (drei Nachkommastellen).","Çıktı 4.61 olsa bile cümlede 4.610 yaz."],[4,"<code>range()</code> gibt den Wertebereich [Min, Max] (ML-Probeklausur B, Aufgabe d).",""]]},
{t:"r",h:"Histogramm als PDF — 8 Punkte in der Probeklausur",code:r`
pdf("Histogramm.pdf")
hist(d$Muenzen,
     freq   = FALSE,                 # normiert: Dichte
     breaks = c(5, 15, 20, 25, 35),  # vorgegebene Klassengrenzen
     right  = FALSE,                 # [5,15), [15,20), ... links geschlossen
     main   = "Sitz 00, Matr.Nr. 12345678, Aufgabenteil e)",
     xlab   = "Muenzen",
     ylab   = "Dichte")
dev.off()`,
notes:[[1,"<code>pdf()</code> öffnet die Datei, <code>dev.off()</code> schließt sie. Ohne <code>dev.off()</code> ist die Datei leer!","pdf() dosyayı açar, dev.off() kapatır. dev.off() unutulursa dosya boş kalır."],[3,"<code>freq = FALSE</code> (oder <code>prob = TRUE</code>) → normiertes Histogramm. Ohne: absolute Häufigkeiten.",""],[5,"Aufgabe sagt [5,15) → rechts offen → <code>right = FALSE</code>. Standard in R ist <code>right = TRUE</code>, also (a,b].","[a,b) istenirse right=FALSE."]]},
{t:"mc",q:r`Mit welchem Befehl erstellst du ein <b>normiertes</b> Histogramm für den Vektor x? (Testat 1)`,o:["hist(x, prob = TRUE) und hist(x, freq = FALSE) — beide","nur hist(x, freq = TRUE)","nur hist(x, prob = FALSE)"],k:0,why:r`<code>prob = TRUE</code> und <code>freq = FALSE</code> bedeuten dasselbe: Dichte auf der y-Achse.`},
{t:"r",h:"Neue Variablen mit cut() und Kontingenztafel (Testat 2, Witcher)",code:r`
# "Weniger als 5 Min", "5 Min bis unter 1 Std", "1 Std oder mehr"
d$Kampfzeit.3 <- cut(d$Kampfzeit, breaks = c(0, 5, 60, Inf), right = FALSE)
# "bis 10", "mehr als 10 bis 20", "mehr als 20 bis 30", "mehr als 30"
d$Muenzen.4  <- cut(d$Muenzen, breaks = c(0, 10, 20, 30, Inf), right = TRUE)
Kontingenz.Tafel <- table(d$Muenzen.4, d$Kampfzeit.3)
Kontingenz.Tafel
prop.table(table(d$Muenzen.4[d$Kampfzeit >= 5 & d$Kampfzeit < 60]))`,
notes:[[2,"„weniger als 5“ und „5 bis unter 60“ → Grenze gehört zur <b>rechten</b> Klasse → links geschlossen: <code>right = FALSE</code>.","„5'ten az“ → [0,5), sağ açık → right=FALSE."],[4,"„bis zu 10“, „mehr als 10 aber maximal 20“ → rechts geschlossen (10,20] → <code>right = TRUE</code>.",""],[5,"<code>table(x, y)</code> mit zwei Variablen = Kontingenztafel (Tag 2).",""],[7,"Nur Zeilen, die die Bedingung erfüllen; <code>prop.table</code> macht relative Häufigkeiten.",""]]},
{t:"r",h:"Streudiagramm speichern",code:r`
pdf("Streudiagramm.pdf")
plot(d$Kampfzeit, d$Muenzen,
     pch = 16, cex = 0.3,
     main = "Streudiagramm",
     xlab = "Kampfzeit (min.)",
     ylab = "Muenzen")
dev.off()`,notes:[[2,"<code>plot(x, y)</code>: erstes Argument x-Achse, zweites y-Achse. <code>pch</code> = Punktsymbol, <code>cex</code> = Punktgröße.",""]]},
{t:"trap",items:[r`<code>dev.off()</code> vergessen → PDF leer.`,r`<code>right</code> falsch gesetzt → Klassen verschoben, Punkte weg.`,r`Nicht gerundet oder mit <code>signif</code> statt <code>round(…, 3)</code> gerundet.`,r`Groß-/Kleinschreibung: <code>d$muenzen</code> ≠ <code>d$Muenzen</code>.`,r`Kein Antwortsatz — reiner Output reicht nicht.`]},
{t:"exam",h:"B-Teil-Training: Witcher (a)–(e)",src:"Probeklausur B, Altklausur 04.03.2022",kind:"B-Teil-Aufgabe (in R lösen)",q:r`Datensatz <code>WitcherData1.csv</code> mit den Variablen Taverne, Tal, Monster, Muenzen. Schreib den Code zuerst selbst auf Papier, dann vergleiche.`,
parts:[{q:r`(a) Arbeitsverzeichnis setzen.`,p:2,s:r`<code>setwd(path.expand("~"))</code>`},
{q:r`(b) Daten als Data Frame <code>d</code> speichern und die ersten 6 Zeilen ausgeben.`,p:4,s:r`<code>d &lt;- read.csv("WitcherData1.csv", sep = ",", dec = ".", header = TRUE)</code><br><code>head(d)</code>`},
{q:r`(c) Objekttypen von Tal und Muenzen bestimmen (Code + Antwortsatz).`,p:4,s:r`<code>typeof(d$Tal)</code> → "character"; <code>typeof(d$Muenzen)</code> → "integer".<br>„Bei der Variable Tal handelt es sich um ein character-Objekt, bei der Variable Muenzen um ein numerisches Objekt des Typs integer.“`},
{q:r`(d) Arithmetisches Mittel und unverzerrte Standardabweichung von Muenzen, auf 3 Nachkommastellen.`,p:4,s:r`<code>round(mean(d$Muenzen), 3)</code> → 22.454; <code>round(sd(d$Muenzen), 3)</code> → 4.61.<br>„Das arithmetische Mittel beträgt 22.454, die unverzerrte Standardabweichung 4.610.“`},
{q:r`(e) Histogramm mit Klassen [5,15), [15,20), [20,25), [25,35), Dichte, beschriftet, als Histogramm.pdf.`,p:8,s:r`Siehe Code-Block oben: <code>pdf("Histogramm.pdf"); hist(d$Muenzen, freq = FALSE, breaks = c(5,15,20,25,35), right = FALSE, main = "Sitz …, Matr.Nr …, Aufgabenteil e)", xlab = "Muenzen", ylab = "Dichte"); dev.off()</code>`}]}
]});
