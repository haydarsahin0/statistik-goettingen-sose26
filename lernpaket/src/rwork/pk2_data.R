set.seed(2610)
n <- 60
Fach <- sample(c("Wiwi","Jura","Medizin","Informatik"), n, replace=TRUE, prob=c(.35,.25,.2,.2))
Bereich <- sample(c("Lesesaal","Gruppenraum","Cafe"), n, replace=TRUE, prob=c(.5,.3,.2))
mu <- c(Wiwi=2.6, Jura=3.4, Medizin=3.0, Informatik=2.2)[Fach]
Dauer <- round(rgamma(n, shape=4, rate=4/mu), 2)
Dauer <- pmin(pmax(Dauer, 0.25), 7.9)
Buecher <- rpois(n, 2.3)
d <- data.frame(Besuch=sprintf("B%02d",1:n), Fach=Fach, Bereich=Bereich, Dauer=Dauer, Buecher=Buecher)
write.csv(d, "../../uebungsdaten/Bibliothek.csv", row.names=FALSE)
print(summary(d)); print(table(d$Fach)); print(range(d$Dauer)); print(mean(d$Buecher))
