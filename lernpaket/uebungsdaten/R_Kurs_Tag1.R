############################################################
# R-Kurs Tag 1 – alle Befehle aus Abschnitt 1.9 des Lernbuchs
# Datei Taverne.csv muss im Ordner Dokumente liegen.
# Jede Zeile mit Strg + Enter ausführen und die Ausgabe ansehen.
############################################################

## 1.9.2 R als Taschenrechner und Objekte
3 + 4 * 2
(3 + 4) * 2
2^3
sqrt(16)
log(10); exp(1)
choose(10, 2)
a <- 5
b <- a * 2
b

## 1.9.3 Vektoren
x <- c(3, 2, 5, 1, 3, 4)
x
length(x)
x[1]
x[c(2, 4)]
x[-1]
x * 2
x + 10
sum(x)
sort(x)
x > 2
x[x > 2]
sum(x > 2)      # Anzahl
mean(x > 2)     # Anteil
1:6
seq(0, 20, by = 5)
rep(1/6, 3)

## 1.9.4 Datentypen
typeof(x)
typeof(1:6)
typeof(c("Wolf", "Troll"))
typeof(x > 2)
f <- factor(c("Wolf", "Troll", "Wolf"))
f
class(f)
levels(f)

## 1.9.5 Datensatz einlesen
setwd(path.expand("~"))
getwd()
d <- read.csv("Taverne.csv", header = TRUE, sep = ";", dec = ".")
head(d)
str(d)
names(d)
dim(d)
d$Muenzen
d[2, ]
d[1:3, c("Tal", "Muenzen")]
typeof(d$Tal)
typeof(d$Muenzen)
typeof(d$Kampfzeit)

## 1.9.6 Kennzahlen
mean(d$Muenzen)
median(d$Muenzen)
var(d$Muenzen)          # mit 1/(n-1)
sd(d$Muenzen)           # mit 1/(n-1)
n <- length(d$Muenzen)
var(d$Muenzen) * (n - 1) / n   # Varianz mit 1/n
round(mean(d$Muenzen), 3)
round(sd(d$Muenzen), 3)
range(d$Muenzen)
quantile(d$Muenzen, c(0.25, 0.5, 0.75))
IQR(d$Muenzen)
summary(d$Muenzen)
table(d$Monster)
prop.table(table(d$Monster))
which(table(d$Monster) == max(table(d$Monster)))   # Modus
tapply(d$Muenzen, d$Tal, mean)
subset(d, Tal == "Bergtal")
d[d$Muenzen > 25, ]
mean(d$Muenzen > 25)
y <- c(3, 2, 5, NA, 4)
mean(y)
mean(y, na.rm = TRUE)

## 1.9.7 Grafiken und PDF
pdf("Histogramm.pdf")
hist(d$Muenzen, breaks = c(10, 20, 30, 40), right = FALSE, freq = FALSE,
     main = "Sitz 12, Matr.Nr. 12345678, Aufgabenteil d)",
     xlab = "Muenzen", ylab = "Dichte")
dev.off()
h <- hist(d$Muenzen, breaks = c(10, 20, 30, 40), right = FALSE, plot = FALSE)
h$counts
h$density
plot(d$Kampfzeit, d$Muenzen, pch = 16,
     xlab = "Kampfzeit (min)", ylab = "Muenzen", main = "Streudiagramm")
boxplot(Muenzen ~ Tal, data = d, main = "Muenzen je Tal", xlab = "Tal", ylab = "Muenzen")
boxplot(d$Kampfzeit, plot = FALSE)$stats

## 1.9.8 Klassen, Kontingenztafeln, Korrelation
d$Kampfzeit.3 <- cut(d$Kampfzeit, breaks = c(0, 5, 60, Inf), right = FALSE)
d$Kampfzeit.3
table(d$Kampfzeit.3)
d$Muenzen.3 <- cut(d$Muenzen, breaks = c(0, 15, 25, Inf),
                   labels = c("wenig", "mittel", "viel"))
table(d$Muenzen.3)
table(d$Tal, d$Kampfzeit.3)
round(prop.table(table(d$Tal[d$Kampfzeit.3 == "[5,60)"])), 2)
cor(d$Muenzen, d$Kampfzeit)
cor(d$Muenzen, d$Kampfzeit, method = "spearman")
