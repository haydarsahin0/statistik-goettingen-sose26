"""Abschnitte 3–5: Spezielle Verteilungen, Schätzer und Dichteschätzung, Maximum-Likelihood."""
from fractions import Fraction as Fr
import math
from itertools import product
from scipy import stats
from skcommon import sec, card, T, r3, r4, r2, fr, log

N = stats.norm

# ======================================================================
sec("3 · Spezielle Verteilungen (V07)", None,
    ["<table class='tab' style='font-size:.86rem;margin:.1em 0'><tr><th>Verteilung</th><th>wann?</th><th>\\(P(X=x)\\) bzw. \\(f(x)\\)</th><th>\\(E(X)\\)</th><th>\\(Var(X)\\)</th><th>R</th></tr>"
     "<tr><td>Bernoulli \\(Be(\\pi)\\)</td><td>ein Versuch, ja/nein</td><td>\\(\\pi\\) (x=1), \\(1-\\pi\\) (x=0)</td><td>\\(\\pi\\)</td><td>\\(\\pi(1-\\pi)\\)</td><td>–</td></tr>"
     "<tr><td>Binomial \\(B(n,\\pi)\\)</td><td>Anzahl Erfolge in n unabhängigen Versuchen</td><td>\\(\\binom nx\\pi^x(1-\\pi)^{n-x}\\)</td><td>\\(n\\pi\\)</td><td>\\(n\\pi(1-\\pi)\\)</td><td>binom</td></tr>"
     "<tr><td>Poisson \\(Po(\\lambda)\\)</td><td>Anzahl Ereignisse pro Zeitraum, ohne Obergrenze</td><td>\\(\\frac{\\lambda^x}{x!}e^{-\\lambda}\\)</td><td>\\(\\lambda\\)</td><td>\\(\\lambda\\)</td><td>pois</td></tr>"
     "<tr><td>Gleich \\(U(a,b)\\)</td><td>jeder Wert in [a, b] gleich plausibel</td><td>\\(\\frac1{b-a}\\)</td><td>\\(\\frac{a+b}2\\)</td><td>\\(\\frac{(b-a)^2}{12}\\)</td><td>unif</td></tr>"
     "<tr><td>Exponential \\(Exp(\\lambda)\\)</td><td>Wartezeit / Dauer bis zum Ereignis</td><td>\\(\\lambda e^{-\\lambda x}\\), \\(F=1-e^{-\\lambda x}\\)</td><td>\\(\\frac1\\lambda\\)</td><td>\\(\\frac1{\\lambda^2}\\)</td><td>exp</td></tr>"
     "<tr><td>Normal \\(N(\\mu,\\sigma^2)\\)</td><td>Messwerte, Summen/Mittelwerte (ZGWS)</td><td>\\(\\frac1{\\sqrt{2\\pi\\sigma^2}}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}\\)</td><td>\\(\\mu\\)</td><td>\\(\\sigma^2\\)</td><td>norm</td></tr></table>",
     "<b>Standardisieren:</b> \\(Z=\\frac{X-\\mu}{\\sigma}\\sim N(0,1)\\), \\(F(x)=\\Phi\\left(\\frac{x-\\mu}{\\sigma}\\right)\\), \\(\\Phi(-z)=1-\\Phi(z)\\). Quantile: \\(q_\\alpha=\\mu+\\sigma z_\\alpha\\); \\(z_{0.9}=1.28\\), \\(z_{0.95}=1.645\\), \\(z_{0.975}=1.96\\), \\(z_{0.99}=2.33\\), \\(z_{0.995}=2.58\\).",
     "<b>ZGWS:</b> Für iid \\(X_i\\) mit \\(E=\\mu\\), \\(Var=\\sigma^2\\) gilt \\(\\bar X\\overset{a}{\\sim}N\\left(\\mu,\\frac{\\sigma^2}n\\right)\\) – egal welche Verteilung die \\(X_i\\) haben.",
     "<b>R:</b> d… = \\(P(X=x)\\) bzw. Dichte · p… = \\(P(X\\le x)\\) · q… = Quantil · r… = Zufallszahlen. In R immer <b>σ</b> (sd) angeben, in der Notation \\(N(\\mu,\\sigma^2)\\) die <b>Varianz</b>!"])

# --- 3.1 Welche Verteilung
card("Welche Verteilung passt? (Erkennen + Parameter)", 85,
 "Geben Sie jeweils eine geeignete Verteilung mit Parametern an: (a) Anzahl defekter Teile unter 20 zufällig (mit Zurücklegen) geprüften, Ausschussquote 3 %. (b) Anzahl Notrufe pro Stunde, im Mittel 4. (c) Zeit bis zum nächsten Notruf in Stunden. (d) Ein Münzwurf (Kopf = 1). (e) Füllmenge einer Flasche, Mittel 500 ml, Standardabweichung 3 ml. (f) Ankunftszeit eines Busses, gleich wahrscheinlich zwischen 0 und 10 Minuten. <span class='pt'>(6 P)</span>",
 ["Zählen mit fester Obergrenze n (Versuche)? → Binomial. Nur ein Versuch → Bernoulli.",
  "Zählen ohne Obergrenze pro Zeitraum? → Poisson (λ = mittlere Anzahl).",
  "Dauer / Wartezeit? → Exponential (λ = 1 / mittlere Dauer).",
  "Messwert symmetrisch um einen Mittelwert? → Normal. „Gleich wahrscheinlich in [a, b]“ → Gleichverteilung.",
  "Parameter immer dazuschreiben: \\(N(500,\\,9)\\) mit <b>Varianz</b> 9."],
 "(a) \\(X\\sim B(20;\\,0.03)\\) · (b) \\(X\\sim Po(4)\\) · (c) \\(X\\sim Exp(4)\\) (Mittel 1/4 Stunde) · (d) \\(X\\sim Be(0.5)\\) · (e) \\(X\\sim N(500;\\,9)\\) · (f) \\(X\\sim U(0;\\,10)\\)",
 "Poisson vs. Exponential: Poisson zählt Ereignisse (diskret), Exponential misst die Zeit dazwischen (stetig). Gleiche Rate λ!")

# --- 3.2 Bernoulli
pairs = list(product(range(1, 7), repeat=2)); pi3 = Fr(sum((a + b) % 3 == 0 for a, b in pairs), 36)
assert pi3 == Fr(1, 3)
card("Bernoulliverteilung", 40,
 "Zwei faire Würfel werden geworfen. X = 1, wenn die Augensumme durch 3 teilbar ist, sonst X = 0. Geben Sie die Verteilung von X an und berechnen Sie \\(E(X)\\) und \\(Var(X)\\). <span class='pt'>(3 P)</span>",
 ["Nur zwei Werte (0 und 1), ein Versuch → Bernoulli.", "π = P(X = 1) durch Abzählen: Summen 3, 6, 9, 12."],
 "Summe 3: 2 Paare, 6: 5, 9: 4, 12: 1 → 12 Paare → \\(\\pi=\\frac{12}{36}=\\frac13\\)<br>\\(X\\sim Be\\left(\\tfrac13\\right)\\), \\(E(X)=\\tfrac13=\\mathbf{0.333}\\), \\(Var(X)=\\tfrac13\\cdot\\tfrac23=\\tfrac29=\\mathbf{0.222}\\)")

# --- 3.3 Binomial per Hand
b = stats.binom(8, 1 / 3)
P0, P1, P2 = Fr(2, 3) ** 8, 8 * Fr(1, 3) * Fr(2, 3) ** 7, 28 * Fr(1, 9) * Fr(2, 3) ** 6
assert abs(float(P0 + P1 + P2) - b.cdf(2)) < 1e-12
card("Binomialverteilung per Hand", 85,
 "(Fortsetzung) Das Würfelexperiment wird 8-mal unabhängig wiederholt. Y = Anzahl der Würfe mit durch 3 teilbarer Summe. Geben Sie die Verteilung von Y an, berechnen Sie \\(E(Y)\\), \\(Var(Y)\\) sowie per Hand \\(P(Y=2)\\) und \\(P(Y\\le2)\\). <span class='pt'>(7 P)</span>",
 ["n unabhängige Wiederholungen eines Bernoulli-Versuchs → \\(Y\\sim B(n,\\pi)\\).",
  "\\(\\binom nx=\\frac{n!}{x!(n-x)!}\\), z. B. \\(\\binom82=\\frac{8\\cdot7}{2}=28\\). Taschenrechner: nCr.",
  "\\(P(Y\\le2)=P(Y=0)+P(Y=1)+P(Y=2)\\) – jeden Summanden einzeln."],
 T("\\(Y\\sim B\\left(8,\\tfrac13\\right)\\), \\(E(Y)=\\tfrac83=\\mathbf{2.667}\\), \\(Var(Y)=8\\cdot\\tfrac13\\cdot\\tfrac23=\\tfrac{16}9=\\mathbf{1.778}\\)<br>"
   "\\(P(Y=2)=\\binom82\\left(\\tfrac13\\right)^2\\left(\\tfrac23\\right)^6=28\\cdot\\tfrac19\\cdot\\tfrac{64}{729}=\\mathbf{«p2»}\\)<br>"
   "\\(P(Y=0)=\\left(\\tfrac23\\right)^8=«p0»\\), \\(P(Y=1)=8\\cdot\\tfrac13\\left(\\tfrac23\\right)^7=«p1»\\)<br>"
   "\\(P(Y\\le2)=«p0»+«p1»+«p2x»=\\mathbf{«s»}\\)",
   p2=r3(float(P2)), p0=r4(float(P0)), p1=r4(float(P1)), p2x=r4(float(P2)), s=r3(float(P0 + P1 + P2))),
 "Zwischenergebnisse mit 4 Nachkommastellen, erst das Endergebnis auf 3 runden.", fig=("sk_bin.svg", 55))

# --- 3.4 Binomial umschreiben (R)
b2 = stats.binom(10, .25)
v = dict(a=r3(b2.pmf(7)), b=r3(b2.cdf(3)), c=r3(1 - b2.cdf(5)), d=r3(b2.cdf(5) - b2.cdf(2)), e=r3(1 - b2.cdf(2)))
card("Binomial: „mindestens“, „mehr als“, „zwischen“ umschreiben", 75,
 "\\(Y\\sim B(10;\\,0.25)\\). Geben Sie R-Befehle an für (i) \\(P(Y=7)\\), (ii) \\(P(Y<4)\\), (iii) \\(P(Y>5)\\), (iv) \\(P(2<Y<6)\\), (v) \\(P(Y\\ge3)\\). Aus einem Sack mit 60 schwarzen und 20 gelben Kugeln wird 5-mal mit Zurücklegen gezogen. Vervollständigen Sie: <code>x &lt;- __binom(10000, size = __, prob = __)</code>. <span class='pt'>(7 P)</span>",
 ["pbinom(k, …) liefert immer \\(P(Y\\le k)\\). Alles andere umschreiben.",
  "\\(P(Y<4)=P(Y\\le3)\\) · \\(P(Y>5)=1-P(Y\\le5)\\) · \\(P(Y\\ge3)=1-P(Y\\le2)\\) · \\(P(2<Y<6)=P(Y\\le5)-P(Y\\le2)\\).",
  "Simulation: Zufallszahlen = <b>r</b>binom. π = 20/80 = 0.25."],
 T("(i) <code>dbinom(7, 10, 0.25)</code> = «a» · (ii) <code>pbinom(3, 10, 0.25)</code> = «b»<br>"
   "(iii) <code>1 - pbinom(5, 10, 0.25)</code> = «c» · (iv) <code>pbinom(5, 10, 0.25) - pbinom(2, 10, 0.25)</code> = «d»<br>"
   "(v) <code>1 - pbinom(2, 10, 0.25)</code> = «e»<br>Lücken: <code>rbinom(10000, size = 5, prob = 0.25)</code>", **v),
 "Diskret: \\(P(Y<4)\\neq P(Y\\le4)\\). Bei stetigen Verteilungen ist das egal.")

# --- 3.5 Poisson
lam = 2.5; po = stats.poisson(lam)
card("Poissonverteilung per Hand", 75,
 "In einem Callcenter gehen im Mittel 2.5 Anrufe pro Minute ein. X = Anzahl Anrufe in einer Minute. Geben Sie die Verteilung, \\(E(X)\\) und \\(Var(X)\\) an. Berechnen Sie per Hand \\(P(X=0)\\), \\(P(X=3)\\) und \\(P(X\\ge2)\\). Wie groß ist \\(P(\\text{kein Anruf in 2 Minuten})\\)? <span class='pt'>(7 P)</span>",
 ["Anzahl pro Zeitraum, keine Obergrenze → Poisson, λ = Mittelwert.", "\\(E(X)=Var(X)=\\lambda\\).",
  "\\(P(X\\ge2)=1-P(X=0)-P(X=1)\\).", "Doppelter Zeitraum → doppelte Rate: in 2 Minuten λ = 5."],
 T("\\(X\\sim Po(2.5)\\), \\(E(X)=Var(X)=2.5\\)<br>\\(P(X=0)=e^{-2.5}=\\mathbf{«a»}\\) · \\(P(X=3)=\\frac{2.5^3}{3!}e^{-2.5}=\\mathbf{«b»}\\)<br>"
   "\\(P(X\\ge2)=1-e^{-2.5}-2.5\\,e^{-2.5}=\\mathbf{«c»}\\)<br>2 Minuten: \\(Po(5)\\): \\(P(Y=0)=e^{-5}=\\mathbf{«d»}\\)",
   a=r3(po.pmf(0)), b=r3(po.pmf(3)), c=r3(1 - po.cdf(1)), d=r3(math.exp(-5))),
 "R-Variante (Testat 4): \\(P(Y>2)\\) für \\(Po(2)\\) ist <code>1-ppois(2, 2)</code> oder <code>1-dpois(0,2)-dpois(1,2)-dpois(2,2)</code>. Falsch wären <code>1-dpois(2,2)</code> und <code>1-ppois(3,2)</code>.")

card("Ist die transformierte Variable noch poissonverteilt?", 35,
 "\\(X\\sim Po(3)\\) sei die Anzahl Tore pro Spiel. Ein Sponsor spendet \\(Z=2X+4\\) Gutscheine. Berechnen Sie \\(E(Z)\\) und \\(Var(Z)\\). Ist Z poissonverteilt? <span class='pt'>(3 P)</span>",
 ["Rechenregeln: \\(E(2X+4)=2E(X)+4\\), \\(Var(2X+4)=4\\,Var(X)\\).", "Poisson hätte \\(E=Var\\). Vergleichen!"],
 "\\(E(Z)=2\\cdot3+4=\\mathbf{10}\\), \\(Var(Z)=4\\cdot3=\\mathbf{12}\\)<br>\\(E(Z)\\neq Var(Z)\\) → Z ist <b>nicht</b> poissonverteilt (außerdem nimmt Z nur gerade Werte ≥ 4 an).")

# --- 3.6 Gleichverteilung
card("Gleichverteilung U(a, b)", 50,
 "Die Wartezeit X (Minuten) sei \\(U(2,10)\\)-verteilt. Geben Sie Dichte und Verteilungsfunktion an. Berechnen Sie \\(P(X>7)\\), \\(P(3<X<5)\\), \\(E(X)\\), \\(Var(X)\\) und das 90 %-Quantil. <span class='pt'>(7 P)</span>",
 ["\\(f(x)=\\frac1{b-a}\\) auf [a, b]. Wahrscheinlichkeit = Breite × Höhe.", "\\(F(x)=\\frac{x-a}{b-a}\\) in [a, b], links 0, rechts 1.",
  "Quantil: \\(F(q)=0.9\\) nach q auflösen → \\(q=a+0.9(b-a)\\)."],
 "\\(f(x)=\\tfrac18\\) für \\(2\\le x\\le10\\), 0 sonst · \\(F(x)=0\\) (x < 2), \\(\\tfrac{x-2}{8}\\) (2 ≤ x ≤ 10), 1 (x > 10)<br>"
 "\\(P(X>7)=\\tfrac38=\\mathbf{0.375}\\) · \\(P(3<X<5)=\\tfrac28=\\mathbf{0.25}\\)<br>"
 "\\(E(X)=\\tfrac{2+10}2=\\mathbf{6}\\) · \\(Var(X)=\\tfrac{8^2}{12}=\\tfrac{16}3=\\mathbf{5.333}\\) · \\(q_{0.9}=2+0.9\\cdot8=\\mathbf{9.2}\\)")

# --- 3.7 Exponential
card("Exponentialverteilung: λ aus dem Mittelwert", 70,
 "Ein Fuchs braucht im Mittel 3 Stunden, bis er eine Gans fängt. Modellieren Sie die Jagdzeit X mit einer geeigneten stetigen Verteilung. Berechnen Sie \\(P(X>10)\\), \\(P(X\\le1)\\), \\(Var(X)\\) und den Median. <span class='pt'>(6 P)</span>",
 ["Dauer → Exponential. \\(E(X)=\\frac1\\lambda=3\\Rightarrow\\lambda=\\frac13\\).",
  "\\(P(X>x)=1-F(x)=e^{-\\lambda x}\\). \\(P(X\\le x)=1-e^{-\\lambda x}\\).",
  "Median: \\(1-e^{-\\lambda m}=0.5\\Rightarrow m=\\frac{\\ln2}{\\lambda}\\)."],
 T("\\(X\\sim Exp\\left(\\tfrac13\\right)\\)<br>\\(P(X>10)=e^{-10/3}=\\mathbf{«a»}\\) · \\(P(X\\le1)=1-e^{-1/3}=\\mathbf{«b»}\\)<br>"
   "\\(Var(X)=\\frac1{\\lambda^2}=\\mathbf{9}\\) · Median \\(=3\\ln2=\\mathbf{«c»}\\)", a=r3(math.exp(-10 / 3)), b=r3(1 - math.exp(-1 / 3)), c=r3(3 * math.log(2))),
 "Falle: λ ist <b>nicht</b> der Mittelwert (3), sondern 1/3. In R: <code>1 - pexp(10, 1/3)</code>. Dichtewerte (dexp) sind keine Wahrscheinlichkeiten – Summen von dexp-Werten sind falsch (Tutorium 7, Aufg. 3h).",
 fig=("sk_exp.svg", 52))

# --- 3.8 Normal standardisieren
z1, z2, z3 = 5 / 3, 2 / 3, -4 / 3
card("Normalverteilung: standardisieren", 90,
 "Das Gewicht X von Mehlpackungen sei \\(N(500,\\,9)\\)-verteilt. Bestimmen Sie \\(P(X>500)\\), \\(P(X\\ge505)\\) und \\(P(496\\le X\\le502)\\). Vervollständigen Sie den R-Befehl <code>pnorm((__ - __)/__) - pnorm((__ - __)/__)</code> für die letzte Wahrscheinlichkeit. <span class='pt'>(6 P)</span>",
 ["\\(\\sigma=\\sqrt9=3\\) (nicht 9!).", "\\(z=\\frac{x-\\mu}{\\sigma}\\), dann \\(\\Phi(z)\\) aus Tabelle/R. Negative z: \\(\\Phi(-z)=1-\\Phi(z)\\).",
  "\\(P(X>500)\\): μ ist die Mitte → 0.5 ohne Rechnung."],
 T("\\(P(X>500)=\\mathbf{0.5}\\)<br>\\(P(X\\ge505)=1-\\Phi\\left(\\tfrac{505-500}{3}\\right)=1-\\Phi(1.6667)=1-«f1»=\\mathbf{«a»}\\)<br>"
   "\\(P(496\\le X\\le502)=\\Phi(0.6667)-\\Phi(-1.3333)=«f2»-«f3»=\\mathbf{«b»}\\)<br>"
   "<code>pnorm((502 - 500)/3) - pnorm((496 - 500)/3)</code>",
   f1=r4(N.cdf(z1)), a=r3(1 - N.cdf(z1)), f2=r4(N.cdf(z2)), f3=r4(N.cdf(z3)), b=r3(N.cdf(z2) - N.cdf(z3))),
 "Mit Tabelle wird z oft auf 2 Stellen gerundet (Φ(1.67) = 0.9525). Kleine Abweichungen in der 3. Stelle werden dann akzeptiert – den Weg zeigen!",
 fig=("sk_norm.svg", 60))

# --- 3.9 Quantil Normal
q95 = 175 + N.ppf(.95) * 9.5
card("Normalverteilung: Quantile und „um mehr als 2σ“", 55,
 "Körpergröße \\(X\\sim N(175,\\,9.5^2)\\). (a) Mit welcher Wahrscheinlichkeit übersteigt die Größe den Erwartungswert um mehr als das Doppelte der Standardabweichung? (b) Welche Größe wird nur von 5 % überschritten? (c) In welchem symmetrischen Bereich um μ liegen 95 %? <span class='pt'>(5 P)</span>",
 ["(a) \\(P(X>\\mu+2\\sigma)=1-\\Phi(2)\\) – unabhängig von μ und σ.", "(b) gesucht \\(q_{0.95}=\\mu+\\sigma z_{0.95}\\).",
  "(c) \\(\\mu\\pm z_{0.975}\\,\\sigma\\)."],
 T("(a) \\(1-\\Phi(2)=1-0.9772=\\mathbf{«a»}\\)<br>(b) \\(q_{0.95}=175+1.6449\\cdot9.5=\\mathbf{«b»}\\) cm<br>(c) \\(175\\pm1.96\\cdot9.5=[\\mathbf{«c»};\\ \\mathbf{«d»}]\\)",
   a=r3(1 - N.cdf(2)), b=r3(q95), c=r3(175 - 1.959964 * 9.5), d=r3(175 + 1.959964 * 9.5)),
 "In R: <code>qnorm(0.95, 175, 9.5)</code> – R will σ = 9.5, nicht 90.25.")

# --- 3.10 Summen von Normalverteilungen
zS = (4990 - 5000) / math.sqrt(90)
card("Summen und lineare Transformation normalverteilter ZV", 40,
 "Das Gewicht einer Packung sei \\(N(500,9)\\). Ein Karton enthält 10 unabhängige Packungen. (a) Wie ist das Gesamtgewicht S verteilt? (b) Berechnen Sie \\(P(S<4990)\\). (c) Wie ist \\(Y=2X+10\\) verteilt? <span class='pt'>(5 P)</span>",
 ["Summe unabhängiger Normalverteilungen ist wieder normal: Erwartungswerte addieren, <b>Varianzen</b> addieren.",
  "\\(aX+b\\sim N(a\\mu+b,\\,a^2\\sigma^2)\\)."],
 T("(a) \\(S\\sim N(10\\cdot500,\\ 10\\cdot9)=N(5000,\\,90)\\)<br>(b) \\(P(S<4990)=\\Phi\\left(\\tfrac{4990-5000}{\\sqrt{90}}\\right)=\\Phi(«z»)=\\mathbf{«p»}\\)<br>(c) \\(Y\\sim N(1010,\\,36)\\)",
   z=r4(zS), p=r3(N.cdf(zS))),
 "Nicht verwechseln: 10 <i>verschiedene</i> Packungen \\(X_1+\\dots+X_{10}\\) (Varianz 10·9) vs. 10-mal <i>dieselbe</i> Packung \\(10X\\) (Varianz 100·9).")

# --- 3.11 ZGWS
card("Zentraler Grenzwertsatz: Verteilung des Mittelwerts", 55,
 "Die Bearbeitungszeit eines Auftrags hat (unbekannte Verteilung) \\(\\mu=12\\) und \\(\\sigma=4\\) Minuten. Es werden 64 Aufträge unabhängig bearbeitet. (a) Geben Sie die approximative Verteilung von \\(\\bar X\\) an. (b) Berechnen Sie \\(P(\\bar X>13)\\). (c) X sei \\(U(a,b)\\) mit \\(E(X)=4\\); wie groß ist approximativ \\(P(\\bar X<4)\\) für n = 100? <span class='pt'>(5 P)</span>",
 ["ZGWS: \\(\\bar X\\overset a\\sim N(\\mu,\\sigma^2/n)\\). Achtung: \\(\\sigma^2/n\\), nicht \\(\\sigma/n\\).",
  "Dann standardisieren wie gewohnt mit \\(sd(\\bar X)=\\sigma/\\sqrt n\\).",
  "(c) μ ist die Mitte der Normalverteilung → 0.5."],
 T("(a) \\(\\bar X\\overset a\\sim N\\left(12,\\tfrac{16}{64}\\right)=N(12;\\,0.25)\\)<br>(b) \\(P(\\bar X>13)=1-\\Phi\\left(\\tfrac{13-12}{0.5}\\right)=1-\\Phi(2)=\\mathbf{«a»}\\)<br>"
   "(c) \\(\\bar X\\overset a\\sim N(4,\\sigma^2/100)\\Rightarrow P(\\bar X<4)=\\mathbf{0.5}\\)", a=r3(1 - N.cdf(2))),
 "Testat 4, Aufgabe 7 war Teil (c). Begriff „approximativ“ bzw. Zeichen \\(\\overset a\\sim\\) hinschreiben.")

# --- 3.12 bivariate Normalverteilung
mx, my, sx, sy, rho = 170, 70, 10, 12, 0.6
mcond = my + rho * sy / sx * (180 - mx); vcond = sy ** 2 * (1 - rho ** 2); pc = 1 - N.cdf((80 - mcond) / math.sqrt(vcond))
card("Bivariate Normalverteilung: Rand und bedingte Verteilung", 25,
 "Größe X (cm) und Gewicht Y (kg) seien bivariat normalverteilt mit \\(\\mu_x=170\\), \\(\\mu_y=70\\), \\(\\sigma_x^2=100\\), \\(\\sigma_y^2=144\\), \\(\\rho=0.6\\). Geben Sie die Randverteilung von Y und die bedingte Verteilung von Y gegeben \\(X=180\\) an. Berechnen Sie \\(P(Y>80\\,|\\,X=180)\\). <span class='pt'>(6 P)</span>",
 ["Randverteilungen: einfach \\(N(\\mu_y,\\sigma_y^2)\\).",
  "Bedingt (V07): \\(E(Y|X=x)=\\mu_y+\\rho\\frac{\\sigma_y}{\\sigma_x}(x-\\mu_x)\\), \\(Var(Y|X=x)=\\sigma_y^2(1-\\rho^2)\\).",
  "Bedingte Varianz ist kleiner: Wissen über X verringert die Unsicherheit über Y."],
 T("\\(Y\\sim N(70,\\,144)\\)<br>\\(E(Y|X=180)=70+0.6\\cdot\\tfrac{12}{10}\\cdot10=«m»\\), \\(Var(Y|X=180)=144\\cdot0.64=«v»\\)<br>"
   "\\(Y|X=180\\sim N(«m»;\\,«v»)\\) · \\(P(Y>80|X=180)=1-\\Phi\\left(\\tfrac{80-77.2}{9.6}\\right)=\\mathbf{«p»}\\)",
   m=r2(mcond)[:-1], v=r2(vcond), p=r3(pc)),
 "Bei ρ = 0 sind X und Y unabhängig – bei der Normalverteilung (und nur da) gilt auch die Umkehrung.")

# --- 3.13 Ziehen ohne Zurücklegen: Lotto-Formel
from math import comb
ph = comb(4, 2) * comb(6, 1) / comb(10, 3)
card("Ziehen ohne Zurücklegen: Lotto-Formel", 20,
 "In einer Urne liegen 10 Kugeln, 4 davon rot. Es werden 3 Kugeln ohne Zurücklegen gezogen. Wie groß ist die Wahrscheinlichkeit für genau 2 rote? <span class='pt'>(2 P)</span>",
 ["Wie Lotto (V05): \\(P(X=x)=\\frac{\\binom{\\text{rot}}{x}\\binom{\\text{andere}}{n-x}}{\\binom{\\text{alle}}{n}}\\).",
  "Nicht Binomial – ohne Zurücklegen ändern sich die Wahrscheinlichkeiten."],
 T("\\(P(X=2)=\\frac{\\binom42\\binom61}{\\binom{10}3}=\\frac{6\\cdot6}{120}=\\mathbf{«p»}\\)", p=r3(ph)[:-2]))

# ======================================================================
sec("4 · Schätzer, Güteeigenschaften und Dichteschätzung (V09)", None,
    ["Ein <b>Schätzer</b> \\(\\hat\\vartheta\\) ist eine Funktion der Stichprobe \\(X_1,\\dots,X_n\\) und damit selbst eine Zufallsvariable.",
     "<b>Bias</b> \\(=E(\\hat\\vartheta)-\\vartheta\\). Bias = 0 ⇔ <b>erwartungstreu / unverzerrt</b>. Asymptotisch erwartungstreu: Bias → 0 für n → ∞.",
     "<b>Varianz</b> des Schätzers: Streuung bei wiederholten Stichproben. <b>MSE</b> \\(=E[(\\hat\\vartheta-\\vartheta)^2]=Bias^2+Var\\). <b>Konsistent</b>: MSE → 0 für n → ∞.",
     "<b>Werkzeuge:</b> \\(E\\left(\\sum a_iX_i\\right)=\\sum a_iE(X_i)\\) · bei iid: \\(Var\\left(\\sum a_iX_i\\right)=\\sum a_i^2Var(X_i)\\) · \\(E(\\bar X)=\\mu\\), \\(Var(\\bar X)=\\sigma^2/n\\) · \\(Var(X_i)=E(X_i^2)-E(X_i)^2\\).",
     "<b>ML-Schätzer</b> sind (unter Annahmen) asymptotisch erwartungstreu, konsistent und asymptotisch normalverteilt – aber nicht immer erwartungstreu.",
     "<b>Histogramm/KDE:</b> mehr Parameter (Klassen, kleine Bandweite) → Approximationsfehler ↓, Schätzfehler ↑. Mehr Daten n → Schätzfehler ↓."])

card("Erwartungstreue prüfen und Bias berechnen", 80,
 "\\(X_1,\\dots,X_n\\) seien iid normalverteilt mit Erwartungswert μ. Prüfen Sie, ob die Schätzer (a) \\(\\hat\\mu_1=\\frac2n\\sum_{i=1}^nX_i\\), (b) \\(\\hat\\mu_2=\\frac{X_1+X_n}{2}\\), (c) \\(\\hat\\mu_3=\\bar X\\) erwartungstreu sind, und geben Sie gegebenenfalls den Bias an. <span class='pt'>(6 P)</span>",
 ["Immer gleich: \\(E(\\hat\\mu)\\) ausrechnen, indem du E in die Summe ziehst und \\(E(X_i)=\\mu\\) einsetzt.",
  "Vergleiche mit μ. Bias = \\(E(\\hat\\mu)-\\mu\\).",
  "Konstanten (2/n) vor das E ziehen; \\(\\sum_{i=1}^n\\mu=n\\mu\\)."],
 "(a) \\(E(\\hat\\mu_1)=\\frac2n\\sum E(X_i)=\\frac2n\\cdot n\\mu=2\\mu\\neq\\mu\\) → verzerrt, \\(Bias=2\\mu-\\mu=\\mathbf{\\mu}\\)<br>"
 "(b) \\(E(\\hat\\mu_2)=\\frac{\\mu+\\mu}{2}=\\mu\\) → <b>erwartungstreu</b><br>(c) \\(E(\\bar X)=\\frac1n\\cdot n\\mu=\\mu\\) → <b>erwartungstreu</b>",
 "Antwortsatz nicht vergessen: „… ist (nicht) erwartungstreu, da \\(E(\\hat\\mu)=\\dots\\)“.")

kb = "Bias = −κ(n+1)/(4n)"
card("Schätzer mit Teilsummen (Testat-Typ) und Multiple Choice", 55,
 "Für X gilt \\(E(X)=\\frac\\kappa2\\). Ein Schätzer für κ sei \\(\\tilde\\kappa=X_1+\\frac1{2n}\\sum_{i=2}^nX_i\\). (a) Berechnen Sie \\(E(\\tilde\\kappa)\\) und den Bias. (b) Welche Aussagen stimmen? (1) \\(\\tilde\\kappa\\) ist erwartungstreu, weil alle Beobachtungen denselben Erwartungswert haben. (2) Der Bias hängt von n ab. (3) Der Bias ist ungleich null. (4) Ein erwartungstreuer Schätzer hat immer einen kleineren MSE als ein verzerrter. <span class='pt'>(5 P)</span>",
 ["Die Summe beginnt bei i = 2 → sie hat nur \\(n-1\\) Summanden!", "Bias = \\(E(\\tilde\\kappa)-\\kappa\\), auf einen Bruch bringen.",
  "MSE = Bias² + Var: Ein verzerrter Schätzer mit kleiner Varianz kann einen kleineren MSE haben."],
 "(a) \\(E(\\tilde\\kappa)=\\frac\\kappa2+\\frac1{2n}(n-1)\\frac\\kappa2=\\kappa\\,\\frac{2n+n-1}{4n}=\\kappa\\,\\frac{3n-1}{4n}\\)<br>"
 "\\(Bias=\\kappa\\frac{3n-1}{4n}-\\kappa=-\\kappa\\,\\frac{n+1}{4n}\\neq0\\)<br>(b) richtig: <b>(2) und (3)</b>; falsch: (1) und (4)",
 "Für n → ∞ geht der Bias gegen −κ/4, also nicht gegen 0: nicht einmal asymptotisch erwartungstreu.")

card("Varianz, MSE und Konsistenz von Schätzern", 50,
 "\\(X_1,\\dots,X_n\\) seien iid mit \\(E(X_i)=\\theta\\) und \\(Var(X_i)=\\theta^2\\). Vergleichen Sie \\(\\hat\\theta_1=\\bar X\\) und \\(\\hat\\theta_2=\\frac{X_1+X_2}{2}\\): Bias, Varianz, MSE und Konsistenz. <span class='pt'>(6 P)</span>",
 ["\\(Var\\left(\\frac1n\\sum X_i\\right)=\\frac1{n^2}\\sum Var(X_i)\\) – der Faktor wird quadriert, Unabhängigkeit nutzen.",
  "Bei Bias 0 ist MSE = Var.", "Konsistent, wenn MSE → 0 für n → ∞."],
 "Beide erwartungstreu: \\(E(\\hat\\theta_1)=E(\\hat\\theta_2)=\\theta\\)<br>"
 "\\(Var(\\hat\\theta_1)=\\frac1{n^2}\\cdot n\\theta^2=\\frac{\\theta^2}n=MSE(\\hat\\theta_1)\\to0\\) → <b>konsistent</b><br>"
 "\\(Var(\\hat\\theta_2)=\\frac14(\\theta^2+\\theta^2)=\\frac{\\theta^2}2=MSE(\\hat\\theta_2)\\), hängt nicht von n ab → <b>nicht konsistent</b><br>"
 "Für n > 2 ist \\(\\hat\\theta_1\\) besser (kleinerer MSE).")

card("Verzerrter Schätzer mit Varianzberechnung (Tutorium 9)", 45,
 "\\(X_1,\\dots,X_n\\) iid mit \\(E(X_i)=\\frac1\\gamma\\) und \\(E(X_i^2)=\\frac{2+\\gamma}{\\gamma}\\), γ > 1. Als Schätzer für γ wird \\(\\hat\\gamma=\\sum_{i=1}^n\\frac{X_i}n\\) benutzt. Zeigen Sie, dass \\(\\hat\\gamma\\) verzerrt ist, und bestimmen Sie \\(Var(\\hat\\gamma)\\). <span class='pt'>(6 P)</span>",
 ["\\(\\hat\\gamma\\) ist einfach \\(\\bar X\\).", "\\(Var(X_i)=E(X_i^2)-E(X_i)^2\\) zuerst ausrechnen.", "\\(Var(\\bar X)=\\frac{Var(X_i)}n\\)."],
 "\\(E(\\hat\\gamma)=\\frac1n\\sum\\frac1\\gamma=\\frac1\\gamma\\neq\\gamma\\) (da γ > 1) → verzerrt<br>"
 "\\(Var(X_i)=\\frac{2+\\gamma}\\gamma-\\frac1{\\gamma^2}=\\frac{\\gamma^2+2\\gamma-1}{\\gamma^2}\\)<br>"
 "\\(Var(\\hat\\gamma)=\\frac1n\\cdot\\frac{\\gamma^2+2\\gamma-1}{\\gamma^2}=\\mathbf{\\frac{\\gamma^2+2\\gamma-1}{n\\gamma^2}}\\)")

card("Produkte im Schätzer kürzen (Probeklausur 2022, Aufgabe 7)", 35,
 "Sei \\(E(X)=\\frac\\alpha4\\). Prüfen Sie, ob \\(\\hat\\alpha=\\frac{\\prod_{i=2}^{n-1}X_i}{\\prod_{i=1}^{n-1}X_i}+\\frac{X_n}{\\alpha}-\\frac14\\) ein unverzerrter Schätzer für α ist. <span class='pt'>(5 P)</span>",
 ["Erst <b>kürzen</b>: Zähler \\(X_2\\cdots X_{n-1}\\), Nenner \\(X_1\\cdot X_2\\cdots X_{n-1}\\) → übrig bleibt \\(\\frac1{X_1}\\).",
  "Dann E in die Summe ziehen: \\(E\\left(\\frac{X_n}\\alpha\\right)=\\frac1\\alpha\\cdot\\frac\\alpha4=\\frac14\\).",
  "Bedingung „unverzerrt“ hinschreiben: \\(E(\\hat\\alpha)\\overset!=\\alpha\\)."],
 "\\(\\hat\\alpha=\\frac1{X_1}+\\frac{X_n}\\alpha-\\frac14\\)<br>\\(E(\\hat\\alpha)=E\\left(\\frac1{X_1}\\right)+\\frac14-\\frac14=E\\left(\\frac1{X_1}\\right)\\)<br>"
 "Offizielle Lösung: \\(E\\left(\\frac1{X_1}\\right)=\\frac1{\\alpha/4}=\\frac4\\alpha\\neq\\alpha\\) → <b>verzerrter Schätzer</b>",
 "Mathematisch ist \\(E(1/X)\\) im Allgemeinen nicht \\(1/E(X)\\). Die Musterlösung rechnet trotzdem so. Das Ergebnis „verzerrt“ stimmt in beiden Fällen. Schreib den Weg wie in der Musterlösung.")

card("MSE-Vergleich mit Zahlen", 35,
 "Für θ = 10 hat Schätzer A Bias 0 und Varianz 4, Schätzer B Bias 1 und Varianz 2. Welcher Schätzer ist nach dem MSE besser? <span class='pt'>(2 P)</span>",
 ["\\(MSE=Bias^2+Var\\) für beide ausrechnen, kleiner ist besser."],
 "\\(MSE(A)=0+4=4\\), \\(MSE(B)=1^2+2=3\\) → <b>B</b> ist nach dem MSE besser, obwohl er verzerrt ist.")

card("Gütekriterien von ML-Schätzern und Fehlerarten", 45,
 "(a) Ergänzen Sie: Für iid-Daten sind ML-Schätzer (unter Zusatzannahmen) ____ (Bias → 0 für n → ∞), ____ (MSE → 0 für n → ∞) und ____. (b) Ein Histogramm mit 10 Klassen hat wie viele freie Parameter? (c) Was passiert mit Approximations- und Schätzfehler, wenn man mehr Klassen wählt bzw. n vergrößert? <span class='pt'>(6 P)</span>",
 ["Die drei Begriffe aus V09, Folie 16 auswendig lernen.", "J Klassen → J Höhen, aber die Fläche muss 1 sein → J − 1 frei.",
  "Approximationsfehler: Modell zu einfach. Schätzfehler: zu wenig Daten pro Parameter."],
 "(a) <b>asymptotisch erwartungstreu</b>, <b>konsistent</b>, <b>asymptotisch normalverteilt</b><br>(b) \\(10-1=\\mathbf{9}\\)<br>"
 "(c) Mehr Klassen: Approximationsfehler ↓, Schätzfehler ↑. Größeres n: Schätzfehler ↓, Approximationsfehler unverändert, Gesamtfehler ↓.")

# --- KDE per Hand
data = [2, 3, 3.5, 6, 7]; x0 = 3
rect = sum(1 for xi in data if x0 - 1 < xi <= x0 + 1) / (2 * 1 * len(data))
b = 1.5; us = [(x0 - xi) / b for xi in data]; ks = [.75 * (1 - u * u) if -1 <= u < 1 else 0 for u in us]; ep = sum(ks) / (len(data) * b)
log("KDE rect", rect); log("KDE epa", ep)
card("Kerndichteschätzer per Hand an einer Stelle", 40,
 "Daten: 2, 3, 3.5, 6, 7. Berechnen Sie den Kerndichteschätzer \\(\\hat f(x)=\\frac1{nb}\\sum K\\left(\\frac{x-x_i}b\\right)\\) an der Stelle x = 3 (a) mit Rechteckkern \\(K(u)=\\frac12\\) für \\(-1\\le u<1\\) und b = 1, (b) mit Epanechnikov-Kern \\(K(u)=\\frac34(1-u^2)\\) für \\(-1\\le u<1\\) und b = 1.5. (c) Welche Wirkung hat eine größere Bandweite? <span class='pt'>(7 P)</span>",
 ["Für jede Beobachtung \\(u_i=\\frac{x-x_i}b\\) berechnen.", "Nur wenn \\(-1\\le u_i<1\\): Kern einsetzen, sonst 0.",
  "Summe durch \\(n\\cdot b\\) teilen.", "Rechteckkern = fließendes Histogramm: zählt Punkte in \\((x-b,\\,x+b]\\)."],
 T("(a) \\(u_i=1,\\ 0,\\ -0.5,\\ -3,\\ -4\\) → nur 3 und 3.5 zählen (u = 1 nicht!): \\(\\hat f(3)=\\frac{0.5+0.5}{5\\cdot1}=\\mathbf{«r»}\\)<br>"
   "(b) \\(u_i=0.6667,\\ 0,\\ -0.3333,\\ -2,\\ -2.6667\\); \\(K=0.4167,\\ 0.75,\\ 0.6667,\\ 0,\\ 0\\)<br>\\(\\hat f(3)=\\frac{1.8333}{5\\cdot1.5}=\\mathbf{«e»}\\)<br>"
   "(c) Größere Bandweite → glattere Schätzung; zu groß verwischt Details, zu klein ist zackig.", r=r3(rect)[:-2], e=r3(ep)),
 "Randfall genau ablesen: Rechteckkern gilt für \\(-1\\le u<1\\), also zählt u = 1 nicht mit.", fig=("sk_kde.svg", 90))

# ======================================================================
sec("5 · Maximum-Likelihood-Schätzung per Hand (V08)", None,
    ["<b>Idee:</b> Wähle den Parameter, unter dem die beobachteten Daten am wahrscheinlichsten sind.",
     "<b>Rezept:</b> ① Likelihood \\(L(\\vartheta)=\\prod_{i=1}^nP(X_i=x_i)\\) bzw. \\(\\prod f(x_i)\\) ② logarithmieren: \\(\\ell(\\vartheta)=\\sum\\log(\\dots)\\) ③ nach ϑ ableiten ④ = 0 setzen ⑤ nach \\(\\hat\\vartheta\\) auflösen ⑥ (falls verlangt) 2. Ableitung < 0 prüfen.",
     "<b>Log-Regeln:</b> \\(\\log(ab)=\\log a+\\log b\\) · \\(\\log(a^b)=b\\log a\\) · \\(\\log(e^x)=x\\) · \\(\\log\\frac1a=-\\log a\\) · \\(\\log\\prod=\\sum\\log\\).",
     "<b>Produkt-Regeln:</b> \\(\\prod_{i=1}^n c=c^n\\) · \\(\\prod a^{x_i}=a^{\\sum x_i}\\) · \\(\\prod e^{-\\lambda x_i}=e^{-\\lambda\\sum x_i}\\).",
     "<b>Ableitungen:</b> \\((\\log\\vartheta)'=\\frac1\\vartheta\\) · \\((\\log(1-\\vartheta))'=\\frac{-1}{1-\\vartheta}\\) · \\((\\log(\\vartheta+1))'=\\frac1{\\vartheta+1}\\) · Terme ohne ϑ fallen weg.",
     "<b>Standard-Ergebnisse:</b> Poisson \\(\\hat\\lambda=\\bar x\\) · Bernoulli \\(\\hat\\pi=\\bar x\\) · Exponential \\(\\hat\\lambda=1/\\bar x\\) · Normal \\(\\hat\\mu=\\bar x\\) · geometrisch \\(\\hat p=\\frac1{1+\\bar x}\\)."])

card("Likelihood für eine konkrete Stichprobe (geometrische Verteilung)", 60,
 "\\(P(X=x)=(1-p)^xp\\) für x = 0, 1, 2, … Beobachtet: 3, 0, 5, 2. (a) Stellen Sie die Likelihood auf und vereinfachen Sie. (b) Berechnen Sie den ML-Schätzer \\(\\hat p\\). <span class='pt'>(6 P)</span>",
 ["Für jede Beobachtung die Wahrscheinlichkeit hinschreiben und alle multiplizieren.", "Potenzen zusammenfassen: p kommt 4-mal vor, \\((1-p)\\) mit Exponent \\(3+0+5+2=10\\).",
  "\\(\\ell(p)=4\\log p+10\\log(1-p)\\), ableiten, null setzen."],
 T("(a) \\(L(p)=(1-p)^3p\\cdot p\\cdot(1-p)^5p\\cdot(1-p)^2p=p^4(1-p)^{10}\\)<br>"
   "(b) \\(\\ell(p)=4\\log p+10\\log(1-p)\\), \\(\\ell'(p)=\\frac4p-\\frac{10}{1-p}\\overset!=0\\)<br>"
   "\\(4(1-\\hat p)=10\\hat p\\Rightarrow\\hat p=\\frac4{14}=\\frac27=\\mathbf{«p»}\\)", p=r3(2 / 7)),
 "Kontrolle mit der allgemeinen Formel: \\(\\hat p=\\frac1{1+\\bar x}=\\frac1{1+2.5}=0.286\\) ✓")

card("ML allgemein: Poissonverteilung mit 2. Ableitung", 75,
 "\\(X_1,\\dots,X_n\\overset{iid}\\sim Po(\\lambda)\\). Leiten Sie den ML-Schätzer allgemein her, prüfen Sie die Bedingung 2. Ordnung und berechnen Sie den Schätzwert für die Stichprobe 4, 1, 3, 0, 2, 2. <span class='pt'>(8 P)</span>",
 ["\\(L(\\lambda)=\\prod\\frac{\\lambda^{x_i}}{x_i!}e^{-\\lambda}=\\lambda^{\\sum x_i}e^{-n\\lambda}\\prod\\frac1{x_i!}\\).",
  "Log: \\(\\ell=\\sum x_i\\log\\lambda-n\\lambda-\\sum\\log(x_i!)\\). Der letzte Term hängt nicht von λ ab.",
  "2. Ableitung: \\(-\\frac{\\sum x_i}{\\lambda^2}<0\\) → Maximum."],
 "\\(\\ell(\\lambda)=\\log\\lambda\\sum x_i-n\\lambda-\\sum\\log(x_i!)\\)<br>\\(\\ell'(\\lambda)=\\frac{\\sum x_i}\\lambda-n\\overset!=0\\Rightarrow\\hat\\lambda=\\frac1n\\sum x_i=\\bar x\\)<br>"
 "\\(\\ell''(\\lambda)=-\\frac{\\sum x_i}{\\lambda^2}<0\\) → Maximum<br>Stichprobe: \\(\\hat\\lambda=\\frac{12}6=\\mathbf{2}\\)")

card("ML: Exponentialverteilung (auch Weibull mit r = 1)", 80,
 "\\(f(x)=\\lambda e^{-\\lambda x}\\) für x ≥ 0. (a) Stellen Sie die Log-Likelihood für eine iid-Stichprobe \\(x_1,\\dots,x_n\\) auf. (b) Bestimmen Sie \\(\\hat\\lambda\\). (c) Prüfen Sie die Bedingung 2. Ordnung. (d) Schätzwert für 2, 5, 1, 4? <span class='pt'>(8 P)</span>",
 ["\\(L=\\prod\\lambda e^{-\\lambda x_i}=\\lambda^ne^{-\\lambda\\sum x_i}\\).", "\\(\\ell=n\\log\\lambda-\\lambda\\sum x_i\\)."],
 "(a) \\(\\ell(\\lambda)=n\\log\\lambda-\\lambda\\sum_{i=1}^nx_i\\)<br>(b) \\(\\ell'=\\frac n\\lambda-\\sum x_i\\overset!=0\\Rightarrow\\hat\\lambda=\\frac n{\\sum x_i}=\\frac1{\\bar x}\\)<br>"
 "(c) \\(\\ell''=-\\frac n{\\lambda^2}<0\\) → Maximum · (d) \\(\\bar x=3\\Rightarrow\\hat\\lambda=\\frac13=\\mathbf{0.333}\\)",
 "Probeklausur 2022, Aufgabe 6: Weibull \\(f=r\\lambda(\\lambda x)^{r-1}e^{-(\\lambda x)^r}\\) mit r = 1 ist genau \\(\\lambda e^{-\\lambda x}\\). Erst r = 1 einsetzen, dann wie hier.")

card("ML: Bernoulli / Anteilswert", 50,
 "Bei 20 Münzwürfen fiel 6-mal Wappen. \\(X_i\\sim Be(\\pi)\\). Leiten Sie den ML-Schätzer für π her und berechnen Sie ihn. <span class='pt'>(5 P)</span>",
 ["\\(P(X_i=x_i)=\\pi^{x_i}(1-\\pi)^{1-x_i}\\).", "\\(L=\\pi^k(1-\\pi)^{n-k}\\) mit k = Anzahl Erfolge."],
 "\\(\\ell(\\pi)=k\\log\\pi+(n-k)\\log(1-\\pi)\\), \\(\\ell'=\\frac k\\pi-\\frac{n-k}{1-\\pi}\\overset!=0\\)<br>"
 "\\(k(1-\\hat\\pi)=(n-k)\\hat\\pi\\Rightarrow\\hat\\pi=\\frac kn=\\frac6{20}=\\mathbf{0.3}\\)",
 "Wie die Tabelle in V08: Unter π = 0.3 ist die beobachtete Stichprobe am wahrscheinlichsten.")

card("ML: allgemeine geometrische Verteilung (Testat 5)", 55,
 "\\(P(X=x)=\\theta(1-\\theta)^x\\), x = 0, 1, 2, … Bestimmen Sie die Log-Likelihood und den ML-Schätzer \\(\\hat\\theta\\) für eine iid-Stichprobe. Vereinfachen Sie so weit wie möglich. <span class='pt'>(6 P)</span>",
 ["\\(L=\\theta^n(1-\\theta)^{\\sum x_i}\\).", "Nach dem Nullsetzen über Kreuz multiplizieren und θ ausklammern.", "Am Ende durch n kürzen → Form mit \\(\\bar x\\)."],
 "\\(\\ell(\\theta)=n\\log\\theta+\\sum x_i\\log(1-\\theta)\\)<br>\\(\\ell'=\\frac n\\theta-\\frac{\\sum x_i}{1-\\theta}\\overset!=0\\Rightarrow n(1-\\hat\\theta)=\\hat\\theta\\sum x_i\\)<br>"
 "\\(\\hat\\theta=\\frac n{n+\\sum x_i}=\\mathbf{\\frac1{1+\\bar x}}\\)")

xs = [0.5, 0.8, 0.9, 0.6]; sl = sum(math.log(v) for v in xs); th = -len(xs) / sl; bb = th - 1
log("theta", th)
card("ML: Dichte mit Parameter im Exponenten (Übungsklausur ML, Aufgabe 1)", 60,
 "Die Dichte sei \\(f(x)=(b+1)\\,x^b\\) für \\(0<x\\le1\\), b ≥ 0. (a) Geben Sie die vereinfachte Log-Likelihood an. (b) Geben Sie die Bedingung an, aus der \\(\\hat b\\) folgt. (c) Geben Sie \\(\\hat b\\) an und berechnen Sie ihn für 0.5, 0.8, 0.9, 0.6. <span class='pt'>(12 P)</span>",
 ["\\(L=\\prod(b+1)x_i^b=(b+1)^n\\prod x_i^b\\).", "\\(\\log x_i^b=b\\log x_i\\) → \\(\\ell=n\\log(b+1)+b\\sum\\log x_i\\).",
  "Ableiten nach b: \\(\\frac n{b+1}+\\sum\\log x_i\\).", "Da \\(x_i\\le1\\), ist \\(\\sum\\log x_i<0\\) → \\(\\hat b\\) kann positiv werden."],
 T("(a) \\(\\ell(b)=n\\log(b+1)+b\\sum_{i=1}^n\\log x_i\\)<br>(b) \\(\\frac n{\\hat b+1}+\\sum\\log x_i=0\\)<br>"
   "(c) \\(\\hat b=-1-\\frac n{\\sum\\log x_i}\\); hier \\(\\sum\\log x_i=«s»\\) → \\(\\hat b=-1+\\frac4{«sa»}=\\mathbf{«b»}\\)",
   s=r4(sl), sa=r4(-sl), b=r3(bb)),
 "Die Punkte gibt es vor allem für (a) und (b). Auch wenn das Umformen hakt: Log-Likelihood und Bedingung sauber aufschreiben!")

card("ML: Normal- und Log-Normalverteilung, μ (σ bekannt)", 55,
 "Gegeben sei die Dichte \\(f(x)=\\frac1{\\sqrt{2\\pi}\\,\\sigma x}\\exp\\left(-\\frac{(\\log x-\\mu)^2}{2\\sigma^2}\\right)\\) für x > 0, σ bekannt. (a) Log-Likelihood möglichst weit vereinfacht. (b) ML-Schätzer für μ. (c) Wert für die Stichprobe \\(1,\\ e,\\ e^2\\). <span class='pt'>(12 P)</span>",
 ["Konstanten herausziehen: \\(L=\\left(\\frac1{\\sqrt{2\\pi}\\sigma}\\right)^n\\prod\\frac1{x_i}\\cdot\\exp\\left(-\\frac1{2\\sigma^2}\\sum(\\log x_i-\\mu)^2\\right)\\).",
  "Beim Ableiten nach μ fallen alle Terme ohne μ weg. Kettenregel: \\(\\frac{d}{d\\mu}(\\log x_i-\\mu)^2=-2(\\log x_i-\\mu)\\)."],
 "(a) \\(\\ell(\\mu)=-n\\log(\\sqrt{2\\pi}\\sigma)-\\sum\\log x_i-\\frac1{2\\sigma^2}\\sum(\\log x_i-\\mu)^2\\)<br>"
 "(b) \\(\\ell'(\\mu)=\\frac1{\\sigma^2}\\sum(\\log x_i-\\mu)\\overset!=0\\Rightarrow\\hat\\mu=\\frac1n\\sum_{i=1}^n\\log x_i\\)<br>(c) \\(\\hat\\mu=\\frac{0+1+2}3=\\mathbf{1}\\)",
 "Für die Normalverteilung (ohne \\(\\log\\) und ohne \\(\\frac1x\\)) kommt genauso \\(\\hat\\mu=\\bar x\\) heraus (V08).")

card("ML: Parameter mit log(2) (Übungsklausur ML, Aufgabe 3)", 50,
 "\\(f(x)=\\frac{\\beta\\log2}{2^{x\\beta}}\\) für x ≥ 0, β > 0. (a) Likelihood. (b) Log-Likelihood. (c) ML-Schätzer \\(\\hat\\beta\\) mit vollständigem Lösungsweg. <span class='pt'>(10 P)</span>",
 ["\\(\\frac1{2^{x\\beta}}=2^{-x\\beta}\\), also \\(\\log(2^{-x_i\\beta})=-x_i\\beta\\log2\\).", "\\(\\log(\\log2)\\) ist nur eine Konstante – beim Ableiten fällt sie weg."],
 "(a) \\(L(\\beta)=(\\log2)^n\\beta^n\\,2^{-\\beta\\sum x_i}\\)<br>(b) \\(\\ell(\\beta)=n\\log(\\log2)+n\\log\\beta-\\beta\\log2\\sum x_i\\)<br>"
 "(c) \\(\\ell'=\\frac n\\beta-\\log2\\sum x_i\\overset!=0\\Rightarrow\\hat\\beta=\\frac n{\\log2\\sum x_i}=\\mathbf{\\frac1{\\log(2)\\,\\bar x}}\\)")

a = (-5 + 11) / 12
assert abs(6 * a * a + 5 * a - 4) < 1e-12
card("ML aus einer Wahrscheinlichkeitstabelle (quadratische Gleichung)", 40,
 "X hat den Träger {1, 2, 3} mit \\(P(X=1)=\\alpha\\), \\(P(X=2)=\\alpha^2\\), \\(P(X=3)=1-\\alpha-\\alpha^2\\), \\(0<\\alpha\\le0.618\\). Stichprobe: 1, 3, 2, 1. Bestimmen Sie L(α) und \\(\\hat\\alpha\\). <span class='pt'>(6 P)</span>",
 ["Für jede Beobachtung die passende Zelle nehmen und multiplizieren.", "\\(\\ell=4\\log\\alpha+\\log(1-\\alpha-\\alpha^2)\\). Innere Ableitung: \\(-1-2\\alpha\\).",
  "Es entsteht \\(6\\alpha^2+5\\alpha-4=0\\) → pq- oder abc-Formel; nur die Lösung im erlaubten Bereich nehmen."],
 "\\(L(\\alpha)=\\alpha\\cdot(1-\\alpha-\\alpha^2)\\cdot\\alpha^2\\cdot\\alpha=\\alpha^4(1-\\alpha-\\alpha^2)\\)<br>"
 "\\(\\ell'=\\frac4\\alpha-\\frac{1+2\\alpha}{1-\\alpha-\\alpha^2}\\overset!=0\\Rightarrow4-4\\alpha-4\\alpha^2=\\alpha+2\\alpha^2\\Rightarrow6\\alpha^2+5\\alpha-4=0\\)<br>"
 "\\(\\alpha=\\frac{-5\\pm\\sqrt{25+96}}{12}=\\frac{-5\\pm11}{12}\\) → \\(\\hat\\alpha=\\mathbf{0.5}\\) (die Lösung −4/3 ist nicht erlaubt)", "Aus Testat 5.")

s2 = sum(v * v for v in [0.02, -0.01, 0.03, -0.02]) / 4
card("ML für die Varianz der Normalverteilung (μ bekannt)", 25,
 "Log-Renditen seien \\(N(0,\\sigma^2)\\). Beobachtet: 0.02, −0.01, 0.03, −0.02. Bestimmen Sie den ML-Schätzer für σ² allgemein und als Zahl. <span class='pt'>(5 P)</span>",
 ["Nach σ² (nicht σ) ableiten: Setze \\(v=\\sigma^2\\). \\(\\ell(v)=-\\frac n2\\log(2\\pi v)-\\frac1{2v}\\sum x_i^2\\).",
  "\\(\\frac{d}{dv}\\left(-\\frac1{2v}\\right)=\\frac1{2v^2}\\)."],
 T("\\(\\ell'(v)=-\\frac n{2v}+\\frac{\\sum x_i^2}{2v^2}\\overset!=0\\Rightarrow\\hat\\sigma^2=\\frac1n\\sum_{i=1}^n x_i^2\\) (mit μ = 0)<br>"
   "\\(\\hat\\sigma^2=\\frac{0.0004+0.0001+0.0009+0.0004}{4}=\\mathbf{«s»}\\)", s=r4(s2)[:-1] if False else "0.00045"),
 "Tutorium 8 macht das numerisch in R mit optimize(). In R gibt man dabei σ an (dnorm), am Ende quadrieren!")

card("Reihenfolge der ML-Schritte (Testat 5)", 40,
 "Bringen Sie in die richtige Reihenfolge: (A) Ggf. prüfen, ob ein Maximum vorliegt. (B) Likelihood aufstellen. (C) Ableiten und null setzen. (D) Verteilungsmodell wählen. (E) Nach dem Parameter auflösen. (F) Log-Likelihood durch Logarithmieren. <span class='pt'>(3 P)</span>",
 ["Logisch denken: Ohne Modell keine Likelihood; ohne Ableitung nichts zum Auflösen."],
 "\\(\\mathbf{D\\to B\\to F\\to C\\to E\\to A}\\)")
