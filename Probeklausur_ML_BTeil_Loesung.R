# Übungsaufgaben zur Maximum-Likelihood-Schätzung
# Lösungen

# set.seed 
set.seed(1234)

# a) Working Directory festlegen
# In der Klausur: setwd(path.expand("~"))
setwd("~/ownCloud/Statistik 1 Vorlesung (ab WS25-26)/Statistik und Data Science 1/Testate/Probeklausuren") # mit Ihrem eigenen Pfad ersetzen!
getwd() # Working Directory überprüfen

# b) 
# Datensatz einlesen (read.csv) und als dataframe in R abspeichern (df <- )
df <- read.csv("Lungenvolumen.csv", header=TRUE, dec = ".", sep = ";") # hier reicht auch der default von read.csv("Lungenvolumen.csv")
# alternativ:  df <- read.table("Lungenvolumen.csv", header=TRUE, dec = ".")

# Gibt den ersten Teil des dataframes zurück, standardmäßig die ersten sechs Einträge
head(df)

# Struktur des dataframes
str(df)

# c) Objekttyp
class(df$Lungenvolumen)
typeof(df$Lungenvolumen)

# Antwortsatz: Die Variable Lungenvolumen besitzt den Objekttypen numeric. Genauer gesagt handelt es sich dabei um eine Fließkommazahl (double). 

# d) Wertebereich & Varianz
round(range(df$Lungenvolumen), 2)
round(var(df$Lungenvolumen), 2)

# Antwortsatz: Der Wertebereich der Variable Lungenvolumen beträgt [0.04, 7.52]. Die unverzerrte Varianz von Lungenvolumen beträgt 1.68.

# e) Histogramm 
pdf("Histogramm.pdf")
hist(df$Lungenvolumen,
     freq = FALSE, # freq=FALSE: normiertes Histogram (default: freq=TRUE, mit absoluten Häufigkeiten)
     right = TRUE, # right=TRUE: die rechte Intervallgrenze ist geschlossen (default: right=TRUE)
     xlab = "Lungenvolumen", 
     ylab = "Wahrscheinlichkeitsdichte", 
     main = "Grafik Aufgabenteil e)")
dev.off()

# f) Problemstellung
# Antwortsatz: Bei der direkten Optimierung der Likelihood in R tritt das 
# Problem des numerical underflow auf, wobei sehr kleine Werte zu 0 abgerundet 
# werden, was die Güte der Schätzung beeinträchtigt.
# Üblicherweise wird die Likelihood logarithmiert, um dieses Problem zu umgehen.

# Erklärung und Beispiel:

# Bei direkter Optimierung der Likelihood besteht das Risiko eines
# "numerical underflow", der zu Fehlern bei der Optimierung führen kann
# "numerical underflow" bedeutet, dass zu 0 abgerundet wird, was die Schätzung beeinträchtigt

# Beispiel für Gammaverteilung unser Daten mit den Parametern alpha=0.01  und beta=0.5:
# dgamma steht für die Dichtefunktion der Gamma-Verteilung in R
dgamma(df$Lungenvolumen,0.01,0.5) # unsere Beispieldaten haben alle sehr kleine Werte 
hist(dgamma(df$Lungenvolumen,0.01,0.5)) # offensichtlich liegen Daten zwischen 0 und 1
min(dgamma(df$Lungenvolumen,0.01,0.5)) # sehr kleiner Minimalwert (0.00003159143)
prod(dgamma(df$Lungenvolumen,0.01,0.5)) # Dieses Produkt ist eigentlich nicht Null, 
                                # sondern nur ein extrem kleiner Wert, den R 
                                # zu Null abrundet (= "numerical underflow")

       
# Lösung: Log-Likelihood optimieren
# Beispiel:
# statt Produkt aus den sehr kleinen Werten: 
prod(dgamma(df$Lungenvolumen,0.01,0.5)) # (hier wird zu Null abgerundet)
# summieren wir jetzt die Logs auf und erhalten einen Wert
log(dgamma(df$Lungenvolumen,0.01,0.5))
# Summe der individuellen Log-Likelihoods
sumoflogs <- sum(log(dgamma(df$Lungenvolumen,0.01,0.5))) 
sumoflogs

# Rücktransformation:
# exp(log-likelihood) = likelihood
exp(sumoflogs)
# Bei Optimierungen muss man die Rücktransformation oft gar nicht durchführen, 
# da der Optimierungsalgorithmus nur die Log-Likelihood maximiert.

# g) 
# Antwortsatz: Die Parameter der Gamma-Verteilung sind standardgemäß auf den 
# Raum der positiven reellen Zahlen [0,inf) restringiert. 
# Die Optimierung über nlm geht aber von nicht-restringierten Parametern im 
# gesamten Raum der reellen Zahlen (-Inf, Inf) aus. 
# Wenn die nlm-Funktion die negativen Werte ausprobiert,
# findet R keine Ergebnisse und gibt hier Fehler bzw. NaNs aus.
# Wir müssen daher die Funktionsparameter transformieren (hier alpha^t, beta^t):
# Für die spätere Optimierung mittels der nlm-Funktion in R 
# müssen wir die positiv definierten Verteilungsparameter der
# Gammaverteilung so transformieren, dass sie sich über den 
# gesamten Raum der reellen Zahlen erstrecken.


# h) neglogL-Funktion
x <- df$Lungenvolumen # zur einfacheren Ansprache der Daten

neglogL <- function(transformed_param,x){
  param <- exp(transformed_param) # param: ausschließlich positive Parameter 
                                  # alpha und beta der Gammaverteilung
                                  # exp() stellt sicher, dass diese positiv sind
                                  # transformed_param: von -Inf bis Inf, im ganzen 
                                  # Raum der reellen Zahlen definierte Parameter, 
                                  # so wie sie in die nlm-Funktion 
                                  # eingefügt werden können 
  alpha <- param[1] # positives alpha der Gammaverteilung
  beta <- param[2] # positives beta der Gammaverteilung
  logLi <- log(dgamma(x,alpha,beta)) # individuelle Log-Likelihoods der Gammaverteilung
  logL <- sum(logLi) # Summe der indiv. Log-Likelihoods
  neglogL<- logL*(-1) # negative Log-Likelihood bilden
  return(neglogL) 
}
# zur Verdeutlichung des Zusammenhangs der Transformation:
curve(exp(x), -3, 3, xlab="transformed_param", ylab="param")

# i)
model <- nlm(neglogL,c(0.01,0.5),x)
model
# Die Warnungen entstehen durch ungültige Parameter-Werte während der Iterationen, 
# die numerisch instabil werden (z. B. alpha oder beta nahe 0). Das passiert häufig 
# bei Optimierungsverfahren wie nlm, da während der Suche Parameter ausprobiert werden, 
# die außerhalb des gültigen Bereichs liegen. Diese Warnungen können in diesem Fall 
# ignoriert werden, da das Modell trotzdem konvergiert. Die initialen Werte für 
# die Optimierung waren möglicherweise zu klein.

# j) 
# Rücktransformation der Schätzer von alpha^t.hat und beta^t.hat 
# aus der Funktion zu den Schätzern der Verteilungsparameter
# alpha.hat und beta.hat

alpha_t.hat <- model$estimate[1] # [1] wählt die erste Spalte von model$estimate aus  
beta_t.hat <- model$estimate[2] # [2] wählt die zweite Spalte von model$estimate aus

alpha.hat <- exp(model$estimate[1]) # exp() gibt positiven Wert für den alpha-Schätzer der Gammaverteilung 
beta.hat <- exp(model$estimate[2]) # exp() gibt positiven Wert für den beta-Schätzer der Gammaverteilung 
alpha.hat
beta.hat

# Antwortsatz: Der rücktransformierte geschätzte Wert des Formparameters 
# alpha.hat beträgt 2.116; der rücktransformierte Wert des Skalenparameters 
# beta.hat beträgt 1.090.

# k)
hist(x,
     freq=FALSE, 
     xlab = "Lungenvolumen", 
     ylab = "Wahrscheinlichkeitsdichte", 
     main = "Grafik Aufgabenteil l)", 
     ylim=c(0, 0.4)) # für vollständige Darstellung der Dichteverteilung
x.seq <- seq(0,8,by=0.01)
lines(x.seq,dgamma(x.seq,alpha.hat,beta.hat),col=2)

#l)
pgamma(3,alpha.hat,beta.hat)

# Antwortsatz: Die Wahrscheinlichkeit, bei der parametrischen Schätzung
# einen Wert von max. 3 Liter Lungenvolumen zu erhalten,
# beträgt 0.818.

#m)
qgamma(0.75,alpha.hat,beta.hat)

# Antwortsatz: Ab einem Wert von 2.603 Litern gehört ein Mensch zu den 25%
# mit dem größten Lungenvolumen (nach dem geschätzten Modell).

