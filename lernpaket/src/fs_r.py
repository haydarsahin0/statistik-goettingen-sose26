"""Formelsammlung R (Teil B): alle Befehle nach Aufgabentyp, mit echtem R-Output."""
from fscommon import Doc

D = Doc(
    key="r", cls="fs-r",
    title="Formelsammlung R",
    sub="Teil B · alle R-Befehle nach Aufgabentyp · mit echtem Output",
    chip="SoSe 26 · Göttingen · Teil B",
    intro=("<p>Alle R-Befehle aus Vorlesungsskripten, Tutorien, Testaten und Probeklausur B – sortiert nach <b>Aufgabentyp</b>. "
           "Jeder Code-Kasten wurde wirklich in R ausgeführt: weiße Zeilen = was du eintippst, hellblaue Zeilen = was R antwortet. "
           "Die Beispiele benutzen den Übungsdatensatz <code>Taverne.csv</code> (Ordner <i>uebungsdaten</i>) – du kannst alles selbst nachtippen.</p>"
           "<p>Rezept-Aufbau: <b>Erkennen</b> (Wortlaut in der Aufgabe) → <b>TR</b> (kısa Türkçe açıklama) → <b>Schritte</b> → <b>R-Code mit Output</b> → <b>⚠ Falle</b> → <b>✎ Antwortsatz</b> für ILIAS.</p>"),
    howto=("<b class='t'>Nasıl kullanılır?</b><ol>"
           "<li>Soruyu oku → <b>{FINDER}</b>'da sorudaki ifadeyi bul → numaraya git.</li>"
           "<li>Kodu kopyala, sadece <b>veri adını</b> (d$…) ve <b>sayıları</b> kendi sorununkilerle değiştir.</li>"
           "<li>Çıktıyı ILIAS'a kodla birlikte yapıştır, sonucu <code>round(…, 3)</code> ile yuvarla ve <b>✎ Antwortsatz</b> kalıbıyla tam cümle yaz.</li>"
           "<li>Hata mesajı alırsan → Bölüm 13 (Fehlermeldungen).</li></ol>"),
    foot="Formelsammlung R · Teil B · SoSe 26",
    outname="Formelsammlung_R.pdf")


def R(no, title, sig="", ne="", r="", st=None, fa="", ks="", run=True, setup="", img=None, err_ok=False, extra="", long=False):
    D.E(no, title, sig=sig, ne=ne, st=st, fa=fa, ks=ks, r=r, run=run, setup=setup, img=img, err_ok=err_ok, extra=extra, long=long)


# =====================================================================
D.S("0", "Klausurablauf und Antwortform (ILIAS)",
    "Teil B'de puanın yarısı biçimden gelir: kod + çıktı + yuvarlanmış sonuç + tam cümle.")

D.E("0.1", "Ablauf in 60 Minuten",
    sig="Hinweisblatt Teil B, Abschlusssitzung",
    ne="45 puan / 60 dakika → 1 puan ≈ 1.3 dakika. Her alt soruyu bitirince hemen ILIAS'a yapıştır ve scripti kaydet.",
    st=["Neues R-Skript öffnen, sofort im Ordner <i>Dokumente</i> speichern (z. B. <code>Klausur.R</code>).",
        "Erste Zeile: <code>setwd(path.expand(\"~\"))</code> – genau so, wie es in der Aufgabe steht.",
        "Datei kurz ansehen (Trennzeichen? Dezimalzeichen? Kopfzeile?) → einlesen (2.1) → <code>head(d)</code> und <code>str(d)</code> zur Kontrolle.",
        "Pro Teilaufgabe: Code schreiben, mit Strg+Enter ausführen, Code <b>und</b> Output in die ILIAS-Box kopieren, Antwortsatz in die zweite Box.",
        "Grafiken: <code>pdf(\"Name.pdf\")</code> … <code>dev.off()</code>, Datei im Ordner prüfen und hochladen.",
        "Folgefehler zählen: Wenn ein Teil nicht klappt, das benötigte Objekt anders erzeugen und weitermachen."],
    fa="Fehlerhaften Code, der nicht Teil der Antwort ist, aus der ILIAS-Box löschen – widersprüchliche Mehrfachlösungen kosten Punkte.")

D.E("0.2", "Antwortform: Code, Output, Antwortsatz",
    sig="„Nutzen Sie für Ihre Antwort die Kästchen zu den Fragen 5 und 6 in ILIAS“",
    ne="Kutu 1: R kodu + R çıktısı. Kutu 2: kodsuz, tam Almanca cümle, sayılar 3 ondalık (R ile yuvarlanmış).",
    st=["Numerische Ergebnisse auf <b>3 Nachkommastellen</b> mit einem R-Befehl runden: <code>round(x, 3)</code>.",
        "Nicht-numerische Antworten in <b>vollen Sätzen</b>.",
        "Grafiktitel über <code>main</code>: Aufgabenteil, Matrikelnummer, Sitzplatznummer; Achsen wie verlangt beschriften.",
        "Dezimalpunkt benutzen (2.762, nicht 2,762)."],
    ks="„Das arithmetische Mittel der Variable Muenzen beträgt 22.083.“ · „Der unverzerrte Schätzer für die Standardabweichung beträgt 7.292.“")

R("0.3", "RStudio-Grundlagen",
  sig="Skript, Konsole, Kommentare, Hilfe",
  ne="Kodu scripte yaz, Strg+Enter ile satırı çalıştır. # sonrası yorumdur. ?komut yardım açar. R büyük/küçük harfe duyarlıdır.",
  r='''x <- 5          # Zuweisung: x bekommt den Wert 5
x * 2           # Ergebnis wird angezeigt, x bleibt 5
x''',
  st=["<code>&lt;-</code> speichert (auch <code>=</code> geht). Ohne Zuweisung wird nur angezeigt. <code>X</code> (groß) wäre ein anderes, nicht existierendes Objekt → Fehler „object 'X' not found“.",
      "Hilfe: <code>?mean</code> oder <code>help(mean)</code>. Objekte anzeigen: <code>ls()</code>; löschen: <code>rm(x)</code>.",
      "Strg+Enter = Zeile/Markierung ausführen · Strg+S = speichern · Pfeil hoch in der Konsole = letzter Befehl."])

# =====================================================================
D.S("1", "Grundlagen: Objekte, Vektoren, Datentypen",
    "Testat 0 ve her sınavın ilk soruları. Vektör = aynı türden değerler dizisi.")

R("1.1", "Rechnen und mathematische Funktionen",
  sig="„Berechnen Sie mit R …“, Taschenrechner-Ersatz",
  ne="R hesap makinesi gibi çalışır. log = doğal logaritma (ln)!",
  r='''2^3; sqrt(16); exp(1); log(10); log10(100); log(8, base = 2)
abs(-3); factorial(5); choose(5, 2); round(3.14159, 3); 7 %/% 2; 7 %% 2''',
  fa="<code>log()</code> ist der natürliche Logarithmus (ln). Für log₁₀: <code>log10()</code>.")

R("1.2", "Vektoren erstellen",
  sig="„Erstellen Sie einen Vektor …“, „die Zahlen von 1 bis 20“",
  ne="c() elle, : ardışık tam sayılar, seq() adımlı dizi, rep() tekrar.",
  r='''x <- c(3, 1, 4, 1, 5)
1:6
seq(0, 1, by = 0.25)
seq(2, 20, length.out = 4)
rep(c("a", "b"), times = 2); rep(0, 3)
length(x)''')

R("1.3", "Rechnen mit Vektoren",
  sig="„Multiplizieren Sie jeden Wert mit …“, Summe, Produkt, kumulierte Summe",
  ne="İşlemler her elemana tek tek uygulanır (vektörize). Döngüye gerek yok.",
  r='''x * 2; x + 10; x^2
sum(x); prod(x); cumsum(x); sort(x); sort(x, decreasing = TRUE); rev(x)
x - mean(x)''')

R("1.4", "Elemente auswählen (Indizierung)",
  sig="„das dritte Element“, „alle Werte größer als …“, „Position des Maximums“",
  ne="Köşeli parantez: x[konum] veya x[koşul]. Eksi işareti = o elemanı çıkar.",
  r='''x[3]; x[c(1, 5)]; x[-1]; x[length(x)]
x[x > 2]
which(x > 2); which.max(x); which(x == max(x))''',
  fa="Indizes beginnen in R bei 1 (nicht bei 0).")

R("1.5", "Vergleiche und logische Werte",
  sig="„Wie viele Werte sind größer als …?“, „Anteil der Werte …“",
  ne="Karşılaştırma TRUE/FALSE verir. sum() → kaç tane; mean() → oran. & = ve, | = veya, ! = değil.",
  r='''x > 2
sum(x > 2); mean(x > 2)
x >= 3 & x <= 4
x == 1 | x == 5
4 %in% x; !(x > 2)''',
  ks="„Der Anteil der Werte größer als 2 beträgt 0.6.“")

R("1.6", "Datentypen bestimmen",
  sig="„Ermitteln Sie die Objekttypen der Variablen …“, „Welcher Datentyp?“",
  ne="typeof() iç türü verir (double/integer/character/logical), class() nesne sınıfını (numeric/factor/data.frame).",
  r='''typeof(3.5); typeof(3L); typeof("Wolf"); typeof(TRUE)
class(3.5); class(factor("Wolf")); class(matrix(1:4, 2))
is.numeric(3.5); as.numeric("2.5"); as.character(12); as.integer(3.9)''',
  st=["<b>double</b> = Kommazahl (numeric) · <b>integer</b> = ganze Zahl (numeric) · <b>character</b> = Text · <b>logical</b> = TRUE/FALSE.",
      "<code>typeof()</code> und <code>class()</code> sind beide als „passender Befehl“ akzeptiert; <code>str(d)</code> zeigt alle Spalten auf einmal."],
  fa="Zahlen mit Anführungszeichen (\"2.5\") sind Text – Rechnen geht erst nach <code>as.numeric()</code>.")

R("1.7", "Faktoren (kategoriale Variablen)",
  sig="„Wandeln Sie … in einen Faktor um“, „Ausprägungen / Levels“",
  ne="Faktör = kategorik değişken; levels = olası kategoriler. Sıra levels ile belirlenir.",
  r='''f <- factor(c("mittel", "gut", "gut", "schlecht"), levels = c("schlecht", "mittel", "gut"))
f; levels(f); table(f); as.numeric(f)''',
  fa="<code>as.numeric(f)</code> liefert die Level-Nummern, nicht die Beschriftung.")

R("1.8", "Fehlende Werte (NA)",
  sig="„fehlende Werte“, Ergebnis ist NA",
  ne="NA varsa mean/sd/sum NA döner → na.rm = TRUE ekle veya na.omit() ile temizle.",
  r='''y <- c(4, NA, 6, 8)
mean(y); mean(y, na.rm = TRUE)
is.na(y); sum(is.na(y)); na.omit(y)''')

R("1.9", "Mengen in R (Testat 0)",
  sig="„Vereinigung“, „Schnittmenge“, „Differenz“, „ist Element von“",
  ne="Küme işlemleri: union (∪), intersect (∩), setdiff (A ohne B).",
  r='''A <- c(1, 2, 5, 8); B <- c(2, 3, 5, 7)
union(A, B); intersect(A, B); setdiff(A, B)
is.element(3, A); length(intersect(A, B))''')

R("1.10", "Text zusammenfügen und ausgeben",
  sig="paste, cat, „geben Sie … aus“",
  ne="paste() boşlukla, paste0() boşluksuz birleştirir. cat() düz metin yazdırır.",
  r='''paste("Sitz", 17, "Matr.Nr.", 12345678)
paste0("T", 1:3)
cat("Mittelwert:", round(mean(x), 3), "\\n")''')

R("1.11", "Matrix, Data Frame und Liste von Hand",
  sig="„Erstellen Sie eine Matrix / einen Data Frame“, Kontingenztafel eingeben",
  ne="matrix sütun sütun doldurur (byrow = TRUE → satır satır). data.frame = farklı türde sütunlar.",
  r='''m <- matrix(c(20, 40, 60, 80), nrow = 2)
m; dim(m); t(m)
df <- data.frame(Name = c("A", "B", "C"), Punkte = c(12, 15, 9))
df; df$Punkte; nrow(df)
l <- list(zahl = 1, text = "a"); l$text''',
  fa="<code>matrix(c(20, 40, 60, 80), nrow = 2)</code> füllt <b>spaltenweise</b>: erste Spalte 20, 40.")

# =====================================================================
R("1.12", "Runden und Zahlen formatieren",
  sig="„auf drei Nachkommastellen runden“, „in der Form X × 10^Y“",
  ne="Sınavda her sayı R komutu ile yuvarlanmalı: round(x, 3). Çok küçük sayılar için signif/format.",
  r='''round(22.08333, 3)
signif(0.000006938384, 4)
format(6.938384e-131, scientific = TRUE, digits = 4)
sprintf("%.3f", 7.29231)''',
  st=["<code>round(x, 3)</code>: 3 Nachkommastellen – Standard für alle Antworten.",
      "<code>signif(x, 4)</code>: 4 gültige Ziffern – gut für sehr kleine Zahlen.",
      "<code>format(x, scientific = TRUE, digits = 4)</code>: wissenschaftliche Schreibweise → als \\(X\\times10^{Y}\\) abschreiben.",
      "<code>sprintf('%.3f', x)</code>: zeigt auch Nullen am Ende (7.290 statt 7.29)."],
  fa="round() ändert die Darstellung im Output; rechne mit dem ungerundeten Objekt weiter und runde nur das Endergebnis.",
  ks="„Die Likelihood beträgt 6.938 × 10^(−131).“")

D.S("2", "Datensatz einlesen, ansehen, auswählen",
    "Her Teil B sınavının (a)–(c) kısmı: 10 puan. Okuma doğru değilse sonraki her şey yanlış olur.")

R("2.1", "Working Directory setzen und Daten einlesen",
  sig="„Setzen Sie mittels setwd(path.expand(\"~\")) Ihr Working Directory“, „Speichern Sie die Daten als Data-Frame-Objekt d“",
  ne="Önce dosyayı bir metin editöründe gör: ayraç (, veya ;), ondalık (. veya ,), ilk satır başlık mı? Buna göre sep, dec, header.",
  r='''setwd(path.expand("~"))     # in der Klausur genau so
getwd()                     # Kontrolle des Ordners
d <- read.csv("Taverne.csv", sep = ";", dec = ".", header = TRUE)
# Alternative: d <- read.table("Taverne.csv", sep = ";", dec = ".", header = TRUE)
head(d)''', run=False,
  st=["Datei ansehen: erste Zeile = Spaltennamen → <code>header = TRUE</code>.",
      "Trennzeichen zwischen den Spalten: Komma → <code>sep = \",\"</code>; Semikolon → <code>sep = \";\"</code>; Tab → <code>sep = \"\\t\"</code>.",
      "Dezimalzeichen in den Zahlen: Punkt → <code>dec = \".\"</code>; Komma → <code>dec = \",\"</code> (dann ist sep meist \";\").",
      "Einlesen, dann <b>sofort</b> <code>head(d)</code> und <code>str(d)</code> zur Kontrolle (2.2)."],
  fa="Dateiname exakt mit Groß-/Kleinschreibung und Endung .csv. Datei muss im Working Directory liegen.")

R("2.2", "Einlesen prüfen: Ist der Datensatz richtig?",
  sig="str() zeigt nur 1 Variable oder Zahlen als chr",
  ne="Tek değişken görünüyorsa sep yanlış. Sayılar chr (metin) görünüyorsa dec yanlış.",
  r='''falsch <- read.csv("Taverne.csv")          # sep vergessen
str(falsch)
d <- read.csv("Taverne.csv", sep = ";", dec = ".", header = TRUE)
str(d)''',
  st=["<b>1 variable</b> mit allen Spalten in einem Text → <code>sep</code> falsch.",
      "Zahlenspalte als <code>chr</code> mit Kommas (\"12,5\") → <code>dec = \",\"</code> fehlt.",
      "Erste Datenzeile als Spaltenname → <code>header</code> falsch."])

R("2.3", "Datensatz ansehen",
  sig="„Geben Sie die ersten 6 Zeilen wieder“, „Wie viele Beobachtungen?“",
  ne="head → ilk 6 satır, dim → satır × sütun, names → sütun adları, summary → özet.",
  r='''head(d)
dim(d); nrow(d); ncol(d)
names(d)
summary(d$Muenzen)''',
  ks="„Der Datensatz enthält 12 Beobachtungen und 5 Variablen.“")

R("2.4", "Spalten und Zeilen auswählen",
  sig="„die Variable …“, „nur die Beobachtungen aus …“, „die dritte Zeile“",
  ne="d$Sütun veya d[satır, sütun]. Boş bırakılan taraf = hepsi.",
  r='''d$Muenzen
d[3, ]
d[1:2, c("Tal", "Muenzen")]
d[d$Tal == "Bergtal", ]
d$Muenzen[d$Monster == "Troll"]''',
  fa="Vergleich mit <code>==</code> (zwei Gleichheitszeichen). Text in Anführungszeichen, genaue Schreibweise.")

R("2.5", "Teildatensatz mit subset",
  sig="„Betrachten Sie nur Kämpfe mit mindestens 5 und weniger als 60 Minuten“",
  ne="subset(veri, koşul) koşula uyan satırları seçer; sütun adları doğrudan yazılır.",
  r='''kurz <- subset(d, Kampfzeit >= 5 & Kampfzeit < 60)
nrow(kurz)
mean(kurz$Muenzen)
subset(d, Tal == "Waldtal", select = c(Monster, Muenzen))''')

R("2.6", "Neue Variable hinzufügen",
  sig="„Ergänzen Sie den Data Frame um eine Spalte …“",
  ne="d$yeni <- hesap. ifelse ile koşullu değişken.",
  r='''d$Muenzen.pro.Min <- round(d$Muenzen / d$Kampfzeit, 3)
d$lang <- ifelse(d$Kampfzeit > 30, "lang", "kurz")
head(d, 3)''')

R("2.7", "Objekttypen der Variablen ermitteln (Probeklausur-Typ)",
  sig="„Ermitteln Sie unter Einbezug eines passenden R-Befehls die Objekttypen der Variablen Tal und Muenzen“",
  ne="typeof (veya class/str) ile her değişkenin türü; cevabı tam cümleyle yaz.",
  r='''typeof(d$Tal)
typeof(d$Muenzen)
typeof(d$Kampfzeit)''',
  ks="„Die Variable Tal ist ein character-Objekt; die Variable Muenzen ist numerisch vom Typ integer (nur ganze Zahlen); Kampfzeit ist numerisch vom Typ double.“")

# =====================================================================
R("2.8", "Sortieren, Extremwerte und eindeutige Werte",
  sig="„Welche Taverne …am meisten?“, „die drei größten …“, „Wie viele verschiedene …?“",
  ne="order ile sırala, which.max ile en büyüğün satırını bul, unique ile farklı değerleri say.",
  r='''d[order(d$Muenzen, decreasing = TRUE), ][1:3, ]
d[which.max(d$Muenzen), ]
unique(d$Tal)
length(unique(d$Monster))
sum(d$Muenzen > 20)
mean(d$Muenzen > 20)''',
  st=["<code>order()</code> liefert die Reihenfolge der Zeilen; <code>decreasing = TRUE</code> für absteigend.",
      "<code>which.max()</code>/<code>which.min()</code> geben die <b>Zeilennummer</b> des Extremwerts.",
      "<code>sum(Bedingung)</code> = Anzahl, <code>mean(Bedingung)</code> = Anteil (TRUE zählt als 1)."],
  ks="„Die meisten Münzen (33) erhielt der Barde in Taverne T08 im Bergtal.“")

R("2.9", "Data Frame selbst erstellen und speichern",
  sig="„Erstellen Sie einen Data Frame mit …“, „speichern Sie … als CSV“",
  ne="Vektörlerden data.frame kur; write.csv ile kaydet.",
  r='''neu <- data.frame(x = c(1, 2, 3), Gruppe = c("A", "B", "A"))
neu
write.csv(neu, "neu.csv", row.names = FALSE)
read.csv("neu.csv")''',
  fa="Ohne <code>row.names = FALSE</code> schreibt R eine zusätzliche Spalte mit Zeilennummern.")

D.S("3", "Kennzahlen und Tabellen",
    "Ortalama, standart sapma, kantil, sıklık tablosu, grup bazlı hesap, kontenjans tablosu, korelasyon.")

R("3.1", "Mittelwert und Standardabweichung",
  sig="„Berechnen und nennen Sie das arithmetische Mittel und den unverzerrten Schätzer für die Standardabweichung“",
  ne="mean ve sd; sd zaten yansız tahminci (n−1). Her zaman round(…, 3).",
  r='''round(mean(d$Muenzen), 3)
round(sd(d$Muenzen), 3)
round(sqrt(var(d$Muenzen)), 3)      # gleich wie sd''',
  ks="„Das arithmetische Mittel der Variable Muenzen beträgt 22.083; der unverzerrte Schätzer für die Standardabweichung beträgt 7.292.“")

R("3.2", "Varianz: unverzerrt und empirisch",
  sig="„unverzerrte Varianz“ vs. „empirische Varianz“",
  ne="var() = n−1 ile (yansız). Ampirik varyans (1/n) için (n−1)/n ile çarp.",
  r='''n <- length(d$Muenzen)
round(var(d$Muenzen), 3)                    # unverzerrt (n - 1)
round(var(d$Muenzen) * (n - 1) / n, 3)      # empirisch (1/n)
round(mean((d$Muenzen - mean(d$Muenzen))^2), 3)   # gleich, per Formel''')

R("3.3", "Median, Quantile, IQR, Spannweite",
  sig="„Median“, „Quartile“, „Interquartilsabstand“, „Wertebereich“",
  ne="quantile() R'nin kendi tanımını kullanır (Teil A'daki ders tanımından farklı olabilir).",
  r='''median(d$Muenzen)
quantile(d$Muenzen, c(0.25, 0.75))
IQR(d$Muenzen)
range(d$Muenzen); max(d$Muenzen) - min(d$Muenzen)
summary(d$Kampfzeit)''',
  fa="In Teil B die R-Werte angeben; in Teil A (per Hand) gilt die Quantil-Definition der Vorlesung.")

R("3.4", "Häufigkeiten und Modus",
  sig="„absolute / relative Häufigkeiten“, „häufigste Ausprägung“",
  ne="table → mutlak, prop.table → oran. Mod: en büyük sıklığın adı.",
  r='''table(d$Monster)
round(prop.table(table(d$Monster)), 3)
names(which.max(table(d$Monster)))
cumsum(table(d$Tal))''')

R("3.5", "Kennzahlen pro Gruppe (tapply, aggregate)",
  sig="„Berechnen Sie den Mittelwert für jedes Tal mit einem einzigen Befehl“",
  ne="tapply(sayı, grup, fonksiyon): her grup için hesap. Sonra en büyük olanı söyle.",
  r='''round(tapply(d$Muenzen, d$Tal, mean), 3)
tapply(d$Kampfzeit, d$Monster, max)
aggregate(Muenzen ~ Tal, data = d, FUN = median)''',
  ks="„Im Bergtal werden im Durchschnitt die meisten Münzen erzielt (26.000).“")

R("3.6", "Klassen bilden mit cut",
  sig="„Klassieren Sie … in die Klassen [0, 10), [10, 60), [60, ∞)“",
  ne="cut(x, breaks, right) → faktör. right = FALSE: [a, b) (sol dahil); right = TRUE: (a, b].",
  r='''d$Kampf.K <- cut(d$Kampfzeit, breaks = c(0, 10, 60, Inf), right = FALSE)
table(d$Kampf.K)
cut(c(10, 20), breaks = c(0, 10, 20), right = TRUE)''',
  fa="„bis unter 10“ / „weniger als“ → <code>right = FALSE</code>; „bis einschließlich“ / „höchstens“ → <code>right = TRUE</code>.")

R("3.7", "Kontingenztafel, Randsummen, bedingte Anteile",
  sig="„Erstellen Sie eine Kontingenztafel“, „mit Randhäufigkeiten“, „Anteil … unter den …“",
  ne="table(x, y) çapraz tablo; addmargins toplamları ekler; prop.table(t, 1) satır içi oranlar, 2 sütun içi.",
  r='''tafel <- table(d$Tal, d$Monster)
tafel
addmargins(tafel)
round(prop.table(tafel, 1), 3)     # 1 = zeilenweise (je Tal)''',
  fa="<code>prop.table(tafel)</code> ohne Zahl = Anteil an allen n; mit 1 zeilenweise, mit 2 spaltenweise.")

R("3.8", "Korrelation und Kovarianz",
  sig="„Wie stark ist der lineare Zusammenhang?“, „Spearman“",
  ne="cor → Pearson (varsayılan), method = \"spearman\" → sıra korelasyonu. cov n−1 ile böler.",
  r='''round(cor(d$Muenzen, d$Kampfzeit), 3)
round(cor(d$Muenzen, d$Kampfzeit, method = "spearman"), 3)
round(cov(d$Muenzen, d$Kampfzeit), 3)''',
  ks="„Der Korrelationskoeffizient nach Bravais-Pearson beträgt 0.928; es liegt ein starker positiver linearer Zusammenhang zwischen Kampfzeit und Münzen vor.“")

# =====================================================================
R("3.9", "Empirische Verteilungsfunktion als Zahl, Quantil nach Vorlesung",
  sig="„Anteil der Beobachtungen mit höchstens …“, „F̂(20)“, „Quantil gemäß Vorlesungsdefinition“",
  ne="ecdf(x) bir fonksiyon döndürür: Fn(20) = ≤ 20 olanların oranı. Ders tanımındaki kantil için type = 2.",
  r='''Fn <- ecdf(d$Muenzen)
Fn(20)
1 - Fn(20)
quantile(d$Muenzen, c(0.25, 0.5, 0.75), type = 2)
quantile(d$Muenzen, c(0.25, 0.5, 0.75))''',
  st=["<code>Fn(a)</code> = Anteil ≤ a; <code>1 - Fn(a)</code> = Anteil > a.",
      "<code>type = 2</code> entspricht der Definition aus V02 (aufrunden bzw. Mittelwert bei ganzzahligem nα); der R-Standard ist <code>type = 7</code>.",
      "Steht in der Aufgabe „mit den Standardeinstellungen von R“, <b>kein</b> type angeben."])

R("3.10", "Standardisieren (z-Werte)",
  sig="„Standardisieren Sie die Variable …“",
  ne="z = (x − ortalama) / sd → ortalama 0, sd 1.",
  r='''z <- (d$Muenzen - mean(d$Muenzen)) / sd(d$Muenzen)
round(head(z), 3)
round(c(mean(z), sd(z)), 3)''')

D.S("4", "Grafiken erstellen und speichern",
    "Grafik sorusu genelde 7–8 puan: doğru komut + breaks/right/freq + başlık + eksen adları + PDF olarak kaydetme.")

R("4.1", "Grafik als PDF speichern (Pflicht in der Klausur)",
  sig="„Speichern Sie Ihre Grafik als .pdf-Datei unter Histogramm.pdf … und laden Sie diese Datei hoch“",
  ne="pdf(\"ad.pdf\") → grafik komutları → dev.off(). Dosya çalışma klasörüne yazılır.",
  r='''pdf("Histogramm.pdf")
hist(d$Muenzen, freq = FALSE, main = "Sitz 17, Matr.Nr. 12345678, Aufgabenteil e)",
     xlab = "Muenzen", ylab = "Dichte")
dev.off()''',
  st=["<code>pdf(\"Name.pdf\")</code> öffnet die Datei, alle folgenden Grafikbefehle landen darin.",
      "<code>dev.off()</code> schließt und speichert – ohne dev.off() ist die Datei leer/kaputt.",
      "PNG: <code>png(\"Name.png\", width = 2000, height = 2000, res = 400)</code> … <code>dev.off()</code>.",
      "Titel <code>main</code>: Sitzplatz, Matrikelnummer, Aufgabenteil. Achsen: <code>xlab</code>, <code>ylab</code> genau wie verlangt."])

R("4.2", "Histogramm mit vorgegebenen Klassen",
  sig="„Intervallgrenzen [5, 15), [15, 20), …“, „Dichte auf der y-Achse“",
  ne="breaks = sınıf sınırları, right = FALSE → [a, b), freq = FALSE → yoğunluk (normlu histogram).",
  r='''h <- hist(d$Muenzen, breaks = c(5, 15, 20, 25, 35), right = FALSE, freq = FALSE,
          main = "Sitz 17, Matr.Nr. 12345678, Aufgabenteil e)",
          xlab = "Muenzen", ylab = "Dichte")
h$counts; round(h$density, 4)
hist(d$Muenzen, breaks = c(5, 15, 20, 25, 35), right = FALSE, plot = FALSE)$counts''',
  img=["fsr_hist.png", "fsr_box.png"],
  fa="Ohne <code>freq = FALSE</code> (bzw. <code>prob = TRUE</code>) zeigt R absolute Häufigkeiten. Standard ist <code>right = TRUE</code> = (a, b].")

R("4.3", "Boxplot (auch nach Gruppen)",
  sig="„Erstellen Sie einen Boxplot … getrennt nach …“",
  ne="boxplot(x) tek değişken; boxplot(sayı ~ grup, data = d) gruplara göre (resim yukarıda sağda).",
  r='''boxplot(Muenzen ~ Tal, data = d, main = "Aufgabenteil f)", xlab = "Tal", ylab = "Muenzen")
boxplot(d$Muenzen, plot = FALSE)$stats      # Whisker unten, Q1, Median, Q3, Whisker oben''')

R("4.4", "Streudiagramm mit Regressionsgerade",
  sig="„Stellen Sie den Zusammenhang grafisch dar“, „Fügen Sie die Regressionsgerade hinzu“",
  ne="plot(x, y) dağılım grafiği; abline(lm(y ~ x)) doğruyu ekler. pch nokta şekli.",
  r='''plot(d$Kampfzeit, d$Muenzen, pch = 16, main = "Aufgabenteil g)",
     xlab = "Kampfzeit in Minuten", ylab = "Muenzen")
abline(lm(Muenzen ~ Kampfzeit, data = d), col = "red")
points(50, 30, col = "blue", pch = 4); lines(c(0, 90), c(20, 20), lty = 2)''',
  img=["fsr_scatter.png", "fsr_kde.png"])

R("4.5", "Kerndichteschätzer (KDE)",
  sig="„Visualisieren Sie einen Kerndichteschätzer“, „Bandbreite“, „Epanechnikov-Kern“",
  ne="density(x) KDE hesaplar, plot ile çiz. bw = bant genişliği, kernel = çekirdek. Histogram üstüne lines() ile (resim yukarıda sağda).",
  r='''kde <- density(d$Kampfzeit)
round(kde$bw, 3)
plot(density(d$Kampfzeit, bw = 10, kernel = "epanechnikov"), main = "Aufgabenteil c)",
     xlab = "Kampfzeit", ylab = "Dichte")
hist(d$Kampfzeit, freq = FALSE); lines(density(d$Kampfzeit))''',
  fa="Kleine Bandbreite → zackig, große → zu glatt. Standard-Kern ist \"gaussian\".")

R("4.6", "Säulendiagramm, empirische Verteilungsfunktion, mehrere Grafiken",
  sig="„Säulendiagramm der Häufigkeiten“, „empirische Verteilungsfunktion“, „nebeneinander“",
  ne="barplot(table(x)) kategoriler için; plot(ecdf(x)) ampirik dağılım fonksiyonu; par(mfrow = c(1, 2)) yan yana.",
  r='''par(mfrow = c(1, 2))
barplot(table(d$Monster), main = "Monster", ylab = "Anzahl")
plot(ecdf(d$Muenzen), main = "ecdf", xlab = "Muenzen", ylab = "F(x)")
par(mfrow = c(1, 1))
F <- ecdf(d$Muenzen); F(20)''')

R("4.7", "Wahrscheinlichkeitsfunktion und Dichte zeichnen",
  sig="„Zeichnen Sie die Wahrscheinlichkeitsfunktion / Dichte von …“",
  ne="Kesikli: plot(değerler, dbinom(...), type = \"h\"). Sürekli: curve(dnorm(x, ...), from, to).",
  r='''plot(0:10, dbinom(0:10, size = 10, prob = 0.3), type = "h", lwd = 3,
     xlab = "x", ylab = "P(X = x)", main = "B(10; 0.3)")
curve(dnorm(x, mean = 100, sd = 15), from = 40, to = 160, ylab = "Dichte")
curve(dexp(x, rate = 0.25), from = 0, to = 20, add = FALSE)''')

# =====================================================================
R("4.8", "Grafik-Feinschliff: Achsen, Farben, Linien, Legende",
  sig="„Zeichnen Sie zusätzlich …ein“, „in derselben Grafik“, „mit Legende“",
  ne="xlim/ylim eksen aralığı; lines/curve/abline var olan grafiğe ekler; legend açıklama kutusu.",
  r='''pdf("Feinschliff.pdf")
hist(d$Muenzen, freq = FALSE, xlim = c(0, 40), ylim = c(0, 0.08), col = "lightblue",
     main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil f)", xlab = "Muenzen", ylab = "Dichte")
lines(density(d$Muenzen), col = "red", lwd = 2)
curve(dnorm(x, mean(d$Muenzen), sd(d$Muenzen)), add = TRUE, col = "blue", lty = 2)
abline(v = mean(d$Muenzen), col = "darkgreen")
legend("topright", legend = c("KDE", "Normal", "Mittelwert"),
       col = c("red", "blue", "darkgreen"), lty = c(1, 2, 1))
dev.off()''',
  st=["<code>lines()</code>, <code>points()</code>, <code>abline()</code>, <code>curve(…, add = TRUE)</code> zeichnen <b>in</b> die bestehende Grafik.",
      "<code>abline(h = …)</code> waagerecht, <code>abline(v = …)</code> senkrecht, <code>abline(a, b)</code> Gerade.",
      "<code>lty</code> Linientyp (1 durchgezogen, 2 gestrichelt), <code>lwd</code> Linienbreite, <code>col</code> Farbe."],
  fa="Zusatzlinien vor <code>dev.off()</code> zeichnen, sonst fehlen sie im PDF.")

R("4.9", "QQ-Plot: Normalverteilung prüfen",
  sig="„Prüfen Sie grafisch, ob … normalverteilt ist“",
  ne="Noktalar doğruya yakınsa normal dağılım varsayımı makul.",
  r='''qqnorm(d$Kampfzeit, main = "QQ-Plot Kampfzeit")
qqline(d$Kampfzeit, col = "red")''',
  ks="„Die Punkte weichen deutlich von der Geraden ab; die Normalverteilungsannahme ist für Kampfzeit fraglich.“")

D.S("5", "Verteilungen in R",
    "Dört harf kuralı: d = olasılık/yoğunluk, p = P(X ≤ x), q = kantil, r = rastgele sayı.")

D.E("5.1", "Das d-p-q-r-Prinzip und alle Parameter",
    sig="dbinom, pnorm, qt, rpois …",
    ne="Önek işlevi, ek dağılımı belirler. Parametre adlarına dikkat: normal → sd (varyans değil!), üstel → rate = λ.",
    extra=("<table class='t'><tr><th>Präfix</th><th>liefert</th><th>Beispiel</th></tr>"
           "<tr><td><code>d…</code></td><td>\\(P(X=x)\\) (diskret) bzw. Dichte \\(f(x)\\)</td><td><code>dbinom(2, 10, 0.3)</code></td></tr>"
           "<tr><td><code>p…</code></td><td>\\(P(X\\le x)=F(x)\\)</td><td><code>pnorm(120, 100, 15)</code></td></tr>"
           "<tr><td><code>q…</code></td><td>Quantil: x mit \\(F(x)=p\\)</td><td><code>qnorm(0.975)</code> = 1.96</td></tr>"
           "<tr><td><code>r…</code></td><td>Zufallszahlen</td><td><code>rpois(5, 2)</code></td></tr></table>"
           "<table class='t'><tr><th>Verteilung</th><th>R-Name und Parameter</th><th>Achtung</th></tr>"
           "<tr><td>Binomial \\(B(n,\\pi)\\)</td><td><code>binom(x, size = n, prob = π)</code></td><td>Bernoulli: size = 1</td></tr>"
           "<tr><td>Poisson \\(Po(\\lambda)\\)</td><td><code>pois(x, lambda = λ)</code></td><td></td></tr>"
           "<tr><td>geometrisch \\(p(1-p)^x\\)</td><td><code>geom(x, prob = p)</code></td><td>zählt Misserfolge vor dem 1. Erfolg</td></tr>"
           "<tr><td>hypergeometrisch</td><td><code>hyper(x, m, n, k)</code></td><td>m gesuchte, n andere, k gezogen</td></tr>"
           "<tr><td>Gleich \\(U(a,b)\\)</td><td><code>unif(x, min = a, max = b)</code></td><td></td></tr>"
           "<tr><td>Exponential \\(Exp(\\lambda)\\)</td><td><code>exp(x, rate = λ)</code></td><td>rate = 1 / Mittelwert</td></tr>"
           "<tr><td>Normal \\(N(\\mu,\\sigma^2)\\)</td><td><code>norm(x, mean = μ, sd = σ)</code></td><td><b>sd = Wurzel der Varianz</b></td></tr>"
           "<tr><td>t</td><td><code>t(x, df)</code></td><td>df = n − 1</td></tr>"
           "<tr><td>χ²</td><td><code>chisq(x, df)</code></td><td></td></tr>"
           "<tr><td>Gamma</td><td><code>gamma(x, shape = α, rate = β)</code></td><td></td></tr></table>"))

D.E("5.2", "Wörter in R-Befehle übersetzen",
    sig="„höchstens“, „mindestens“, „mehr als“, „weniger als“, „zwischen“",
    ne="p… her zaman „≤“ demektir. Kesikli dağılımda „<“ ve „≥“ için k−1 kullan; süreklide < ile ≤ aynıdır.",
    extra=("<table class='t'><tr><th>Wortlaut</th><th>diskret (z. B. Binomial)</th><th>stetig (z. B. Normal)</th></tr>"
           "<tr><td>genau k</td><td><code>dbinom(k, n, p)</code></td><td>= 0</td></tr>"
           "<tr><td>höchstens k (≤)</td><td><code>pbinom(k, n, p)</code></td><td><code>pnorm(k, mu, sd)</code></td></tr>"
           "<tr><td>weniger als k (&lt;)</td><td><code>pbinom(k - 1, n, p)</code></td><td><code>pnorm(k, mu, sd)</code></td></tr>"
           "<tr><td>mehr als k (&gt;)</td><td><code>1 - pbinom(k, n, p)</code></td><td><code>1 - pnorm(k, mu, sd)</code></td></tr>"
           "<tr><td>mindestens k (≥)</td><td><code>1 - pbinom(k - 1, n, p)</code></td><td><code>1 - pnorm(k, mu, sd)</code></td></tr>"
           "<tr><td>zwischen a und b (inkl.)</td><td><code>pbinom(b, n, p) - pbinom(a - 1, n, p)</code></td><td><code>pnorm(b, …) - pnorm(a, …)</code></td></tr></table>"),
    fa="Testat 4: \\(P(Y&gt;2)\\) für \\(Y\\sim Po(2)\\) = <code>1 - ppois(2, 2)</code> = <code>1 - dpois(0, 2) - dpois(1, 2) - dpois(2, 2)</code>; <b>nicht</b> <code>1 - ppois(3, 2)</code>.")

R("5.3", "Binomialverteilung",
  sig="„n unabhängige Versuche“, „mit Zurücklegen“",
  ne="dbinom tek değer, pbinom birikimli. size = deneme sayısı, prob = başarı olasılığı.",
  r='''round(dbinom(2, size = 10, prob = 0.3), 3)        # P(X = 2)
round(pbinom(2, size = 10, prob = 0.3), 3)        # P(X <= 2)
round(1 - pbinom(4, size = 10, prob = 0.3), 3)    # P(X >= 5)
round(sum(dbinom(2:4, size = 10, prob = 0.3)), 3) # P(2 <= X <= 4)
qbinom(0.5, size = 10, prob = 0.3)                # Median''')

R("5.4", "Poissonverteilung",
  sig="„im Durchschnitt λ pro …“",
  ne="lambda = ortalama (sorulan zaman aralığına göre!).",
  r='''round(dpois(0, lambda = 2), 3)          # P(X = 0)
round(1 - ppois(2, lambda = 2), 3)      # P(X > 2)
round(ppois(4, lambda = 6), 3)          # 3 Stunden statt 1: lambda = 6''')

R("5.5", "Normalverteilung",
  sig="„\\(X\\sim N(\\mu,\\sigma^2)\\)“, „Quantil“, „zwischen“",
  ne="pnorm(x, mean, sd), qnorm(p, mean, sd). Varyans verilmişse karekökünü al!",
  r='''round(pnorm(120, mean = 100, sd = 15), 3)              # P(X <= 120)
round(1 - pnorm(85, mean = 100, sd = sqrt(225)), 3)    # P(X > 85), Varianz 225
round(pnorm(115, 100, 15) - pnorm(85, 100, 15), 3)     # P(85 < X < 115)
round(qnorm(0.9, mean = 100, sd = 15), 3)              # 90 %-Quantil
round(qnorm(c(0.95, 0.975)), 3)                        # z-Quantile''',
  fa="<code>pnorm(x, 100, 225)</code> wäre falsch – das dritte Argument ist die Standardabweichung.")

R("5.6", "Exponential-, Gleich-, t-, χ²- und Gammaverteilung",
  sig="Wartezeit, „gleichverteilt“, Quantile für KI/Tests",
  ne="Üstel: rate = 1/ortalama. t ve χ² kantilleri güven aralığı ve testler için.",
  r='''round(1 - pexp(6, rate = 1/4), 3)        # Wartezeit > 6, Mittel 4
round(punif(9, min = 4, max = 20), 3)     # P(X <= 9) bei U(4, 20)
round(qt(0.975, df = 15), 3)
round(qchisq(c(0.025, 0.975), df = 9), 3)
round(pgamma(30, shape = 2, rate = 0.1), 3)''')

# =====================================================================
R("5.7", "Kombinatorik, Laplace und Bayes in R",
  sig="„Wie viele Möglichkeiten …?“, „Wahrscheinlichkeit, dass die Augensumme …“, Baumdiagramm nachrechnen",
  ne="choose = binom katsayısı, factorial = faktöriyel. Laplace: tüm sonuçları expand.grid ile listele. Bayes'i değişkenlerle hesapla.",
  r='''choose(5, 2)
factorial(4)
w <- expand.grid(a = 1:6, b = 1:6)
mean(w$a + w$b == 7)
pA <- 0.3; pB_A <- 0.2; pB_nA <- 0.05
pB <- pA * pB_A + (1 - pA) * pB_nA
pB
pA * pB_A / pB''',
  ks="„Die Wahrscheinlichkeit, dass eine erkrankte Person raucht, beträgt 0.632.“")

D.S("6", "Zufallszahlen und Simulation",
    "set.seed ile tekrarlanabilir rastgele sayılar; simülasyonla olasılık ve ortalamanın dağılımı.")

R("6.1", "Zufallszahlen mit set.seed",
  sig="„Simulieren Sie …“, „Nutzen Sie set.seed(123)“",
  ne="set.seed aynı rastgele sayıları tekrar üretir; sınavda verilen seed'i mutlaka kullan.",
  r='''set.seed(123)
x <- rbinom(10000, size = 5, prob = 0.25)    # Testat 4: 20 gelbe von 80 Kugeln
round(mean(x == 2), 3); round(dbinom(2, 5, 0.25), 3)
set.seed(1); round(rnorm(3, mean = 10, sd = 2), 3)
set.seed(1); sample(1:6, 5, replace = TRUE)''',
  fa="set.seed direkt vor dem Zufallsbefehl ausführen, sonst kommen andere Zahlen heraus.")

R("6.2", "Simulation: Verteilung des Mittelwerts (ZGWS)",
  sig="„Simulieren Sie 1 000 Stichproben vom Umfang n und berechnen Sie jeweils den Mittelwert“",
  ne="replicate(tekrar, ifade) her seferinde yeni örneklem çeker; ortalamalar yaklaşık normal dağılır.",
  r='''set.seed(42)
mittel <- replicate(1000, mean(rexp(36, rate = 1/50)))
round(mean(mittel), 3); round(sd(mittel), 3)     # ≈ 50 und 50/sqrt(36) = 8.333
hist(mittel, freq = FALSE)''')

R("6.3", "Ziehen aus einer Urne",
  sig="„mit/ohne Zurücklegen“, „Wahrscheinlichkeiten prob = …“",
  ne="sample(x, size, replace, prob). replace = FALSE → geri koymadan.",
  r='''set.seed(7)
sample(c("rot", "weiss"), 5, replace = TRUE, prob = c(0.4, 0.6))
sample(1:49, 6)                                  # Lotto, ohne Zurücklegen
round(dhyper(2, m = 4, n = 6, k = 3), 3)         # genau 2 rote aus 4 rot / 6 andere''')

# =====================================================================
D.S("7", "Programmieren: Funktionen und Schleifen",
    "Kendi fonksiyonunu yaz, döngü kur, koşul kullan. Likelihood ve „Yennefer“ tipi soruların temeli.")

R("7.1", "Eine Funktion schreiben",
  sig="„Schreiben Sie eine Funktion name(x), die …“",
  ne="isim <- function(argümanlar) { hesap; return(sonuç) }. Sonra isim(değer) ile çağır.",
  r='''var.emp <- function(x) {
  n <- length(x)
  return(sum((x - mean(x))^2) / n)
}
round(var.emp(d$Muenzen), 3)
quadrat <- function(a, b = 2) a^b      # b hat einen Standardwert
quadrat(3); quadrat(3, 3)''')

R("7.2", "for-Schleife",
  sig="„Berechnen Sie … für alle Werte von 1 bis 10“, „mithilfe einer Schleife“",
  ne="for (i in değerler) { ... }. Sonuçları önceden oluşturulan vektöre kaydet.",
  r='''erg <- numeric(5)
for (i in 1:5) {
  erg[i] <- i^2
}
erg
for (k in c(2, 4)) print(k * 10)''',
  fa="Ergebnisvektor vor der Schleife anlegen (<code>numeric(n)</code>), sonst geht der Wert jeder Runde verloren.")

R("7.3", "if / else und ifelse",
  sig="„Falls … , dann …, sonst …“",
  ne="if tek değer için, ifelse vektörün her elemanı için.",
  r='''z <- 7
if (z > 5) {
  print("groß")
} else {
  print("klein")
}
ifelse(d$Muenzen >= 25, "viel", "wenig")''')

R("7.4", "sapply und while",
  sig="Funktion auf viele Werte anwenden, „solange …“",
  ne="sapply(değerler, fonksiyon) döngünün kısa yolu. while koşul sağlandıkça tekrarlar.",
  r='''sapply(1:5, function(i) i^2)
i <- 1
while (2^i < 100) i <- i + 1
i''')

R("7.5", "Text-Funktion mit Schleife (Probeklausur-Typ „Yennefer-Zahl“)",
  sig="„Schreiben Sie eine Funktion, die … aneinanderreiht“",
  ne="paste0 ile döngüde metin büyüt. Sonuç için return.",
  r='''zahl.fun <- function(n) {
  z <- "0."
  for (i in 1:n) z <- paste0(z, i)
  return(z)
}
zahl.fun(12)
nchar(zahl.fun(12)) - 2      # Anzahl Nachkommastellen''')

# =====================================================================
D.S("8", "Maximum-Likelihood in R",
    "Probeklausur B'de 15 puan: tekil likelihood'lar, toplam likelihood, likelihood fonksiyonu, ızgara araması, optimise/nlm.")

R("8.1", "Individuelle Likelihoods und Gesamt-Likelihood",
  sig="„Ergänzen Sie d um eine Spalte iL20 mit den individuellen Likelihoods … Berechnen Sie die Likelihood aller Beobachtungen“",
  ne="Her gözlem için d…(x, parametre) = tekil likelihood. Hepsinin çarpımı (prod) = toplam likelihood.",
  r='''d$iL20 <- dpois(d$Muenzen, lambda = 20)
head(d[, c("Muenzen", "iL20")], 3)
(L20 <- prod(d$iL20))
formatC(L20, format = "e", digits = 3)''',
  st=["Spalte mit <code>d$neu &lt;- d…(d$X, Parameter)</code> anlegen.", "<code>prod()</code> = Produkt aller Werte = Likelihood.",
      "Form \\(X\\times10^{Y}\\): <code>formatC(L, format = \"e\", digits = 3)</code> → „4.104e-20“ heißt \\(4.104\\times10^{-20}\\)."],
  ks="„Die Likelihood aller Beobachtungen unter λ = 20 beträgt L(λ = 20) = 4.104 × 10^(-20).“")

R("8.2", "Likelihood-Funktion und ML-Schätzer über einen Bereich",
  sig="„Schreiben Sie eine Funktion Likelihood.pois(lambda, x) … für alle Werte 17 ≤ λ ≤ 23 … bestimmen Sie den ML-Schätzer“",
  ne="Fonksiyon parametre ve veriyi alır, prod(d…) döndürür. Tüm değerler için hesapla, en büyüğü seç (which.max).",
  r='''Likelihood.pois <- function(lambda, x) {
  L <- prod(dpois(x, lambda))
  return(L)
}
werte <- 17:23
L <- sapply(werte, Likelihood.pois, x = d$Muenzen)
cbind(werte, L)
werte[which.max(L)]''',
  ks="„Die Likelihood ist bei λ = 22 maximal; der ML-Schätzer aus der gegebenen Menge ist λ̂ = 22.“",
  fa="Den λ-Wert mit der größten Likelihood angeben, nicht die Likelihood selbst. Mit einer for-Schleife und print() geht es genauso.")

R("8.3", "Log-Likelihood (gegen numerical underflow)",
  sig="„Log-Likelihood“, Likelihood ist 0 (zu klein)",
  ne="Çok gözlemde çarpım 0'a yuvarlanır → logaritma al: sum(log(d…)) veya log = TRUE.",
  r='''logL.pois <- function(lambda, x) sum(dpois(x, lambda, log = TRUE))
round(logL.pois(20, d$Muenzen), 3)
round(sum(log(dpois(d$Muenzen, 20))), 3)      # gleich
prod(dpois(rep(d$Muenzen, 100), 20))          # 1200 Werte: Produkt wird 0''')

R("8.4", "ML-Schätzer mit optimise (ein Parameter)",
  sig="„Bestimmen Sie den ML-Schätzer numerisch“, ein Parameter",
  ne="optimise(fonksiyon, interval, veri, maximum = TRUE) aralıktaki maksimumu bulur.",
  r='''opt <- optimise(logL.pois, interval = c(10, 40), x = d$Muenzen, maximum = TRUE)
round(opt$maximum, 3)
round(mean(d$Muenzen), 3)       # Kontrolle: Poisson-ML = Mittelwert''')

R("8.5", "ML mit nlm (zwei Parameter, Transformation)",
  sig="„Schätzen Sie α und β mit nlm … Startwerte … rücktransformiert“",
  ne="nlm <b>minimize</b> eder → negatif log-likelihood yaz. Parametreler pozitifse exp() dönüşümü; sonucu exp() ile geri çevir.",
  r='''x <- d$Kampfzeit
neglogL <- function(t_param, x) {
  param <- exp(t_param)              # garantiert positive Parameter
  -sum(dgamma(x, shape = param[1], rate = param[2], log = TRUE))
}
model <- suppressWarnings(nlm(neglogL, c(0.01, 0.5), x))
round(exp(model$estimate), 3)        # alpha, beta zurücktransformiert''',
  st=["Funktion bekommt den <b>transformierten</b> Parametervektor, rechnet <code>exp()</code> und gibt <b>−</b>Log-Likelihood zurück.",
      "Startwerte: so wie in der Aufgabe; stehen dort transformierte Werte (\\(\\alpha_t,\\beta_t\\)), direkt einsetzen.",
      "Ergebnis <code>model$estimate</code> ist transformiert → <code>exp()</code>."],
  fa="Warnungen („NaNs produced“) während der Iteration sind meist harmlos.")

R("8.6", "Likelihood grafisch darstellen",
  sig="„Stellen Sie die Log-Likelihood für λ zwischen … grafisch dar“",
  ne="Parametre ızgarası oluştur, her değer için log-likelihood hesapla, plot(type = \"l\").",
  r='''lam <- seq(15, 30, by = 0.1)
ll <- sapply(lam, logL.pois, x = d$Muenzen)
plot(lam, ll, type = "l", xlab = "lambda", ylab = "Log-Likelihood")
abline(v = lam[which.max(ll)], lty = 2)
lam[which.max(ll)]''')

# =====================================================================
R("8.7", "ML für eine selbst definierte Dichte (Teil-A-Typ in R)",
  sig="„Schreiben Sie die Dichte als Funktion …“, „bestimmen Sie den ML-Schätzer numerisch“",
  ne="Dichte'yi function olarak yaz, log-likelihood = sum(log(f)). optimise ile maksimize et, analitik sonuçla karşılaştır.",
  r='''f <- function(x, lambda) lambda^2 * x * exp(-lambda * x)
x <- c(1, 3, 2, 0.5, 3.5)
logL <- function(lambda) sum(log(f(x, lambda)))
optimise(logL, interval = c(0.01, 10), maximum = TRUE)$maximum
2 / mean(x)''',
  st=["Dichte genau wie in der Aufgabe abschreiben (<code>^</code> für Potenzen, <code>exp()</code> für e).",
      "Intervall bei <code>optimise</code> groß genug, aber nur zulässige Werte (z. B. λ > 0).",
      "<code>$maximum</code> = Schätzer, <code>$objective</code> = maximale Log-Likelihood."],
  ks="„Der numerisch bestimmte ML-Schätzer beträgt λ̂ = 1.000 und stimmt mit dem analytischen Ergebnis 2/x̄ überein.“")

R("8.8", "ML-Schätzer der Standardverteilungen direkt",
  sig="„Berechnen Sie den ML-Schätzer für … (Bernoulli/Poisson/Exponential/Normal)“",
  ne="Bilinen modellerde ML tahmini doğrudan bir ortalama formülü.",
  r='''y <- c(1, 0, 1, 1, 0)
mean(y)
w <- c(2.1, 0.7, 1.5, 3.2)
1 / mean(w)
c(mean(w), mean((w - mean(w))^2))''',
  st=["Bernoulli: \\(\\hat\\pi=\\bar x\\) · Poisson: \\(\\hat\\lambda=\\bar x\\) · Exponential: \\(\\hat\\lambda=1/\\bar x\\)",
      "Normal: \\(\\hat\\mu=\\bar x\\), \\(\\hat\\sigma^2=\\frac1n\\sum(x_i-\\bar x)^2\\) – Nenner \\(n\\), also <b>nicht</b> <code>var()</code>!"])

D.S("9", "Konfidenzintervalle und Tests in R",
    "Elle formül (qnorm/qt/qchisq) veya hazır fonksiyon (t.test, binom.test, chisq.test). Çıktıdan doğru sayıyı oku.")

R("9.1", "Konfidenzintervall für μ (σ bekannt und unbekannt)",
  sig="„Berechnen Sie ein 95 %-Konfidenzintervall für den Erwartungswert“",
  ne="σ biliniyorsa qnorm, bilinmiyorsa qt(…, n−1) ve sd. t.test()$conf.int aynı sonucu verir.",
  r='''x <- d$Kampfzeit; n <- length(x)
round(mean(x) + c(-1, 1) * qnorm(0.975) * 30 / sqrt(n), 3)        # sigma = 30 bekannt
round(mean(x) + c(-1, 1) * qt(0.975, n - 1) * sd(x) / sqrt(n), 3) # sigma unbekannt
round(t.test(x, conf.level = 0.95)$conf.int, 3)''',
  ks="„Das 95 %-Konfidenzintervall für die mittlere Kampfzeit lautet [14.365; 53.335].“")

R("9.2", "Konfidenzintervall für Anteil und Varianz",
  sig="„KI für den Anteil“, „KI für die Varianz“",
  ne="Oran: p̂ ± z·√(p̂(1−p̂)/n). Varyans: (n−1)s²/χ² kantilleri (büyük kantil alt sınır).",
  r='''p <- 60 / 200
round(p + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / 200), 3)
s2 <- var(d$Muenzen); n <- 12
round((n - 1) * s2 / qchisq(c(0.975, 0.025), df = n - 1), 3)''')

R("9.3", "t-Test mit t.test und Output lesen",
  sig="„Überprüfen Sie die Behauptung mit einem geeigneten Test in R“, „Welcher Code ist richtig?“",
  ne="t.test(x, mu = μ₀, alternative = \"greater\"/\"less\"/\"two.sided\"). Çıktıdan t, df, p-value oku; p ≤ α → H₀ ret.",
  r='''t.test(d$Muenzen, mu = 20, alternative = "greater")''',
  st=["\\(H_1:\\mu&gt;\\mu_0\\) → <code>\"greater\"</code> · \\(H_1:\\mu&lt;\\mu_0\\) → <code>\"less\"</code> · \\(H_1:\\mu\\ne\\mu_0\\) → Standard (zweiseitig).",
      "Konfidenzniveau ändern: <code>conf.level = 0.9</code>.", "Zahlen direkt holen: <code>t.test(…)$p.value</code>, <code>$statistic</code>, <code>$conf.int</code>."],
  ks="„H₀: μ ≤ 20 gegen H₁: μ > 20. Der p-Wert beträgt 0.172 > 0.05, daher wird H₀ nicht verworfen; eine mittlere Münzzahl über 20 kann zum Niveau 5 % nicht statistisch abgesichert werden.“")

R("9.4", "Test von Hand: Teststatistik, kritischer Wert, p-Wert",
  sig="„Berechnen Sie Teststatistik und p-Wert in R“ (Gauß-Test, t-Test)",
  ne="z veya t'yi formülle hesapla; kritik değer q…, p-değeri p… ile.",
  r='''x <- d$Muenzen; n <- length(x)
z <- (mean(x) - 20) / (6 / sqrt(n))          # Gauss-Test, sigma = 6 bekannt
round(z, 3); round(qnorm(0.95), 3); round(1 - pnorm(z), 3)
t <- (mean(x) - 20) / (sd(x) / sqrt(n))      # t-Test
round(t, 3); round(1 - pt(t, df = n - 1), 3)
round(2 * (1 - pt(abs(t), df = n - 1)), 3)   # zweiseitig''')

R("9.5", "Binomialtest (exakt und über pbinom)",
  sig="„Anteil“, „7 von 8 Versuchen“, kleines n",
  ne="binom.test(başarı, n, p = π₀, alternative) veya p-değerini doğrudan pbinom ile.",
  r='''binom.test(7, 8, p = 0.5, alternative = "greater")$p.value
1 - pbinom(6, 8, 0.5)                       # P(X >= 7), gleich
z <- (220 - 400 * 0.5) / sqrt(400 * 0.5 * 0.5); round(1 - pnorm(z), 4)   # approximativ''')

R("9.6", "χ²-Unabhängigkeitstest und χ²-Anpassungstest",
  sig="„Testen Sie, ob … unabhängig sind“, „Ist der Würfel fair?“",
  ne="Tabloyu matrix olarak gir; chisq.test(tablo, correct = FALSE) — dersteki elle hesapla aynı. Uyum testi: chisq.test(sıklıklar, p = oranlar).",
  r='''tafel <- matrix(c(20, 40, 60, 80), nrow = 2)     # spaltenweise!
test <- chisq.test(tafel, correct = FALSE)
test$expected
round(test$statistic, 3); round(test$p.value, 3)
chisq.test(c(45, 35, 20), p = c(0.5, 0.3, 0.2))''',
  fa="Bei 2×2-Tafeln macht R ohne <code>correct = FALSE</code> eine Stetigkeitskorrektur – dann stimmt der Wert nicht mit der Rechnung per Hand überein.")

R("9.7", "χ²-Varianztest von Hand",
  sig="„Testen Sie, ob die Varianz größer als … ist“",
  ne="χ² = (n−1)·s²/σ₀²; kritik değer qchisq, p-değeri 1 − pchisq.",
  r='''x <- d$Muenzen; n <- length(x)
chi <- (n - 1) * var(x) / 25                  # H0: sigma^2 <= 25
round(chi, 3); round(qchisq(0.95, n - 1), 3); round(1 - pchisq(chi, n - 1), 3)''')

# =====================================================================
R("9.8", "Zwei Gruppen vergleichen (Zwei-Stichproben-t-Test)",
  sig="„Unterscheiden sich die mittleren … in Flusstal und Bergtal?“",
  ne="İki grubun ortalamasını karşılaştır: t.test(x1, x2). Tek yönlüyse alternative ekle.",
  r='''x1 <- d$Muenzen[d$Tal == "Flusstal"]
x2 <- d$Muenzen[d$Tal == "Bergtal"]
t.test(x1, x2, alternative = "two.sided")''',
  st=["H₀: μ₁ = μ₂ vs. H₁: μ₁ ≠ μ₂ (bzw. < / > mit alternative).",
      "Bei verbundenen Stichproben (vorher/nachher, gleiche Personen): <code>paired = TRUE</code>.",
      "Gleiche Varianzen angenommen: <code>var.equal = TRUE</code>."],
  ks="„Da der p-Wert 0.095 > 0.05 ist, kann H₀ nicht abgelehnt werden; ein Unterschied der mittleren Münzanzahl ist nicht statistisch abgesichert.“")

R("9.9", "Anteil testen und KI für einen Anteil (prop.test, binom.test)",
  sig="„80 von 100 …“, „Anteil größer als 75 %?“",
  ne="prop.test normal yaklaşımı, binom.test tam test. İkisi de GA verir.",
  r='''prop.test(x = 80, n = 100, p = 0.75, alternative = "greater", correct = FALSE)$p.value
binom.test(80, 100, p = 0.75, alternative = "greater")$p.value
p <- 0.8; n <- 100
p + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / n)''',
  fa="Das KI aus der Vorlesung ist das Wald-Intervall (letzte Zeile); prop.test ohne/ mit correct liefert ein etwas anderes Intervall.")

D.S("10", "Lineare Regression in R",
    "lm ile model, summary ile katsayılar ve anlamlılık, predict ile tahmin.")

R("10.1", "Modell schätzen und Output lesen",
  sig="„Schätzen Sie ein lineares Regressionsmodell von … auf …“, „Interpretieren Sie“",
  ne="lm(y ~ x, data = d). summary'de Estimate = katsayı, Pr(>|t|) = p-değeri (H₀: β = 0), R-squared.",
  r='''m <- lm(Muenzen ~ Kampfzeit, data = d)
summary(m)''',
  ks="„Steigt die Kampfzeit um eine Minute, steigt die Münzzahl im Durchschnitt um 0.221 Münzen (ceteris paribus). Der Koeffizient ist signifikant (p < 0.001).“")

R("10.2", "Koeffizienten, Prognose, Residuen, R²",
  sig="„Welche Münzzahl wird für 30 Minuten prognostiziert?“, „Bestimmtheitsmaß“",
  ne="coef → katsayılar, predict(m, newdata = data.frame(...)) → tahmin, residuals → kalıntılar, summary(m)$r.squared → R².",
  r='''round(coef(m), 3)
round(predict(m, newdata = data.frame(Kampfzeit = 30)), 3)
round(head(residuals(m), 3), 3)
round(summary(m)$r.squared, 3)
round(confint(m, level = 0.95), 3)''',
  fa="In <code>newdata</code> muss der Spaltenname exakt wie im Modell heißen (Kampfzeit).")

# =====================================================================
D.S("11", "Komplette Teil-B-Klausur Schritt für Schritt (Altklausur-Typ)",
    "Gerçek sınavın (Altklausur Witcher) tüm alt soruları sırayla: kod, çıktı, Antwortsatz. Kendi sınavında sadece dosya ve değişken adlarını değiştir.")
D.E("11.1", "a) Working Directory setzen",
    sig="„Setzen Sie mittels setwd(path.expand(\"~\")) Ihr Working Directory …“ (2 P)",
    ne="Komutu aynen yaz. Kontrol için getwd().",
    r='''setwd(path.expand("~"))
getwd()''', run=False)
R("11.2", "b) Daten einlesen und die ersten 6 Zeilen wiedergeben (4 P)",
  sig="„Speichern Sie die … Daten als Data-Frame-Objekt d … und geben Sie die ersten 6 Zeilen wieder“",
  ne="Ayırıcıyı kontrol et (burada ;). head(d) çıktısını da kopyala.",
  r='''d <- read.csv("Taverne.csv", sep = ";", dec = ".", header = TRUE)
head(d)''')
R("11.3", "c) Objekttypen ermitteln (4 P)",
  sig="„Ermitteln Sie unter Einbezug eines passenden R-Befehls die Objekttypen der Variablen Tal und Muenzen“",
  r='''typeof(d$Tal)
typeof(d$Muenzen)
class(d$Muenzen)''',
  ks="„Die Variable Tal ist vom Typ character (Text). Die Variable Muenzen ist ein numerisches Objekt vom Typ integer, d. h. sie enthält nur ganze Zahlen.“")
R("11.4", "d) Mittelwert und unverzerrte Standardabweichung (4 P)",
  sig="„Berechnen und nennen Sie das arithmetische Mittel und den unverzerrten Schätzer für die Standardabweichung … auf 3 Nachkommastellen“",
  r='''round(mean(d$Muenzen), 3)
round(sd(d$Muenzen), 3)''',
  ks="„Das arithmetische Mittel der Variable Muenzen beträgt 22.083. Der unverzerrte Schätzer für die Standardabweichung beträgt 7.292.“")
R("11.5", "e) Histogramm mit vorgegebenen Klassen speichern (8 P)",
  sig="„Histogramm … Intervallgrenzen [5,15), [15,20), [20,25), [25,35) … Titel … Dichte … als Histogramm.pdf speichern“",
  r='''pdf("Histogramm.pdf")
hist(d$Muenzen, breaks = c(5, 15, 20, 25, 35), right = FALSE, freq = FALSE,
     main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil e)",
     xlab = "Muenzen", ylab = "Dichte")
dev.off()''',
  st=["breaks = genau die Grenzen aus der Aufgabe · [a, b) → <code>right = FALSE</code> · Dichte → <code>freq = FALSE</code>.",
      "Titel, x- und y-Achse exakt wie verlangt; Datei im Ordner prüfen und in ILIAS hochladen."])
R("11.6", "f) Individuelle Likelihoods und Gesamt-Likelihood (6 P)",
  sig="„… Poissonverteilung … λ = 20 … Spalte iL20 … Likelihood aller Beobachtungen … in der Form X × 10^Y“",
  r='''d$iL20 <- dpois(d$Muenzen, lambda = 20)
head(d)
L20 <- prod(d$iL20)
L20''',
  ks="„Unter der Annahme λ = 20 beträgt die Likelihood aller Beobachtungen L(20) = X × 10^(Y)“ – X und Y aus dem Output ablesen (3 Nachkommastellen).")
R("11.7", "g) Likelihood-Funktion und ML-Schätzer auf einem Gitter (9 P)",
  sig="„Schreiben Sie eine Funktion Likelihood.pois(lambda, x) … für alle λ ∈ {17, …, 23} … ML-Schätzer“",
  r='''Likelihood.pois <- function(lambda, x) {
  return(prod(dpois(x, lambda)))
}
werte <- 17:23
L <- sapply(werte, Likelihood.pois, x = d$Muenzen)
cbind(werte, L)
werte[which.max(L)]
mean(d$Muenzen)''',
  ks="„Aus der gegebenen Menge maximiert λ = 22 die Likelihood; der ML-Schätzer ist λ̂ = 22 (analytisch wäre x̄ = 22.083).“")
R("11.8", "h) Funktion mit Schleife: Zahl aus Ziffern zusammensetzen (8 P)",
  sig="„Schreiben Sie eine R-Funktion YenneferZahl.fun, welche für n … die Zahl 0.123456789101112… bestimmt“",
  r='''YenneferZahl.fun <- function(n) {
  s <- ""
  for (i in 1:n) {
    s <- paste0(s, i)
  }
  return(paste0("0.", s))
}
YenneferZahl.fun(17)
substr(YenneferZahl.fun(60), 1, 101)''',
  st=["Leeren Text anlegen, in der Schleife jede Zahl anhängen (<code>paste0</code> ohne Leerzeichen).",
      "„bis auf die 99. Nachkommastelle“: genügend Zahlen anhängen, dann mit <code>substr(…, 1, 101)</code> abschneiden (\"0.\" + 99 Ziffern)."])

# =====================================================================
D.S("12", "Antwortsätze für ILIAS – Katalog",
    "Kutu 2 için hazır cümleler. Sayıları kendi çıktından al, 3 ondalık.")
D.E("12.1", "Datentypen, Kennzahlen, Häufigkeiten",
    ks="„Die Variable … ist vom Typ character/integer/numeric.“ · „Das arithmetische Mittel der Variable … beträgt ….“ · „Der unverzerrte Schätzer für die Standardabweichung beträgt ….“ · „Der Median beträgt …, der Interquartilsabstand ….“ · „Die häufigste Ausprägung (Modus) ist ….“ · „Der Anteil der Beobachtungen mit … beträgt ….“")
D.E("12.2", "Gruppen, Tabellen, Grafiken",
    ks="„Im Tal … ist die durchschnittliche Münzanzahl mit … am höchsten.“ · „In der Gruppe … ist der Anteil … mit … am größten.“ · „Der Boxplot zeigt, dass … den höchsten Median hat und die Werte dort am stärksten streuen.“ · „Das Histogramm ist rechtsschief.“")
D.E("12.3", "Korrelation und Regression",
    ks="„Der Korrelationskoeffizient nach Bravais-Pearson beträgt …; es liegt ein (schwacher/mittlerer/starker) (positiver/negativer) linearer Zusammenhang vor.“ · „Die geschätzte Regressionsgerade lautet ŷ = a + b·x. Steigt x um eine Einheit, steigt/sinkt y im Mittel um b.“ · „Das Bestimmtheitsmaß R² = … bedeutet, dass …% der Streuung von y durch x erklärt werden.“")
D.E("12.4", "Likelihood und ML",
    ks="„Unter der Annahme λ = … beträgt die Likelihood aller Beobachtungen … × 10^(…).“ · „Aus der gegebenen Menge maximiert λ = … die Likelihood; der ML-Schätzer ist λ̂ = ….“ · „Der numerisch bestimmte ML-Schätzer beträgt …“")
D.E("12.5", "Konfidenzintervalle und Tests",
    ks="„Hypothesen: H₀: μ ≤ μ₀ vs. H₁: μ > μ₀.“ · „Da der p-Wert … kleiner als α = 0.05 ist, wird H₀ abgelehnt. Es kann statistisch abgesichert werden, dass ….“ · „Da der p-Wert … größer als α ist, kann H₀ nicht abgelehnt werden. Es kann nicht statistisch abgesichert werden, dass ….“ · „Das 95 %-Konfidenzintervall für … lautet [… ; …].“")

# =====================================================================
D.S("13", "Fehlermeldungen und Kontrolle",
    "Hata mesajını okuyunca çoğu zaman sebep hemen belli olur.")

D.E("13.1", "Typische Fehlermeldungen und ihre Lösung",
    sig="Error in …",
    ne="Mesajın son kısmı ne olduğunu söyler: nesne yok, fonksiyon yok, beklenmeyen sembol, sayısal olmayan argüman.",
    extra=("<table class='t'><tr><th>Meldung</th><th>Ursache</th><th>Lösung</th></tr>"
           "<tr><td><code>object 'X' not found</code></td><td>Objekt nicht erstellt, Tippfehler, Groß/Klein</td><td>Zeile mit der Zuweisung ausführen; Schreibweise prüfen</td></tr>"
           "<tr><td><code>could not find function \"…\"</code></td><td>Funktionsname falsch oder eigene Funktion noch nicht ausgeführt</td><td>Schreibweise; Funktionsdefinition zuerst ausführen</td></tr>"
           "<tr><td><code>unexpected symbol / ')' / ','</code></td><td>Klammer, Komma oder Anführungszeichen fehlt bzw. zu viel</td><td>Klammern zählen</td></tr>"
           "<tr><td><code>non-numeric argument to binary operator</code></td><td>mit Text gerechnet</td><td><code>str(d)</code>; Einlesen mit richtigem dec / as.numeric</td></tr>"
           "<tr><td><code>argument is not numeric or logical: returning NA</code></td><td>mean() auf Text-Spalte</td><td>richtige Spalte, Einlesen prüfen</td></tr>"
           "<tr><td><code>cannot open file 'X.csv': No such file</code></td><td>falscher Ordner oder Dateiname</td><td><code>getwd()</code>, <code>list.files()</code>, setwd</td></tr>"
           "<tr><td><code>undefined columns selected</code></td><td>Spaltenname falsch in d[ , \"…\"]</td><td><code>names(d)</code></td></tr>"
           "<tr><td><code>$ operator is invalid for atomic vectors</code></td><td>$ auf einen Vektor statt Data Frame</td><td>Objekt prüfen (<code>class()</code>)</td></tr>"
           "<tr><td>Ergebnis <code>NA</code></td><td>fehlende Werte</td><td><code>na.rm = TRUE</code></td></tr>"
           "<tr><td>Konsole zeigt <code>+</code></td><td>Befehl unvollständig (Klammer offen)</td><td>Esc drücken, Klammer ergänzen</td></tr></table>"))

D.E("13.2", "Checkliste vor dem Abgeben",
    sig="letzte 5 Minuten",
    ne="Her kutuyu bu listeyle kontrol et.",
    st=["Jede Teilaufgabe: Code <b>und</b> Output in Box 1, Antwortsatz (ohne Code) in Box 2.",
        "Alle Zahlen mit <code>round(…, 3)</code> gerundet, auch im Antwortsatz.",
        "Grafiken: Titel mit Sitz, Matrikelnummer, Aufgabenteil; Achsenbeschriftung; als PDF gespeichert und hochgeladen.",
        "Fehlerhaften Code aus der Antwort gelöscht; keine zwei widersprüchlichen Ergebnisse.",
        "R-Skript gespeichert (Strg+S) im Ordner Dokumente."])
