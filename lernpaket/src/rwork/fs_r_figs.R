## Abbildungen für die Formelsammlung R (werden als PNG in fig/ abgelegt)
invisible(Sys.setlocale("LC_ALL", "C.UTF-8"))
d <- read.csv("../../uebungsdaten/Taverne.csv", sep = ";", dec = ".", header = TRUE)
f <- function(name, expr) { png(file.path("..", "fig", name), width = 1500, height = 1150, res = 230); par(mar = c(4.2, 4.2, 3, 1)); expr; dev.off() }
f("fsr_hist.png", hist(d$Muenzen, breaks = c(5, 15, 20, 25, 35), right = FALSE, freq = FALSE,
                       main = "Sitz 17, Matr.Nr. 12345678, Aufgabenteil e)", xlab = "Muenzen", ylab = "Dichte",
                       col = "#bfe5d3", border = "#047857", cex.main = 0.95))
f("fsr_box.png", boxplot(Muenzen ~ Tal, data = d, main = "Aufgabenteil f)", xlab = "Tal", ylab = "Muenzen",
                         col = "#bfe5d3", border = "#064e3b"))
f("fsr_scatter.png", { plot(d$Kampfzeit, d$Muenzen, pch = 16, col = "#064e3b", main = "Aufgabenteil g)",
                            xlab = "Kampfzeit in Minuten", ylab = "Muenzen")
                       abline(lm(Muenzen ~ Kampfzeit, data = d), col = "red", lwd = 2) })
f("fsr_kde.png", { hist(d$Kampfzeit, freq = FALSE, col = "#e7f6ef", border = "#047857", main = "Histogramm + KDE",
                        xlab = "Kampfzeit", ylab = "Dichte", ylim = c(0, 0.02))
                   lines(density(d$Kampfzeit), lwd = 2, col = "#064e3b")
                   lines(density(d$Kampfzeit, bw = 10, kernel = "epanechnikov"), lwd = 2, lty = 2, col = "red")
                   legend("topright", c("gaussian (Standard)", "epanechnikov, bw = 10"), lty = c(1, 2), col = c("#064e3b", "red"), bty = "n", cex = 0.8) })
