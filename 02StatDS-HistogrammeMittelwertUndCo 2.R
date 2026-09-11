################################################
#### Kapitel 2 Statistik und Data Science 1 ####
################################################

rm(list=ls())

# Illustrationsbspiel: Zimmergrößen
x <- c(22,12,8,20,35,20,18,60,15,20,18 ,13,20,74, 15, 24,
       18,18,16,22,13,19, 80, 27,14,15, 15,30, 9, 67, 
       24,20, 10, 15, 77, 12, 10, 9, 27, 18, 9, 9, 13, 25, 8,
       28, 11, 29, 54, 28, 8, 22, 7, 73, 
       44 )# aus pad
# Variante 1: Alle Auspr?gungsm?glichkeiten
(a1a <- unique(x))
(a1b <- sort(a1a))
# Variante 2: cut Befehl
(a2a <- cut(x,c(0,10,20,100),include.lowest=TRUE))
(a2b <- cut(x,c(0,10,20,100),right=FALSE))
(a2c <- cut(x,c(0,exp(1),2*pi,Inf),right=FALSE,include.lowest=TRUE))
(a2d <- cut(x,c(0,exp(1),2*pi,Inf),right=FALSE,include.lowest=TRUE,
           labels=c("<Euler","Euler->2Pi",">2Pi")))
# Variante 3: Grundmengen
G <- 1:100 # Grundmenge
P <- c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97) # Primzahlen
Pc<- setdiff(G,P) # Komplement
is.element(x,P)
(a3 <- factor(ifelse(is.element(x,P),"P","Pc"),
       levels=c("P","Pc"),
       labels = c("Prime","no Prime")))

############################
# Häufigkeitsverteilungen #
############################

## Häufigkeitstabellen - mit Variante 2b
table(a2b) # absolute Häufigkeit
table(a2b)/sum(table(a2b)) # relative Häufigkeit

## Säulendiagramm
hist(x,freq=TRUE)
hist(as.numeric(a2b),breaks=seq(min(as.numeric(a2b))-0.5,max(as.numeric(a2b))+0.5,by=1),xaxt="n")
axis(1,1:max(as.numeric(a2b)),levels(a2b),cex.axis=0.4)

## Histogramm
pdf("MeinErsteHistogramm.pdf")
h <- hist(x,breaks=c(0,10,20,100),right=FALSE,
     main="Ein Histogramm von Wohnraum",
     xlab="Wohnraum in qm",ylab="Dichte")
dev.off()
str(h)
h$density
h$counts

hist(x)

#############
# Lagemaße #
#############

## Mittelwert
x <- c(x,NA) # NA ergänzen
mean(x, na.rm = TRUE)

## Modus
x <- na.omit(x) # NA wieder rausnehmen
which(table(x)==max(table(x)))

## Median
quantile(x,0.5)

#################
# Streuungsmaße #
#################

#Varianz und Standardabweichung
var(x)
sd(x)

#Interquartilsabstand
quantile(x,0.75)-quantile(x,0.25) # 


#################
# Boxplot #
#################
boxplot(x, range=1.5,main="Boxplot", ylab="Zimmergrößen", horizontal=FALSE)





