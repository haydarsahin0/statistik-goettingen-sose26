"""Formelsammlung Statistik – Abschnitte 0–6 (Werkzeug + deskriptive Statistik)."""
from fs_stat_doc import D

# =====================================================================
D.S("0", "Werkzeugkasten: Klausurregeln und Mathe",
    "Bu bölüm her soruda lazım: kurallar, logaritma, toplam/çarpım işareti, türev, integral. Takıldığın matematik adımı için buraya bak.")

D.E("0.1", "Klausurregeln Teil A (gelten für jede Aufgabe)",
    sig="Deckblatt und Hinweise der Probeklausur, Abschlusssitzung",
    ne="Bu kurallara uymazsan doğru hesapta bile puan kaybedersin.",
    st=["<b>Endergebnis</b> auf <b>3 Nachkommastellen</b> (kaufmännisch: ab 5 aufrunden), <b>Zwischenergebnisse</b> mit mindestens <b>4</b>. Vollständig gekürzte Brüche sind erlaubt (\\(\\tfrac{19}{49}\\)). Ganze Zahlen und Ausdrücke wie \\(\\sqrt2\\) oder \\(\\log 4\\) bleiben stehen.",
        "<b>Dezimalpunkt</b>: 0.375, nicht 0,375.",
        "Gewertet wird nur, was im <b>Lösungskästchen</b> steht. „Geben Sie Ihren Lösungsweg an“ → der Weg gehört ins Kästchen.",
        "<b>Nur eine</b> Lösung pro Kästchen. Falsches sauber durchstreichen.",
        "Aufgabe widersprüchlich? „<b>nicht lösbar</b>“ ins Kästchen und Begründung in die Box am Ende.",
        "Kugelschreiber/Tinte, <b>kein Bleistift, nicht rot, nicht grün</b>. Taschenrechner von der Positivliste. 1 handgeschriebenes A4-Blatt (beidseitig).",
        "Zeit: 100 Minuten für 75 Punkte → <b>1 Punkt ≈ 1.3 Minuten</b>. Länger als 5 Minuten fest? Weiter, später zurück."],
    fa="Zwischenergebnisse nicht auf 3 Stellen runden und damit weiterrechnen – bei Varianz und Bayes verschiebt sich sonst das Ergebnis.",
    ks="Folgefehler werden berücksichtigt – nie ein Kästchen leer lassen; mit dem eigenen Zwischenergebnis weiterrechnen.")

D.E("0.2", "Logarithmus und Potenzen",
    sig="log, ln, exp, e<sup>x</sup> – vor allem bei Maximum-Likelihood",
    ne="Bu derste <b>log = ln</b> (doğal logaritma). Hesap makinesinde <b>ln</b> tuşu! Kontrol: ln 2 = 0.6931 (0.3010 çıkıyorsa yanlış tuş).",
    fm=r"\[\log(ab)=\log a+\log b\qquad \log\tfrac ab=\log a-\log b\qquad \log(a^b)=b\log a\qquad \log(e^x)=x\qquad e^{\log x}=x\qquad \log 1=0\]"
       r"\[a^m\cdot a^n=a^{m+n}\qquad (a^m)^n=a^{m\cdot n}\qquad a^{-n}=\tfrac1{a^n}\qquad \sqrt a=a^{1/2}\qquad e^a\cdot e^b=e^{a+b}\qquad \log\tfrac1a=-\log a\]",
    bsp=r"\(\log\left(\theta^n e^{-\theta\sum x_i}\right)=n\log\theta-\theta\sum x_i\) · \(\log(2^{-\beta x})=-\beta x\log 2\)",
    fa=r"\(\log(a+b)\ne\log a+\log b\). Mit log₁₀ statt ln wird jedes Ergebnis um den Faktor 2.3026 zu klein.")

D.E("0.3", "Summen- und Produktzeichen",
    sig="\\(\\sum\\), \\(\\prod\\), „Hinweis: \\(\\sum x_i=\\dots\\)“",
    ne="Σ = topla, Π = çarp. İndeksi (i) olmayan sabit dışarı çıkar: Σ'de n·c, Π'de c<sup>n</sup> olur.",
    fm=r"\[\sum_{i=1}^n c=n\,c\qquad \sum c\,x_i=c\sum x_i\qquad \sum(x_i+y_i)=\sum x_i+\sum y_i\qquad \sum_{i=1}^n x_i=n\bar x\qquad \sum(x_i-\bar x)=0\]"
       r"\[\prod_{i=1}^n c=c^n\qquad \prod c\,x_i=c^n\prod x_i\qquad \prod a^{x_i}=a^{\sum x_i}\qquad \prod e^{-\lambda x_i}=e^{-\lambda\sum x_i}\qquad \log\prod a_i=\sum\log a_i\]",
    bsp=r"\(\prod_{i=1}^n \lambda e^{-\lambda x_i}=\lambda^n e^{-\lambda\sum x_i}\) · \(\sum_{i=1}^{4}(2x_i+1)=2\sum x_i+4\)",
    fa=r"\(\sum x_i^2\ne\left(\sum x_i\right)^2\) · \(\prod c=c^n\), nicht \(n\cdot c\) · Terme mit Index (\(x_i\)) dürfen nicht vor das Zeichen.")

D.E("0.4", "Ableiten (für ML und Extremwerte)",
    sig="„Bestimmen Sie den ML-Schätzer“, „Bedingung zweiter Ordnung“",
    ne="ML'de türev her zaman <b>parametreye göre</b> (θ, λ, p, π) alınır. Veriler (x<sub>i</sub>, Σx<sub>i</sub>, n) sabit sayı gibi davranır.",
    fm=r"\[(x^n)'=n\,x^{n-1}\qquad(\log x)'=\tfrac1x\qquad(e^x)'=e^x\qquad(e^{cx})'=c\,e^{cx}\qquad(c\cdot f)'=c\cdot f'\qquad c'=0\]"
       r"\[(\log(1-x))'=\tfrac{-1}{1-x}\qquad(\log(x+1))'=\tfrac1{x+1}\qquad\left(\tfrac n\theta\right)'=-\tfrac n{\theta^2}\qquad\left(\tfrac{1}{\theta^2}\right)'=-\tfrac2{\theta^3}\qquad (f(g(x)))'=f'(g(x))\cdot g'(x)\]",
    bsp=r"\(\ell(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log(x_i!)\ \Rightarrow\ \ell'(\lambda)=\frac{\sum x_i}{\lambda}-n\) (der letzte Term enthält kein λ → fällt weg) · \(\ell''(\lambda)=-\frac{\sum x_i}{\lambda^2}\)",
    fa="Konstanten ohne Parameter fallen beim Ableiten weg – beim Logarithmieren aber nicht einfach weglassen, sondern hinschreiben.")

D.E("0.5", "Integrieren (für Dichten)",
    sig="Dichte \\(f(x)\\), „gültige Dichtefunktion“, \\(E(X)\\) stetig, \\(P(a\\le X\\le b)\\)",
    ne="Yoğunlukta <b>integral = alan = olasılık</b>. Neredeyse her soruda kuvvet kuralı yeter: üssü 1 artır, yeni üsse böl.",
    fm=r"\[\int x^n\,dx=\frac{x^{n+1}}{n+1}\ (n\ne-1)\qquad\int c\,dx=c\,x\qquad\int e^{-\lambda x}dx=-\tfrac1\lambda e^{-\lambda x}\qquad\int_a^b f(x)\,dx=\big[F(x)\big]_a^b=F(b)-F(a)\]",
    st=["Integral in Summanden zerlegen, Konstanten vor das Integral ziehen.",
        "Stammfunktion bilden (Potenzregel).",
        "Grenzen einsetzen: <b>obere minus untere</b>.",
        "Stückweise definierte Dichte: jedes Stück über <b>sein</b> Intervall integrieren und addieren."],
    bsp=r"\(\int_0^2\frac x2\,dx=\left[\frac{x^2}{4}\right]_0^2=\frac44-0=1\) · \(\int_1^3(x-1)\,dx=\left[\frac{x^2}2-x\right]_1^3=1.5-(-0.5)=2\)",
    fa="Untere Grenze vergessen (\\(-F(a)\\)) – nur bei a = 0 und \\(F(0)=0\\) ist sie wirklich 0.")

D.E("0.6", "Fakultät, Binomialkoeffizient, Abzählen",
    sig="„auf wie viele Arten“, \\(\\binom nk\\), Ziehen mit/ohne Zurücklegen, Lotto",
    ne="\\(\\binom nk\\) = n eleman içinden sırasız k tane seçme sayısı. Hesap makinesinde <b>nCr</b>.",
    fm=r"\[n!=1\cdot2\cdots n,\quad 0!=1\qquad\binom nk=\frac{n!}{k!\,(n-k)!}\qquad\binom n0=\binom nn=1\qquad\binom n1=n\qquad\binom nk=\binom n{n-k}\]",
    extra=("<table class='t'><tr><th>k aus n ziehen</th><th>mit Zurücklegen</th><th>ohne Zurücklegen</th></tr>"
           "<tr><td>mit Reihenfolge</td><td>\\(n^k\\)</td><td>\\(\\frac{n!}{(n-k)!}\\)</td></tr>"
           "<tr><td>ohne Reihenfolge</td><td>\\(\\binom{n+k-1}{k}\\)</td><td>\\(\\binom nk\\)</td></tr></table>"),
    bsp=r"\(\binom52=\frac{5\cdot4}{2\cdot1}=10\) · 3 Ziffern aus 0–9 mit Zurücklegen: \(10^3=1000\) · 6 aus 49 (Lotto): \(\binom{49}6=13\,983\,816\)",
    fa="Ohne Zurücklegen ist nicht binomialverteilt – dafür 7.12 benutzen.")

D.E("0.7", "Taschenrechner als Kontrolle",
    sig="Mittelwert, Varianz, Korrelation, Regressionsgerade nachprüfen",
    ne="Hesap makinesi kontrol içindir; çözüm yolunu yine de kutuya yaz.",
    st=["1 Variable: Menü → Statistik → <i>1-Variable</i> → Werte eingeben (ggf. Häufigkeitsspalte einschalten) → OPTN → <i>1-Variablen-Berechnung</i>: \\(\\bar x,\\ \\sum x,\\ \\sum x^2,\\ \\sigma x,\\ sx\\).",
        "2 Variablen: Menü → Statistik → <i>y = a + bx</i> → x und y eingeben → OPTN → <i>Regressionsberechnung</i> (a, b, r) bzw. <i>2-Variablen-Berechnung</i> (\\(\\sum xy\\)).",
        "\\(\\sigma x\\) = \\(s\\) (Nenner n) · \\(sx\\) = \\(s_*\\) (Nenner n − 1)."],
    fa="Tastenwege unterscheiden sich je Modell – vor der Klausur mit deinem Rechner üben.")

# =====================================================================
D.S("1", "Grundbegriffe, Merkmale, Stichproben (V01)",
    "Puanı kolay, kelimeleri doğru seçmek yeter. Her cevapta gerekçe yaz.")

D.E("1.1", "Grundgesamtheit, Stichprobe, Einheit, Merkmal",
    sig="„Was ist die Grundgesamtheit / statistische Einheit / das Merkmal?“",
    ne="Birim = verinin toplandığı nesne · Grundgesamtheit = soruyla ilgili <b>tüm</b> birimler · Stichprobe = incelenen alt küme · Merkmal = ölçülen özellik.",
    st=["<b>Statistische Einheit</b>: Objekt, an dem gemessen wird (im Singular nennen: „ein Kunde“). Kann abstrakt sein (ein Spiel, ein Tag).",
        "<b>Grundgesamtheit</b>: alle relevanten Einheiten, mit Ort und Zeit („alle Studierenden der Uni Göttingen im SoSe 26“). Kann hypothetisch sein.",
        "<b>Stichprobe</b>: tatsächlich untersuchte Teilmenge. <b>Merkmal</b> X (groß) = Eigenschaft; <b>Ausprägung</b> x (klein) = konkreter Wert.",
        "<b>Deskriptiv</b> = Daten beschreiben · <b>induktiv</b> = von der Stichprobe auf die Grundgesamtheit schließen, unter Berücksichtigung der Unsicherheit."],
    fa="Nicht die Notation (Ω) wiedergeben, sondern die Eigenschaft im Sachkontext erklären.")

D.E("1.2", "Diskret oder stetig?",
    sig="„Geben Sie an, ob ein diskretes oder stetiges Merkmal vorliegt“",
    ne="Sayılabilir değerler (adet) → diskret. Bir aralıktaki her değer mümkün (süre, ağırlık, para) → stetig.",
    st=["<b>Diskret</b>: endlich oder abzählbar unendlich viele Ausprägungen (Anzahl, Note, Kategorie). Nominale/ordinale Merkmale sind immer diskret.",
        "<b>Stetig</b>: jeder Wert in einem Intervall möglich (Zeit, Gewicht, Länge, Einkommen).",
        "<b>Quasi-stetig</b>: gerundet gemessen, aber wie stetig behandelt (Größe in cm, Geldbeträge)."],
    bsp="Anzahl Mensabesuche → diskret · Wartezeit in Minuten → stetig · Lieblingsfarbe → diskret (nominal)",
    ks="„X ist ein stetiges Merkmal, da (in einem Intervall) jeder reelle Wert angenommen werden kann.“")

D.E("1.3", "Skalenniveau bestimmen",
    sig="„Welches Skalenniveau liegt zugrunde?“, „Ist der Median sinnvoll?“",
    ne="nominal = sadece isim · ordinal = sıralanır, farklar yorumlanmaz · kardinal (metrisch) = farklar anlamlı. Ölçek, hangi ölçünün anlamlı olduğunu belirler.",
    extra=("<table class='t'><tr><th>Skala</th><th>Bedeutung</th><th>Beispiele</th><th>sinnvolle Maße</th></tr>"
           "<tr><td>nominal</td><td>nur Namen, keine Ordnung</td><td>Fach, Partei, Farbe, Mensa</td><td>Modus</td></tr>"
           "<tr><td>ordinal</td><td>ordnen ja, Abstände nicht interpretierbar</td><td>Schulnote, Zufriedenheit 1–5, Rang</td><td>Modus, Median, Quantile</td></tr>"
           "<tr><td>kardinal (metrisch)</td><td>Abstände (oft auch Verhältnisse) sinnvoll</td><td>Alter, Zeit, Punkte 0–100, Einkommen</td><td>alle: Mittel, Varianz, Korrelation</td></tr></table>"),
    st=["Frage: Kann ich ordnen? Nein → nominal.", "Ja: Haben Abstände eine Bedeutung (2→3 so viel wie 7→8)? Nein → ordinal, ja → kardinal.",
        "0/1-kodiert (binär): Mittelwert = Anteil (sinnvoll). In der Probeklausur-Lösung: „ordinal/binär“."],
    fa="Skala 1–5 ist ordinal (nicht kardinal, auch wenn es Zahlen sind). Punkte 0–100 sind kardinal.",
    ks="„Der Median ist für das Merkmal nicht sinnvoll, da es nominal skaliert ist und sich die Ausprägungen nicht ordnen lassen.“")

D.E("1.4", "Stichprobenverfahren",
    sig="„Wie heißt dieses Stichprobenverfahren?“, „repräsentativ“",
    ne="Basit rastgele · katmanlı (her gruptan rastgele) · küme (tüm grupları rastgele seç) · kota (rastgele değil).",
    extra=("<table class='t'><tr><th>Verfahren</th><th>Wie?</th><th>Merkmal</th></tr>"
           "<tr><td>einfache Zufallsstichprobe</td><td>jede Einheit / jede Stichprobe gleich wahrscheinlich</td><td>nur zufällige Unterschiede</td></tr>"
           "<tr><td>geschichtet</td><td>Gruppen (Schichten) bilden, aus <b>jeder</b> Schicht zufällig ziehen</td><td>jede Gruppe sicher vertreten</td></tr>"
           "<tr><td>Klumpen</td><td>zufällig <b>ganze</b> Gruppen ziehen (Schulklassen, Orte), darin alle befragen</td><td>billig; Klumpen innen heterogen</td></tr>"
           "<tr><td>Quote</td><td>vorgegebene Quoten bewusst erfüllen</td><td>nicht zufällig</td></tr></table>"),
    fa="„Aus jedem Stadtteil 30 zufällig“ = geschichtet. „3 Stadtteile zufällig, dort alle“ = Klumpen.",
    ks="„Repräsentativ heißt: keine systematischen Unterschiede zwischen Stichprobe und Grundgesamtheit.“")

D.E("1.5", "Versuchsplanung, Störvariablen",
    sig="„Störvariable“, „Wie kann man den Einfluss kontrollieren?“",
    ne="Störvariable: sonucu etkileyen ama incelenmeyen değişken (yaş, ön bilgi). Kontrol: Homogenisierung, Randomisierung, Modellierung.",
    st=["<b>Homogenisierung</b>: Gruppen bilden, in denen die Störvariable gleich ist.",
        "<b>Randomisierung</b>: Einheiten zufällig auf Gruppen (mit/ohne Maßnahme) verteilen.",
        "<b>Statistische Modellierung</b>: Störvariable in der Analyse berücksichtigen (z. B. als weitere Variable in der Regression)."])

# =====================================================================
D.S("2", "Häufigkeiten, Verteilungsfunktion, Histogramm (V02)",
    "Tablo tamamlama, ampirik dağılım fonksiyonu ve histogram: Probeklausur 2022'de 10+ puan.")

D.E("2.1", "Häufigkeitstabelle vervollständigen",
    sig="Tabelle mit \\(h_j,\\ f_j,\\ H_j,\\ F_j\\) und Lücken",
    ne="h = mutlak sıklık · f = oran (h/n) · H = birikimli sıklık · F = birikimli oran. İleri toplama, geri çıkarma.",
    fm=r"\[f_j=\frac{h_j}{n}\qquad H_j=h_1+\dots+h_j\qquad F_j=\frac{H_j}{n}=f_1+\dots+f_j\qquad h_j=H_j-H_{j-1}\qquad n=\sum h_j\]",
    st=["n bestimmen (\\(\\sum h_j\\) oder letztes \\(H_J\\)).", "Fehlende \\(h\\) aus \\(f\\cdot n\\) oder aus \\(H_j-H_{j-1}\\).",
        "Kontrolle: \\(\\sum f_j=1\\), letztes \\(F=1\\), F nie fallend."],
    bsp=r"\(h=3,7,8,5,2\) (n = 25) → \(f=0.12;\ 0.28;\ 0.32;\ 0.20;\ 0.08\) · \(F=0.12;\ 0.40;\ 0.72;\ 0.92;\ 1\)")

D.E("2.2", "Wörter in Verteilungsfunktion übersetzen (diskret)",
    sig="„höchstens“, „mindestens“, „mehr als“, „weniger als“, „zwischen“",
    ne="Her soruyu önce „≤“ biçimine çevir; F(x) her zaman „x dahil o noktaya kadar“ demektir.",
    extra=("<table class='t'><tr><th>Wortlaut (ganzzahlige Werte)</th><th>Rechnung</th><th>Wortlaut</th><th>Rechnung</th></tr>"
           "<tr><td>höchstens k (≤ k)</td><td>\\(F(k)\\)</td><td>mehr als k (&gt; k)</td><td>\\(1-F(k)\\)</td></tr>"
           "<tr><td>weniger als k (&lt; k)</td><td>\\(F(k-1)\\)</td><td>mindestens k (≥ k)</td><td>\\(1-F(k-1)\\)</td></tr>"
           "<tr><td>zwischen a und b (beide inkl.)</td><td>\\(F(b)-F(a-1)\\)</td><td>genau k</td><td>\\(f(k)\\) bzw. \\(P(X=k)\\)</td></tr></table>"),
    fa="Bei stetigen Merkmalen/Zufallsvariablen ist „<“ = „≤“ (eine einzelne Stelle hat Wahrscheinlichkeit 0). Bei diskreten nicht!",
    bsp=r"Mit \(F=0.12;0.40;0.72;0.92;1\) für die Werte 0, 1, 2, 3, 5: mehr als 1 → \(1-0.40=0.6\) · mindestens 3 → \(1-F(2)=0.28\)")

D.E("2.3", "Empirische Verteilungsfunktion aufstellen und zeichnen",
    sig="„Stellen Sie \\(\\hat F(x)\\) auf“, „Zeichnen Sie die empirische Verteilungsfunktion“",
    ne="\\(\\hat F(x)\\) = x'e eşit veya küçük gözlemlerin oranı. Merdiven fonksiyonu: her farklı değerde zıplar.",
    fm=r"\[\hat F(x)=\frac{\#\{i:\ x_i\le x\}}{n}\]",
    st=["Daten <b>sortieren</b>, verschiedene Werte \\(a_1&lt;a_2&lt;\\dots\\) mit kumulierten Anteilen \\(F_j\\).",
        "Fallunterscheidung: 0 für \\(x&lt;a_1\\); \\(F_1\\) für \\(a_1\\le x&lt;a_2\\); …; 1 für \\(x\\ge a_J\\).",
        "Skizze: waagerechte Stufen, <b>● links</b> (Wert gehört dazu), <b>○ rechts</b>; keine senkrechten Linien; Achsen beschriften; links bei 0 und rechts bei 1 weiterlaufen lassen."],
    bsp=r"Daten 1, 1, 2, 4, 4, 4 (n = 6): \(\hat F(x)=\begin{cases}0 & x<1\\ \tfrac13 & 1\le x<2\\ 0.5 & 2\le x<4\\ 1 & x\ge4\end{cases}\)",
    fa="Probeklausur: 6 Punkte für diese Aufgabe. Punkte (●/○) und die Fortsetzung nach links/rechts werden bewertet.")

D.E("2.4", "Histogramm: Säulenhöhen (Dichte)",
    sig="„normiertes Histogramm“, „Höhen der Säulen“, „Klassieren Sie“",
    ne="Histogramda <b>alan</b> = oran. Yükseklik = oran / sınıf genişliği. Toplam alan 1.",
    fm=r"\[\text{Höhe}_j=\frac{f_j}{\text{Breite}_j}=\frac{h_j}{n\cdot\text{Breite}_j}\qquad\sum_j \text{Höhe}_j\cdot\text{Breite}_j=1\]",
    st=["Werte den Klassen zuordnen (Klammern beachten: [a, b) heißt a gehört dazu, b nicht).", "\\(f_j=h_j/n\\).", "Höhe = \\(f_j\\) / Breite.", "Kontrolle: Summe aller Flächen = 1."],
    bsp=r"n = 50: [0, 10): 10 · [10, 20): 25 · [20, 40]: 15 → \(f=0.2;\ 0.5;\ 0.3\) → Höhen \(0.02;\ 0.05;\ 0.015\)",
    fa="Bei ungleichen Klassenbreiten nicht die Häufigkeit als Höhe nehmen (= Säulendiagramm, verzerrt).")

D.E("2.5", "Anteil aus dem Histogramm ablesen",
    sig="„Schätzen Sie den Anteil zwischen … und …“, „Welche Annahme treffen Sie?“",
    ne="İstenen aralığı sınıflara böl, her parça için genişlik × yükseklik, topla. Varsayımı yaz: sınıf içinde düzgün dağılım.",
    st=["Intervall an den Klassengrenzen zerschneiden.", "Je Stück: <b>Stückbreite × Höhe</b>.", "Addieren. Anzahl = Anteil × n.",
        "Annahme hinschreiben: Werte innerhalb jeder Klasse gleichmäßig verteilt."],
    bsp=r"Mit den Höhen aus 2.4, Anteil zwischen 15 und 30: \(5\cdot0.05+10\cdot0.015=0.25+0.15=0.4\)",
    ks="„Annahme: Die Beobachtungen sind innerhalb der Klassen gleichmäßig verteilt.“")

D.E("2.6", "Diagramm wählen, Modalklasse, Form",
    sig="„Säulendiagramm oder Histogramm?“, „Modalklasse“, „rechtsschief“",
    ne="Histogram = alan orantılı (sürekli veri). Sütun grafiği = yükseklik orantılı. Modal sınıf = en çok gözlemli sınıf (en yüksek sütun olmayabilir!).",
    st=["<b>Modalklasse</b> = Klasse mit größtem \\(h_j\\). Bei ungleichen Breiten nicht unbedingt die höchste Säule.",
        "<b>Rechtsschief = linkssteil</b>: langer Schwanz rechts, \\(\\bar x&gt;x_{med}&gt;x_{mod}\\). <b>Linksschief = rechtssteil</b>: umgekehrt.",
        "uni-/bi-/multimodal = ein/zwei/mehrere Gipfel."],
    fa="„Die Modalklasse ist immer die höchste Säule“ → im Allgemeinen <b>falsch</b> (nur bei gleich breiten Klassen).")

# =====================================================================
D.S("3", "Lagemaße (V02)", "Ortalama, medyan, mod: hangisi ne zaman anlamlı ve nasıl hesaplanır.")

D.E("3.1", "Arithmetisches Mittel",
    sig="„Berechnen Sie das arithmetische Mittel \\(\\bar x\\)“",
    ne="Hepsini topla, n'e böl. Tablodan: değer × oran, topla.",
    fm=r"\[\bar x=\frac1n\sum_{i=1}^n x_i\qquad\bar x=\sum_j a_j f_j=\frac1n\sum_j a_j h_j\]",
    bsp=r"2, 5, 3, 8, 4, 3, 6, 25, 4, 5: \(\bar x=\frac{65}{10}=6.5\)",
    fa="Nur für kardinale (und 0/1-)Merkmale. Nicht robust: ein Ausreißer (25) zieht das Mittel hoch.")

D.E("3.2", "Median",
    sig="„Bestimmen Sie den Median \\(x_{med}\\)“",
    ne="Veriyi sırala, ortadaki değer. n çiftse ortadaki iki değerin ortalaması.",
    fm=r"\[x_{med}=\begin{cases}x_{\left(\frac{n+1}{2}\right)} & n\ \text{ungerade}\\[4pt] \dfrac{x_{(n/2)}+x_{(n/2+1)}}{2} & n\ \text{gerade}\end{cases}\]",
    st=["<b>Sortieren</b>; \\(x_{(i)}\\) = i-ter Wert der sortierten Liste.", "Platz berechnen; bei Tabellen den Platz über die kumulierten \\(H_j\\) finden."],
    bsp=r"Sortiert 2, 3, 3, 4, 4, 5, 5, 6, 8, 25 (n = 10): \(x_{med}=\frac{x_{(5)}+x_{(6)}}2=\frac{4+5}2=4.5\)",
    fa="Nicht aus der unsortierten Liste und nicht aus der Liste der <i>verschiedenen</i> Werte ablesen. Ab ordinal sinnvoll.",
    ks="„Der Median ist robuster gegenüber Ausreißern als das arithmetische Mittel.“")

D.E("3.3", "Modus",
    sig="„Modus \\(x_{mod}\\)“, „häufigste Ausprägung“",
    ne="En sık görülen değer. Her ölçekte (nominal dahil) anlamlı. Birden fazla olabilir.",
    bsp="2, 3, 3, 4, 4, 5, 5, 6, 8, 25 → drei Modi: 3, 4, 5 (alle zweimal). Bei Kategorien: die Kategorie mit der größten Häufigkeit nennen (nicht die Häufigkeit).")

D.E("3.4", "Mittelwert klassierter Daten",
    sig="„Klassieren Sie … und bestimmen Sie den Mittelwert für die klassierten Daten“",
    ne="Her sınıfın gözlemleri sınıf ortasında kabul edilir. Sonuç gerçek ortalamaya yaklaşık eşittir.",
    fm=r"\[m_j=\frac{c_{j-1}+c_j}{2}\qquad\bar x_K=\sum_j f_j\,m_j\qquad s_K^2=\sum_j f_j m_j^2-\bar x_K^2\]",
    st=["Werte zählen → \\(h_j\\), \\(f_j\\).", "Klassenmitten \\(m_j\\).", "\\(\\bar x_K=\\sum f_jm_j\\)."],
    bsp=r"\(f=0.2;0.5;0.3\) mit Mitten 5, 15, 30: \(\bar x_K=1+7.5+9=17.5\)",
    fa="Klassengrenzen genau beachten: [0, 10) enthält 10 nicht.")

D.E("3.5", "Gesamtmittel aus Gruppen, Wert korrigieren",
    sig="„Gruppe A … Gruppe B … Mittelwert insgesamt“, „ein Wert wurde falsch erfasst“",
    ne="Toplam ortalama = ağırlıklı ortalama. Değer düzeltirken toplam üzerinden git: \\(\\sum x_i=n\\bar x\\).",
    fm=r"\[\bar x=\frac{n_1\bar x_1+n_2\bar x_2+\dots}{n_1+n_2+\dots}\qquad\sum x_i=n\bar x\]",
    bsp=r"A: 20 Personen, \(\bar x=3\); B: 30 Personen, \(\bar x=5\) → \(\frac{60+150}{50}=4.2\) · Wert 14 statt 9 bei n = 5, \(\bar x=7\): neue Summe \(35+5=40\) → \(\bar x=8\)",
    fa="Nicht einfach \\((3+5)/2=4\\) rechnen – die Gruppengrößen gewichten.")

D.E("3.6", "Lage und Schiefe, lineare Transformation",
    sig="„Wie ändert sich der Mittelwert, wenn …“, „°C in °F“, „rechtsschief“",
    ne="y = a + b·x dönüşümünde ortalama, medyan, mod ve kantiller aynı şekilde dönüşür.",
    fm=r"\[y_i=a+b\,x_i\ \Rightarrow\ \bar y=a+b\,\bar x,\quad y_{med}=a+b\,x_{med}\qquad\text{rechtsschief: }\bar x>x_{med}>x_{mod}\]",
    bsp=r"Mittel 20 °C → \(32+1.8\cdot20=68\) °F · Minuten → Sekunden: Mittel × 60",
    fa="Für nichtlineare Funktionen (log, Quadrat) gilt das nur für den Median, nicht für den Mittelwert.")

# =====================================================================
D.S("4", "Streuung, Quantile, Boxplot (V02)", "Varyans: hangi formül (1/n mi 1/(n−1) mi) sorulduğuna dikkat.")

D.E("4.1", "α-Quantil (Definition der Vorlesung)",
    sig="„Quartil“, „unteres/oberes Quartil“, „90 %-Quantil“, „Dezil“",
    ne="n·α = sıra numarası. Tam sayı değilse <b>yukarı yuvarla</b>; tam sayıysa o sıradaki ile bir sonrakinin ortalaması.",
    fm=r"\[x_\alpha=\begin{cases}x_{(\lceil n\alpha\rceil)} & n\alpha\ \text{nicht ganzzahlig (aufrunden)}\\[3pt] \dfrac{x_{(n\alpha)}+x_{(n\alpha+1)}}{2} & n\alpha\ \text{ganzzahlig}\end{cases}\]",
    st=["Sortieren.", "\\(n\\alpha\\) berechnen – das ist die <b>Platznummer</b>.", "Regel anwenden."],
    bsp=r"Sortiert 2, 3, 3, 4, 4, 5, 5, 6, 8, 25: \(x_{0.25}\): \(10\cdot0.25=2.5\) → Platz 3 → 3 · \(x_{0.75}\): \(7.5\) → Platz 8 → 6",
    fa="R (quantile) rechnet anders – in Teil A immer die Definition der Vorlesung benutzen.")

D.E("4.2", "Varianz und Standardabweichung",
    sig="„empirische Varianz \\(s^2\\)“, „unverzerrte / korrigierte Varianz \\(s_*^2\\)“, „Standardabweichung“",
    ne="Empirische Varianz: n'e böl. Unverzerrt (s*²): n−1'e böl. Standart sapma = karekök. R'deki var/sd = n−1.",
    fm=r"\[s^2=\frac1n\sum(x_i-\bar x)^2=\frac1n\sum x_i^2-\bar x^2\qquad s_*^2=\frac1{n-1}\sum(x_i-\bar x)^2=\frac{n}{n-1}\,s^2\qquad s=\sqrt{s^2}\]",
    st=["\\(\\bar x\\) und \\(\\sum x_i^2\\) bestimmen (oft als Hinweis gegeben).", "\\(s^2=\\frac{\\sum x_i^2}{n}-\\bar x^2\\).", "Falls verlangt: \\(s_*^2=\\frac n{n-1}s^2\\), Wurzel für s."],
    bsp=r"\(\sum x_i=65,\ \sum x_i^2=829,\ n=10\): \(s^2=82.9-6.5^2=40.65\) · \(s_*^2=\frac{10}{9}\cdot40.65=45.167\) · \(s=6.376\)",
    fa="„empirische Varianz“ = Nenner n. Nur bei „unverzerrt / korrigiert / \\(s_*\\)“ Nenner n − 1. Varianz ist nie negativ.",
    ks="„Die Standardabweichung hat dieselbe Maßeinheit wie das Merkmal und ist daher leichter zu interpretieren.“")

D.E("4.3", "Varianz aus einer Häufigkeitstabelle",
    sig="Tabelle mit Ausprägungen \\(a_j\\) und \\(h_j\\) bzw. \\(f_j\\)",
    ne="Önce ortalama, sonra kareler ortalaması; fark = varyans.",
    fm=r"\[\bar x=\sum a_jf_j\qquad s^2=\sum a_j^2f_j-\bar x^2\]",
    bsp=r"Werte 0, 1, 2 mit \(f=0.5;0.3;0.2\): \(\bar x=0.7\), \(\sum a_j^2f_j=0.3+0.8=1.1\) → \(s^2=1.1-0.49=0.61\)")

D.E("4.4", "Spannweite, IQR, Wirkung von Transformationen",
    sig="„Interquartilsabstand“, „Spannweite“, „Daten werden in … umgerechnet“",
    ne="IQR = x<sub>0.75</sub> − x<sub>0.25</sub>. y = a + bx: a (kaydırma) yayılımı değiştirmez; b ile çarpılır (varyansta b²).",
    fm=r"\[\text{IQR}=x_{0.75}-x_{0.25}\qquad\text{Spannweite}=x_{max}-x_{min}\qquad y=a+bx:\ s_y^2=b^2s_x^2,\ s_y=|b|\,s_x,\ \text{IQR}_y=|b|\,\text{IQR}_x\]",
    bsp=r"IQR = 6 − 3 = 3 (Daten aus 4.1) · Minuten → Sekunden: Varianz × 3600, Standardabweichung × 60")

D.E("4.5", "Boxplot und Ausreißer",
    sig="„Zeichnen Sie einen Boxplot“, „Gibt es Ausreißer?“, „Wo enden die Whisker?“",
    ne="Kutu = x<sub>0.25</sub>…x<sub>0.75</sub>, ortada medyan. Sınırlar: Q1 − 1.5·IQR ve Q3 + 1.5·IQR. Bıyık, sınırın içindeki en uç <b>gerçek veri</b> değerinde biter.",
    fm=r"\[\text{untere Grenze}=x_{0.25}-1.5\,\text{IQR}\qquad\text{obere Grenze}=x_{0.75}+1.5\,\text{IQR}\]",
    st=["Quartile und Median (4.1, 3.2).", "Grenzen berechnen.", "Whisker = extremster Datenwert <b>innerhalb</b> der Grenzen.", "Werte außerhalb = Ausreißer (einzelne Punkte)."],
    bsp=r"\(x_{0.25}=3,\ x_{0.75}=6\), IQR = 3: Grenzen \(-1.5\) und \(10.5\) → 25 ist Ausreißer; oberer Whisker endet bei 8, unterer bei 2.",
    fa="Whisker nicht bis zur Grenze (10.5) zeichnen, sondern bis zum letzten echten Wert (8).")

# =====================================================================
D.S("5", "Zwei Merkmale: Kontingenztafel und χ² (V03)",
    "İki kategorik değişken: tabloyu tamamla, koşullu oranları karşılaştır, χ² hesapla.")

D.E("5.1", "Kontingenztafel aus einem Text vervollständigen",
    sig="„Erstellen Sie die vollständige Kontingenztafel (inkl. Randhäufigkeiten)“",
    ne="Önce boş tabloyu çiz (satır/sütun toplamlarıyla), metindeki sayıları yerleştir, kalanları farkla bul.",
    st=["Tafel mit Zeilen-/Spaltensummen und n zeichnen.", "Zahlen aus dem Text eintragen (Prozent „der Frauen“ × Zeilensumme).",
        "Rest per Differenz: Zeile/Spalte muss ihre Summe ergeben.", "Kontrolle: Summe aller Zellen = n."],
    bsp=("200 Studierende, 80 davon Frauen; 20 Frauen und 40 Männer rauchen:"
         "<table class='t c' style='width:auto'><tr><th></th><th>raucht</th><th>raucht nicht</th><th>Σ</th></tr>"
         "<tr><th>Frau</th><td>20</td><td>60</td><td>80</td></tr><tr><th>Mann</th><td>40</td><td>80</td><td>120</td></tr>"
         "<tr><th>Σ</th><td>60</td><td>140</td><td>200</td></tr></table>"))

D.E("5.2", "Bedingte Häufigkeiten und Unabhängigkeit",
    sig="„Anteil der Raucher unter den Frauen“, „Deutet das auf einen Zusammenhang hin?“",
    ne="„… arasında / … içinde“ diyen grup paydaya gelir. Koşullu oranlar farklıysa → ilişki var (bağımlı).",
    fm=r"\[f(b_k\mid a_j)=\frac{h_{jk}}{h_{j\bullet}}\qquad\text{unabhängig}\iff f(b_k\mid a_j)=f(b_k)=\frac{h_{\bullet k}}{n}\ \text{für alle }j,k\]",
    bsp=r"Raucher unter Frauen \(\frac{20}{80}=0.25\), unter Männern \(\frac{40}{120}=0.333\) → unterschiedlich → Hinweis auf einen Zusammenhang.",
    fa="„Anteil der Frauen unter den Rauchern“ (20/60) ≠ „Anteil der Raucher unter den Frauen“ (20/80).",
    ks="„Da sich die bedingten Anteile unterscheiden (0.25 vs. 0.333), deutet dies auf einen Zusammenhang zwischen Geschlecht und Rauchen hin.“")

D.E("5.3", "Erwartete Häufigkeiten und χ²-Koeffizient",
    sig="„bei Unabhängigkeit erwartete Häufigkeiten“, „χ²-Koeffizient“",
    ne="Beklenen = satır toplamı × sütun toplamı / n. χ² = her hücre için (gözlenen − beklenen)² / beklenen, hepsini topla.",
    fm=r"\[\tilde h_{jk}=\frac{h_{j\bullet}\,h_{\bullet k}}{n}\qquad\chi^2=\sum_j\sum_k\frac{(h_{jk}-\tilde h_{jk})^2}{\tilde h_{jk}}\]",
    st=["Erwartete Tafel berechnen (nicht runden, Randsummen bleiben gleich).", "Differenzen beobachtet − erwartet (je Zeile/Spalte Summe 0).", "Quadrat durch <b>erwartet</b> teilen, alle Zellen addieren."],
    bsp=r"Tafel aus 5.1: \(\tilde h=24;\ 56;\ 36;\ 84\) → \(\chi^2=\frac{16}{24}+\frac{16}{56}+\frac{16}{36}+\frac{16}{84}=1.587\)",
    fa="Durch den erwarteten Wert teilen, nicht durch den beobachteten. χ² ist nie negativ; = 0 bei perfekter Unabhängigkeit. Als Test: 13.11.")

# =====================================================================
D.S("6", "Kovarianz, Korrelation, Kausalität (V03)", "İki sayısal değişken arasındaki doğrusal ilişki.")

D.E("6.1", "Empirische Kovarianz",
    sig="„Berechnen Sie die empirische Kovarianz \\(s_{xy}\\)“",
    ne="Çarpımların ortalaması eksi ortalamaların çarpımı. Sadece <b>işaret</b> yorumlanır (birimlere bağlı).",
    fm=r"\[s_{xy}=\frac1n\sum(x_i-\bar x)(y_i-\bar y)=\frac1n\sum x_iy_i-\bar x\,\bar y\]",
    bsp=r"x = 1, 2, 3, 4, 5; y = 2, 4, 5, 4, 5: \(\bar x=3,\ \bar y=4,\ \sum x_iy_i=66\) → \(s_{xy}=13.2-12=1.2\)",
    fa="R (cov) teilt durch n − 1. In Teil A: empirisch = 1/n, passend zu \\(s_x^2\\) mit 1/n.",
    ks="„Die positive Kovarianz deutet auf einen positiven linearen Zusammenhang hin; ihre Höhe ist nicht interpretierbar, da sie von den Maßeinheiten abhängt.“")

D.E("6.2", "Korrelationskoeffizient nach Bravais-Pearson",
    sig="„Ermitteln Sie \\(r_{xy}\\) bzw. \\(\\rho_{xy}\\) und interpretieren Sie“",
    ne="r = kovaryans / (sx·sy), −1 ile 1 arası. Yorum: <b>güç + yön + doğrusal + değişkenler</b>.",
    fm=r"\[r_{xy}=\frac{s_{xy}}{s_x\,s_y}=\frac{\sum x_iy_i-n\bar x\bar y}{\sqrt{\left(\sum x_i^2-n\bar x^2\right)\left(\sum y_i^2-n\bar y^2\right)}}\in[-1,1]\]",
    extra="<table class='t c' style='width:auto'><tr><th>|r|</th><td>&lt; 0.3</td><td>0.3 bis &lt; 0.7</td><td>≥ 0.7</td></tr><tr><th>Stärke</th><td>schwach</td><td>mittel</td><td>stark</td></tr></table>",
    st=["\\(s_x^2,\\ s_y^2,\\ s_{xy}\\) mit demselben Nenner (1/n).", "\\(r=s_{xy}/\\sqrt{s_x^2s_y^2}\\).", "Interpretation als Satz. Gegebene gerundete Werte benutzen, wenn die Aufgabe sie vorgibt."],
    bsp=r"Fortsetzung 6.1: \(s_x^2=11-9=2\), \(s_y^2=17.2-16=1.2\) → \(r=\frac{1.2}{\sqrt{2\cdot1.2}}=0.775\)",
    fa="r misst nur <b>lineare</b> Zusammenhänge. r = 0 heißt nicht „unabhängig“ (z. B. \\(y=x^2\\)).",
    ks="„r = 0.775: starker positiver linearer Zusammenhang zwischen X und Y.“")

D.E("6.3", "Rangkorrelation nach Spearman",
    sig="„Rangkorrelationskoeffizient“, ordinale Merkmale, „monotoner Zusammenhang“",
    ne="Değerler yerine sıralarını (rank) kullan. En küçük = 1. Eşitlikte ortalama sıra.",
    fm=r"\[r_{Sp}=r\big(rk(x),\,rk(y)\big)\qquad\text{ohne Bindungen: }r_{Sp}=1-\frac{6\sum d_i^2}{n(n^2-1)},\quad d_i=rk(x_i)-rk(y_i)\]",
    bsp=r"Ränge x: 1, 2, 3, 4, 5; Ränge y: 2, 1, 4, 3, 5 → \(d=-1,1,-1,1,0\), \(\sum d^2=4\) → \(r_{Sp}=1-\frac{24}{120}=0.8\)",
    fa="Kurzformel nur ohne Bindungen; mit Bindungen Pearson auf die (Durchschnitts-)Ränge anwenden.")

D.E("6.4", "Transformationen: was ändert sich?",
    sig="„Die Temperatur wird in °F angegeben“, „cm statt m“",
    ne="Birim değişince kovaryans değişir, korelasyon değişmez (b·d < 0 ise sadece işareti döner).",
    fm=r"\[u=a+bx,\ v=c+dy:\qquad s_{uv}=b\,d\,s_{xy}\qquad r_{uv}=\operatorname{sign}(bd)\cdot r_{xy}\]",
    bsp=r"°C → °F (\(F=32+1.8C\)): Kovarianz × 1.8, Korrelation bleibt gleich.")

D.E("6.5", "Kausalität, Scheinkorrelation, ökologischer Fehlschluss",
    sig="„Der Trainer behauptet, … führt zu …“, „Stimmen Sie zu? Begründen Sie“",
    ne="Korelasyon nedensellik değildir. Üçüncü değişken veya tesadüf olabilir. Nedensellik için deney + kontrol gerekir.",
    st=["<b>Kausal</b> nachweisbar nur mit gezielter Manipulation von X und Kontrolle aller anderen Einflüsse (Randomisierung).",
        "<b>Scheinkorrelation</b>: Zusammenhang durch eine <b>Drittvariable</b> oder reinen Zufall.",
        "<b>Ökologischer Fehlschluss</b>: von Gruppendaten (Städte, Länder) auf Individuen schließen."],
    ks="„Nein. Ein hoher Korrelationskoeffizient zeigt nur einen statistischen (linearen) Zusammenhang, keine Kausalität. Er könnte z. B. durch eine Drittvariable entstehen; für einen Kausalnachweis wäre ein kontrolliertes Experiment nötig.“")
