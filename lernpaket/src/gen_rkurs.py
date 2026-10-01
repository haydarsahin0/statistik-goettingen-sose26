"""R-Komplettkurs für Klausurteil B im Klausurformat.
Alle R-Outputs werden echt erzeugt: Code jeder Karte wird in einer R-Sitzung ausgeführt."""
import os, re, shutil, subprocess, html
import pymupdf

SRC = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(SRC, "rwork")
FIG = os.path.join(SRC, "fig")
DATA = os.path.join(SRC, "..", "uebungsdaten")
shutil.rmtree(WORK, ignore_errors=True); os.makedirs(WORK)
for f in ["Taverne.csv", "Fahrrad.csv"]:
    shutil.copy(os.path.join(DATA, f), WORK)

C = []


def sec(t, intro=None):
    C.append(dict(kind="sec", t=t, intro=intro))


def card(title, p, auf, steps, code=None, satz=None, warn=None, pdf=None, run=True, extra=None):
    C.append(dict(kind="card", title=title, p=p, auf=auf, steps=steps, code=code, satz=satz,
                  warn=warn, pdf=pdf, run=run, extra=extra))


# ======================================================================
sec("0 · Bevor du anfängst",
    "So ist Teil B aufgebaut: 60 Minuten, 45 Punkte, eine große Aufgabe mit Teilen (a), (b), (c) … zu einem Datensatz. "
    "Du arbeitest in RStudio, die Antworten trägst du in ILIAS ein. Pro Teilaufgabe gibt es bis zu zwei Kästchen: "
    "<b>Kästchen 1</b> = R-Code und R-Output (kopieren und einfügen), <b>Kästchen 2</b> = Antwortsatz ohne Code, gerundet auf 3 Nachkommastellen.")

card("RStudio bedienen", 100,
 "Öffnen Sie ein neues R-Skript, schreiben Sie einen Befehl hinein und führen Sie ihn aus. <span class='pt'>(0 P – aber nötig für alles)</span>",
 ["File → New File → R Script (Strg + Umschalt + N). Oben links ist jetzt dein Skript.",
  "Befehl ins Skript schreiben. Cursor in die Zeile setzen und <b>Strg + Enter</b> drücken → der Befehl läuft in der Console (unten links).",
  "Mehrere Zeilen markieren + Strg + Enter → alle laufen nacheinander.",
  "<code>#</code> = Kommentar. Alles danach wird nicht ausgeführt.",
  "Skript oft speichern (Strg + S) im Ordner Dokumente.",
  "Code + Output für ILIAS: in der Console markieren und kopieren."],
 "3 + 4      # Kommentar: R als Taschenrechner\n2^3\nsqrt(16)", None)

card("Runden und Antwortsatz", 100,
 "Berechnen Sie 10/3 und geben Sie das Ergebnis auf drei Nachkommastellen gerundet an. <span class='pt'>(1 P)</span>",
 ["Immer mit <code>round(Zahl, 3)</code> runden – die Klausur verlangt einen R-Befehl zum Runden.",
  "Kästchen 1: Code und Output. Kästchen 2: ganzer Satz mit der gerundeten Zahl."],
 "round(10/3, 3)\nround(10/3, digits = 2)",
 "Das Ergebnis beträgt 3.333.",
 "R zeigt Nullen am Ende nicht (2.5 statt 2.500). Das ist trotzdem korrekt gerundet.")

# ======================================================================
sec("1 · Grundlagen: Objekte, Vektoren, Datentypen")

card("Objekte speichern", 60,
 "Speichern Sie die Zahl 7 im Objekt a und die Zahl 3 im Objekt b. Berechnen Sie a/b und speichern Sie das Ergebnis in q. <span class='pt'>(2 P)</span>",
 ["<code>&lt;-</code> ist der Zuweisungspfeil: rechts der Wert, links der Name.",
  "Den Namen allein ausführen → R zeigt den Inhalt.",
  "Groß- und Kleinschreibung zählt: <code>A</code> ist nicht <code>a</code>."],
 "a <- 7\nb <- 3\nq <- a / b\nq")

card("Vektoren erstellen", 70,
 "Erstellen Sie (i) einen Vektor x mit den Werten 4, 8, 15, 16, 23, 42, (ii) einen Vektor mit den Zahlen 1 bis 20, (iii) die Folge 2, 4, 6, 8 und (iv) einen Vektor mit fünfmal der 0. Bestimmen Sie die Länge und die Summe von x. <span class='pt'>(4 P)</span>",
 ["<code>c(…)</code> verbindet Werte zu einem Vektor.", "<code>1:20</code> = alle ganzen Zahlen von 1 bis 20.",
  "<code>seq(von, bis, by = Schritt)</code> = Folge.", "<code>rep(Wert, Anzahl)</code> = Wiederholung.",
  "<code>length()</code> = Anzahl Elemente · <code>sum()</code> = Summe."],
 "x <- c(4, 8, 15, 16, 23, 42)\n1:20\nseq(2, 8, by = 2)\nrep(0, 5)\nlength(x)\nsum(x)")

card("Rechnen mit Vektoren", 50,
 "Multiplizieren Sie jedes Element von x mit 1.5. Berechnen Sie die Summe der quadrierten Werte von x. <span class='pt'>(2 P)</span>",
 ["R rechnet automatisch mit <b>jedem</b> Element – keine Schleife nötig.", "<code>x^2</code> quadriert jedes Element."],
 "x * 1.5\nsum(x^2)")

card("Elemente auswählen", 60,
 "Geben Sie das erste, das dritte und das letzte Element von x aus. Geben Sie alle Werte größer als 10 aus. An welchen Positionen stehen sie? <span class='pt'>(3 P)</span>",
 ["Eckige Klammern <code>x[ ]</code> wählen aus. <code>x[1]</code> = erstes Element.", "<code>x[c(1, 3)]</code> = mehrere Positionen. <code>x[length(x)]</code> = letztes.",
  "<code>x[x &gt; 10]</code> = alle Werte, für die die Bedingung TRUE ist.", "<code>which(x &gt; 10)</code> = Positionen."],
 "x[1]\nx[c(1, 3)]\nx[length(x)]\nx > 10\nx[x > 10]\nwhich(x > 10)")

card("Vergleiche und logische Werte", 50,
 "Wie viele Werte von x sind größer als 10? Welcher Anteil? Ist 15 in x enthalten? <span class='pt'>(3 P)</span>",
 ["Vergleiche: <code>==</code> gleich, <code>!=</code> ungleich, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code>, <code>&lt;=</code>.",
  "Verknüpfen: <code>&amp;</code> = und, <code>|</code> = oder.", "TRUE zählt als 1, FALSE als 0 → <code>sum()</code> = Anzahl, <code>mean()</code> = Anteil.",
  "<code>is.element(15, x)</code> oder <code>15 %in% x</code>."],
 "sum(x > 10)\nmean(x > 10)\nis.element(15, x)\nx > 5 & x < 20",
 "4 Werte von x (66.7 %) sind größer als 10.")

card("Datentypen bestimmen", 80,
 "Bestimmen Sie den Objekttyp von x, von \"Bergtal\" und von TRUE. <span class='pt'>(3 P)</span>",
 ["<code>typeof()</code>: double, integer, character, logical.", "<code>class()</code>: numeric, integer, character, logical, factor, data.frame.",
  "Zahlen mit Komma → double/numeric · nur ganze Zahlen aus Datei → integer · Text → character · TRUE/FALSE → logical.",
  "Prüfen: <code>is.numeric()</code>, <code>is.character()</code>, <code>is.factor()</code>. Umwandeln: <code>as.numeric()</code>, <code>as.character()</code>."],
 "typeof(x)\nclass(x)\ntypeof(\"Bergtal\")\ntypeof(TRUE)\nis.numeric(x)\nas.numeric(\"3.5\")")

card("Faktoren", 40,
 "Speichern Sie die Antworten \"ja\", \"nein\", \"ja\", \"ja\" als Factor mit den Stufen ja und nein. Geben Sie die Stufen aus. <span class='pt'>(2 P)</span>",
 ["Factor = Kategorie-Variable mit festen Stufen (levels).", "<code>factor(x, levels = c(…))</code>. <code>levels()</code> zeigt die Stufen.", "<code>cut()</code> erzeugt automatisch einen Factor."],
 "f <- factor(c(\"ja\", \"nein\", \"ja\", \"ja\"), levels = c(\"ja\", \"nein\"))\nf\nlevels(f)\ntable(f)")

card("Fehlende Werte (NA)", 30,
 "Der Vektor y enthält einen fehlenden Wert: 3, NA, 5, 8. Berechnen Sie den Mittelwert. <span class='pt'>(2 P)</span>",
 ["NA = fehlender Wert. Mit NA liefert <code>mean()</code> wieder NA.", "Lösung: <code>na.rm = TRUE</code> oder <code>na.omit()</code>."],
 "y <- c(3, NA, 5, 8)\nmean(y)\nmean(y, na.rm = TRUE)\nis.na(y)\nna.omit(y)",
 "Der Mittelwert der vorhandenen Werte beträgt 5.333.")

card("Mengen in R (Testat 0)", 25,
 "A &lt;- 3:6, B &lt;- 4:2, C &lt;- seq(2, 8, by = 2). Bestimmen Sie A ∪ B, A ∩ C, B \\ C und ob 6 in C liegt. <span class='pt'>(4 P)</span>",
 ["Vereinigung <code>union()</code>, Schnitt <code>intersect()</code>, Differenz <code>setdiff()</code>, Element <code>is.element()</code>."],
 "A <- 3:6\nB <- 4:2\nC <- seq(2, 8, by = 2)\nunion(A, B)\nintersect(A, C)\nsetdiff(B, C)\nis.element(6, C)")

card("Text zusammenfügen und ausgeben", 20,
 "Fügen Sie \"Lambda =\" und die Zahl 20 zu einem Text zusammen und geben Sie ihn aus. <span class='pt'>(1 P)</span>",
 ["<code>paste(\"a\", \"b\")</code> mit Leerzeichen, <code>paste0()</code> ohne Leerzeichen.", "<code>cat()</code> gibt Text aus, <code>\"\\n\"</code> = neue Zeile."],
 "paste(\"Lambda =\", 20)\npaste0(\"0.\", 1, 2, 3)\ncat(\"Lambda =\", 20, \"\\n\")")

card("Matrix und Data Frame von Hand", 30,
 "Erstellen Sie eine 2×2-Matrix mit den Werten 15, 75, 45, 65 (spaltenweise) und einen Data Frame mit den Spalten Name und Alter. <span class='pt'>(2 P)</span>",
 ["<code>matrix(Werte, nrow = Zeilen)</code> füllt spaltenweise (<code>byrow = TRUE</code> → zeilenweise).",
  "<code>data.frame(Spalte1 = …, Spalte2 = …)</code>. <code>dim()</code> = Zeilen und Spalten."],
 "m <- matrix(c(15, 75, 45, 65), nrow = 2)\nm\ndf <- data.frame(Name = c(\"Ana\", \"Ben\"), Alter = c(21, 24))\ndf\ndim(df)")

# ======================================================================
sec("2 · Datensatz einlesen und ansehen")

card("Working Directory setzen und Daten einlesen", 100,
 "Die Daten sind in der Datei Taverne.csv im Ordner Dokumente abgespeichert. Setzen Sie mittels setwd(path.expand(\"~\")) Ihr Working Directory. Speichern Sie die Daten als Data-Frame-Objekt d und geben Sie die ersten 6 Zeilen wieder. <span class='pt'>(4 P)</span>",
 ["<code>setwd(path.expand(\"~\"))</code> = Ordner Dokumente als Arbeitsordner.",
  "<code>list.files()</code> zeigt, welche Dateien dort liegen → Dateiname genau abschreiben.",
  "Datei vorher ansehen (RStudio: Files → Datei → View File): Trennzeichen zwischen Spalten = <code>sep</code>, Dezimalzeichen = <code>dec</code>.",
  "<code>read.csv(\"Datei\", sep = …, dec = …, header = TRUE)</code>. <code>head(d)</code> = erste 6 Zeilen."],
 "setwd(path.expand(\"~\"))\nlist.files()\nd <- read.csv(\"Taverne.csv\", sep = \";\", dec = \".\", header = TRUE)\nhead(d)",
 None,
 "Fehler „kann Datei nicht öffnen“ → Datei liegt nicht in Dokumente oder Name falsch geschrieben (list.files() prüfen).")

card("Anderes Dateiformat (Komma als Dezimalzeichen)", 60,
 "Lesen Sie Fahrrad.csv ein (Speicherung als Objekt f). Prüfen Sie, ob die Zahlen richtig eingelesen wurden. <span class='pt'>(3 P)</span>",
 ["In der Datei steht <code>12,6</code> → deutsches Format: <code>sep = \";\"</code> und <code>dec = \",\"</code>.",
  "Mit <code>str()</code> prüfen: Zahlen müssen <code>num</code> sein. Sind sie <code>chr</code> → dec falsch.",
  "Nur eine Spalte → sep falsch."],
 "f <- read.csv(\"Fahrrad.csv\", sep = \";\", dec = \",\", header = TRUE)\nstr(f)")

card("Struktur und Objekttypen ermitteln", 80,
 "Der Data Frame ist eine spezielle Liste. Ermitteln Sie unter Einbezug eines passenden R-Befehls die Objekttypen der Variablen Tal und Muenzen. <span class='pt'>(4 P)</span>",
 ["<code>str(d)</code> zeigt alle Variablen mit Typ. Oder einzeln: <code>typeof(d$Tal)</code>, <code>class(d$Tal)</code>.",
  "<code>d$Name</code> = eine Spalte des Data Frames.", "chr = character · int = integer (numeric, ganze Zahlen) · num = numeric (double)."],
 "str(d)\ntypeof(d$Tal)\nclass(d$Muenzen)",
 "Die Variable Tal ist ein character-Objekt. Die Variable Muenzen ist numerisch vom Typ integer (nur ganze Zahlen).")

card("Größe und Namen des Datensatzes", 40,
 "Wie viele Beobachtungen und Variablen enthält d? Wie heißen die Variablen? <span class='pt'>(2 P)</span>",
 ["<code>nrow()</code> Zeilen · <code>ncol()</code> Spalten · <code>dim()</code> beides · <code>names()</code> Variablennamen · <code>summary(d)</code> Überblick."],
 "nrow(d)\nncol(d)\ndim(d)\nnames(d)",
 "Der Datensatz enthält 12 Beobachtungen und 5 Variablen.")

card("Zeilen und Spalten auswählen", 50,
 "Geben Sie (i) die 3. Zeile, (ii) die Spalte Muenzen, (iii) alle Tavernen im Bergtal, (iv) die Taverne mit den meisten Münzen aus. <span class='pt'>(4 P)</span>",
 ["<code>d[Zeile, Spalte]</code>. Leer = alle. <code>d[3, ]</code> = Zeile 3.",
  "<code>d[d$Tal == \"Bergtal\", ]</code> = alle Zeilen mit Bedingung (Komma nicht vergessen!).",
  "<code>subset(d, Bedingung)</code> macht dasselbe.", "<code>which.max()</code> = Position des Maximums."],
 "d[3, ]\nd$Muenzen\nd[d$Tal == \"Bergtal\", ]\nd[which.max(d$Muenzen), ]")

card("Teildatensatz mit subset", 50,
 "Betrachten Sie nur die Beobachtungen, bei denen die Kampfzeit mindestens 5, aber weniger als 60 Minuten betrug. Wie viele sind es? <span class='pt'>(2 P)</span>",
 ["<code>subset(d, Bedingung)</code>. Mehrere Bedingungen mit <code>&amp;</code> (und) oder <code>|</code> (oder).",
  "Danach mit dem neuen Objekt weiterrechnen (<code>s$…</code>, nicht <code>d$…</code>)."],
 "s <- subset(d, Kampfzeit >= 5 & Kampfzeit < 60)\nnrow(s)\ns",
 "6 Beobachtungen haben eine Kampfzeit von mindestens 5 und unter 60 Minuten.")

card("Neue Variable hinzufügen", 40,
 "Ergänzen Sie d um die Variable MproMin = Münzen pro Kampfminute. <span class='pt'>(2 P)</span>",
 ["<code>d$NeuerName &lt;- Rechnung</code> fügt eine Spalte hinzu."],
 "d$MproMin <- d$Muenzen / d$Kampfzeit\nhead(d)")

# ======================================================================
sec("3 · Kennzahlen (deskriptive Statistik)")

card("Mittelwert und Standardabweichung", 90,
 "Berechnen und nennen Sie das arithmetische Mittel und den unverzerrten Schätzer der Standardabweichung der Variable Kampfzeit. Runden Sie auf drei Nachkommastellen. <span class='pt'>(4 P)</span>",
 ["<code>mean()</code>, <code>sd()</code>. <code>sd</code> und <code>var</code> rechnen <b>immer</b> mit n − 1 (unverzerrt).", "Mit <code>round(…, 3)</code> runden."],
 "round(mean(d$Kampfzeit), 3)\nround(sd(d$Kampfzeit), 3)",
 "Das arithmetische Mittel der Kampfzeit beträgt 33.85 Minuten. Der unverzerrte Schätzer der Standardabweichung beträgt 30.667 Minuten.")

card("Varianz: unverzerrt und empirisch", 50,
 "Berechnen Sie die unverzerrte und die empirische (1/n) Varianz der Variable Muenzen. <span class='pt'>(3 P)</span>",
 ["<code>var()</code> = unverzerrt (n − 1).", "Empirisch: <code>var(x) * (n − 1) / n</code> mit <code>n &lt;- length(x)</code>. Oder <code>mean(x^2) − mean(x)^2</code>."],
 "n <- length(d$Muenzen)\nround(var(d$Muenzen), 3)\nround(var(d$Muenzen) * (n - 1) / n, 3)\nround(mean(d$Muenzen^2) - mean(d$Muenzen)^2, 3)",
 "Die unverzerrte Varianz beträgt 53.174, die empirische Varianz 48.743.")

card("Median, Quantile, IQR, Wertebereich", 70,
 "Bestimmen Sie Median, Interquartilsabstand, das 90 %-Quantil und den Wertebereich der Variable Kampfzeit. <span class='pt'>(4 P)</span>",
 ["<code>median()</code>, <code>IQR()</code>, <code>quantile(x, 0.9)</code>, <code>range()</code> (Min und Max), <code>min()</code>, <code>max()</code>.",
  "<code>summary()</code> gibt Min, Quartile, Median, Mittel, Max auf einmal."],
 "median(d$Kampfzeit)\nIQR(d$Kampfzeit)\nquantile(d$Kampfzeit, 0.9)\nquantile(d$Kampfzeit, c(0.25, 0.75))\nrange(d$Kampfzeit)\nsummary(d$Kampfzeit)",
 "Der Median der Kampfzeit beträgt 26.5 Minuten, der Interquartilsabstand 45.875 Minuten. Der Wertebereich ist [2.5, 90].",
 "R-Quantile weichen von der Vorlesungsdefinition (Teil A) ab – in Teil B immer den R-Befehl nehmen.")

card("Häufigkeiten und Modus", 60,
 "Bestimmen Sie die absoluten und relativen Häufigkeiten der Variable Monster. Welches Monster kommt am häufigsten vor? <span class='pt'>(3 P)</span>",
 ["<code>table()</code> = absolute Häufigkeiten. <code>prop.table(table())</code> = relative.", "Modus: <code>which.max(table(x))</code> oder <code>which(table(x) == max(table(x)))</code>.", "<code>sort()</code> sortiert, <code>unique()</code> = verschiedene Werte."],
 "table(d$Monster)\nround(prop.table(table(d$Monster)), 3)\nwhich.max(table(d$Monster))",
 "Am häufigsten kommt der Troll vor (4-mal, Anteil 0.333).")

card("Kennzahlen pro Gruppe", 60,
 "Berechnen Sie die durchschnittliche Anzahl an Münzen für jedes Tal. In welchem Tal verdient Jaskier im Durchschnitt am meisten? <span class='pt'>(3 P)</span>",
 ["<code>tapply(Zahl, Gruppe, Funktion)</code>.", "Alternative: <code>aggregate(d$Muenzen, by = list(d$Tal), mean)</code>."],
 "round(tapply(d$Muenzen, d$Tal, mean), 3)\naggregate(d$Muenzen, by = list(d$Tal), mean)",
 "Im Bergtal verdient Jaskier im Durchschnitt am meisten (26 Münzen).")

card("Klassen bilden mit cut", 45,
 "Ergänzen Sie d um die Variable Kampfzeit.3 mit den Ausprägungen {weniger als 5 Minuten, 5 Minuten bis weniger als eine Stunde, eine Stunde oder mehr} als Factor. Ergänzen Sie außerdem Muenzen.4 mit {bis 10, mehr als 10 bis 20, mehr als 20 bis 30, mehr als 30}. <span class='pt'>(4 P)</span>",
 ["<code>cut(x, breaks = Grenzen, right = …)</code>. Letzte Grenze <code>Inf</code>.",
  "„weniger als / bis unter“ → [a, b) → <code>right = FALSE</code>.", "„bis zu / höchstens / mehr als … bis …“ → (a, b] → <code>right = TRUE</code>.",
  "Einheit beachten: 1 Stunde = 60 Minuten.", "Optional: <code>labels = c(…)</code> für eigene Namen."],
 "d$Kampfzeit.3 <- cut(d$Kampfzeit, breaks = c(0, 5, 60, Inf), right = FALSE)\nd$Muenzen.4 <- cut(d$Muenzen, breaks = c(0, 10, 20, 30, Inf), right = TRUE)\ntable(d$Kampfzeit.3)\nis.factor(d$Kampfzeit.3)")

card("Kontingenztafel und bedingte Verteilung", 45,
 "Erstellen Sie die Kontingenztafel von Muenzen.4 und Kampfzeit.3. Wie häufig lag bei 5 bis unter 60 Minuten die Anzahl der Münzen in (10, 20]? Geben Sie die zeilenweise bedingte Verteilung an. <span class='pt'>(4 P)</span>",
 ["<code>table(Zeilen, Spalten)</code> = Kontingenztafel.", "Zelle ablesen: Zeile (10,20], Spalte [5,60).",
  "<code>prop.table(tafel, 1)</code> = zeilenweise, <code>prop.table(tafel, 2)</code> = spaltenweise, ohne Zahl = gesamt.", "<code>addmargins(tafel)</code> = mit Randsummen."],
 "Kontingenz.Tafel <- table(d$Muenzen.4, d$Kampfzeit.3)\nKontingenz.Tafel\naddmargins(Kontingenz.Tafel)\nround(prop.table(Kontingenz.Tafel, 1), 3)",
 "Bei einer Kampfzeit von 5 bis unter 60 Minuten lag die Anzahl der Münzen 2-mal zwischen 10 und 20.")

card("Randverteilung einer Teilgruppe", 35,
 "Betrachten Sie nur Kampfzeiten von mindestens 5 und unter 60 Minuten. Ermitteln Sie die relative Häufigkeit jeder Ausprägung von Muenzen.4 auf zwei Dezimalstellen. <span class='pt'>(3 P)</span>",
 ["Erst <code>subset()</code>, dann <code>prop.table(table())</code> auf die Teilgruppe."],
 "s <- subset(d, Kampfzeit >= 5 & Kampfzeit < 60)\nround(prop.table(table(s$Muenzen.4)), 2)",
 "(0,10]: 0.00 · (10,20]: 0.33 · (20,30]: 0.67 · (30,Inf]: 0.00.")

card("Korrelation und Kovarianz", 60,
 "Wie stark ist der lineare Zusammenhang zwischen Kampfzeit und Muenzen? Berechnen Sie zusätzlich Spearman und die Kovarianz. <span class='pt'>(4 P)</span>",
 ["<code>cor(x, y)</code> = Pearson (Standard). <code>cor(x, y, method = \"spearman\")</code>.", "<code>cov(x, y)</code> rechnet mit n − 1.",
  "Antwort: Stärke + Richtung + linear + Merkmale."],
 "round(cor(d$Kampfzeit, d$Muenzen), 3)\nround(cor(d$Kampfzeit, d$Muenzen, method = \"spearman\"), 3)\nround(cov(d$Kampfzeit, d$Muenzen), 3)\nround(cor(rank(d$Kampfzeit), rank(d$Muenzen)), 3)",
 "Der Korrelationskoeffizient nach Pearson beträgt 0.928; es besteht ein starker positiver linearer Zusammenhang zwischen Kampfzeit und Münzen.")

# ======================================================================
sec("4 · Grafiken erstellen und als Datei speichern")

card("Normiertes Histogramm als PDF", 85,
 "Erstellen Sie ein normiertes Histogramm der Variable Kampfzeit mit den Intervallen [0, 10), [10, 40), [40, 100). Titel „Sitz 17, Matr.Nr. 12345678, Aufgabenteil e)“, x-Achse „Kampfzeit in Minuten“, y-Achse „Dichte“. Speichern Sie die Grafik als Histogramm.pdf. <span class='pt'>(8 P)</span>",
 ["<code>pdf(\"Name.pdf\")</code> öffnet die Datei – <b>vor</b> dem Plot.", "<code>hist()</code> mit: <code>breaks</code> (Grenzen), <code>freq = FALSE</code> (normiert = Dichte), <code>right = FALSE</code> bei [a, b), <code>main</code>, <code>xlab</code>, <code>ylab</code>.",
  "<code>dev.off()</code> schließt und speichert – <b>nach</b> dem Plot.", "Datei im Ordner Dokumente prüfen und in ILIAS hochladen."],
 "pdf(\"Histogramm.pdf\")\nhist(d$Kampfzeit, breaks = c(0, 10, 40, 100), freq = FALSE, right = FALSE,\n     main = \"Sitz 17, Matr.Nr. 12345678, Aufgabenteil e)\",\n     xlab = \"Kampfzeit in Minuten\", ylab = \"Dichte\")\ndev.off()",
 None, "Ohne <code>freq = FALSE</code> zeigt R absolute Häufigkeiten (Säulendiagramm). <code>prob = TRUE</code> ist gleichwertig. Fehler „some 'x' not counted“ → breaks decken nicht alle Werte ab.",
 pdf="Histogramm.pdf")

card("Häufigkeiten eines Histogramms ohne Grafik", 25,
 "Lassen Sie sich die absoluten Häufigkeiten und Dichten der Klassen ausgeben, ohne die Grafik zu zeichnen. <span class='pt'>(2 P)</span>",
 ["<code>hist(…, plot = FALSE)</code> speichert die Kennzahlen.", "<code>$counts</code> = Anzahl pro Klasse, <code>$density</code> = Höhen, <code>cumsum()</code> = kumuliert."],
 "h <- hist(d$Kampfzeit, breaks = c(0, 10, 40, 100), right = FALSE, plot = FALSE)\nh$counts\nround(h$density, 4)\ncumsum(h$counts)")

card("Streudiagramm als PDF (auch als Lückentext)", 50,
 "Erstellen Sie ein Streudiagramm von Kampfzeit (x-Achse) und Muenzen (y-Achse) mit dem Titel „Streudiagramm“ und speichern Sie es als Streudiagramm.pdf. <span class='pt'>(5 P)</span>",
 ["<code>plot(x, y)</code>: erste Variable = x-Achse.", "<code>pch = 16</code> gefüllte Punkte, <code>cex</code> Punktgröße, <code>col</code> Farbe, <code>xlim</code>/<code>ylim</code> Achsenbereich.",
  "Lückentext Testat 2: <code>pdf</code> · <code>plot</code> · <code>d$Kampfzeit</code> · <code>d$Muenzen</code> · <code>main</code> · <code>xlab</code> · <code>\"Muenzen\"</code> · <code>dev</code>."],
 "pdf(\"Streudiagramm.pdf\")\nplot(d$Kampfzeit, d$Muenzen, pch = 16, cex = 1,\n     main = \"Streudiagramm\", xlab = \"Kampfzeit (min.)\", ylab = \"Muenzen\")\ndev.off()",
 None, "PNG statt PDF: <code>png(\"Name.png\", width = 2000, height = 2000, res = 400)</code> … <code>dev.off()</code>.", pdf="Streudiagramm.pdf")

card("Boxplot und Säulendiagramm", 35,
 "Erstellen Sie Boxplots der Münzen getrennt nach Tal und ein Säulendiagramm der Häufigkeiten der Monster. Geben Sie die Boxplot-Kennzahlen aus. <span class='pt'>(4 P)</span>",
 ["<code>boxplot(Zahl ~ Gruppe, data = d)</code> – Tilde ~ heißt „nach“.", "<code>boxplot(x, plot = FALSE)$stats</code> = unterer Whisker, Q1, Median, Q3, oberer Whisker.",
  "<code>barplot(table(d$Monster))</code> = Säulendiagramm für kategoriale Daten."],
 "pdf(\"Boxplot.pdf\")\nboxplot(Muenzen ~ Tal, data = d, main = \"Muenzen nach Tal\", xlab = \"Tal\", ylab = \"Muenzen\")\ndev.off()\nboxplot(d$Kampfzeit, plot = FALSE)$stats\nbarplot(table(d$Monster), main = \"Monster\", ylab = \"Anzahl\")",
 None, None, pdf="Boxplot.pdf")

card("Kerndichteschätzer (KDE)", 60,
 "Visualisieren Sie einen Kerndichteschätzer der Verteilung der Variable Dauer (Datensatz f). Titel mit Sitz, Matrikelnummer und Aufgabenteil, x-Achse „Dauer“, y-Achse „Dichte“. Speichern Sie die Grafik als KDE.pdf. <span class='pt'>(5 P)</span>",
 ["<code>density(x)</code> berechnet den KDE, <code>plot(density(x), …)</code> zeichnet ihn.", "Bandbreite: <code>bw = …</code> (klein → unruhig, groß → zu glatt). Kern: <code>kernel = \"epanechnikov\"</code> (Standard: \"gaussian\").",
  "Mit Histogramm kombinieren: erst <code>hist(…, freq = FALSE)</code>, dann <code>lines(density(x))</code>."],
 "pdf(\"KDE.pdf\")\nplot(density(f$Dauer), main = \"Sitz 17, Matr.Nr. 12345678, Aufgabenteil c)\",\n     xlab = \"Dauer\", ylab = \"Dichte\")\ndev.off()\ndensity(f$Dauer)$bw\nplot(density(f$Dauer, bw = 5, kernel = \"epanechnikov\"))",
 None, None, pdf="KDE.pdf")

card("Linien, Punkte, Kurven ergänzen", 35,
 "Zeichnen Sie ein normiertes Histogramm von Dauer und ergänzen Sie die Dichte einer Exponentialverteilung mit Rate 1/35.86 sowie eine senkrechte Linie beim Mittelwert. <span class='pt'>(4 P)</span>",
 ["Erst die Grundgrafik (hist, plot), dann ergänzen: <code>lines(x, y)</code>, <code>points(x, y)</code>, <code>abline(v = …)</code> (senkrecht), <code>abline(h = …)</code> (waagerecht), <code>curve(f(x), add = TRUE)</code>.",
  "x-Werte für eine Kurve: <code>seq(0, 120, by = 0.5)</code>.", "<code>ylim = c(0, …)</code>, damit die Kurve ganz sichtbar ist.", "Mehrere Grafiken nebeneinander: <code>par(mfrow = c(1, 2))</code>."],
 "pdf(\"HistDichte.pdf\")\nhist(f$Dauer, freq = FALSE, breaks = seq(0, 120, by = 15), ylim = c(0, 0.03),\n     main = \"Dauer mit Exponentialdichte\", xlab = \"Dauer\", ylab = \"Dichte\")\nx.seq <- seq(0, 120, by = 0.5)\nlines(x.seq, dexp(x.seq, rate = 1/35.86), col = 2)\nabline(v = mean(f$Dauer), lty = 2)\ndev.off()",
 None, None, pdf="HistDichte.pdf")

# ======================================================================
sec("5 · Verteilungen in R",
    "Für jede Verteilung gibt es vier Befehle: <b>d</b> = Wahrscheinlichkeit/Dichte P(X = x) bzw. f(x) · <b>p</b> = Verteilungsfunktion P(X ≤ x) · <b>q</b> = Quantil (umgekehrt zu p) · <b>r</b> = Zufallszahlen. "
    "Namen: binom, pois, unif, exp, norm, t, chisq, gamma.")

card("Binomialverteilung", 60,
 "X ~ Bin(n = 10, π = 0.3). Berechnen Sie P(X = 2), P(X ≤ 2), P(X &gt; 4), P(2 &lt; X ≤ 5) und den Median. <span class='pt'>(5 P)</span>",
 ["P(X = k) → <code>dbinom(k, size = n, prob = π)</code>.", "P(X ≤ k) → <code>pbinom(k, n, π)</code>.", "P(X &gt; k) → <code>1 - pbinom(k, n, π)</code>. P(X ≥ k) → <code>1 - pbinom(k - 1, n, π)</code>.",
  "P(a &lt; X ≤ b) → <code>pbinom(b, …) - pbinom(a, …)</code>.", "Quantil → <code>qbinom(0.5, n, π)</code>."],
 "dbinom(2, size = 10, prob = 0.3)\npbinom(2, 10, 0.3)\n1 - pbinom(4, 10, 0.3)\npbinom(5, 10, 0.3) - pbinom(2, 10, 0.3)\nqbinom(0.5, 10, 0.3)\ndbinom(0:3, 10, 0.3)",
 "P(X > 4) = 0.150.")

card("Poissonverteilung", 70,
 "Y ~ Po(λ = 2). Mittels welches R-Befehls lässt sich P(Y &gt; 2) berechnen? Berechnen Sie außerdem P(Y = 0) und P(Y ≤ 3). <span class='pt'>(3 P)</span>",
 ["<code>dpois(k, lambda)</code> = P(Y = k). <code>ppois(k, lambda)</code> = P(Y ≤ k).",
  "P(Y &gt; 2) = 1 − P(Y ≤ 2) = <code>1 - ppois(2, 2)</code> = <code>1 - dpois(0,2) - dpois(1,2) - dpois(2,2)</code>."],
 "1 - ppois(2, lambda = 2)\n1 - dpois(0, 2) - dpois(1, 2) - dpois(2, 2)\ndpois(0, 2)\nppois(3, 2)",
 "P(Y > 2) beträgt 0.323.",
 "Falsch wäre <code>1 - dpois(2, 2)</code> – das ist P(Y ≠ 2).")

card("Normalverteilung", 70,
 "X ~ N(μ = 500, σ = 5). Bestimmen Sie P(X &gt; 505), P(495 ≤ X ≤ 505), das 95 %-Quantil und P(X &gt; 505) über die Standardisierung. <span class='pt'>(4 P)</span>",
 ["<code>pnorm(x, mean = μ, sd = σ)</code> = P(X ≤ x). Achtung: <b>sd</b>, nicht Varianz!", "P(X &gt; x) = <code>1 - pnorm(x, μ, σ)</code>.",
  "Quantil: <code>qnorm(p, μ, σ)</code>.", "Standardisiert: <code>pnorm((x - μ) / σ)</code> (Standardnormalverteilung). Stetig: P(X &gt; x) = P(X ≥ x)."],
 "1 - pnorm(505, mean = 500, sd = 5)\npnorm(505, 500, 5) - pnorm(495, 500, 5)\nqnorm(0.95, 500, 5)\n1 - pnorm((505 - 500) / 5)\nqnorm(0.975)",
 "P(X > 505) beträgt 0.159.")

card("Gleich-, Exponential-, t-, χ²- und Gammaverteilung", 45,
 "Berechnen Sie (i) P(X ≤ 1.5) für X ~ U(0, 2), (ii) P(X ≤ 200) für X ~ Exp(0.006), (iii) das 97.5 %-Quantil der t-Verteilung mit 9 Freiheitsgraden, (iv) das 95 %-Quantil der χ²-Verteilung mit 29 FG, (v) P(X ≤ 3) für X ~ Gamma(2, 1). <span class='pt'>(5 P)</span>",
 ["<code>punif(x, min, max)</code> · <code>pexp(x, rate)</code> · <code>qt(p, df)</code> · <code>qchisq(p, df)</code> · <code>pgamma(x, shape, rate)</code>.",
  "Dichten mit d…, Quantile mit q…, Zufallszahlen mit r…."],
 "punif(1.5, min = 0, max = 2)\npexp(200, rate = 0.006)\nqt(0.975, df = 9)\nqchisq(0.95, df = 29)\npgamma(3, shape = 2, rate = 1)")

card("Zufallszahlen und Simulation (Lückentext Testat 4)", 40,
 "Vervollständigen Sie: <code>set.seed(123)</code> / <code>x &lt;- ___binom(10000, size = ___, prob = ___)</code> / <code>hist(x, prob = T, breaks = seq(-0.5, 5.5, by = 1))</code> für X ~ Bin(5, 0.3). Vergleichen Sie die simulierten Anteile mit dbinom. <span class='pt'>(3 P)</span>",
 ["<code>set.seed(Zahl)</code> = gleiche Zufallszahlen bei jedem Lauf (reproduzierbar).", "<code>r…</code> erzeugt Zufallszahlen: <code>rbinom(Anzahl, size, prob)</code>, <code>rpois</code>, <code>rnorm</code>, <code>runif</code>.",
  "<code>sample(1:6, 10, replace = TRUE)</code> = Würfelwürfe."],
 "set.seed(123)\nx <- rbinom(10000, size = 5, prob = 0.3)\nround(prop.table(table(x)), 3)\nround(dbinom(0:5, 5, 0.3), 3)\nsample(1:6, 10, replace = TRUE)",
 "Lücken: <code>r</code>, <code>5</code>, <code>0.3</code>.")

card("Wahrscheinlichkeitsfunktion / Dichte plotten", 25,
 "Stellen Sie die Wahrscheinlichkeitsfunktion von Po(3) für 0 bis 15 und die Dichte von N(0, 1) dar. <span class='pt'>(3 P)</span>",
 ["Diskret: <code>plot(werte, dpois(werte, 3), pch = 16)</code> (Punkte).", "Stetig: <code>plot(werte, dnorm(werte), type = \"l\")</code> (Linie), werte mit <code>seq()</code>."],
 "vals <- 0:15\nplot(vals, dpois(vals, 3), pch = 16, main = \"Po(3)\", xlab = \"x\", ylab = \"P(X = x)\")\nv <- seq(-3, 3, length.out = 200)\nplot(v, dnorm(v), type = \"l\", main = \"N(0,1)\", xlab = \"x\", ylab = \"Dichte\")")

# ======================================================================
sec("6 · Programmieren: Funktionen und Schleifen")

card("Eine Funktion schreiben", 60,
 "Schreiben Sie eine Funktion quadsum(x), welche die Summe der quadrierten Werte eines Vektors zurückgibt. Testen Sie sie mit 1:4. <span class='pt'>(3 P)</span>",
 ["Aufbau: <code>name &lt;- function(argumente) { … return(ergebnis) }</code>.", "Die Funktion erst ausführen (definieren), dann aufrufen: <code>quadsum(1:4)</code>."],
 "quadsum <- function(x) {\n  s <- sum(x^2)\n  return(s)\n}\nquadsum(1:4)")

card("for-Schleife", 50,
 "Berechnen Sie mit einer for-Schleife für λ = 1, …, 5 den Wert P(X = 3) mit X ~ Po(λ) und geben Sie jeweils „Lambda = … P = …“ aus. <span class='pt'>(3 P)</span>",
 ["<code>for (i in 1:5) { … }</code> – i nimmt nacheinander jeden Wert an.", "Ergebnisse speichern: vorher leeren Vektor anlegen <code>erg &lt;- numeric(5)</code>, in der Schleife <code>erg[i] &lt;- …</code>.",
  "Kürzer ohne Schleife: <code>sapply(1:5, function(l) dpois(3, l))</code> oder direkt <code>dpois(3, 1:5)</code>."],
 "erg <- numeric(5)\nfor (lambda in 1:5) {\n  erg[lambda] <- dpois(3, lambda)\n  cat(\"Lambda =\", lambda, \"P =\", round(erg[lambda], 3), \"\\n\")\n}\nwhich.max(erg)")

card("if / else und ifelse", 35,
 "Ersetzen Sie in x alle Werte größer als 10 durch 1 – einmal mit ifelse und einmal mit einer Funktion mit if/else. <span class='pt'>(3 P)</span>",
 ["<code>ifelse(Bedingung, wenn_ja, wenn_nein)</code> arbeitet mit dem ganzen Vektor.", "<code>if (Bedingung) { … } else { … }</code> prüft <b>einen</b> Wert → in einer Schleife benutzen."],
 "x <- c(4, 8, 15, 16, 23, 42)\nifelse(x > 10, 1, x)\nersetze <- function(v) {\n  for (i in 1:length(v)) {\n    if (v[i] > 10) { v[i] <- 1 } else { v[i] <- v[i] }\n  }\n  return(v)\n}\nersetze(x)")

card("Text-Funktion mit Schleife (Yennefer-Zahl, PK B h)", 20,
 "Schreiben Sie eine Funktion YenneferZahl.fun(n), welche „0.“ und alle natürlichen Zahlen von 1 bis n hintereinander schreibt. Geben Sie das Ergebnis für n = 17 an. <span class='pt'>(8 P)</span>",
 ["Start-Text <code>\"0.\"</code>. In der Schleife mit <code>paste0(alt, i)</code> anhängen.", "Am Ende <code>return()</code>."],
 "YenneferZahl.fun <- function(n) {\n  y <- \"0.\"\n  for (i in 1:n) {\n    y <- paste0(y, i)\n  }\n  return(y)\n}\nYenneferZahl.fun(17)",
 "Die Yennefer-Zahl bis n = 17 lautet 0.1234567891011121314151617.")

# ======================================================================
sec("7 · Maximum-Likelihood in R",
    "Idee: Die Likelihood L(θ) = Produkt der Einzelwahrscheinlichkeiten (diskret: d…-Funktion) bzw. Einzeldichten (stetig). Der ML-Schätzer ist der Parameterwert mit der größten Likelihood.")

card("Individuelle Likelihoods und Gesamt-Likelihood", 70,
 "Gehen Sie davon aus, dass Muenzen Poisson-verteilt ist, mit λ = 20. Ergänzen Sie d um die Spalte iL20 mit den individuellen Likelihoods und berechnen Sie die Likelihood aller Beobachtungen in der Form X × 10^Y (X auf drei Nachkommastellen). <span class='pt'>(6 P)</span>",
 ["Individuelle Likelihood = Wahrscheinlichkeit jeder Beobachtung: <code>dpois(d$Muenzen, 20)</code>.", "Gesamt = Produkt: <code>prod()</code>.",
  "Darstellung: R zeigt z. B. <code>4.104144e-20</code> = 4.104 × 10^(−20). Mit <code>signif(L, 4)</code> oder <code>format(L, digits = 4)</code>."],
 "d$iL20 <- dpois(d$Muenzen, lambda = 20)\nhead(d[, c(\"Muenzen\", \"iL20\")])\nL20 <- prod(d$iL20)\nL20\nformat(L20, digits = 4)",
 "Die Likelihood aller Beobachtungen unter λ = 20 beträgt L(λ = 20) = 4.104 × 10^(−20).")

card("Likelihood-Funktion und ML-Schätzer über einen Bereich", 70,
 "Schreiben Sie eine Funktion Likelihood.pois(lambda, x), welche die Likelihood für ein beliebiges λ bestimmt. Berechnen Sie die Likelihood für alle λ ∈ {17, …, 23} und bestimmen Sie daraus den ML-Schätzer. <span class='pt'>(9 P)</span>",
 ["Funktion: <code>prod(dpois(x, lambda))</code>.", "Für alle Werte: <code>for</code>-Schleife oder <code>sapply(17:23, …)</code>.", "Maximum: <code>which.max()</code> gibt die Position; Wert über den Vektor der λ.",
  "Kontrolle: Bei Poisson ist der ML-Schätzer = Mittelwert (22.083) → 22 passt."],
 "Likelihood.pois <- function(lambda, x) {\n  L <- prod(dpois(x, lambda))\n  return(L)\n}\nlambdas <- 17:23\nLs <- sapply(lambdas, Likelihood.pois, x = d$Muenzen)\nnames(Ls) <- lambdas\nLs\nlambdas[which.max(Ls)]",
 "Das Maximum der Likelihood ergibt sich bei λ = 22; der ML-Schätzer aus der gegebenen Menge ist λ̂ = 22.")

card("Log-Likelihood und numerical underflow", 50,
 "Warum ist es bei der direkten Optimierung der Likelihood in R problematisch? Wie umgeht man das Problem? Berechnen Sie die Log-Likelihood für λ = 22. <span class='pt'>(3 P)</span>",
 ["Viele kleine Wahrscheinlichkeiten multipliziert → Zahl so klein, dass R sie auf 0 rundet (numerical underflow).", "Lösung: Logarithmus → Summe statt Produkt: <code>sum(log(dpois(x, λ)))</code> bzw. <code>sum(dpois(x, λ, log = TRUE))</code>.",
  "Das Maximum liegt an derselben Stelle (log ist monoton)."],
 "prod(dpois(rep(d$Muenzen, 40), 22))\nsum(log(dpois(d$Muenzen, 22)))\nsum(dpois(d$Muenzen, 22, log = TRUE))",
 "Bei der direkten Optimierung tritt numerical underflow auf: Das Produkt sehr kleiner Werte wird zu 0 gerundet. Deshalb maximiert man die Log-Likelihood (Summe der logarithmierten Werte).")

card("ML-Schätzer mit optimise (ein Parameter)", 40,
 "Bestimmen Sie den ML-Schätzer für λ der Poissonverteilung numerisch im Intervall [10, 40]. <span class='pt'>(4 P)</span>",
 ["<code>optimise(funktion, interval = c(a, b), daten, maximum = TRUE)</code> sucht das Maximum für <b>einen</b> Parameter.",
  "Ergebnis: <code>$maximum</code> = Schätzer, <code>$objective</code> = Funktionswert."],
 "logL.pois <- function(lambda, x) sum(log(dpois(x, lambda)))\nopt <- optimise(logL.pois, interval = c(10, 40), x = d$Muenzen, maximum = TRUE)\nround(opt$maximum, 3)",
 "Der ML-Schätzer für λ beträgt 22.083 (= Mittelwert der Münzen).")

card("ML mit nlm (zwei Parameter, Gamma-Verteilung)", 45,
 "Die Dauer (Datensatz f) sei Gamma(α, β)-verteilt. Warum müssen die Parameter für nlm transformiert werden? Schreiben Sie die Funktion neglogL und schätzen Sie α und β mit nlm (Startwerte 1 und 0.1). Geben Sie die rücktransformierten Schätzer an. <span class='pt'>(10 P)</span>",
 ["<code>nlm()</code> <b>minimiert</b> → negative Log-Likelihood benutzen.", "α, β &gt; 0, aber nlm probiert alle reellen Zahlen → Transformation: param = <code>exp(t_param)</code>; Startwerte mit <code>log()</code> übergeben.",
  "Funktion: param &lt;- exp(t) · alpha &lt;- param[1] · beta &lt;- param[2] · −sum(log(dgamma(x, alpha, beta))).",
  "<code>model &lt;- nlm(neglogL, log(c(1, 0.1)), x)</code>. Schätzer: <code>exp(model$estimate)</code>. Warnungen während der Iteration sind meist harmlos."],
 "x <- f$Dauer\nneglogL <- function(t_param, x) {\n  param <- exp(t_param)\n  alpha <- param[1]\n  beta <- param[2]\n  return(-sum(log(dgamma(x, alpha, beta))))\n}\nmodel <- nlm(neglogL, log(c(1, 0.1)), x)\nround(exp(model$estimate), 3)",
 "Die Parameter der Gammaverteilung sind positiv, nlm optimiert aber über alle reellen Zahlen; daher werden sie mit exp() transformiert. Die rücktransformierten Schätzer betragen α̂ = 2.453 und β̂ = 0.068.")

card("Geschätzte Verteilung nutzen", 40,
 "Zeichnen Sie das normierte Histogramm von Dauer mit der geschätzten Gammadichte. Wie groß ist P(Dauer ≤ 30) laut Modell? Ab welcher Dauer gehört man zu den 25 % längsten Ausleihen? <span class='pt'>(6 P)</span>",
 ["Kurve: <code>lines(x.seq, dgamma(x.seq, alpha.hat, beta.hat))</code>.", "Wahrscheinlichkeit: <code>pgamma()</code>. Grenze der obersten 25 %: <code>qgamma(0.75, …)</code>."],
 "alpha.hat <- exp(model$estimate[1])\nbeta.hat <- exp(model$estimate[2])\npdf(\"Gamma.pdf\")\nhist(x, freq = FALSE, breaks = seq(0, 120, by = 10), ylim = c(0, 0.025),\n     main = \"Grafik Aufgabenteil k)\", xlab = \"Dauer\", ylab = \"Dichte\")\nx.seq <- seq(0, 120, by = 0.5)\nlines(x.seq, dgamma(x.seq, alpha.hat, beta.hat), col = 2)\ndev.off()\nround(pgamma(30, alpha.hat, beta.hat), 3)\nround(qgamma(0.75, alpha.hat, beta.hat), 3)",
 "Laut Modell beträgt P(Dauer ≤ 30) 0.478. Ab 47.586 Minuten gehört eine Ausleihe zu den 25 % längsten.",
 None, pdf="Gamma.pdf")

# ======================================================================
sec("8 · Konfidenzintervalle und Tests in R")

card("Konfidenzintervall für μ (σ bekannt und unbekannt)", 55,
 "Für die Münzen (n = 12) berechnen Sie ein 90 %-Konfidenzintervall für μ (i) mit bekanntem σ = 7, (ii) mit unbekanntem σ. <span class='pt'>(5 P)</span>",
 ["σ bekannt: x̄ ± <code>qnorm(1 - alpha/2)</code> · σ/√n.", "σ unbekannt: x̄ ± <code>qt(1 - alpha/2, n - 1)</code> · s/√n mit <code>s = sd(x)</code>.", "Ergebnis immer als Intervall [unten, oben] angeben."],
 "x <- d$Muenzen\nn <- length(x)\nalpha <- 0.1\nround(mean(x) + c(-1, 1) * qnorm(1 - alpha/2) * 7 / sqrt(n), 3)\nround(mean(x) + c(-1, 1) * qt(1 - alpha/2, n - 1) * sd(x) / sqrt(n), 3)",
 "Das 90 %-Konfidenzintervall für μ (σ unbekannt) lautet [18.303, 25.864].")

card("Konfidenzintervall für Anteil und Varianz", 30,
 "(i) Von 100 Befragten sagen 40 „ja“. 95 %-KI für den Anteil π. (ii) 95 %-KI für die Varianz der Münzen. <span class='pt'>(4 P)</span>",
 ["Anteil: π̂ ± <code>qnorm(1 - alpha/2)</code> · √(π̂(1 − π̂)/n).", "Varianz: [(n−1)s²/<code>qchisq(1 - alpha/2, n-1)</code>, (n−1)s²/<code>qchisq(alpha/2, n-1)</code>]."],
 "p <- 40/100\nround(p + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / 100), 3)\ns2 <- var(d$Muenzen)\nround(c((n - 1) * s2 / qchisq(0.975, n - 1), (n - 1) * s2 / qchisq(0.025, n - 1)), 3)")

card("t-Test mit t.test und Output lesen", 55,
 "Testen Sie zum Niveau α = 0.1, ob die mittlere Anzahl Münzen größer als 20 ist. Stellen Sie die Hypothesen auf, geben Sie Prüfgröße, Ablehnungsbereich, p-Wert und Testentscheidung an. <span class='pt'>(6 P)</span>",
 ["Hypothesen: H0: μ ≤ 20 gegen H1: μ &gt; 20.", "<code>t.test(x, mu = 20, alternative = \"greater\", conf.level = 0.9)</code>. Zweiseitig: <code>\"two.sided\"</code>, links: <code>\"less\"</code>.",
  "Output: <code>t</code> = Prüfgröße, <code>df</code> = Freiheitsgrade, <code>p-value</code>.", "Ablehnungsbereich (rechts): (<code>qt(1 - alpha, n - 1)</code>, ∞).", "Entscheidung: p-Wert &lt; α → H0 ablehnen."],
 "tt <- t.test(d$Muenzen, mu = 20, alternative = \"greater\", conf.level = 0.9)\ntt\nround(qt(0.9, df = 11), 3)\nround(tt$statistic, 3)\nround(tt$p.value, 3)",
 "H0: μ ≤ 20, H1: μ > 20. Die Prüfgröße t = 0.99 liegt nicht im Ablehnungsbereich (1.363, ∞); der p-Wert 0.172 ist größer als α = 0.1. H0 wird nicht abgelehnt.")

card("Test von Hand mit qnorm/qt/pnorm", 35,
 "Daten 19.2, 17.4, 18.5, 16.5, 18.9; H0: μ = 17, σ² = 2.25 bekannt, α = 0.01 (zweiseitig). Berechnen Sie z, die kritischen Werte und den p-Wert. <span class='pt'>(4 P)</span>",
 ["z = (x̄ − μ0)/(σ/√n).", "Kritische Werte: <code>qnorm(alpha/2)</code> und <code>qnorm(1 - alpha/2)</code>.", "p-Wert zweiseitig: <code>2 * (1 - pnorm(abs(z)))</code>. σ unbekannt → <code>qt</code>/<code>pt</code> mit n − 1."],
 "y <- c(19.2, 17.4, 18.5, 16.5, 18.9)\nz <- (mean(y) - 17) / (sqrt(2.25) / sqrt(length(y)))\nround(z, 3)\nround(qnorm(c(0.005, 0.995)), 3)\nround(2 * (1 - pnorm(abs(z))), 3)",
 "z = 1.64 liegt nicht im Ablehnungsbereich (−∞, −2.576) ∪ (2.576, ∞); p = 0.101 > 0.01 → H0 wird nicht abgelehnt.")

card("Binomialtest über pbinom", 30,
 "Bei 20 Münzwürfen fällt 15-mal Kopf. Berechnen Sie den p-Wert für H0: π = 0.5 gegen H1: π &gt; 0.5. <span class='pt'>(2 P)</span>",
 ["p-Wert = P(X ≥ 15) unter H0 = <code>1 - pbinom(14, 20, 0.5)</code> = <code>sum(dbinom(15:20, 20, 0.5))</code>."],
 "1 - pbinom(14, 20, 0.5)\nsum(dbinom(15:20, 20, 0.5))",
 "Der p-Wert beträgt 0.021; zum Niveau 5 % wird H0 abgelehnt.")

card("χ²-Unabhängigkeitstest mit chisq.test", 40,
 "Testen Sie mit der Kontingenztafel (Rauchen × Sport: 15, 75, 45, 65), ob Rauchen und Sport unabhängig sind (α = 0.05). Geben Sie die erwarteten Häufigkeiten, die Prüfgröße und den p-Wert an. <span class='pt'>(5 P)</span>",
 ["Tafel als Matrix: <code>matrix(c(…), nrow = 2)</code> (spaltenweise!).", "<code>chisq.test(tafel, correct = FALSE)</code> (ohne Korrektur = wie in der Vorlesung von Hand).",
  "<code>$expected</code>, <code>$statistic</code>, <code>$p.value</code>.", "Mit Daten: <code>chisq.test(table(d$X, d$Y))</code>."],
 "tafel <- matrix(c(15, 75, 45, 65), nrow = 2)\ntest <- chisq.test(tafel, correct = FALSE)\ntest$expected\nround(test$statistic, 3)\nround(test$p.value, 4)",
 "Die Prüfgröße beträgt χ² = 13.853, der p-Wert 0.0002 < 0.05. H0 (Unabhängigkeit) wird abgelehnt; Rauchen und Sport hängen zusammen.",
 "Bei 2×2-Tafeln nutzt R ohne <code>correct = FALSE</code> die Yates-Korrektur – dann weicht der Wert vom Handergebnis ab.")

# ======================================================================
sec("9 · Fehler finden und Klausur-Ablauf")

card("Typische Fehlermeldungen", 40,
 "Erklären Sie die Fehler: (i) „kann Datei nicht öffnen“, (ii) „Objekt 'd' nicht gefunden“, (iii) „unerwartetes Symbol“, (iv) Mittelwert ist NA, (v) Zahlen sind chr. <span class='pt'>(–)</span>",
 ["(i) Datei nicht im Working Directory oder Name falsch → <code>list.files()</code>.", "(ii) Objekt wurde nie erstellt (Zeile davor hatte einen Fehler) oder falsch geschrieben.",
  "(iii) Komma, Klammer oder Anführungszeichen fehlt.", "(iv) NA in den Daten → <code>na.rm = TRUE</code>.", "(v) <code>dec</code> falsch → neu einlesen mit richtigem dec.",
  "Gegen Fehler: Klammern zählen, Anführungszeichen paarweise, Groß-/Kleinschreibung prüfen, <code>?befehl</code> öffnet die Hilfe."],
 None, None, None, run=False)

card("Ablauf in der Klausur (60 Minuten)", 100,
 "So gehst du in Teil B vor. <span class='pt'>(45 P)</span>",
 ["Minute 0–3: Datei in Dokumente ansehen (sep/dec), Skript öffnen und speichern.", "Pro Teilaufgabe: Code ins Skript, Strg + Enter, Output prüfen.",
  "Kästchen 1: Code + Output aus der Console kopieren. Kästchen 2: Satz mit 3 Nachkommastellen.", "Grafik: pdf() … dev.off(), Titel mit Sitz, Matr.Nr., Aufgabenteil, Datei hochladen.",
  "Hängst du fest: Ersatzobjekt erzeugen und weiter (Folgefehler werden gewertet). Falschen Code aus der Antwort löschen.", "Letzte 5 Minuten: alle Kästchen gefüllt? Alle Dateien hochgeladen?"],
 None, None, None, run=False)

# ======================================================================
# R ausführen
script = ['options(width = 90)']
for i, c in enumerate(C):
    if c["kind"] == "card" and c["code"] and c["run"]:
        script.append('cat("@@CARD%d@@\\n")' % i)
        script.append(c["code"])
script.append('cat("@@END@@\\n")')
open(os.path.join(WORK, "kurs.R"), "w").write("\n".join(script) + "\n")
env = dict(os.environ, HOME=WORK, LANG="de_DE.UTF-8", LANGUAGE="de")
res = subprocess.run(["R", "--no-save", "--quiet"], input="\n".join(script) + "\n", text=True,
                     capture_output=True, cwd=WORK, env=env)
out = res.stdout + res.stderr
parts = re.split(r'> cat\("@@CARD(\d+)@@\\n"\)\n@@CARD\d+@@\n', out)
outputs = {}
for j in range(1, len(parts), 2):
    k = int(parts[j]); txt = parts[j + 1]
    txt = re.split(r'> cat\("@@CARD|> cat\("@@END', txt)[0]
    outputs[k] = txt.rstrip()

# PDFs zu Bildern
def pdf2png(name):
    p = os.path.join(WORK, name)
    if not os.path.exists(p): return None
    pix = pymupdf.open(p)[0].get_pixmap(dpi=60)
    outn = "rk_" + name.replace(".pdf", ".png")
    pix.save(os.path.join(FIG, outn)); return outn

def esc(s): return html.escape(s, quote=False)

H = ['<section class="t5">',
     '<div class="fs-kopf"><h1>R-Komplettkurs für Teil B · im Klausurformat</h1>',
     '<p>Von null bis zur Klausur an einem Tag. Jede Karte: <b>Aufgabe</b> (wie in der Klausur) → <b>So löst du es</b> → <b>Kästchen 1: R-Code und R-Output</b> (echt, aus R) → <b>Kästchen 2: Antwortsatz</b>. '
     'Tippe jeden Code selbst in RStudio ab. Daten: Taverne.csv (Objekt d) und Fahrrad.csv (Objekt f) aus dem Ordner uebungsdaten – kopiere sie in deinen Ordner Dokumente.</p></div>',
     '<div class="legend"><b>Prozent</b> = geschätzte Wahrscheinlichkeit, dass dieser Aufgabentyp in Teil B (oder als R-Frage in Teil A) vorkommt – nach Probeklausur B 2022, ML-Übungsklausur B, Testaten und R-Skripten der Vorlesung. '
     '<span class="ol hi">≥ 70 %</span> fast sicher · <span class="ol mid">30–69 %</span> häufig · <span class="ol lo">&lt; 30 %</span> manchmal. '
     '<br><b>Tagesplan:</b> 09–10 Abschnitt 0–2 · 10–12 Abschnitt 3–4 · 13–14 Abschnitt 5 · 14–16 Abschnitt 6–7 · 16–17 Abschnitt 8 · 17–18 Probeklausur Teil B auf Zeit.</div>']
for i, c in enumerate(C):
    if c["kind"] == "sec":
        H.append('<h2 class="rzh">%s</h2>' % c["t"])
        if c["intro"]: H.append('<p class="small" style="margin:.2em 0 .5em">%s</p>' % c["intro"])
        continue
    p = c["p"]; cl = "hi" if p >= 70 else "mid" if p >= 30 else "lo"
    s = ['<div class="rz"><div class="q"><span>%s</span><span class="ol %s">~%d %%</span></div><div class="b">' % (c["title"], cl, p)]
    s.append('<div class="auf"><b>Aufgabe.</b> %s</div>' % c["auf"])
    s.append('<div class="yap" style="grid-column:1/-1"><b class="l">So löst du es</b><ol>%s</ol></div>' % "".join("<li>%s</li>" % x for x in c["steps"]))
    if c["code"]:
        o = outputs.get(i, "") if c["run"] else ""
        body = esc(o) if o else esc(c["code"])
        s.append('<div class="lk2" style="grid-column:1/-1"><b style="font-size:.7rem;color:#64748b">Kästchen 1 · R-Code und R-Output</b><pre class="out" style="margin:.2em 0">%s</pre></div>' % body)
    if c["satz"]:
        s.append('<div class="lk2" style="grid-column:1/-1"><b style="font-size:.7rem;color:#64748b">Kästchen 2 · Antwortsatz</b><br>%s</div>' % c["satz"])
    if c["warn"]: s.append('<div class="dikkat">%s</div>' % c["warn"])
    if c["pdf"]:
        png = pdf2png(c["pdf"])
        if png: s.append('<div class="fig"><img src="fig/%s" style="width:42%%"><div class="small muted">Inhalt der Datei %s</div></div>' % (png, c["pdf"]))
    s.append('</div></div>')
    H.append("\n".join(s))
H.append("</section>")
open(os.path.join(SRC, "content", "rkurs.html"), "w", encoding="utf-8").write("\n".join(H))
print(sum(1 for c in C if c["kind"] == "card"), "Karten;", len(outputs), "Outputs")
errs = [k for k, v in outputs.items() if "Fehler" in v or "Error" in v]
print("Karten mit Fehlern:", errs)
