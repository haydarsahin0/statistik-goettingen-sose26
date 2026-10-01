options(width = 90)
cat("@@CARD1@@\n")
3 + 4      # Kommentar: R als Taschenrechner
2^3
sqrt(16)
cat("@@CARD2@@\n")
round(10/3, 3)
round(10/3, digits = 2)
cat("@@CARD4@@\n")
a <- 7
b <- 3
q <- a / b
q
cat("@@CARD5@@\n")
x <- c(4, 8, 15, 16, 23, 42)
1:20
seq(2, 8, by = 2)
rep(0, 5)
length(x)
sum(x)
cat("@@CARD6@@\n")
x * 1.5
sum(x^2)
cat("@@CARD7@@\n")
x[1]
x[c(1, 3)]
x[length(x)]
x > 10
x[x > 10]
which(x > 10)
cat("@@CARD8@@\n")
sum(x > 10)
mean(x > 10)
is.element(15, x)
x > 5 & x < 20
cat("@@CARD9@@\n")
typeof(x)
class(x)
typeof("Bergtal")
typeof(TRUE)
is.numeric(x)
as.numeric("3.5")
cat("@@CARD10@@\n")
f <- factor(c("ja", "nein", "ja", "ja"), levels = c("ja", "nein"))
f
levels(f)
table(f)
cat("@@CARD11@@\n")
y <- c(3, NA, 5, 8)
mean(y)
mean(y, na.rm = TRUE)
is.na(y)
na.omit(y)
cat("@@CARD12@@\n")
A <- 3:6
B <- 4:2
C <- seq(2, 8, by = 2)
union(A, B)
intersect(A, C)
setdiff(B, C)
is.element(6, C)
cat("@@CARD13@@\n")
paste("Lambda =", 20)
paste0("0.", 1, 2, 3)
cat("Lambda =", 20, "\n")
cat("@@CARD14@@\n")
m <- matrix(c(15, 75, 45, 65), nrow = 2)
m
df <- data.frame(Name = c("Ana", "Ben"), Alter = c(21, 24))
df
dim(df)
cat("@@CARD16@@\n")
setwd(path.expand("~"))
list.files()
d <- read.csv("Taverne.csv", sep = ";", dec = ".", header = TRUE)
head(d)
cat("@@CARD17@@\n")
f <- read.csv("Fahrrad.csv", sep = ";", dec = ",", header = TRUE)
str(f)
cat("@@CARD18@@\n")
str(d)
typeof(d$Tal)
class(d$Muenzen)
cat("@@CARD19@@\n")
nrow(d)
ncol(d)
dim(d)
names(d)
cat("@@CARD20@@\n")
d[3, ]
d$Muenzen
d[d$Tal == "Bergtal", ]
d[which.max(d$Muenzen), ]
cat("@@CARD21@@\n")
s <- subset(d, Kampfzeit >= 5 & Kampfzeit < 60)
nrow(s)
s
cat("@@CARD22@@\n")
d$MproMin <- d$Muenzen / d$Kampfzeit
head(d)
cat("@@CARD24@@\n")
round(mean(d$Kampfzeit), 3)
round(sd(d$Kampfzeit), 3)
cat("@@CARD25@@\n")
n <- length(d$Muenzen)
round(var(d$Muenzen), 3)
round(var(d$Muenzen) * (n - 1) / n, 3)
round(mean(d$Muenzen^2) - mean(d$Muenzen)^2, 3)
cat("@@CARD26@@\n")
median(d$Kampfzeit)
IQR(d$Kampfzeit)
quantile(d$Kampfzeit, 0.9)
quantile(d$Kampfzeit, c(0.25, 0.75))
range(d$Kampfzeit)
summary(d$Kampfzeit)
cat("@@CARD27@@\n")
table(d$Monster)
round(prop.table(table(d$Monster)), 3)
which.max(table(d$Monster))
cat("@@CARD28@@\n")
round(tapply(d$Muenzen, d$Tal, mean), 3)
aggregate(d$Muenzen, by = list(d$Tal), mean)
cat("@@CARD29@@\n")
d$Kampfzeit.3 <- cut(d$Kampfzeit, breaks = c(0, 5, 60, Inf), right = FALSE)
d$Muenzen.4 <- cut(d$Muenzen, breaks = c(0, 10, 20, 30, Inf), right = TRUE)
table(d$Kampfzeit.3)
is.factor(d$Kampfzeit.3)
cat("@@CARD30@@\n")
Kontingenz.Tafel <- table(d$Muenzen.4, d$Kampfzeit.3)
Kontingenz.Tafel
addmargins(Kontingenz.Tafel)
round(prop.table(Kontingenz.Tafel, 1), 3)
cat("@@CARD31@@\n")
s <- subset(d, Kampfzeit >= 5 & Kampfzeit < 60)
round(prop.table(table(s$Muenzen.4)), 2)
cat("@@CARD32@@\n")
round(cor(d$Kampfzeit, d$Muenzen), 3)
round(cor(d$Kampfzeit, d$Muenzen, method = "spearman"), 3)
round(cov(d$Kampfzeit, d$Muenzen), 3)
round(cor(rank(d$Kampfzeit), rank(d$Muenzen)), 3)
cat("@@CARD34@@\n")
pdf("Histogramm.pdf")
hist(d$Kampfzeit, breaks = c(0, 10, 40, 100), freq = FALSE, right = FALSE,
     main = "Sitz 17, Matr.Nr. 12345678, Aufgabenteil e)",
     xlab = "Kampfzeit in Minuten", ylab = "Dichte")
dev.off()
cat("@@CARD35@@\n")
h <- hist(d$Kampfzeit, breaks = c(0, 10, 40, 100), right = FALSE, plot = FALSE)
h$counts
round(h$density, 4)
cumsum(h$counts)
cat("@@CARD36@@\n")
pdf("Streudiagramm.pdf")
plot(d$Kampfzeit, d$Muenzen, pch = 16, cex = 1,
     main = "Streudiagramm", xlab = "Kampfzeit (min.)", ylab = "Muenzen")
dev.off()
cat("@@CARD37@@\n")
pdf("Boxplot.pdf")
boxplot(Muenzen ~ Tal, data = d, main = "Muenzen nach Tal", xlab = "Tal", ylab = "Muenzen")
dev.off()
boxplot(d$Kampfzeit, plot = FALSE)$stats
barplot(table(d$Monster), main = "Monster", ylab = "Anzahl")
cat("@@CARD38@@\n")
pdf("KDE.pdf")
plot(density(f$Dauer), main = "Sitz 17, Matr.Nr. 12345678, Aufgabenteil c)",
     xlab = "Dauer", ylab = "Dichte")
dev.off()
density(f$Dauer)$bw
plot(density(f$Dauer, bw = 5, kernel = "epanechnikov"))
cat("@@CARD39@@\n")
pdf("HistDichte.pdf")
hist(f$Dauer, freq = FALSE, breaks = seq(0, 120, by = 15), ylim = c(0, 0.03),
     main = "Dauer mit Exponentialdichte", xlab = "Dauer", ylab = "Dichte")
x.seq <- seq(0, 120, by = 0.5)
lines(x.seq, dexp(x.seq, rate = 1/35.86), col = 2)
abline(v = mean(f$Dauer), lty = 2)
dev.off()
cat("@@CARD41@@\n")
dbinom(2, size = 10, prob = 0.3)
pbinom(2, 10, 0.3)
1 - pbinom(4, 10, 0.3)
pbinom(5, 10, 0.3) - pbinom(2, 10, 0.3)
qbinom(0.5, 10, 0.3)
dbinom(0:3, 10, 0.3)
cat("@@CARD42@@\n")
1 - ppois(2, lambda = 2)
1 - dpois(0, 2) - dpois(1, 2) - dpois(2, 2)
dpois(0, 2)
ppois(3, 2)
cat("@@CARD43@@\n")
1 - pnorm(505, mean = 500, sd = 5)
pnorm(505, 500, 5) - pnorm(495, 500, 5)
qnorm(0.95, 500, 5)
1 - pnorm((505 - 500) / 5)
qnorm(0.975)
cat("@@CARD44@@\n")
punif(1.5, min = 0, max = 2)
pexp(200, rate = 0.006)
qt(0.975, df = 9)
qchisq(0.95, df = 29)
pgamma(3, shape = 2, rate = 1)
cat("@@CARD45@@\n")
set.seed(123)
x <- rbinom(10000, size = 5, prob = 0.3)
round(prop.table(table(x)), 3)
round(dbinom(0:5, 5, 0.3), 3)
sample(1:6, 10, replace = TRUE)
cat("@@CARD46@@\n")
vals <- 0:15
plot(vals, dpois(vals, 3), pch = 16, main = "Po(3)", xlab = "x", ylab = "P(X = x)")
v <- seq(-3, 3, length.out = 200)
plot(v, dnorm(v), type = "l", main = "N(0,1)", xlab = "x", ylab = "Dichte")
cat("@@CARD48@@\n")
quadsum <- function(x) {
  s <- sum(x^2)
  return(s)
}
quadsum(1:4)
cat("@@CARD49@@\n")
erg <- numeric(5)
for (lambda in 1:5) {
  erg[lambda] <- dpois(3, lambda)
  cat("Lambda =", lambda, "P =", round(erg[lambda], 3), "\n")
}
which.max(erg)
cat("@@CARD50@@\n")
x <- c(4, 8, 15, 16, 23, 42)
ifelse(x > 10, 1, x)
ersetze <- function(v) {
  for (i in 1:length(v)) {
    if (v[i] > 10) { v[i] <- 1 } else { v[i] <- v[i] }
  }
  return(v)
}
ersetze(x)
cat("@@CARD51@@\n")
YenneferZahl.fun <- function(n) {
  y <- "0."
  for (i in 1:n) {
    y <- paste0(y, i)
  }
  return(y)
}
YenneferZahl.fun(17)
cat("@@CARD53@@\n")
d$iL20 <- dpois(d$Muenzen, lambda = 20)
head(d[, c("Muenzen", "iL20")])
L20 <- prod(d$iL20)
L20
format(L20, digits = 4)
cat("@@CARD54@@\n")
Likelihood.pois <- function(lambda, x) {
  L <- prod(dpois(x, lambda))
  return(L)
}
lambdas <- 17:23
Ls <- sapply(lambdas, Likelihood.pois, x = d$Muenzen)
names(Ls) <- lambdas
Ls
lambdas[which.max(Ls)]
cat("@@CARD55@@\n")
prod(dpois(rep(d$Muenzen, 40), 22))
sum(log(dpois(d$Muenzen, 22)))
sum(dpois(d$Muenzen, 22, log = TRUE))
cat("@@CARD56@@\n")
logL.pois <- function(lambda, x) sum(log(dpois(x, lambda)))
opt <- optimise(logL.pois, interval = c(10, 40), x = d$Muenzen, maximum = TRUE)
round(opt$maximum, 3)
cat("@@CARD57@@\n")
x <- f$Dauer
neglogL <- function(t_param, x) {
  param <- exp(t_param)
  alpha <- param[1]
  beta <- param[2]
  return(-sum(log(dgamma(x, alpha, beta))))
}
model <- nlm(neglogL, c(0.01, 0.5), x)
round(exp(model$estimate), 3)
cat("@@CARD58@@\n")
alpha.hat <- exp(model$estimate[1])
beta.hat <- exp(model$estimate[2])
pdf("Gamma.pdf")
hist(x, freq = FALSE, breaks = seq(0, 120, by = 10), ylim = c(0, 0.025),
     main = "Grafik Aufgabenteil k)", xlab = "Dauer", ylab = "Dichte")
x.seq <- seq(0, 120, by = 0.5)
lines(x.seq, dgamma(x.seq, alpha.hat, beta.hat), col = 2)
dev.off()
round(pgamma(30, alpha.hat, beta.hat), 3)
round(qgamma(0.75, alpha.hat, beta.hat), 3)
cat("@@CARD60@@\n")
x <- d$Muenzen
n <- length(x)
alpha <- 0.1
round(mean(x) + c(-1, 1) * qnorm(1 - alpha/2) * 7 / sqrt(n), 3)
round(mean(x) + c(-1, 1) * qt(1 - alpha/2, n - 1) * sd(x) / sqrt(n), 3)
cat("@@CARD61@@\n")
p <- 40/100
round(p + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / 100), 3)
s2 <- var(d$Muenzen)
round(c((n - 1) * s2 / qchisq(0.975, n - 1), (n - 1) * s2 / qchisq(0.025, n - 1)), 3)
cat("@@CARD62@@\n")
tt <- t.test(d$Muenzen, mu = 20, alternative = "greater", conf.level = 0.9)
tt
round(qt(0.9, df = 11), 3)
round(tt$statistic, 3)
round(tt$p.value, 3)
cat("@@CARD63@@\n")
y <- c(19.2, 17.4, 18.5, 16.5, 18.9)
z <- (mean(y) - 17) / (sqrt(2.25) / sqrt(length(y)))
round(z, 3)
round(qnorm(c(0.005, 0.995)), 3)
round(2 * (1 - pnorm(abs(z))), 3)
cat("@@CARD64@@\n")
1 - pbinom(14, 20, 0.5)
sum(dbinom(15:20, 20, 0.5))
cat("@@CARD65@@\n")
tafel <- matrix(c(15, 75, 45, 65), nrow = 2)
test <- chisq.test(tafel, correct = FALSE)
test$expected
round(test$statistic, 3)
round(test$p.value, 4)
cat("@@END@@\n")
