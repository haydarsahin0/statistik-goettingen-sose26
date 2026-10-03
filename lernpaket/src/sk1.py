"""Abschnitte 0–2: Klausurregeln, Wahrscheinlichkeitsrechnung, Zufallsvariablen."""
from fractions import Fraction as Fr
import math
from itertools import product
from skcommon import sec, card, T, r3, r4, fr, log

# ======================================================================
sec("0 · So arbeitest du mit diesem Kurs",
    "Diese Regeln stehen in den offiziellen Klausurhinweisen. Wer sie verletzt, verliert Punkte – auch bei richtiger Rechnung.",
    ["<b>Runden:</b> Endergebnis auf <b>3</b> Nachkommastellen, Zwischenergebnisse mit mindestens <b>4</b>. Voll gekürzte Brüche sind auch erlaubt (z. B. \\(\\tfrac{19}{49}\\)). Ganze Zahlen und Ausdrücke wie \\(\\log 4\\) oder \\(\\sqrt 2\\) darfst du so stehen lassen.",
     "<b>Dezimalpunkt:</b> 0.375, nicht 0,375.",
     "<b>Nur ins Kästchen</b> kommt, was bewertet wird. Wird ein Lösungsweg verlangt („Geben Sie Ihren Lösungsweg an“), gehört der Weg <b>ins Kästchen</b>.",
     "<b>Nie zwei Lösungen</b> anbieten. Falsches sauber durchstreichen.",
     "<b>Nicht lösbar?</b> „nicht lösbar“ ins Kästchen und die Begründung in das Feld am Ende der Klausur.",
     "<b>Stift:</b> Kugelschreiber oder Tinte, nicht rot, nicht grün, kein Bleistift. Taschenrechner von der Positivliste."])

card("Ein Lösungskästchen richtig füllen", 100,
 "Berechnen Sie \\(P(A\\cup B)\\) für \\(P(A)=0.3\\), \\(P(B)=0.5\\), \\(P(A\\cap B)=0.2\\). Geben Sie Ihren Lösungsweg an. <span class='pt'>(2 P)</span>",
 ["Formel <b>allgemein</b> hinschreiben (1. Punkt ist oft schon für die richtige Formel).",
  "Zahlen einsetzen.", "Ergebnis ausrechnen und klar markieren."],
 "\\(P(A\\cup B)=P(A)+P(B)-P(A\\cap B)=0.3+0.5-0.2=\\mathbf{0.6}\\)",
 "Steht nur „Berechnen Sie“ ohne „Lösungsweg“, reicht das Ergebnis im Kästchen. Ein kurzer Weg schadet aber nie (Folgefehler werden dann eher anerkannt).")

# ======================================================================
sec("1 · Wahrscheinlichkeitsrechnung (V04)", None,
    ["<b>Ω</b> = Ergebnisraum (alle möglichen Ergebnisse). <b>Ereignis</b> = Teilmenge von Ω.",
     "<b>Laplace</b> (alle Ergebnisse gleich wahrscheinlich): \\(P(A)=\\frac{|A|}{|\\Omega|}\\) = günstige / mögliche.",
     "<b>Kolmogorov:</b> \\(P(A)\\ge0\\), \\(P(\\Omega)=1\\), bei disjunkten Ereignissen \\(P(A\\cup B)=P(A)+P(B)\\).",
     "<b>Regeln:</b> \\(P(\\bar A)=1-P(A)\\) · \\(P(A\\cup B)=P(A)+P(B)-P(A\\cap B)\\)", "<b>Differenz:</b> \\(P(A\\setminus B)=P(A\\cap\\bar B)=P(A)-P(A\\cap B)\\)",
     "<b>Bedingt:</b> \\(P(A|B)=\\frac{P(A\\cap B)}{P(B)}\\) · <b>Produktsatz:</b> \\(P(A\\cap B)=P(A|B)\\,P(B)=P(B|A)\\,P(A)\\).",
     "<b>Unabhängig</b> \\(\\Leftrightarrow P(A\\cap B)=P(A)\\,P(B)\\Leftrightarrow P(A|B)=P(A)\\). Ziehen <i>mit</i> Zurücklegen → unabhängig, <i>ohne</i> → abhängig.",
     "<b>Totale Wahrscheinlichkeit:</b> \\(P(B)=\\sum_i P(B|A_i)\\,P(A_i)\\) · <b>Bayes:</b> \\(P(A_j|B)=\\frac{P(B|A_j)\\,P(A_j)}{\\sum_i P(B|A_i)\\,P(A_i)}\\)."])

# --- 1.1 Text → Mengen
pA, pB, pAB = 0.5, 0.4, 0.15
weder = 1 - (pA + pB - pAB); genau1 = pA + pB - 2 * pAB
card("Text in Mengen-Sprache übersetzen", 70,
 "Für die Ereignisse A = „Kunde kauft Kaffee“ und B = „Kunde kauft Kuchen“ gilt \\(P(A)=0.5\\), \\(P(B)=0.4\\), \\(P(A\\cap B)=0.15\\). Berechnen Sie die Wahrscheinlichkeit, dass ein Kunde (i) weder Kaffee noch Kuchen kauft, (ii) genau eines von beiden kauft, (iii) Kaffee, aber keinen Kuchen kauft. <span class='pt'>(4 P)</span>",
 ["Übersetze zuerst die Wörter: <b>und</b> = ∩ · <b>oder</b> (mindestens eins) = ∪ · <b>nicht</b> = Strich (Komplement) · <b>aber nicht</b> = \\(A\\cap\\bar B\\) · <b>weder … noch</b> = \\(\\bar A\\cap\\bar B=\\overline{A\\cup B}\\).",
  "<b>Genau eines</b> = \\((A\\cap\\bar B)\\cup(\\bar A\\cap B)\\) = \\(P(A)+P(B)-2P(A\\cap B)\\).",
  "Venn-Diagramm skizzieren: Die vier Bereiche addieren sich zu 1."],
 T("(i) \\(P(\\bar A\\cap\\bar B)=1-P(A\\cup B)=1-(0.5+0.4-0.15)=\\mathbf{«w»}\\)<br>"
   "(ii) \\(P(\\text{genau eines})=0.5+0.4-2\\cdot0.15=\\mathbf{«g»}\\)<br>"
   "(iii) \\(P(A\\cap\\bar B)=P(A)-P(A\\cap B)=0.5-0.15=\\mathbf{0.35}\\)", w=r3(weder)[:-1], g=r3(genau1)[:-2]),
 "„Oder“ heißt in der Statistik immer „mindestens eines“ (also auch beide).", fig=("sk_venn.svg", 55))

# --- 1.2 Laplace Mengen und Mächtigkeit
Om = set(range(1, 11)); A = {2, 4, 6, 8, 10}; B = {1, 2, 3, 4}
nAnB = len(A - B); nAcuB = len((Om - A) | B); pAgBc = Fr(len(A - B), len(Om - B)); pAuB = Fr(len(A | B), 10)
card("Mengen und Mächtigkeiten im Laplace-Experiment", 60,
 "Gegeben ist das Laplace-Experiment \\(\\Omega=\\{1,2,\\dots,10\\}\\) mit \\(A=\\{2,4,6,8,10\\}\\) und \\(B=\\{1,2,3,4\\}\\). Berechnen Sie \\(|A\\cap\\bar B|\\), \\(|\\bar A\\cup B|\\), \\(P(A\\cup B)\\) sowie die Wahrscheinlichkeit, dass A eintritt, wenn B nicht eingetreten ist (mit korrekter Notation). <span class='pt'>(6 P)</span>",
 ["Komplement ausschreiben: \\(\\bar B=\\Omega\\setminus B\\) = alle Zahlen, die <b>nicht</b> in B sind.",
  "\\(|\\,\\cdot\\,|\\) = Anzahl der Elemente (Mächtigkeit), keine Wahrscheinlichkeit!",
  "Laplace: \\(P=\\) Anzahl / 10. Bedingt: Ω wird auf die Bedingung verkleinert → durch \\(|\\bar B|\\) teilen.",
  "„A, wenn B nicht eingetreten ist“ = \\(P(A\\,|\\,\\bar B)\\): Die Bedingung steht <b>rechts</b> vom Strich."],
 T("\\(\\bar B=\\{5,6,7,8,9,10\\}\\), \\(A\\cap\\bar B=\\{6,8,10\\}\\Rightarrow|A\\cap\\bar B|=\\mathbf{«a»}\\)<br>"
   "\\(\\bar A=\\{1,3,5,7,9\\}\\), \\(\\bar A\\cup B=\\{1,2,3,4,5,7,9\\}\\Rightarrow|\\bar A\\cup B|=\\mathbf{«b»}\\)<br>"
   "\\(A\\cup B=\\{1,2,3,4,6,8,10\\}\\Rightarrow P(A\\cup B)=\\frac{7}{10}=\\mathbf{0.7}\\)<br>"
   "\\(P(A\\,|\\,\\bar B)=\\frac{|A\\cap\\bar B|}{|\\bar B|}=\\frac{3}{6}=\\mathbf{0.5}\\)", a=nAnB, b=nAcuB),
 "Probeklausur 2022 (Aufgabe 4) war genau dieser Typ: 6 Punkte für Abzählen. Sorgfältig auflisten!")
assert nAnB == 3 and nAcuB == 7 and pAgBc == Fr(1, 2) and pAuB == Fr(7, 10)

# --- 1.3 zwei Würfel
pairs = list(product(range(1, 7), repeat=2))
p8 = Fr(sum(a + b == 8 for a, b in pairs), 36); p10 = Fr(sum(a + b >= 10 for a, b in pairs), 36); pp = Fr(sum(a == b for a, b in pairs), 36)
card("Zwei Würfel: Abzählen mit 36 Paaren", 45,
 "Zwei faire Würfel werden geworfen. Berechnen Sie die Wahrscheinlichkeit, dass (i) die Augensumme 8 beträgt, (ii) die Augensumme mindestens 10 beträgt, (iii) ein Pasch fällt. <span class='pt'>(3 P)</span>",
 ["Ω hat \\(6\\cdot6=36\\) gleich wahrscheinliche <b>geordnete</b> Paare: (2,6) und (6,2) sind verschieden!",
  "Günstige Paare auflisten und zählen, dann durch 36 teilen."],
 T("(i) Summe 8: (2,6),(3,5),(4,4),(5,3),(6,2) → \\(\\frac{5}{36}=\\mathbf{«a»}\\)<br>"
   "(ii) Summe ≥ 10: (4,6),(5,5),(6,4),(5,6),(6,5),(6,6) → \\(\\frac{6}{36}=\\frac16=\\mathbf{«b»}\\)<br>"
   "(iii) Pasch: (1,1),…,(6,6) → \\(\\frac{6}{36}=\\mathbf{«c»}\\)", a=r3(float(p8)), b=r3(float(p10)), c=r3(float(pp))),
 "Häufigster Fehler: (3,5) und (5,3) nur einmal zählen. Bei Würfeln immer mit Reihenfolge zählen.")

# --- 1.4 Rechenregeln + Unabhängigkeit
card("Rechenregeln: fehlende Wahrscheinlichkeiten finden", 55,
 "Es gilt \\(P(A\\cup B)=0.7\\), \\(P(A)=0.4\\), \\(P(B)=0.5\\). Berechnen Sie \\(P(A\\cap B)\\), \\(P(A\\setminus B)\\), \\(P(\\bar A\\cap\\bar B)\\) und \\(P(B|A)\\). Sind A und B unabhängig? <span class='pt'>(5 P)</span>",
 ["Additionssatz nach dem Unbekannten umstellen: \\(P(A\\cap B)=P(A)+P(B)-P(A\\cup B)\\).",
  "\\(P(A\\setminus B)=P(A)-P(A\\cap B)\\).", "\\(P(\\bar A\\cap\\bar B)=1-P(A\\cup B)\\).",
  "Unabhängigkeit: Vergleiche \\(P(A\\cap B)\\) mit \\(P(A)\\cdot P(B)\\)."],
 "\\(P(A\\cap B)=0.4+0.5-0.7=\\mathbf{0.2}\\)<br>\\(P(A\\setminus B)=0.4-0.2=\\mathbf{0.2}\\)<br>\\(P(\\bar A\\cap\\bar B)=1-0.7=\\mathbf{0.3}\\)<br>"
 "\\(P(B|A)=\\frac{0.2}{0.4}=\\mathbf{0.5}\\)<br>\\(P(A)\\cdot P(B)=0.4\\cdot0.5=0.2=P(A\\cap B)\\) → A und B sind <b>stochastisch unabhängig</b> (auch: \\(P(B|A)=0.5=P(B)\\)).",
 "Unabhängig ≠ disjunkt! Disjunkte Ereignisse mit positiver Wahrscheinlichkeit sind sogar immer <b>abhängig</b> (\\(P(A\\cap B)=0\\neq P(A)P(B)\\)).")

# --- 1.5 bedingte W'keit Testat-Typ
pA, pB, pAgB = 0.3, 0.5, 0.4
pAB = pAgB * pB; pAuB = pA + pB - pAB; pAgBc = (pA - pAB) / (1 - pB); pBgA = pAB / pA
card("Bedingte Wahrscheinlichkeit und Komplement", 65,
 "Es gilt \\(P(A)=0.3\\), \\(P(B)=0.5\\) und \\(P(A|B)=0.4\\). Bestimmen Sie \\(P(A\\cup B)\\), \\(P(A|\\bar B)\\) und \\(P(B|A)\\). <span class='pt'>(4 P)</span>",
 ["Fast immer zuerst den <b>Schnitt</b> holen: \\(P(A\\cap B)=P(A|B)\\cdot P(B)\\).",
  "\\(P(A|\\bar B)=\\frac{P(A\\cap\\bar B)}{P(\\bar B)}=\\frac{P(A)-P(A\\cap B)}{1-P(B)}\\).",
  "\\(P(B|A)\\) ist <b>nicht</b> \\(P(A|B)\\): andere Bedingung, anderer Nenner."],
 T("\\(P(A\\cap B)=0.4\\cdot0.5=0.2\\)<br>\\(P(A\\cup B)=0.3+0.5-0.2=\\mathbf{«u»}\\)<br>"
   "\\(P(A|\\bar B)=\\frac{0.3-0.2}{1-0.5}=\\frac{0.1}{0.5}=\\mathbf{«c»}\\)<br>\\(P(B|A)=\\frac{0.2}{0.3}=\\frac23=\\mathbf{«d»}\\)",
   u=r3(pAuB)[:-2], c=r3(pAgBc)[:-2], d=r3(pBgA)),
 "Testat 3 hatte genau diesen Aufbau. Das Werkzeug ist immer: Schnitt → dann alles andere.")

# --- 1.6 Unabhängigkeit prüfen Glücksrad
Om = set(range(1, 11)); A = {1, 2, 3, 4}; B = {2, 4, 6, 8, 10}; Cc = {1, 5, 9}
P = lambda S: Fr(len(S), 10)
assert P(A & B) == P(A) * P(B) and P(A & Cc) != P(A) * P(Cc)
card("Unabhängigkeit von Ereignissen prüfen", 60,
 "Ein Glücksrad hat die Felder 1 bis 10 (Laplace). Es seien \\(A=\\{1,2,3,4\\}\\), \\(B=\\{2,4,6,8,10\\}\\), \\(C=\\{1,5,9\\}\\). Berechnen Sie \\(P(A\\cup C)\\) und \\(P(A|B)\\). Sind A und B unabhängig? Sind A und C unabhängig? <span class='pt'>(5 P)</span>",
 ["Schnittmengen auflisten.", "Unabhängig ⇔ \\(P(A\\cap B)=P(A)\\cdot P(B)\\). <b>Beide Seiten ausrechnen und vergleichen</b>, dann einen Satz schreiben."],
 "\\(A\\cup C=\\{1,2,3,4,5,9\\}\\Rightarrow P(A\\cup C)=\\mathbf{0.6}\\)<br>"
 "\\(A\\cap B=\\{2,4\\}\\Rightarrow P(A|B)=\\frac{0.2}{0.5}=\\mathbf{0.4}\\)<br>"
 "A, B: \\(P(A\\cap B)=0.2=0.4\\cdot0.5=P(A)P(B)\\) → <b>unabhängig</b>.<br>"
 "A, C: \\(P(A\\cap C)=P(\\{1\\})=0.1\\neq0.4\\cdot0.3=0.12\\) → <b>abhängig</b>.")

# --- 1.7 totale Wahrscheinlichkeit
pAi = [0.5, 0.3, 0.2]; pV = [0.1, 0.2, 0.05]
pVtot = sum(a * b for a, b in zip(pAi, pV)); log("P(V) Lieferdienst", pVtot)
card("Satz der totalen Wahrscheinlichkeit (mit fehlendem Anteil)", 80,
 "Ein Lieferdienst hat drei Fahrer. Fahrer 1 liefert 50 %, Fahrer 2 30 % der Bestellungen, den Rest liefert Fahrer 3. Die Verspätungswahrscheinlichkeiten sind 0.1 (Fahrer 1), 0.2 (Fahrer 2) und 0.05 (Fahrer 3). Wie groß ist die Wahrscheinlichkeit, dass eine zufällige Bestellung verspätet ist? <span class='pt'>(4 P)</span>",
 ["Ereignisse benennen: \\(A_i\\) = „Fahrer i liefert“, V = „verspätet“.",
  "Gegebene Zahlen sauber zuordnen: Prozent der Bestellungen = \\(P(A_i)\\); „Verspätung, <b>wenn</b> Fahrer i“ = \\(P(V|A_i)\\).",
  "Fehlenden Anteil über Komplement: \\(P(A_3)=1-0.5-0.3\\).",
  "Formel: \\(P(V)=\\sum P(V|A_i)P(A_i)\\) – oder Baumdiagramm: Pfade multiplizieren, Pfade zu V addieren."],
 T("\\(P(A_3)=1-0.5-0.3=0.2\\)<br>\\(P(V)=P(V|A_1)P(A_1)+P(V|A_2)P(A_2)+P(V|A_3)P(A_3)\\)<br>"
   "\\(=0.1\\cdot0.5+0.2\\cdot0.3+0.05\\cdot0.2=0.05+0.06+0.01=\\mathbf{«v»}\\)", v=r3(pVtot)[:-1]),
 "Die \\(A_i\\) müssen eine <b>disjunkte Zerlegung</b> von Ω sein (jede Bestellung genau ein Fahrer). Dann summieren sich die \\(P(A_i)\\) zu 1.",
 fig=("sk_baum.svg", 70))

# --- 1.8 Bayes
pA2gV = 0.2 * 0.3 / pVtot; pA1gVc = 0.9 * 0.5 / (1 - pVtot)
card("Satz von Bayes: Rückschluss auf die Ursache", 85,
 "(Fortsetzung) Eine Bestellung kommt verspätet an. Mit welcher Wahrscheinlichkeit wurde sie von Fahrer 2 geliefert? Mit welcher Wahrscheinlichkeit stammt eine <i>pünktliche</i> Bestellung von Fahrer 1? <span class='pt'>(4 P)</span>",
 ["Gesucht ist die <b>umgedrehte</b> Bedingung: gegeben \\(P(V|A_2)\\), gesucht \\(P(A_2|V)\\).",
  "Bayes: \\(P(A_2|V)=\\frac{P(V|A_2)\\,P(A_2)}{P(V)}\\). Zähler = ein Pfad, Nenner = alle Pfade zu V.",
  "Für „pünktlich“: \\(P(\\bar V|A_1)=1-0.1=0.9\\) und \\(P(\\bar V)=1-P(V)\\)."],
 T("\\(P(A_2|V)=\\frac{0.2\\cdot0.3}{0.12}=\\frac{0.06}{0.12}=\\mathbf{«a»}\\)<br>"
   "\\(P(A_1|\\bar V)=\\frac{P(\\bar V|A_1)P(A_1)}{P(\\bar V)}=\\frac{0.9\\cdot0.5}{0.88}=\\mathbf{«b»}\\)", a=r3(pA2gV)[:-2], b=r3(pA1gVc)),
 "Interpretation als Satz: „Eine verspätete Bestellung stammt mit Wahrscheinlichkeit 0.5 von Fahrer 2.“ Obwohl Fahrer 2 nur 30 % liefert, verursacht er die Hälfte der Verspätungen.")

# --- 1.9 Probeklausur-Typ: bedingte W'keiten gegeben B und nicht B
PB = 0.6; s_B = [0.7, 0.2]; s_nB = [0.2, 0.3]
s3B = 1 - sum(s_B); s3nB = 1 - sum(s_nB); PS3 = s3B * PB + s3nB * (1 - PB)
PS2 = s_B[1] * PB + s_nB[1] * (1 - PB); PBgS2 = s_B[1] * PB / PS2
pmind = 1 - PB ** 8
log("PS3", PS3); log("PB|S2", PBgS2); log("mind 1 nicht bestanden", pmind)
card("Bayes im Probeklausur-Format (Lernstrategien)", 75,
 "Eine Klausur wird mit Wahrscheinlichkeit 0.6 bestanden (B). Unter den Bestehenden lernen 70 % regelmäßig (\\(S_1\\)), 20 % nur mit Videos (\\(S_2\\)), der Rest gar nicht (\\(S_3\\)). Unter den Nicht-Bestehenden sind es 20 % (\\(S_1\\)) und 30 % (\\(S_2\\)), der Rest \\(S_3\\). Berechnen Sie (a) \\(P(\\bar B)\\), \\(P(S_3|B)\\), \\(P(S_3|\\bar B)\\) und \\(P(S_3)\\), (b) die Bestehenswahrscheinlichkeit einer Person mit Strategie \\(S_2\\), (c) die Wahrscheinlichkeit, dass unter 8 unabhängig befragten Personen mindestens eine nicht bestanden hat. <span class='pt'>(11 P)</span>",
 ["Achtung, die Richtung: „Unter den Bestehenden lernen 70 % regelmäßig“ = \\(P(S_1|B)=0.7\\) (nicht \\(P(B|S_1)\\)!).",
  "Rest über das Komplement innerhalb derselben Bedingung: \\(P(S_3|B)=1-P(S_1|B)-P(S_2|B)\\).",
  "\\(P(S_3)\\) mit totaler Wahrscheinlichkeit über B und \\(\\bar B\\).",
  "(b) ist Bayes: \\(P(B|S_2)=\\frac{P(S_2|B)P(B)}{P(S_2)}\\).",
  "(c) „mindestens eine“ → Gegenereignis „keine“: \\(1-P(\\text{alle bestanden})=1-0.6^8\\)."],
 T("(a) \\(P(\\bar B)=1-0.6=\\mathbf{0.4}\\)<br>\\(P(S_3|B)=1-0.7-0.2=\\mathbf{0.1}\\) · \\(P(S_3|\\bar B)=1-0.2-0.3=\\mathbf{0.5}\\)<br>"
   "\\(P(S_3)=0.1\\cdot0.6+0.5\\cdot0.4=0.06+0.2=\\mathbf{«s3»}\\)<br>"
   "(b) \\(P(S_2)=0.2\\cdot0.6+0.3\\cdot0.4=0.24\\) → \\(P(B|S_2)=\\frac{0.2\\cdot0.6}{0.24}=\\mathbf{«b»}\\)<br>"
   "(c) X = Anzahl Nicht-Besteher, \\(X\\sim B(8;\\,0.4)\\): \\(P(X\\ge1)=1-P(X=0)=1-0.6^8=\\mathbf{«c»}\\)",
   s3=r3(PS3)[:-1], b=r3(PBgS2)[:-2], c=r3(pmind)),
 "In der Probeklausur 2022 brachte genau dieser Typ 11 Punkte (Aufgabe 3). Trick in (c): „Vereinfachen Sie so weit wie möglich“ → \\(\\binom{8}{0}0.4^0\\,0.6^8=0.6^8\\).")

# --- 1.10 Medizinischer Test, natürliche Häufigkeiten
prev, sens, spez = 0.02, 0.95, 0.90
pT = sens * prev + (1 - spez) * (1 - prev); pKgT = sens * prev / pT; pGgN = spez * (1 - prev) / (1 - pT)
log("P(T+)", pT); log("P(K|T+)", pKgT); log("P(G|T-)", pGgN)
card("Medizinischer Test: Sensitivität, Spezifität, Prävalenz", 55,
 "Eine Krankheit hat eine Prävalenz von 2 %. Ein Test erkennt Kranke mit Wahrscheinlichkeit 0.95 (Sensitivität) und ist bei Gesunden mit Wahrscheinlichkeit 0.90 negativ (Spezifität). Berechnen Sie die Wahrscheinlichkeit eines positiven Tests und die Wahrscheinlichkeit, bei positivem Test krank zu sein. Interpretieren Sie. <span class='pt'>(5 P)</span>",
 ["Übersetzen: K = krank, T = Test positiv. Prävalenz = \\(P(K)\\), Sensitivität = \\(P(T|K)\\), Spezifität = \\(P(\\bar T|\\bar K)\\) → \\(P(T|\\bar K)=1-0.9=0.1\\).",
  "Totale W'keit für \\(P(T)\\), dann Bayes für \\(P(K|T)\\).",
  "Kontrolle mit 10 000 Personen: 200 krank → 190 positiv; 9 800 gesund → 980 positiv. Von 1 170 Positiven sind 190 krank."],
 T("\\(P(T)=0.95\\cdot0.02+0.1\\cdot0.98=0.019+0.098=\\mathbf{«t»}\\)<br>"
   "\\(P(K|T)=\\frac{0.95\\cdot0.02}{0.117}=\\frac{0.019}{0.117}=\\mathbf{«k»}\\)<br>"
   "Nur etwa 16 % der positiv Getesteten sind wirklich krank. Grund: Die Krankheit ist selten, deshalb gibt es viel mehr falsch Positive (980) als richtig Positive (190).",
   t=r3(pT), k=r3(pKgT)),
 "Das Ergebnis hängt stark von der Prävalenz ab (V04, Folie 36). Bei P(K|T) immer an die vielen Gesunden denken.")

# --- 1.11 Ziehen ohne Zurücklegen
p1 = Fr(10, 20); p2 = Fr(4, 20) * Fr(6, 19); pmit = Fr(4, 20) * Fr(6, 20)
card("Ziehen ohne Zurücklegen (Kugeln)", 45,
 "In einer Kiste liegen 10 rote, 6 blaue und 4 gelbe Kugeln. Es wird ohne Zurücklegen gezogen. Rot: verloren, Spielende. Blau: gewonnen, Spielende. Gelb: noch einmal ziehen. Wie groß ist die Wahrscheinlichkeit, (i) mit dem ersten Zug zu verlieren, (ii) mit dem zweiten Zug zu gewinnen? <span class='pt'>(4 P)</span>",
 ["Erster Zug: Laplace mit 20 Kugeln.",
  "„Im zweiten Zug gewinnen“ heißt: <b>erst gelb, dann blau</b> → Produktsatz \\(P(G_1\\cap B_2)=P(G_1)\\cdot P(B_2|G_1)\\).",
  "Ohne Zurücklegen: Beim zweiten Zug sind nur noch 19 Kugeln da (6 blaue)."],
 T("(i) \\(P(R_1)=\\frac{10}{20}=\\mathbf{0.5}\\)<br>(ii) \\(P(G_1\\cap B_2)=\\frac{4}{20}\\cdot\\frac{6}{19}=\\frac{24}{380}=\\frac{6}{95}=\\mathbf{«b»}\\)",
   b=r3(float(p2))),
 T("Mit Zurücklegen wäre es \\(\\frac{4}{20}\\cdot\\frac{6}{20}=«m»\\). Lies genau, ob zurückgelegt wird.", m=r3(float(pmit))[:-1]))

# --- 1.12 mindestens einer
q = 1 - 0.95 ** 12; genau = 12 * 0.05 * 0.95 ** 11
card("„Mindestens einer“ über das Gegenereignis", 60,
 "Ein Gerät besteht aus 12 Bauteilen, die unabhängig voneinander mit Wahrscheinlichkeit 0.05 ausfallen. Wie groß ist die Wahrscheinlichkeit, dass mindestens ein Bauteil ausfällt? Und genau eines? <span class='pt'>(3 P)</span>",
 ["„Mindestens eins“ hat viele Fälle (1, 2, …, 12). Das Gegenereignis „keins“ hat nur einen Fall.",
  "\\(P(\\text{mind. 1})=1-P(\\text{keins})=1-0.95^{12}\\) (Unabhängigkeit → multiplizieren).",
  "„Genau eins“: welches der 12 Teile ausfällt, ist egal → 12 Möglichkeiten (Binomialverteilung)."],
 T("\\(P(X\\ge1)=1-0.95^{12}=1-0.5404=\\mathbf{«a»}\\)<br>\\(P(X=1)=\\binom{12}{1}\\,0.05\\cdot0.95^{11}=\\mathbf{«b»}\\)", a=r3(q), b=r3(genau)))

# --- 1.13 Fehlinterpretation
PI = 0.05; pGgI = 0.5; pG = 0.8
pIgG = pGgI * PI / pG; pIgNG = (1 - pGgI) * PI / (1 - pG)
card("Fehlinterpretation: P(A|B) mit P(B|A) verwechselt", 30,
 "80 % einer Bevölkerung sind geimpft (G). 5 % sind infiziert (I). Unter den Infizierten ist die Hälfte geimpft. Eine Zeitung schreibt: „Die Impfung schützt nicht, denn die Hälfte der Infizierten ist geimpft.“ Berechnen Sie \\(P(I|G)\\) und \\(P(I|\\bar G)\\) und beurteilen Sie die Aussage. <span class='pt'>(4 P)</span>",
 ["Gegeben ist \\(P(G|I)=0.5\\) – das ist <b>nicht</b> das Infektionsrisiko der Geimpften.",
  "Bayes: \\(P(I|G)=\\frac{P(G|I)P(I)}{P(G)}\\), analog für \\(\\bar G\\)."],
 T("\\(P(I|G)=\\frac{0.5\\cdot0.05}{0.8}=\\mathbf{«a»}\\) · \\(P(I|\\bar G)=\\frac{0.5\\cdot0.05}{0.2}=\\mathbf{«b»}\\)<br>"
   "Die Aussage ist falsch: Ungeimpfte infizieren sich viermal so häufig. Dass die Hälfte der Infizierten geimpft ist, liegt daran, dass es viel mehr Geimpfte gibt.",
   a=r3(pIgG), b=r3(pIgNG)),
 "Tutorium 5 (Impf-Grafik) behandelt genau diese Verwechslung. Immer fragen: Wer ist die Bezugsgruppe (rechts vom Strich)?")

# ======================================================================
sec("2 · Zufallsvariablen: Verteilung, Erwartungswert, Varianz (V05–V06)", None,
    ["<b>Zufallsvariable X</b> ordnet jedem Ergebnis eine Zahl zu. <b>Träger</b> T = mögliche Werte.",
     "<b>Diskret:</b> Wahrscheinlichkeitsfunktion \\(P(X=x)\\), alle Werte ≥ 0, Summe = 1. <b>Stetig:</b> Dichte \\(f(x)\\ge0\\), \\(\\int f=1\\), \\(P(X=x)=0\\), \\(f(x)>1\\) ist erlaubt.",
     "<b>Verteilungsfunktion</b> \\(F(x)=P(X\\le x)\\): \\(P(a<X\\le b)=F(b)-F(a)\\), \\(P(X>a)=1-F(a)\\). Diskret: Treppe. Stetig: \\(F(x)=\\int_{-\\infty}^x f(t)\\,dt\\).",
     "<b>Erwartungswert:</b> \\(E(X)=\\sum x\\,P(X=x)\\) bzw. \\(\\int x f(x)\\,dx\\). \\(E(g(X))=\\sum g(x)P(X=x)\\) – aber im Allgemeinen \\(E(g(X))\\neq g(E(X))\\).",
     "<b>Varianz:</b> \\(Var(X)=E(X^2)-(E(X))^2\\) (Verschiebungssatz), \\(sd(X)=\\sqrt{Var(X)}\\).",
     "<b>Rechenregeln:</b> \\(E(aX+b)=aE(X)+b\\) · \\(Var(aX+b)=a^2Var(X)\\) · \\(E(X+Y)=E(X)+E(Y)\\) immer · \\(Var(aX+bY)=a^2Var(X)+b^2Var(Y)+2ab\\,Cov(X,Y)\\); bei Unabhängigkeit ist \\(Cov=0\\).",
     "<b>Zwei ZV:</b> Rand \\(P(X=x)=\\sum_y P(X=x,Y=y)\\) · bedingt \\(P(X=x|Y=y)=\\frac{P(X=x,Y=y)}{P(Y=y)}\\) · \\(Cov(X,Y)=E(XY)-E(X)E(Y)\\) · \\(\\rho=\\frac{Cov}{sd(X)\\,sd(Y)}\\). Unabhängig ⇒ unkorreliert (nicht umgekehrt)."])

# --- 2.1 W-Funktion aufstellen
card("Wahrscheinlichkeitsfunktion und Träger aufstellen", 55,
 "Bei einem Spiel zahlen Sie 2 € Einsatz und würfeln einmal mit einem fairen Würfel. Sie bekommen die Augenzahl in Euro ausgezahlt. X sei Ihr Gewinn. Geben Sie den Träger und die Wahrscheinlichkeitsfunktion von X an. Berechnen Sie \\(E(X)\\) und \\(P(X>0)\\). <span class='pt'>(5 P)</span>",
 ["Gewinn = Auszahlung − Einsatz → \\(X=\\text{Augenzahl}-2\\).", "Träger = alle möglichen Werte von X.",
  "Wahrscheinlichkeitsfunktion <b>vollständig</b> hinschreiben, mit „0 sonst“.",
  "\\(E(X)=E(\\text{Augenzahl})-2=3.5-2\\) (lineare Transformation)."],
 "\\(T_X=\\{-1,0,1,2,3,4\\}\\)<br>\\(P(X=x)=\\begin{cases}\\frac16 & x\\in\\{-1,0,1,2,3,4\\}\\\\0&\\text{sonst}\\end{cases}\\)<br>"
 "\\(E(X)=3.5-2=\\mathbf{1.5}\\) · \\(P(X>0)=P(X\\in\\{1,2,3,4\\})=\\frac46=\\mathbf{0.667}\\)",
 "„0 sonst“ vergessen kostet in Tutorium-Lösungen ausdrücklich Punkte. Der Gewinn des Spielleiters ist \\(Y=-X\\), Träger \\(\\{-4,\\dots,1\\}\\).")

# --- 2.2 Konstante c (diskret) + E + Var mit Brüchen
c = Fr(1, 14); EX = sum(c * x ** 2 * x for x in (1, 2, 3)); EX2 = sum(c * x ** 2 * x ** 2 for x in (1, 2, 3)); V = EX2 - EX ** 2
assert c * 14 == 1 and EX == Fr(18, 7) and EX2 == 7 and V == Fr(19, 49)
card("Konstante c bestimmen, dann E(X) und Var(X)", 65,
 "Für eine Zufallsvariable X gilt \\(P(X=x)=c\\cdot x^2\\) für \\(x\\in\\{1,2,3\\}\\) und 0 sonst. (a) Bestimmen Sie c. (b) Berechnen Sie \\(E(X)\\) und \\(Var(X)\\). <span class='pt'>(6 P)</span>",
 ["(a) Alle Wahrscheinlichkeiten müssen sich zu 1 addieren: \\(c\\cdot1+c\\cdot4+c\\cdot9=1\\).",
  "(b) Tabelle mit Spalten x, P, x·P, x²·P anlegen und Spalten summieren.",
  "Varianz mit Verschiebungssatz \\(E(X^2)-(E(X))^2\\). Mit Brüchen rechnen ist hier am genauesten."],
 T("(a) \\(14c=1\\Rightarrow c=\\frac1{14}\\)<br>(b) \\(E(X)=\\frac{1\\cdot1+4\\cdot2+9\\cdot3}{14}=\\frac{36}{14}=\\frac{18}{7}=\\mathbf{«e»}\\)<br>"
   "\\(E(X^2)=\\frac{1+16+81}{14}=\\frac{98}{14}=7\\)<br>\\(Var(X)=7-\\left(\\frac{18}{7}\\right)^2=\\frac{343-324}{49}=\\frac{19}{49}=\\mathbf{«v»}\\)",
   e=r3(float(EX)), v=r3(float(V))),
 "Auch bei \\(P(X=x)=x/c\\) (Tutorium 6) gilt: Summe = 1 nach c auflösen.")

# --- 2.3 E/Var aus Tabelle + 2.4 Wahrscheinlichkeiten aus F
xs = [0, 1, 2, 4]; ps = [0.1, 0.3, 0.4, 0.2]
E = sum(x * p for x, p in zip(xs, ps)); E2 = sum(x * x * p for x, p in zip(xs, ps)); Vv = E2 - E * E
card("Erwartungswert und Varianz aus einer Tabelle", 85,
 "Die Zufallsvariable X (Anzahl Reklamationen pro Tag) hat die Wahrscheinlichkeitsfunktion \\(P(X=0)=0.1\\), \\(P(X=1)=0.3\\), \\(P(X=2)=0.4\\), \\(P(X=4)=0.2\\). Berechnen Sie \\(E(X)\\), \\(Var(X)\\) und \\(sd(X)\\). <span class='pt'>(4 P)</span>",
 ["\\(E(X)=\\sum x\\cdot P(X=x)\\).", "\\(E(X^2)=\\sum x^2\\cdot P(X=x)\\) – die Wahrscheinlichkeiten werden <b>nicht</b> quadriert!",
  "\\(Var=E(X^2)-E(X)^2\\), \\(sd=\\sqrt{Var}\\)."],
 T("\\(E(X)=0\\cdot0.1+1\\cdot0.3+2\\cdot0.4+4\\cdot0.2=\\mathbf{«e»}\\)<br>\\(E(X^2)=0+0.3+1.6+3.2=5.1\\)<br>"
   "\\(Var(X)=5.1-1.9^2=\\mathbf{«v»}\\) · \\(sd(X)=\\sqrt{1.49}=\\mathbf{«s»}\\)", e="1.9", v="1.49", s=r3(math.sqrt(Vv))),
 "Plausibilitätscheck: Var ≥ 0 und E(X) liegt zwischen kleinstem und größtem Wert.")
assert abs(E - 1.9) < 1e-12 and abs(Vv - 1.49) < 1e-12

card("Wahrscheinlichkeiten mit der Verteilungsfunktion (diskret)", 70,
 "(Fortsetzung) Geben Sie die Verteilungsfunktion F(x) an und berechnen Sie \\(P(X\\le1)\\), \\(P(X<2)\\), \\(P(X\\ge2)\\), \\(P(1<X\\le4)\\) und \\(P(X=3)\\). <span class='pt'>(6 P)</span>",
 ["F kumuliert die Wahrscheinlichkeiten: 0.1, 0.4, 0.8, 1. Zwischen den Werten bleibt F konstant (Treppe).",
  "<b>Diskret ist &lt; nicht dasselbe wie ≤:</b> \\(P(X<2)=P(X\\le1)\\), \\(P(X\\ge2)=1-P(X\\le1)\\).",
  "\\(P(a<X\\le b)=F(b)-F(a)\\)."],
 "\\(F(x)=\\begin{cases}0&x<0\\\\0.1&0\\le x<1\\\\0.4&1\\le x<2\\\\0.8&2\\le x<4\\\\1&x\\ge4\\end{cases}\\)<br>"
 "\\(P(X\\le1)=\\mathbf{0.4}\\) · \\(P(X<2)=F(1)=\\mathbf{0.4}\\) · \\(P(X\\ge2)=1-F(1)=\\mathbf{0.6}\\)<br>"
 "\\(P(1<X\\le4)=F(4)-F(1)=\\mathbf{0.6}\\) · \\(P(X=3)=\\mathbf{0}\\) (3 liegt nicht im Träger)",
 "Skizze: ● am linken Ende jeder Stufe (gehört dazu), ○ am rechten Ende, keine senkrechten Linien.", fig=("sk_Fdisk.svg", 55))

# --- 2.5 E(g(X))
EX = 0.3 * 1 + 0.5 * 2 + 0.2 * 3; Elog = 0.5 * math.log(2) + 0.2 * math.log(3); Einv = 0.3 + 0.5 / 2 + 0.2 / 3
card("Verteilungsfunktion lesen und E(g(X)) berechnen", 55,
 "X nimmt die Werte 1, 2, 3 an. Es gilt \\(F(x)=0\\) für \\(x<1\\), \\(F(x)=0.3\\) für \\(1\\le x<2\\), \\(F(x)=?\\) für \\(2\\le x<3\\) und \\(F(x)=1\\) für \\(x\\ge3\\), außerdem \\(P(X=2)=0.5\\). Ergänzen Sie das „?“, und bestimmen Sie \\(E(X)\\) und \\(E(Y)\\) für \\(Y=\\log(X)\\). <span class='pt'>(5 P)</span>",
 ["Sprunghöhe der Treppe = Wahrscheinlichkeit: \\(P(X=1)=0.3\\), dann \\(F(2)=0.3+0.5\\), \\(P(X=3)=1-F(2)\\).",
  "\\(E(\\log X)=\\sum\\log(x)\\,P(X=x)\\) – <b>nicht</b> \\(\\log(E(X))\\).", "log = natürlicher Logarithmus (ln), \\(\\log1=0\\)."],
 T("\\(?=F(2)=0.3+0.5=\\mathbf{0.8}\\), \\(P(X=3)=0.2\\)<br>\\(E(X)=1\\cdot0.3+2\\cdot0.5+3\\cdot0.2=\\mathbf{«e»}\\)<br>"
   "\\(E(\\log X)=0\\cdot0.3+\\log2\\cdot0.5+\\log3\\cdot0.2=\\mathbf{«l»}\\)  (zum Vergleich \\(\\log(1.9)=«lg»\\))",
   e="1.9", l=r3(Elog), lg=r3(math.log(1.9))),
 "So sieht Testat 4, Aufgabe 1 aus. Der Vergleich zeigt: \\(E(g(X))\\neq g(E(X))\\).")

# --- 2.6 Dichte: c bestimmen, E, Var (stetig)
card("Stetige Dichte: c bestimmen und prüfen", 70,
 "X habe die Dichte \\(f(x)=c\\,(x-2)\\) für \\(2\\le x\\le3\\) und 0 sonst. Bestimmen Sie c so, dass f eine gültige Dichte ist, und begründen Sie, dass f dann alle Eigenschaften einer Dichte erfüllt. <span class='pt'>(4 P)</span>",
 ["Bedingung 1: \\(\\int_{-\\infty}^{\\infty}f(x)\\,dx=1\\). Außerhalb von [2, 3] ist f = 0 → nur von 2 bis 3 integrieren.",
  "Stammfunktion von \\(x-2\\) ist \\(\\tfrac{x^2}{2}-2x\\) (oder \\(\\tfrac{(x-2)^2}{2}\\)).",
  "Bedingung 2: \\(f(x)\\ge0\\) für alle x. Prüfen: für \\(x\\in[2,3]\\) ist \\(x-2\\ge0\\) und \\(c>0\\)."],
 "\\(\\int_2^3c(x-2)\\,dx=c\\left[\\tfrac{(x-2)^2}{2}\\right]_2^3=c\\cdot\\tfrac12\\overset{!}{=}1\\Rightarrow c=\\mathbf{2}\\)<br>"
 "\\(f(x)=2(x-2)\\ge0\\) auf [2, 3] und 0 sonst → nicht negativ und Fläche 1 → gültige Dichte.",
 "Testat 4 fragte nach den Eigenschaften einer Dichte. Richtig sind nur \\(\\int f=1\\) und \\(f\\ge0\\). Falsch sind \\(f\\le1\\), \\(P(X=x)=f(x)\\) und „stetig und monoton“.",
 fig=("sk_dichte.svg", 55))

EX = Fr(8, 3); EX2 = Fr(43, 6); Vd = EX2 - EX ** 2
assert Vd == Fr(1, 18)
card("Stetige Zufallsvariable: E(X) und Var(X) per Integral", 70,
 "(Fortsetzung, \\(f(x)=2(x-2)\\) auf [2, 3]) Berechnen Sie \\(E(X)\\), \\(E(X^2)\\) und \\(Var(X)\\). <span class='pt'>(5 P)</span>",
 ["\\(E(X)=\\int x\\,f(x)\\,dx=\\int_2^3(2x^2-4x)\\,dx\\). Erst ausmultiplizieren, dann integrieren.",
  "\\(E(X^2)=\\int_2^3x^2\\cdot2(x-2)\\,dx=\\int_2^3(2x^3-4x^2)\\,dx\\).",
  "Obere minus untere Grenze; Klammern setzen (Minus-Fehler!)."],
 T("\\(E(X)=\\left[\\tfrac23x^3-2x^2\\right]_2^3=(18-18)-(\\tfrac{16}{3}-8)=\\tfrac83=\\mathbf{«e»}\\)<br>"
   "\\(E(X^2)=\\left[\\tfrac12x^4-\\tfrac43x^3\\right]_2^3=(40.5-36)-(8-\\tfrac{32}{3})=\\tfrac{43}{6}\\)<br>"
   "\\(Var(X)=\\tfrac{43}{6}-\\left(\\tfrac83\\right)^2=\\tfrac{129-128}{18}=\\tfrac1{18}=\\mathbf{«v»}\\)", e=r3(float(EX)), v=r3(float(Vd))),
 "Plausibel? E(X) liegt in [2, 3] und näher bei 3, weil die Dichte nach rechts ansteigt.")

card("Verteilungsfunktion herleiten, Wahrscheinlichkeiten, Median", 60,
 "(Fortsetzung) Leiten Sie F(x) her und berechnen Sie \\(P(X>2.5)\\), \\(P(X<2.2)\\), \\(P(2.2<X<2.8)\\) und den Median. <span class='pt'>(7 P)</span>",
 ["\\(F(x)=\\int_2^x2(t-2)\\,dt\\) – Integrationsvariable t, obere Grenze x.",
  "Drei Bereiche angeben: links 0, Mitte Formel, rechts 1.",
  "Stetig: \\(<\\) und \\(\\le\\) sind egal. \\(P(X>a)=1-F(a)\\).",
  "Median \\(x_{0.5}\\): \\(F(x_{0.5})=0.5\\) lösen; nur die Lösung in [2, 3] nehmen."],
 T("\\(F(x)=\\begin{cases}0&x<2\\\\(x-2)^2&2\\le x\\le3\\\\1&x>3\\end{cases}\\)<br>"
   "\\(P(X>2.5)=1-0.5^2=\\mathbf{0.75}\\) · \\(P(X<2.2)=0.2^2=\\mathbf{0.04}\\)<br>\\(P(2.2<X<2.8)=0.8^2-0.2^2=\\mathbf{0.6}\\)<br>"
   "\\((x-2)^2=0.5\\Rightarrow x_{0.5}=2+\\sqrt{0.5}=\\mathbf{«m»}\\)", m=r3(2 + math.sqrt(.5))),
 "Kontrolle: F(2) = 0 und F(3) = 1 müssen herauskommen.")

# --- 2.9 stückweise Dichte (Testat 4 A6)
E1 = Fr(8, 18); E2 = Fr(1, 12) * ((3 * 36 - Fr(216, 3)) - (3 * 4 - Fr(8, 3)))
assert E1 + E2 == Fr(8, 3)
card("Stückweise definierte Dichte: Erwartungswert", 35,
 "Y habe die Dichte \\(f(y)=\\frac y6\\) für \\(0\\le y\\le2\\), \\(f(y)=\\frac{6-y}{12}\\) für \\(2<y\\le6\\) und 0 sonst. Bestimmen Sie \\(E(Y)\\). <span class='pt'>(4 P)</span>",
 ["Das Integral in zwei Teile zerlegen – je ein Stück der Dichte.", "Jeweils \\(y\\cdot f(y)\\) integrieren und die Teile addieren."],
 "\\(E(Y)=\\int_0^2\\tfrac{y^2}{6}dy+\\int_2^6\\tfrac{6y-y^2}{12}dy=\\left[\\tfrac{y^3}{18}\\right]_0^2+\\tfrac1{12}\\left[3y^2-\\tfrac{y^3}{3}\\right]_2^6\\)<br>"
 "\\(=\\tfrac49+\\tfrac1{12}\\left(36-\\tfrac{28}{3}\\right)=\\tfrac49+\\tfrac{20}{9}=\\tfrac83=\\mathbf{2.667}\\)",
 "Aus Testat 4. Vorher kurz prüfen: Flächen \\(\\tfrac13+\\tfrac23=1\\) ✓.")

# --- 2.10 lineare Transformation & Summen
EZ = 3 * 4 - 2 * 1 + 5; VZ = 9 * 2 + 4 * 3
card("Rechenregeln: lineare Transformation und Summen", 85,
 "Es seien X und Y unabhängig mit \\(E(X)=4\\), \\(Var(X)=2\\), \\(E(Y)=1\\), \\(Var(Y)=3\\). Berechnen Sie für \\(Z=3X-2Y+5\\) den Erwartungswert, die Varianz und die Standardabweichung. <span class='pt'>(4 P)</span>",
 ["Erwartungswert: Konstanten bleiben, Faktoren ziehen einfach heraus.",
  "Varianz: Faktoren werden <b>quadriert</b>, die Konstante +5 fällt weg, ein Minus wird durch das Quadrat positiv.",
  "Unabhängig → keine Kovarianz-Terme."],
 T("\\(E(Z)=3\\cdot4-2\\cdot1+5=\\mathbf{«e»}\\)<br>\\(Var(Z)=3^2\\cdot2+(-2)^2\\cdot3=18+12=\\mathbf{«v»}\\)<br>\\(sd(Z)=\\sqrt{30}=\\mathbf{«s»}\\)",
   e=EZ, v=VZ, s=r3(math.sqrt(30))),
 "Klassiker-Fehler: \\(Var(3X)=3\\,Var(X)\\) (falsch, richtig ist \\(9\\,Var(X)\\)) oder \\(Var(X-Y)=Var(X)-Var(Y)\\) (falsch, es wird addiert).")

card("Rückwärts rechnen mit den Rechenregeln (Tutorium-Typ)", 55,
 "X habe \\(E(X)=3\\) und \\(Var(X)=1\\). Für \\(Z=0.5X+Y\\) mit X, Y unabhängig gilt \\(E(Z)=8.5\\) und \\(Var(Y)=1\\). Bestimmen Sie \\(E(Y)\\) und \\(Var(Z)\\). Wie ändert sich \\(Var(Z)\\), wenn \\(Cov(X,Y)=0.4\\) wäre? <span class='pt'>(4 P)</span>",
 ["\\(E(Z)=0.5E(X)+E(Y)\\) aufstellen und nach \\(E(Y)\\) auflösen.",
  "\\(Var(Z)=0.5^2Var(X)+Var(Y)+2\\cdot0.5\\cdot Cov(X,Y)\\)."],
 "\\(8.5=0.5\\cdot3+E(Y)\\Rightarrow E(Y)=\\mathbf{7}\\)<br>\\(Var(Z)=0.25\\cdot1+1=\\mathbf{1.25}\\)<br>"
 "Mit Kovarianz: \\(Var(Z)=0.25+1+2\\cdot0.5\\cdot0.4=\\mathbf{1.65}\\)",
 "Unabhängigkeit wird erst für die <b>Varianz</b> gebraucht, nicht für den Erwartungswert.")

# --- 2.11 gemeinsame Verteilung
J = {(0, 0): .10, (0, 1): .20, (0, 2): .10, (1, 0): .15, (1, 1): .25, (1, 2): .20}
PX = {x: sum(v for (a, b), v in J.items() if a == x) for x in (0, 1)}; PY = {y: sum(v for (a, b), v in J.items() if b == y) for y in (0, 1, 2)}
EX = sum(x * p for x, p in PX.items()); EY = sum(y * p for y, p in PY.items()); EXY = sum(a * b * v for (a, b), v in J.items())
cov = EXY - EX * EY; VX = sum(x * x * p for x, p in PX.items()) - EX ** 2; VY = sum(y * y * p for y, p in PY.items()) - EY ** 2
rho = cov / math.sqrt(VX * VY)
log("cov", cov); log("rho", rho)
TAB = ("<table class='tab' style='margin:.2em 0'><tr><th>X \\ Y</th><th>0</th><th>1</th><th>2</th></tr>"
       "<tr><th>0</th><td>0.10</td><td>0.20</td><td>0.10</td></tr><tr><th>1</th><td>0.15</td><td>0.25</td><td>0.20</td></tr></table>")
card("Gemeinsame Wahrscheinlichkeitsfunktion: Rand und bedingte Verteilung", 60,
 "X = „Kunde hat Kundenkarte“ (0/1), Y = Anzahl gekaufter Artikel. Gemeinsame Wahrscheinlichkeitsfunktion:" + TAB +
 "Berechnen Sie die Randverteilungen, \\(P(X=1|Y=2)\\) und die bedingte Verteilung von Y gegeben \\(X=0\\). Sind X und Y unabhängig? <span class='pt'>(7 P)</span>",
 ["Randverteilung = Zeilen- bzw. Spaltensummen.", "Bedingt: Zelle durch passende Randsumme der <b>Bedingung</b> teilen.",
  "Bedingte Verteilung vollständig angeben (alle y, Summe = 1, „0 sonst“).",
  "Unabhängig nur, wenn <b>jede</b> Zelle = Produkt der Ränder ist. Eine passende Zelle reicht nicht!"],
 "Rand X: \\(P(X=0)=0.4\\), \\(P(X=1)=0.6\\) · Rand Y: 0.25, 0.45, 0.30<br>"
 "\\(P(X=1|Y=2)=\\frac{0.20}{0.30}=\\mathbf{0.667}\\)<br>\\(P(Y=y|X=0)=\\frac{0.10}{0.4},\\frac{0.20}{0.4},\\frac{0.10}{0.4}=\\mathbf{0.25,\\ 0.5,\\ 0.25}\\) für y = 0, 1, 2 (0 sonst)<br>"
 "Zelle (0,0): \\(0.10=0.4\\cdot0.25\\) passt, aber Zelle (0,1): \\(0.20\\neq0.4\\cdot0.45=0.18\\) → <b>nicht unabhängig</b>.",
 "Tutorium 5, Aufgabe 1: Zeilen und Spalten nicht vertauschen – erst klären, was die Bedingung ist.")

card("Kovarianz und Korrelation zweier Zufallsvariablen", 45,
 "(Fortsetzung) Berechnen Sie \\(Cov(X,Y)\\) und den Korrelationskoeffizienten \\(\\rho(X,Y)\\). <span class='pt'>(5 P)</span>",
 ["\\(E(X)\\), \\(E(Y)\\) aus den Rändern.", "\\(E(XY)=\\sum\\sum x\\,y\\,P(X=x,Y=y)\\): Nur Zellen mit x ≠ 0 und y ≠ 0 tragen bei.",
  "\\(Cov=E(XY)-E(X)E(Y)\\), \\(\\rho=\\frac{Cov}{\\sqrt{Var(X)Var(Y)}}\\)."],
 T("\\(E(X)=0.6\\), \\(E(Y)=0.45+2\\cdot0.3=1.05\\)<br>\\(E(XY)=1\\cdot1\\cdot0.25+1\\cdot2\\cdot0.20=0.65\\)<br>"
   "\\(Cov(X,Y)=0.65-0.6\\cdot1.05=\\mathbf{«c»}\\)<br>\\(Var(X)=0.6-0.36=0.24\\), \\(Var(Y)=1.65-1.05^2=0.5475\\)<br>"
   "\\(\\rho=\\frac{0.02}{\\sqrt{0.24\\cdot0.5475}}=\\mathbf{«r»}\\) → sehr schwacher positiver linearer Zusammenhang", c=r3(cov)[:-1], r=r3(rho)),
 "Unkorreliert (ρ = 0) heißt <b>nicht</b> automatisch unabhängig. Nur bei gemeinsamer Normalverteilung ist beides gleich.")

# --- 2.13 gemeinsame Dichte
card("Gemeinsame Dichte: Randdichten und Unabhängigkeit", 25,
 "\\((X,Y)\\) habe die Dichte \\(f(x,y)=6x^2y\\) für \\(0\\le x,y\\le1\\) und 0 sonst. (a) Zeigen Sie, dass f eine Dichte ist. (b) Bestimmen Sie die Randdichten. Sind X und Y unabhängig? Wie groß ist ρ? (c) Berechnen Sie \\(P(X<\\tfrac12,\\,Y<\\tfrac12)\\) und \\(E(X)\\). <span class='pt'>(8 P)</span>",
 ["(a) Doppelintegral = 1 und \\(f\\ge0\\).", "(b) Randdichte von X: über <b>y</b> integrieren. Randdichte von Y: über <b>x</b> integrieren.",
  "Unabhängig ⇔ \\(f(x,y)=f_X(x)\\cdot f_Y(y)\\) ⇒ dann ρ = 0.", "(c) Grenzen passend zu dx und dy einsetzen."],
 "(a) \\(\\int_0^1\\int_0^1 6x^2y\\,dx\\,dy=\\int_0^1 2y\\,dy=1\\), \\(f\\ge0\\) ✓<br>"
 "(b) \\(f_X(x)=\\int_0^16x^2y\\,dy=3x^2\\), \\(f_Y(y)=\\int_0^16x^2y\\,dx=2y\\) (je auf [0, 1], 0 sonst)<br>"
 "\\(3x^2\\cdot2y=6x^2y=f(x,y)\\) → <b>unabhängig</b> → \\(\\rho=0\\)<br>"
 "(c) \\(P=\\int_0^{1/2}\\int_0^{1/2}6x^2y\\,dx\\,dy=\\tfrac18\\cdot\\tfrac14=\\tfrac1{32}=\\mathbf{0.031}\\) · \\(E(X)=\\int_0^1x\\cdot3x^2dx=\\mathbf{0.75}\\)",
 "Kommt seltener, aber Tutorium 6 hatte zwei solche Aufgaben. Wenn die Zeit knapp ist: lieber überspringen.")

# --- 2.14 fairer Einsatz
Ex = 0.1 * 8 + 0.2 * 1 + 0.7 * (-2); Ex2 = 0.1 * 64 + 0.2 * 1 + 0.7 * 4
card("Erwarteter Gewinn und fairer Einsatz", 40,
 "Ein Los kostet 2 €. Mit Wahrscheinlichkeit 0.1 gewinnt man 10 €, mit 0.2 gewinnt man 3 €, sonst nichts. X sei der Nettogewinn. Berechnen Sie \\(E(X)\\) und \\(Var(X)\\). Bei welchem Lospreis wäre das Spiel fair? <span class='pt'>(5 P)</span>",
 ["Netto = Auszahlung − Einsatz: 8 €, 1 €, −2 €.", "Fair heißt \\(E(\\text{Nettogewinn})=0\\) ⇔ Preis = erwartete Auszahlung."],
 T("\\(E(X)=0.1\\cdot8+0.2\\cdot1+0.7\\cdot(-2)=\\mathbf{«e»}\\) € (erwarteter Verlust)<br>"
   "\\(E(X^2)=6.4+0.2+2.8=9.4\\), \\(Var(X)=9.4-0.16=\\mathbf{«v»}\\)<br>Fair: Preis \\(=0.1\\cdot10+0.2\\cdot3=\\mathbf{1.6}\\) €", e=r3(Ex)[:-2], v=r3(Ex2 - Ex ** 2)[:-1]),
 "Wie Chuck-a-Luck in V06: Gleicher Erwartungswert kann sehr unterschiedliches Risiko (Varianz) haben.")
