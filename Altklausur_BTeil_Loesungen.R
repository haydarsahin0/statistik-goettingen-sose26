### Musterloesung Teil B
## Klausur vom 04.03.2022
## Last Update: 01.07.2025

## a) 
# In der Klausur: setwd(path.expand("~"))
setwd("~/ownCloud/Statistik 1 Vorlesung (ab WS25-26)/Statistik und Data Science 1/Testate/Probeklausuren") # mit Ihrem eigenen Pfad ersetzen!
getwd() # Working Directory überprüfen

## b) 
d <- read.csv("WitcherData1.csv",sep=",",dec=".",header=TRUE)
# Alternative: read.table()
head(d)

## c)
typeof(d$Tal) # alternativ class(), str(d)
typeof(d$Muenzen)# alternativ class()

# Antwortsatz: Bei der Variable Tal handelt es sich um ein character-Objekt, 
# bei der Variable Münzen um ein numerisches Objekt 
# (des Typs integer, d.h. es enthält nur ganze Zahlen). 

## d) 
round(mean(d$Muenzen),digits=3) # alternativ haendisch z.B. sum(d$Muenzen)/length(d$Muenzen)
round(sd(d$Muenzen),digits=3) # alternativ haendisch

# Antwortsatz: Der Schätzer für das arithmetische Mittel der Variable Muenzen beträgt 22.454. 
# Der unverzerrte Schätzer für die Standarabweichung der Variable Muenzen beträgt 4.610.

## e)
# statt pdf() und dev.off() geht es auch ohne, 
# dafür mit Export abspeichern der Graphik
pdf("Histogramm.pdf")
hist(d$Muenzen,
     freq=FALSE,
     breaks=c(5,15,20,25,35), # Intervallgrenzen
     right=FALSE, # Sollen die Intervalle rechts geschlossen sein? hier: nein!
     main="Aufgabenteil e)",
     xlab="Muenzen",
     ylab="Dichte")
dev.off()

## f) 
d$iL20 <- dpois(d$Muenzen,20)
head(d)

(Likelihood <- prod(d$iL20)) 
# 6.938384e-131, d.h. in der Form X x 10^Y:
# 6.938 x 10^(-131)

# Antwortsatz: Die Likelihood aller gegebenen Beobachtungen unter der Annahme, 
# dass der Parameter Lambda gleich 20 ist, beträgt L(λ=20) = 6.938 x 10^(-131).

## g) 
# Vorgehen:
# 1.  Die Likelihood-Funktion definieren.
# 2. Likelihood für jeden Lambda-Wert im Bereich von 17 bis 23 berechnen.
# 3. Den Maximum Likelihood Schätzer (den Wert von Lambda mit der höchsten Likelihood) bestimmen.

# 1. Funktion zur Berechnung der Likelihood für die Poisson-Verteilung 
Likelihood.pois <- function(lambda,x){ # alternativ, auch ohne x
  L <- prod(dpois(x,lambda)) # alternativ, statt x vorab Werte definiert
  return(L)
}

# 2. Berechnung der Likelihood für alle Lambda-Werte im Bereich 17 bis 23
likelihoods <- for(lambda in 17:23){ # alternativ haendisch, statt mit for-loop
  print(Likelihood.pois(lambda,d$Muenzen))
}

#17: 3.128764e-158
#18: 2.720028e-146
#19: 2.817315e-137
#20: 6.938384e-131
#21: 7.328025e-127
#22: 5.513116e-125
#23: 4.586278e-125

# Finde den größten Wert (die maximale Likelihood) dieser Lambda-Werte

# Gegebene Likelihood-Werte
likelihood_values <- c(3.128764e-158, 2.720028e-146, 2.817315e-137, 
                       6.938384e-131, 7.328025e-127, 5.513116e-125, 4.586278e-125)

# Bestimmen des maximalen Wertes
(max_likelihood <- max(likelihood_values))
## maximale Likelihood liegt bei lamda=22

# Antwortsatz: Das Maximum der Likelihood ergibt sich bei λ=22; 
# somit ist der Maximum-Likelihood-Schätzer Lambda_hat = 22.

#h) Yennefer bzw. Champernowne-Zahl
# Funktion zur Berechnung der Yennefer-Zahl bis zu einer gegebenen Zahl n

# Überlegung vorab:
# Zunächst gilt es, die Anzahl der Dezimalstellen, n, zu bestimmen.
# 99 NKS setzen sich zusammen aus: den "einziffrigen" Zahlen von 1-9; d.h. 9 Zahlen.
# es bleiben von den 99 Dezimalstellen 99-9=90 Stellen übrig. 
# Die 90 übrigen Dezimalstellen bestehen aus 45 "zweiziffrigen" Zahlen von 10-99 (10,11,12,...), d.h. 90/2=45 Zahlen.
# Gesamte Anzahl an Dezimalstellen beträgt also: 9+45=54

YenneferZahl.fun <- function(n) {
  Yenneferzahl <- "0."
  for (i in 1:n) {
    Yenneferzahl <- paste0(Yenneferzahl, i)
  }
  return(Yenneferzahl)
}

# Beispielaufruf der Funktion für n = 54
YenneferZahl_54 <- YenneferZahl.fun(54)
cat("Yennefer-Zahl für n = 54:", YenneferZahl_54, "/n")

## Das Ergebnis ist die Yennefer-Zahl mit 99 NKS.

# Antwortsatz: Auf 99 Nachkommastellen gerundet beträgt die Yennefer-Zahl
# 0.1234567891011121314151617181920212223242526272829303132333...
# ...43536373839404142434445464748495051525354

# Hinweis: In der hiesigen Welt ist diese Zahl als die Champerowne-Zahl bekannt



###########################################################
# alternative Lösung für g) (fancy, aber etwas schwieriger)
###########################################################

# Berechnung der Likelihood für alle Lambda-Werte im Bereich 17 bis 23
# see lapply (Apply a Function over a List or Vector)
likelihoods <- sapply(17:23, function(lambda) {  
  Likelihood.pois(lambda, d$Muenzen)
})

# Likelihood-Werte ausgeben
names(likelihoods) <- 17:23  # Lambda-Werte als Namen hinzufügen
print(likelihoods)

# Bestimmen des maximalen Wertes
max_likelihood <- max(likelihoods)
best_lambda <- as.numeric(names(which.max(likelihoods)))  # Lambda mit maximaler Likelihood

# Ergebnisse ausgeben
cat("Maximale Likelihood:", max_likelihood, "\n")
cat("Lambda mit maximaler Likelihood:", best_lambda, "\n")


