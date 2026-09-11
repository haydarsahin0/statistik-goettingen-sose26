#### VL11 Hypothesentests II ####
#################################

#### Tests bei Normalvert. und bekannter Varianz

### Ablehnungsbereich
x <- c(19.2,17.4,18.5,16.5,18.9)
xbar <- mean(x)
n <- length(x)
mu0 <- 17
var <- 2.25
alpha <- 0.01

## ohne Standardisierung
(A1 <- qnorm(alpha/2,mu0,sqrt(var)/sqrt(n)))
(A2 <- qnorm(1-alpha/2,mu0,sqrt(var)/sqrt(n)))

## mit Standardisierung
(z <- (xbar-mu0)/(sqrt(var)/sqrt(n)))
(A1.z <- qnorm(alpha/2))
(A2.z <- qnorm(1-alpha/2))

#### p-Wert
2*(1-pnorm(xbar,mu0,sqrt(var)/sqrt(n)))
2*(1-pnorm(z))

#### Konfidenzintervall
(KIug <- qnorm(alpha/2,xbar,sqrt(var)/sqrt(n)))
(KIog <- qnorm(1-alpha/2,xbar,sqrt(var)/sqrt(n)))

#### Tests bei Normalvert. und unbekannter Varianz
x <- c(19.2,17.4,18.5,16.5,18.9)
xbar <- mean(x)
n <- length(x)
mu0 <- 17
s2 <- sd(x)^2
alpha <- 0.01

## mit Standardisierung
(t <- (xbar-mu0)/(sqrt(s2)/sqrt(n)))
(A1.t <- qt(alpha/2,n-1))
(A2.t <- qt(1-alpha/2,n-1))

## mit t.test - Gleichseitig
ttest.obj <- t.test(x, mu = 17,alternative="two.sided",
                    conf.level=0.01)
ttest.obj$estimate # Punktschätzer für mu
ttest.obj$statistic # T-Statistik
ttest.obj$p.value # P-Wert für H0
ttest.obj$conf.int # KI für mu

#### Tests bei Normalvert. für Varianz
sigma0 <- 2
(z <- (n-1)*sd(x)^2 / sigma0^2)
(A1.chisq <- qchisq(alpha/2,n-1))
(A1.chisq <- qchisq(1-alpha/2,n-1))
## !!!nicht chisq.test!!!
# chisqtest.obj <- chisq.test(x, )

#### Unabhängigkeitstest
Kontingenztafel <- matrix(c(140,144,80,91,21,19,57,64,43,53,101,85,47,55),nrow=2)
(chisqtest.obj <-chisq.test(Kontingenztafel))
chisqtest.obj$expected
chisqtest.obj$statistic
chisqtest.obj$p.value

#### Anpassungstest

