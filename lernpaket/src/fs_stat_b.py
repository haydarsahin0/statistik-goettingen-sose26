"""Formelsammlung Statistik – Abschnitte 7–9 (Wahrscheinlichkeit, Zufallsvariablen, Verteilungen)."""
from fs_stat_doc import D

# =====================================================================
D.S("7", "Wahrscheinlichkeitsrechnung (V04)",
    "Probeklausur 2022: 17 Puan (Mengen 6 + Bayes 11). En önemli araç: metni doğru sembole çevirmek.")

D.E("7.1", "Text in Mengen-Sprache übersetzen",
    sig="„und“, „oder“, „nicht“, „weder … noch“, „genau eines“, „mindestens eines“, „aber nicht“",
    ne="Önce kelimeleri sembole çevir, sonra hesapla. „Oder“ istatistikte her zaman „en az biri“ (ikisi de olabilir).",
    extra=("<table class='t'><tr><th>Wortlaut</th><th>Menge</th><th>Wahrscheinlichkeit</th></tr>"
           "<tr><td>A und B</td><td>\\(A\\cap B\\)</td><td>\\(P(A\\cap B)\\)</td></tr>"
           "<tr><td>A oder B (mindestens eines)</td><td>\\(A\\cup B\\)</td><td>\\(P(A)+P(B)-P(A\\cap B)\\)</td></tr>"
           "<tr><td>nicht A</td><td>\\(\\bar A\\)</td><td>\\(1-P(A)\\)</td></tr>"
           "<tr><td>A, aber nicht B</td><td>\\(A\\cap\\bar B=A\\setminus B\\)</td><td>\\(P(A)-P(A\\cap B)\\)</td></tr>"
           "<tr><td>weder A noch B</td><td>\\(\\bar A\\cap\\bar B=\\overline{A\\cup B}\\)</td><td>\\(1-P(A\\cup B)\\)</td></tr>"
           "<tr><td>genau eines von beiden</td><td>\\((A\\cap\\bar B)\\cup(\\bar A\\cap B)\\)</td><td>\\(P(A)+P(B)-2P(A\\cap B)\\)</td></tr>"
           "<tr><td>höchstens eines</td><td>\\(\\overline{A\\cap B}\\)</td><td>\\(1-P(A\\cap B)\\)</td></tr></table>"),
    bsp=r"\(P(A)=0.5,\ P(B)=0.4,\ P(A\cap B)=0.15\): weder noch \(1-0.75=0.25\) · genau eines \(0.9-0.3=0.6\) · A aber nicht B \(0.35\)",
    fa="Venn-Diagramm skizzieren: Die vier Bereiche (nur A, nur B, beide, keines) ergeben zusammen 1.")

D.E("7.2", "Mengen und Mächtigkeiten (Laplace-Experiment)",
    sig="„Ergebnisraum Ω = {…}“, „Berechnen Sie die Mächtigkeiten \\(|A\\cap\\bar B|\\)“",
    ne="|·| = eleman <b>sayısı</b> (olasılık değil). Tümleyeni açıkça yaz: \\(\\bar B\\) = Ω'da olup B'de olmayanlar.",
    fm=r"\[\bar A=\Omega\setminus A\qquad\overline{A\cup B}=\bar A\cap\bar B\qquad\overline{A\cap B}=\bar A\cup\bar B\quad\text{(De Morgan)}\qquad|A\cup B|=|A|+|B|-|A\cap B|\]",
    st=["Alle Komplemente <b>ausschreiben</b> (Liste).", "Schnitt = in beiden Listen; Vereinigung = in mindestens einer.", "Elemente zählen. Kontrolle über De Morgan / Komplement: \\(|\\bar A\\cup B|=|\\Omega|-|A\\cap\\bar B|\\)."],
    bsp=r"Ω = {1,…,8}, A = {1,2,3,4}, B = {3,4,5,6}: \(\bar B=\{1,2,7,8\}\), \(A\cap\bar B=\{1,2\}\Rightarrow|A\cap\bar B|=2\) · \(|\bar A\cup B|=8-2=6\)",
    fa="Probeklausur 2022 Aufgabe 4 (6 P) war genau das – sorgfältig auflisten, nicht im Kopf.")

D.E("7.3", "Laplace-Wahrscheinlichkeit",
    sig="„Laplace-Experiment“, „fairer Würfel“, „zufällig gezogen“",
    ne="Tüm sonuçlar eşit olasılıklıysa: istenen sayısı / tüm sonuçların sayısı.",
    fm=r"\[P(A)=\frac{|A|}{|\Omega|}=\frac{\text{günstige}}{\text{mögliche}}\]",
    bsp=r"Zwei Würfel, Augensumme 7: \(\frac{6}{36}=\frac16\) · Ω = {1,…,8}, A = {1,2,3,4}: \(P(A)=\frac48=0.5\)")

D.E("7.4", "Rechenregeln (Kolmogorov)",
    sig="„Berechnen Sie \\(P(A\\cup B)\\)“, „Gegenereignis“",
    ne="Tümleyen: 1 − P. Birleşim: topla, kesişimi bir kez çıkar. Ayrık (disjunkt) olaylarda kesişim 0.",
    fm=r"\[0\le P(A)\le1\qquad P(\Omega)=1\qquad P(\bar A)=1-P(A)\qquad P(A\cup B)=P(A)+P(B)-P(A\cap B)\qquad P(A\setminus B)=P(A)-P(A\cap B)\]",
    bsp=r"\(P(A)=0.3,\ P(B)=0.5,\ P(A\cap B)=0.2\): \(P(A\cup B)=0.3+0.5-0.2=0.6\)",
    fa="Disjunkt (\\(A\\cap B=\\emptyset\\)) ist nicht dasselbe wie unabhängig! Disjunkte Ereignisse mit \\(P&gt;0\\) sind sogar abhängig.")

D.E("7.5", "Vierfeldertafel (Wahrscheinlichkeiten)",
    sig="zwei Ereignisse mit \\(P(A)\\), \\(P(B)\\), \\(P(A\\cap B)\\); „Füllen Sie die Tafel“",
    ne="Kontenjans tablosu gibi, ama sayı yerine olasılık; toplam 1. Eksikleri farkla bul.",
    extra=("<table class='t c' style='width:auto'><tr><th></th><th>\\(B\\)</th><th>\\(\\bar B\\)</th><th>Σ</th></tr>"
           "<tr><th>\\(A\\)</th><td>\\(P(A\\cap B)\\)</td><td>\\(P(A\\cap\\bar B)\\)</td><td>\\(P(A)\\)</td></tr>"
           "<tr><th>\\(\\bar A\\)</th><td>\\(P(\\bar A\\cap B)\\)</td><td>\\(P(\\bar A\\cap\\bar B)\\)</td><td>\\(P(\\bar A)\\)</td></tr>"
           "<tr><th>Σ</th><td>\\(P(B)\\)</td><td>\\(P(\\bar B)\\)</td><td>1</td></tr></table>"),
    bsp=r"\(P(A)=0.3,\ P(B)=0.6,\ P(A\cap B)=0.12\) → \(P(A\cap\bar B)=0.18\), \(P(\bar A\cap B)=0.48\), \(P(\bar A\cap\bar B)=0.22\)")

D.E("7.6", "Bedingte Wahrscheinlichkeit",
    sig="„unter der Bedingung“, „wenn bekannt ist, dass“, „gegeben“, „von den …“, „unter den …“",
    ne="P(A|B): B'nin olduğu <b>biliniyor</b>, A'yı arıyoruz. Bilinen her zaman çizginin <b>sağında</b>; paydaya o gelir.",
    fm=r"\[P(A\mid B)=\frac{P(A\cap B)}{P(B)}\qquad P(A\cap B)=P(A\mid B)\,P(B)=P(B\mid A)\,P(A)\qquad P(\bar A\mid B)=1-P(A\mid B)\]",
    st=["Was ist bekannt (Bedingung)? → rechts vom Strich.", "Schnitt durch die Wahrscheinlichkeit der Bedingung teilen.", "Laplace: \\(P(A\\mid B)=\\frac{|A\\cap B|}{|B|}\\) (Ω schrumpft auf B)."],
    bsp=r"Tafel aus 7.5: \(P(A\mid B)=\frac{0.12}{0.6}=0.2\) · \(P(B\mid A)=\frac{0.12}{0.3}=0.4\) · \(P(A\mid\bar B)=\frac{0.18}{0.4}=0.45\)",
    fa="\\(P(A\\mid B)\\ne P(B\\mid A)\\). „A, wenn B nicht eingetreten ist“ = \\(P(A\\mid\\bar B)\\).")

D.E("7.7", "Stochastische Unabhängigkeit prüfen",
    sig="„Sind A und B stochastisch unabhängig? Begründen Sie rechnerisch“",
    ne="Kesişim = çarpım ise bağımsız. Ya da P(A|B) = P(A). Sayılarla göster.",
    fm=r"\[A,B\ \text{unabhängig}\iff P(A\cap B)=P(A)\cdot P(B)\iff P(A\mid B)=P(A)\]",
    st=["\\(P(A)\\), \\(P(B)\\), \\(P(A\\cap B)\\) bestimmen.", "\\(P(A)\\cdot P(B)\\) ausrechnen und mit \\(P(A\\cap B)\\) vergleichen.", "Gleich → unabhängig, sonst abhängig. Satz mit Zahlen."],
    bsp=r"7.5: \(0.3\cdot0.6=0.18\ne0.12=P(A\cap B)\) → abhängig · Laplace Ω = {1,…,10}, A = {1,2,3,4,5}, B = {2,4,6,8,10}: \(P(A\cap B)=0.2\ne0.25\) → abhängig",
    ks="„Da \\(P(A\\cap B)=0.12\\ne0.18=P(A)\\cdot P(B)\\), sind A und B stochastisch abhängig.“")

D.E("7.8", "Baumdiagramm und Pfadregeln",
    sig="mehrstufiger Vorgang, „zuerst … dann …“, Anteile und bedingte Anteile",
    ne="Dal üzerindeki sayılar koşullu olasılıklar. Bir yol boyunca <b>çarp</b>, aynı sonuca giden yolları <b>topla</b>.",
    st=["1. Stufe: die Ereignisse, deren Wahrscheinlichkeit <b>unbedingt</b> gegeben ist (z. B. Anteile der Maschinen).",
        "2. Stufe: die bedingten Wahrscheinlichkeiten \\(P(\\cdot\\mid\\text{1. Stufe})\\). Jeder Knoten: Summe der Äste = 1 (fehlende Äste als 1 − …).",
        "<b>Pfadregel</b>: entlang eines Pfades multiplizieren. <b>Summenregel</b>: Pfade zum gleichen Ergebnis addieren."],
    fa="Welche Variable kommt zuerst? Die, auf die sich die Bedingung bezieht. Steht „von den Bestandenen gehören 80 % zu Strategie 1“, ist „Bestehen“ die 1. Stufe.")

D.E("7.9", "Satz der totalen Wahrscheinlichkeit",
    sig="„Mit welcher Wahrscheinlichkeit ist ein zufällig ausgewähltes Teil defekt?“",
    ne="Bir olayın toplam olasılığı = ona giden tüm yolların toplamı.",
    fm=r"\[P(B)=\sum_i P(B\mid A_i)\,P(A_i)=P(B\mid A_1)P(A_1)+P(B\mid A_2)P(A_2)+\dots\]",
    bsp=r"Maschine 1 (60 %, 2 % Ausschuss), Maschine 2 (40 %, 5 % Ausschuss): \(P(D)=0.02\cdot0.6+0.05\cdot0.4=0.012+0.02=0.032\)",
    fa="Die \\(A_i\\) müssen eine Zerlegung sein (disjunkt, zusammen Ω): Anteile summieren sich zu 1.")

D.E("7.10", "Satz von Bayes (Rückschluss auf die Ursache)",
    sig="„Ein Teil ist defekt. Mit welcher Wahrscheinlichkeit stammt es von Maschine 2?“",
    ne="Sonuç biliniyor, nedeni arıyoruz. <b>Benim yolum / o sonuca giden tüm yollar.</b>",
    fm=r"\[P(A_j\mid B)=\frac{P(B\mid A_j)\,P(A_j)}{P(B)}=\frac{P(B\mid A_j)\,P(A_j)}{\sum_i P(B\mid A_i)\,P(A_i)}\]",
    st=["Gesucht übersetzen: bekannt = B (rechts), gesucht = Ursache \\(A_j\\).", "Nenner \\(P(B)\\) mit 7.9.", "Zähler = Pfad über \\(A_j\\).", "Teilen. Gegenereignis-Version: alles mit \\(\\bar B\\) (\\(P(\\bar B\\mid A_i)=1-P(B\\mid A_i)\\), \\(P(\\bar B)=1-P(B)\\))."],
    bsp=r"7.9: \(P(M_2\mid D)=\frac{0.05\cdot0.4}{0.032}=\frac{0.02}{0.032}=0.625\) · \(P(M_1\mid\bar D)=\frac{0.98\cdot0.6}{0.968}=0.607\)",
    fa="Kontrolle: Alle \\(P(A_i\\mid B)\\) zusammen ergeben 1.",
    ks="„Ein defektes Teil stammt mit einer Wahrscheinlichkeit von 0.625 von Maschine 2.“")

D.E("7.11", "Medizinischer Test: Sensitivität, Spezifität, Prävalenz",
    sig="„Prävalenz“, „Sensitivität“, „Spezifität“, „bei positivem Test krank“",
    ne="Prävalenz = P(K) · Sensitivität = P(T|K) · Spezifität = \\(P(\\bar T\\mid\\bar K)\\). Bayes ile P(K|T).",
    fm=r"\[P(T)=P(T\mid K)P(K)+P(T\mid\bar K)P(\bar K)\qquad P(T\mid\bar K)=1-\text{Spez.}\qquad P(K\mid T)=\frac{\text{Sens.}\cdot P(K)}{P(T)}\]",
    bsp=r"Prävalenz 1 %, Sens. 0.9, Spez. 0.95: \(P(T)=0.9\cdot0.01+0.05\cdot0.99=0.0585\) · \(P(K\mid T)=\frac{0.009}{0.0585}=0.154\) · \(P(\bar K\mid\bar T)=\frac{0.95\cdot0.99}{0.9415}=0.999\)",
    fa="\\(P(\\bar K)=1-\\text{Prävalenz}\\) (z. B. 0.99) wird oft vergessen. Kontrolle mit 10 000 Personen: 100 krank → 90 positiv; 9 900 gesund → 495 positiv.",
    ks="„Obwohl der Test gut ist, ist eine positiv getestete Person nur mit Wahrscheinlichkeit 0.154 krank, da die Krankheit selten ist.“")

D.E("7.12", "Ziehen ohne Zurücklegen (hypergeometrisch, „Lotto“)",
    sig="„ohne Zurücklegen“, „Urne mit … roten und … weißen Kugeln“, „genau k“",
    ne="Geri koymadan çekmede olasılıklar değişir → binom değil. „Lotto formülü“ kullan.",
    fm=r"\[P(X=k)=\frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}\qquad N=\text{alle},\ M=\text{gesuchte Sorte},\ n=\text{gezogen}\]",
    bsp=r"10 Kugeln, 4 rot, 3 gezogen: \(P(\text{genau 2 rot})=\frac{\binom42\binom61}{\binom{10}3}=\frac{6\cdot6}{120}=0.3\)",
    fa="Mit Zurücklegen → Binomialverteilung (9.4) und Unabhängigkeit; ohne Zurücklegen → abhängig.")

# =====================================================================
D.S("8", "Zufallsvariablen: Verteilung, Erwartungswert, Varianz (V05–V06)",
    "Testat 4'ün konusu. Reçete hep aynı: Träger → olasılık fonksiyonu/yoğunluk → E(X) → Var(X).")

D.E("8.1", "Träger und Wahrscheinlichkeitsfunktion (diskret)",
    sig="„Geben Sie den Träger und die Wahrscheinlichkeitsfunktion von X an“",
    ne="Träger = X'in alabileceği değerler. Olasılık fonksiyonu = her değerin olasılığı + „0 sonst“.",
    fm=r"\[f(x)=P(X=x)=\begin{cases}p_1 & x=x_1\\ p_2 & x=x_2\\ \ \vdots\\ 0 & \text{sonst}\end{cases}\qquad p_j\ge0,\quad\sum_j p_j=1\]",
    st=["X genau definieren (z. B. Gewinn = Auszahlung − Einsatz).", "Träger T = alle möglichen Werte von X (nicht die des Würfels!).",
        "Jedem Wert seine Wahrscheinlichkeit zuordnen; gleiche Werte zusammenfassen.", "„0 sonst“ hinschreiben. Kontrolle: Summe = 1."],
    bsp=r"Zwei Münzwürfe, X = Anzahl Kopf: \(T=\{0,1,2\}\), \(P(X=0)=\tfrac14,\ P(X=1)=\tfrac12,\ P(X=2)=\tfrac14\), 0 sonst",
    fa="„0 sonst“ fehlt → Punktabzug (Tutorium-Lösungen).")

D.E("8.2", "Konstante c bestimmen (diskret)",
    sig="„\\(P(X=x)=c\\cdot\\dots\\) für \\(x\\in\\{\\dots\\}\\). Bestimmen Sie c“",
    ne="Tüm olasılıkların toplamı 1 olmalı → denklem kur, c'yi çöz.",
    fm=r"\[\sum_{x\in T}P(X=x)=1\ \Rightarrow\ c\]",
    bsp=r"\(P(X=x)=c(x+1)\) für \(x\in\{0,1,2\}\): \(c(1+2+3)=6c=1\Rightarrow c=\tfrac16\)",
    fa="Danach prüfen, ob alle Wahrscheinlichkeiten zwischen 0 und 1 liegen; sonst „nicht lösbar“.")

D.E("8.3", "Verteilungsfunktion F(x) (diskret)",
    sig="„Vervollständigen Sie F(x)“, „Bestimmen Sie \\(P(X\\le3)\\) mit F“, Treppenfunktion",
    ne="F(x) = P(X ≤ x): olasılıkları soldan sağa biriktir. Merdivenin basamak yüksekliği = o değerin olasılığı.",
    fm=r"\[F(x)=P(X\le x)=\sum_{x_j\le x}P(X=x_j)\qquad P(a<X\le b)=F(b)-F(a)\qquad P(X>a)=1-F(a)\qquad P(X=x_j)=\text{Sprunghöhe}\]",
    bsp=r"\(P(X=1)=0.2,\ P(X=2)=0.5,\ P(X=4)=0.3\): \(F=0\ (x<1);\ 0.2\ (1\le x<2);\ 0.7\ (2\le x<4);\ 1\ (x\ge4)\) · \(P(X\le3)=0.7\) · \(P(X<2)=0.2\) · \(P(X=3)=0\)",
    fa="Bei diskreten ZV ist \\(P(X&lt;2)=F(1)\\ne F(2)\\). Werte außerhalb des Trägers haben Wahrscheinlichkeit 0. Wörter → 2.2.")

D.E("8.4", "Dichte (stetig): Eigenschaften und c bestimmen",
    sig="„Bestimmen Sie c derart, dass f eine gültige Dichtefunktion ist“, „Welche Eigenschaften muss eine Dichte erfüllen?“",
    ne="Yoğunluk: f(x) ≥ 0 ve toplam alan (integral) = 1. f(x) > 1 olabilir! P(X = x) = 0.",
    fm=r"\[f(x)\ge0\ \text{für alle }x\qquad\int_{-\infty}^{\infty}f(x)\,dx=1\qquad P(a\le X\le b)=\int_a^b f(x)\,dx\qquad P(X=x)=0\]",
    st=["Integral über den Träger aufstellen und = 1 setzen.", "Integrieren (0.5), nach c auflösen.", "Prüfen: \\(f(x)\\ge0\\) auf dem Träger."],
    bsp=r"\(f(x)=c\,x^2\) für \(0\le x\le3\): \(c\left[\tfrac{x^3}3\right]_0^3=9c=1\Rightarrow c=\tfrac19\)",
    fa="„f(x) ≤ 1“ und „f(x) = P(X = x)“ sind <b>keine</b> Eigenschaften einer Dichte (Testat-Multiple-Choice).")

D.E("8.5", "Verteilungsfunktion, Wahrscheinlichkeiten und Quantile (stetig)",
    sig="„Bestimmen Sie F(x)“, „\\(P(X\\le1)\\)“, „Median der Zufallsvariable“",
    ne="F(x) = soldan x'e kadar alan = integral. Medyan: F(x) = 0.5 denklemini çöz.",
    fm=r"\[F(x)=\int_{-\infty}^{x}f(t)\,dt\qquad P(a<X\le b)=F(b)-F(a)\qquad x_{med}:\ F(x_{med})=0.5\qquad x_\alpha:\ F(x_\alpha)=\alpha\]",
    bsp=r"\(f(x)=\tfrac{x^2}9\) auf [0, 3]: \(F(x)=\tfrac{x^3}{27}\) (0 für x < 0, 1 für x > 3) · \(P(X\le1.5)=\tfrac{3.375}{27}=0.125\) · Median: \(x^3=13.5\Rightarrow x_{med}=2.381\)",
    fa="F vollständig angeben: 0 links vom Träger, 1 rechts davon.")

D.E("8.6", "Erwartungswert E(X)",
    sig="„Bestimmen Sie den Erwartungswert“, „im Mittel“, „durchschnittlicher Gewinn“",
    ne="Uzun vadede ortalama değer = <b>değer × olasılık, topla</b> (stetig: integral). Ağırlıklı ortalamadır.",
    fm=r"\[E(X)=\sum_{x\in T}x\cdot P(X=x)\qquad E(X)=\int_{-\infty}^{\infty}x\,f(x)\,dx\]",
    bsp=r"8.2: \(E(X)=0\cdot\tfrac16+1\cdot\tfrac26+2\cdot\tfrac36=\tfrac86=\tfrac43=1.333\) · 8.4: \(E(X)=\int_0^3 x\cdot\tfrac{x^2}9dx=\left[\tfrac{x^4}{36}\right]_0^3=2.25\)",
    fa="E(X) muss nicht im Träger liegen (Würfel: 3.5). Tabellenform: Spalten x | P | x·P | x²·P anlegen.")

D.E("8.7", "Erwartungswert einer Funktion E(g(X)), E(X²)",
    sig="„Bestimmen Sie E(Y) für Y = log(X)“, „\\(E(X^2)\\)“, „\\(Y=X^2\\)“",
    ne="g(X)'in beklentisi: her değer için g(x)·P(X=x), topla. Önce E(X) bulup g'ye koymak <b>yanlış</b>.",
    fm=r"\[E(g(X))=\sum g(x)\,P(X=x)\qquad E(g(X))=\int g(x)\,f(x)\,dx\qquad E(g(X))\ne g(E(X))\ \text{(außer g linear)}\]",
    bsp=r"X ∈ {0, 1, 2} mit 0.5, 0.3, 0.2: \(E(X^2)=0+0.3+0.8=1.1\), aber \((E(X))^2=0.49\) · 8.4: \(E(X^2)=\int_0^3\tfrac{x^4}9dx=\tfrac{243}{45}=5.4\)",
    fa="log ist in diesem Kurs ln; \\(\\log 1=0\\).")

D.E("8.8", "Varianz und Standardabweichung einer Zufallsvariable",
    sig="„Berechnen Sie Var(X)“",
    ne="Var = E(X²) − (E(X))². Önce iki beklentiyi bul, sonra çıkar. Kesirlerle git, sonda ondalığa çevir.",
    fm=r"\[Var(X)=E(X^2)-\big(E(X)\big)^2=E\big[(X-E(X))^2\big]\qquad sd(X)=\sqrt{Var(X)}\]",
    bsp=r"8.2: \(E(X^2)=\tfrac{0+2+12}6=\tfrac73\) → \(Var(X)=\tfrac73-\tfrac{16}9=\tfrac59=0.556\) · 8.4: \(Var(X)=5.4-2.25^2=0.3375\to0.338\)",
    fa="Mit gerundetem E(X) quadrieren verfälscht das Ergebnis. Var ≥ 0 – sonst Rechenfehler.")

D.E("8.9", "Rechenregeln für E und Var",
    sig="„\\(Z=0.5X+Y\\)“, „\\(E(2X+4)\\)“, „X und Y unabhängig“, „Bestimmen Sie E(Y) rückwärts“",
    ne="Toplamın beklentisi her zaman toplanır. Varyans: sabit kaydırma etkisiz, çarpan karesiyle; toplamda bağımsızsa varyanslar toplanır (fark için de!).",
    fm=r"\[E(aX+b)=aE(X)+b\qquad Var(aX+b)=a^2Var(X)\qquad E(X\pm Y)=E(X)\pm E(Y)\]"
       r"\[Var(aX+bY)=a^2Var(X)+b^2Var(Y)+2ab\,Cov(X,Y)\qquad\text{unabhängig: }Cov=0,\ E(XY)=E(X)E(Y)\]",
    bsp=r"\(E(X)=3,\ Var(X)=1,\ Var(Y)=1\), unabhängig: \(Var(X-Y)=1+1=2\) · \(E(2X+4)=10\), \(Var(2X+4)=4\) · \(Var(0.5X+Y)=0.25+1=1.25\)",
    fa="\\(Var(X-Y)=Var(X)+Var(Y)\\) (nicht minus!) bei Unabhängigkeit. \\(Var(2X)=4Var(X)\\), aber \\(Var(X_1+X_2)=2Var(X)\\) bei iid.")

D.E("8.10", "Zwei diskrete Zufallsvariablen (gemeinsame Verteilung)",
    sig="Tabelle \\(P(X=x,Y=y)\\), „Randverteilung“, „bedingte Verteilung“, „Kovarianz“",
    ne="Marjinal = satır/sütun toplamı. Koşullu = hücre / marjinal. Cov = E(XY) − E(X)E(Y).",
    fm=r"\[P(X=x)=\sum_y P(X=x,Y=y)\qquad P(Y=y\mid X=x)=\frac{P(X=x,Y=y)}{P(X=x)}\qquad Cov(X,Y)=E(XY)-E(X)E(Y)\qquad\rho=\frac{Cov}{sd(X)\,sd(Y)}\]",
    bsp=r"\(P(0,0)=0.3,\ P(0,1)=0.2,\ P(1,0)=0.1,\ P(1,1)=0.4\): \(E(X)=0.5,\ E(Y)=0.6,\ E(XY)=0.4\) → \(Cov=0.4-0.3=0.1\ne0\) → abhängig · \(P(Y=1\mid X=1)=\frac{0.4}{0.5}=0.8\)",
    fa="Unabhängig ⇒ Cov = 0, aber Cov = 0 ⇏ unabhängig. Unabhängigkeit: jede Zelle = Produkt der Ränder.")

# =====================================================================
D.S("9", "Spezielle Verteilungen (V07)",
    "Önce hangi dağılım olduğunu tanı (9.2), sonra formülü uygula. Tablo 9.1 tüm E ve Var değerlerini içerir.")

D.E("9.1", "Übersicht: alle Verteilungen auf einen Blick",
    sig="„Wie lautet die Verteilung von X (mit Parametern)?“, „Erwartungswert und Varianz“",
    ne="Formül, beklenen değer, varyans ve R komutu tek tabloda.",
    extra=("<table class='t'><tr><th>Verteilung</th><th>\\(P(X=x)\\) bzw. \\(f(x)\\)</th><th>Träger</th><th>\\(E(X)\\)</th><th>\\(Var(X)\\)</th><th>R</th></tr>"
           "<tr><td>Bernoulli \\(Be(\\pi)\\)</td><td>\\(\\pi^x(1-\\pi)^{1-x}\\)</td><td>{0, 1}</td><td>\\(\\pi\\)</td><td>\\(\\pi(1-\\pi)\\)</td><td>binom, size=1</td></tr>"
           "<tr><td>Binomial \\(B(n,\\pi)\\)</td><td>\\(\\binom nx\\pi^x(1-\\pi)^{n-x}\\)</td><td>{0, …, n}</td><td>\\(n\\pi\\)</td><td>\\(n\\pi(1-\\pi)\\)</td><td>binom</td></tr>"
           "<tr><td>Poisson \\(Po(\\lambda)\\)</td><td>\\(\\frac{\\lambda^x}{x!}e^{-\\lambda}\\)</td><td>{0, 1, 2, …}</td><td>\\(\\lambda\\)</td><td>\\(\\lambda\\)</td><td>pois</td></tr>"
           "<tr><td>Geometrisch (Testat-Form)</td><td>\\(p(1-p)^x\\)</td><td>{0, 1, 2, …}</td><td>\\(\\frac{1-p}{p}\\)</td><td>\\(\\frac{1-p}{p^2}\\)</td><td>geom</td></tr>"
           "<tr><td>Gleich \\(U(a,b)\\)</td><td>\\(\\frac1{b-a}\\)</td><td>[a, b]</td><td>\\(\\frac{a+b}2\\)</td><td>\\(\\frac{(b-a)^2}{12}\\)</td><td>unif</td></tr>"
           "<tr><td>Exponential \\(Exp(\\lambda)\\)</td><td>\\(\\lambda e^{-\\lambda x}\\)</td><td>[0, ∞)</td><td>\\(\\frac1\\lambda\\)</td><td>\\(\\frac1{\\lambda^2}\\)</td><td>exp</td></tr>"
           "<tr><td>Normal \\(N(\\mu,\\sigma^2)\\)</td><td>\\(\\frac1{\\sqrt{2\\pi\\sigma^2}}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}\\)</td><td>ℝ</td><td>\\(\\mu\\)</td><td>\\(\\sigma^2\\)</td><td>norm</td></tr></table>"),
    fa="In \\(N(\\mu,\\sigma^2)\\) steht die <b>Varianz</b>; R (pnorm, qnorm) will die <b>Standardabweichung</b> σ.")

D.E("9.2", "Welche Verteilung passt? (Erkennungsschlüssel)",
    sig="„Durch welche Verteilung kann Y am geeignetsten modelliert werden?“",
    ne="Metindeki ipucu kelimeden dağılımı seç, parametreyi metinden al.",
    extra=("<table class='t'><tr><th>Signal im Text</th><th>Verteilung</th><th>Parameter aus dem Text</th></tr>"
           "<tr><td>ein Versuch, Erfolg ja/nein</td><td>Bernoulli</td><td>π = Erfolgswahrscheinlichkeit</td></tr>"
           "<tr><td>Anzahl Erfolge in n unabhängigen gleichen Versuchen, „mit Zurücklegen“</td><td>Binomial</td><td>n, π</td></tr>"
           "<tr><td>Anzahl Ereignisse pro Zeitraum/Fläche, „im Durchschnitt … pro Monat“, ohne feste Obergrenze</td><td>Poisson</td><td>λ = Durchschnitt im <b>gefragten</b> Zeitraum</td></tr>"
           "<tr><td>„ohne Zurücklegen“ aus kleiner Urne</td><td>hypergeometrisch (7.12)</td><td>N, M, n</td></tr>"
           "<tr><td>Anzahl Misserfolge bis zum ersten Erfolg</td><td>geometrisch</td><td>p</td></tr>"
           "<tr><td>„jeder Wert zwischen a und b gleich wahrscheinlich“</td><td>Gleichverteilung</td><td>a, b</td></tr>"
           "<tr><td>Wartezeit / Dauer bis zum Ereignis, „im Mittel 3 Stunden“</td><td>Exponential</td><td>λ = 1 / Mittelwert</td></tr>"
           "<tr><td>Messwerte (Gewicht, Größe, Füllmenge), Summen und Mittelwerte vieler ZV</td><td>Normal</td><td>μ, σ²</td></tr></table>"))

D.E("9.3", "Bernoulliverteilung",
    sig="„Erfolg/Misserfolg“, „0/1“, ein einzelner Versuch",
    ne="Tek deneme: başarı 1 (olasılık π), başarısızlık 0.",
    fm=r"\[P(X=1)=\pi,\quad P(X=0)=1-\pi\qquad E(X)=\pi\qquad Var(X)=\pi(1-\pi)\]",
    bsp=r"Münzwurf mit \(\pi=0.5\): \(E=0.5\), \(Var=0.25\)")

D.E("9.4", "Binomialverteilung",
    sig="„n-mal unabhängig“, „Anzahl der …“, „mit Zurücklegen“, „rät bei allen Fragen“",
    ne="n bağımsız denemede başarı sayısı. „En az / en fazla“ → toplamla veya tümleyenle.",
    fm=r"\[P(X=x)=\binom nx\pi^x(1-\pi)^{n-x}\qquad E(X)=n\pi\qquad Var(X)=n\pi(1-\pi)\qquad P(X\ge1)=1-(1-\pi)^n\]",
    st=["n, π aus dem Text; Verteilung hinschreiben: \\(X\\sim B(n,\\pi)\\).", "Wortlaut in Werte übersetzen (2.2): „mindestens 2“ = \\(1-P(0)-P(1)\\).", "Einzelwahrscheinlichkeiten ausrechnen, addieren."],
    bsp=r"\(X\sim B(10;\,0.3)\): \(P(X=2)=\binom{10}2\,0.3^2\,0.7^8=45\cdot0.09\cdot0.0576=0.233\) · \(P(X\ge1)=1-0.7^{10}=0.972\) · \(E=3,\ Var=2.1\)",
    fa="Gegenwahrscheinlichkeit spart Zeit: „mindestens 1“ = 1 − „keiner“.")

D.E("9.5", "Poissonverteilung",
    sig="„im Durchschnitt λ pro Stunde/Monat“, „Anzahl der Anrufe/Tore/Gewittertage“",
    ne="Belirli zamanda olay sayısı. λ = o zaman aralığındaki ortalama. Zaman aralığı değişirse λ da orantılı değişir.",
    fm=r"\[P(X=x)=\frac{\lambda^x}{x!}e^{-\lambda}\qquad E(X)=Var(X)=\lambda\qquad P(X=0)=e^{-\lambda}\qquad\text{Zeitraum}\times k\Rightarrow\lambda\times k\]",
    bsp=r"2 Anrufe pro Stunde: \(P(X=0)=e^{-2}=0.135\) · \(P(X\le1)=e^{-2}(1+2)=0.406\) · \(P(X>2)=1-e^{-2}(1+2+2)=0.323\) · in 3 Stunden: \(\lambda=6\)",
    fa="\\(Z=2X+4\\) ist nicht mehr poissonverteilt (E = 10 ≠ Var = 12).")

D.E("9.6", "Geometrische Verteilung (Testat-/ML-Form)",
    sig="\\(P(X=x)=p(1-p)^x\\) für x = 0, 1, 2, …",
    ne="İlk başarıya kadar başarısızlık sayısı. Sınavda genelde ML sorusu olarak çıkar (11.6).",
    fm=r"\[P(X=x)=p\,(1-p)^x\qquad E(X)=\frac{1-p}{p}\qquad Var(X)=\frac{1-p}{p^2}\qquad P(X\ge k)=(1-p)^k\]",
    bsp=r"\(p=0.25\): \(P(X=2)=0.25\cdot0.75^2=0.141\) · \(E(X)=3\)",
    fa="Andere Bücher zählen die Versuche (x = 1, 2, …) – immer die Formel aus der Aufgabe nehmen.")

D.E("9.7", "Stetige Gleichverteilung U(a, b)",
    sig="„gleichverteilt zwischen a und b“, „jeder Zeitpunkt gleich wahrscheinlich“",
    ne="Yoğunluk sabit bir dikdörtgen: olasılık = genişlik × yükseklik.",
    fm=r"\[f(x)=\frac1{b-a}\ (a\le x\le b)\qquad F(x)=\frac{x-a}{b-a}\qquad E(X)=\frac{a+b}2\qquad Var(X)=\frac{(b-a)^2}{12}\qquad x_\alpha=a+\alpha(b-a)\]",
    bsp=r"\(U(0,20)\): \(P(X>15)=\frac5{20}=0.25\) · \(P(4\le X\le9)=\frac5{20}=0.25\) · \(E=10\), \(Var=\frac{400}{12}=33.333\)")

D.E("9.8", "Exponentialverteilung",
    sig="„Wartezeit“, „Zeit bis zum Defekt“, „im Mittel 3 Stunden“, Weibull mit r = 1",
    ne="Bekleme süresi. λ = 1 / ortalama. P(X > x) = e<sup>−λx</sup> (en çok kullanılan formül).",
    fm=r"\[f(x)=\lambda e^{-\lambda x}\ (x\ge0)\qquad F(x)=1-e^{-\lambda x}\qquad P(X>x)=e^{-\lambda x}\qquad E(X)=\frac1\lambda\qquad Var(X)=\frac1{\lambda^2}\qquad x_{med}=\frac{\log 2}{\lambda}\]",
    bsp=r"Mittel 4 Minuten → \(\lambda=0.25\): \(P(X>6)=e^{-1.5}=0.223\) · \(P(X\le2)=1-e^{-0.5}=0.393\) · Median \(=\frac{0.6931}{0.25}=2.773\)",
    fa="λ ist nicht der Mittelwert, sondern sein Kehrwert. Im Fuchs-Beispiel (im Mittel 3 h): λ = 1/3.")

D.E("9.9", "Normalverteilung: standardisieren und Φ ablesen",
    sig="„\\(X\\sim N(\\mu,\\sigma^2)\\)“, „Berechnen Sie \\(P(X\\le\\dots)\\)“",
    ne="Önce z = (x − μ)/σ ile standart normale çevir, sonra Φ tablosundan oku (Ek 15.1). Negatif z: Φ(−z) = 1 − Φ(z).",
    fm=r"\[Z=\frac{X-\mu}{\sigma}\sim N(0,1)\qquad P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)\qquad\Phi(-z)=1-\Phi(z)\qquad P(a<X<b)=\Phi(z_b)-\Phi(z_a)\]",
    st=["σ = Wurzel der Varianz!", "z berechnen (auf 2 Stellen für die Tabelle).", "„≤“ → Φ(z); „>“ → 1 − Φ(z); „zwischen“ → Differenz."],
    bsp=r"\(X\sim N(100,\,225)\) (σ = 15): \(P(X\le120)=\Phi(1.33)=0.908\) · \(P(X>85)=1-\Phi(-1)=\Phi(1)=0.841\) · \(P(85<X<115)=2\Phi(1)-1=0.683\)",
    fa="Bei \\(N(100, 225)\\) ist 225 die Varianz – durch σ = 15 teilen, nicht durch 225.")

D.E("9.10", "Normalverteilung: Quantile und σ-Regeln",
    sig="„Welchen Wert überschreiten nur 10 %?“, „um mehr als 2σ vom Mittel“",
    ne="Kantil: x<sub>α</sub> = μ + σ·z<sub>α</sub>. Önemli z değerlerini ezberle.",
    fm=r"\[x_\alpha=\mu+\sigma\,z_\alpha\qquad z_{1-\alpha}=-z_\alpha\qquad P(|X-\mu|\le\sigma)\approx0.683,\ \ 2\sigma:\ 0.954,\ \ 3\sigma:\ 0.997\]",
    extra="<table class='t c' style='width:auto'><tr><th>α</th><td>0.90</td><td>0.95</td><td>0.975</td><td>0.99</td><td>0.995</td></tr><tr><th>\\(z_\\alpha\\)</th><td>1.282</td><td>1.645</td><td>1.960</td><td>2.326</td><td>2.576</td></tr></table>",
    bsp=r"\(N(100,225)\): 90 %-Quantil \(=100+15\cdot1.282=119.23\) · 5 %-Quantil \(=100-15\cdot1.645=75.33\)")

D.E("9.11", "Summen und lineare Transformation normalverteilter ZV",
    sig="„10 unabhängige Packungen“, „Gesamtgewicht“, „\\(Y=2X+3\\)“",
    ne="Normal dağılımlıların doğrusal kombinasyonu yine normal: beklentiler toplanır, (bağımsızsa) varyanslar toplanır.",
    fm=r"\[aX+b\sim N(a\mu+b,\ a^2\sigma^2)\qquad X\pm Y\sim N(\mu_X\pm\mu_Y,\ \sigma_X^2+\sigma_Y^2)\ \text{(unabh.)}\qquad \sum_{i=1}^n X_i\sim N(n\mu,\ n\sigma^2)\qquad\bar X\sim N\!\left(\mu,\tfrac{\sigma^2}n\right)\]",
    bsp=r"\(X\sim N(10,4),\ Y\sim N(20,9)\) unabhängig: \(X+Y\sim N(30,13)\), \(X-Y\sim N(-10,13)\), \(3X+1\sim N(31,36)\)",
    fa="Summe von n gleichen ZV (Varianz \\(n\\sigma^2\\)) ≠ n-faches einer ZV (Varianz \\(n^2\\sigma^2\\)).")

D.E("9.12", "Zentraler Grenzwertsatz (ZGWS)",
    sig="„Geben Sie die approximative Verteilung von \\(\\bar X\\) an“, n groß (n ≥ 30)",
    ne="n büyükse \\(\\bar X\\) yaklaşık normal: ortalama μ, varyans σ²/n — X'in kendi dağılımı ne olursa olsun.",
    fm=r"\[\bar X\overset{a}{\sim}N\!\left(\mu,\ \frac{\sigma^2}{n}\right)\qquad\sum X_i\overset{a}{\sim}N(n\mu,\ n\sigma^2)\qquad P(\bar X\le c)\approx\Phi\!\left(\frac{c-\mu}{\sigma/\sqrt n}\right)\]",
    bsp=r"n = 36, μ = 50, σ = 12: \(\bar X\overset a\sim N(50,\,4)\) · \(P(\bar X>53)\approx1-\Phi(1.5)=0.067\) · Testat-Typ: \(E(X)=4\) → \(P(\bar X<4)\approx\Phi(0)=0.5\)",
    fa="Standardabweichung von \\(\\bar X\\) ist \\(\\sigma/\\sqrt n\\), nicht σ.")

D.E("9.13", "t- und χ²-Verteilung (wo sie vorkommen)",
    sig="„t-Quantil“, „\\(\\chi^2_{n-1;0.95}\\)“, „df“, R-Output mit qt / qchisq",
    ne="t: σ bilinmiyorsa ortalama için (KI 12.3, t-Test 13.6). χ²: varyans için (12.5, 13.9) ve χ²-testleri. Kantiller sınavda verilir.",
    st=["<b>t(df)</b>: symmetrisch um 0, breiter als N(0, 1); für großes df ≈ N(0, 1). \\(t_{df;\\alpha}=-t_{df;1-\\alpha}\\).",
        "<b>χ²(df)</b>: nur positive Werte, rechtsschief, nicht symmetrisch → untere und obere Quantile getrennt nachschlagen.",
        "Freiheitsgrade: t-Test/KI für μ: n − 1 · Varianz: n − 1 · χ²-Unabhängigkeit: (J − 1)(K − 1) · χ²-Anpassung: J − 1."],
    extra="<p class='small'>Tabellen mit Quantilen: Anhang 15.2 und 15.3.</p>")

D.E("9.14", "Bivariate Normalverteilung (selten, Kür)",
    sig="„bivariat normalverteilt mit ρ“, „bedingte Verteilung von Y gegeben X = x“",
    ne="Marjinaller normal. Koşullu dağılım da normal; varyans küçülür.",
    fm=r"\[Y\mid X=x\ \sim\ N\!\left(\mu_y+\rho\frac{\sigma_y}{\sigma_x}(x-\mu_x),\ \ \sigma_y^2(1-\rho^2)\right)\]",
    bsp=r"\(\mu_x=170,\ \mu_y=70,\ \sigma_x=10,\ \sigma_y=12,\ \rho=0.6\), \(x=180\): \(E=77.2\), \(Var=92.16\) → \(P(Y>80\mid X=180)=1-\Phi\left(\frac{80-77.2}{9.6}\right)=1-\Phi(0.2917)=0.385\)")
