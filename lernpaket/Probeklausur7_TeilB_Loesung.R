### Musterloesung Probeklausur 7 Teil B (Fussball.csv)

## a)
setwd(path.expand("~"))
getwd()

## b)
d <- read.csv("Fussball.csv", sep = ",", dec = ".", header = TRUE)
head(d)

## c)
typeof(d$Ort)        # "character"
typeof(d$Zuschauer)  # "integer"
# Antwortsatz: Ort ist ein character-Objekt, Zuschauer ein numerisches Objekt vom Typ integer.
# Wetter ist nominalskaliert (Kategorien ohne natuerliche Reihenfolge).

## d)
heim <- d$Zuschauer[d$Ort == "Heim"]
round(mean(heim), 3)   # 416.848
round(sd(heim), 3)     # 58.168
# Antwortsatz: Bei Heimspielen betraegt der Schaetzer fuer das arithmetische Mittel
# der Zuschauer 416.848, der unverzerrte Schaetzer fuer die Standardabweichung 58.168.

## e)
pdf("Histogramm.pdf")
hist(d$Laufleistung, freq = FALSE,
     breaks = c(100, 106, 110, 113, 116, 122), right = FALSE,
     main = "Sitz ..., Matr.Nr. ..., Aufgabenteil e)",
     xlab = "Laufleistung in km", ylab = "Dichte")
dev.off()

## f)
d$iL15 <- dpois(d$Tore, 1.5)
head(d)
prod(d$iL15)   # 5.293488e-43
# Antwortsatz: L(lambda = 1.5) = 5.293 x 10^(-43).

## g)
logLik.pois <- function(lambda, x) {
  sum(log(dpois(x, lambda)))
}
for (lambda in seq(1, 2.4, by = 0.2)) {
  print(c(lambda, logLik.pois(lambda, d$Tore)))
}
# 1.0 -103.053 | 1.2 -98.897 | 1.4 -97.361 | 1.6 -97.743
# 1.8 -99.589  | 2.0 -102.590 | 2.2 -106.526 | 2.4 -111.234
round(mean(d$Tore), 3)  # 1.453
# Antwortsatz: Die Log-Likelihood ist bei lambda = 1.4 maximal, also ist lambda_hat = 1.4
# (auf dem Gitter). Das arithmetische Mittel betraegt 1.453. Beide liegen nahe beieinander,
# weil der ML-Schaetzer der Poisson-Verteilung allgemein lambda_hat = x_quer ist;
# 1.4 ist der Gitterwert, der 1.453 am naechsten liegt.

## h)
# (i)
round(t.test(d$Laufleistung, conf.level = 0.95)$conf.int, 3)   # [110.475; 112.422]
# alternativ von Hand:
n <- length(d$Laufleistung); m <- mean(d$Laufleistung); s <- sd(d$Laufleistung)
round(m + c(-1, 1) * qt(0.975, n - 1) * s / sqrt(n), 3)
# Antwortsatz: Das 95%-KI fuer die erwartete Laufleistung ist [110.475; 112.422] km.
# (ii)
t.test(d$Laufleistung, mu = 110, alternative = "greater")
# t = 2.973, df = 63, p-value = 0.002
# Antwortsatz: H0: mu <= 110 vs. H1: mu > 110. Der p-Wert betraegt 0.002 < 0.01,
# also wird H0 abgelehnt. Die Mannschaft laeuft im Mittel signifikant mehr als 110 km
# pro Spiel; die Behauptung des Trainers wird gestuetzt.

## i)
# Stellen zaehlen: 1,4,9 -> 3 Stellen; 4^2..9^2 (16..81) -> 6 Zahlen x 2 = 12 Stellen;
# ab 10^2 = 100 dreistellig: 81 - 3 - 12 = 66 Stellen -> 66/3 = 22 Zahlen: 10^2 .. 31^2.
# Also n = 31 (31^2 = 961 ist noch dreistellig).
Leinetal.fun <- function(n) {
  zahl <- "0."
  for (i in 1:n) zahl <- paste0(zahl, i^2)
  return(zahl)
}
z <- Leinetal.fun(31)
z
nchar(z) - 2   # 81
# Antwortsatz: Die Leinetal-Zahl mit 81 Nachkommastellen lautet
# 0.149162536496481100121144169196225256289324361400441484529576625676729784841900961
# (bis zur Quadratzahl 31^2 = 961).
