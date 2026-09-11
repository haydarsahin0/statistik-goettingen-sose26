#### VL10 Inferenz-Statistik III ####
#####################################

rm(list=ls())
setwd("E:/ownCloud/Statistik4Wiwis/01_StatVorlesung/RscriptsVorlesungStatistik")
set.seed(30041777) # Geburtsdatum Gauss

## Erwartungswerte und deren Wahrscheinlichkeiten
x <- rbinom(10,10,0.5)
x
probs <- dbinom(1:10,10,0.5)
plot(1:10,probs)

probs <- dbinom(1:100,100,0.5)
plot(1:100,probs)

## Konfidenzintervalle (mit bek. Varianz)
alpha <- 0.1
wahresd <- 2
n <- 10
wahremu <- 20
x <- rnorm(n,wahremu,wahresd)
(xbar <- mean(x))
(KIl <- xbar-qnorm(1-alpha/2)*wahresd/sqrt(n))
(KIu <- xbar+qnorm(1-alpha/2)*wahresd/sqrt(n))

## Konfidenzintervalle (mit unbek. Varianz)
(KIl <- mean(x)-qt(1-alpha/2,n-1)*sd(x)/sqrt(n))
(KIu <- mean(x)+qt(1-alpha/2,n-1)*sd(x)/sqrt(n))

## Konfidenzitnervall für Varianz mit Chisq Verteilung
sdhat <- sd(x)
(KIl <- (n-1)*sdhat^2/qchisq(1-alpha/2,n-1))
(KIu <- (n-1)*sdhat^2/qchisq(alpha/2,n-1))

## Approximativer Erwartungswert nach zentralem Grenzwertsatz
wahremu <- 20
wahrevar <- 2^2
n <- 10
xbarwerte <- seq(15,25,by=0.1)
plot(xbarwerte,dnorm(xbarwerte,wahremu,sqrt(wahrevar)/sqrt(n)),type="l")

## Konfidenzintervall für den Anteilswert
alpha <- 0.1
n <- 10
wahrepi <- 0.5
x <- rbinom(1,n,0.5)
pihat <- x/n
(KIl <- pihat-qnorm(1-alpha/2)*sqrt((pihat*(1-pihat)/n)))
(KIu <- pihat+qnorm(1-alpha/2)*sqrt((pihat*(1-pihat)/n)))
