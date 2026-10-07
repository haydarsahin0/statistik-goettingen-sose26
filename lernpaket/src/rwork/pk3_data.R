# Probeklausur 3: Datensatz Fitness.csv erzeugen + alle Kontrollrechnungen Teil A
set.seed(910)
n <- 80
Studio <- sample(c("Nord","Sued","Zentrum"), n, replace=TRUE, prob=c(.3,.3,.4))
Abo <- ifelse(runif(n) < c(Nord=.3, Sued=.5, Zentrum=.4)[Studio], "Premium", "Basic")
Minuten <- round(rnorm(n, 66, 14) + ifelse(Abo=="Premium", 5, 0))
Besuche <- rpois(n, 2.5)
Wartezeit <- pmax(round(rexp(n, 0.45), 2), 0.05)
d <- data.frame(Mitglied=sprintf("M%02d",1:n), Studio, Abo, Minuten, Besuche, Wartezeit)
write.csv(d, "../../uebungsdaten/Fitness.csv", row.names=FALSE)
print(summary(d))
