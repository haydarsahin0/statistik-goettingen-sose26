#### VL05 Grundlagen III ####
#############################

set.seed(30041777) # Geburtsdatum Gauss

## Binomialverteilung
dbinom(x=0:3,size=3,prob=0.5)
pbinom(q=0:3,size=3,prob=0.5)
qbinom(p=0.5,size=3,prob=0.5)
rbinom(n=3,size=3,prob=0.5)

par(mfrow=c(1,2))
vals <- 0:3
plot(vals,dbinom(vals,3,0.5),main="Wahrscheinlichkeitsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,pch=16)
plot(vals,pbinom(vals,3,0.5),main="Verteilungsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,pch=16)

## Poissonverteilung
dpois(x=0:5,lambda= 3)
ppois(q=0:5,lambda= 3)
qpois(p=0.1991483,lambda=3)
rpois(n=1,lambda= 3)

vals <- 0:15
plot(vals,dpois(vals,3),main="Wahrscheinlichkeitsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,pch=16)
plot(vals,ppois(vals,3),main="Verteilungsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,pch=16)

## Gleichverteilung
dunif(x = 1, min= 0, max= 2)
punif(q = 1.5, min= 0, max= 2)
qunif(p = 0.75, min= 0, max= 2)
runif(n = 3, min= 0, max= 2)

vals <- seq(-0.5,2.5,length.out=1000)
plot(vals,dunif(vals,0,2),main="Dichtefunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,type="l")
plot(vals,punif(vals,0,2),main="Verteilungsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,type="l")

## Exponentialverteilung
dexp(x=100,rate=0.006)
pexp(q=200,rate=0.006)
qexp(p=0.6988058, rate = 0.006)
rexp(n=3, rate= 0.006)

vals <- seq(-1,1000,by=0.1)
Rate <- 1e-3
plot(vals,dexp(vals,Rate),main="Dichtefunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,type="l")
plot(vals,pexp(vals,Rate),main="Verteilungsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,type="l")

## Gaußsche Normalverteilung
dnorm(x=190,mean=183,sd=14)
pnorm(q=190,mean=183,sd=14)
qnorm(p=0.6914625,mean=183,sd=14)
rnorm(n=3,mean=183,sd=14)

vals <- seq(-2,2,length.out=1000)
mu <- 0
sigma <- 1
plot(vals,dnorm(vals,mu,sigma),main="Dichtefunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,type="l")
plot(vals,pnorm(vals,mu,sigma),main="Verteilungsfunktion",xlab="X",ylab="Wahrscheinlichkeit",
     las=1,type="l")

