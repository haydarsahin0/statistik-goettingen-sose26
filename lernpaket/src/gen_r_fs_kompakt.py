# R-Formelsammlung kompakt (Teil B): 2 Seiten, Karten-Layout, jeder Befehl mit türkischer Erklärung
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'extra', 'r_fs_kompakt.html')

# (Kartennummer, Titel, Farbe, [(Code, Türkisch)], Hinweis)
CARDS = [
 ('01', 'Start & Einlesen', '#2563eb', [
  ('setwd(path.expand("~"))', 'Arbeitsverzeichnis setzen (erste Zeile)'),
  ('getwd(); list.files()', 'Ordner / Dateien prüfen'),
  ('d <- read.csv("D.csv")', 'CSV einlesen (sep="," dec=".")'),
  ('read.csv("D.csv", sep=";", dec=",")', 'deutsches Format: ; und Komma 3,5'),
  ('read.csv2("D.csv")', 'dasselbe, Kurzform'),
  ('read.table("D.txt", header=TRUE)', 'Textdatei, 1. Zeile = Spaltennamen'),
  ('head(d); str(d); summary(d)', 'erste Zeilen · Struktur/Typen · Überblick'),
  ('dim(d); nrow(d); names(d)', 'Dimension · Anzahl Zeilen · Spaltennamen'),
 ], 'Zahlen als <code>chr</code>? → <code>dec=","</code> fehlt.'),
 ('02', 'Datentypen', '#7c3aed', [
  ('class(x); typeof(x)', 'Datentyp: numeric / integer / character / factor'),
  ('is.numeric(x); is.character(x)', 'Typ prüfen (TRUE/FALSE)'),
  ('as.numeric(x); as.character(x)', 'Typ umwandeln'),
  ('factor(x); levels(f)', 'in Faktor umwandeln · Kategorien'),
  ('factor(x, levels=c(..), ordered=TRUE)', 'ordinales Merkmal (geordneter Faktor)'),
  ('data.frame(x=c(..), g=c(..))', 'eigenen Dataframe erstellen'),
 ], 'Satz: „Die Variable … ist vom Typ …“'),
 ('03', 'Zugriff & Filtern', '#0891b2', [
  ('d$x;  d[i, ];  d[ , "x"]', 'Spalte · Zeile i · Spalte per Name'),
  ('d$x[d$g == "A"]', 'Werte mit Bedingung (== doppelt!)'),
  ('subset(d, g=="A" & x>3)', 'Teildatensatz (& und, | oder)'),
  ('which(x > 3); which.max(x)', 'Zeilennummern · Position des Maximums'),
  ('sort(x); d[order(d$x), ]', 'sortieren · Datensatz sortieren'),
  ('d$neu <- ifelse(x>30,"a","b")', 'neue Spalte mit Bedingung'),
  ('cut(x, breaks=c(..), right=FALSE)', 'in Klassen einteilen [a,b)'),
  ('is.na(x); mean(x, na.rm=TRUE)', 'fehlende Werte finden · ignorieren'),
  ('unique(x);  "A" %in% x', 'verschiedene Werte · enthalten?'),
 ], ''),
 ('04', 'Rechnen & Mengen', '#0d9488', [
  ('c(); 1:5; seq(0,1,by=.25); rep(2,3)', 'Vektor · Folge · Folge mit Schritt · Wiederholung'),
  ('sum(x); prod(x); length(x)', 'Summe · Produkt · Anzahl'),
  ('cumsum(x); max(x); min(x)', 'kumulierte Summe · Maximum · Minimum'),
  ('sqrt(x); exp(x); log(x)', 'Wurzel · e hoch x · <b>log = ln</b>'),
  ('choose(n,k); factorial(n)', 'Binomialkoeffizient · Fakultät'),
  ('union(A,B); intersect(A,B)', 'Vereinigung ∪ · Schnitt ∩'),
  ('setdiff(A,B); is.element(6,B)', 'Differenz A\\B · Element von?'),
  ('matrix(v, nrow=2); colSums(M)', 'Matrix · Spaltensummen'),
  ('apply(M, 1, sum)', 'Funktion auf jede Zeile (2 = Spalte)'),
  ('for (i in 1:n) { … }', 'Schleife: wiederhole für i = 1…n'),
 ], ''),
 ('05', 'Häufigkeiten', '#16a34a', [
  ('table(x)', 'absolute Häufigkeiten'),
  ('prop.table(table(x))', 'relative Häufigkeiten (Summe 1)'),
  ('cumsum(prop.table(table(x)))', 'kumulierte rel. Häufigkeiten = empir. Verteilungsfunktion'),
  ('Fh <- ecdf(x); Fh(2)', '\\(\\hat F(2)\\) = Anteil „≤ 2“'),
  ('table(x, y); addmargins(t)', 'Kontingenztafel · mit Randsummen'),
  ('prop.table(t, margin=1)', 'bedingte Häufigkeiten je Zeile (2 = Spalte)'),
 ], ''),
 ('06', 'Lage & Streuung', '#ca8a04', [
  ('mean(x); median(x)', 'arithmetisches Mittel · Median'),
  ('names(which.max(table(x)))', 'Modus (häufigster Wert)'),
  ('var(x); sd(x)', 'unverzerrte Varianz \\(s_*^2\\), Std.abw. \\(s_*\\) (<b>n−1</b>)'),
  ('var(x)*(n-1)/n', 'empirische Varianz \\(s^2\\) (durch n)'),
  ('quantile(x, c(.25,.5,.75))', 'Quantile (Vorlesung: <code>type=2</code>)'),
  ('IQR(x); range(x)', 'Interquartilsabstand · Min und Max'),
  ('tapply(d$x, d$g, mean)', 'Mittelwert je Gruppe'),
  ('aggregate(x ~ g, data=d, mean)', 'dasselbe als Tabelle'),
 ], '<code>var</code>, <code>sd</code>, <code>cov</code> teilen durch n−1!'),
 ('07', 'Zusammenhang', '#ea580c', [
  ('cov(x, y); cor(x, y)', 'Kovarianz (n−1) · Korrelation nach Bravais-Pearson'),
  ('cor(x, y, method="spearman")', 'Rangkorrelation nach Spearman'),
  ('chisq.test(t)$expected', 'erwartete Häufigkeiten bei Unabhängigkeit'),
  ('chisq.test(t, correct=FALSE)$statistic', 'χ²-Koeffizient'),
 ], ''),
 ('08', 'Grafiken', '#dc2626', [
  ('pdf("a.pdf") … dev.off()', 'Grafik als PDF speichern (auch png())'),
  ('hist(x, breaks=c(..), right=FALSE, freq=FALSE)', 'Histogramm: Klassengrenzen, links geschlossen, Dichte'),
  ('main=, xlab=, ylab=', 'Titel (Aufgabe + Matrikel-Nr. + Platz), Achsen'),
  ('lines(density(x))', 'Kerndichteschätzer ins Histogramm'),
  ('density(x, bw=2, kernel="epanechnikov")', 'KDE mit Bandweite und Kern'),
  ('boxplot(y ~ g, data=d)', 'Boxplot je Gruppe'),
  ('plot(x, y); abline(lm(y ~ x))', 'Streudiagramm + Regressionsgerade'),
  ('barplot(table(x))', 'Säulendiagramm'),
  ('plot(ecdf(x))', 'empirische Verteilungsfunktion zeichnen'),
  ('curve(dexp(x, r), add=TRUE)', 'theoretische Dichte einzeichnen'),
  ('par(mfrow=c(1,2))', 'zwei Grafiken nebeneinander'),
 ], ''),
 ('09', 'Verteilungen d · p · q · r', '#9333ea', [
  ('dbinom(k, n, p)', '\\(P(X=k)\\) Binomialverteilung'),
  ('pbinom(k, n, p)', '\\(P(X\\le k)\\)'),
  ('1 - pbinom(k-1, n, p)', '\\(P(X\\ge k)\\) (<b>k−1</b>!)'),
  ('dpois(k, λ); ppois(k, λ)', 'Poissonverteilung'),
  ('pnorm(x, μ, σ); qnorm(p, μ, σ)', 'Normalverteilung (σ = Std.abw., nicht Varianz!)'),
  ('pexp(x, rate=λ); qexp(p, λ)', 'Exponentialverteilung, λ = 1/Mittelwert'),
  ('punif(x, a, b); dgeom(k, p)', 'Gleichverteilung · geometrische Vert.'),
  ('dgamma(x, shape, rate)', 'Dichte der Gammaverteilung'),
  ('qt(.975, df); qchisq(.95, df)', 't- und χ²-Quantile'),
  ('1 - pnorm(z); 1 - pt(t, df)', 'p-Wert rechtsseitig'),
  ('rbinom(N,n,p); rnorm(N,μ,σ)', 'Zufallszahlen erzeugen'),
 ], 'd = Dichte/W\'keit · p = Verteilungsfunktion (≤) · q = Quantil · r = Zufallszahlen'),
 ('10', 'Simulation', '#db2777', [
  ('set.seed(123)', 'Zufall reproduzierbar machen'),
  ('sample(1:6, 5, replace=TRUE)', '5-mal würfeln (mit Zurücklegen)'),
  ('mean(x == 3)', 'relative Häufigkeit ≈ Wahrscheinlichkeit'),
 ], ''),
 ('11', 'Likelihood & ML', '#1d4ed8', [
  ('prod(dpois(x, λ))', '<b>Likelihood</b> = Produkt der Wahrscheinlichkeiten'),
  ('sum(dpois(x, λ, log=TRUE))', '<b>Log-Likelihood</b> = Summe der Logarithmen'),
  ('sum(log(dgamma(x, a, b)))', 'bei Produkt = 0 (Underflow) Logs summieren'),
  ('L <- function(l) prod(dpois(x, l))', 'Likelihood als Funktion definieren'),
  ('for (l in 17:23) print(L(l))', 'Gitter: L für jedes λ (offizielle Lösung)'),
  ('g <- 17:23; g[which.max(sapply(g, L))]', 'Gitter: bestes λ in einer Zeile'),
  ('optimize(f, c(0.1,5), maximum=TRUE)', 'numerisches Maximum (1 Parameter)'),
  ('mean(x);  1/mean(x)', 'Kontrolle: Poisson \\(\\hat\\lambda=\\bar x\\) · Exp \\(1/\\bar x\\)'),
 ], 'Satz: „Das Maximum der Likelihood liegt bei λ = …“'),
 ('11b', 'nlm (mehrere Parameter)', '#1e40af', [
  ('nl <- function(tp, x) -sum(log(dgamma(x, exp(tp[1]), exp(tp[2]))))', '<b>negative</b> Log-Likelihood; <code>exp()</code> macht Parameter positiv'),
  ('m <- nlm(nl, p=c(0,0), x=x)', 'minimieren (Startwerte p)'),
  ('exp(m$estimate)', 'zurücktransformieren → \\(\\hat\\alpha,\\hat\\beta\\)'),
  ('-m$minimum', 'maximale Log-Likelihood'),
 ], 'Warnungen „NA/Inf replaced“ sind normal.'),
 ('12', 'Konfidenzintervalle', '#0f766e', [
  ('mean(x)+c(-1,1)*qnorm(.975)*σ/sqrt(n)', 'KI für μ, σ bekannt'),
  ('mean(x)+c(-1,1)*qt(.975,n-1)*sd(x)/sqrt(n)', 'KI für μ, σ unbekannt'),
  ('t.test(x, conf.level=.95)$conf.int', 'dasselbe automatisch'),
  ('p+c(-1,1)*qnorm(.975)*sqrt(p*(1-p)/n)', 'KI für einen Anteil'),
  ('(n-1)*var(x)/qchisq(c(.975,.025), n-1)', 'KI für die Varianz'),
 ], ''),
 ('13', 'Hypothesentests', '#b91c1c', [
  ('t.test(x, mu=μ0, alternative="greater")', 't-Test, H₁: μ > μ0 ("less" <, "two.sided" ≠)'),
  ('t.test(...)$p.value; $statistic', 'p-Wert · Prüfgröße'),
  ('(mean(x)-μ0)/(σ/sqrt(n))', 'Gauß-Test von Hand; p = 1-pnorm(z)'),
  ('chisq.test(table(x, y))', 'χ²-Unabhängigkeitstest'),
  ('chisq.test(table(x), p=c(..))', 'χ²-Anpassungstest'),
  ('binom.test(k, n, p=.5, alternative="greater")', 'exakter Binomialtest'),
  ('qt(.95, df)', 'kritischer Wert / Ablehnungsbereich'),
 ], '<b>p ≤ α → H₀ ablehnen.</b> „Da der p-Wert … kleiner als α ist, wird H₀ abgelehnt …“'),
 ('14', 'Regression', '#4f46e5', [
  ('m <- lm(y ~ x, data=d); coef(m)', 'a (Achsenabschnitt) und b (Steigung)'),
  ('summary(m)$r.squared', 'Bestimmtheitsmaß R²'),
  ('summary(m)$coefficients', 'Koeffizienten + p-Werte'),
  ('predict(m, data.frame(x=40))', 'Prognose für x = 40'),
  ('resid(m)', 'Residuen \\(y-\\hat y\\)'),
 ], ''),
 ('15', 'Ausgabe & Runden', '#475569', [
  ('round(x, 3)', 'auf 3 Nachkommastellen runden (immer!)'),
  ('sprintf("%.20f", x)', 'feste Anzahl Nachkommastellen ausgeben'),
  ('z <- "0."; for (i in 1:54) z <- paste0(z, i)', 'Yennefer-Zahl: 99 Nachkommastellen (Altklausur h)'),
  ('options(scipen=999)', 'keine Darstellung wie e-131'),
  ('paste("a", 1); cat("n =", n)', 'Text + Zahl verbinden / ausgeben'),
 ], ''),
]

FEHLER = [
 ('mehr Spalten als Spaltennamen', '<code>sep=";", dec=","</code> ergänzen'),
 ('cannot open file / Datei nicht gefunden', '<code>setwd</code> + <code>list.files()</code> prüfen'),
 ('object not found', 'Tippfehler / Groß-Klein, Objekt fehlt'),
 ('could not find function', 'Befehl falsch geschrieben'),
 ('Argument nicht numerisch → NA', 'Spalte ist Text: <code>dec</code> / <code>as.numeric</code>'),
 ('Ergebnis NA', '<code>na.rm=TRUE</code>'),
]

SAETZE = [
 ('Typ', '„Die Variable <i>x</i> ist vom Typ <i>integer</i>.“'),
 ('Lage', '„Das arithmetische Mittel von <i>x</i> beträgt 30.637.“'),
 ('Likelihood', '„Die Likelihood unter λ = 20 beträgt 6.938 · 10⁻¹³¹.“'),
 ('ML', '„Das Maximum der Likelihood liegt bei λ = 22; der ML-Schätzer ist 22.“'),
 ('Test', '„Da der p-Wert 0.001 kleiner als α = 0.05 ist, wird H₀ abgelehnt. Es ist abgesichert, dass …“'),
 ('KI', '„Das 95 %-KI lautet [28.935; 32.340].“'),
]

CSS = r'''<style>
@page{size:A4;margin:7mm 7mm 8mm}
.w{width:auto!important;padding:0!important}
body{background:#f4f6fb!important;font-family:Inter,Arial,sans-serif;font-size:9.1px!important;line-height:1.32!important;color:#0f172a}
.hero{display:flex;justify-content:space-between;align-items:flex-end;background:linear-gradient(120deg,#0f172a,#1e3a8a 60%,#2563eb);color:#fff;border-radius:9px;padding:3mm 4mm;margin-bottom:2.2mm}
.hero h1{font:800 19px Inter;margin:0!important;color:#fff!important;letter-spacing:-.01em}
.hero .s{font-size:8.4px;opacity:.85;margin-top:.6mm}
.hero .chip{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);border-radius:20px;padding:.8mm 3mm;font-weight:700;font-size:8.4px;white-space:nowrap}
.flow{display:flex;gap:1.4mm;margin-bottom:2.2mm}
.flow div{flex:1;background:#fff;border-radius:6px;padding:1.2mm 1.8mm;border:1px solid #e2e8f0;font-size:8.6px}
.flow b.n{display:inline-block;width:12px;height:12px;border-radius:50%;background:#1e3a8a;color:#fff;text-align:center;line-height:12px;font-size:7px;margin-right:3px}
.grid{column-count:3;column-gap:2mm}
.card{break-inside:avoid;background:#fff;border-radius:7px;margin:0 0 2mm;border:1px solid #e2e8f0;box-shadow:0 .4mm 1mm rgba(15,23,42,.06);overflow:hidden}
.card .hd{display:flex;align-items:center;gap:1.6mm;padding:1.1mm 2mm;border-bottom:1px solid #eef2f7}
.card .no{background:var(--c);color:#fff;border-radius:4px;font:800 9px Inter;padding:.3mm 1.3mm}
.card .ti{font:800 10.6px Inter;color:var(--c)}
.card table{width:100%;border-collapse:collapse;table-layout:fixed}
.card td.t{word-break:break-word}
.card td{padding:.6mm 1.6mm;vertical-align:top;border-bottom:1px dotted #e5e7eb}
.card tr:last-child td{border-bottom:0}
.card td.k{width:56%}
.card code.c{display:inline-block;font:8.5px/1.32 "JetBrains Mono",monospace;font-variant-ligatures:none;background:#0f172a;color:#e2e8f0;border-radius:3px;padding:.25mm 1mm;white-space:pre-wrap;word-break:break-word}
.card td.t{color:#334155}
.card .ft{background:color-mix(in srgb,var(--c) 9%,#fff);color:#1e293b;padding:.8mm 2mm;font-size:8.6px;border-top:1px solid #eef2f7}
code{font-family:"JetBrains Mono",monospace;font-size:.95em;font-variant-ligatures:none;background:#eef2ff;border-radius:2px;padding:0 1px}
.katex{font-size:1.02em}
.mini td{font-size:7.2px}
</style>'''

def card(no, title, color, rows, foot):
    h = f'<div class="card" style="--c:{color}"><div class="hd"><span class="no">{no}</span><span class="ti">{title}</span></div><table>'
    for c, t in rows:
        h += f'<tr><td class="k"><code class="c">{html.escape(c)}</code></td><td class="t">{t}</td></tr>'
    h += '</table>'
    if foot: h += f'<div class="ft">{foot}</div>'
    return h + '</div>'

def build():
    h = [CSS, '<div class="hero"><div><h1>R-Formelsammlung · Teil B</h1><div class="s">Alle Befehle für die ILIAS-Klausur · jeder Befehl mit kurzer Erklärung · Details & echte Outputs: R_Befehle_TeilB.pdf</div></div><div class="chip">60 min · 45 Punkte</div></div>']
    h.append('<div class="flow">'
             '<div><b class="n">1</b>Code schreiben, mit <b>Strg+Enter</b> ausführen</div>'
             '<div><b class="n">2</b><b>Code + Output</b> → ILIAS-Box</div>'
             '<div><b class="n">3</b>Ergebnis <code>round(…, 3)</code></div>'
             '<div><b class="n">4</b>2. Box: <b>ganzer Antwortsatz</b></div>'
             '<div><b class="n">5</b>Skript oft speichern · Grafiken hochladen</div></div>')
    h.append('<div class="grid">')
    for c in CARDS:
        h.append(card(*c))
    h.append(card('!', 'Fehlermeldungen', '#be123c', FEHLER, ''))
    h.append(card('✎', 'Antwortsätze (ILIAS)', '#15803d', [(k, v) for k, v in SAETZE], 'Nicht-numerische Antworten immer als <b>ganzer Satz</b>.').replace('<code class="c">', '<code class="c" style="background:#15803d">'))
    h.append('</div>')
    open(OUT, 'w').write('\n'.join(h))
    print(OUT)

if __name__ == '__main__':
    build()
