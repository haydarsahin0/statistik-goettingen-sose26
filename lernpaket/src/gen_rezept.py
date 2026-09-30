"""Erzeugt content/rezept1.html – Rezeptbuch Tag 1 im Klausurformat."""
import os

C = []  # (section, title, prob, aufgabe, steps, loesung, warn, fig)


def sec(t):
    C.append(("SEC", t))


def card(title, p, aufgabe, steps, loesung, warn=None, fig=None, bsp=None):
    C.append(("CARD", title, p, aufgabe, steps, loesung, warn, fig, bsp))


# =====================================================================
sec("A · Grundbegriffe, Skalen, Stichproben")

card("Skalenniveau und diskret/stetig", 90,
 "Eine Umfrage im Fitnessstudio erhebt: (i) Alter in Jahren, (ii) Anzahl Besuche pro Woche, (iii) Tarif (Basic, Premium, Student), (iv) Zufriedenheit von 1 bis 7. Geben Sie jeweils das Skalenniveau an und ob das Merkmal diskret oder stetig ist. <span class='pt'>(4 P)</span>",
 ["Frage 1: Kann man die Werte ordnen? Nein → <b>nominal</b>.",
  "Frage 2: Sind die Abstände sinnvoll? Nein → <b>ordinal</b>. Ja → <b>kardinal</b>.",
  "Frage 3: Wird gezählt (Personen, Besuche)? → <b>diskret</b>. Wird gemessen (Zeit, Gewicht, Geld, Größe)? → <b>stetig</b>.",
  "Nominale und ordinale Merkmale sind immer diskret."],
 "(i) Alter: kardinal, stetig<br>(ii) Anzahl Besuche: kardinal, diskret<br>(iii) Tarif: nominal, diskret<br>(iv) Zufriedenheit: ordinal, diskret",
 "Skala 1–7 ist <b>ordinal</b>, nicht kardinal. Punkte 0–100 sind kardinal. 0/1-Merkmal (richtig/falsch): „ordinalskaliert/binär“.")

card("Sinnvolle Lagemaße", 60,
 "Welche Lagemaße sind für das Merkmal (iii) Tarif und (iv) Zufriedenheit sinnvoll? Begründen Sie. <span class='pt'>(2 P)</span>",
 ["Skala bestimmen.", "nominal → nur Modus. ordinal → Modus und Median. kardinal → Modus, Median, Mittelwert.",
  "Immer einen Grund dazuschreiben."],
 "Tarif: nur der Modus, da das Merkmal nominal ist.<br>Zufriedenheit: Modus und Median, da das Merkmal ordinal ist (ordnen möglich, Abstände nicht interpretierbar).",
 "Ausnahme: 0/1-Daten → Mittelwert = Anteil der Einsen ist sinnvoll.")

card("Einheit, Grundgesamtheit, Stichprobe", 25,
 "Das Studio befragt zufällig 200 seiner 2400 Mitglieder (Jahr 2026). Nennen Sie die statistische Einheit, die Grundgesamtheit und die Stichprobe. <span class='pt'>(3 P)</span>",
 ["Einheit = <b>ein</b> einzelnes Objekt (Singular).", "Grundgesamtheit = <b>alle</b> + Ort + Zeit.", "Stichprobe = die wirklich Befragten."],
 "Einheit: ein Mitglied des Studios.<br>Grundgesamtheit: alle 2400 Mitglieder des Studios im Jahr 2026.<br>Stichprobe: die 200 befragten Mitglieder.",
 "Nicht „die Mitglieder“ als Einheit schreiben.")

card("Stichprobenverfahren", 30,
 "(a) Aus jedem der 7 Stadtteile werden zufällig 30 Personen gezogen. (b) Es werden zufällig 3 Schulen gewählt und alle Lehrkräfte befragt. Welche Verfahren liegen vor? <span class='pt'>(2 P)</span>",
 ["„zufällig aus der ganzen Liste“ → einfache Zufallsstichprobe.",
  "„aus <b>jeder</b> Gruppe zufällig“ / „Anteile wie in der Gesamtheit“ → geschichtete Stichprobe.",
  "„zufällig <b>ganze</b> Gruppen, darin <b>alle</b>“ → Klumpenstichprobe.",
  "„Quoten bewusst erfüllen, nicht zufällig“ → Quotenverfahren."],
 "(a) Geschichtete Stichprobe.<br>(b) Klumpenstichprobe.",
 "Nur Göttinger Schulen für ganz Deutschland → Klumpen, nicht geschichtet.")

card("Störvariable und Kontrolle", 20,
 "Ein Studio testet ein neues Trainingsprogramm. Nennen Sie eine Störvariable und eine Möglichkeit, sie zu kontrollieren. <span class='pt'>(2 P)</span>",
 ["Störvariable: beeinflusst das Ergebnis, wird aber nicht untersucht (Alter, Vorwissen, Fitness).",
  "Kontrolle: Randomisierung (zufällige Gruppen) · Homogenisierung (gleiche Gruppen bilden) · statistische Modellierung (Variable in die Analyse)."],
 "Störvariable: das Alter der Teilnehmenden. Kontrolle durch Randomisierung, d. h. zufällige Aufteilung auf Trainings- und Kontrollgruppe.")

card("Repräsentativ? Schluss auf die Grundgesamtheit", 15,
 "Eine Online-Umfrage mit 20 Teilnehmenden ergibt 35 % Raucher. Ein Kommilitone sagt: „Also rauchen 35 % aller Deutschen.“ Nehmen Sie Stellung. <span class='pt'>(2 P)</span>",
 ["Fehlen Personen systematisch? (Online → ohne Internet fehlen).", "Ist n klein? → Schätzung unsicher."],
 "Nein. Die Stichprobe ist nicht repräsentativ, da Personen ohne Internet keine Chance hatten, teilzunehmen. Außerdem ist n = 20 zu klein; der wahre Anteil kann deutlich abweichen.")

card("Modell · deterministisch · deskriptiv/induktiv", 10,
 "Korrigieren Sie: „Ein Modell ist die fehlerfreie Wiedergabe der Realität.“ <span class='pt'>(1 P)</span>",
 ["Auswendig lernen – keine Rechnung."],
 "Ein Modell ist eine vereinfachte Beschreibung der Realität.<br><i>Weitere Sätze:</i> Deterministisch: keine Unsicherheit im Modell. · Induktive Statistik schließt von der Stichprobe auf die Grundgesamtheit unter Berücksichtigung der Unsicherheit. · Ein diskretes Merkmal kann auch abzählbar unendlich viele Werte haben.")

# =====================================================================
sec("B · Häufigkeiten, Histogramm, Verteilungsfunktion")

card("Häufigkeitstabelle vervollständigen", 35,
 "30 Personen: Anzahl gelesener Bücher 1–5. Bekannt: h₁ = 4, H₂ = 12, f₃ = 1/3, F₄ = 28/30. Vervollständigen Sie die Tabelle (h, f, H, F). <span class='pt'>(3 P)</span>",
 ["n = Summe aller h (hier gegeben: 30).", "f = h / n.", "H = von links <b>aufaddieren</b>.", "F = H / n. Letztes F = 1.",
  "Rückwärts: h = H − vorheriges H · h = f · n · H = F · n."],
 "h: 4, 8, 10, 6, 2 · f: 0.133, 0.267, 0.333, 0.2, 0.067<br>H: 4, 12, 22, 28, 30 · F: 0.133, 0.4, 0.733, 0.933, 1",
 "Brüche sind erlaubt (8/30 = 4/15).")

card("Anteile: höchstens / weniger als / mehr als / mindestens", 40,
 "Bestimmen Sie die Anteile der Studierenden mit (i) mehr als 3, (ii) mindestens 3, (iii) weniger als 4, (iv) nicht mehr als 5 Semestern. (F: F(2)=1/23, F(3)=8/23, F(4)=13/23, F(5)=18/23) <span class='pt'>(4 P)</span>",
 ["höchstens k / nicht mehr als k → F(k).", "weniger als k → F(k−1).", "mehr als k → 1 − F(k).", "mindestens k → 1 − F(k−1)."],
 "(i) 1 − 8/23 = 15/23 · (ii) 1 − 1/23 = 22/23 · (iii) F(3) = 8/23 · (iv) F(5) = 18/23")

card("Höhen im normierten Histogramm", 45,
 "50 Studierende, Pendelzeit: [0,10): 8 · [10,20): 15 · [20,30): 12 · [30,60): 10 · [60,90]: 5. Berechnen Sie für jede Klasse die relative Häufigkeit und die Höhe der Säule im (normierten) Histogramm. <span class='pt'>(4 P)</span>",
 ["f = Anzahl / n (8/50 = 0.16).", "Breite = obere − untere Grenze (10).", "Höhe = f / Breite (0.16/10 = 0.016).", "Kontrolle: Summe (Breite · Höhe) = 1."],
 "f: 0.16, 0.3, 0.24, 0.2, 0.1<br>Höhe: 0.016, 0.03, 0.024, 0.0067, 0.0033",
 "Bei absoluten Häufigkeiten: Höhe = h / (Breite · n).")

card("Histogramm zeichnen", 30,
 "Zeichnen Sie das normierte Histogramm der Pendelzeiten. <span class='pt'>(3 P)</span>",
 ["x-Achse: Klassengrenzen eintragen (0, 10, 20, 30, 60, 90), Name + Einheit.", "y-Achse: „Dichte“, Skala bis zur größten Höhe.",
  "Pro Klasse ein Rechteck: Breite = Klasse, Höhe = berechnete Höhe.", "Rechtecke berühren sich (keine Lücken). Titel."],
 "Zeichnung wie unten. Achsen: „Pendelzeit in Minuten“ / „Dichte“.",
 "Nicht die Anzahl als Höhe nehmen – das wäre ein Säulendiagramm.", fig="rz_hist")

card("Anteil in einem Intervall aus dem Histogramm", 40,
 "Schätzen Sie mit dem Histogramm den Anteil der Studierenden, die zwischen 25 und 45 Minuten pendeln. Welche Annahme treffen Sie? <span class='pt'>(3 P)</span>",
 ["Intervall in Stücke teilen, jedes Stück in einer Klasse: 25–30 und 30–45.", "Pro Stück: Breite · Höhe: 5 · 0.024 = 0.12 · 15 · 0.0067 = 0.1.", "Addieren: 0.22. Anzahl? × n."],
 "Anteil ≈ 5 · 0.024 + 15 · 0.0067 = 0.22.<br>Annahme: Die Werte sind innerhalb jeder Klasse gleichmäßig verteilt.",
 "Den Annahme-Satz nie vergessen (1 Punkt).")

card("Anzahl aus dem Histogramm", 30,
 "Ein normiertes Histogramm von 400 Beobachtungen hat über (30, 40] die Höhe 0.025. Wie viele Beobachtungen liegen in dieser Klasse? <span class='pt'>(1 P)</span>",
 ["Höhe · Breite = Anteil: 0.025 · 10 = 0.25.", "Anteil · n = Anzahl: 0.25 · 400."],
 "100 Beobachtungen.")

card("Modalklasse", 30,
 "Welche Klasse ist die Modalklasse? Ist die Aussage „Die Modalklasse ist immer die Klasse mit der höchsten Säule“ korrekt? <span class='pt'>(2 P)</span>",
 ["Modalklasse = Klasse mit der <b>größten Anzahl</b> (nicht die höchste Säule).", "Bei ungleichen Breiten kann eine breite Klasse viele Werte, aber eine niedrige Säule haben."],
 "Modalklasse: [10, 20), da dort die meisten Beobachtungen liegen (15).<br>Die Aussage ist im Allgemeinen falsch: Bei ungleichen Klassenbreiten ist die Höhe = f / Breite.")

card("Säulendiagramm oder Histogramm?", 30,
 "Wieso ist die folgende Grafik (absolute Häufigkeiten, ungleiche Klassenbreiten) kein Histogramm? Was ist der Nachteil? Wie muss der R-Befehl geändert werden? <span class='pt'>(3 P)</span>",
 ["Säulendiagramm: Höhe = Anzahl. Histogramm: Fläche = Anteil.", "Nachteil: breite Klassen wirken zu groß.", "R: <code>freq = FALSE</code> oder <code>prob = TRUE</code>."],
 "Es ist ein Säulendiagramm, da absolute Häufigkeiten bei unterschiedlichen Klassenbreiten dargestellt werden. Das führt zu einer verzerrten Darstellung. Richtig: <code>hist(x, breaks = …, freq = FALSE)</code>.",
 fig="saeule_hist")

card("Empirische Verteilungsfunktion aufstellen und skizzieren", 55,
 "Zehn Studierende: Tassen Kaffee gestern: 0, 1, 1, 2, 2, 2, 3, 3, 4, 6. Stellen Sie F̂(x) als Funktion mit Fallunterscheidung auf und skizzieren Sie sie. <span class='pt'>(4 P)</span>",
 ["Verschiedene Werte sortieren: 0, 1, 2, 3, 4, 6.", "Kumulierte Anteile: 0.1, 0.3, 0.6, 0.8, 0.9, 1.",
  "Fallunterscheidung: erste Zeile 0, letzte Zeile 1; links ≤, rechts &lt;.",
  "Skizze: waagerechte Stufen, ● links (gehört dazu), ○ rechts. Keine senkrechten Linien. Links bei 0 und rechts bei 1 ins Unendliche weiterzeichnen. Achsen beschriften."],
 "F̂(x) = 0 für x &lt; 0<br>0.1 für 0 ≤ x &lt; 1<br>0.3 für 1 ≤ x &lt; 2<br>0.6 für 2 ≤ x &lt; 3<br>0.8 für 3 ≤ x &lt; 4<br>0.9 für 4 ≤ x &lt; 6<br>1 für x ≥ 6<br>+ Skizze wie unten",
 fig="rz_ecdf")

card("Verteilungsfunktion ablesen", 35,
 "Lesen Sie ab: F̂(2.5), den Anteil mit mehr als 2 Tassen, den Anteil mit mindestens 1 Tasse und den Median. <span class='pt'>(3 P)</span>",
 ["F̂(2.5): Stufe über 2.5 → 0.6.", "mehr als 2: 1 − F(2) = 0.4 · mindestens 1: 1 − F(0) = 0.9.",
  "Median aus der Grafik: bei 0.5 waagerecht gehen, bis man eine Stufe trifft → x-Wert ablesen."],
 "F̂(2.5) = 0.6 · Anteil &gt; 2: 0.4 · Anteil ≥ 1: 0.9 · Median = 2")

card("Aus der Verteilungsfunktion zurückrechnen", 20,
 "F̂ springt bei 10 auf 0.3, bei 20 auf 0.6 und bei 30 auf 1 (n = 10). Bestimmen Sie die absoluten Häufigkeiten und den Mittelwert. <span class='pt'>(3 P)</span>",
 ["Sprunghöhe = f: 0.3, 0.3, 0.4.", "h = f · n: 3, 3, 4.", "Mittelwert = Σ Wert · h / n."],
 "h: 3, 3, 4 · x̄ = (3·10 + 3·20 + 4·30)/10 = 21")

# =====================================================================
sec("C · Lagemaße")

card("Mittelwert, Median, Modus aus Rohdaten", 85,
 "Wartezeiten (min): 12, 7, 3, 9, 7, 15, 7, 10. Berechnen Sie arithmetisches Mittel, Median und Modus. <span class='pt'>(3 P)</span>",
 ["Zuerst <b>sortieren</b>: 3, 7, 7, 7, 9, 10, 12, 15 (n = 8).", "Mittelwert = Summe / n = 70/8.",
  "Median: n ungerade → mittlerer Wert. n gerade → Mittel aus Platz n/2 und n/2+1 (Platz 4 und 5).", "Modus = häufigster Wert."],
 "x̄ = 70/8 = 8.75 · x_med = (7 + 9)/2 = 8 · x_mod = 7",
 "Median immer aus der sortierten Liste aller Werte.")

card("Lagemaße aus einer Häufigkeitstabelle", 40,
 "20 Haushalte, Kinder a: 0, 1, 2, 3, 4 mit h: 5, 8, 4, 2, 1. Bestimmen Sie Modus, Median und Mittelwert. <span class='pt'>(3 P)</span>",
 ["Mittelwert: Σ a · h / n = (0 + 8 + 8 + 6 + 4)/20.", "Median: H bilden (5, 13, 17, …). Platz 10 und 11 → beide bei a = 1.", "Modus: a mit größtem h."],
 "x̄ = 26/20 = 1.3 · x_med = 1 · x_mod = 1")

card("Klassierte Daten: Mittelwert und Varianz", 45,
 "Arbeitszeit: [0,4]: 40.2 %, (4,8]: 19.6 %, (8,12]: 21.9 %, (12,16]: 18.3 %. Berechnen Sie näherungsweise Mittelwert und Varianz mit den Klassenmitten. <span class='pt'>(3 P)</span>",
 ["Klassenmitte m = (unten + oben)/2: 2, 6, 10, 14.", "Tabelle: f · m und f · m².", "Mittelwert = Σ f · m.", "Varianz = Σ f · m² − Mittelwert²."],
 "x̄ = 0.402·2 + 0.196·6 + 0.219·10 + 0.183·14 = 6.732<br>s² = 66.432 − 6.732² = 21.112",
 "Prozente sind schon f – nicht durch n teilen. Mit Anzahlen: Σ h·m / n.")

card("Gesamtmittelwert aus zwei Gruppen", 15,
 "Filiale A: 9 Personen, Ø 4.844 Tsd. €. Filiale B: 6 Personen, Ø 3.5 Tsd. €. Berechnen Sie das Durchschnittsgehalt aller 15 Personen. <span class='pt'>(2 P)</span>",
 ["Summe je Gruppe = n · Mittel: 43.6 und 21.", "Summen addieren, durch alle teilen."],
 "x̄ = (9 · 4.844 + 6 · 3.5)/15 = 64.6/15 = 4.307",
 "Nicht (4.844 + 3.5)/2 rechnen.")

card("Fehlender, falscher oder neuer Wert", 10,
 "5 Werte haben den Mittelwert 6. Vier Werte sind 4, 8, 5, 7. Wie lautet der fünfte? <span class='pt'>(1 P)</span>",
 ["Summe = n · Mittelwert = 30.", "Fehlender Wert = Summe − bekannte Werte."],
 "5 · 6 − (4 + 8 + 5 + 7) = 6")

card("Welches Lagemaß ist typischer? (Ausreißer)", 35,
 "Gehälter (Tsd. €): 2.8, 3.1, 3.1, 3.4, 3.6, 3.9, 4.2, 4.5, 15.0. Welches Lagemaß beschreibt das typische Gehalt besser? <span class='pt'>(1 P)</span>",
 ["Gibt es einen extremen Wert? → Median."],
 "Der Median (3.6), da er robust gegenüber dem Ausreißer 15.0 ist; der Mittelwert (4.844) wird von ihm nach oben gezogen.")

card("Schiefe bestimmen", 35,
 "Ist die Verteilung rechtsschief, symmetrisch oder linksschief? Begründen Sie mit den Lagemaßen. <span class='pt'>(2 P)</span>",
 ["Mittelwert &gt; Median &gt; Modus → rechtsschief (linkssteil).", "Mittelwert &lt; Median &lt; Modus → linksschief.", "Alle etwa gleich → symmetrisch.", "Zahlen in die Antwort schreiben."],
 "Rechtsschief, da x̄ = 4.844 &gt; x_med = 3.6 &gt; x_mod = 3.1.")

card("Transformation: Lagemaße und Streuung", 20,
 "Lieferzeiten in Tagen: x̄ = 5.5, s² = 9.917, s = 3.149. Die Zeiten werden in Stunden umgerechnet. Wie ändern sich Mittelwert, Varianz und Standardabweichung? <span class='pt'>(2 P)</span>",
 ["Faktor finden: Tage → Stunden: · 24. (+5 % → · 1.05)", "Mittelwert, Median, s, IQR: · Faktor.", "Varianz: · Faktor².", "Nur addiert (+200 €)? → Mittelwert + 200, Varianz und s bleiben gleich."],
 "x̄ = 24 · 5.5 = 132 Stunden<br>s² = 24² · 9.917 = 5712 Stunden²<br>s = 24 · 3.149 = 75.58 Stunden",
 "Nicht neu rechnen – nur die Regel anwenden.")

card("0/1-Daten", 25,
 "20 Vorhersagen: 11-mal falsch (0), 9-mal richtig (1). Skalenniveau? Berechnen Sie Modus, Median, Mittelwert und Varianz. Falls nicht sinnvoll, begründen Sie. <span class='pt'>(5 P)</span>",
 ["Skala: ordinalskaliert/binär.", "Modus = häufigerer Wert, Median = Mitte der sortierten Liste.", "Mittelwert = Anzahl Einsen / n = Anteil.", "Varianz: x̄(1 − x̄) <b>oder</b> „nicht sinnvoll“ – nur eins davon schreiben."],
 "ordinalskaliert/binär · x_mod = 0 · x_med = 0 · x̄ = 9/20 = 0.45<br>s² = 0.45 · 0.55 = 0.248")

# =====================================================================
sec("D · Quantile, Streuung, Boxplot")

card("Quartile nach der Vorlesungsdefinition", 45,
 "Lieferzeiten (sortiert): 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 9, 14. Bestimmen Sie das untere und das obere Quartil sowie den Interquartilsabstand. <span class='pt'>(3 P)</span>",
 ["Plätze über die Werte schreiben: 1 … 12.", "n · 0.25 = 3 → das ist eine <b>Platznummer</b>.",
  "Keine ganze Zahl → aufrunden → dieser Platz. Ganze Zahl k → Mittel aus Platz k und k+1.", "Genauso mit 0.75. IQR = oben − unten."],
 "12 · 0.25 = 3 → x₀.₂₅ = (x₍₃₎ + x₍₄₎)/2 = (3 + 4)/2 = 3.5<br>12 · 0.75 = 9 → x₀.₇₅ = (6 + 7)/2 = 6.5<br>IQR = 3",
 "„x₀.₇₅ = 9“ ist falsch – 9 ist der Platz, nicht der Wert.")

card("Varianz und Standardabweichung", 85,
 "Hinweis: Σx = 66, Σx² = 482, n = 12. Berechnen Sie die empirische Varianz s², die unverzerrte Varianz s*² und die Standardabweichung s. Geben Sie Ihren Lösungsweg an. <span class='pt'>(3 P)</span>",
 ["Mittelwert: 66/12 = 5.5.", "s² = Σx²/n − Mittelwert² = 40.1667 − 30.25.", "s*² = s² · n/(n−1) – keine Wurzel!", "s = √s².",
  "Ohne Σx²: jeden Wert quadrieren und addieren. Tabelle: Σ a²·h / n − x̄²."],
 "s² = 482/12 − 5.5² = 9.917<br>s*² = 12/11 · 9.917 = 10.818<br>s = √9.917 = 3.149",
 "„empirisch“ = 1/n. „unverzerrt“ = 1/(n−1). R: var und sd sind unverzerrt.")

card("Varianz aus R-Output umrechnen", 20,
 "R liefert <code>var(x)</code> = 53.174 bei n = 12. Wie groß ist die empirische Varianz? <span class='pt'>(1 P)</span>",
 ["R rechnet mit n − 1.", "s² = var · (n − 1)/n."],
 "s² = 53.174 · 11/12 = 48.743")

card("Ausreißer, Whisker und Boxplot zeichnen", 35,
 "Gibt es Ausreißer nach der 1.5·IQR-Regel? Wo enden die Whisker? Skizzieren Sie den Boxplot (x₀.₂₅ = 3.5, Median 4.5, x₀.₇₅ = 6.5, Daten wie oben). <span class='pt'>(3 P)</span>",
 ["1.5 · IQR = 4.5.", "Grenzen: 3.5 − 4.5 = −1 und 6.5 + 4.5 = 11.", "Werte außerhalb = Ausreißer (14).",
  "Whisker enden beim letzten <b>echten Wert innerhalb</b> der Grenzen: unten 2, oben 9.",
  "Zeichnen: Achse mit Zahlen, Box von 3.5 bis 6.5, Strich bei 4.5, Whisker, Punkt bei 14."],
 "Grenzen: −1 und 11. Der Wert 14 ist ein Ausreißer. Unterer Whisker bei 2, oberer Whisker bei 9.<br>+ Skizze wie unten",
 "Die Whisker gehen nicht bis zur Grenze (11), sondern bis 9. Beide Whisker nennen!", fig="rz_box")

card("Boxplots lesen und vergleichen", 30,
 "Lesen Sie für Gruppe A Median, x₀.₂₅ und Maximum ab. Welche Aussagen sind korrekt? (i) A streut stärker als B. (ii) A hat einen Ausreißer bei 40. (iii) Gruppe B verursacht längere Kämpfe. (iv) A ist rechtsschief. <span class='pt'>(4 P)</span>",
 ["Strich in der Box = Median. Box-Ränder = x₀.₂₅ und x₀.₇₅. Whisker-Ende = Min/Max (ohne Ausreißer).",
  "Streuung vergleichen: Breite der Box (IQR).", "Nur eingezeichnete Punkte sind Ausreißer.", "Median nah am unteren Rand + langer oberer Whisker → rechtsschief.",
  "Unterschiede zwischen Gruppen sind keine Kausalität."],
 "A: Median 8, x₀.₂₅ = 5, Maximum 40.<br>(i) richtig (IQR 15 gegen 4) · (ii) falsch, kein Punkt eingezeichnet · (iii) falsch, nur Zusammenhang, keine Kausalität · (iv) richtig",
 fig="rz_box2")

card("Vorteil von Standardabweichung und Median", 35,
 "Welchen Vorteil bietet die Standardabweichung gegenüber der Varianz? Nennen Sie einen Vorteil des Medians gegenüber dem Mittelwert. <span class='pt'>(2 P)</span>",
 ["Auswendig lernen."],
 "Die Standardabweichung hat die gleiche Maßeinheit wie das Merkmal.<br>Der Median ist robust gegenüber Ausreißern.",
 "Nicht: „Die Standardabweichung wird durch Ausreißer nicht verzerrt“ – das ist falsch.")

card("Spannweite und Form der Verteilung", 10,
 "Bestimmen Sie die Spannweite und beschreiben Sie die Form der Verteilung. <span class='pt'>(2 P)</span>",
 ["Spannweite = Maximum − Minimum.", "Form: Anzahl Gipfel (unimodal/bimodal) + Schiefe."],
 "Spannweite = 90 − 2.5 = 87.5. Die Verteilung ist unimodal und rechtsschief.")

# =====================================================================
sec("E · Zwei Merkmale: Kontingenztafel und χ²")

card("Kontingenztafel aus einem Text", 35,
 "Von 200 Studierenden rauchen 60 (R). Von den Rauchenden treiben 15 Sport (S). Insgesamt treiben 110 keinen Sport. Erstellen Sie die Kontingenztafel inkl. Randhäufigkeiten. <span class='pt'>(3 P)</span>",
 ["Leere 2×2-Tafel mit Σ-Zeile und Σ-Spalte zeichnen, n = 200 unten rechts.", "Zahlen aus dem Text eintragen (60, 15, 110).",
  "Rest durch Subtraktion: 60 − 15 = 45 · 200 − 60 = 140 · 200 − 110 = 90 · 90 − 15 = 75 · 140 − 75 = 65.", "Kontrolle: alle Summen stimmen."],
 "<table class='tab'><tr><th></th><th>S</th><th>kein S</th><th>Σ</th></tr><tr><th>R</th><td>15</td><td>45</td><td>60</td></tr><tr><th>kein R</th><td>75</td><td>65</td><td>140</td></tr><tr><th>Σ</th><td>90</td><td>110</td><td>200</td></tr></table>",
 "„30 % der Frauen“ → × Anzahl Frauen, nicht × n.")

card("Bedingte Anteile und Zusammenhang", 35,
 "Berechnen Sie den Anteil der Sporttreibenden unter den Rauchenden und unter den Nichtrauchenden. Deutet das auf einen Zusammenhang hin? <span class='pt'>(3 P)</span>",
 ["„unter den Rauchenden“ → durch die Summe der Rauchenden teilen (60).", "Genauso für die andere Gruppe (140).", "Anteile verschieden → Zusammenhang. Gleich → kein Zusammenhang.", "„Anteil aller …“ oder „A und B“ → durch n teilen."],
 "Unter den Rauchenden: 15/60 = 0.25 · unter den Nichtrauchenden: 75/140 = 0.536.<br>Ja, die Anteile unterscheiden sich deutlich, also gibt es einen Zusammenhang zwischen Rauchen und Sport.")

card("Bedingte Verteilung als Tabelle", 20,
 "Bestimmen Sie die bedingte Verteilung von „Sport“ gegeben „Rauchen“ (zeilenweise). <span class='pt'>(2 P)</span>",
 ["Jede Zelle durch ihre Zeilensumme teilen.", "Jede Zeile ergibt 1."],
 "R: 0.25 / 0.75 · kein R: 0.536 / 0.464")

card("Erwartete Häufigkeiten und χ²-Koeffizient", 30,
 "Berechnen Sie die bei Unabhängigkeit erwarteten Häufigkeiten und den χ²-Koeffizienten. <span class='pt'>(4 P)</span>",
 ["Erwartet pro Zelle: Zeilensumme · Spaltensumme / n (60 · 90/200 = 27).", "Pro Zelle: (beobachtet − erwartet)² / erwartet.", "Alle Zellen addieren.", "Kontrolle: erwartete Tafel hat dieselben Randsummen."],
 "Erwartet: 27, 33, 63, 77<br>χ² = 12²/27 + 12²/33 + 12²/63 + 12²/77 = 5.333 + 4.364 + 2.286 + 1.870 = 13.853<br>χ² &gt; 0 → Zusammenhang.",
 "Im Nenner steht der <b>erwartete</b> Wert. χ² ist nie negativ.")

card("Tafel bei Unabhängigkeit", 15,
 "Wie müsste die Tafel aussehen, wenn Rauchen und Sport unabhängig wären? Wie groß wäre dann χ²? <span class='pt'>(2 P)</span>",
 ["Genau die erwarteten Häufigkeiten eintragen."],
 "Rauchen: 27 | 33 · Nichtrauchen: 63 | 77. Dann wäre χ² = 0.")

# =====================================================================
sec("F · Kovarianz, Korrelation, Kausalität")

card("Streudiagramm zeichnen", 40,
 "Filialen: x (Werbung, Tsd. €): 2, 4, 3, 6, 5, 1 · y (Umsatz, Tsd. €): 30, 45, 38, 60, 48, 25. Zeichnen Sie ein beschriftetes Streudiagramm. <span class='pt'>(2 P)</span>",
 ["x-Achse: erstes Merkmal mit Name und Einheit, Skala.", "y-Achse: zweites Merkmal mit Name und Einheit, Skala.", "Jedes Paar (x, y) als Punkt einzeichnen.", "Titel darüber schreiben."],
 "Zeichnung wie unten mit Achsen „Werbeausgaben X (Tsd. €)“ und „Umsatz Y (Tsd. €)“.",
 "Ohne Achsenbeschriftung gibt es höchstens die Hälfte der Punkte.", fig="rz_streu")

card("Streudiagramme lesen und zuordnen · r = 0 skizzieren", 35,
 "Ordnen Sie die Korrelationskoeffizienten 0.96, −0.91, 0.58, 0.13 und −0.02 den Grafiken A–E zu. Skizzieren Sie ein Streudiagramm mit r ≈ 0. <span class='pt'>(3 P)</span>",
 ["Steigt die Wolke → r positiv. Fällt sie → r negativ.", "Je schmaler die Wolke um eine Gerade → |r| näher bei 1.", "Runde Wolke oder U-Form → r ≈ 0.", "r misst nur <b>lineare</b> Zusammenhänge: die Parabel (E) hat r ≈ 0, obwohl y von x abhängt."],
 "A: 0.96 · B: −0.91 · C: 0.58 · D: 0.13 · E: −0.02<br>Skizze r = 0: runde Punktwolke ohne Richtung, Achsen beschriftet.",
 fig="rz_r5")

card("Kovarianz und Korrelation aus Summen", 85,
 "Hinweis: n = 6, Σx = 21, Σy = 246, Σx² = 91, Σy² = 10898, Σxy = 979. Berechnen Sie die empirische Kovarianz und den Korrelationskoeffizienten nach Bravais-Pearson. <span class='pt'>(4 P)</span>",
 ["Mittelwerte: x̄ = 21/6 = 3.5, ȳ = 246/6 = 41.", "s²ₓ = Σx²/n − x̄² = 2.917 · s²ᵧ = Σy²/n − ȳ² = 135.333.",
  "Kovarianz s_xy = Σxy/n − x̄ · ȳ.", "r = s_xy / √(s²ₓ · s²ᵧ)."],
 "s_xy = 979/6 − 3.5 · 41 = 19.667<br>r = 19.667 / √(2.917 · 135.333) = 0.990",
 "r = 1 ist fast nie richtig – dann Zähler und Nenner prüfen. Sind s (nicht s²) gegeben: r = s_xy / (s_x · s_y).")

card("Kovarianz und Korrelation aus Rohdaten (Arbeitstabelle)", 45,
 "Portal A: 6, 8, 7, 9, 5 · Portal B: 7, 9, 6, 10, 6. Berechnen Sie x̄, ȳ, s²ₓ, s²ᵧ, s_xy (mit 1/n) und r. <span class='pt'>(4 P)</span>",
 ["Tabelle mit Spalten x, y, x², y², <b>x·y</b>.", "Jede Spalte summieren: 35, 38, 255, 302, 276.", "Dann weiter wie oben."],
 "x̄ = 7 · ȳ = 7.6 · s²ₓ = 2 · s²ᵧ = 2.64<br>s_xy = 276/5 − 7 · 7.6 = 2 · r = 2/√(2 · 2.64) = 0.870",
 "Ohne x·y-Spalte keine Kovarianz.")

card("Korrelationskoeffizient interpretieren", 85,
 "Interpretieren Sie r = 0.870. <span class='pt'>(1–2 P)</span>",
 ["Stärke: |r| &lt; 0.3 schwach · 0.3 bis &lt; 0.7 mittel · ≥ 0.7 stark.", "Richtung: positiv oder negativ.", "Das Wort „linear“.", "Die beiden Merkmale nennen."],
 "Es gibt einen starken positiven linearen Zusammenhang zwischen den Bewertungen von Portal A und Portal B.")

card("Kovarianz interpretieren", 30,
 "Was bedeutet das Vorzeichen der Kovarianz? Kann ihr Wert interpretiert werden? <span class='pt'>(2 P)</span>",
 ["Nur das Vorzeichen deuten."],
 "Das positive Vorzeichen deutet auf einen positiven linearen Zusammenhang hin. Die Höhe ist nicht interpretierbar, da sie von den Einheiten der Merkmale abhängt (z. B. kg·cm).")

card("Einheiten ändern: Kovarianz und Korrelation", 20,
 "Der Umsatz wird in Euro statt in Tsd. € angegeben. Wie ändern sich Kovarianz und Korrelation? <span class='pt'>(2 P)</span>",
 ["Faktor finden: Tsd. € → €: · 1000 · cm → m: · 0.01 · °C → °F: · 1.8 (+32 egal).", "Kovarianz · Faktor.", "Korrelation bleibt gleich (Faktor negativ → nur Vorzeichen wechselt)."],
 "Die Kovarianz wird mit 1000 multipliziert (19 667). Die Korrelation bleibt unverändert (0.990), da sie maßstabsunabhängig ist.")

card("Kovarianz aus gegebener Korrelation", 15,
 "Gegeben: r = −0.6, s²ₓ = 4, s²ᵧ = 25. Berechnen Sie die Kovarianz. <span class='pt'>(1 P)</span>",
 ["Erst Wurzeln ziehen: s_x = 2, s_y = 5.", "s_xy = r · s_x · s_y."],
 "s_xy = −0.6 · 2 · 5 = −6")

card("Rangkorrelation nach Spearman", 25,
 "Bestimmen Sie die Ränge und den Spearman-Koeffizienten (Portal A: 6, 8, 7, 9, 5 · Portal B: 7, 9, 6, 10, 6). <span class='pt'>(3 P)</span>",
 ["Ränge vergeben: kleinster Wert = 1. Gleiche Werte → Durchschnitt der Plätze (2 × 6 → beide 1.5).",
  "Mit den Rängen genau wie Pearson rechnen: Mittelwert der Ränge = (n+1)/2 = 3.",
  "Varianz der Ränge, Kovarianz der Ränge, dann r.",
  "Abkürzung: Ränge von x und y identisch → r_Sp = 1; genau umgekehrt → −1."],
 "Ränge A: 2, 4, 3, 5, 1 · Ränge B: 3, 4, 1.5, 5, 1.5<br>s²_A = 55/5 − 9 = 2 · s²_B = 54.5/5 − 9 = 1.9 · Kov = 53/5 − 9 = 1.6<br>r_Sp = 1.6/√(2 · 1.9) = 0.821",
 "Nicht nur die Ränge angeben – der Koeffizient ist auch gefragt.")

card("Kausalität beurteilen · Drittvariable", 70,
 "Die Geschäftsführung folgert: „Mehr Werbung verursacht mehr Umsatz.“ Beurteilen Sie die Aussage und nennen Sie eine mögliche Drittvariable. <span class='pt'>(2 P)</span>",
 ["Satz 1: Nein, nur Zusammenhang, keine Kausalität.", "Satz 2: konkrete Drittvariable, die <b>beide</b> Merkmale beeinflusst (oder umgekehrte Richtung).", "Satz 3: Für Kausalität braucht man ein randomisiertes Experiment."],
 "Nein. Die Daten zeigen nur einen statistischen Zusammenhang, keine Kausalität. Er könnte durch eine Drittvariable wie die Lage der Filiale entstehen, die sowohl das Werbebudget als auch den Umsatz beeinflusst. Für einen Kausalnachweis bräuchte man ein randomisiertes Experiment.")

card("Scheinkorrelation und ökologischer Fehlschluss", 15,
 "Margarineverbrauch und Scheidungsrate korrelieren mit r = 0.99. Die Regierung verbietet Margarine. Beurteilen Sie. Was ist ein ökologischer Fehlschluss? <span class='pt'>(3 P)</span>",
 ["Scheinkorrelation: hohe Korrelation ohne direkten Zusammenhang – Drittvariable oder Zufall.", "Ökologischer Fehlschluss: von Gruppendaten auf Einzelpersonen schließen."],
 "Das Verbot ist nicht sinnvoll: Es handelt sich um eine Scheinkorrelation. Mögliche Drittvariable: die wirtschaftliche Lage; auch Zufall ist möglich.<br>Ökologischer Fehlschluss: Aus aggregierten Gruppendaten (z. B. Stadtbezirken) wird unzulässig auf Individuen geschlossen.")

card("Richtig oder falsch? (Klassiker)", 45,
 "Welche Aussagen sind korrekt? (a) Wenn ρ ≠ 0, sind X und Y nie unabhängig. (b) Wenn Y = −X², kann ρ ≈ 0 sein. (c) Wenn X = Y, gilt ρ = 1. (d) Wenn ρ ≠ 0, besteht ein kausaler Zusammenhang. (e) Wenn Cov ≥ 0.8, liegt ein starker Zusammenhang vor. <span class='pt'>(5 P)</span>",
 ["Unabhängig ⇒ ρ = 0, aber ρ = 0 ⇏ unabhängig.", "r misst nur lineare Zusammenhänge.", "Kovarianz hängt von den Einheiten ab."],
 "(a) richtig · (b) richtig · (c) richtig · (d) falsch · (e) falsch")

# =====================================================================
sec("G · Mathe-Werkzeug")

card("Summenzeichen", 15,
 "Lösen Sie die Summe Σ(xᵢ − x̄) so weit wie möglich auf. <span class='pt'>(1 P)</span>",
 ["Σ(xᵢ − x̄) = Σxᵢ − n · x̄ = Σxᵢ − Σxᵢ.", "Konstante n-mal summiert: Σc = n · c.", "Nur Zahlen ohne Index dürfen vor das Summenzeichen."],
 "Σ(xᵢ − x̄) = 0")

# =====================================================================
sec("H · R (Teil B)")

card("Daten einlesen (auch als Lückentext)", 95,
 "Setzen Sie mittels <code>setwd(path.expand(\"~\"))</code> Ihr Working Directory. Speichern Sie die Daten aus <code>WitcherData2.csv</code> als Data-Frame-Objekt d und geben Sie die ersten sechs Zeilen wieder. <span class='pt'>(4 P)</span>",
 ["Datei zuerst ansehen: Trennzeichen zwischen den Spalten = sep; Dezimalzeichen = dec.", "Erste Zeile mit Namen → header = TRUE.", "Mit str(d) prüfen: nur 1 Variable → sep falsch."],
 "<code>setwd(path.expand(\"~\"))<br>d &lt;- read.csv(\"WitcherData2.csv\", sep = \";\", dec = \".\", header = TRUE)<br>head(d)</code><br>+ R-Output einfügen",
 "Deutsches CSV (12,5): <code>dec = \",\"</code>.")

card("Objekttypen bestimmen", 80,
 "Ermitteln Sie unter Einbezug eines passenden R-Befehls die Objekttypen der Variablen Tal und Muenzen. <span class='pt'>(4 P)</span>",
 ["<code>str(d)</code> oder <code>typeof(d$Tal)</code> / <code>class(d$Tal)</code>.", "chr = character · int = integer (numerisch, ganze Zahlen) · num = numeric · Factor = factor."],
 "<code>str(d)</code> + Output<br>Die Variable Tal ist ein character-Objekt, die Variable Muenzen ist numerisch vom Typ integer (nur ganze Zahlen).")

card("Mittelwert und Standardabweichung", 90,
 "Berechnen und nennen Sie das arithmetische Mittel und den unverzerrten Schätzer der Standardabweichung der Variable Muenzen. Runden Sie auf drei Nachkommastellen. <span class='pt'>(4 P)</span>",
 ["Immer mit round(…, 3) runden.", "sd ist schon unverzerrt."],
 "<code>round(mean(d$Muenzen), 3)<br>round(sd(d$Muenzen), 3)</code> + Output<br>Das arithmetische Mittel der Variable Muenzen beträgt 22.454. Der unverzerrte Schätzer der Standardabweichung beträgt 4.610.",
 "Fehlende Werte: <code>mean(d$X, na.rm = TRUE)</code>.")

card("Median, IQR, Quantile, Varianz", 60,
 "Bestimmen Sie Median und Interquartilsabstand der Variable Kampfzeit (zwei Nachkommastellen). <span class='pt'>(3 P)</span>",
 ["median(), IQR(), quantile(x, 0.9), summary().", "Empirische Varianz: var(x) · (n−1)/n."],
 "<code>round(median(d$Kampfzeit), 2)<br>round(IQR(d$Kampfzeit), 2)</code> + Output<br>Der Median der Kampfzeit beträgt 26.5 Minuten, der Interquartilsabstand 45.88 Minuten.")

card("Normiertes Histogramm als PDF", 80,
 "Erstellen Sie ein normiertes Histogramm der Variable Muenzen mit den Intervallen [5, 15), [15, 20), [20, 25), [25, 35). Titel „Sitz …, Matr.Nr. …, Aufgabenteil e)“, x-Achse „Muenzen“, y-Achse „Dichte“. Speichern Sie die Grafik als Histogramm.pdf. <span class='pt'>(8 P)</span>",
 ["pdf(\"Name.pdf\") <b>vor</b> der Grafik, dev.off() <b>danach</b>.", "freq = FALSE → normiert.", "[a, b) → right = FALSE. (a, b] → right = TRUE.", "breaks müssen Minimum und Maximum abdecken.", "Datei im Ordner prüfen und hochladen."],
 "<code>pdf(\"Histogramm.pdf\")<br>hist(d$Muenzen, breaks = c(5, 15, 20, 25, 35),<br>&nbsp;&nbsp;freq = FALSE, right = FALSE,<br>&nbsp;&nbsp;main = \"Sitz 12, Matr.Nr. 123, Aufgabenteil e)\",<br>&nbsp;&nbsp;xlab = \"Muenzen\", ylab = \"Dichte\")<br>dev.off()</code>",
 "Fehler „some 'x' not counted“ → breaks sind zu klein.")

card("Streudiagramm / Boxplot / Säulendiagramm (auch Lückentext)", 35,
 "Vervollständigen Sie: <code>pdf(\"Streudiagramm.pdf\")</code> / <code>___(___, ___, pch = 16, ___ = \"Streudiagramm\", ___ = \"Kampfzeit (min.)\", ylab = ___)</code> / <code>___.off()</code> <span class='pt'>(4 P)</span>",
 ["Streudiagramm: plot(x, y). Erste Variable = x-Achse.", "Boxplot: boxplot(Zahl ~ Gruppe, data = d). Säulen: barplot(table(d$X)).", "main = Titel, xlab/ylab = Achsen."],
 "<code>pdf(\"Streudiagramm.pdf\")<br>plot(d$Kampfzeit, d$Muenzen, pch = 16,<br>&nbsp;&nbsp;main = \"Streudiagramm\", xlab = \"Kampfzeit (min.)\", ylab = \"Muenzen\")<br>dev.off()</code>")

card("Klassen bilden mit cut (Lückentext)", 35,
 "Die Variable Kampfzeit.3 hat drei Ausprägungen: {weniger als 5 Minuten, 5 Minuten bis weniger als eine Stunde, eine Stunde oder mehr}. Speichern Sie sie als Factor in d. <span class='pt'>(4 P)</span>",
 ["breaks: Grenzen mit Inf am Ende (1 Stunde = 60 Minuten).", "„weniger als“ → right = FALSE. „bis zu / maximal“ → right = TRUE."],
 "<code>d$Kampfzeit.3 &lt;- cut(d$Kampfzeit, breaks = c(0, 5, 60, Inf), right = FALSE)<br>d$Muenzen.4 &lt;- cut(d$Muenzen, breaks = c(0, 10, 20, 30, Inf), right = TRUE)</code>")

card("Kontingenztafel, Teilgruppe, relative Häufigkeiten", 40,
 "Erstellen Sie die Kontingenztafel von Muenzen.4 und Kampfzeit.3. Ermitteln Sie für Kampfzeiten von mindestens 5 und unter 60 Minuten die relative Häufigkeit jeder Ausprägung von Muenzen.4 (zwei Dezimalstellen). <span class='pt'>(4 P)</span>",
 ["table(x, y) = Kontingenztafel.", "subset(d, Bedingung): &amp; = und, | = oder.", "prop.table(table(…)) = relative Häufigkeiten. prop.table(…, 1) = zeilenweise."],
 "<code>Kontingenz.Tafel &lt;- table(d$Muenzen.4, d$Kampfzeit.3)<br>s &lt;- subset(d, Kampfzeit &gt;= 5 &amp; Kampfzeit &lt; 60)<br>round(prop.table(table(s$Muenzen.4)), 2)</code> + Output")

card("Gruppen vergleichen, zählen, Anteile", 60,
 "Berechnen Sie die durchschnittliche Anzahl Münzen für jedes Tal. In welchem Tal verdient Jaskier am meisten? Wie viele Tavernen zahlten mehr als 20 Münzen? <span class='pt'>(4 P)</span>",
 ["tapply(Zahl, Gruppe, mean).", "sum(Bedingung) = Anzahl. mean(Bedingung) = Anteil."],
 "<code>round(tapply(d$Muenzen, d$Tal, mean), 3)<br>sum(d$Muenzen &gt; 20)</code> + Output<br>Im Bergtal verdient Jaskier im Durchschnitt am meisten (26 Münzen). 7 Tavernen zahlten mehr als 20 Münzen.")

card("Korrelation in R", 60,
 "Wie stark ist der lineare Zusammenhang zwischen Kampfzeit und Muenzen? Berechnen und interpretieren Sie eine geeignete Maßzahl. <span class='pt'>(4 P)</span>",
 ["cor(x, y) = Pearson (Standard).", "cor(x, y, method = \"spearman\") = Spearman.", "Interpretation wie in Teil A (Stärke + Richtung + linear + Merkmale)."],
 "<code>round(cor(d$Kampfzeit, d$Muenzen), 3)</code> + Output<br>Der Korrelationskoeffizient nach Pearson beträgt 0.928; es besteht ein starker positiver linearer Zusammenhang zwischen Kampfzeit und Münzen.")

card("R-Output lesen (auch in Teil A)", 30,
 "<code>&gt; length(x)</code> 12 · <code>&gt; var(x)</code> 53.174 · <code>&gt; summary(x)</code>: Min 10, 1st Qu. 17.25, Median 23, Mean 22.08, 3rd Qu. 27.5, Max 33. Bestimmen Sie die empirische Varianz, den IQR und ob es Ausreißer gibt. <span class='pt'>(3 P)</span>",
 ["var in R = unverzerrt → · (n−1)/n.", "IQR = 3rd Qu. − 1st Qu.", "Grenzen = Quartile ∓ 1.5 · IQR, mit Min und Max vergleichen."],
 "s² = 53.174 · 11/12 = 48.743 · IQR = 27.5 − 17.25 = 10.25<br>Grenzen 1.875 und 42.875 → keine Ausreißer (Min 10, Max 33).")

card("Typische Fehler in R", 25,
 "Warum liefert <code>mean(d$Dauer)</code> NA bzw. einen Fehler? <span class='pt'>(1 P)</span>",
 ["NA in den Daten → na.rm = TRUE.", "„object not found“ → Name falsch geschrieben oder Objekt nicht erstellt.", "Zahlen als chr eingelesen → dec falsch gewählt.", "Nur 1 Spalte → sep falsch."],
 "Die Variable enthält fehlende Werte (NA). Lösung: <code>mean(d$Dauer, na.rm = TRUE)</code>.")

# =====================================================================
H = ['<section class="t1">',
     '<div class="fs-kopf"><h1>Rezeptbuch Tag 1 · im Klausurformat</h1>',
     '<p>Jede Karte: <b>Aufgabe</b> (wie in der Klausur) → <b>So löst du es</b> (Schritt für Schritt) → <b>Lösungskästchen</b> (genau das schreibst du hin) → <b>Vorsicht</b>.</p></div>',
     '<div class="legend"><b>Prozent-Zahl</b> = geschätzte Wahrscheinlichkeit, dass dieser Aufgabentyp in der Klausur vorkommt (nach Probeklausur 2022, Testaten 1–2, Tutorien 1–3). Nur eine Schätzung. '
     '<span class="ol hi">≥ 70 %</span> fast sicher · <span class="ol mid">30–69 %</span> häufig · <span class="ol lo">&lt; 30 %</span> manchmal.</div>']
for c in C:
    if c[0] == "SEC":
        H.append('<h2 class="rzh">%s</h2>' % c[1]); continue
    _, title, p, auf, steps, loes, warn, fig, bsp = c
    cl = "hi" if p >= 70 else "mid" if p >= 30 else "lo"
    s = ['<div class="rz"><div class="q"><span>%s</span><span class="ol %s">~%d %%</span></div><div class="b">' % (title, cl, p)]
    s.append('<div class="auf"><b>Aufgabe.</b> %s</div>' % auf)
    s.append('<div class="yap"><b class="l">So löst du es</b><ol>%s</ol></div>' % "".join("<li>%s</li>" % x for x in steps))
    s.append('<div class="lk2">%s</div>' % loes)
    if warn: s.append('<div class="dikkat">%s</div>' % warn)
    if fig: s.append('<div class="fig"><img src="fig/%s.svg" style="width:%s"></div>' % (fig, "95%" if fig == "rz_r5" else "70%"))
    s.append('</div></div>')
    H.append("\n".join(s))
H.append('<h2 class="rzh">Vor dem Abgeben</h2><div class="rz"><div class="q"><span>Checkliste für jede Aufgabe</span></div><div class="b"><div class="yap"><ol>'
         '<li>Jeden Teil der Frage beantwortet? („;“ und „und“ zählen)</li><li>„Begründen Sie“ → mit Zahlen begründen.</li><li>Ergebnis auf 3 Nachkommastellen oder gekürzter Bruch.</li></ol></div>'
         '<div class="yap"><ol start="4"><li>Plausibel? Anteil 0–1, Varianz ≥ 0, |r| ≤ 1, χ² ≥ 0.</li><li>Nur eine Lösung im Kästchen, Falsches durchgestrichen.</li><li>Kein Kästchen leer lassen.</li></ol></div></div></div>')
H.append("</section>")
open(os.path.join(os.path.dirname(__file__), "content", "rezept1.html"), "w", encoding="utf-8").write("\n".join(H))
print(sum(1 for c in C if c[0] == "CARD"), "Karten")
