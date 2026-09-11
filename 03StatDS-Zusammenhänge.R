################################################
#### Kapitel 3 Statistik und Data Science 1 ####
################################################

## Datengenerierung
set.seed(30041777) # Geburtsdatum Gauss
x <- rnorm(1000)
y <- rnorm(1000)

## Kontingenztafel
breaks.x <- c(-5,-1,1,5)
x_c <- cut(x, breaks=breaks.x) # Gruppierungen per cut definieren
y_c <- cut(y, 4)#cut(y, c(-Inf,0,10,100)) # Gruppierungen per cut definieren
z <- table(x_c, y_c) # Abs.H?ufigkeiten in Kontingenztafel
z
z.r <- table(x_c,y_c)/sum(table(x_c,y_c)) # Rel. H?ufigkeiten in Kontigenztafel
z.r

## Randverteilungen
apply(z.r,1,sum)
apply(z.r,2,sum)

## Bedingte Verteilungen
### bedingte Verteilung nach X
z.bv.x <- diag(1/apply(z,1,sum)) %*% z
apply(z.bv.x, 1, sum)

### bedingte Verteilung nach Y
z.bv.y <- z %*% diag(1/apply(z,2,sum))
apply(z.bv.y, 2, sum)

## Chisq Koeffizient
### Kontingenztafel unter Unabhängigkeitsannahme
z.tilde <- apply(z,1,sum) %*% t(apply(z,2,sum))/sum(z)
### Chisq Koeffizient
(chisq.koef <- sum((z-z.tilde)^2/z.tilde))

## Streudiagramme
plot(x,y, main="Ein Streudiagramm",pch=16,cex=0.1)
## Mit Opacity & Overlays
plot(x,y, main="Ein Streudiagramm",pch=16,col=grey(0.2,alpha=0.3))

## 3d Histogram
hist(x)
hist(x,breaks=breaks.x)
hist(as.numeric(x_c),breaks=seq(0.5,3.5),freq=FALSE)
#install.packages("plot3D", repos='http://cran.us.r-project.org') # uncomment - needed for Jupyter Notebooks
library(plot3D)
hist3D(z=z, border="black",phi=40,theta=130,zlab="h(x,y)",breaks=seq(0,250,by=25),NAcol=jet.col(5)[1]) #phi=vertical angle, theta= horizontal angle

##  Plot as a 2D heatmap:
image2D(z=z, border="black",las=1,breaks=seq(0,250,by=25),NAcol=jet.col(5)[1])

## Korrelationsmaße
## Pearson 
mean.x <- mean(x)
mean.y <- mean(y)
x.demeaned <- x-mean.x
y.demeaned <- y-mean.y
xy.demeaned<- x.demeaned*y.demeaned
sum(x.demeaned^2)
sum(y.demeaned^2)
sum(xy.demeaned)
(cor.pearson <- sum(xy.demeaned)/(sqrt(sum(x.demeaned^2)*sum(y.demeaned^2))))
cor(x,y, method="pearson")

## Spearman
x.rk <-rank(x)
y.rk <- rank(y)
xy.rk<- x.rk-y.rk
sum(xy.rk^2)
(cor.spearman <- 1-6*sum(xy.rk^2)/(length(x)*(length(x)^2-1)))
cor(x,y, method="spearman")
