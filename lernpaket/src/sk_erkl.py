r"""Erklärschicht für den Statistik-Komplettkurs:
LERN  = Lernteil vor jedem Abschnitt (Abschnittsnummer → HTML)
VERST = 'Verstehen'-Kasten je Karte (Kartentitel → HTML)
CHECK = Kurz-Check je Abschnitt (Abschnittsnummer → [(Frage, Lösung)])"""

LERN = {}
VERST = {}
CHECK = {}

# ======================================================================
LERN["1"] = r"""
<p><b>Worum geht es?</b> Eine Wahrscheinlichkeit ist eine Zahl zwischen 0 und 1, die sagt, wie oft etwas <i>auf lange Sicht</i> passiert. P = 0.25 heißt: bei sehr vielen Wiederholungen ungefähr in jedem vierten Fall.</p>
<p><b>Ereignisse sind Mengen.</b> Ω ist die Liste aller möglichen Ergebnisse (Würfel: {1,…,6}). Ein Ereignis ist ein Teil davon, z. B. „gerade“ = {2, 4, 6}. Deshalb rechnen wir mit Mengenzeichen:
\(A\cap B\) = „A <b>und</b> B passieren beide“ (Schnitt), \(A\cup B\) = „mindestens eines“ (Vereinigung), \(\bar A\) = „A passiert nicht“.</p>
<p><b>Bedingte Wahrscheinlichkeit = die Welt wird kleiner.</b> \(P(A|B)\) heißt: Wir <i>wissen schon</i>, dass B passiert ist. Dann zählt nur noch B als neue Welt.
Beispiel Würfel: B = „höchstens 3“ = {1, 2, 3}, A = „gerade“. In der kleinen Welt {1, 2, 3} ist nur die 2 gerade → \(P(A|B)=\frac13\). Genau das sagt die Formel \(\frac{P(A\cap B)}{P(B)}=\frac{1/6}{3/6}\).</p>
<p><b>Unabhängig</b> heißt: Das Wissen über B ändert nichts an A, also \(P(A|B)=P(A)\). Daraus folgt die Prüfregel \(P(A\cap B)=P(A)\cdot P(B)\).</p>
<p><b>Baumdiagramm – das wichtigste Werkzeug:</b> 1. Stufe = „Ursache / Gruppe“ (\(A_1, A_2, \dots\)), 2. Stufe = „Ergebnis“ (B oder \(\bar B\)). An die Äste schreibst du die Wahrscheinlichkeiten.
<b>Entlang eines Pfades multiplizieren</b>, <b>mehrere Pfade addieren</b>. Totale Wahrscheinlichkeit = alle Pfade zu B addieren. Bayes = „mein Pfad“ geteilt durch „alle Pfade zu B“.</p>
<div class="vorgemacht"><b>Vorgemacht (Schritt für Schritt):</b> 60 % der Kunden zahlen mit Karte (K), 40 % bar. Kartenzahler kaufen mit 0.5 ein Getränk (G), Barzahler mit 0.2.
<ol><li>Benennen: \(P(K)=0.6\), \(P(\bar K)=0.4\), \(P(G|K)=0.5\), \(P(G|\bar K)=0.2\).</li>
<li>Pfade zu G: \(0.6\cdot0.5=0.30\) und \(0.4\cdot0.2=0.08\).</li>
<li>Totale W'keit: \(P(G)=0.30+0.08=0.38\).</li>
<li>Bayes: Ein Getränkekäufer zahlt mit Karte mit \(P(K|G)=\frac{0.30}{0.38}=0.789\).</li></ol></div>
<p><b>Typische Denkfehler:</b> ① \(P(A|B)\) und \(P(B|A)\) verwechseln (Bedingung steht immer rechts). ② „unabhängig“ mit „disjunkt“ verwechseln. ③ \(P(A\cup B)=P(A)+P(B)\) rechnen, obwohl A und B gemeinsam auftreten können – dann den Schnitt abziehen.</p>"""

CHECK["1"] = [
    (r"\(P(A)=0.3\), \(P(B)=0.4\), A und B unabhängig. Berechne \(P(A\cap B)\) und \(P(A\cup B)\).",
     r"\(P(A\cap B)=0.3\cdot0.4=0.12\); \(P(A\cup B)=0.3+0.4-0.12=0.58\)"),
    (r"Fairer Würfel: Wie groß ist P(gerade | Augenzahl > 3)?",
     r"Neue Welt {4, 5, 6}, davon gerade {4, 6} → \(\frac23=0.667\)"),
    (r"2 % der Teile sind defekt. Ein Prüfgerät schlägt bei defekten Teilen mit 0.9 an, bei intakten mit 0.05. Wie oft schlägt es insgesamt an?",
     r"\(0.9\cdot0.02+0.05\cdot0.98=0.018+0.049=0.067\)"),
]

VERST.update({
"Ein Lösungskästchen richtig füllen": r"Die Korrektur vergibt Punkte für <b>Formel → Einsetzen → Ergebnis</b>. Wer nur „0.6“ schreibt und sich verrechnet, bekommt 0 Punkte. Wer die Formel hinschreibt, bekommt trotz Rechenfehler meist Teilpunkte. Gewöhne dir diese drei Schritte bei jeder Aufgabe an.",
"Text in Mengen-Sprache übersetzen": r"Stell dir das Venn-Diagramm mit vier Feldern vor: nur A, nur B, beides, keines. Gegeben sind \(P(A)=0.5\) (nur A + beides), \(P(B)=0.4\) (nur B + beides) und beides = 0.15. Dann ist <b>nur A</b> = 0.5 − 0.15 = 0.35 und <b>nur B</b> = 0.4 − 0.15 = 0.25. <b>Keines</b> ist der Rest bis 1: 1 − 0.35 − 0.25 − 0.15 = 0.25. „Genau eines“ = nur A + nur B = 0.6. Mit diesen vier Feldern kannst du jede Frage dieser Art beantworten.",
"Mengen und Mächtigkeiten im Laplace-Experiment": r"Laplace heißt: Jede Zahl ist gleich wahrscheinlich. Deshalb ist Wahrscheinlichkeit hier einfach <b>Abzählen</b>. Schreibe zuerst jede Menge vollständig aus (besonders das Komplement), dann bilde Schnitt bzw. Vereinigung durch Vergleichen. Bei \(P(A|\bar B)\) ist \(\bar B\) die neue Welt: 6 Zahlen, davon 3 auch in A → 3/6.",
"Zwei Würfel: Abzählen mit 36 Paaren": r"Warum 36 und nicht 21? Weil nur die <b>geordneten</b> Paare gleich wahrscheinlich sind. (2,6) heißt „erster Würfel 2, zweiter 6“ – das ist ein anderes Ergebnis als (6,2). Würde man die Reihenfolge ignorieren, hätte ein Pasch wie (4,4) dieselbe Wahrscheinlichkeit wie {2,6}, was falsch ist (er hat nur halb so viel). Tipp: 6×6-Tabelle zeichnen und die Felder markieren.",
"Rechenregeln: fehlende Wahrscheinlichkeiten finden": r"Der Additionssatz \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\) hat vier Größen. Kennst du drei, bekommst du die vierte durch Umstellen. Der Schnitt wird abgezogen, weil er in \(P(A)\) <i>und</i> in \(P(B)\) steckt, also sonst doppelt gezählt wäre. Unabhängigkeit prüfst du danach immer mit dem Produkt-Test.",
"Bedingte Wahrscheinlichkeit und Komplement": r"Rechenweg: Aus \(P(A|B)=\frac{P(A\cap B)}{P(B)}\) folgt durch Multiplizieren mit \(P(B)\) der Schnitt \(P(A\cap B)=0.4\cdot0.5=0.2\). Für \(P(A|\bar B)\) brauchst du den Teil von A <b>außerhalb</b> von B: \(P(A)-P(A\cap B)=0.1\). Diesen teilst du durch die neue Welt \(P(\bar B)=0.5\). Merke: Fast jede Aufgabe mit bedingten Wahrscheinlichkeiten beginnt mit dem Schnitt.",
"Unabhängigkeit von Ereignissen prüfen": r"Unabhängigkeit ist eine <b>Rechen-Eigenschaft</b>, keine Bauchgefühl-Frage. Man sieht sie nicht an den Mengen, man muss \(P(A\cap B)\) und \(P(A)\cdot P(B)\) ausrechnen. Hier: A = {1, 2, 3, 4} enthält genau die Hälfte gerader Zahlen (2 und 4), genau wie Ω. Wissen „gerade“ ändert also nichts an A → unabhängig. Bei C = {1, 5, 9} ist das nicht so.",
"Satz der totalen Wahrscheinlichkeit (mit fehlendem Anteil)": r"Idee: Die Verspätungen entstehen auf drei getrennten Wegen (Fahrer 1, 2, 3). Jeder Weg trägt „Anteil des Fahrers × seine Verspätungsquote“ bei, und die Beiträge werden addiert. Das ist ein <b>gewichteter Durchschnitt</b> der drei Quoten. Deshalb muss \(P(V)\) immer zwischen der kleinsten (0.05) und der größten (0.2) Quote liegen – ein guter Kontrollcheck.",
"Satz von Bayes: Rückschluss auf die Ursache": r"Bayes beantwortet die Frage „<b>Woher</b> kommt es?“, wenn man das Ergebnis schon gesehen hat. Im Baum: Von allen Pfaden, die bei „verspätet“ enden (0.05 + 0.06 + 0.01 = 0.12), stammt der Pfad über Fahrer 2 mit 0.06. Sein Anteil ist 0.06/0.12 = 0.5. Bayes ist nichts anderes als „mein Pfad durch alle passenden Pfade“.",
"Bayes im Probeklausur-Format (Lernstrategien)": r"Hier ist der Baum <b>umgekehrt</b> aufgebaut: 1. Stufe bestanden / nicht bestanden, 2. Stufe Strategie. Male ihn so, wie die Angaben es nahelegen. „Unter den Bestehenden …“ beschreibt die Äste <i>nach</i> B. Für \(P(S_3)\) addierst du die beiden Pfade, die bei \(S_3\) enden. Für \(P(B|S_2)\) nimmst du den Pfad B → \(S_2\) geteilt durch beide Pfade zu \(S_2\). Teil (c) ist ein eigener kleiner Baustein: „mindestens einer“ immer über „keiner“.",
"Medizinischer Test: Sensitivität, Spezifität, Prävalenz": r"Warum ist \(P(K|T)\) so klein, obwohl der Test „95 % gut“ ist? Weil es so viele Gesunde gibt. 10 % von sehr vielen Gesunden (980 falsch Positive) sind mehr als 95 % von wenigen Kranken (190 richtig Positive). Rechne bei solchen Aufgaben im Kopf mit 10 000 Personen. Das macht Bayes sichtbar und ist eine perfekte Kontrolle.",
"Ziehen ohne Zurücklegen (Kugeln)": r"Bei mehreren Zügen nacheinander gilt der Produktsatz: \(P(1.\text{ Zug}\cap2.\text{ Zug})=P(1.)\cdot P(2.\,|\,1.)\). Das „|“ bedeutet: Beim zweiten Zug ist die Kiste schon verändert (eine gelbe fehlt, nur noch 19 Kugeln). Mit Zurücklegen wäre die Kiste wieder wie am Anfang – dann sind die Züge unabhängig.",
"„Mindestens einer“ über das Gegenereignis": r"„Mindestens einer“ umfasst 1, 2, 3, … bis 12 Ausfälle – zwölf Fälle einzeln ausrechnen wäre mühsam. Das Gegenteil „kein einziger fällt aus“ ist ein einziger Fall: Alle 12 halten, je mit 0.95, unabhängig → \(0.95^{12}\). Dann 1 minus das Ergebnis. Merksatz: <b>„mindestens einer“ = 1 − „keiner“</b>.",
"Fehlinterpretation: P(A|B) mit P(B|A) verwechselt": r"„Die Hälfte der Infizierten ist geimpft“ ist \(P(G|I)\). Das Risiko eines Geimpften ist aber \(P(I|G)\) – eine ganz andere Bezugsgruppe. Weil 80 % geimpft sind, stellen Geimpfte selbst bei guter Schutzwirkung viele Infizierte. Erst der Vergleich \(P(I|G)\) mit \(P(I|\bar G)\) zeigt die Schutzwirkung.",
})

# ======================================================================
LERN["2"] = r"""
<p><b>Zufallsvariable = eine Zahl, die vom Zufall abhängt.</b> Beispiel: X = Augenzahl, X = Gewinn in €, X = Wartezeit in Minuten. Wir wollen wissen: Welche Werte kann X annehmen, und wie wahrscheinlich ist welcher?</p>
<p><b>Diskret</b> (zählbar, z. B. 0, 1, 2, …): Man gibt eine Tabelle der Wahrscheinlichkeiten an – die <b>Wahrscheinlichkeitsfunktion</b>. Alle Werte ≥ 0 und zusammen genau 1.<br>
<b>Stetig</b> (messbar, z. B. 2.371 Minuten): Ein einzelner Wert hat Wahrscheinlichkeit 0. Man beschreibt X mit einer <b>Dichte</b> f(x). Wahrscheinlichkeit = <b>Fläche unter f</b>. Stell dir 1 kg Sand vor, der über die x-Achse verteilt ist: Wo viel Sand liegt, ist die Dichte hoch. Die Sandmenge über [a, b] ist \(P(a\le X\le b)\).</p>
<p><b>Verteilungsfunktion</b> \(F(x)=P(X\le x)\) = „alles bis x aufgesammelt“. Sie steigt von 0 auf 1. Diskret ist sie eine Treppe (Sprung = Wahrscheinlichkeit), stetig eine glatte Kurve (Integral der Dichte).</p>
<p><b>Erwartungswert E(X)</b> = Durchschnitt auf lange Sicht = Schwerpunkt. Würfel: \(\frac{1+2+\dots+6}{6}=3.5\) – obwohl man nie 3.5 würfelt. Rechnung: jeden Wert mal seine Wahrscheinlichkeit, alles addieren (stetig: integrieren).<br>
<b>Varianz Var(X)</b> = durchschnittliche quadrierte Abweichung vom Erwartungswert = Maß für Streuung/Risiko. In der Praxis rechnest du mit dem <b>Verschiebungssatz</b> \(Var(X)=E(X^2)-E(X)^2\).</p>
<p><b>Rechenregeln, anschaulich:</b> Verschiebst du X um b (+5 €), verschiebt sich E(X) mit, die Streuung bleibt. Streckst du X mit a (Euro → Cent, a = 100), wird E mit a, die Varianz aber mit \(a^2\) multipliziert, denn die Varianz hat quadrierte Einheiten.</p>
<div class="vorgemacht"><b>Vorgemacht:</b> \(P(X=0)=0.2\), \(P(X=1)=0.5\), \(P(X=2)=0.3\).
<ol><li>Kontrolle: 0.2 + 0.5 + 0.3 = 1 ✓</li>
<li>\(E(X)=0\cdot0.2+1\cdot0.5+2\cdot0.3=1.1\)</li>
<li>\(E(X^2)=0^2\cdot0.2+1^2\cdot0.5+2^2\cdot0.3=1.7\) (nur x wird quadriert!)</li>
<li>\(Var(X)=1.7-1.1^2=0.49\), \(sd(X)=0.7\)</li></ol></div>
<div class="vorgemacht"><b>Integral-Auffrischung:</b> \(\int x^n\,dx=\frac{x^{n+1}}{n+1}\) · \(\int c\,dx=cx\) · \(\int_a^b g(x)\,dx=G(b)-G(a)\).
Beispiel: \(\int_0^2 3x^2\,dx=[x^3]_0^2=8-0=8\). Klammern setzen, wenn G(a) negativ ist!</div>
<p><b>Typische Denkfehler:</b> ① Bei \(E(X^2)\) die Wahrscheinlichkeiten quadrieren. ② \(Var(aX)=a\,Var(X)\) statt \(a^2\). ③ Diskret \(P(X<2)\) wie \(P(X\le2)\) behandeln.</p>"""

CHECK["2"] = [
    (r"X nimmt 1 und 3 jeweils mit Wahrscheinlichkeit 0.5 an. Berechne E(X) und Var(X).", r"\(E(X)=2\); \(E(X^2)=0.5+4.5=5\); \(Var(X)=5-4=1\)"),
    (r"\(f(x)=c\) auf [0, 4], sonst 0. Bestimme c und \(P(X\le1)\).", r"\(4c=1\Rightarrow c=0.25\); \(P(X\le1)=0.25\)"),
    (r"\(E(X)=2\), \(Var(X)=3\). Berechne \(E(5-2X)\) und \(Var(5-2X)\).", r"\(E=5-4=1\); \(Var=(-2)^2\cdot3=12\)"),
]

VERST.update({
"Wahrscheinlichkeitsfunktion und Träger aufstellen": r"Gehe vom Zufallsexperiment aus: Würfel zeigt 1…6, jede Zahl mit 1/6. Jetzt übersetzt du jedes Ergebnis in den Gewinn: 1 → −1 €, 2 → 0 €, …, 6 → 4 €. Die Wahrscheinlichkeiten wandern einfach mit. Der Träger ist die Liste der möglichen Gewinne. \(E(X)\) kannst du direkt summieren (\(\frac{-1+0+1+2+3+4}{6}=1.5\)) oder mit der Regel E(Augenzahl − 2) = 3.5 − 2.",
"Konstante c bestimmen, dann E(X) und Var(X)": r"Warum muss die Summe 1 sein? Weil X <i>sicher</i> irgendeinen Wert annimmt – die Wahrscheinlichkeiten aller Werte zusammen sind 100 %. Das liefert eine Gleichung für c. Danach ist es eine normale Tabelle: \(P(X=1)=\frac1{14}\), \(P(X=2)=\frac4{14}\), \(P(X=3)=\frac9{14}\). Mit Brüchen bleibt alles exakt; erst am Ende in eine Dezimalzahl umrechnen.",
"Erwartungswert und Varianz aus einer Tabelle": r"Lege eine Tabelle an mit den Spalten x, P(X = x), x·P und x²·P. Die Summe der dritten Spalte ist E(X), die der vierten E(X²). Das ist übersichtlich, und die Korrektoren sehen deinen Weg. Varianz = (Summe Spalte 4) − (Summe Spalte 3)².",
"Wahrscheinlichkeiten mit der Verteilungsfunktion (diskret)": r"F(x) addiert alle Wahrscheinlichkeiten <b>bis einschließlich x</b>. Bei einer diskreten ZV springt F nur an den Trägerpunkten. Zwischen 2 und 4 passiert nichts, deshalb ist F(3) = F(2) = 0.8 und \(P(X=3)=0\). Übersetze jede Frage in „≤“: „&lt; 2“ = „≤ 1“, „≥ 2“ = 1 − „≤ 1“.",
"Verteilungsfunktion lesen und E(g(X)) berechnen": r"Die Sprunghöhen der Treppe sind die Einzelwahrscheinlichkeiten. Sprung bei 1: 0.3, bei 2: 0.5, Rest bei 3: 0.2. Für \(E(\log X)\) setzt du nicht den Erwartungswert in log ein, sondern rechnest <b>für jeden Wert</b> \(\log(x)\cdot P(X=x)\) und addierst. Warum ist das anders? Weil log keine Gerade ist – nur bei linearen Funktionen darf man E „durchreichen“.",
"Stetige Dichte: c bestimmen und prüfen": r"Gleiche Idee wie im diskreten Fall, nur mit Fläche statt Summe: Die gesamte Fläche unter f muss 1 sein. f ist nur auf [2, 3] ungleich 0, also integrierst du nur dort. Die Fläche eines Dreiecks (Breite 1, Höhe c) ist c/2 – das ist eine schöne Kontrolle ohne Integral: c/2 = 1 → c = 2.",
"Stetige Zufallsvariable: E(X) und Var(X) per Integral": r"Im stetigen Fall wird aus der Summe ein Integral: \(\sum x\,P(X=x)\) → \(\int x\,f(x)\,dx\). Rechenweg ausführlich: \(x\cdot2(x-2)=2x^2-4x\) → Stammfunktion \(\frac23x^3-2x^2\) → bei 3: \(18-18=0\); bei 2: \(\frac{16}3-8=-\frac83\) → \(0-(-\frac83)=\frac83\). Für \(E(X^2)\) genauso mit \(x^2\cdot f(x)\).",
"Verteilungsfunktion herleiten, Wahrscheinlichkeiten, Median": r"F(x) ist die Fläche von ganz links bis x. Links von 2 liegt nichts (F = 0), rechts von 3 ist alles erfasst (F = 1). Dazwischen integrierst du von 2 bis x: \(\int_2^x2(t-2)\,dt=[(t-2)^2]_2^x=(x-2)^2\). Wir nennen die Integrationsvariable t, weil x schon die Obergrenze ist. Den Median findest du, indem du rückwärts fragst: Bei welchem x ist die Hälfte erfasst?",
"Stückweise definierte Dichte: Erwartungswert": r"Wenn die Dichte aus zwei Formeln besteht, zerlegst du das Integral an der Knickstelle (hier y = 2) und rechnest jedes Stück mit seiner eigenen Formel. Am Ende addierst du. Erst die Gesamtfläche prüfen (soll 1 sein): So merkst du sofort, ob du die Aufgabe richtig gelesen hast.",
"Rechenregeln: lineare Transformation und Summen": r"Erwartungswert: „Alles, was linear ist, darf rein und raus“ – Faktoren und Summen ziehst du einfach durch. Varianz: Konstanten verschieben nur, sie streuen nicht → +5 fällt weg. Ein Faktor streckt die Abweichungen, und weil sie quadriert werden, kommt der Faktor <b>im Quadrat</b> heraus. Darum wird auch −2 zu +4: Streuung kann nie negativ werden.",
"Rückwärts rechnen mit den Rechenregeln (Tutorium-Typ)": r"Schreibe die Regel als Gleichung mit einer Unbekannten hin: \(8.5=0.5\cdot3+E(Y)\) und löse nach E(Y) auf. Für die Varianz brauchst du Unabhängigkeit, damit der Kovarianzterm wegfällt. Ist eine Kovarianz gegeben, kommt \(2\cdot a\cdot b\cdot Cov\) dazu (hier \(2\cdot0.5\cdot1\cdot0.4\)).",
"Gemeinsame Wahrscheinlichkeitsfunktion: Rand und bedingte Verteilung": r"Die Tabelle ist eine Kontingenztafel mit Wahrscheinlichkeiten statt Häufigkeiten – genau wie an Tag 1. Rand = Summen am Rand. Bedingt = „eine Zeile bzw. Spalte herausgreifen und neu auf 1 skalieren“. Für Unabhängigkeit müsste die Tabelle aus den Rändern „multipliziert“ entstehen; ein einziges abweichendes Feld widerlegt das.",
"Kovarianz und Korrelation zweier Zufallsvariablen": r"Die Kovarianz misst, ob große X-Werte eher mit großen Y-Werten zusammen auftreten. \(E(XY)\) ist der „gemeinsame Durchschnitt“ und \(E(X)E(Y)\) der Wert, den man bei Unabhängigkeit erwarten würde. Die Differenz zeigt den Zusammenhang. Die Korrelation teilt durch beide Standardabweichungen und liegt daher zwischen −1 und 1 – wie r an Tag 1.",
"Gemeinsame Dichte: Randdichten und Unabhängigkeit": r"Randdichte = „die andere Variable wegintegrieren“, so wie man beim Rand einer Tabelle über die andere Richtung summiert. Für \(f_X(x)\) integrierst du über y (x bleibt als Zahl stehen). Lässt sich f(x, y) als Produkt einer reinen x-Funktion und einer reinen y-Funktion schreiben, sind X und Y unabhängig.",
"Erwarteter Gewinn und fairer Einsatz": r"Fair heißt: Auf lange Sicht gewinnt keiner – erwarteter Nettogewinn 0. Rechne zuerst die erwartete <b>Auszahlung</b> aus (0.1 · 10 + 0.2 · 3 = 1.6). Das ist der faire Preis. Der Lospreis von 2 € liegt darüber, deshalb verliert man im Schnitt 0.40 € pro Los.",
})

# ======================================================================
LERN["3"] = r"""
<p><b>Verteilungen sind fertige Modelle.</b> Statt jedes Mal eine Tabelle aufzustellen, erkennst du die Situation und nimmst die passende Formel. Frage dich der Reihe nach:</p>
<ol><li><b>Wird gezählt?</b> Gibt es eine feste Anzahl n Versuche mit ja/nein? → <b>Binomial</b> (bei n = 1: Bernoulli). Keine Obergrenze, „pro Stunde / pro Tag“? → <b>Poisson</b>.</li>
<li><b>Wird eine Zeit / Dauer gemessen?</b> → <b>Exponential</b>.</li>
<li><b>Messwert um einen Mittelwert, symmetrisch?</b> → <b>Normal</b>. „Gleich wahrscheinlich zwischen a und b“ → <b>Gleichverteilung</b>.</li></ol>
<p><b>Binomialformel verstehen:</b> \(P(X=x)=\binom nx\pi^x(1-\pi)^{n-x}\). Beispiel n = 3 Würfe, π = 0.5, genau 2 Treffer: Mögliche Reihenfolgen TTN, TNT, NTT – das sind \(\binom32=3\). Jede Reihenfolge hat Wahrscheinlichkeit \(0.5^2\cdot0.5^1=0.125\). Zusammen \(3\cdot0.125=0.375\). Der Binomialkoeffizient zählt also die Reihenfolgen, der Rest ist die Wahrscheinlichkeit einer Reihenfolge.</p>
<p><b>Poisson:</b> λ = durchschnittliche Anzahl im Zeitraum. Erwartungswert und Varianz sind beide λ. <b>Exponential:</b> Zeit bis zum nächsten Ereignis. Bei Rate λ ist die mittlere Wartezeit 1/λ.</p>
<p><b>Normalverteilung:</b> Glockenkurve um μ, Breite σ. Faustregel: ca. 68 % liegen in μ ± σ, 95 % in μ ± 2σ. Es gibt keine Formel für F. Man <b>standardisiert</b> – misst also „wie viele Standardabweichungen über μ“: \(z=\frac{x-\mu}\sigma\). Dann liest man \(\Phi(z)\) aus der Tabelle (Anhang).</p>
<div class="vorgemacht"><b>Vorgemacht (Normalverteilung mit Tabelle):</b> \(X\sim N(100,\,25)\), gesucht \(P(X>92)\).
<ol><li>\(\sigma=\sqrt{25}=5\).</li><li>\(z=\frac{92-100}{5}=-1.6\).</li><li>\(P(X>92)=1-\Phi(-1.6)=1-(1-\Phi(1.6))=\Phi(1.6)=0.9452\).</li>
<li>Plausibel? 92 liegt unter dem Mittel, also ist „größer als 92“ mehr als die Hälfte ✓</li></ol></div>
<p><b>ZGWS in einem Satz:</b> Mittelwerte vieler unabhängiger Beobachtungen sind annähernd normalverteilt – egal wie die einzelnen Werte verteilt sind. Die Streuung des Mittelwerts schrumpft mit \(\sigma/\sqrt n\).</p>
<p><b>Typische Denkfehler:</b> ① In \(N(\mu,\sigma^2)\) steht die Varianz, in R die Standardabweichung. ② Bei Exponential λ = Mittelwert setzen (richtig: λ = 1/Mittelwert). ③ Diskret „mehr als 4“ = „≥ 4“ rechnen (richtig: ≥ 5).</p>"""

CHECK["3"] = [
    (r"\(X\sim B(4;\,0.5)\). Berechne \(P(X=2)\).", r"\(\binom42\cdot0.5^4=6\cdot\frac1{16}=0.375\)"),
    (r"\(X\sim Po(2)\). Berechne \(P(X=0)\).", r"\(e^{-2}=0.135\)"),
    (r"\(X\sim N(100,\,25)\). Berechne \(P(X\le110)\) mit der Tabelle.", r"\(z=\frac{110-100}5=2\Rightarrow\Phi(2)=0.977\)"),
    (r"Die mittlere Wartezeit ist 5 Minuten (exponentialverteilt). Wie groß ist λ?", r"\(\lambda=\frac15=0.2\)"),
]

VERST.update({
"Welche Verteilung passt? (Erkennen + Parameter)": r"Gehe die Frage-Kette aus dem Lernteil durch: zählen oder messen? Feste Versuchszahl oder offene Anzahl pro Zeitraum? Die Parameter stehen fast immer im Text: n und π bei Binomial, „im Mittel 4“ = λ bei Poisson, „Mittel 500, sd 3“ bei Normal (Varianz 9 schreiben!).",
"Bernoulliverteilung": r"Bernoulli ist der kleinste Baustein: ein Versuch, Erfolg (1) oder Misserfolg (0). E(X) = π, denn \(1\cdot\pi+0\cdot(1-\pi)\). Die eigentliche Arbeit ist hier nur, π durch Abzählen zu finden.",
"Binomialverteilung per Hand": r"Rechne jeden Summanden einzeln und schreibe ihn hin. Beispiel \(P(Y=1)\): Es gibt 8 Positionen für den einen Treffer, jede hat \(\frac13\cdot(\frac23)^7\). \(P(Y\le2)\) heißt „0 oder 1 oder 2 Treffer“ – drei disjunkte Fälle, also addieren. E und Var gibt es geschenkt: nπ und nπ(1−π).",
"Binomial: „mindestens“, „mehr als“, „zwischen“ umschreiben": r"Zeichne einen Zahlenstrahl 0, 1, 2, …, 10 und markiere die gewünschten Werte. pbinom(k) deckt immer alles von 0 bis k ab. „Mehr als 5“ = 6 bis 10 = alles minus (0 bis 5). „Zwischen 2 und 6 (ohne Ränder)“ = 3, 4, 5 = (0 bis 5) minus (0 bis 2). So vermeidest du Grenzfehler.",
"Poissonverteilung per Hand": r"Formel \(\frac{\lambda^x}{x!}e^{-\lambda}\): Für x = 0 ist \(\lambda^0=1\) und \(0!=1\), es bleibt \(e^{-\lambda}\). Für „mindestens 2“ nimmst du wieder das Gegenteil (0 oder 1). Verdoppelt sich der Zeitraum, verdoppelt sich die mittlere Anzahl – also λ = 5 für zwei Minuten.",
"Ist die transformierte Variable noch poissonverteilt?": r"Die Poissonverteilung hat eine „Signatur“: E = Var. Nach der Transformation sind E(Z) = 10 und Var(Z) = 12 verschieden – also kann Z keine Poissonverteilung sein. Außerdem nimmt Z nur die Werte 4, 6, 8, … an, eine Poisson-ZV dagegen alle Werte 0, 1, 2, …",
"Gleichverteilung U(a, b)": r"Die Dichte ist ein Rechteck der Breite b − a. Damit die Fläche 1 ist, muss die Höhe \(\frac1{b-a}\) sein. Jede Wahrscheinlichkeit ist dann einfach „Teilbreite durch Gesamtbreite“: \(P(X>7)=\frac{10-7}{8}\). Der Erwartungswert liegt in der Mitte.",
"Exponentialverteilung: λ aus dem Mittelwert": r"\(P(X>x)=e^{-\lambda x}\) bekommst du direkt aus F: \(1-(1-e^{-\lambda x})\). Diese „Überlebensformel“ ist bei Wartezeiten die praktischste. Tipp: Stimmt das Ergebnis grob? Bei Mittel 3 Stunden ist „länger als 10 Stunden“ selten → kleine Zahl ✓",
"Normalverteilung: standardisieren": r"Standardisieren übersetzt jede Normalverteilung in die eine Tabelle von N(0, 1). z = 1.667 heißt: 505 liegt 1.667 Standardabweichungen über dem Mittel. Für Bereiche: \(P(a\le X\le b)=\Phi(z_b)-\Phi(z_a)\). Bei negativem z benutzt du die Symmetrie \(\Phi(-z)=1-\Phi(z)\), denn die Tabelle hat nur positive z.",
"Normalverteilung: Quantile und „um mehr als 2σ“": r"Ein Quantil ist die Rückwärtsfrage: Nicht „wie wahrscheinlich ist x?“, sondern „welches x hat 95 % unter sich?“. In der Tabelle suchst du also 0.95 im Inneren (→ z ≈ 1.645) und rechnest dann zurück: x = μ + σz. Das Gegenstück zum Standardisieren.",
"Summen und lineare Transformation normalverteilter ZV": r"Bei Summen <b>unabhängiger</b> Größen addieren sich die Varianzen, nicht die Standardabweichungen. Darum ist die sd des Kartons \(\sqrt{90}=9.49\) und nicht 10 · 3 = 30. Einzelne Schwankungen gleichen sich teilweise aus. 10X (dieselbe Packung zehnmal) hätte dagegen sd 30.",
"Zentraler Grenzwertsatz: Verteilung des Mittelwerts": r"Ein Mittelwert schwankt viel weniger als einzelne Werte: Die Standardabweichung des Mittelwerts ist \(\frac{\sigma}{\sqrt n}=\frac4{8}=0.5\). Deshalb ist ein Mittelwert von 13 (nur eine Minute über μ) schon ungewöhnlich: z = 2. Der ZGWS erlaubt die Normalverteilung, auch wenn die Einzelzeiten nicht normal sind.",
"Bivariate Normalverteilung: Rand und bedingte Verteilung": r"Kennt man X, kann man Y besser vorhersagen: Der bedingte Erwartungswert verschiebt sich in Richtung des Zusammenhangs (ρ > 0 → größer), und die Unsicherheit schrumpft um den Faktor \(1-\rho^2\). Für die Wahrscheinlichkeit standardisierst du dann mit dem <b>bedingten</b> μ und σ.",
"Ziehen ohne Zurücklegen: Lotto-Formel": r"Zähle Möglichkeiten: Auf wie viele Arten kann man 2 der 4 roten wählen (6) und 1 der 6 anderen (6)? Das sind 36 günstige Kombinationen von insgesamt \(\binom{10}3=120\). Laplace: günstige durch mögliche.",
})

# ======================================================================
LERN["4"] = r"""
<p><b>Ein Schätzer ist ein Rezept</b>, das aus den Daten eine Zahl macht, z. B. \(\bar X\) für μ. Weil die Daten zufällig sind, ist auch das Ergebnis zufällig: Mit einer neuen Stichprobe kommt eine andere Zahl heraus.</p>
<p><b>Zielscheiben-Bild:</b> Der wahre Parameter ist die Mitte der Scheibe, jede Stichprobe ein Schuss.
<b>Bias</b> = Schüsse liegen <i>systematisch</i> daneben (Visier verstellt). <b>Varianz</b> = Schüsse streuen weit (zittrige Hand). <b>MSE</b> = mittlerer quadrierter Abstand zur Mitte = Bias² + Varianz. <b>Konsistent</b> = mit mehr Daten landen die Schüsse immer näher an der Mitte.</p>
<div class="vorgemacht"><b>Vorgemacht – Erwartungstreue prüfen:</b> \(\hat\mu=\frac{X_1+2X_2}{3}\), \(E(X_i)=\mu\).
<ol><li>E auf den ganzen Schätzer: \(E(\hat\mu)=E\left(\frac{X_1+2X_2}3\right)\).</li>
<li>Linearität: \(=\frac13\left(E(X_1)+2E(X_2)\right)\).</li><li>Einsetzen: \(=\frac13(\mu+2\mu)=\mu\).</li>
<li>Satz: „\(E(\hat\mu)=\mu\), also ist \(\hat\mu\) erwartungstreu.“ Varianz (iid): \(\frac19(\sigma^2+4\sigma^2)=\frac59\sigma^2\).</li></ol></div>
<p><b>Dichteschätzung:</b> Ein Histogramm schätzt die Dichte mit Treppenstufen. Ein <b>Kerndichteschätzer</b> setzt auf jeden Datenpunkt einen kleinen „Hügel“ (den Kern) und addiert alle Hügel. Die Bandweite b ist die Breite der Hügel: schmal → zackig, breit → glatt.</p>
<p><b>Typische Denkfehler:</b> ① Bei \(Var\) den Faktor \(\frac1n\) nicht quadrieren. ② Die Anzahl der Summanden falsch zählen (Summe ab i = 2 hat n − 1 Glieder). ③ „Erwartungstreu = immer besser“ – der MSE entscheidet.</p>"""

CHECK["4"] = [
    (r"Ist \(\hat\theta=\frac{X_1+X_2+X_3}3\) erwartungstreu für \(\mu=E(X_i)\)?", r"\(E(\hat\theta)=\frac{3\mu}3=\mu\) → ja"),
    (r"Bias von \(\hat\mu=X_1+X_2\) für μ?", r"\(E=2\mu\Rightarrow Bias=\mu\)"),
    (r"Ein Schätzer hat Bias 2 und Varianz 1. MSE?", r"\(2^2+1=5\)"),
]

VERST.update({
"Erwartungstreue prüfen und Bias berechnen": r"Der Trick ist immer gleich: Erwartungswert und Summe dürfen vertauscht werden, Konstanten wandern nach vorne. \(E\left(\frac2n\sum X_i\right)=\frac2n\sum E(X_i)=\frac2n\cdot n\mu\). Dann vergleichst du mit dem Ziel μ. Der Schätzer \(\frac{X_1+X_n}2\) ist unverzerrt, nutzt aber nur 2 Werte – er ist erwartungstreu, aber nicht gut (große Varianz).",
"Schätzer mit Teilsummen (Testat-Typ) und Multiple Choice": r"Zähle die Summanden: \(\sum_{i=2}^n\) läuft von 2 bis n, das sind n − 1 Stück. Jeder hat Erwartungswert κ/2. Danach Bruchrechnung: Alles auf den Nenner 4n bringen. Für die Multiple Choice: (4) ist falsch, weil ein verzerrter Schätzer mit sehr kleiner Varianz einen kleineren MSE haben kann (siehe MSE-Vergleich).",
"Varianz, MSE und Konsistenz von Schätzern": r"Warum ist \(\bar X\) konsistent? Mit jeder weiteren Beobachtung mittelt sich der Zufall stärker heraus: Var = θ²/n → 0. Der Schätzer aus nur zwei Werten ignoriert alle weiteren Daten, seine Varianz bleibt θ²/2 – egal wie groß n ist. Konsistenz heißt: mehr Daten machen den Schätzer besser.",
"Verzerrter Schätzer mit Varianzberechnung (Tutorium 9)": r"Zwei Bausteine: (1) Varianz einer einzelnen Beobachtung aus \(E(X^2)-E(X)^2\), dabei die Brüche auf den Nenner γ² bringen. (2) Varianz des Mittelwerts = Einzelvarianz / n. Der Schätzer ist verzerrt, weil er 1/γ schätzt statt γ.",
"Produkte im Schätzer kürzen (Probeklausur 2022, Aufgabe 7)": r"Die Aufgabe sieht schlimm aus, ist aber ein Kürzungstrick: Im Zähler stehen \(X_2\) bis \(X_{n-1}\), im Nenner \(X_1\) bis \(X_{n-1}\). Alles außer \(X_1\) kürzt sich weg. Danach bleiben drei einfache Terme. Lerne: Erst vereinfachen, dann den Erwartungswert bilden.",
"MSE-Vergleich mit Zahlen": r"Zielscheibe: A trifft im Mittel genau, streut aber stark (Varianz 4). B liegt etwas daneben (Bias 1), streut aber wenig (Varianz 2). Der mittlere quadrierte Abstand zur Mitte ist bei B kleiner (3 < 4).",
"Gütekriterien von ML-Schätzern und Fehlerarten": r"Merke die drei Eigenschaften als „aKa“: <b>a</b>symptotisch erwartungstreu, <b>K</b>onsistent, <b>a</b>symptotisch normalverteilt. Beim Histogramm: Mehr Klassen bilden die wahre Form genauer nach (kleiner Approximationsfehler). Dafür fallen pro Klasse weniger Daten an, und die Höhen schwanken stärker (großer Schätzfehler).",
"Kerndichteschätzer per Hand an einer Stelle": r"Stell dir vor: An x = 3 fragst du jeden Datenpunkt „Wie nah bist du?“. u = Abstand in Bandweiten. Punkte weiter als eine Bandweite entfernt tragen nichts bei (K = 0). Nahe Punkte tragen viel bei – beim Epanechnikov-Kern umso mehr, je näher sie sind. Am Ende teilst du durch n · b, damit die Gesamtfläche 1 ist.",
})

# ======================================================================
LERN["5"] = r"""
<p><b>Die Idee:</b> Wir haben Daten und ein Modell mit unbekanntem Parameter (z. B. λ). Wir probieren gedanklich alle λ durch und fragen: <b>Unter welchem λ wären genau diese Daten am wahrscheinlichsten?</b> Dieses λ ist der ML-Schätzer. Beispiel Münze: 6-mal Wappen in 20 Würfen passt am besten zu P(Wappen) = 0.3.</p>
<p><b>Warum der Logarithmus?</b> Die Likelihood ist ein langes Produkt. Ableiten von Produkten ist mühsam. Der Logarithmus macht aus dem Produkt eine Summe, und Summen leitet man Glied für Glied ab. Weil log immer steigt, liegt das Maximum an derselben Stelle.</p>
<div class="vorgemacht"><b>Vorgemacht – Poisson, jede Zeile erklärt:</b>
<ol><li>Likelihood: \(L(\lambda)=\prod_{i=1}^n\frac{\lambda^{x_i}}{x_i!}e^{-\lambda}\) (eine Wahrscheinlichkeit pro Beobachtung, alle multipliziert).</li>
<li>Logarithmus mit \(\log(a\cdot b)=\log a+\log b\): \(\ell(\lambda)=\sum\left(x_i\log\lambda-\log(x_i!)-\lambda\right)\).</li>
<li>Summe aufteilen: \(\ell(\lambda)=\log\lambda\sum x_i-\sum\log(x_i!)-n\lambda\) (\(\sum\lambda=n\lambda\)).</li>
<li>Ableiten nach λ: \(\frac{1}{\lambda}\sum x_i-0-n\) (der mittlere Term enthält kein λ → fällt weg).</li>
<li>Null setzen: \(\frac{\sum x_i}{\hat\lambda}=n\Rightarrow\hat\lambda=\frac{\sum x_i}n=\bar x\).</li>
<li>Kontrolle 2. Ableitung: \(-\frac{\sum x_i}{\lambda^2}<0\) → Maximum ✓</li></ol></div>
<p><b>Ableitungen, die du brauchst:</b> \(\frac{d}{d\vartheta}\log\vartheta=\frac1\vartheta\) · \(\frac{d}{d\vartheta}\log(1-\vartheta)=-\frac1{1-\vartheta}\) · \(\frac{d}{d\vartheta}(c\cdot\vartheta)=c\) · Konstanten → 0. Beim Auflösen: Brüche „über Kreuz“ multiplizieren, dann ϑ ausklammern.</p>
<p><b>Punkte-Strategie:</b> Auch wenn das Auflösen hakt, bringen Likelihood (aufgestellt), Log-Likelihood (vereinfacht) und Ableitung = 0 schon den Großteil der Punkte.</p>
<p><b>Typische Denkfehler:</b> ① \(\log(a+b)=\log a+\log b\) (falsch!). ② \(\prod c=c\) statt \(c^n\). ③ Nach der falschen Größe ableiten (σ statt σ²).</p>"""

CHECK["5"] = [
    (r"\(\ell(\lambda)=5\log\lambda-2\lambda\). Bestimme \(\hat\lambda\).", r"\(\frac5\lambda-2=0\Rightarrow\hat\lambda=2.5\)"),
    (r"\(L(p)=p^3(1-p)^7\). Bestimme \(\hat p\).", r"\(\frac3p-\frac7{1-p}=0\Rightarrow\hat p=0.3\)"),
    (r"Exponentialverteilung, Daten 1 und 3. \(\hat\lambda\)?", r"\(\bar x=2\Rightarrow\hat\lambda=0.5\)"),
]

VERST.update({
"Likelihood für eine konkrete Stichprobe (geometrische Verteilung)": r"Konkrete Zahlen machen es einfach: Jede Beobachtung liefert einen Faktor \((1-p)^{x}p\). Beim Multiplizieren addieren sich die Exponenten. p taucht viermal auf (vier Beobachtungen), \((1-p)\) mit der Summe der Werte als Exponent. Die Ableitung von \(10\log(1-p)\) ist \(-\frac{10}{1-p}\) (Kettenregel: innere Ableitung −1).",
"ML allgemein: Poissonverteilung mit 2. Ableitung": r"Das ist das Muster-Beispiel aus dem Lernteil. Wichtig für die Punkte: zeigen, dass \(\sum\log(x_i!)\) nicht von λ abhängt (fällt beim Ableiten weg), und die zweite Ableitung mit Vorzeichen-Begründung angeben („negativ, da alle \(x_i\ge0\) und λ > 0“).",
"ML: Exponentialverteilung (auch Weibull mit r = 1)": r"\(\prod\lambda e^{-\lambda x_i}\): Das λ vor der e-Funktion kommt n-mal vor → \(\lambda^n\). Die Exponenten der e-Funktionen addieren sich → \(e^{-\lambda\sum x_i}\). Logarithmus: \(n\log\lambda-\lambda\sum x_i\). Das Ergebnis \(1/\bar x\) passt zur Intuition: Kurze Wartezeiten bedeuten eine hohe Rate.",
"ML: Bernoulli / Anteilswert": r"Die Bernoulli-Formel \(\pi^{x}(1-\pi)^{1-x}\) ist ein Trick: Für x = 1 bleibt π, für x = 0 bleibt 1 − π. Das Ergebnis „Anteil = Erfolge / Versuche“ ist genau das, was man auch ohne Formel schätzen würde. ML bestätigt die Intuition.",
"ML: allgemeine geometrische Verteilung (Testat 5)": r"Gleicher Ablauf wie bei der konkreten Stichprobe, nur mit \(\sum x_i\) statt einer Zahl. Beim Auflösen: \(n(1-\theta)=\theta\sum x_i\) → ausmultiplizieren → alle θ auf eine Seite → \(\theta(n+\sum x_i)=n\). Durch n kürzen ergibt die schöne Form mit \(\bar x\).",
"ML: Dichte mit Parameter im Exponenten (Übungsklausur ML, Aufgabe 1)": r"Wenn der Parameter im Exponenten steht, hilft \(\log(x^b)=b\log x\): Der Parameter wird zum Faktor vor einer Konstanten. \(\sum\log x_i\) ist nach der Datenerhebung einfach eine Zahl, bei Werten zwischen 0 und 1 negativ. Ableitung von \(n\log(b+1)\) ist \(\frac n{b+1}\) (innere Ableitung 1).",
"ML: Normal- und Log-Normalverteilung, μ (σ bekannt)": r"Teile die Log-Likelihood in „Teil ohne μ“ und „Teil mit μ“. Nur \(-\frac1{2\sigma^2}\sum(\log x_i-\mu)^2\) hängt von μ ab. Beim Ableiten der Klammer im Quadrat: Kettenregel → \(2(\log x_i-\mu)\cdot(-1)\). Ergebnis: μ̂ ist der Mittelwert der logarithmierten Daten – bei der Normalverteilung einfach \(\bar x\).",
"ML: Parameter mit log(2) (Übungsklausur ML, Aufgabe 3)": r"Nicht von log(2) verwirren lassen: Es ist eine Zahl (≈ 0.693) wie jede andere. \(2^{-x\beta}\) logarithmiert ergibt \(-x\beta\log2\). Danach ist die Aufgabe identisch mit der Exponentialverteilung (dort wäre statt \(\log2\) einfach 1).",
"ML aus einer Wahrscheinlichkeitstabelle (quadratische Gleichung)": r"Für jede Beobachtung den passenden Tabellenwert einsetzen: 1 → α, 3 → \(1-\alpha-\alpha^2\), 2 → α², 1 → α. Nach dem Ableiten über Kreuz multiplizieren, alles auf eine Seite → quadratische Gleichung → Mitternachtsformel \(\frac{-b\pm\sqrt{b^2-4ac}}{2a}\). Nur die Lösung im erlaubten Bereich (0 bis 0.618) zählt.",
"ML für die Varianz der Normalverteilung (μ bekannt)": r"Trick: Schreibe v statt σ², damit du nach der richtigen Größe ableitest. \(-\frac1{2v}\) abgeleitet ist \(+\frac1{2v^2}\) (Potenzregel mit \(v^{-1}\)). Nach dem Nullsetzen mit \(2v^2\) multiplizieren und auflösen. Ergebnis: durchschnittliche quadrierte Abweichung von μ.",
"Reihenfolge der ML-Schritte (Testat 5)": r"Denke an den Ablauf beim Kochen: Rezept wählen (Modell) → Zutaten zusammenstellen (Likelihood) → vereinfachen (log) → Herd an (ableiten, = 0) → Ergebnis (auflösen) → probieren (2. Ableitung).",
})

# ======================================================================
LERN["6"] = r"""
<p><b>Warum ein Intervall?</b> Ein Schätzwert wie \(\bar x=52.3\) ist fast nie exakt richtig. Ehrlicher ist: „μ liegt <i>wahrscheinlich</i> zwischen 50.3 und 54.3“. Ein Konfidenzintervall hat immer dieselbe Bauform:</p>
<p style="text-align:center;font-size:1.05rem">\(\text{Schätzer}\ \pm\ \text{Quantil}\times\text{Standardfehler}\)</p>
<ul><li><b>Schätzer:</b> \(\bar x\) (für μ) oder \(\hat\pi\) (für einen Anteil).</li>
<li><b>Quantil:</b> Wie sicher willst du sein? 95 % → links und rechts je 2.5 % abschneiden → Quantil \(1-\alpha/2=0.975\) → z = 1.96. Bei unbekanntem σ benutzt du das etwas größere t-Quantil (df = n − 1), weil das Schätzen von σ zusätzliche Unsicherheit bringt.</li>
<li><b>Standardfehler:</b> Wie stark schwankt der Schätzer? Für \(\bar x\): \(\sigma/\sqrt n\) (bzw. \(s_*/\sqrt n\)); für \(\hat\pi\): \(\sqrt{\hat\pi(1-\hat\pi)/n}\).</li></ul>
<div class="vorgemacht"><b>Vorgemacht:</b> n = 25, \(\bar x=40\), \(s_*=5\), σ unbekannt, 95 %, gegeben \(t_{24;\,0.975}=2.064\).
<ol><li>Welcher Fall? σ unbekannt → t, df = 24.</li><li>Standardfehler: \(5/\sqrt{25}=1\).</li><li>Halbe Breite: \(2.064\cdot1=2.064\).</li>
<li>KI: \([37.936;\ 42.064]\).</li></ol></div>
<p><b>Interpretation:</b> Das Verfahren erwischt bei 95 % aller Stichproben das wahre μ. Für <i>ein</i> berechnetes Intervall sagt man: „Mit 95 % Konfidenz liegt μ zwischen …“ – aber nicht „μ liegt mit 95 % Wahrscheinlichkeit darin“ (μ ist fest).</p>
<p><b>Typische Denkfehler:</b> ① 0.95 statt 0.975 als Quantil bei 95 %. ② df = n statt n − 1. ③ σ² statt σ einsetzen. ④ Beim Varianz-KI die Quantile vertauschen.</p>"""

CHECK["6"] = [
    (r"Welches z-Quantil brauchst du für ein 95 %-KI?", r"\(z_{0.975}=1.96\)"),
    (r"\(\bar x=10\), σ = 2 bekannt, n = 4, 95 %-KI?", r"\(10\pm1.96\cdot\frac22=[8.04;\ 11.96]\)"),
    (r"n = 9, σ unbekannt: Wie viele Freiheitsgrade hat das t-Quantil?", r"df = n − 1 = 8"),
]

VERST.update({
"KI für μ bei bekannter Varianz": r"Bauform: Schätzer 52.3 ± Quantil 1.96 × Standardfehler 4/√16 = 1. Bei 90 % braucht man weniger Sicherheit, also ein kleineres Quantil (1.645) und ein schmaleres Intervall. Kontrolle: Der Schätzer liegt genau in der Mitte des Intervalls.",
"KI für μ bei unbekannter Varianz (t-Quantil aus R-Output)": r"Zwei Entscheidungen, beide vor dem Rechnen: (1) Welche Zeile? σ unbekannt → t mit df = n − 1 = 14. (2) Welche Spalte? 95 % zweiseitig → 0.975. Erst dann den Wert ablesen (2.145). Wer die 15er-Zeile oder die 0.95-Spalte nimmt, verliert die Punkte – die Aufgabe ist genau darauf angelegt.",
"KI für einen Anteilswert": r"Ein Anteil ist ein Mittelwert von 0/1-Werten, daher funktioniert dieselbe Bauform. Die Varianz einer Bernoulli-Variable ist π(1−π). Weil π unbekannt ist, setzen wir \(\hat\pi\) ein. Standardfehler \(\sqrt{0.8\cdot0.2/100}=0.04\), dann ± 1.96 · 0.04.",
"KI für die Varianz (χ²-Quantile aus R-Output)": r"Hier ist die Bauform anders: Man teilt statt ± zu rechnen. Merke: Durch das <b>große</b> Quantil teilen ergibt die <b>kleine</b> Grenze. Kontrolle: \(s_*^2=0.962\) muss im Intervall liegen ✓ (aber nicht in der Mitte, denn die χ²-Verteilung ist schief).",
"Rückwärts: Was steckt in diesem R-Befehl?": r"Lege die Formel \(\bar x\pm z\cdot\frac{\sigma}{\sqrt n}\) neben den R-Befehl und ordne Stück für Stück zu: Die Zahl vor dem ± ist \(\bar x\), qnorm(0.995) ist das Quantil, die 2 ist σ, sqrt(100) ist √n. Das Quantil 0.995 = 1 − α/2 verrät α = 0.01.",
"Konfidenzintervalle richtig interpretieren": r"Eselsbrücke: Das Intervall ist der Fänger, μ ist der Fisch, der stillhält. „95 %“ beschreibt, wie gut der Fänger arbeitet, wenn man ihn oft auswirft. Ein schon ausgeworfener Fänger hat den Fisch – oder nicht. Mehr Daten → kleinerer Standardfehler → schmaleres Netz.",
})

# ======================================================================
LERN["7"] = r"""
<p><b>Gerichts-Analogie:</b> Im Gericht gilt „unschuldig, bis die Schuld bewiesen ist“. <b>H₀ = unschuldig</b> (der langweilige Normalzustand), <b>H₁ = schuldig</b> (das, was man beweisen will). Nur wenn die Beweise (Daten) sehr stark gegen H₀ sprechen, wird verurteilt (H₀ verworfen). Ein Freispruch heißt nicht „bewiesen unschuldig“, sondern nur „nicht genug Beweise“. Genauso ist ein nicht verworfenes H₀ <b>nicht bewiesen</b>.</p>
<ul><li><b>Fehler 1. Art</b> = Unschuldigen verurteilen (H₀ wahr, aber verworfen). Seine Wahrscheinlichkeit ist höchstens α (z. B. 5 %).</li>
<li><b>Fehler 2. Art</b> = Schuldigen freisprechen (H₁ wahr, aber H₀ beibehalten).</li></ul>
<p><b>Teststatistik</b> = „Wie weit sind die Daten von H₀ entfernt, gemessen in Standardfehlern?“ Beispiel Gauß-Test: \(z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}\). Ist z groß (positiv oder negativ), sprechen die Daten gegen H₀.</p>
<p><b>Ablehnungsbereich</b> = die extremsten α % der möglichen Werte unter H₀. Wo sie liegen, sagt H₁: H₁ „&lt;“ → links, „&gt;“ → rechts, „≠“ → auf beiden Seiten je α/2.<br>
<b>p-Wert</b> = „Wie überraschend sind meine Daten, wenn H₀ stimmt?“ Klein (≤ α) → so überraschend, dass wir H₀ nicht mehr glauben.</p>
<div class="vorgemacht"><b>Vorgemacht – das 5-Schritte-Schema:</b> Es soll gezeigt werden, dass die Wartezeit im Mittel über 10 Minuten liegt; σ = 3, n = 36, \(\bar x=11\), α = 5 %.
<ol><li>Hypothesen: \(H_0:\mu\le10\), \(H_1:\mu>10\) (das Gezeigte steht in H₁).</li>
<li>Teststatistik: \(z=\frac{11-10}{3/6}=2\).</li><li>Verteilung unter H₀: N(0, 1).</li>
<li>Ablehnungsbereich rechtsseitig: \([1.645;\infty)\); p-Wert \(=1-\Phi(2)=0.023\).</li>
<li>Entscheidung: 2 ≥ 1.645 (p < 0.05) → H₀ verwerfen. Die mittlere Wartezeit liegt zum Niveau 5 % signifikant über 10 Minuten.</li></ol></div>
<p><b>Typische Denkfehler:</b> ① Die Behauptung, die man zeigen will, in H₀ schreiben. ② „H₀ ist bewiesen“ formulieren. ③ Bei zweiseitigen Tests das Quantil \(1-\alpha\) statt \(1-\alpha/2\) nehmen.</p>"""

CHECK["7"] = [
    (r"„Es soll nachgewiesen werden, dass mehr als 50 % zufrieden sind.“ Hypothesen?", r"\(H_0:\pi\le0.5\), \(H_1:\pi>0.5\)"),
    (r"p = 0.03, α = 0.05. Entscheidung?", r"p ≤ α → H₀ verwerfen"),
    (r"Zweiseitiger Gauß-Test, α = 0.1. Kritischer Wert?", r"\(z_{0.95}=1.645\), verwerfen bei \(|z|\ge1.645\)"),
]

VERST.update({
"Hypothesenpaar aus dem Text aufstellen": r"Suche im Text das Signalwort „absichern / zeigen / nachweisen / belegen“. Der Satzteil dahinter wird H₁, ohne Gleichheitszeichen. H₀ ist das Gegenteil und bekommt das Gleichheitszeichen. Danach prüfen: Steht in H₀ und H₁ derselbe Wert (μ₀)? Ergänzen sich die Zeichen (≤ / > oder ≥ / &lt; oder = / ≠)?",
"Fehler 1. und 2. Art im Sachkontext": r"Übersetze immer in Alltagssprache: „H₀ wird verworfen“ = der Melder schlägt Alarm. Fehler 1. Art = Alarm ohne Feuer, Fehler 2. Art = Feuer ohne Alarm. Mit α stellst du die Empfindlichkeit ein: weniger Fehlalarme, aber öfter einen echten Brand übersehen.",
"Ablehnungsbereiche bestimmen": r"Male dir die Dichte unter H₀ und schneide die extremsten α % ab. Einseitig liegt die ganze Fläche α auf einer Seite (Quantil 1 − α), zweiseitig je α/2 auf beiden Seiten (Quantil 1 − α/2). Bei χ² gibt es keine negativen Werte: Links nimmt man das kleine Quantil \(\chi^2_{\alpha}\).",
"p-Wert berechnen und interpretieren": r"Der p-Wert ist die Fläche „noch extremer als mein Wert“ – in die Richtung, die H₁ angibt. Rechtsseitig: Fläche rechts von z. Linksseitig: Fläche links. Zweiseitig: beide Seiten, also das Doppelte der kleineren Fläche.",
"Testentscheidung zu mehreren Niveaus": r"Ein p-Wert entscheidet für alle α auf einmal: H₀ wird für jedes α ≥ p verworfen. Mit Ablehnungsbereichen musst du für jedes α den kritischen Wert neu bestimmen. Größeres α → größerer Bereich → leichter zu verwerfen.",
"Exakter Binomialtest mit Tabelle": r"Unter H₀ (π = 0.2) erwartet man 2 Nieten von 10. Beobachtet: 5 – ist das noch Zufall? Der p-Wert \(P(Z\ge5)\) sagt: Nur in 3.3 % der Fälle würde man bei π = 0.2 so viele oder mehr Nieten sehen. Das ist seltener als α = 5 % → wir glauben H₀ nicht mehr.",
})

# ======================================================================
LERN["8"] = r"""
<p><b>Alle Tests laufen gleich ab</b> – nur die Teststatistik ändert sich. Du musst also lernen, (1) <b>welcher Test</b> passt und (2) welche <b>Formel und Verteilung</b> dazugehört. Der Rest ist das 5-Schritte-Schema aus Abschnitt 7.</p>
<ul><li>Es geht um einen <b>Mittelwert</b> μ: σ bekannt → <b>Gauß-Test</b> (N(0, 1)); σ unbekannt → <b>t-Test</b> (t(n − 1)).</li>
<li>Es geht um einen <b>Anteil</b> π: großes n → <b>approximativer Binomialtest</b> (N(0, 1)); kleines n → exakt mit der Binomialverteilung.</li>
<li>Es geht um eine <b>Streuung</b> σ²: <b>χ²-Varianztest</b> (χ²(n − 1)).</li>
<li>Es geht um einen <b>Median</b> ohne Verteilungsannahme: <b>Vorzeichentest</b> (B(n; 0.5)).</li>
<li><b>Zwei kategoriale Merkmale</b> (Kreuztabelle): <b>χ²-Unabhängigkeitstest</b>. <b>Vorgegebene Verteilung</b> prüfen: <b>χ²-Anpassungstest</b>.</li></ul>
<div class="vorgemacht"><b>Vorgemacht – t-Test komplett:</b> Daten 12, 15, 9, 14 (normal, σ unbekannt). Zeige μ > 10, α = 5 %; gegeben \(t_{3;\,0.95}=2.353\).
<ol><li>\(H_0:\mu\le10\), \(H_1:\mu>10\).</li>
<li>\(\bar x=12.5\); Abweichungen −0.5, 2.5, −3.5, 1.5 → Quadrate 0.25, 6.25, 12.25, 2.25 → Summe 21 → \(s_*^2=21/3=7\), \(s_*=2.6458\).</li>
<li>\(T=\frac{12.5-10}{2.6458}\sqrt4=1.890\), unter H₀ \(T\sim t(3)\).</li>
<li>Ablehnungsbereich \([2.353;\infty)\).</li><li>1.890 &lt; 2.353 → H₀ nicht verwerfen; μ > 10 ist nicht nachweisbar.</li></ol></div>
<p><b>χ²-Tests anschaulich:</b> Vergleiche „was ich beobachte“ mit „was ich erwarten würde, wenn H₀ stimmt“. Große Abweichungen → großes χ² → H₀ verwerfen. Deshalb sind χ²-Tests auf Unabhängigkeit bzw. Anpassung immer <b>rechtsseitig</b>.</p>"""

CHECK["8"] = [
    (r"Mittelwert testen, σ ist bekannt. Welcher Test?", r"Gauß-Test, Teststatistik N(0, 1)"),
    (r"Varianztest mit n = 15: Verteilung unter H₀?", r"χ²(14)"),
    (r"χ²-Unabhängigkeitstest mit einer 3×4-Tafel: Freiheitsgrade?", r"(3 − 1)(4 − 1) = 6"),
]

VERST.update({
"Gauß-Test (σ bekannt) vollständig": r"Die Teststatistik misst, wie viele Standardfehler \(\bar x\) unter dem behaupteten Wert liegt: 247.6 ist 2.4 ml zu wenig, ein Standardfehler ist 4/3 = 1.33 ml → z = −1.8. Unter H₀ wäre so ein Wert selten (3.6 %). Jeder der fünf Schritte bringt typischerweise einen Punkt.",
"t-Test per Hand (σ unbekannt)": r"Unterschied zum Gauß-Test: σ wird aus den Daten geschätzt (\(s_*\), mit n − 1 im Nenner), und die Teststatistik folgt der t-Verteilung. Die t-Verteilung hat dickere Ränder, deshalb sind die kritischen Werte größer (4.604 statt 2.576). Man braucht stärkere Beweise, weil man σ nicht genau kennt.",
"t.test-Output: richtigen Code wählen und entscheiden": r"Drei Dinge prüfen: richtiger Datenvektor, richtiges mu, richtige alternative. Die alternative ist die Richtung von H₁: \"less\" für &lt;, \"greater\" für &gt;, ohne Angabe ≠. Der t-Wert ist bei allen drei Varianten gleich – nur der p-Wert ändert sich, weil eine andere Fläche gemeint ist.",
"Approximativer Binomialtest für einen Anteil": r"Unter H₀ erwartet man \(n\pi_0=200\) Zustimmungen mit Standardabweichung \(\sqrt{n\pi_0(1-\pi_0)}=10.95\). Beobachtet sind 182, also 1.643 Standardabweichungen zu wenig. Das liegt ganz knapp vor der 5 %-Grenze (1.645). Lehre: Erst am Ende runden, sonst kippt die Entscheidung.",
"Varianztest (χ²) vollständig": r"Die Teststatistik vergleicht die beobachtete Streuung mit der behaupteten: \(\frac{(n-1)s_*^2}{\sigma_0^2}\). Ist die Streuung wirklich kleiner, wird der Wert klein → linksseitiger Test. Achtung, die Aufgabe nennt σ = 0.08. Im Nenner steht σ² = 0.0064.",
"p-Wert und Ablehnungsbereich in die χ²-Dichte einzeichnen": r"Zeichnen ist hier nur eine Bildversion von „p &lt; α“: Beide Flächen beginnen links bei 0. Die α-Fläche reicht bis zum kritischen Wert, die p-Fläche bis zur Teststatistik. Liegt die Teststatistik links vom kritischen Wert, ist die p-Fläche kleiner → verwerfen.",
"Vorzeichentest für den Median": r"Wenn 50 wirklich der Median wäre, läge jeder Wert mit Wahrscheinlichkeit 0.5 darunter – wie ein Münzwurf. 7 von 10 unter 50 ist aber nicht ungewöhnlich (p = 0.344). Zweiseitig zählt man „mindestens so extrem“ auf beiden Seiten: 7 oder mehr bzw. 3 oder weniger.",
"χ²-Unabhängigkeitstest per Hand": r"Erwartete Häufigkeit unter Unabhängigkeit: Wenn 90/140 aller Studierenden bestehen, sollten auch von den 80 BWLern 90/140 bestehen → 80 · 90 / 140 = 51.43. Je weiter die beobachteten Zahlen davon abweichen, desto größer wird χ². Das kennst du schon von Tag 1 – neu ist nur der Vergleich mit dem Quantil.",
"χ²-Anpassungstest (Würfel fair?)": r"Bei einem fairen Würfel erwartet man bei 60 Würfen je 10 pro Augenzahl. Die Abweichungen (−2, −1, 2, −3, 0, 4) werden quadriert, durch 10 geteilt und addiert. df = Kategorien − 1, weil die letzte Häufigkeit durch die anderen festliegt (Summe = 60).",
"Test mit einer einzigen Beobachtung (Cappuccino-Typ)": r"Mit nur einer Beobachtung ist n = 1, also Standardfehler = σ. Frage: Ist 4.10 € für Göttingen ungewöhnlich teuer <i>oder</i> billig? → zweiseitig. Test und KI führen zur selben Entscheidung (Dualität). Das KI um 4.10 schließt 3.20 aus ⇔ |z| > 1.96.",
"Welcher Test passt? (Entscheidungsbaum)": r"Erste Frage immer: <b>Über welchen Parameter</b> wird eine Aussage gemacht (μ, π, σ², Median, Zusammenhang, Verteilung)? Zweite Frage: Was ist bekannt (σ?) bzw. wie groß ist n? Wer die erste Frage richtig beantwortet, hat den Test fast immer gefunden.",
})

# ======================================================================
LERN["9"] = r"""
<p><b>Idee:</b> Durch eine Punktwolke wird die Gerade gelegt, die „am besten passt“. Am besten heißt: Die senkrechten Abstände der Punkte zur Geraden (<b>Residuen</b>) sollen insgesamt möglichst klein sein. Man quadriert sie, damit sich positive und negative Abstände nicht aufheben und große Fehler stärker zählen → <b>Methode der kleinsten Quadrate (KQ)</b>.</p>
<p><b>Steigung</b> \(\hat\beta_1=\frac{s_{xy}}{s_x^2}\) – Kovarianz durch Varianz von x (Tag 1!). <b>Achsenabschnitt</b> \(\hat\beta_0=\bar y-\hat\beta_1\bar x\): Die Gerade läuft immer durch den Schwerpunkt \((\bar x,\bar y)\).</p>
<div class="vorgemacht"><b>Vorgemacht:</b> Punkte (1, 2), (2, 4), (3, 5).
<ol><li>\(\bar x=2\), \(\bar y=\frac{11}3=3.667\).</li><li>\(\sum(x_i-\bar x)(y_i-\bar y)=(-1)(-1.667)+0+(1)(1.333)=3\); \(\sum(x_i-\bar x)^2=2\).</li>
<li>\(\hat\beta_1=1.5\), \(\hat\beta_0=3.667-1.5\cdot2=0.667\).</li><li>Gerade: \(\hat y=0.667+1.5x\). Für x = 2: ŷ = 3.667, Residuum 4 − 3.667 = 0.333.</li></ol></div>
<p><b>R²</b> = Anteil der Streuung von y, den die Gerade erklärt (0 = gar nicht, 1 = perfekt). <b>Interpretation einer Steigung</b> immer mit „im Durchschnitt“, Einheiten und „ceteris paribus“ (wenn alle anderen Variablen gleich bleiben).</p>"""

CHECK["9"] = [
    (r"\(\hat\beta_0=1\), \(\hat\beta_1=2\). Prognose für x = 3? Residuum, wenn y = 8 beobachtet wurde?", r"\(\hat y=7\); Residuum \(8-7=1\)"),
    (r"lm-Output: Estimate 0.8, Std. Error 0.2. t value?", r"\(0.8/0.2=4\)"),
]

VERST.update({
"KQ-Gerade per Hand": r"Die Tabellenmethode ist am sichersten: Spalten \(x_i-\bar x\), \(y_i-\bar y\), deren Produkt und \((x_i-\bar x)^2\). Die Steigung ist „gemeinsame Bewegung durch Bewegung von x“. Kontrolle: Der Punkt \((\bar x,\bar y)=(3;\,5.6)\) muss auf der Geraden liegen (1.4 + 1.4 · 3 = 5.6 ✓).",
"Prognose, Residuen und R²": r"Residuum positiv = Punkt liegt über der Geraden (Modell unterschätzt). Die Residuen summieren sich bei KQ immer zu 0 – gute Kontrolle (0.2 + 0.8 − 1.6 + 0 + 0.6 = 0 ✓). R² vergleicht die übrig gebliebene Streuung (Residuen) mit der Gesamtstreuung von y.",
"lm-Output lesen: Interpretation, Prognose, Signifikanz": r"Lies den Output wie eine Tabelle: Jede Zeile ist ein Koeffizient. Estimate = Schätzwert, Std. Error = Standardfehler, t value = Estimate / Std. Error, Pr(>|t|) = p-Wert des Tests β = 0. Für die Prognose setzt du die Werte in die Gleichung ein, für Dummy-Variablen 0 oder 1.",
})
