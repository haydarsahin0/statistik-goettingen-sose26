#### VL09 Inferenz-Statistik II ####
###################################

setwd("E:/ownCloud/Statistik4Wiwis/01_StatVorlesung/RscriptsVorlesungStatistik")
set.seed(30041777) # Geburtsdatum Gauss

## Verzerrung und Varianz 
D <- 2e6 # Anzahl der Durchläufe
lambda <- 5 # wahres Lambda
n <- 5# Stichprobengröße
Schaetzer1 <- NULL
Schaetzer2 <- NULL
Schaetzer3 <- NULL
Schaetzer4 <- NULL
for(d in 1:D){
  s <- rpois(n,lambda)
  Schaetzer1.d <- 3
  Schaetzer1 <- c(Schaetzer1,Schaetzer1.d)
  Schaetzer2.d <- s[1]
  Schaetzer2 <- c(Schaetzer2,Schaetzer2.d)
  Schaetzer3.d <- mean(s)
  Schaetzer3 <- c(Schaetzer3,Schaetzer3.d)
  Schaetzer4.d <- 2*mean(s)
  Schaetzer4 <- c(Schaetzer4,Schaetzer4.d)
}
dev.off()
par(mfrow=c(2,2))
par(mar=c(3.5, 3.5, 2, 1))
breaks <- seq(0,20,by=0.25)
hist(Schaetzer1,breaks,main="Schaetzer1",ylab="",xlab="")
hist(Schaetzer2,breaks,main="Schaetzer2",ylab="",xlab="")
hist(Schaetzer3,breaks,main="Schaetzer3",ylab="",xlab="")
hist(Schaetzer4,breaks,main="Schaetzer4",ylab="",xlab="")
## Bias
dev.off()
par(mfrow=c(2,2))
par(mar=c(3.5, 3.5, 2, 1))
breaks <- seq(-10,10,by=0.25)
Abweichung1 <- Schaetzer1 - lambda
hist(Abweichung1,breaks,main="Abweichung1",ylab="",xlab="")
Bias1 <- mean(Schaetzer1) - lambda
Var1 <- sum((Schaetzer1 - mean(Schaetzer1))^2)/length(Schaetzer1)
MSE1 <- sum((Schaetzer1 - lambda)^2)/length(Schaetzer1)

Abweichung2 <- Schaetzer2 - lambda
hist(Abweichung2,breaks,main="Abweichung2",ylab="",xlab="")
Bias2 <- mean(Schaetzer2) - lambda
Var2 <- sum((Schaetzer2 - mean(Schaetzer2))^2)/length(Schaetzer2)
MSE2 <- sum((Schaetzer2 - lambda)^2)/length(Schaetzer2)

Abweichung3 <- Schaetzer3 - lambda
hist(Abweichung3,breaks,main="Abweichung3",ylab="",xlab="")
Bias3 <- mean(Schaetzer3) - lambda
Var3 <- sum((Schaetzer3 - mean(Schaetzer3))^2)/length(Schaetzer4)
MSE3 <- sum((Schaetzer3 - lambda)^2)/length(Schaetzer3)

Abweichung4 <- Schaetzer4 - lambda
hist(Abweichung4,breaks,main="Abweichung4",ylab="",xlab="")
Bias4 <- mean(Schaetzer4) - lambda
Var4 <- sum((Schaetzer4 - mean(Schaetzer4))^2)/length(Schaetzer4)
MSE4 <- sum((Schaetzer4 - lambda)^2)/length(Schaetzer4)

Schaetzer.df <- data.frame(
  Bias=c(Bias1,Bias2,Bias3,Bias4),Var=c(Var1,Var2,Var3,Var4),
  MSE=c(MSE1,MSE2,MSE3,MSE4))
Schaetzer.df


## Kerndichteschätzer
#par(mfrow=c(2,2))
x <- rnorm(100)
kde.default <- density(x)
plot(kde.default)
kde.e1 <- density(x,bw=0.5,kernel="epanechnikov")
plot(kde.e1)
