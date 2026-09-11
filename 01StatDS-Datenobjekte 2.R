#######################
#### Vorlesung 01 #####
#######################

## Datenobjekte in R
# Vektoren
x  <- c(1,2,3)
print(x)
y  <- c(1,5,9)
y
(z  <- c("A","B","C"))
(l  <- x>=y)
f <- factor(c("a","b","a","a"),levels=c("a","b"))
f

# Matritzen
M1 <- matrix(1:6,nrow=2)
M1
M2 <- matrix(1:6,nrow=2,byrow=TRUE)
M2
M3 <- cbind(x,y)
M3
M4 <- cbind(x,z)
M4

# Listen
L <- list()
L$x <- x
L$z <- z
L$M <- M1
L
L$x
L$M

d <- data.frame(x=x,z=z)
d

## Objekttypen
# mode(x)
typeof(x)

# x.int <- as.integer(x)
# mode(x.int)
# typeof(x.int)

z <- c("x","y","z")
# mode(z)
typeof(z)

# mode(l)
typeof(l)

## Objekttypen nutzen
is.numeric(x)
is.logical(x)
is.matrix(x)
is.vector(x)

as.numeric(f)
as.numeric(f)-1

length(x)

dim(x) # funktioniert nur f?r Matritzen und Data frames
dim(M1)
dim(d)

## Aufgabenbeispiel
library("AER")
library("arules")
data(CPS1988)

names(CPS1988)[1:3]<- c("wage","edu","exp")
CPS1988 <- subset(CPS1988,exp>=0)
CPS1988$exp2 <- discretize(CPS1988$exp,method="fixed",breaks=c(0,10,25,50,100,Inf))
head(CPS1988)
d <- CPS1988[,c(1,2,8,6)]
head(d)
d[c(1,11356,20499),]
typeof(d)
dim(d)
is.factor(d[,3])
is.character(d[,4])


### SG1.4: Ein erstes statstisches Ma? und dessen Anwendung

# Das Iris Dataset
library("datasets")
data(iris) # Iris, introduced by Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems, contains three plant species (setosa, virginica, versicolor) and four features measured for each sample. These quantify the morphologic variation of the iris flower in its three species, all measurements given in centimeters.
d <- iris
names(d)
which(names(d)==c("Sepal.Length"))
which(names(d)==c("Species"))
d[1:5,c(1,5)]
sample(1:dim(iris)[1],dim(iris)[1],replace=FALSE)
set.seed(123)
d2 <- d[sample(1:dim(iris)[1],15,replace=FALSE),c(1,5)]
d2

# Das arithmetische Mittel
mean(d2$Sepal.Length)
mean(iris$Sepal.Length)

# Das arithmetische Mittel f?r Gruppen (der lange Weg)
means <- rep(NA,3)
means[1] <- mean(subset(d2,Species=="setosa")$Sepal.Length)
means[2] <- mean(subset(d2,Species=="versicolor")$Sepal.Length)
means[3] <- mean(subset(d2,Species=="virginica")$Sepal.Length)

means
round(means,digits=1)

# Das arithmetische Mittel f?r Gruppen (der kurze Weg)
list(d2$Species),list(d2$Species),mean)
aggregate(d2$Sepal.Length,by=list(d2$Species),mean)
