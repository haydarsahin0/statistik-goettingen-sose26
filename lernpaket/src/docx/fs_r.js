// Formelsammlung R (Teil B) als Word-Datei
const path = require('path');
const { Book } = require('./fslib');
const B = new Book('Formelsammlung R (Teil B)');

B.cover('Formelsammlung R', 'Teil B · ILIAS-Klausur am Computer · Statistik und Data Science I · Göttingen', [
  '**Aufbau:** Von den Grundlagen bis zu Likelihood und Tests – in der Reihenfolge, in der die Teilaufgaben in der Klausur typischerweise kommen.',
  '**Farbige Kästen:** ★ gelb = Punkte-Retter · ✎ grün = Antwortsatz für ILIAS · ⚠ rot = typische Falle · ➜ blau = Rezept · TR = Türkische Erklärung.',
  '**Code-Kästen:** dunkler Hintergrund = R-Code; Zeilen mit # sind Kommentare, Zeilen mit [1] zeigen den Output.',
  '**Kapitel 15** enthält ein komplettes Musterskript für eine ganze Teil-B-Klausur – als Vorlage zum Abtippen und Anpassen.',
]);
B.toc(['0  Ablauf Teil B & Punkte-Retter', '1  R-Grundlagen: Objekte, Vektoren, Indizes', '2  Datentypen & Objekttypen', '3  Working Directory & Daten einlesen', '4  Data Frames bearbeiten',
  '5  Deskriptive Statistik', '6  Grafiken (Histogramm, Boxplot, Streudiagramm, …) & als PDF speichern', '7  Zusammenhänge: Tabellen, Korrelation, Regression', '8  Verteilungen: d-, p-, q-, r-Funktionen',
  '9  Simulation & Zufallszahlen', '10 Likelihood & Maximum-Likelihood in R', '11 Eigene Funktionen, Schleifen, Text', '12 Kerndichteschätzer', '13 Konfidenzintervalle & Tests in R',
  '14 Fehlermeldungen & Rettung', '15 Komplettes Musterskript einer Teil-B-Klausur', '16 Antwortsatz-Vorlagen']);

// ───────────────── 0
B.h1('0  Ablauf Teil B & Punkte-Retter');
B.h2('So ist jede Teilaufgabe in ILIAS aufgebaut');
B.ul(['**Box 1: R-Code + R-Output** (aus der Konsole kopieren, mit `>` vor dem Code und dem `[1] …` Output).', '**Box 2: inhaltliche Antwort** in vollen Sätzen, OHNE Code (nur wenn gefragt).',
  'Grafiken: als PDF speichern und hochladen; Titel mit `main` = Sitz, Matrikelnummer, Aufgabenteil; Achsen beschriften.', 'Ergebnisse auf **3 Nachkommastellen** mit `round(…, 3)` runden – auch im Antwortsatz.', 'Falschen Code, der nicht zur Antwort gehört, aus der ILIAS-Box löschen.']);
B.box('retter', 'Code immer abgeben – auch wenn er einen Fehler wirft. Ein richtiger Ansatz (z. B. `hist(d$Dauer, freq = FALSE, …)`) bringt Teilpunkte.',
  'Folgefehler werden berücksichtigt: Fehlt ein Objekt aus einer früheren Teilaufgabe, erzeuge es anders (z. B. Werte von Hand mit `c(…)`) und rechne weiter.',
  'Datensatz lässt sich nicht einlesen? Trotzdem alle Befehle mit `d$Variable` hinschreiben – so steht es in den Hinweisen.',
  'Antwortsatz = Frage wiederholen + Zahl mit 3 Nachkommastellen + Einheit/Sachzusammenhang.', 'Regelmäßig speichern (Skript + ILIAS)!');
B.box('tipp', 'Arbeitsweise: 1) Neues R-Skript im Ordner Dokumente anlegen.  2) Jede Teilaufgabe als Abschnitt `## e)` im Skript.  3) Code mit Strg+Enter ausführen.  4) Code + Output aus der Konsole nach ILIAS kopieren.  5) Antwortsatz schreiben.');
B.box('tr', 'Her alt soruda iki kutu var: (1) kod + çıktı, (2) cümleyle cevap. Hata alsan bile kodu yaz, yarım puan gelir. Sayıları round(…, 3) ile yuvarla.');

// ───────────────── 1
B.h1('1  R-Grundlagen: Objekte, Vektoren, Indizes');
B.code(['x <- c(4, 8, 15, 16, 23, 42)   # Vektor erzeugen (Zuweisung mit <-)', 'x[2]                            # 2. Element', '[1] 8', 'x[c(1, 3)]                      # 1. und 3. Element', 'x[-1]                           # alle außer dem 1.',
  'x[x > 10]                       # logische Auswahl', '[1] 15 16 23 42', 'length(x); sum(x); prod(x)', 'seq(0, 1, by = 0.25)            # 0.00 0.25 0.50 0.75 1.00', 'seq(17, 23)    # oder 17:23', 'rep(1, 5)                       # 1 1 1 1 1',
  'sort(x); rev(x); order(x)       # sortieren, umdrehen, Reihenfolge-Index', 'x^2; sqrt(x); log(x); exp(x)    # elementweise', 'which(x == 16)                  # Position: 4', 'which.max(x); which.min(x)']);
B.table(['Operator', 'Bedeutung'], [['==  !=', 'gleich / ungleich'], ['<  <=  >  >=', 'Vergleiche'], ['&  |  !', 'und / oder / nicht'], ['%in%', 'ist enthalten in, z. B. d$Fach %in% c("Jura", "Wiwi")'], ['<-', 'Zuweisung'], ['#', 'Kommentar']], [2, 7]);
B.box('falle', 'R unterscheidet Groß/Kleinschreibung: `d$Dauer` ≠ `d$dauer`.  ·  Dezimalpunkt: 2.5, nicht 2,5.  ·  Text in Anführungszeichen: "Jura".');

// ───────────────── 2
B.h1('2  Datentypen & Objekttypen');
B.table(['Typ', 'Beispiel', 'class()', 'typeof()'], [['ganze Zahl', '3L, Spalte mit nur ganzen Zahlen aus read.csv', 'integer', 'integer'], ['Kommazahl', '2.5', 'numeric', 'double'], ['Text', '"Jura"', 'character', 'character'],
  ['Kategorie', 'factor(c("a","b"))', 'factor', 'integer'], ['Wahrheitswert', 'TRUE, FALSE', 'logical', 'logical'], ['Tabelle', 'd <- read.csv(…)', 'data.frame', 'list'], ['Matrix', 'matrix(1:6, nrow = 2)', 'matrix array', 'integer']], [2, 3.5, 2, 2]);
B.code(['class(d$Studio)        # [1] "character"', 'class(d$Besuche)       # [1] "integer"', 'typeof(d$Minuten)      # [1] "integer" bzw. "double"', 'str(d)                 # Überblick über alle Variablen und Typen',
  'd$Studio <- as.factor(d$Studio)       # in Faktor umwandeln', 'as.numeric("3.5")                     # Text -> Zahl', 'levels(d$Studio)                      # Kategorien eines Faktors']);
B.box('satz', '„Die Variable Studio ist ein Objekt vom Typ character (Text), die Variable Besuche ist ein numerisches Objekt vom Typ integer, d. h. sie enthält nur ganze Zahlen.“');
B.box('retter', 'Bei „Objekttyp ermitteln“ immer einen Befehl (class/typeof/str) zeigen UND den Typ im Satz nennen – beides gibt Punkte.');

// ───────────────── 3
B.h1('3  Working Directory & Daten einlesen');
B.code(['setwd(path.expand("~"))      # in der Klausur: Ordner Dokumente', 'getwd()                      # prüfen, wo man ist', 'list.files()                 # liegt die CSV-Datei hier?',
  'd <- read.csv("Fitness.csv", sep = ",", dec = ".", header = TRUE)', '# Semikolon-getrennt mit Dezimalkomma:', 'd <- read.csv("Daten.csv", sep = ";", dec = ",")   # oder read.csv2("Daten.csv")',
  'd <- read.table("data.csv", sep = ";", header = TRUE)', 'head(d)      # erste 6 Zeilen   ·   head(d, 10) erste 10', 'tail(d); dim(d); nrow(d); ncol(d); names(d); summary(d)']);
B.box('tipp', 'Erst die CSV-Datei mit einem Texteditor ansehen: Trennzeichen „,“ oder „;“? Dezimal „.“ oder „,“? Kopfzeile vorhanden? → dann sep, dec, header passend setzen.');
B.box('falle', 'Wenn head(d) nur EINE Spalte mit allen Werten zeigt, ist sep falsch.  ·  Zahlen als character eingelesen → dec falsch.  ·  Dateiname exakt (Groß-/Kleinschreibung, .csv).');

// ───────────────── 4
B.h1('4  Data Frames bearbeiten');
B.code(['d$Minuten                         # eine Spalte (Vektor)', 'd[3, ]                            # 3. Zeile', 'd[, 2]                            # 2. Spalte', 'd[d$Studio == "Nord", ]           # nur Zeilen von Studio Nord',
  'subset(d, Abo == "Premium" & Minuten > 60)', 'd$Stunden <- d$Minuten / 60       # neue Spalte', 'd$lang <- ifelse(d$Minuten > 70, "ja", "nein")', 'mean(d$Minuten[d$Abo == "Premium"])   # Mittel einer Teilgruppe',
  'sum(d$Abo == "Premium")           # Anzahl Premium (TRUE zählt 1)', 'mean(d$Abo == "Premium")          # Anteil Premium', 'd <- d[order(d$Minuten), ]        # nach Minuten sortieren', 'na.omit(d)                        # Zeilen mit NA entfernen']);

// ───────────────── 5
B.h1('5  Deskriptive Statistik');
B.table(['Kennzahl', 'R-Befehl', 'Achtung'], [
  ['arithm. Mittel', 'mean(x)', 'bei NA: mean(x, na.rm = TRUE)'], ['Median', 'median(x)', ''], ['Modus', 'names(which.max(table(x)))', 'oder table(x) ansehen'],
  ['Quantile', 'quantile(x, c(0.25, 0.75))', 'type = 7 Standard; Vorlesungsdefinition ≈ type = 2'], ['Interquartilsabstand', 'IQR(x)', 'mit R-Standard (type 7)'], ['Min, Max, Spannweite', 'min(x), max(x), diff(range(x))', ''],
  ['Varianz s*² (n−1)', 'var(x)', 'unverzerrt!'], ['Standardabw. s* (n−1)', 'sd(x)', 'unverzerrt!'], ['Varianz s² (1/n)', 'mean((x - mean(x))^2)  oder  var(x)*(n-1)/n', 'falls „empirische Varianz“ verlangt'],
  ['5-Punkte-Zusammenfassung', 'summary(x)', 'Min, Q1, Median, Mean, Q3, Max'], ['Häufigkeiten', 'table(x)', 'absolut'], ['relative Häufigkeiten', 'prop.table(table(x))', ''], ['kumuliert', 'cumsum(prop.table(table(x)))', ''],
  ['Gruppenmittel', 'tapply(d$Minuten, d$Studio, mean)', 'oder aggregate(Minuten ~ Studio, data = d, FUN = mean)'], ['Runden', 'round(x, 3)', 'immer 3 Nachkommastellen']], [2.6, 4.4, 3.4]);
B.code(['round(mean(d$Minuten), 3)', '[1] 68.275', 'round(sd(d$Minuten), 3)', '[1] 13.807', 'tapply(d$Minuten, d$Studio, median)', 'round(quantile(d$Minuten, c(0.25, 0.5, 0.75)), 3)']);
B.box('satz', '„Das arithmetische Mittel der Variable Minuten beträgt 68.275. Der unverzerrte Schätzer für die Standardabweichung beträgt 13.807.“');
B.box('falle', 'sd() und var() teilen durch n−1 (= s*). „Unverzerrte Standardabweichung“ → sd(). „Empirische Varianz mit 1/n“ → von Hand.  ·  Gerundet nur das ENDergebnis.');

// ───────────────── 6
B.h1('6  Grafiken & als PDF speichern');
B.h2('Rahmen zum Speichern (immer gleich)');
B.code(['pdf("Histogramm.pdf")          # Datei öffnen (im Working Directory)', '  ... Grafikbefehl ...', 'dev.off()                      # Datei schließen – sonst ist das PDF leer!']);
B.h2('Histogramm mit vorgegebenen Klassen');
B.code(['pdf("Histogramm.pdf")', 'hist(d$Dauer,', '     breaks = c(0, 1, 2, 3, 5, 8),   # Klassengrenzen', '     right = FALSE,                  # Intervalle [a, b): links geschlossen', '     freq = FALSE,                   # y-Achse = Dichte',
  '     main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil e)",', '     xlab = "Aufenthaltsdauer in Stunden",', '     ylab = "Dichte")', 'dev.off()']);
B.box('falle', 'Ungleich breite Klassen → freq = FALSE (Dichte), sonst falsches Bild.  ·  [a, b) → right = FALSE; (a, b] → right = TRUE (Standard).  ·  Alle Daten müssen in den breaks liegen, sonst Fehler „some x not counted“.');
B.h2('Boxplot (auch nach Gruppen)');
B.code(['pdf("Boxplot.pdf")', 'boxplot(Minuten ~ Studio, data = d,', '        main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil e)",', '        xlab = "Studio", ylab = "Trainingsdauer in Minuten")', 'dev.off()', 'boxplot(d$Minuten, horizontal = TRUE)   # ein einzelner Boxplot']);
B.h2('Weitere Grafiken');
B.code(['plot(d$Minuten, d$Wartezeit, xlab = "…", ylab = "…", main = "…")   # Streudiagramm', 'abline(lm(Wartezeit ~ Minuten, data = d), col = "red")          # Regressionsgerade einzeichnen',
  'barplot(table(d$Studio), main = "…", xlab = "Studio", ylab = "Anzahl")', 'plot(ecdf(d$Minuten), main = "…", xlab = "…", ylab = "F(x)")      # empirische Verteilungsfunktion',
  'plot(density(d$Minuten), main = "…")                              # Kerndichteschätzer', 'curve(dnorm(x, 68, 14), from = 30, to = 110, add = TRUE, col = "blue")  # Dichte darüber',
  'lines(density(d$Minuten), col = "red")                            # Linie zu bestehendem Plot', 'legend("topright", legend = c("KDE", "Normal"), col = c("red", "blue"), lty = 1)', 'par(mfrow = c(1, 2))                                              # 2 Grafiken nebeneinander']);
B.box('retter', 'Titel und Achsenbeschriftung sind fast immer eigene Punkte: main = "Sitz …, Matr.Nr. …, Aufgabenteil …", xlab, ylab GENAU wie in der Aufgabe.',
  'PDF leer/fehlt? Grafik im Plot-Fenster über „Export → Save as PDF“ speichern – gibt ebenfalls Punkte.');

// ───────────────── 7
B.h1('7  Zusammenhänge: Tabellen, Korrelation, Regression');
B.code(['tab <- table(d$Studio, d$Abo)          # Kontingenztabelle (absolut)', 'tab', 'addmargins(tab)                        # mit Randsummen', 'prop.table(tab)                        # relative Häufigkeiten (gesamt)',
  'round(prop.table(tab, margin = 1), 3)  # zeilenweise: Anteil je Studio', 'round(prop.table(tab, margin = 2), 3)  # spaltenweise']);
B.code(['cov(d$x, d$y)                          # Kovarianz (n−1)', 'cor(d$x, d$y)                          # Pearson', 'cor(d$x, d$y, method = "spearman")     # Spearman (Rangkorrelation)', 'rank(d$x)                              # Ränge',
  'modell <- lm(y ~ x, data = d)          # Regression y = a + b·x', 'coef(modell)                           # a (Intercept) und b', 'summary(modell)                        # inkl. R² ("Multiple R-squared")',
  'predict(modell, newdata = data.frame(x = 22))   # Prognose', 'round(summary(modell)$r.squared, 3)']);
B.box('satz', '„Der Korrelationskoeffizient nach Bravais-Pearson beträgt 0.997; es liegt ein sehr starker positiver linearer Zusammenhang vor.“',
  '„Die geschätzte Regressionsgerade lautet ŷ = −8.654 + 3.269·x. Steigt x um eine Einheit, steigt y im Mittel um 3.269 Einheiten.“',
  '„Im Studio Nord ist der Anteil der Premium-Mitglieder mit 0.533 am höchsten.“');
B.box('falle', 'lm(y ~ x): ZUERST die abhängige Variable (y), dann die erklärende (x).  ·  margin = 1 → Zeilen, margin = 2 → Spalten.  ·  cov/var in R mit n−1 – für r egal (kürzt sich).');

// ───────────────── 8
B.h1('8  Verteilungen: d-, p-, q-, r-Funktionen');
B.table(['Präfix', 'Bedeutung', 'Beispiel Normal'], [['d…', 'Dichte bzw. P(X = x)', 'dnorm(x, mean, sd)'], ['p…', 'Verteilungsfunktion P(X ≤ x)', 'pnorm(q, mean, sd)'], ['q…', 'Quantil: x mit P(X ≤ x) = p', 'qnorm(p, mean, sd)'], ['r…', 'Zufallszahlen', 'rnorm(n, mean, sd)']], [1.5, 4, 4]);
B.table(['Verteilung', 'R-Name + Parameter', 'Beispiel'], [['Binomial B(n, π)', 'binom(x, size = n, prob = π)', 'dbinom(4, 5, 0.25)'], ['Poisson Po(λ)', 'pois(x, lambda)', 'dpois(3, 2.5)'], ['Normal N(μ, σ²)', 'norm(x, mean = μ, sd = σ)', 'pnorm(36, 30, 4)  ← sd, nicht Varianz!'],
  ['Exponential Exp(λ)', 'exp(x, rate = λ)', 'pexp(2, rate = 0.4)'], ['Gleichverteilung U(a, b)', 'unif(x, min = a, max = b)', 'punif(0.3, 0, 1)'], ['t-Verteilung', 't(x, df)', 'qt(0.975, df = 8)'], ['χ²-Verteilung', 'chisq(x, df)', 'qchisq(0.95, df = 3)']], [3, 3.5, 3.5]);
B.h2('Typische Wahrscheinlichkeiten');
B.code(['dbinom(4, size = 5, prob = 0.25)            # P(X = 4)', '1 - pbinom(3, size = 5, prob = 0.25)        # P(X ≥ 4) = 1 − P(X ≤ 3)', 'pbinom(3, 5, 0.25, lower.tail = FALSE)      # dasselbe: P(X > 3)',
  'sum(dbinom(2:4, 5, 0.25))                   # P(2 ≤ X ≤ 4)', 'ppois(2, lambda = 2.5)                      # P(X ≤ 2)', '1 - pnorm(36, mean = 30, sd = 4)            # P(X > 36)', 'pnorm(35, 30, 4) - pnorm(25, 30, 4)         # P(25 ≤ X ≤ 35)',
  'qnorm(0.975)                                # 1.959964', 'qt(0.95, df = 8)                            # 1.859548']);
B.box('falle', 'Diskret: P(X ≥ k) = 1 − pbinom(k − 1, …) (k − 1!).  ·  Normal: sd = Wurzel aus der Varianz.  ·  Exponential: Parameter heißt rate = λ (Erwartungswert 1/λ).');

// ───────────────── 9
B.h1('9  Simulation & Zufallszahlen');
B.code(['set.seed(123)                         # reproduzierbar', 'x <- rnorm(100, mean = 50, sd = 10)', 'w <- sample(1:6, 1000, replace = TRUE) # Würfel 1000-mal', 'mean(w == 6)                          # relative Häufigkeit einer 6',
  'sample(c("K", "Z"), 10, replace = TRUE)', 'mean(replicate(10000, mean(sample(1:6, 2, replace = TRUE)) > 4))   # Wahrscheinlichkeit per Simulation']);

// ───────────────── 10
B.h1('10  Likelihood & Maximum-Likelihood in R');
B.h2('a) Individuelle Likelihoods & Gesamt-Likelihood');
B.code(['d$iL04 <- dexp(d$Wartezeit, rate = 0.4)   # stetig: Dichte', 'd$iL2  <- dpois(d$Buecher, lambda = 2)    # diskret: Wahrscheinlichkeitsfunktion', 'head(d)', 'L <- prod(d$iL04)                         # Likelihood = Produkt', 'L', '[1] 8.31605e-64',
  'format(L, scientific = TRUE, digits = 4)  # 8.316e-64  ->  8.316 × 10^(-64)', 'logL <- sum(log(d$iL04))                  # Log-Likelihood = Summe der Logs']);
B.box('satz', '„Unter der Annahme λ = 0.4 beträgt die Likelihood aller Beobachtungen L(λ = 0.4) = 8.316 × 10^(−64).“');
B.box('falle', 'Darstellung X × 10^Y: aus 8.31605e-64 wird 8.316 × 10^(−64) – X auf 3 Nachkommastellen, Y ganze Zahl (hier negativ!).');
B.h2('b) Likelihood-Funktion schreiben & über einem Gitter maximieren');
B.code(['Likelihood.exp <- function(lambda, x) {', '  L <- prod(dexp(x, rate = lambda))', '  return(L)', '}', 'lam <- seq(0.30, 0.60, by = 0.05)', 'Ls  <- sapply(lam, Likelihood.exp, x = d$Wartezeit)',
  'cbind(lam, Ls)                     # Tabelle λ und L(λ)', 'lam[which.max(Ls)]                 # ML-Schätzer aus dem Gitter', '[1] 0.45', '# Alternative mit for-Schleife:', 'for (l in lam) print(Likelihood.exp(l, d$Wartezeit))']);
B.h2('c) Numerisch optimieren');
B.code(['logL <- function(lambda, x) sum(dexp(x, rate = lambda, log = TRUE))', 'optimize(logL, interval = c(0.01, 5), x = d$Wartezeit, maximum = TRUE)   # $maximum = λ̂',
  '# mehrere Parameter: negative Log-Likelihood mit nlm minimieren', 'nll <- function(p, x) -sum(dnorm(x, mean = p[1], sd = p[2], log = TRUE))', 'nlm(nll, p = c(60, 10), x = d$Minuten)$estimate']);
B.h2('d) Analytische ML-Schätzer zum Vergleich');
B.table(['Modell', 'ML-Schätzer', 'R'], [['Poisson(λ)', 'λ̂ = x̄', 'mean(x)'], ['Exponential(λ)', 'λ̂ = 1/x̄', '1/mean(x)'], ['Bernoulli(π)', 'π̂ = Anteil', 'mean(x == "ja")'], ['Normal μ, σ²', 'μ̂ = x̄, σ̂² = (1/n)Σ(x−x̄)²', 'mean(x); mean((x-mean(x))^2)']], [3, 3.5, 3.5]);
B.box('satz', '„Aus der vorgegebenen Menge maximiert λ = 0.45 die Likelihood; der ML-Schätzer ist daher λ̂ = 0.45. Der analytische ML-Schätzer 1/x̄ = 0.445 liegt sehr nahe daran.“');
B.box('retter', 'Funktion mit function(lambda, x) und return() sauber hinschreiben – auch ohne Ergebnis gibt die Struktur Punkte. Gitter mit sapply ODER for-Schleife, beides ist erlaubt.');

// ───────────────── 11
B.h1('11  Eigene Funktionen, Schleifen, Text');
B.code(['quadrat <- function(x) {          # Funktion definieren', '  return(x^2)', '}', 'quadrat(4)                        # [1] 16', '', 'for (i in 1:5) {                  # for-Schleife', '  print(i^2)', '}',
  'erg <- numeric(5)                 # Ergebnisvektor vorbereiten', 'for (i in 1:5) erg[i] <- i^2', '', 'if (x > 0) { "positiv" } else { "nicht positiv" }', 'k <- 0; while (k < 3) { k <- k + 1 }',
  'paste("Sitz", 12, "Aufgabe e)")   # "Sitz 12 Aufgabe e)"', 'paste0("0.", 1, 2, 3)             # "0.123" (ohne Leerzeichen)', 'paste(1:3, collapse = "")         # "123"', 'cat("Ergebnis:", round(3.14159, 3), "\\n")']);
B.box('tipp', 'Aufgabe „Zahl aus aneinandergereihten Ziffern bauen“ (Typ Yennefer-Zahl):', 'f <- function(n) { s <- paste(1:n, collapse = ""); return(paste0("0.", s)) }   →  f(17) ergibt "0.1234567891011121314151617"');

// ───────────────── 12
B.h1('12  Kerndichteschätzer');
B.code(['dens <- density(d$Minuten)                         # Standard: Gauß-Kern', 'plot(dens, main = "…", xlab = "Minuten", ylab = "Dichte")', 'density(d$Minuten, bw = 5)                         # Bandweite festlegen',
  'density(d$Minuten, kernel = "epanechnikov")        # anderer Kern ("gaussian", "rectangular", "triangular", "biweight")', 'hist(d$Minuten, freq = FALSE); lines(density(d$Minuten), col = "red")']);
B.ul(['Große Bandweite → glattere Kurve, kleine Bandweite → zackige Kurve.', '„biweight“ entspricht dem Bisquare-Kern aus der Vorlesung.']);

// ───────────────── 13
B.h1('13  Konfidenzintervalle & Tests in R');
B.h2('t-Test (Erwartungswert, Varianz unbekannt)');
B.code(['t.test(d$Minuten, mu = 70, alternative = "less", conf.level = 0.95)', '', '        One Sample t-test', 'data:  d$Minuten', 't = -1.1175, df = 79, p-value = 0.1336', 'alternative hypothesis: true mean is less than 70', '95 percent confidence interval:', '     -Inf 70.84423',
  'sample estimates:', 'mean of x', '   68.275']);
B.table(['Behauptung', 'H₁', 'alternative ='], [['„weniger als μ₀“', 'μ < μ₀', '"less"'], ['„mehr als μ₀“', 'μ > μ₀', '"greater"'], ['„ungleich / unterscheidet sich“', 'μ ≠ μ₀', '"two.sided" (Standard)']], [4, 2, 3]);
B.code(['t.test(x, mu = 200)$p.value                       # nur p-Wert', 't.test(x, conf.level = 0.95)$conf.int              # zweiseitiges 95 %-KI', 't.test(Minuten ~ Abo, data = d)                   # Zwei-Stichproben-t-Test (Gruppen)',
  'binom.test(x = 15, n = 20, p = 0.5, alternative = "greater")   # Binomialtest', 'prop.test(x = 50, n = 80, p = 0.5)                # approx. Anteilstest / KI für π', 'chisq.test(table(d$Studio, d$Abo))                # χ²-Unabhängigkeitstest',
  'chisq.test(c(20, 30, 50), p = c(0.25, 0.25, 0.5))   # χ²-Anpassungstest']);
B.h2('KI von Hand (wenn verlangt)');
B.code(['n <- length(x); m <- mean(x); s <- sd(x)', 'm + c(-1, 1) * qt(0.975, df = n - 1) * s / sqrt(n)     # σ unbekannt', 'm + c(-1, 1) * qnorm(0.975) * sigma / sqrt(n)          # σ bekannt',
  'T <- (m - 70) / (s / sqrt(n)); T                        # Teststatistik von Hand', 'pt(T, df = n - 1)                                       # p-Wert linksseitig']);
B.box('satz', '„Hypothesen: H₀: μ ≥ 70 vs. H₁: μ < 70. Der p-Wert beträgt 0.134 > 0.05 = α. Daher kann H₀ nicht abgelehnt werden: Es kann nicht statistisch abgesichert werden, dass die mittlere Trainingsdauer weniger als 70 Minuten beträgt.“');
B.box('falle', 'Die Behauptung, die bewiesen werden soll, gehört in H₁ und bestimmt alternative.  ·  „p-value = 2.2e-16“ heißt p < 0.001 (sehr klein).  ·  conf.level bei einseitigem Test liefert ein einseitiges KI (−Inf …).');

// ───────────────── 14
B.h1('14  Fehlermeldungen & Rettung');
B.table(['Fehlermeldung', 'Ursache', 'Lösung'], [
  ['cannot open file … No such file', 'falsches Working Directory / Dateiname', 'getwd(), list.files(), setwd(path.expand("~")), Dateiname prüfen'],
  ['object \'d\' not found', 'Objekt noch nicht erzeugt', 'Zeile mit d <- read.csv(…) zuerst ausführen'],
  ['could not find function', 'Tippfehler / Funktion nicht definiert', 'Schreibweise prüfen, eigene Funktion zuerst ausführen'],
  ['non-numeric argument', 'Rechnen mit Text', 'class() prüfen, as.numeric(), dec = "," beim Einlesen'],
  ['some \'x\' not counted', 'Daten außerhalb der breaks', 'breaks so wählen, dass min und max abgedeckt sind'],
  ['Ergebnis NA', 'fehlende Werte', 'na.rm = TRUE'], ['unexpected symbol / \'}\'', 'Klammer oder Komma fehlt', 'Klammern zählen, Komma zwischen Argumenten'], ['leeres PDF', 'dev.off() vergessen', 'dev.off() ausführen']], [3, 3, 4]);
B.box('retter', 'Steckst du fest: nicht 10 Minuten an einem Fehler hängen. Code so abgeben, wie er ist (zeigt den Ansatz), und mit der nächsten Teilaufgabe weitermachen.');

// ───────────────── 15
B.h1('15  Komplettes Musterskript einer Teil-B-Klausur');
B.code(['## a) Working Directory', 'setwd(path.expand("~"))', '', '## b) Einlesen + erste 6 Zeilen', 'd <- read.csv("Fitness.csv", sep = ",", dec = ".", header = TRUE)', 'head(d)', '',
  '## c) Objekttypen', 'class(d$Studio); class(d$Besuche)', '', '## d) Lage- und Streuungsmaße', 'round(median(d$Minuten), 3); round(IQR(d$Minuten), 3)', 'round(mean(d$Minuten), 3);   round(sd(d$Minuten), 3)', '',
  '## e) Grafik speichern', 'pdf("Boxplot.pdf")', 'boxplot(Minuten ~ Studio, data = d, main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil e)",', '        xlab = "Studio", ylab = "Trainingsdauer in Minuten")', 'dev.off()', 'tapply(d$Minuten, d$Studio, median)', '',
  '## f) Kontingenztabelle + bedingte Anteile', 'tab <- table(d$Studio, d$Abo); tab', 'round(prop.table(tab, margin = 1), 3)', '', '## g) individuelle Likelihoods + Likelihood', 'd$iL04 <- dexp(d$Wartezeit, rate = 0.4)', 'L <- prod(d$iL04); L', '',
  '## h) Likelihood-Funktion + Gitter', 'Likelihood.exp <- function(lambda, x) { return(prod(dexp(x, rate = lambda))) }', 'lam <- seq(0.30, 0.60, by = 0.05)', 'Ls <- sapply(lam, Likelihood.exp, x = d$Wartezeit)', 'cbind(lam, Ls); lam[which.max(Ls)]; 1 / mean(d$Wartezeit)', '',
  '## i) Test', 't.test(d$Minuten, mu = 70, alternative = "less")']);

// ───────────────── 16
B.h1('16  Antwortsatz-Vorlagen');
B.table(['Teilaufgabe', 'Antwortsatz (Zahlen ersetzen)'], [
  ['Objekttyp', 'Die Variable Studio ist vom Typ character, die Variable Besuche vom Typ integer (ganze Zahlen).'],
  ['Mittel / sd', 'Das arithmetische Mittel der Variable Minuten beträgt 68.275, der unverzerrte Schätzer der Standardabweichung 13.807.'],
  ['Median / IQR', 'Der Median der Trainingsdauer beträgt 69.000 Minuten, der Interquartilsabstand 20.250 Minuten.'],
  ['Grafik-Vergleich', 'Im Studio … ist der Median der Trainingsdauer am höchsten; dort streuen die Werte auch am stärksten.'],
  ['Gruppen', 'Mitglieder des Studios … trainieren im Durchschnitt am längsten (… Minuten).'],
  ['Anteile', 'Im Studio Nord ist der Anteil der Premium-Mitglieder mit 0.533 am höchsten.'],
  ['Likelihood', 'Die Likelihood aller Beobachtungen unter λ = 0.4 beträgt 8.316 × 10^(−64).'],
  ['ML-Gitter', 'Aus der vorgegebenen Menge maximiert λ = 0.45 die Likelihood; damit ist λ̂ = 0.45 der ML-Schätzer.'],
  ['Korrelation', 'Der Korrelationskoeffizient beträgt …; es liegt ein (schwacher/mittlerer/starker) (positiver/negativer) linearer Zusammenhang vor.'],
  ['Regression', 'Steigt x um eine Einheit, so steigt/sinkt y laut Modell im Mittel um … Einheiten.'],
  ['Test ablehnen', 'Da der p-Wert (…) kleiner als α = 0.05 ist, wird H₀ abgelehnt. Es kann statistisch abgesichert werden, dass …'],
  ['Test nicht ablehnen', 'Da der p-Wert (…) größer als α = 0.05 ist, kann H₀ nicht abgelehnt werden. Es kann nicht statistisch abgesichert werden, dass …'],
  ['KI', 'Das 95 %-Konfidenzintervall für den Erwartungswert lautet [… ; …].']], [2.4, 7.6]);

B.save(path.join(__dirname, '../../Formelsammlung_R_TeilB.docx')).then(() => console.log('ok'));
