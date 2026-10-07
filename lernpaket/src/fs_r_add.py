# Ergänzungen für die R-Formelsammlung: werden in fs_r.py vor den genannten Abschnitten eingefügt (einmalig)
import re, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fs_r.py')
s = open(P, encoding='utf-8').read()
if 'R("1.12"' in s:
    raise SystemExit('schon ergänzt')

ADD = {}
ADD['D.S("2"'] = r'''
R("1.12", "Runden und Zahlen formatieren",
  sig="„auf drei Nachkommastellen runden“, „in der Form X × 10^Y“",
  ne="Sınavda her sayı R komutu ile yuvarlanmalı: round(x, 3). Çok küçük sayılar için signif/format.",
  r=\'\'\'round(22.08333, 3)
signif(0.000006938384, 4)
format(6.938384e-131, scientific = TRUE, digits = 4)
sprintf("%.3f", 7.29231)\'\'\',
  st=["<code>round(x, 3)</code>: 3 Nachkommastellen – Standard für alle Antworten.",
      "<code>signif(x, 4)</code>: 4 gültige Ziffern – gut für sehr kleine Zahlen.",
      "<code>format(x, scientific = TRUE, digits = 4)</code>: wissenschaftliche Schreibweise → als \\(X\\times10^{Y}\\) abschreiben.",
      "<code>sprintf('%.3f', x)</code>: zeigt auch Nullen am Ende (7.290 statt 7.29)."],
  fa="round() ändert die Darstellung im Output; rechne mit dem ungerundeten Objekt weiter und runde nur das Endergebnis.",
  ks="„Die Likelihood beträgt 6.938 × 10^(−131).“")
'''
ADD['D.S("3"'] = r'''
R("2.8", "Sortieren, Extremwerte und eindeutige Werte",
  sig="„Welche Taverne …am meisten?“, „die drei größten …“, „Wie viele verschiedene …?“",
  ne="order ile sırala, which.max ile en büyüğün satırını bul, unique ile farklı değerleri say.",
  r=\'\'\'d[order(d$Muenzen, decreasing = TRUE), ][1:3, ]
d[which.max(d$Muenzen), ]
unique(d$Tal)
length(unique(d$Monster))
sum(d$Muenzen > 20)
mean(d$Muenzen > 20)\'\'\',
  st=["<code>order()</code> liefert die Reihenfolge der Zeilen; <code>decreasing = TRUE</code> für absteigend.",
      "<code>which.max()</code>/<code>which.min()</code> geben die <b>Zeilennummer</b> des Extremwerts.",
      "<code>sum(Bedingung)</code> = Anzahl, <code>mean(Bedingung)</code> = Anteil (TRUE zählt als 1)."],
  ks="„Die meisten Münzen (33) erhielt der Barde in Taverne T08 im Bergtal.“")

R("2.9", "Data Frame selbst erstellen und speichern",
  sig="„Erstellen Sie einen Data Frame mit …“, „speichern Sie … als CSV“",
  ne="Vektörlerden data.frame kur; write.csv ile kaydet.",
  r=\'\'\'neu <- data.frame(x = c(1, 2, 3), Gruppe = c("A", "B", "A"))
neu
write.csv(neu, "neu.csv", row.names = FALSE)
read.csv("neu.csv")\'\'\',
  fa="Ohne <code>row.names = FALSE</code> schreibt R eine zusätzliche Spalte mit Zeilennummern.")
'''
ADD['D.S("4"'] = r'''
R("3.9", "Empirische Verteilungsfunktion als Zahl, Quantil nach Vorlesung",
  sig="„Anteil der Beobachtungen mit höchstens …“, „F̂(20)“, „Quantil gemäß Vorlesungsdefinition“",
  ne="ecdf(x) bir fonksiyon döndürür: Fn(20) = ≤ 20 olanların oranı. Ders tanımındaki kantil için type = 2.",
  r=\'\'\'Fn <- ecdf(d$Muenzen)
Fn(20)
1 - Fn(20)
quantile(d$Muenzen, c(0.25, 0.5, 0.75), type = 2)
quantile(d$Muenzen, c(0.25, 0.5, 0.75))\'\'\',
  st=["<code>Fn(a)</code> = Anteil ≤ a; <code>1 - Fn(a)</code> = Anteil > a.",
      "<code>type = 2</code> entspricht der Definition aus V02 (aufrunden bzw. Mittelwert bei ganzzahligem nα); der R-Standard ist <code>type = 7</code>.",
      "Steht in der Aufgabe „mit den Standardeinstellungen von R“, <b>kein</b> type angeben."])

R("3.10", "Standardisieren (z-Werte)",
  sig="„Standardisieren Sie die Variable …“",
  ne="z = (x − ortalama) / sd → ortalama 0, sd 1.",
  r=\'\'\'z <- (d$Muenzen - mean(d$Muenzen)) / sd(d$Muenzen)
round(head(z), 3)
round(c(mean(z), sd(z)), 3)\'\'\')
'''
ADD['D.S("5"'] = r'''
R("4.8", "Grafik-Feinschliff: Achsen, Farben, Linien, Legende",
  sig="„Zeichnen Sie zusätzlich …ein“, „in derselben Grafik“, „mit Legende“",
  ne="xlim/ylim eksen aralığı; lines/curve/abline var olan grafiğe ekler; legend açıklama kutusu.",
  r=\'\'\'pdf("Feinschliff.pdf")
hist(d$Muenzen, freq = FALSE, xlim = c(0, 40), ylim = c(0, 0.08), col = "lightblue",
     main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil f)", xlab = "Muenzen", ylab = "Dichte")
lines(density(d$Muenzen), col = "red", lwd = 2)
curve(dnorm(x, mean(d$Muenzen), sd(d$Muenzen)), add = TRUE, col = "blue", lty = 2)
abline(v = mean(d$Muenzen), col = "darkgreen")
legend("topright", legend = c("KDE", "Normal", "Mittelwert"),
       col = c("red", "blue", "darkgreen"), lty = c(1, 2, 1))
dev.off()\'\'\',
  st=["<code>lines()</code>, <code>points()</code>, <code>abline()</code>, <code>curve(…, add = TRUE)</code> zeichnen <b>in</b> die bestehende Grafik.",
      "<code>abline(h = …)</code> waagerecht, <code>abline(v = …)</code> senkrecht, <code>abline(a, b)</code> Gerade.",
      "<code>lty</code> Linientyp (1 durchgezogen, 2 gestrichelt), <code>lwd</code> Linienbreite, <code>col</code> Farbe."],
  fa="Zusatzlinien vor <code>dev.off()</code> zeichnen, sonst fehlen sie im PDF.")

R("4.9", "QQ-Plot: Normalverteilung prüfen",
  sig="„Prüfen Sie grafisch, ob … normalverteilt ist“",
  ne="Noktalar doğruya yakınsa normal dağılım varsayımı makul.",
  r=\'\'\'qqnorm(d$Kampfzeit, main = "QQ-Plot Kampfzeit")
qqline(d$Kampfzeit, col = "red")\'\'\',
  ks="„Die Punkte weichen deutlich von der Geraden ab; die Normalverteilungsannahme ist für Kampfzeit fraglich.“")
'''
ADD['D.S("6"'] = r'''
R("5.7", "Kombinatorik, Laplace und Bayes in R",
  sig="„Wie viele Möglichkeiten …?“, „Wahrscheinlichkeit, dass die Augensumme …“, Baumdiagramm nachrechnen",
  ne="choose = binom katsayısı, factorial = faktöriyel. Laplace: tüm sonuçları expand.grid ile listele. Bayes'i değişkenlerle hesapla.",
  r=\'\'\'choose(5, 2)
factorial(4)
w <- expand.grid(a = 1:6, b = 1:6)
mean(w$a + w$b == 7)
pA <- 0.3; pB_A <- 0.2; pB_nA <- 0.05
pB <- pA * pB_A + (1 - pA) * pB_nA
pB
pA * pB_A / pB\'\'\',
  ks="„Die Wahrscheinlichkeit, dass eine erkrankte Person raucht, beträgt 0.632.“")
'''
ADD['D.S("9"'] = r'''
R("8.7", "ML für eine selbst definierte Dichte (Teil-A-Typ in R)",
  sig="„Schreiben Sie die Dichte als Funktion …“, „bestimmen Sie den ML-Schätzer numerisch“",
  ne="Dichte'yi function olarak yaz, log-likelihood = sum(log(f)). optimise ile maksimize et, analitik sonuçla karşılaştır.",
  r=\'\'\'f <- function(x, lambda) lambda^2 * x * exp(-lambda * x)
x <- c(1, 3, 2, 0.5, 3.5)
logL <- function(lambda) sum(log(f(x, lambda)))
optimise(logL, interval = c(0.01, 10), maximum = TRUE)$maximum
2 / mean(x)\'\'\',
  st=["Dichte genau wie in der Aufgabe abschreiben (<code>^</code> für Potenzen, <code>exp()</code> für e).",
      "Intervall bei <code>optimise</code> groß genug, aber nur zulässige Werte (z. B. λ > 0).",
      "<code>$maximum</code> = Schätzer, <code>$objective</code> = maximale Log-Likelihood."],
  ks="„Der numerisch bestimmte ML-Schätzer beträgt λ̂ = 1.000 und stimmt mit dem analytischen Ergebnis 2/x̄ überein.“")

R("8.8", "ML-Schätzer der Standardverteilungen direkt",
  sig="„Berechnen Sie den ML-Schätzer für … (Bernoulli/Poisson/Exponential/Normal)“",
  ne="Bilinen modellerde ML tahmini doğrudan bir ortalama formülü.",
  r=\'\'\'y <- c(1, 0, 1, 1, 0)
mean(y)
w <- c(2.1, 0.7, 1.5, 3.2)
1 / mean(w)
c(mean(w), mean((w - mean(w))^2))\'\'\',
  st=["Bernoulli: \\(\\hat\\pi=\\bar x\\) · Poisson: \\(\\hat\\lambda=\\bar x\\) · Exponential: \\(\\hat\\lambda=1/\\bar x\\)",
      "Normal: \\(\\hat\\mu=\\bar x\\), \\(\\hat\\sigma^2=\\frac1n\\sum(x_i-\\bar x)^2\\) – Nenner \\(n\\), also <b>nicht</b> <code>var()</code>!"])
'''
ADD['D.S("10"'] = r'''
R("9.8", "Zwei Gruppen vergleichen (Zwei-Stichproben-t-Test)",
  sig="„Unterscheiden sich die mittleren … in Flusstal und Bergtal?“",
  ne="İki grubun ortalamasını karşılaştır: t.test(x1, x2). Tek yönlüyse alternative ekle.",
  r=\'\'\'x1 <- d$Muenzen[d$Tal == "Flusstal"]
x2 <- d$Muenzen[d$Tal == "Bergtal"]
t.test(x1, x2, alternative = "two.sided")\'\'\',
  st=["H₀: μ₁ = μ₂ vs. H₁: μ₁ ≠ μ₂ (bzw. < / > mit alternative).",
      "Bei verbundenen Stichproben (vorher/nachher, gleiche Personen): <code>paired = TRUE</code>.",
      "Gleiche Varianzen angenommen: <code>var.equal = TRUE</code>."],
  ks="„Da der p-Wert 0.073 > 0.05 ist, kann H₀ nicht abgelehnt werden; ein Unterschied der mittleren Münzanzahl ist nicht statistisch abgesichert.“")

R("9.9", "Anteil testen und KI für einen Anteil (prop.test, binom.test)",
  sig="„80 von 100 …“, „Anteil größer als 75 %?“",
  ne="prop.test normal yaklaşımı, binom.test tam test. İkisi de GA verir.",
  r=\'\'\'prop.test(x = 80, n = 100, p = 0.75, alternative = "greater", correct = FALSE)$p.value
binom.test(80, 100, p = 0.75, alternative = "greater")$p.value
p <- 0.8; n <- 100
p + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / n)\'\'\',
  fa="Das KI aus der Vorlesung ist das Wald-Intervall (letzte Zeile); prop.test ohne/ mit correct liefert ein etwas anderes Intervall.")
'''
for marker, txt in ADD.items():
    assert s.count(marker) == 1, marker
    s = s.replace(marker, txt.replace("\\'", "'").strip('\n') + '\n\n' + marker, 1)

# Abschnitt 11 -> 13, neue Abschnitte 11 (komplette Klausur) und 12 (Antwortsätze)
s = s.replace('D.S("11", "Fehlermeldungen und Kontrolle"', 'D.S("13", "Fehlermeldungen und Kontrolle"')
s = s.replace('D.E("11.1", "Typische Fehlermeldungen', 'D.E("13.1", "Typische Fehlermeldungen').replace('D.E("11.2", "Checkliste', 'D.E("13.2", "Checkliste')
s = s.replace('Bölüm 11 (Fehlermeldungen)', 'Bölüm 13 (Fehlermeldungen)')
NEW = r'''
# =====================================================================
D.S("11", "Komplette Teil-B-Klausur Schritt für Schritt (Altklausur-Typ)",
    "Gerçek sınavın (Altklausur Witcher) tüm alt soruları sırayla: kod, çıktı, Antwortsatz. Kendi sınavında sadece dosya ve değişken adlarını değiştir.")
D.E("11.1", "a) Working Directory setzen",
    sig="„Setzen Sie mittels setwd(path.expand(\"~\")) Ihr Working Directory …“ (2 P)",
    ne="Komutu aynen yaz. Kontrol için getwd().",
    r=\'\'\'setwd(path.expand("~"))
getwd()\'\'\', run=False)
R("11.2", "b) Daten einlesen und die ersten 6 Zeilen wiedergeben (4 P)",
  sig="„Speichern Sie die … Daten als Data-Frame-Objekt d … und geben Sie die ersten 6 Zeilen wieder“",
  ne="Ayırıcıyı kontrol et (burada ;). head(d) çıktısını da kopyala.",
  r=\'\'\'d <- read.csv("Taverne.csv", sep = ";", dec = ".", header = TRUE)
head(d)\'\'\')
R("11.3", "c) Objekttypen ermitteln (4 P)",
  sig="„Ermitteln Sie unter Einbezug eines passenden R-Befehls die Objekttypen der Variablen Tal und Muenzen“",
  r=\'\'\'typeof(d$Tal)
typeof(d$Muenzen)
class(d$Muenzen)\'\'\',
  ks="„Die Variable Tal ist vom Typ character (Text). Die Variable Muenzen ist ein numerisches Objekt vom Typ integer, d. h. sie enthält nur ganze Zahlen.“")
R("11.4", "d) Mittelwert und unverzerrte Standardabweichung (4 P)",
  sig="„Berechnen und nennen Sie das arithmetische Mittel und den unverzerrten Schätzer für die Standardabweichung … auf 3 Nachkommastellen“",
  r=\'\'\'round(mean(d$Muenzen), 3)
round(sd(d$Muenzen), 3)\'\'\',
  ks="„Das arithmetische Mittel der Variable Muenzen beträgt 22.917. Der unverzerrte Schätzer für die Standardabweichung beträgt 7.267.“")
R("11.5", "e) Histogramm mit vorgegebenen Klassen speichern (8 P)",
  sig="„Histogramm … Intervallgrenzen [5,15), [15,20), [20,25), [25,35) … Titel … Dichte … als Histogramm.pdf speichern“",
  r=\'\'\'pdf("Histogramm.pdf")
hist(d$Muenzen, breaks = c(5, 15, 20, 25, 35), right = FALSE, freq = FALSE,
     main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil e)",
     xlab = "Muenzen", ylab = "Dichte")
dev.off()\'\'\',
  st=["breaks = genau die Grenzen aus der Aufgabe · [a, b) → <code>right = FALSE</code> · Dichte → <code>freq = FALSE</code>.",
      "Titel, x- und y-Achse exakt wie verlangt; Datei im Ordner prüfen und in ILIAS hochladen."])
R("11.6", "f) Individuelle Likelihoods und Gesamt-Likelihood (6 P)",
  sig="„… Poissonverteilung … λ = 20 … Spalte iL20 … Likelihood aller Beobachtungen … in der Form X × 10^Y“",
  r=\'\'\'d$iL20 <- dpois(d$Muenzen, lambda = 20)
head(d)
L20 <- prod(d$iL20)
L20\'\'\',
  ks="„Unter der Annahme λ = 20 beträgt die Likelihood aller Beobachtungen L(20) = X × 10^(Y)“ – X und Y aus dem Output ablesen (3 Nachkommastellen).")
R("11.7", "g) Likelihood-Funktion und ML-Schätzer auf einem Gitter (9 P)",
  sig="„Schreiben Sie eine Funktion Likelihood.pois(lambda, x) … für alle λ ∈ {17, …, 23} … ML-Schätzer“",
  r=\'\'\'Likelihood.pois <- function(lambda, x) {
  return(prod(dpois(x, lambda)))
}
werte <- 17:23
L <- sapply(werte, Likelihood.pois, x = d$Muenzen)
cbind(werte, L)
werte[which.max(L)]
mean(d$Muenzen)\'\'\',
  ks="„Aus der gegebenen Menge maximiert λ = 23 die Likelihood; der ML-Schätzer ist λ̂ = 23 (analytisch wäre x̄ = 22.917).“")
R("11.8", "h) Funktion mit Schleife: Zahl aus Ziffern zusammensetzen (8 P)",
  sig="„Schreiben Sie eine R-Funktion YenneferZahl.fun, welche für n … die Zahl 0.123456789101112… bestimmt“",
  r=\'\'\'YenneferZahl.fun <- function(n) {
  s <- ""
  for (i in 1:n) {
    s <- paste0(s, i)
  }
  return(paste0("0.", s))
}
YenneferZahl.fun(17)
substr(YenneferZahl.fun(60), 1, 101)\'\'\',
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

'''
marker = '# =====================================================================\nD.S("13", "Fehlermeldungen und Kontrolle"'
if marker not in s:
    marker = 'D.S("13", "Fehlermeldungen und Kontrolle"'
s = s.replace(marker, NEW.replace("\\'", "'").strip('\n') + '\n\n' + marker, 1)
open(P, 'w', encoding='utf-8').write(s)
print('ok')
