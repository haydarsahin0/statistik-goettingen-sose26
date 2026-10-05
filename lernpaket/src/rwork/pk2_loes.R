## a)
# setwd(path.expand("~"))
## b)
d <- read.csv("Bibliothek.csv", sep=",", dec=".", header=TRUE)
head(d)
## c)
typeof(d$Fach)
typeof(d$Buecher)
## d)
round(mean(d$Dauer), 3)
round(sd(d$Dauer), 3)
## e)
pdf("Histogramm.pdf")
hist(d$Dauer, freq=FALSE, breaks=c(0,1,2,3,5,8), right=FALSE,
     main="Sitz 00, Matr.Nr. 12345678, Aufgabenteil e)",
     xlab="Aufenthaltsdauer in Stunden", ylab="Dichte")
dev.off()
h <- hist(d$Dauer, breaks=c(0,1,2,3,5,8), right=FALSE, plot=FALSE); print(h$counts); print(round(h$density,4))
## f)
round(tapply(d$Dauer, d$Fach, mean), 3)
## g)
d$iL2 <- dpois(d$Buecher, lambda=2)
head(d)
(L2 <- prod(d$iL2))
## h)
Likelihood.pois <- function(lambda, x){
  L <- prod(dpois(x, lambda))
  return(L)
}
for(lambda in seq(1.5, 3, by=0.25)){
  print(c(lambda, Likelihood.pois(lambda, d$Buecher)))
}
## i)
t.test(d$Dauer, mu=2.5, alternative="greater")
