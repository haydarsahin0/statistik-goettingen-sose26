"""Abschnitte 6–10: Konfidenzintervalle, Testprinzipien, spezielle Tests, Regression, Klausurstrategie."""
import math, subprocess, html
from scipy import stats
from skcommon import sec, card, T, r3, r4, r2, log

N = stats.norm

# ======================================================================
sec("6 · Konfidenzintervalle (V10)", None,
    ["<b>Idee:</b> Ein Intervall [L, U] aus den Daten, das den wahren Parameter mit Wahrscheinlichkeit 1 − α überdeckt. Die <b>Grenzen</b> sind zufällig, der Parameter ist fest.",
     "<table class='tab' style='font-size:.86rem;margin:.1em 0'><tr><th>Situation</th><th>Konfidenzintervall zum Niveau 1 − α</th><th>Quantil</th></tr>"
     "<tr><td>μ, Normalverteilung, σ bekannt (oder n groß, ZGWS)</td><td>\\(\\bar x\\pm z_{1-\\alpha/2}\\,\\frac{\\sigma}{\\sqrt n}\\)</td><td><code>qnorm(1-α/2)</code></td></tr>"
     "<tr><td>μ, Normalverteilung, σ unbekannt</td><td>\\(\\bar x\\pm t_{n-1;\\,1-\\alpha/2}\\,\\frac{s_*}{\\sqrt n}\\)</td><td><code>qt(1-α/2, n-1)</code></td></tr>"
     "<tr><td>Anteilswert π</td><td>\\(\\hat\\pi\\pm z_{1-\\alpha/2}\\sqrt{\\frac{\\hat\\pi(1-\\hat\\pi)}n}\\)</td><td><code>qnorm(1-α/2)</code></td></tr>"
     "<tr><td>Varianz σ², Normalverteilung</td><td>\\(\\left[\\frac{(n-1)s_*^2}{\\chi^2_{n-1;\\,1-\\alpha/2}};\\ \\frac{(n-1)s_*^2}{\\chi^2_{n-1;\\,\\alpha/2}}\\right]\\)</td><td><code>qchisq(…, n-1)</code></td></tr></table>",
     "\\(s_*^2=\\frac1{n-1}\\sum(x_i-\\bar x)^2\\) (unverzerrt) = <code>var()</code> in R. Es gilt \\((n-1)s_*^2=n\\,s^2\\).",
     "Breiter wird das KI bei: größerem σ, höherem Niveau 1 − α, kleinerem n. Doppelte Genauigkeit braucht vierfaches n."])

h = N.ppf(.975) * 4 / 4; h90 = N.ppf(.95) * 4 / 4
card("KI für μ bei bekannter Varianz", 80,
 "Die Füllmenge sei normalverteilt mit σ = 4 ml. Eine Stichprobe von n = 16 Flaschen ergab \\(\\bar x=52.3\\). Bestimmen Sie ein 95 %- und ein 90 %-Konfidenzintervall für μ. <span class='pt'>(4 P)</span>",
 ["σ bekannt → z-Quantil. 95 % → \\(1-\\alpha/2=0.975\\) → \\(z=1.96\\). 90 % → 0.95 → 1.645.",
  "Halbe Breite: \\(z\\cdot\\sigma/\\sqrt n\\) = 1.96 · 4 / 4.", "Intervall als [L; U] mit 3 Nachkommastellen."],
 T("95 %: \\(52.3\\pm1.96\\cdot\\frac4{\\sqrt{16}}=52.3\\pm1.96=[\\mathbf{«a»};\\ \\mathbf{«b»}]\\)<br>90 %: \\(52.3\\pm1.645\\cdot1=[\\mathbf{«c»};\\ \\mathbf{«d»}]\\)",
   a=r3(52.3 - h), b=r3(52.3 + h), c=r3(52.3 - h90), d=r3(52.3 + h90)),
 "Höheres Niveau → breiteres Intervall. Für ein 99 %-KI: z = 2.576.")

t14 = 2.145; ht = t14 * 7 / math.sqrt(15)
card("KI für μ bei unbekannter Varianz (t-Quantil aus R-Output)", 85,
 "Wachheitsdauer normalverteilt; n = 15, \\(\\bar x=180.5\\), \\(s_*^2=49\\). R-Output: <code>round(qt(c(0.9,0.925,0.95,0.975),15),3)</code> → 1.341 1.517 1.753 2.131; <code>round(qt(c(0.9,0.925,0.95,0.975),14),3)</code> → 1.345 1.523 1.761 2.145. Berechnen Sie das 95 %-KI für μ. <span class='pt'>(4 P)</span>",
 ["σ unbekannt → t-Verteilung mit <b>n − 1 = 14</b> Freiheitsgraden (Falle: Zeile mit 15 ist falsch!).",
  "95 % → Quantil 0.975 → 2.145.", "\\(s_*=\\sqrt{49}=7\\)."],
 T("\\(180.5\\pm t_{14;\\,0.975}\\frac{s_*}{\\sqrt n}=180.5\\pm2.145\\cdot\\frac7{\\sqrt{15}}=180.5\\pm«h»\\)<br>KI = \\([\\mathbf{«a»};\\ \\mathbf{«b»}]\\)",
   h=r4(ht), a=r3(180.5 - ht), b=r3(180.5 + ht)),
 "Testat 6, Aufgabe 4 – die Falle mit df = 15 vs. 14 und 0.95 vs. 0.975 ist Absicht.")

p = 0.8; hp = N.ppf(.975) * math.sqrt(p * (1 - p) / 100)
card("KI für einen Anteilswert", 75,
 "Von 100 geprüften Bohnen waren 80 perfekt. (a) Berechnen Sie ein 95 %-KI für den Anteil perfekter Bohnen (4 Nachkommastellen). (b) Vervollständigen Sie den R-Befehl für die obere Grenze: <code>__ + qnorm(__) * sqrt(__)</code>. <span class='pt'>(4 P)</span>",
 ["\\(\\hat\\pi=80/100=0.8\\).", "\\(\\sqrt{\\hat\\pi(1-\\hat\\pi)/n}=\\sqrt{0.8\\cdot0.2/100}=0.04\\)."],
 T("(a) \\(0.8\\pm1.96\\cdot0.04=[\\mathbf{«a»};\\ \\mathbf{«b»}]\\)<br>(b) <code>0.8 + qnorm(0.975) * sqrt(0.8*0.2/100)</code>",
   a=r4(p - hp), b=r4(p + hp)),
 "Hier verlangte die Aufgabe ausdrücklich 4 Nachkommastellen – Aufgabenanweisung schlägt die Standardregel.")

s2v = 0.9624938; L = 29 * s2v / 45.72; U = 29 * s2v / 16.05
card("KI für die Varianz (χ²-Quantile aus R-Output)", 60,
 "n = 30 normalverteilte Messungen. R-Output: <code>var(x)</code> → 0.9624938, <code>var(x)*29</code> → 27.91232, <code>var(x)*30</code> → 28.87481, <code>round(qchisq(c(0.025,0.05,0.95,0.975),29),2)</code> → 16.05 17.71 42.56 45.72, dasselbe mit 30 → 16.79 18.49 43.77 46.98. Bestimmen Sie das 95 %-KI für σ². <span class='pt'>(4 P)</span>",
 ["Formel: \\(\\left[\\frac{(n-1)s_*^2}{\\chi^2_{n-1;\\,0.975}};\\ \\frac{(n-1)s_*^2}{\\chi^2_{n-1;\\,0.025}}\\right]\\) – das <b>große</b> Quantil steht unter der <b>unteren</b> Grenze.",
  "<code>var()</code> ist schon \\(s_*^2\\), also Zähler = var · 29 = 27.91232. Freiheitsgrade 29."],
 T("\\(\\left[\\frac{27.91232}{45.72};\\ \\frac{27.91232}{16.05}\\right]=[\\mathbf{«a»};\\ \\mathbf{«b»}]\\)", a=r3(L), b=r3(U)),
 "Das KI für σ² ist nicht symmetrisch um \\(s_*^2\\). Wer var·30 oder df = 30 nimmt, verliert die Punkte.")

card("Rückwärts: Was steckt in diesem R-Befehl?", 40,
 "Eine Mitarbeiterin hat nur noch die Eingabe <code>c(3 - 2*qnorm(0.995)/sqrt(100), 3 + 2*qnorm(0.995)/sqrt(100))</code>. Wie lauten Stichprobenmittel, Konfidenzniveau, Standardabweichung und Stichprobenumfang? <span class='pt'>(4 P)</span>",
 ["Mit der Formel \\(\\bar x\\pm z_{1-\\alpha/2}\\frac\\sigma{\\sqrt n}\\) Stück für Stück vergleichen.", "qnorm(0.995) → \\(1-\\alpha/2=0.995\\Rightarrow\\alpha=0.01\\)."],
 "\\(\\bar x=\\mathbf3\\) · \\(1-\\alpha/2=0.995\\Rightarrow\\alpha=0.01\\), Niveau <b>99 %</b> · \\(\\sigma=\\mathbf2\\) · \\(\\sqrt n=10\\Rightarrow n=\\mathbf{100}\\)")

card("Konfidenzintervalle richtig interpretieren", 70,
 "Ein 95 %-KI für μ lautet [176.6; 184.4]. Welche Aussagen sind richtig? (1) μ liegt mit Wahrscheinlichkeit 95 % in [176.6; 184.4]. (2) Bei vielen Wiederholungen überdecken etwa 95 % der so konstruierten Intervalle μ. (3) Mit größerem n wird das KI tendenziell schmaler. (4) Ein 99 %-KI aus denselben Daten ist schmaler. (5) Da 180 im KI liegt, wird \\(H_0:\\mu=180\\) zweiseitig zum Niveau 5 % verworfen. <span class='pt'>(5 P)</span>",
 ["μ ist fest, nur das Intervall ist zufällig. Wahrscheinlichkeitsaussagen beziehen sich auf das Verfahren.",
  "Dualität (V11): KI zum Niveau 1 − α ↔ zweiseitiger Test zum Niveau α."],
 "Richtig: <b>(2), (3)</b>. Falsch: (1) (nach der Berechnung ist μ fest – drin oder nicht), (4) (99 % ist breiter), (5) (180 liegt <i>im</i> KI → H₀ wird <i>nicht</i> verworfen; verworfen wird nur, wenn der Wert außerhalb des KI liegt).",
 "Fehlerbalken-Bild (Testat 6): Bei 100 Stichproben verfehlen etwa 5 Intervalle das wahre μ, alle sind unterschiedlich lang (σ unbekannt) und liegen um μ verstreut.",
 fig=("sk_ki.svg", 62))

# ======================================================================
sec("7 · Prinzipien statistischer Tests (V11)", None,
    ["<b>H₁</b> = was du <b>statistisch absichern</b> (beweisen) willst. <b>H₀</b> = das Gegenteil, enthält immer das Gleichheitszeichen (=, ≤, ≥).",
     "<b>Fehler 1. Art (α-Fehler):</b> H₀ verwerfen, obwohl H₀ wahr ist. Wird durch das Signifikanzniveau α begrenzt. <b>Fehler 2. Art (β-Fehler):</b> H₀ nicht verwerfen, obwohl H₁ wahr ist – nicht kontrolliert.",
     "<b>Ablauf:</b> Hypothesen → Teststatistik und ihre Verteilung unter H₀ → Ablehnungsbereich A (zu α) → Entscheidung: Teststatistik ∈ A ⇒ H₀ verwerfen.",
     "<table class='tab' style='font-size:.86rem;margin:.1em 0'><tr><th>Verteilung unter H₀</th><th>linksseitig (H₁: <)</th><th>rechtsseitig (H₁: >)</th><th>zweiseitig (H₁: ≠)</th></tr>"
     "<tr><td>N(0, 1)</td><td>\\((-\\infty;-z_{1-\\alpha}]\\)</td><td>\\([z_{1-\\alpha};\\infty)\\)</td><td>\\(|z|\\ge z_{1-\\alpha/2}\\)</td></tr>"
     "<tr><td>t(df)</td><td>\\((-\\infty;-t_{df;1-\\alpha}]\\)</td><td>\\([t_{df;1-\\alpha};\\infty)\\)</td><td>\\(|t|\\ge t_{df;1-\\alpha/2}\\)</td></tr>"
     "<tr><td>χ²(df)</td><td>\\([0;\\chi^2_{df;\\alpha}]\\)</td><td>\\([\\chi^2_{df;1-\\alpha};\\infty)\\)</td><td>\\([0;\\chi^2_{df;\\alpha/2}]\\cup[\\chi^2_{df;1-\\alpha/2};\\infty)\\)</td></tr>"
     "<tr><td><b>p-Wert</b></td><td>\\(P(T\\le t)\\)</td><td>\\(1-P(T\\le t)\\)</td><td>\\(2\\cdot\\min(\\text{links},\\text{rechts})\\)</td></tr></table>",
     "<b>p-Wert</b> = Wahrscheinlichkeit, unter H₀ einen noch extremeren Wert der Teststatistik zu erhalten; = kleinstes α, zu dem H₀ verworfen wird. <b>p ≤ α ⇒ H₀ verwerfen.</b>",
     "<b>Formulierung:</b> „H₀ wird verworfen; H₁ ist zum Niveau α statistisch abgesichert.“ bzw. „H₀ kann nicht verworfen werden.“ Nie „H₀ ist bewiesen“."])

card("Hypothesenpaar aus dem Text aufstellen", 95,
 "Stellen Sie jeweils H₀ und H₁ auf: (a) Es soll abgesichert werden, dass ein Skispringer <i>nicht weiter</i> als 133.5 m springt. (b) Es soll gezeigt werden, dass der Schatten <i>langsamer</i> als 180 ms zieht. (c) Unterscheidet sich die Letalitätsrate <i>signifikant</i> von 4 %? (d) Ist die Schwankung (Varianz) durch die Kampagne <i>kleiner</i> geworden als 71 479.11? (e) Kaffee steigert die Punktzahl über 20. <span class='pt'>(5 P)</span>",
 ["Satzteil, der <b>abgesichert / gezeigt / nachgewiesen</b> werden soll → H₁ (ohne Gleichheitszeichen).",
  "H₀ = Gegenteil mit =, ≤ oder ≥.", "„unterscheidet sich“, „weicht ab“ → zweiseitig (≠).",
  "Parameter richtig wählen: μ (Mittelwert), π (Anteil), σ² (Varianz)."],
 "(a) \\(H_0:\\mu\\ge133.5\\) vs. \\(H_1:\\mu<133.5\\)<br>(b) \\(H_0:\\mu\\le180\\) vs. \\(H_1:\\mu>180\\) (langsamer = mehr ms)<br>"
 "(c) \\(H_0:\\pi=0.04\\) vs. \\(H_1:\\pi\\neq0.04\\)<br>(d) \\(H_0:\\sigma^2\\ge71479.11\\) vs. \\(H_1:\\sigma^2<71479.11\\)<br>(e) \\(H_0:\\mu\\le20\\) vs. \\(H_1:\\mu>20\\)",
 "Probeklausur 2022 (2 P), Tutorium 11 und 12, Testat 6 – kommt praktisch immer. Bei „langsamer“, „teurer“ usw. erst überlegen, ob die Zahl größer oder kleiner wird.")

card("Fehler 1. und 2. Art im Sachkontext", 60,
 "Ein Rauchmelder testet \\(H_0\\): „Es brennt nicht“ gegen \\(H_1\\): „Es brennt“. Beschreiben Sie den Fehler 1. und 2. Art in Worten. Welcher Fehler wird durch α kontrolliert? Was passiert, wenn man α verkleinert? <span class='pt'>(4 P)</span>",
 ["Fehler 1. Art: H₀ <b>fälschlich verworfen</b>. Fehler 2. Art: H₀ <b>fälschlich beibehalten</b>.",
  "Kleineres α → kleinerer Ablehnungsbereich → seltener Fehler 1. Art, aber öfter Fehler 2. Art (\\(\\alpha_{max}+\\beta_{max}=1\\) beim Binomialtest-Beispiel)."],
 "Fehler 1. Art: Alarm, obwohl es nicht brennt (Fehlalarm). Fehler 2. Art: Kein Alarm, obwohl es brennt.<br>"
 "α begrenzt die Wahrscheinlichkeit des <b>Fehlers 1. Art</b>. Kleineres α → weniger Fehlalarme, aber die Wahrscheinlichkeit des Fehlers 2. Art steigt.")

zq = dict(z95=r3(N.ppf(.95)), z975=r3(N.ppf(.975)), t95=r3(stats.t.ppf(.95, 9)), t975=r3(stats.t.ppf(.975, 9)),
          c05=r3(stats.chi2.ppf(.05, 11)), c95=r3(stats.chi2.ppf(.95, 11)), c025=r3(stats.chi2.ppf(.025, 11)), c975=r3(stats.chi2.ppf(.975, 11)))
card("Ablehnungsbereiche bestimmen", 80,
 "Geben Sie für α = 0.05 die Ablehnungsbereiche an: (a) Gauß-Test, linksseitig; (b) Gauß-Test, zweiseitig; (c) t-Test mit n = 10, rechtsseitig; (d) t-Test mit n = 10, zweiseitig; (e) Varianztest mit n = 12, linksseitig; (f) Varianztest mit n = 12, zweiseitig. <span class='pt'>(6 P)</span>",
 ["Richtung aus H₁ ablesen, dann Tabelle oben benutzen.", "t- und χ²-Tests: df = n − 1.",
  "R: <code>qnorm(0.95)</code>, <code>qt(0.95, 9)</code>, <code>qchisq(0.05, 11)</code> usw. In der Klausur stehen die Werte meist als R-Output da."],
 T("(a) \\((-\\infty;\\,-«z95»]\\) · (b) \\((-\\infty;\\,-«z975»]\\cup[«z975»;\\,\\infty)\\)<br>"
   "(c) \\([«t95»;\\,\\infty)\\) · (d) \\((-\\infty;\\,-«t975»]\\cup[«t975»;\\,\\infty)\\)<br>"
   "(e) \\([0;\\,«c05»]\\) · (f) \\([0;\\,«c025»]\\cup[«c975»;\\,\\infty)\\)", **zq),
 "χ² ist nicht symmetrisch: Für links brauchst du das kleine Quantil \\(\\chi^2_{\\alpha}\\), nicht „minus“ irgendwas.", fig=("sk_ab.svg", 92))

pl = N.cdf(-1.629); pr = 1 - N.cdf(2.2); pz = 2 * (1 - N.cdf(1.64))
card("p-Wert berechnen und interpretieren", 80,
 "Berechnen Sie den p-Wert (R-Befehl angeben) für (a) linksseitigen Gauß-Test mit z = −1.629, (b) rechtsseitigen Gauß-Test mit z = 2.2, (c) zweiseitigen Gauß-Test mit z = 1.64. Interpretieren Sie den p-Wert aus (b). <span class='pt'>(5 P)</span>",
 ["Links: \\(\\Phi(z)\\). Rechts: \\(1-\\Phi(z)\\). Zweiseitig: \\(2\\,(1-\\Phi(|z|))\\).",
  "Interpretation: Wahrscheinlichkeit unter H₀ für einen mindestens so extremen Wert; kleinstes α, zu dem H₀ verworfen würde."],
 T("(a) <code>pnorm(-1.629)</code> = \\(\\mathbf{«a»}\\) · (b) <code>1 - pnorm(2.2)</code> = \\(\\mathbf{«b»}\\) · (c) <code>2*(1 - pnorm(1.64))</code> = \\(\\mathbf{«c»}\\)<br>"
   "(b): Wäre H₀ wahr, würde man nur mit Wahrscheinlichkeit 0.014 eine noch größere Teststatistik beobachten. H₀ kann zu jedem α ≥ 0.014 verworfen werden.",
   a=r3(pl), b=r3(pr), c=r3(pz)),
 "Der p-Wert ist <b>nicht</b> die Wahrscheinlichkeit, dass H₀ wahr ist.")

card("Testentscheidung zu mehreren Niveaus", 70,
 "Ein Test liefert p = 0.014 (bzw. bei einem anderen Test die Teststatistik z = −1.629 mit linksseitigem Ablehnungsbereich). Treffen Sie die Entscheidungen für α = 1 %, 5 %, 10 % mit Begründung. <span class='pt'>(4 P)</span>",
 ["p ≤ α → verwerfen. Oder: Teststatistik im Ablehnungsbereich → verwerfen.", "Für jedes α ein Satz."],
 "p = 0.014: α = 10 % und 5 %: \\(0.014<\\alpha\\) → H₀ verwerfen. α = 1 %: \\(0.014>0.01\\) → H₀ nicht verwerfen.<br>"
 "z = −1.629: \\(A_{1\\%}=(-\\infty;-2.326]\\), \\(A_{5\\%}=(-\\infty;-1.645]\\), \\(A_{10\\%}=(-\\infty;-1.282]\\) → nur für <b>α = 10 %</b> verwerfen (−1.629 ≤ −1.282).",
 "Großes α macht es leichter, H₀ zu verwerfen.")

pb = 1 - stats.binom(10, .2).cdf(4)
card("Exakter Binomialtest mit Tabelle", 40,
 "Ein Händler behauptet, höchstens 20 % seiner Lose seien Nieten. Sie kaufen 10 Lose und ziehen 5 Nieten. Testen Sie zum Niveau 5 %, ob der Nietenanteil größer als 20 % ist. Gegeben: \\(P(Z\\le4)=0.9672\\) für \\(Z\\sim B(10;\\,0.2)\\). <span class='pt'>(5 P)</span>",
 ["Hypothesen: \\(H_0:\\pi\\le0.2\\) vs. \\(H_1:\\pi>0.2\\).", "Teststatistik Z = Anzahl Nieten, unter H₀ \\(B(10;0.2)\\).",
  "Rechtsseitig: p = \\(P(Z\\ge5)=1-P(Z\\le4)\\)."],
 T("\\(H_0:\\pi\\le0.2\\), \\(H_1:\\pi>0.2\\); \\(Z\\sim B(10;\\,0.2)\\) unter H₀, \\(z_{obs}=5\\)<br>p-Wert \\(=P(Z\\ge5)=1-0.9672=\\mathbf{«p»}\\le0.05\\) → H₀ verwerfen; ein Nietenanteil über 20 % ist zum Niveau 5 % statistisch abgesichert.",
   p=r3(pb)),
 "R: <code>1 - pbinom(4, 10, 0.2)</code> oder <code>binom.test(5, 10, 0.2, alternative = \"greater\")</code>.")

# ======================================================================
sec("8 · Spezielle Tests (V12)", None,
    ["<table class='tab' style='font-size:.85rem;margin:.1em 0'><tr><th>Test</th><th>wofür</th><th>Teststatistik</th><th>unter H₀</th></tr>"
     "<tr><td>Gauß-Test</td><td>μ, σ bekannt</td><td>\\(Z=\\frac{\\bar X-\\mu_0}{\\sigma}\\sqrt n\\)</td><td>N(0, 1)</td></tr>"
     "<tr><td>t-Test</td><td>μ, σ unbekannt</td><td>\\(T=\\frac{\\bar X-\\mu_0}{S_*}\\sqrt n\\)</td><td>t(n − 1)</td></tr>"
     "<tr><td>Binomialtest (approx.)</td><td>Anteil π, n groß</td><td>\\(Z=\\frac{X-n\\pi_0}{\\sqrt{n\\pi_0(1-\\pi_0)}}\\)</td><td>≈ N(0, 1)</td></tr>"
     "<tr><td>Varianztest</td><td>σ², Normalverteilung</td><td>\\(\\chi^2=\\frac{(n-1)S_*^2}{\\sigma_0^2}=\\frac{nS^2}{\\sigma_0^2}\\)</td><td>χ²(n − 1)</td></tr>"
     "<tr><td>Vorzeichentest</td><td>Median, keine Verteilungsannahme</td><td>Z = Anzahl \\(x_i\\le\\vartheta_0\\)</td><td>B(n; 0.5)</td></tr>"
     "<tr><td>χ²-Unabhängigkeit</td><td>zwei kategoriale Merkmale</td><td>\\(\\sum\\frac{(h_{jk}-\\tilde h_{jk})^2}{\\tilde h_{jk}}\\)</td><td>χ²((J−1)(K−1)), rechtsseitig</td></tr>"
     "<tr><td>χ²-Anpassung</td><td>passt eine vorgegebene Verteilung?</td><td>\\(\\sum\\frac{(h_j-n\\pi_j)^2}{n\\pi_j}\\)</td><td>χ²(J − 1), rechtsseitig</td></tr></table>",
     "<b>Antwortschema für jede Testaufgabe:</b> ① H₀/H₁ ② Teststatistik mit Formel + Zahl ③ Verteilung unter H₀ ④ Ablehnungsbereich oder p-Wert ⑤ Entscheidung als Satz im Sachkontext."])

z = (247.6 - 250) / (4 / 3); pz = N.cdf(z)
card("Gauß-Test (σ bekannt) vollständig", 85,
 "Eine Maschine soll 250 ml abfüllen; die Füllmenge ist normalverteilt mit σ² = 16. Bei n = 9 Flaschen ist \\(\\bar x=247.6\\). Sichern Sie zum Niveau 5 % ab, dass die Maschine im Mittel zu wenig abfüllt: Hypothesen, Prüfgröße mit Verteilung, Ablehnungsbereich, p-Wert, Entscheidung. <span class='pt'>(8 P)</span>",
 ["„zu wenig“ abzusichern → \\(H_1:\\mu<250\\) (linksseitig).", "\\(\\sigma=4\\), \\(\\sqrt n=3\\).", "p-Wert links: \\(\\Phi(z)\\)."],
 T("\\(H_0:\\mu\\ge250\\) vs. \\(H_1:\\mu<250\\)<br>\\(Z=\\frac{\\bar X-\\mu_0}{\\sigma}\\sqrt n=\\frac{247.6-250}{4}\\cdot3=\\mathbf{«z»}\\), unter H₀ \\(Z\\sim N(0,1)\\)<br>"
   "\\(A=(-\\infty;\\,-1.645]\\); p-Wert \\(=\\Phi(-1.8)=\\mathbf{«p»}\\)<br>\\(-1.8\\in A\\) (bzw. p < 0.05) → H₀ verwerfen. Zum Niveau 5 % ist abgesichert, dass die Maschine im Mittel weniger als 250 ml abfüllt.",
   z=r3(z)[:-2], p=r3(pz)),
 "Probeklausur 2022 (Aufgabe 8) und Tutorium 12 (Lucky Luke) folgen genau diesem Schema.")

xb = [19.2, 17.4, 18.5, 16.5, 18.9]; m = sum(xb) / 5; s2 = sum((v - m) ** 2 for v in xb) / 4; tt = (m - 17) / math.sqrt(s2 / 5)
card("t-Test per Hand (σ unbekannt)", 75,
 "Bleistifte sollen 17 cm lang sein. Gemessen: 19.2, 17.4, 18.5, 16.5, 18.9 (normalverteilt, σ unbekannt). Testen Sie zweiseitig zum Niveau 1 %. Gegeben: \\(t_{4;\\,0.995}=4.604\\), \\(t_{5;\\,0.995}=4.032\\). <span class='pt'>(7 P)</span>",
 ["\\(\\bar x\\) und \\(s_*^2=\\frac1{n-1}\\sum(x_i-\\bar x)^2\\) berechnen.", "df = n − 1 = 4.", "Zweiseitig: \\(|t|\\ge t_{4;0.995}\\) → verwerfen."],
 T("\\(H_0:\\mu=17\\) vs. \\(H_1:\\mu\\neq17\\)<br>\\(\\bar x=18.1\\), \\(s_*^2=«s2»\\), \\(T=\\frac{18.1-17}{\\sqrt{«s2»}}\\sqrt5=\\mathbf{«t»}\\), unter H₀ \\(T\\sim t(4)\\)<br>"
   "\\(A=(-\\infty;-4.604]\\cup[4.604;\\infty)\\); \\(|«t»|<4.604\\) → H₀ wird <b>nicht</b> verworfen. Eine Abweichung von 17 cm ist zum Niveau 1 % nicht nachweisbar.",
   s2=r3(s2), t=r3(tt)),
 "Mit bekanntem σ = 1.5 (Gauß-Test) hätte z = 1.640 – auch dann keine Ablehnung (V12).")

data = [32, 35, 29, 38, 31, 34]
res = {alt: stats.ttest_1samp(data, 30, alternative=alt) for alt in ("less", "greater", "two-sided")}
tv = res["greater"].statistic
log("t lieferzeit", tv)
card("t.test-Output: richtigen Code wählen und entscheiden", 70,
 "Ein Lieferdienst behauptet: Lieferzeit im Mittel höchstens 30 Minuten. Sie wollen zum Niveau 5 % absichern, dass sie im Mittel länger ist. Daten: 32, 35, 29, 38, 31, 34. Drei Versuche in R:<br>"
 + T("(1) <code>t.test(x, mu = 30, alternative = \"l\")</code> → t = «t», p-value = «p1»<br>"
     "(2) <code>t.test(x, mu = 30, alternative = \"g\")</code> → t = «t», p-value = «p2»<br>"
     "(3) <code>t.test(x, mu = 30)</code> → t = «t», p-value = «p3»<br>",
     t=r4(tv), p1=r4(res["less"].pvalue), p2=r4(res["greater"].pvalue), p3=r4(res["two-sided"].pvalue)) +
 "Welcher Code ist richtig? Treffen Sie die Testentscheidung. <span class='pt'>(4 P)</span>",
 ["H₁: μ > 30 → <code>alternative = \"greater\"</code> (\"g\"). Der Default ist zweiseitig.", "Entscheidung über p ≤ α."],
 T("Richtig ist <b>(2)</b>, da \\(H_1:\\mu>30\\) rechtsseitig ist.<br>p = «p2» < 0.05 → H₀ verwerfen; eine mittlere Lieferzeit über 30 Minuten ist zum Niveau 5 % statistisch abgesichert.",
   p2=r4(res["greater"].pvalue)),
 "Probeklausur 2022, Aufgabe 8c (3 P). Achte auch darauf, ob der richtige Datenvektor und das richtige mu verwendet werden.")

zp = (182 - 200) / math.sqrt(500 * .4 * .6); pp = N.cdf(zp)
card("Approximativer Binomialtest für einen Anteil", 60,
 "Eine Partei behauptet, 40 % Zustimmung zu haben. In einer Umfrage mit n = 500 stimmen 182 zu. Sichern Sie ab, dass der Anteil kleiner als 40 % ist (Normalapproximation) – zu α = 5 % und α = 10 %. <span class='pt'>(7 P)</span>",
 ["\\(H_0:\\pi\\ge0.4\\) vs. \\(H_1:\\pi<0.4\\).", "\\(Z=\\frac{X-n\\pi_0}{\\sqrt{n\\pi_0(1-\\pi_0)}}\\) mit X = Anzahl (nicht Anteil!).",
  "Kritische Werte: \\(-z_{0.95}=-1.645\\), \\(-z_{0.90}=-1.282\\)."],
 T("\\(Z=\\frac{182-500\\cdot0.4}{\\sqrt{500\\cdot0.4\\cdot0.6}}=\\frac{-18}{\\sqrt{120}}=\\mathbf{«z»}\\), unter H₀ approx. N(0, 1)<br>"
   "α = 5 %: \\(-1.643>-1.645\\) → knapp <b>nicht</b> verwerfen. α = 10 %: \\(-1.643\\le-1.282\\) → verwerfen.<br>p-Wert \\(=\\Phi(-1.643)=«p»\\)",
   z=r3(zp), p=r3(pp)),
 "Grenzfall mit Absicht! Mit 3 Nachkommastellen rechnen, nicht vorher grob runden. (Wie Tutorium 11: Iran-Letalitätsrate.)")

cups = [0.32, 0.35, 0.34, 0.37, 0.36]; mc = sum(cups) / 5; sc = sum((v - mc) ** 2 for v in cups) / 4; chi = 4 * sc / 0.08 ** 2
crit = stats.chi2.ppf(.01, 4); pc = stats.chi2.cdf(chi, 4)
log("chi kaffee", chi)
card("Varianztest (χ²) vollständig", 60,
 "Die Standardabweichung der Füllmenge soll kleiner als σ = 0.08 l sein. Stichprobe: 0.32, 0.35, 0.34, 0.37, 0.36 (normalverteilt). (a) Unverzerrte Stichprobenvarianz (4 Nachkommastellen). (b) Hypothesen. (c) Prüfgröße. (d) Entscheidung zu α = 0.01, gegeben \\(\\chi^2_{4;\\,0.01}=0.297\\). <span class='pt'>(8 P)</span>",
 ["Aufpassen: Gegeben ist σ = 0.08, im Test steht \\(\\sigma_0^2=0.0064\\).", "\\(\\chi^2=\\frac{(n-1)s_*^2}{\\sigma_0^2}\\), df = 4, linksseitig → \\(A=[0;\\chi^2_{4;\\alpha}]\\)."],
 T("(a) \\(\\bar x=0.348\\), \\(s_*^2=\\frac{0.00148}{4}=0.00037\\approx\\mathbf{«s»}\\) (weiterrechnen mit 0.00037)<br>(b) \\(H_0:\\sigma^2\\ge0.0064\\) vs. \\(H_1:\\sigma^2<0.0064\\)<br>"
   "(c) \\(\\chi^2=\\frac{4\\cdot0.00037}{0.0064}=\\mathbf{«c»}\\sim\\chi^2(4)\\) unter H₀<br>(d) \\(0.231\\in[0;\\,0.297]\\) → H₀ verwerfen; geringere Schwankung zum Niveau 1 % abgesichert (p = «p»).",
   s=r4(sc), c=r3(chi), p=r3(pc)),
 "Testat 6, Aufgabe 7 und Tutorium 12, Aufgabe 2. Häufigster Fehler: σ statt σ² in den Nenner.")

X = 12 * 29368.0208 / 71479.11; crit10 = stats.chi2.ppf(.1, 11); pX = stats.chi2.cdf(X, 11)
card("p-Wert und Ablehnungsbereich in die χ²-Dichte einzeichnen", 30,
 T("Varianztest mit n = 12, \\(H_1:\\sigma^2<71479.11\\), Prüfgröße X = «x». Zeichnen Sie den Ablehnungsbereich für α = 0.1 (\\(\\chi^2_{11;\\,0.1}=«k»\\)) und den p-Wert in die Dichte der χ²(11)-Verteilung ein und entscheiden Sie grafisch. <span class='pt'>(4 P)</span>", x=r3(X), k=r3(crit10)),
 ["Linksseitig: Ablehnungsbereich = Fläche <b>links</b> von 5.578 schraffieren.", "p-Wert = Fläche links von der Prüfgröße 4.930.",
  "p-Fläche liegt <b>innerhalb</b> der α-Fläche ⇔ p < α ⇔ verwerfen."],
 T("Ablehnungsbereich [0; «k»] und p-Fläche [0; «x»] schraffiert (siehe Bild). Die p-Fläche ist kleiner als die α-Fläche (p = «p» < 0.1) → H₀ verwerfen: Die Umsatzschwankung ist zum Niveau 10 % signifikant kleiner geworden.",
   k=r3(crit10), x=r3(X), p=r3(pX)),
 None, fig=("sk_chi2.svg", 60))

vz = [38, 42, 47, 49, 51, 55, 44, 40, 46, 53]; Zs = sum(v <= 50 for v in vz); bz = stats.binom(10, .5)
pvz = bz.cdf(10 - Zs) + 1 - bz.cdf(Zs - 1)
card("Vorzeichentest für den Median", 30,
 "Bearbeitungszeiten (Minuten): 38, 42, 47, 49, 51, 55, 44, 40, 46, 53. Testen Sie ohne Verteilungsannahme zweiseitig zum Niveau 5 %, ob der Median von 50 abweicht. \\(P(Z\\le3)=0.1719\\) für \\(Z\\sim B(10;\\,0.5)\\). <span class='pt'>(5 P)</span>",
 ["Z = Anzahl Beobachtungen ≤ 50. Unter H₀ ist Z ~ B(n; 0.5).", "Zweiseitig: Werte, die mindestens so extrem sind, auf beiden Seiten zählen (Symmetrie!)."],
 T("\\(H_0:x_{med}=50\\) vs. \\(H_1:x_{med}\\neq50\\); \\(Z=7\\) (Werte ≤ 50)<br>p-Wert \\(=P(Z\\ge7)+P(Z\\le3)=2\\cdot0.1719=\\mathbf{«p»}>0.05\\) → H₀ nicht verwerfen.",
   p=r3(pvz)))

obs = [[60, 20], [30, 30]]; rs = [sum(r) for r in obs]; cs = [sum(c) for c in zip(*obs)]; n = sum(rs)
exp = [[rs[i] * cs[j] / n for j in range(2)] for i in range(2)]
chi2 = sum((obs[i][j] - exp[i][j]) ** 2 / exp[i][j] for i in range(2) for j in range(2)); pch = 1 - stats.chi2.cdf(chi2, 1)
log("chi2 unabh", chi2)
card("χ²-Unabhängigkeitstest per Hand", 55,
 "Studiengang und Klausurergebnis: BWL – bestanden 60, nicht bestanden 20; VWL – bestanden 30, nicht bestanden 30. Testen Sie zum Niveau 5 %, ob Studiengang und Ergebnis abhängig sind (\\(\\chi^2_{1;\\,0.95}=3.841\\)). <span class='pt'>(8 P)</span>",
 ["Erwartete Häufigkeit = Zeilensumme × Spaltensumme / n.", "\\(\\chi^2=\\sum\\frac{(h-\\tilde h)^2}{\\tilde h}\\) über <b>alle</b> Zellen.",
  "df = (J − 1)(K − 1) = 1; immer rechtsseitig: \\(A=[\\chi^2_{df;1-\\alpha};\\infty)\\)."],
 T("\\(H_0\\): unabhängig vs. \\(H_1\\): abhängig. n = 140, Zeilen 80/60, Spalten 90/50.<br>"
   "\\(\\tilde h\\): «e11», «e12» (BWL); «e21», «e22» (VWL)<br>\\(\\chi^2=\\frac{(60-51.43)^2}{51.43}+\\frac{(20-28.57)^2}{28.57}+\\frac{(30-38.57)^2}{38.57}+\\frac{(30-21.43)^2}{21.43}=\\mathbf{«c»}\\)<br>"
   "\\(«c»\\ge3.841\\) → H₀ verwerfen; Studiengang und Ergebnis sind zum Niveau 5 % abhängig (p = «p»).",
   e11=r2(exp[0][0]), e12=r2(exp[0][1]), e21=r2(exp[1][0]), e22=r2(exp[1][1]), c=r3(chi2), p=r3(pch)),
 "Die χ²-Größe kennst du aus Tag 1 (Kontingenz). Neu ist nur: Vergleich mit dem Quantil und ein Testsatz.")

h = [8, 9, 12, 7, 10, 14]; ca = sum((v - 10) ** 2 / 10 for v in h)
card("χ²-Anpassungstest (Würfel fair?)", 40,
 "Ein Würfel wurde 60-mal geworfen: Augenzahlen 1–6 mit Häufigkeiten 8, 9, 12, 7, 10, 14. Testen Sie zum Niveau 5 %, ob der Würfel fair ist (\\(\\chi^2_{5;\\,0.95}=11.07\\)). <span class='pt'>(6 P)</span>",
 ["\\(H_0:\\pi_j=\\frac16\\) für alle j.", "Erwartet: \\(n\\pi_j=10\\) je Augenzahl.", "df = J − 1 = 5 (minus Anzahl geschätzter Parameter, hier 0)."],
 T("\\(\\chi^2=\\frac{(8-10)^2+(9-10)^2+(12-10)^2+(7-10)^2+0^2+(14-10)^2}{10}=\\frac{34}{10}=\\mathbf{«c»}\\)<br>\\(3.4<11.07\\) → H₀ nicht verwerfen; kein Nachweis, dass der Würfel unfair ist.", c=r3(ca)[:-2]),
 "„Nicht verwerfen“ heißt nicht „der Würfel ist fair“ – nur: kein Beweis für Unfairness.")

zc = (4.10 - 3.20) / 0.40; pcc = 2 * (1 - N.cdf(zc))
card("Test mit einer einzigen Beobachtung (Cappuccino-Typ)", 30,
 "Kaffeepreise in Göttingen seien \\(N(3.20;\\,0.40^2)\\). Auf dem Kontoauszug steht ein Kaffee für 4.10 €. Testen Sie zum Niveau 5 %, ob er nicht aus Göttingen stammt: Hypothesen, Prüfgröße, p-Wert, KI für den Preis dieses Kaffees, Entscheidung. <span class='pt'>(7 P)</span>",
 ["n = 1 → \\(Z=\\frac{x-\\mu_0}{\\sigma}\\).", "„stammt nicht aus Göttingen“ = Preis gehört nicht zu dieser Verteilung → zweiseitig.",
  "KI: \\(x\\pm1.96\\,\\sigma\\); enthält es 3.20?"],
 T("\\(H_0:\\mu=3.20\\) vs. \\(H_1:\\mu\\neq3.20\\)<br>\\(Z=\\frac{4.10-3.20}{0.40}=\\mathbf{«z»}\\) · p-Wert \\(=2(1-\\Phi(2.25))=\\mathbf{«p»}\\)<br>"
   "KI: \\(4.10\\pm1.96\\cdot0.40=[«l»;\\ «u»]\\) enthält 3.20 nicht → H₀ verwerfen (auch p < 0.05).",
   z=r2(zc), p=r3(pcc), l=r3(4.10 - 1.959964 * .4), u=r3(4.10 + 1.959964 * .4)),
 "Testat 6, Aufgabe 5 hatte diesen Aufbau (dort mit anderen Zahlen und knapper Entscheidung).")

card("Welcher Test passt? (Entscheidungsbaum)", 100,
 "Ordnen Sie den passenden Test zu: (a) Mittlere Wartezeit > 10 min? σ unbekannt, n = 12. (b) Anteil Raucher ≠ 25 %? n = 400. (c) Hängen Geschlecht und Parteiwahl zusammen? (d) Ist die Streuung kleiner geworden? (e) Mittleres Gewicht ≠ 500 g, σ = 3 bekannt. (f) Median ≠ 50, keine Verteilungsannahme. (g) Treten alle Kategorien gleich häufig auf? <span class='pt'>(7 P)</span>",
 ["Worum geht es? Mittelwert → Gauß/t (σ bekannt?). Anteil → Binomial. Varianz → χ²-Varianztest. Zwei kategoriale Merkmale → χ²-Unabhängigkeit. Vorgegebene Verteilung → χ²-Anpassung. Median ohne Annahme → Vorzeichentest."],
 "(a) t-Test (rechtsseitig) · (b) approx. Binomialtest (zweiseitig) · (c) χ²-Unabhängigkeitstest · (d) χ²-Varianztest (linksseitig) · (e) Gauß-Test (zweiseitig) · (f) Vorzeichentest · (g) χ²-Anpassungstest")

# ======================================================================
sec("9 · Lineare Regression (V13 / Tutorium 13)",
    "V13 ist ein Ausblick, Tutorium 13 rechnet aber Regressionsaufgaben. Klausurrelevanz deshalb mittel bis niedrig – lerne diesen Abschnitt erst, wenn 1–8 sitzen.",
    ["Modell: \\(y_i=\\beta_0+\\beta_1x_i+\\varepsilon_i\\), \\(E(\\varepsilon_i)=0\\), \\(Var(\\varepsilon_i)=\\sigma^2\\).",
     "<b>KQ-Schätzer:</b> \\(\\hat\\beta_1=\\frac{\\sum(x_i-\\bar x)(y_i-\\bar y)}{\\sum(x_i-\\bar x)^2}=\\frac{\\sum x_iy_i-n\\bar x\\bar y}{\\sum x_i^2-n\\bar x^2}\\), \\(\\hat\\beta_0=\\bar y-\\hat\\beta_1\\bar x\\).",
     "<b>Prognose</b> \\(\\hat y_i=\\hat\\beta_0+\\hat\\beta_1x_i\\), <b>Residuum</b> \\(\\hat\\varepsilon_i=y_i-\\hat y_i\\), \\(R^2=\\frac{\\sum(\\hat y_i-\\bar y)^2}{\\sum(y_i-\\bar y)^2}\\) (Anteil erklärter Streuung, 0 bis 1).",
     "<b>Interpretation</b> \\(\\hat\\beta_j\\): Steigt \\(x_j\\) um eine Einheit, ändert sich y im Durchschnitt um \\(\\hat\\beta_j\\) Einheiten – ceteris paribus.",
     "<b>Signifikanztest</b> \\(H_0:\\beta_j=0\\): \\(T=\\frac{\\hat\\beta_j}{\\hat\\sigma_{\\hat\\beta_j}}\\sim t(n-p-1)\\) (= t value), p-Wert in Pr(>|t|). <b>KI:</b> \\(\\hat\\beta_j\\pm t_{n-p-1;1-\\alpha/2}\\hat\\sigma_{\\hat\\beta_j}\\)."])

x = [1, 2, 3, 4, 5]; y = [3, 5, 4, 7, 9]
xm = sum(x) / 5; ym = sum(y) / 5; sxy = sum((a - xm) * (b - ym) for a, b in zip(x, y)); sxx = sum((a - xm) ** 2 for a in x)
b1 = sxy / sxx; b0 = ym - b1 * xm; yh = [b0 + b1 * a for a in x]; res = [b - c for b, c in zip(y, yh)]
R2 = sum((c - ym) ** 2 for c in yh) / sum((b - ym) ** 2 for b in y)
assert abs(b1 - 1.4) < 1e-12 and abs(b0 - 1.4) < 1e-12
card("KQ-Gerade per Hand", 35,
 "Werbeausgaben x (Tsd. €) und Umsatz y (Tsd. €): (1, 3), (2, 5), (3, 4), (4, 7), (5, 9). Schätzen Sie \\(\\hat\\beta_0\\) und \\(\\hat\\beta_1\\) nach der Methode der kleinsten Quadrate und geben Sie die Regressionsgerade an. Interpretieren Sie \\(\\hat\\beta_1\\). <span class='pt'>(6 P)</span>",
 ["Tabelle: \\(x_i-\\bar x\\), \\(y_i-\\bar y\\), Produkt, \\((x_i-\\bar x)^2\\).", "Erst \\(\\hat\\beta_1\\), dann \\(\\hat\\beta_0=\\bar y-\\hat\\beta_1\\bar x\\).",
  "Interpretation mit Einheiten und „im Durchschnitt“."],
 "\\(\\bar x=3\\), \\(\\bar y=5.6\\); \\(\\sum(x_i-\\bar x)(y_i-\\bar y)=5.2+0.6+0+1.4+6.8=14\\); \\(\\sum(x_i-\\bar x)^2=10\\)<br>"
 "\\(\\hat\\beta_1=\\frac{14}{10}=\\mathbf{1.4}\\), \\(\\hat\\beta_0=5.6-1.4\\cdot3=\\mathbf{1.4}\\) → \\(\\hat y=1.4+1.4x\\)<br>"
 "Steigen die Werbeausgaben um 1 000 €, steigt der Umsatz im Durchschnitt um 1 400 €.", None, fig=("sk_reg.svg", 52))

card("Prognose, Residuen und R²", 30,
 "(Fortsetzung) Berechnen Sie die prognostizierten Werte, die Residuen und \\(R^2\\). Interpretieren Sie \\(R^2\\). Welcher Umsatz wird bei 6 000 € Werbung prognostiziert? <span class='pt'>(6 P)</span>",
 ["\\(\\hat y_i\\) in die Gerade einsetzen; Residuum = beobachtet − prognostiziert.", "\\(R^2=1-\\frac{\\sum\\hat\\varepsilon_i^2}{\\sum(y_i-\\bar y)^2}\\) geht schneller.",
  "Bei einer einfachen Regression gilt \\(R^2=r_{xy}^2\\) (Kontrolle mit Tag 1)."],
 T("\\(\\hat y=2.8;\\ 4.2;\\ 5.6;\\ 7.0;\\ 8.4\\) · \\(\\hat\\varepsilon=0.2;\\ 0.8;\\ -1.6;\\ 0;\\ 0.6\\)<br>"
   "\\(R^2=1-\\frac{3.6}{23.2}=\\mathbf{«r»}\\): 84.5 % der Streuung des Umsatzes werden durch die Werbung erklärt.<br>Prognose: \\(1.4+1.4\\cdot6=\\mathbf{9.8}\\) Tsd. €",
   r=r3(R2)))

# --- lm-Output echt aus R
rcode = r'''set.seed(42); n <- 40
Lernstunden <- round(runif(n, 0, 20), 1); Vorkurs <- rbinom(n, 1, 0.5)
Punkte <- round(18 + 2.1*Lernstunden + 6*Vorkurs + rnorm(n, 0, 7), 1)
m <- lm(Punkte ~ Lernstunden + Vorkurs); print(summary(m))
cat("@@", coef(summary(m)), df.residual(m), "\n")'''
out = subprocess.run(["Rscript", "-e", rcode], capture_output=True, text=True).stdout
summ, nums = out.split("@@")
summ = summ[summ.index("Call:"):].rstrip()
v = [float(t) for t in nums.split()]
est, se, tv, pv, dfr = v[0:3], v[3:6], v[6:9], v[9:12], int(v[12])
q = stats.t.ppf(.975, dfr)
log("lm est", est); log("lm p", pv)
card("lm-Output lesen: Interpretation, Prognose, Signifikanz", 35,
 "Gegeben ist der R-Output einer Regression der Klausurpunkte auf Lernstunden und Vorkurs (1 = besucht, 0 = nicht):<pre class='out' style='font-size:.68rem'>" + html.escape(summ) + "</pre>"
 "(a) Interpretieren Sie den Koeffizienten von Lernstunden. (b) Prognostizieren Sie die Punkte für 10 Lernstunden mit Vorkurs. (c) Testen Sie zum Niveau 5 %, ob Vorkurs einen Einfluss hat (Hypothesen, Prüfgröße mit Verteilung, R-Befehl für den p-Wert, Entscheidung). (d) Wie groß ist n? (e) 95 %-KI für den Koeffizienten von Lernstunden. <span class='pt'>(10 P)</span>",
 ["Estimate = \\(\\hat\\beta_j\\); Std. Error = \\(\\hat\\sigma_{\\hat\\beta_j}\\); t value = Estimate / Std. Error; Pr(>|t|) = zweiseitiger p-Wert.",
  "Freiheitsgrade stehen bei „Residual standard error … on df degrees of freedom“; n = df + p + 1.",
  "Dummy-Variable (0/1): Koeffizient = durchschnittlicher Unterschied zwischen den Gruppen, c.p."],
 T("(a) Eine zusätzliche Lernstunde erhöht die Punktzahl im Durchschnitt um «b1» Punkte, ceteris paribus.<br>"
   "(b) \\(\\hat y=«b0»+«b1»\\cdot10+«b2»\\cdot1=\\mathbf{«yh»}\\)<br>"
   "(c) \\(H_0:\\beta_{Vorkurs}=0\\) vs. \\(H_1:\\beta_{Vorkurs}\\neq0\\); \\(T=\\frac{«b2»}{«s2»}=«t2»\\sim t(«df»)\\); <code>2*(1-pt(«t2», «df»))</code> = «p2» → «dec»<br>"
   "(d) \\(n=«df»+2+1=«n»\\)<br>(e) \\(«b1»\\pm«q»\\cdot«s1»=[«l»;\\ «u»]\\) (mit <code>qt(0.975, «df»)</code> = «q»)",
   b0=r3(est[0]), b1=r3(est[1]), b2=r3(est[2]), yh=r3(est[0] + 10 * est[1] + est[2]), s2=r3(se[2]), t2=r3(tv[2]), df=dfr,
   p2=r3(pv[2]), dec="H₀ verwerfen, Vorkurs hat einen signifikanten Einfluss." if pv[2] <= .05 else "H₀ nicht verwerfen.",
   n=dfr + 3, q=r3(q), s1=r3(se[1]), l=r3(est[1] - q * se[1]), u=r3(est[1] + q * se[1])),
 "Tutorium 13, Aufgabe 3 (Piggy Bank) ist genau dieser Typ. Die Signifikanzsterne sind nur eine Legende für den p-Wert.")

# ======================================================================
sec("10 · Klausurstrategie Teil A", None,
    ["<b>Reihenfolge:</b> Erst alle Aufgaben überfliegen (3 Min.), dann sichere Punkte holen: Hypothesen, Verteilung erkennen, E/Var, Bayes. Lange Integrale und ML-Umformungen zuletzt.",
     "<b>Zeit:</b> 100 Minuten für 75 Punkte ≈ 1.3 Minuten pro Punkt. Hängst du mehr als 5 Minuten fest: weiter und später zurückkommen.",
     "<b>Teilpunkte:</b> Formel allgemein hinschreiben, Werte einsetzen, Ergebnis markieren. Auch ohne Endergebnis gibt es Punkte für Formel und Ansatz.",
     "<b>Folgefehler</b> werden berücksichtigt – nie ein Kästchen leer lassen; mit dem eigenen (falschen) Zwischenergebnis weiterrechnen.",
     "<b>Kontrollfragen:</b> Wahrscheinlichkeit zwischen 0 und 1? Varianz ≥ 0? |ρ| ≤ 1? KI enthält den Schätzer? Richtiges Quantil (1 − α/2 bei zweiseitig)? df = n − 1?"])

card("Was auf dein A4-Blatt (Seite 2) gehört", 100,
 "Stellen Sie die Inhalte für die Rückseite Ihres handgeschriebenen A4-Blatts zusammen (Tag 1 steht auf der Vorderseite). <span class='pt'>(0 P – aber viele Punkte in der Klausur)</span>",
 ["Nur, was du nicht sicher im Kopf hast. Lieber Formeln + Mini-Beispiel als lange Texte.", "Selbst schreiben! Kopien sind nicht erlaubt."],
 "① Rechenregeln W'keit + totale W'keit + Bayes (1 Zeile Baum-Skizze)<br>② E/Var diskret und stetig, Verschiebungssatz, \\(E(aX+b)\\), \\(Var(aX+bY)\\) mit Cov<br>"
 "③ Verteilungstabelle (Be, B, Po, U, Exp, N) mit f, E, Var, R-Kürzel; \\(Z=\\frac{X-\\mu}\\sigma\\); z-Quantile 1.28/1.645/1.96/2.33/2.576<br>"
 "④ Bias, MSE = Bias² + Var, konsistent; ML-Rezept + Log-Regeln + Standardergebnisse<br>"
 "⑤ KI-Tabelle (z, t, Anteil, Varianz) ⑥ Test-Tabelle (Teststatistiken + Ablehnungsbereiche + p-Wert-Formeln) ⑦ Antwortschema für Tests ⑧ KQ-Formeln, R², Interpretation c.p.")

card("Lernplan bis zur Klausur (9. Oktober)", 100,
 "Planen Sie die verbleibenden Tage. <span class='pt'>(0 P)</span>",
 ["Jeden Tag: neue Abschnitte + 20 Minuten Wiederholung des Vortags (Karten ohne Hinsehen lösen).",
  "R-Komplettkurs parallel: abends 1–2 Stunden (Teil B ist 45 Punkte!)."],
 "<b>Tag 1:</b> Abschnitt 1 (Wahrscheinlichkeit) · <b>Tag 2:</b> Abschnitt 2 (Zufallsvariablen) · <b>Tag 3:</b> Abschnitt 3 (Verteilungen) · "
 "<b>Tag 4:</b> Abschnitte 4–5 (Schätzer, ML) · <b>Tag 5:</b> Abschnitte 6–8 (KI, Tests) · <b>Tag 6:</b> Abschnitt 9 + Probeklausur A und ML-Übungsklausur auf Zeit · <b>Tag 7:</b> Fehler nacharbeiten, A4-Blatt fertig schreiben, früh schlafen.")
