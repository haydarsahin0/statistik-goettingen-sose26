#### VL09 Inferenz-Statistik II ####
###################################

setwd("E:/ownCloud/Statistik4Wiwis/01_StatVorlesung/RscriptsVorlesungStatistik")
set.seed(30041777) # Geburtsdatum Gauss

## Kerndichteschätzer
#par(mfrow=c(2,2))
x <- rnorm(100)
kde.default <- density(x)
plot(kde.default)
kde.e1 <- density(x,bw=0.5,kernel="epanechnikov")
plot(kde.e1)
