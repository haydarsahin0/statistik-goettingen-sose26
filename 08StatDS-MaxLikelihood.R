#### VL08 Inferenz-Statistik I ####
###################################

setwd("E:/ownCloud/Statistik4Wiwis/01_StatVorlesung/RscriptsVorlesungStatistik")
set.seed(30041777) # Geburtsdatum Gauss
library("xtable")

### Beispiel Münzwurf (mit anderen Zahlen)
Wuerfe <- rbinom(20,1,0.3)
x <- sum(Wuerfe)
#### Likelihoods für ein Wurf
Likelihood.fun <- function(par,x,N){
  L <- dbinom(x,N,par)
  return(L)
}
Likelihood.fun(0.5,x,20) # Likelihood für faire Münze

# diverse Likelihoods
pis <- seq(0.1,0.9,by=0.1)
Likelihoods <- Likelihood.fun(pis,x,20)
matrix(c(pis,Likelihoods),byrow=FALSE,nrow=length(pis))

plot(pis,Likelihoods,main="Likelihoods ein Wurf")

#### Mit mehreren Beobachtungen
#### Likelihoods für Apfelkonsum
Likelihood.fun <- function(lambda,x){
  L <- prod(dpois(x,lambda))
  return(L)
}

#### Likelihoods für Apfelkonsum
LogLikelihood.fun <- function(lambda,x){
  logL <- sum(log(dpois(x,lambda)))
  return(logL)
}

## Beispiel 
Apfelkonsum <- rpois(5,4) 
plot(1:10,rep(0,10),type="n",ylim=c(0,10e-5))
for(lambda.i in 1:10){
  cat(paste("Lamda =",lambda.i,"\n"))
  L.i <- Likelihood.fun(lambda.i,Apfelkonsum)
  l.i <- LogLikelihood.fun(lambda.i,Apfelkonsum)
  cat(paste("Likelihood",L.i,"\n"))
  cat(paste("LogLikelihood",l.i,"\n"))
  points(lambda.i,L.i)
}

### Beispiel Numerical Underflow
Apfelkonsum <- rpois(1000,4) 

for(lambda.i in 1:10){
  cat(paste("Lamda =",lambda.i,"\n"))
  L.i <- Likelihood.fun(lambda.i,Apfelkonsum)
  cat(paste("Likelihood",L.i,"\n"))
}

for(lambda.i in 1:10){
  cat(paste("Lamda =",lambda.i,"\n"))
  L.i <- Likelihood.fun(lambda.i,Apfelkonsum)
  l.i <- LogLikelihood.fun(lambda.i,Apfelkonsum)
  cat(paste("Likelihood",L.i,"\n"))
  cat(paste("LogLikelihood",l.i,"\n"))
}


## Normalverteilung & num. Max.
x <- rnorm(10,mean=0)
Likelihood.mu <- function(mu,x){
  L <- prod(dnorm(x,mean=mu))
  return(L) 
}
optimise(Likelihood.mu,interval=c(-3,3),x,maximum=TRUE)

## Bivariate Likelihood Funktion
# generating data and true data generating pdf
library("mvtnorm")
set.seed(30041777) # Geburtsdatum Gauss
n <- 100
mu <- c(0.1,-0.2)
cov <- matrix(c(1.5,-0.5,-0.5,0.5),nrow=2)
xy <- rmvnorm(n, mu, cov )
plot(xy[,1],xy[,2],xlim=c(-3.5,3.5),ylim=c(-3.5,3.5),pch=16,
     xlab="x",ylab="y")
x.seq <- y.seq <- seq(-3.5,3.5,by=0.1)
den.m <- matrix(NA,length(x.seq),length(y.seq))
for(i in 1:length(x.seq)){
  for(j in 1:length(y.seq)){
    den.m[i,j] <- dmvnorm(c(x.seq[i],y.seq[j]),mu,cov)
  }
}
contour(x.seq,y.seq,den.m,add=TRUE,nlevels=5,lwd=2,col=2)

# bivariate Likelihood Funktion
logL.fun2 <- function(param,cov,xy){
  mu <- param
  cov <- cov
  n <- nrow(xy)
  lis <- rep(NA,n)
  for(i in 1:n){
    lis[i] <- log(dmvnorm(c(xy[i,1],xy[i,2]),mu,cov))
  }
  logL <- sum(lis)
  return(logL)
}

# multivariate Likelihood Funktion
logL.fun5 <- function(wparam,xy){
  nparam <- c(wparam[1:2],exp(wparam[3:4]),wparam[5]) # natural paramaters = exp(working parameters) f?r Varianzen, sodass >0
  mu <- nparam[1:2]
  cov <- matrix(c(nparam[3],nparam[5],nparam[5],nparam[4]),nrow=2) 
  n <- nrow(xy)
  lis <- rep(NA,n)
  for(i in 1:n){
    lis[i] <- log(dmvnorm(c(xy[i,1],xy[i,2]),mu,cov))
  }
  logL <- sum(lis)
  return(logL)
}

nlogL.fun5 <- function(param,xy){
  n.logL <- -logL.fun5(param,xy)
  return(n.logL)
}

maxL5est <-nlm(nlogL.fun5,p=c(1,1,1,1,1),xy=xy,print.level=1)
wparam.est <- maxL5est$estimate
nparam.est <- c(wparam.est[1:2],exp(wparam.est[3:4]),wparam.est[5])
(mu.est <- nparam.est[1:2])
(cov.est <- matrix(c(nparam.est[3],nparam.est[5],nparam.est[5],nparam.est[4]),nrow=2) )


den.m5 <- matrix(NA,length(x.seq),length(y.seq))
for(i in 1:length(x.seq)){
  for(j in 1:length(y.seq)){
    den.m5[i,j] <- dmvnorm(c(x.seq[i],y.seq[j]),mu.est,cov.est)
  }
}
contour(x.seq,y.seq,den.m5,add=TRUE,nlevels=5,col="blue")
