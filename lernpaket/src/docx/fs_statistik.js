// Formelsammlung Statistik (Teil A) als Word-Datei
const fs = require('fs'), path = require('path');
const { Book } = require('./fslib');
const B = new Book('Formelsammlung Statistik (Teil A)');
const csv = f => fs.readFileSync(path.join(__dirname, '../rwork', f), 'utf8').trim().split('\n').slice(1).map(l => l.split(','));

B.cover('Formelsammlung Statistik', 'Teil A · Statistik und Data Science I · Göttingen · alle Themen V01–V12', [
  '**Aufbau:** Die Kapitel folgen der Vorlesung von vorne nach hinten. Jedes Kapitel: Begriffe → Formeln → Rezept → Punkte-Retter → typische Fallen → Antwortsätze.',
  '**Farbige Kästen:** ★ gelb = Punkte-Retter (das bringt Teilpunkte, auch wenn du nicht fertig wirst) · ✎ grün = fertiger Antwortsatz · ⚠ rot = typische Falle · ➜ blau = Schritt-für-Schritt-Rezept · TR = Türkische Erklärung.',
  '**Notation:** x̄ = arithmetisches Mittel, Σ = Summe über i = 1…n, log = natürlicher Logarithmus (ln), Φ = Verteilungsfunktion der Standardnormalverteilung.',
  '**Tipp für das A4-Blatt:** Übertrage die gelben Kästen und die Rezepte – sie sind die Punkte-Lieferanten.',
]);
B.toc(['0  Allgemeine Punkte-Retter für jede Aufgabe', '1  Daten, Merkmale, Skalenniveaus (V01)', '2  Häufigkeiten, Verteilungsfunktion, Histogramm (V02)',
  '3  Lagemaße (V02)', '4  Streuungsmaße & Boxplot (V02)', '5  Zusammenhänge: Kontingenz, Korrelation, Regression (V03)', '6  Wahrscheinlichkeitsrechnung (V04)',
  '7  Zufallsvariablen: diskret & stetig (V05)', '8  Erwartungswert, Varianz, zwei Zufallsvariablen (V06)', '9  Integral- & Ableitungs-Spickzettel',
  '10 Spezielle Verteilungen & ZGWS (V07)', '11 Schätzer und ihre Güte, Kerndichteschätzer (V08/V09)', '12 Maximum-Likelihood (V08)',
  '13 Konfidenzintervalle (V10)', '14 Statistische Tests (V11/V12)', '15 Interpretations- & Antwortsätze (Sammlung)', '16 Tabellen: Φ(z), t-Quantile, χ²-Quantile']);

// ───────────────── 0
B.h1('0  Allgemeine Punkte-Retter für jede Aufgabe');
B.box('retter', 'Formel IMMER zuerst allgemein hinschreiben, dann Zahlen einsetzen, dann Ergebnis. Die allgemeine Formel allein bringt oft schon 0.5–1 Punkt.',
  'Jede Teilfrage beantworten – auch geraten. Leere Kästchen = sicher 0 Punkte.',
  'Bezeichnung links vom Gleichheitszeichen: „P(A | B) = …“, „s² = …“, „λ̂ = …“. Nie nur eine nackte Zahl.',
  'Folgefehler werden berücksichtigt: Wenn (a) falsch ist, rechne in (b) mit deinem Ergebnis aus (a) korrekt weiter.',
  'Kannst du einen Wert nicht berechnen, nimm den in der Aufgabe angebotenen Ersatzwert („Wenn Sie … nicht berechnen konnten, verwenden Sie …“).',
  'Ist eine Aufgabe wirklich nicht lösbar: „nicht lösbar“ ins Kästchen + Begründung in die Box am Ende.');
B.h2('Form der Lösung (aus den Klausurhinweisen)');
B.ul(['**Dezimalpunkt** statt Komma: 0.25, nicht 0,25.', 'Endergebnis: **vollständig gekürzter Bruch** oder **3 Nachkommastellen** (kaufmännisch gerundet). Zwischenergebnisse mit mindestens **4** Nachkommastellen.',
  'Ausnahmen: ganze Zahlen und Ausdrücke wie √2 oder log(4) dürfen stehen bleiben.', 'Nur **eine** Lösung pro Kästchen – Falsches sauber durchstreichen.',
  'Nur Kugelschreiber/Tinte, kein Bleistift, kein Rot/Grün.', 'Alles außerhalb der Kästchen zählt nicht (außer klar markiert). Nebenrechnungen werden nicht korrigiert.']);
B.h2('10-Sekunden-Kontrolle nach jedem Kästchen');
B.table(['Prüfe', 'Frage an dich'], [['Alles?', 'Jede Teilfrage, jedes „Begründen Sie“, jede Interpretation beantwortet?'], ['Plausibel?', '0 ≤ P ≤ 1 · Var ≥ 0 · −1 ≤ r ≤ 1 · Summe aller Wahrscheinlichkeiten = 1 · Median liegt zwischen min und max'],
  ['Abgeschrieben?', 'Zahl im Kästchen = Zahl aus der Nebenrechnung?'], ['Form?', 'Punkt statt Komma · 3 Stellen · Bruch gekürzt · Bezeichnung links']], [2, 7]);
B.box('falle', 'Rechnen mit gerundeten Zwischenwerten (z. B. 1/3 ≈ 0.3) verfälscht Entscheidungen wie „unabhängig/abhängig“. Bei Laplace-Aufgaben mit Brüchen rechnen!');
B.box('tr', 'Formülü önce genel hâliyle yaz, sonra sayıları koy. Sonuç yanlış olsa bile yol puanı gelir. Hiçbir kutuyu boş bırakma.');

// ───────────────── 1
B.h1('1  Daten, Merkmale, Skalenniveaus (V01)');
B.h2('Grundbegriffe');
B.table(['Begriff', 'Bedeutung', 'Beispiel'], [['Statistische Einheit', 'Objekt, an dem gemessen wird', 'eine Person'], ['Grundgesamtheit', 'alle interessierenden Einheiten', 'alle Studierenden in Göttingen'],
  ['Stichprobe', 'tatsächlich untersuchte Teilmenge (Umfang n)', '50 befragte Studierende'], ['Merkmal (Variable)', 'interessierende Eigenschaft', 'Alter, Studienfach'], ['Merkmalsausprägung', 'konkreter Wert', '23 Jahre, „Jura“']], [2, 3, 3]);
B.h2('Skalenniveaus');
B.table(['Skala', 'Was ist erlaubt?', 'Sinnvolle Lagemaße', 'Beispiele'], [
  ['Nominal', 'nur = / ≠ (Kategorien ohne Ordnung)', 'nur Modus', 'Geschlecht, Studienfach, Farbe, Lieblingssorte'],
  ['Ordinal', 'zusätzlich Ordnung < >; Abstände nicht interpretierbar', 'Modus, Median, Quantile', 'Schulnoten, Zufriedenheit (gut/mittel/schlecht), Rang'],
  ['Metrisch – Intervallskala', 'Abstände interpretierbar, kein natürlicher Nullpunkt', 'Modus, Median, Mittelwert', 'Temperatur in °C, Jahreszahl'],
  ['Metrisch – Verhältnisskala', 'natürlicher Nullpunkt, Quotienten sinnvoll', 'alle (auch geometr. Mittel)', 'Gewicht, Einkommen, Dauer, Anzahl']], [2.2, 3.2, 2.4, 3.2]);
B.h2('Diskret vs. stetig');
B.ul(['**Diskret:** endlich oder abzählbar viele Ausprägungen (meist Anzahlen: 0, 1, 2, …). Beispiel: Anzahl Besuche, Anzahl Kinder.',
  '**Stetig:** jeder Wert in einem Intervall möglich (Messungen). Beispiel: Zeit, Gewicht, Länge, Temperatur.',
  '**Quasi-stetig:** eigentlich diskret, aber sehr fein (Einkommen in Cent) → wie stetig behandeln.', 'Nominale/ordinale Merkmale sind immer diskret.']);
B.box('satz', '„Das Merkmal Anzahl der Bestellungen ist metrisch (verhältnisskaliert) und diskret, da nur ganze Zahlen 0, 1, 2, … möglich sind und ein natürlicher Nullpunkt existiert.“',
  '„Das Merkmal Lieblingssorte ist nominalskaliert und diskret, da die Kategorien keine natürliche Ordnung besitzen.“');
B.box('falle', 'Kodierte Kategorien (1 = Jura, 2 = Wiwi) bleiben nominal – Zahlen machen ein Merkmal nicht metrisch! Mittelwert/Median dann „nicht sinnvoll“ + Begründung.');
B.box('retter', 'Bei „Skalenniveau + diskret/stetig“ immer BEIDES nennen und mit einem Halbsatz begründen. Fehlt die Begründung, gibt es oft nur halbe Punkte.');

// ───────────────── 2
B.h1('2  Häufigkeiten, Verteilungsfunktion, Histogramm (V02)');
B.h2('Häufigkeiten');
B.f('absolute Häufigkeit: hⱼ = Anzahl der Beobachtungen mit Ausprägung aⱼ,   Σ hⱼ = n', 'relative Häufigkeit: fⱼ = hⱼ / n,   Σ fⱼ = 1', 'kumulierte relative Häufigkeit bis aⱼ: f₁ + f₂ + … + fⱼ');
B.h2('Empirische Verteilungsfunktion F̂(x)');
B.f('F̂(x) = (Anzahl der Beobachtungen ≤ x) / n  =  Σ_{aⱼ ≤ x} fⱼ');
B.box('tipp', '1) Daten sortieren, verschiedene Werte a₁ < a₂ < … notieren.  2) Für jeden Wert fⱼ bestimmen.  3) Kumulieren.  4) Fallunterscheidung aufschreiben:',
  'F̂(x) = 0 für x < a₁;  = f₁ für a₁ ≤ x < a₂;  = f₁+f₂ für a₂ ≤ x < a₃;  …;  = 1 für x ≥ a_k',
  '5) Skizze: Treppe, an jedem Wert Sprung um fⱼ nach oben, ● links geschlossen (Wert gehört dazu), ○ rechts offen.');
B.h2('Anteile aus F̂ ablesen');
B.table(['Gesucht', 'Formel'], [['Anteil ≤ x', 'F̂(x)'], ['Anteil > x', '1 − F̂(x)'], ['Anteil < x', 'F̂(x) − f(x) = F̂ an der Stufe direkt links von x'], ['Anteil ≥ x', '1 − F̂(Stufe links von x)'], ['Anteil a < X ≤ b', 'F̂(b) − F̂(a)']], [3, 6]);
B.h2('Klassierte Daten & Histogramm');
B.f('Klassenbreite: dⱼ = obere Grenze − untere Grenze', 'Säulenhöhe (normiertes Histogramm, Fläche = 1):  ĥⱼ = fⱼ / dⱼ', 'Klassenmitte: mⱼ = (untere + obere Grenze) / 2', 'Mittelwert klassierter Daten: x̄ ≈ Σ fⱼ · mⱼ = (1/n) Σ hⱼ · mⱼ');
B.ul(['**Modalklasse** = Klasse mit der **größten Säulenhöhe** (nicht unbedingt größte Häufigkeit, wenn Breiten verschieden!).', '**Fläche einer Säule = Anteil** der Daten in der Klasse.',
  '**Anteil in einem Teil einer Klasse** (Annahme Gleichverteilung in der Klasse): Anteil = Säulenhöhe × Breite des Teilstücks.']);
B.box('retter', 'Histogramm-Skizze: Achsen beschriften (x: Merkmal mit Einheit, y: „Dichte“ bzw. fⱼ/dⱼ), Klassengrenzen eintragen, Höhen eintragen. Auch eine grobe Skizze gibt Punkte.');
B.box('falle', 'Bei ungleich breiten Klassen ist die Höhe NICHT fⱼ, sondern fⱼ / dⱼ.  ·  Klassen: [a, b) heißt a gehört dazu, b nicht.');
B.box('tr', 'Histogramda sütun yüksekliği = oran / genişlik. Alan = oran. Sınıf ortası ile ortalama: her sınıfın ortasını oranıyla çarp, topla.');

// ───────────────── 3
B.h1('3  Lagemaße (V02)');
B.h2('Modus, Median, Quantile');
B.f('Modus x_mod: häufigste Ausprägung (ab Nominalskala)', 'Median: Daten sortieren x₍₁₎ ≤ … ≤ x₍ₙ₎', '  n ungerade: x_med = x₍(n+1)/2₎', '  n gerade:   x_med = ( x₍n/2₎ + x₍n/2+1₎ ) / 2');
B.f('α-Quantil x_α (Vorlesung): berechne n·α', '  n·α keine ganze Zahl → aufrunden: x_α = x₍⌈nα⌉₎', '  n·α ganze Zahl → x_α zwischen x₍nα₎ und x₍nα+1₎, eindeutig: Mittelwert ( x₍nα₎ + x₍nα+1₎ ) / 2');
B.ul(['Unteres Quartil x₀.₂₅, Median x₀.₅, oberes Quartil x₀.₇₅.', 'Beispiel (Vorlesung): n = 26, α = 0.25 → 6.5 → aufrunden auf 7 → x₀.₂₅ = x₍₇₎.']);
B.h2('Arithmetisches Mittel');
B.f('x̄ = (1/n) · Σ xᵢ', 'aus Häufigkeitstabelle: x̄ = Σ aⱼ · fⱼ', 'gepoolt aus Gruppen: x̄ = (n₁x̄₁ + n₂x̄₂) / (n₁ + n₂)', 'lineare Transformation y = a + b·x  ⇒  ȳ = a + b·x̄');
B.h2('Eigenschaften');
B.table(['Lagemaß', 'Skala', 'Robust gegen Ausreißer?'], [['Modus', 'ab nominal', 'ja'], ['Median / Quantile', 'ab ordinal', 'ja'], ['arithm. Mittel', 'metrisch', 'nein – wird von Extremwerten gezogen']], [3, 3, 4]);
B.ul(['Rechtsschief (langer rechter Rand): x_mod < x_med < x̄ · Linksschief: x̄ < x_med < x_mod · Symmetrisch: alle ≈ gleich.', 'Σ (xᵢ − x̄) = 0 (Schwerpunkteigenschaft).']);
B.box('satz', '„Da der Wert 14 ein Ausreißer ist, beschreibt der Median (3) das typische Verhalten besser als das arithmetische Mittel (3.667), weil der Median robust gegenüber Extremwerten ist.“');
B.box('falle', 'Median nur nach dem SORTIEREN.  ·  Bei nominalen Daten: Median „nicht sinnvoll“ + Begründung („keine Ordnung“).');

// ───────────────── 4
B.h1('4  Streuungsmaße & Boxplot (V02)');
B.f('Spannweite: R = x_max − x_min', 'Interquartilsabstand: d_Q = x₀.₇₅ − x₀.₂₅',
  'empirische Varianz: s² = (1/n) Σ (xᵢ − x̄)²', 'Verschiebungssatz: s² = (1/n) Σ xᵢ² − x̄²   ← schnellster Weg mit Σxᵢ²',
  'unverzerrte (korrigierte) Varianz: s*² = (1/(n−1)) Σ (xᵢ − x̄)² = n/(n−1) · s²', 'Standardabweichung: s = √s²,  s* = √s*²', 'lineare Transformation y = a + b·x ⇒ s²_y = b²·s²_x,  s_y = |b|·s_x');
B.box('tipp', '1) x̄ = Σxᵢ / n   2) Σxᵢ²/n berechnen   3) s² = Σxᵢ²/n − x̄²   4) s*² = s² · n/(n−1)   5) beide mit Bezeichnung hinschreiben.');
B.h2('Boxplot');
B.ul(['Box von x₀.₂₅ bis x₀.₇₅, Strich beim Median.', 'Whisker bis zum kleinsten/größten Wert, der **kein Ausreißer** ist.',
  '**Ausreißerregel:** Ausreißer, wenn Wert < x₀.₂₅ − 1.5·d_Q oder > x₀.₇₅ + 1.5·d_Q. Ausreißer als einzelne Punkte zeichnen.', 'Lange rechte Box-/Whiskerhälfte → rechtsschief.']);
B.box('retter', 'Bei „Ist x ein Ausreißer?“: Grenzen x₀.₇₅ + 1.5·d_Q und x₀.₂₅ − 1.5·d_Q konkret ausrechnen und vergleichen – die Rechnung ist der Punkt.');
B.box('falle', 'In R liefert var() und sd() die Version mit (n−1) = s*. In Teil A genau lesen, ob s² (1/n) oder s*² (1/(n−1)) verlangt ist!');

// ───────────────── 5
B.h1('5  Zusammenhänge: Kontingenz, Korrelation, Regression (V03)');
B.h2('Kontingenztafel (zwei kategoriale Merkmale)');
B.f('hᵢⱼ = Anzahl mit X = aᵢ und Y = bⱼ;  Randhäufigkeiten hᵢ• (Zeilensumme), h•ⱼ (Spaltensumme)', 'relative Häufigkeit: fᵢⱼ = hᵢⱼ / n',
  'bedingte Häufigkeit von Y gegeben X = aᵢ:  f(bⱼ | aᵢ) = hᵢⱼ / hᵢ•   (zeilenweise normieren)', 'bei Unabhängigkeit erwartet:  h̃ᵢⱼ = hᵢ• · h•ⱼ / n',
  'χ²-Koeffizient: χ² = Σᵢ Σⱼ (hᵢⱼ − h̃ᵢⱼ)² / h̃ᵢⱼ   (0 = kein Zusammenhang)');
B.box('satz', '„Sind die bedingten Verteilungen in allen Zeilen gleich (bzw. hᵢⱼ = h̃ᵢⱼ), so sind die Merkmale empirisch unabhängig.“');
B.h2('Kovarianz & Korrelation (metrische Merkmale)');
B.f('empirische Kovarianz: s_xy = (1/n) Σ (xᵢ − x̄)(yᵢ − ȳ) = (1/n) Σ xᵢyᵢ − x̄·ȳ', 'Korrelation nach Bravais-Pearson: r_xy = s_xy / (s_x · s_y) = s_xy / √(s²_x · s²_y)',
  'Achtung: s_x, s_y hier mit 1/n (passend zu s_xy). Gleiche Faktoren kürzen sich: mit (n−1) überall geht es auch.');
B.table(['|r|', 'Interpretation'], [['r = 0', 'kein linearer Zusammenhang'], ['0 < |r| < 0.5', 'schwacher linearer Zusammenhang'], ['0.5 ≤ |r| < 0.8', 'mittlerer linearer Zusammenhang'], ['|r| ≥ 0.8', 'starker linearer Zusammenhang'], ['r = ±1', 'perfekter linearer Zusammenhang (alle Punkte auf einer Geraden)']], [2, 7]);
B.ul(['Vorzeichen: r > 0 gleichsinnig („je mehr …, desto mehr …“), r < 0 gegensinnig.', 'r misst nur **lineare** Zusammenhänge; r = 0 heißt nicht „kein Zusammenhang“ (z. B. U-Form möglich).']);
B.h2('Rangkorrelation nach Spearman');
B.f('Ränge bilden: rg(xᵢ), rg(yᵢ) (kleinster Wert Rang 1; bei Bindungen Durchschnittsränge)', 'r_SP = Pearson-Korrelation der Ränge', 'ohne Bindungen: r_SP = 1 − 6·Σ dᵢ² / (n(n² − 1)),  dᵢ = rg(xᵢ) − rg(yᵢ)');
B.ul(['Misst **monotone** Zusammenhänge, robust gegen Ausreißer, ab ordinal.', 'Steigen x und y in derselben Reihenfolge → r_SP = 1 (auch wenn nicht linear).']);
B.h2('Lineare Regression (Kleinste Quadrate)');
B.f('ŷ = a + b·x', 'b = s_xy / s²_x', 'a = ȳ − b·x̄', 'Prognose: ŷ(x₀) = a + b·x₀', 'Residuum: eᵢ = yᵢ − ŷᵢ;  Σ eᵢ = 0;  Gerade geht durch (x̄, ȳ)', 'Bestimmtheitsmaß: R² = r²_xy (Anteil erklärter Streuung, 0 ≤ R² ≤ 1)');
B.box('tipp', '1) x̄, ȳ  2) s_xy = Σxy/n − x̄ȳ  3) s²_x = Σx²/n − x̄²  4) b = s_xy/s²_x  5) a = ȳ − b·x̄  6) Gerade hinschreiben: ŷ = a + b·x.');
B.box('satz', 'Steigung: „Steigt X um eine Einheit (z. B. 1 °C), so steigt Y im Mittel um b Einheiten (laut Modell).“',
  'Achsenabschnitt: „Für x = 0 sagt das Modell ŷ = a voraus (oft nur rechnerisch, nicht sinnvoll interpretierbar).“',
  'Korrelation: „r = 0.997: sehr starker positiver linearer Zusammenhang – je höher die Temperatur, desto mehr Eis wird verkauft.“',
  'Kausalität: „Korrelation bedeutet keine Kausalität. Der Zusammenhang kann durch eine Drittvariable (Scheinkorrelation) oder umgekehrte Wirkungsrichtung entstehen.“');
B.box('falle', 'Prognosen weit außerhalb des Datenbereichs (Extrapolation) sind unzuverlässig – erwähnen, wenn gefragt „Beurteilen Sie“.  ·  b und r haben immer dasselbe Vorzeichen.');
B.box('retter', 'Auch ohne Ergebnis: „b = s_xy / s²_x“ und „a = ȳ − b·x̄“ hinschreiben + Gerade „ŷ = a + b·x“. Interpretation darf mit dem Ersatzwert erfolgen.');

// ───────────────── 6
B.h1('6  Wahrscheinlichkeitsrechnung (V04)');
B.h2('Mengen & Ereignisse');
B.table(['Symbol', 'Bedeutung', 'In Worten'], [['A ∩ B', 'Schnitt', 'A und B'], ['A ∪ B', 'Vereinigung', 'A oder B (oder beide)'], ['Ā', 'Komplement / Gegenereignis', 'nicht A'], ['A \\ B = A ∩ B̄', 'Differenz', 'A, aber nicht B'], ['A ∩ B = ∅', 'disjunkt', 'schließen sich aus'], ['|A|', 'Mächtigkeit', 'Anzahl Elemente']], [2, 3, 3]);
B.f('De Morgan:  (A ∪ B)‾ = Ā ∩ B̄     (A ∩ B)‾ = Ā ∪ B̄', '|A ∪ B| = |A| + |B| − |A ∩ B|');
B.h2('Rechenregeln');
B.f('Laplace: P(A) = |A| / |Ω|  (alle Ergebnisse gleich wahrscheinlich)', 'Gegenereignis: P(Ā) = 1 − P(A)', 'Additionssatz: P(A ∪ B) = P(A) + P(B) − P(A ∩ B)',
  'disjunkt: P(A ∪ B) = P(A) + P(B)', 'P(A ∩ B̄) = P(A) − P(A ∩ B)');
B.h2('Bedingte Wahrscheinlichkeit, Bayes, Unabhängigkeit');
B.f('bedingt: P(A | B) = P(A ∩ B) / P(B)', 'Multiplikationssatz (Pfadregel): P(A ∩ B) = P(B) · P(A | B) = P(A) · P(B | A)',
  'totale Wahrscheinlichkeit: P(A) = Σᵢ P(A | Bᵢ) · P(Bᵢ)   (Bᵢ Zerlegung von Ω)', 'Bayes: P(Bⱼ | A) = P(A | Bⱼ) · P(Bⱼ) / Σᵢ P(A | Bᵢ) · P(Bᵢ)',
  'Unabhängigkeit: P(A ∩ B) = P(A) · P(B)  ⇔  P(A | B) = P(A)', 'Gegenwahrscheinlichkeit bedingt: P(Ā | B) = 1 − P(A | B)');
B.box('tipp', 'Baumdiagramm: 1. Stufe = das Ereignis, nach dem in der Aufgabe ZUERST unterschieden wird („Zunächst betrachtet er die pünktlichen …“). 2. Stufe = bedingte Wahrscheinlichkeiten.',
  'Fehlende Äste: Summe der Äste an einem Knoten = 1 (z. B. Dienst C = 1 − 0.70 − 0.25).');
B.h2('Die drei Retter-Regeln im Baum');
B.table(['Gefragt', 'Was tun?', 'Beispiel'], [['P(A | B), B steht am Ast vorher', 'ABLESEN (Zahl am Ast)', '„von den Pünktlichen 5 %“ → P(C | P) = 0.05'],
  ['P(A ∩ B)', 'Pfad MULTIPLIZIEREN', 'P(P ∩ C) = 0.8 · 0.05'], ['P(A) (am Ende des Baums)', 'alle Pfade zu A ADDIEREN', 'P(C) = 0.8·0.05 + 0.2·0.3'], ['P(B | A), Richtung umgedreht', 'BAYES: Pfad / Summe', 'P(V | C) = 0.06 / 0.1']], [3, 2.5, 3.5]);
B.h2('„Mindestens einer“ & Kombinatorik');
B.f('P(mindestens ein Erfolg bei n unabhängigen Versuchen) = 1 − P(kein Erfolg) = 1 − (1 − p)ⁿ', 'n! = 1·2·…·n,  0! = 1', 'Binomialkoeffizient: (n über k) = n! / (k!·(n−k)!)  = Anzahl Möglichkeiten, k aus n ohne Reihenfolge zu wählen');
B.table(['Ziehen', 'mit Reihenfolge', 'ohne Reihenfolge'], [['mit Zurücklegen', 'nᵏ', '(n+k−1 über k)'], ['ohne Zurücklegen', 'n! / (n−k)!', '(n über k)']], [3, 3, 3]);
B.box('satz', '„Da P(A ∩ B) = 0.2 = 0.5 · 0.4 = P(A) · P(B), sind A und B stochastisch unabhängig.“  ·  „Da P(pünktlich | A) = 0.903 ≠ 0.8 = P(pünktlich), sind die Ereignisse abhängig.“');
B.box('falle', 'P(A | B) ≠ P(A ∩ B) ≠ P(B | A).  ·  Disjunkt ≠ unabhängig (disjunkte Ereignisse mit P > 0 sind immer abhängig!).  ·  „Ohne Zurücklegen“: im 2. Zug ändern sich die Wahrscheinlichkeiten.');
B.box('retter', 'Baumdiagramm zeichnen und alle Äste beschriften, auch wenn nicht verlangt – daraus kann der Korrektor deinen Weg erkennen. Bei Unabhängigkeit immer beide Seiten ausrechnen und vergleichen.');
B.box('tr', '“|” işareti varsa dalı oku, “∩” varsa yolu çarp, tek başına P(A) ise yolları topla, yön tersse Bayes: yol / toplam.');

// ───────────────── 7
B.h1('7  Zufallsvariablen: diskret & stetig (V05)');
B.table(['', 'Diskret', 'Stetig'], [
  ['Träger T', 'Liste möglicher Werte {x₁, x₂, …}', 'Intervall, auf dem f(x) > 0'],
  ['Verteilung', 'Wahrscheinlichkeitsfunktion P(X = x) bzw. f(x)', 'Dichte f(x) ≥ 0'],
  ['Normierung', 'Σ P(X = xᵢ) = 1', '∫ f(x) dx = 1 (über den Träger)'],
  ['P(a ≤ X ≤ b)', 'Σ_{a ≤ xᵢ ≤ b} P(X = xᵢ)', '∫ₐᵇ f(x) dx = F(b) − F(a)'],
  ['P(X = a)', 'kann > 0 sein', 'immer 0 → ≤ und < egal'],
  ['Verteilungsfunktion', 'F(x) = Σ_{xᵢ ≤ x} P(X = xᵢ) (Treppe)', 'F(x) = ∫_{−∞}^{x} f(t) dt (stetige Kurve), f = F′']], [2, 4, 4]);
B.h2('Rezept: Konstante c bestimmen');
B.f('stetig: ∫_{Träger} f(x) dx = 1  →  nach c auflösen', 'diskret: Σ P(X = xᵢ) = 1  →  nach c auflösen', 'Beispiel: f(x) = c·x² auf [0, 3]:  c·[x³/3]₀³ = 9c = 1  ⇒  c = 1/9');
B.h2('Verteilungsfunktion F(x) aufstellen (stetig)');
B.f('F(x) = 0 für x < untere Grenze', 'F(x) = ∫_{untere}^{x} f(t) dt für x im Träger', 'F(x) = 1 für x > obere Grenze', 'Beispiel: f(x) = x²/9 auf [0,3]:  F(x) = x³/27 für 0 ≤ x ≤ 3');
B.h2('Quantile & Median einer Zufallsvariable');
B.f('x_α löst F(x_α) = α;  Median: F(x_med) = 0.5', 'Beispiel: x³/27 = 0.5 ⇒ x_med = ∛13.5 = 2.381');
B.h2('Unabhängigkeit von Zufallsvariablen');
B.f('P(X = x, Y = y) = P(X = x)·P(Y = y) für alle x, y  (stetig: f(x, y) = f_X(x)·f_Y(y))', 'iid = unabhängig und identisch verteilt (Standardannahme für Stichproben)');
B.box('retter', 'Dichte-Aufgabe: Immer zuerst „∫ f(x) dx = 1“ hinschreiben mit den Grenzen des Trägers. F(x) immer mit DREI Fällen (0 / Formel / 1).');
B.box('falle', '„0 sonst“ nie vergessen.  ·  Wahrscheinlichkeitsfunktion = P(X = x) (Liste), Verteilungsfunktion = F(x) (Treppe/kumuliert) – nicht verwechseln!  ·  Bei Dichte: Integral, keine Summe.');

// ───────────────── 8
B.h1('8  Erwartungswert, Varianz, zwei Zufallsvariablen (V06)');
B.table(['', 'Diskret', 'Stetig'], [['E(X)', 'Σ xᵢ · P(X = xᵢ)', '∫ x · f(x) dx'], ['E(X²)', 'Σ xᵢ² · P(X = xᵢ)', '∫ x² · f(x) dx'], ['E(g(X))', 'Σ g(xᵢ) · P(X = xᵢ)', '∫ g(x) · f(x) dx'], ['Var(X)', 'E(X²) − E(X)²', 'E(X²) − E(X)²']], [2, 4, 4]);
B.box('tipp', 'Varianz in 3 Zeilen: ① E(X) ② E(X²) ③ Var(X) = E(X²) − E(X)².  Kontrolle: Var ≥ 0.  KEINE Division durch n (das gibt es nur bei Daten)!');
B.h2('Rechenregeln');
B.f('E(a + bX) = a + b·E(X)', 'Var(a + bX) = b²·Var(X)   (Konstante a fällt weg!)', 'E(X + Y) = E(X) + E(Y)   (immer)', 'Var(X + Y) = Var(X) + Var(Y) + 2·Cov(X, Y);  bei Unabhängigkeit: Var(X) + Var(Y)',
  'Var(X − Y) = Var(X) + Var(Y) − 2·Cov(X, Y)', 'E(g(X)) ≠ g(E(X)) im Allgemeinen (z. B. E(X²) ≠ E(X)², E(log X) ≠ log E(X))', 'Standardisierung: Z = (X − E(X)) / √Var(X) hat E(Z) = 0, Var(Z) = 1');
B.h2('Zwei Zufallsvariablen (bivariat)');
B.f('gemeinsame Verteilung: P(X = x, Y = y) (Tabelle)', 'Randverteilung: P(X = x) = Σ_y P(X = x, Y = y)  (Zeilensumme)', 'bedingte Verteilung: P(Y = y | X = x) = P(X = x, Y = y) / P(X = x)',
  'E(XY) = Σ Σ x·y·P(X = x, Y = y)', 'Kovarianz: Cov(X, Y) = E(XY) − E(X)·E(Y)', 'Korrelation: ρ(X, Y) = Cov(X, Y) / √(Var(X)·Var(Y)),  −1 ≤ ρ ≤ 1', 'unabhängig ⇒ Cov = 0 (Umkehrung gilt nicht allgemein)');
B.box('falle', 'Var(X − Y) hat ein PLUS bei Var(Y).  ·  Var(3X) = 9·Var(X), nicht 3·Var(X).  ·  Var(X₁ + X₂) = 2σ², aber Var(2X) = 4σ².');
B.box('retter', 'Bei Schätzer-Aufgaben: Regeln E(aX) = aE(X), Var(aX) = a²Var(X) und Var der Summe hinschreiben, dann einsetzen – jede Zeile gibt Punkte.');

// ───────────────── 9
B.h1('9  Integral- & Ableitungs-Spickzettel');
B.h2('Stammfunktionen');
B.table(['f(x)', 'Stammfunktion F(x)', 'Hinweis'], [['c (Konstante)', 'c·x', ''], ['xⁿ (n ≠ −1)', 'xⁿ⁺¹ / (n+1)', 'Potenzregel: Exponent +1, durch neuen Exponenten'], ['1/x', 'log|x|', ''], ['e^{ax}', '(1/a)·e^{ax}', 'z. B. ∫ λe^{−λx} dx = −e^{−λx}'],
  ['c·f(x)', 'c·F(x)', 'Konstante rausziehen'], ['f(x) + g(x)', 'F(x) + G(x)', 'summandenweise'], ['x·e^{−λx}', '−(x/λ + 1/λ²)·e^{−λx}', 'partielle Integration']], [2.5, 3.5, 4]);
B.f('Bestimmtes Integral: ∫ₐᵇ f(x) dx = [F(x)]ₐᵇ = F(b) − F(a)', 'Partielle Integration: ∫ u·v′ dx = u·v − ∫ u′·v dx');
B.h2('Ableitungen (für Maximum-Likelihood)');
B.table(['Funktion', 'Ableitung'], [['xⁿ', 'n·xⁿ⁻¹'], ['log(x)', '1/x'], ['c·log(θ)', 'c/θ'], ['eˣ', 'eˣ'], ['e^{aθ}', 'a·e^{aθ}'], ['log(1 − θ)', '−1/(1 − θ)'], ['c·θ', 'c'], ['Konstante (ohne θ)', '0']], [4, 4]);
B.h2('Log- und Potenzregeln');
B.f('log(a·b) = log a + log b    log(a/b) = log a − log b    log(aᵇ) = b·log a', 'log(e^{x}) = x    log(1) = 0    log(∏ xᵢ) = Σ log xᵢ', 'aⁿ·aᵐ = aⁿ⁺ᵐ    ∏ θ = θⁿ    ∏ e^{−λxᵢ} = e^{−λΣxᵢ}');
B.box('tr', 'Potans kuralı: üssü 1 artır, yeni üsse böl. Sınırları koy: üst − alt. Sabit (c) integralin dışına çıkar.');

// ───────────────── 10
B.h1('10  Spezielle Verteilungen & ZGWS (V07)');
B.table(['Verteilung', 'Träger', 'P(X = x) bzw. f(x)', 'E(X)', 'Var(X)'], [
  ['Bernoulli B(1, π)', '{0, 1}', 'πˣ (1−π)¹⁻ˣ', 'π', 'π(1−π)'],
  ['Binomial B(n, π)', '{0, …, n}', '(n über x) πˣ (1−π)ⁿ⁻ˣ', 'nπ', 'nπ(1−π)'],
  ['Poisson Po(λ)', '{0, 1, 2, …}', 'λˣ e^{−λ} / x!', 'λ', 'λ'],
  ['Gleichverteilung U(a, b)', '[a, b]', '1 / (b − a)', '(a + b)/2', '(b − a)²/12'],
  ['Exponential Exp(λ)', '[0, ∞)', 'λ e^{−λx};  F(x) = 1 − e^{−λx}', '1/λ', '1/λ²'],
  ['Normal N(μ, σ²)', 'ℝ', '1/(√(2π)σ) · exp(−(x−μ)²/(2σ²))', 'μ', 'σ²']], [2.6, 1.6, 3.6, 1.2, 1.6]);
B.h2('Wann welche Verteilung?');
B.ul(['**Binomial:** Anzahl Erfolge bei n unabhängigen Versuchen mit gleicher Erfolgswahrscheinlichkeit π (Multiple-Choice raten, Qualitätskontrolle).', '**Poisson:** Anzahl seltener Ereignisse in einem Zeitraum (Anrufe pro Stunde, Kunden pro Minute).',
  '**Exponential:** Wartezeit bis zum nächsten Ereignis (gedächtnislos).', '**Normal:** Messgrößen, Summen/Mittelwerte vieler Einflüsse (ZGWS).', '**Gleichverteilung:** jeder Wert im Intervall gleich wahrscheinlich.']);
B.h2('Normalverteilung rechnen');
B.f('Standardisieren: Z = (X − μ) / σ ~ N(0, 1)', 'P(X ≤ x) = Φ((x − μ)/σ)', 'P(X > x) = 1 − Φ((x − μ)/σ)', 'P(a ≤ X ≤ b) = Φ((b − μ)/σ) − Φ((a − μ)/σ)', 'Symmetrie: Φ(−z) = 1 − Φ(z)', 'Quantil: x_α = μ + z_α·σ');
B.table(['α', '0.90', '0.95', '0.975', '0.99', '0.995'], [['z_α', '1.282', '1.645', '1.960', '2.326', '2.576']], [1, 1, 1, 1, 1, 1]);
B.box('falle', 'N(30, 16) heißt Varianz 16 → σ = 4 (Wurzel ziehen!).  ·  P(X > x) = 1 − Φ(…), nicht Φ(…).');
B.h2('Summen, Mittelwerte, Zentraler Grenzwertsatz');
B.f('X ~ N(μ₁, σ₁²), Y ~ N(μ₂, σ₂²) unabhängig ⇒ X + Y ~ N(μ₁ + μ₂, σ₁² + σ₂²)', 'a + bX ~ N(a + bμ, b²σ²)', 'X₁,…,Xₙ iid N(μ, σ²) ⇒ X̄ ~ N(μ, σ²/n)',
  'ZGWS: X₁,…,Xₙ iid mit E = μ, Var = σ² ⇒ X̄ ≈ N(μ, σ²/n) bzw. Σ Xᵢ ≈ N(nμ, nσ²) für großes n (Faustregel n ≥ 30)', 'Binomial-Approximation: B(n, π) ≈ N(nπ, nπ(1−π)) für großes n');
B.box('retter', 'Bei Binomial-Fragen immer Verteilung MIT Parametern hinschreiben: „Y ~ B(5; 0.25)“ – gibt oft schon einen Punkt. P(Y ≥ k) = P(Y = k) + … + P(Y = n) oder 1 − P(Y ≤ k−1).');

// ───────────────── 11
B.h1('11  Schätzer und ihre Güte, Kerndichteschätzer (V08/V09)');
B.h2('Begriffe');
B.ul(['**Parameter θ:** unbekannte feste Größe der Grundgesamtheit (μ, π, λ, σ²).', '**Schätzer θ̂ = T(X₁,…,Xₙ):** Zufallsvariable (Formel). **Schätzwert:** konkrete Zahl aus den Daten.',
  'Standardschätzer: μ̂ = X̄,  π̂ = Anteil,  σ̂² = S*² = (1/(n−1)) Σ (Xᵢ − X̄)² (erwartungstreu).']);
B.h2('Gütekriterien');
B.f('Bias: Bias(θ̂) = E(θ̂) − θ', 'erwartungstreu (unverzerrt): E(θ̂) = θ  ⇔  Bias = 0', 'Varianz: Var(θ̂) = E[(θ̂ − E(θ̂))²]', 'MSE: MSE(θ̂) = E[(θ̂ − θ)²] = Var(θ̂) + Bias(θ̂)²',
  'konsistent: MSE(θ̂) → 0 für n → ∞', 'effizienter: bei zwei erwartungstreuen Schätzern der mit kleinerer Varianz');
B.box('tipp', 'Erwartungstreue prüfen: 1) E(θ̂) mit Linearität ausrechnen (E(Xᵢ) = μ einsetzen)  2) mit θ vergleichen  3) Satz: „Da E(θ̂) = μ, ist θ̂ erwartungstreu.“ bzw. „Bias = …“.',
  'Varianz: Var(Σ aᵢXᵢ) = Σ aᵢ² σ² (bei Unabhängigkeit).  Beispiel: Var((3X₁ + X₂)/4) = (9 + 1)/16 · σ² = 5/8 σ².');
B.f('E(X̄) = μ    Var(X̄) = σ²/n    E(S²) = (n−1)/n · σ² (verzerrt)    E(S*²) = σ²');
B.box('falle', 'Bei Produkten: E(X₁·X₂) = E(X₁)·E(X₂) nur bei Unabhängigkeit.  ·  E(1/X) ≠ 1/E(X).');
B.h2('Nichtparametrische Dichteschätzung');
B.ul(['**Histogramm** als Dichteschätzer: hängt von Klassenbreite und Startpunkt ab.', '**Kerndichteschätzer:** glatte Schätzung ohne Verteilungsannahme.']);
B.f('f̂(x) = (1/(n·b)) · Σ K((x − xᵢ)/b)     b = Bandweite', 'Epanechnikov: K(u) = 3/4 · (1 − u²) für −1 ≤ u < 1, sonst 0', 'Bisquare: K(u) = 15/16 · (1 − u²)² für −1 ≤ u < 1, sonst 0', 'Gauß: K(u) = (1/√(2π)) · exp(−u²/2)',
  'Rechteck (fließendes Histogramm): K(u) = 1/2 für −1 ≤ u < 1');
B.ul(['**Große Bandweite b** → glatt, Details gehen verloren (Bias groß, Varianz klein).', '**Kleine Bandweite b** → zackig, viel Zufallsrauschen (Bias klein, Varianz groß).', 'Kern = symmetrische Dichte um 0; die Wahl des Kerns ist weniger wichtig als die Bandweite.']);
B.box('tipp', 'f̂(x₀) von Hand: für jede Beobachtung uᵢ = (x₀ − xᵢ)/b berechnen → K(uᵢ) (0, wenn |u| ≥ 1) → summieren → durch n·b teilen.');

// ───────────────── 12
B.h1('12  Maximum-Likelihood (V08)');
B.box('tipp', '1) Likelihood: L(θ) = ∏ f(xᵢ; θ)', '2) Log-Likelihood: l(θ) = log L(θ) = Σ log f(xᵢ; θ) – vereinfachen (Log-Regeln!)', '3) Ableiten: l′(θ) = …',
  '4) Nullsetzen: l′(θ̂) = 0 → nach θ̂ auflösen', '5) Hinreichende Bedingung: l″(θ̂) < 0 ⇒ Maximum', '6) Schätzwert: Daten einsetzen');
B.h2('Musterbeispiel (Klausurtyp): f(x; λ) = λ²·x·e^{−λx}, x > 0');
B.f('L(λ) = ∏ λ² xᵢ e^{−λxᵢ} = λ²ⁿ · (∏ xᵢ) · e^{−λ Σ xᵢ}', 'l(λ) = 2n·log λ + Σ log xᵢ − λ Σ xᵢ', 'l′(λ) = 2n/λ − Σ xᵢ = 0  ⇒  λ̂ = 2n / Σ xᵢ = 2 / x̄', 'l″(λ) = −2n/λ² < 0  ⇒  Maximum ✓');
B.h2('Musterbeispiel: f(x; θ) = θ·x^{θ−1}, 0 < x < 1');
B.f('l(θ) = n·log θ + (θ − 1)·Σ log xᵢ', 'l′(θ) = n/θ + Σ log xᵢ = 0  ⇒  θ̂ = −n / Σ log xᵢ', 'l″(θ) = −n/θ² < 0 ✓');
B.h2('Standard-Ergebnisse (zum Kontrollieren)');
B.table(['Modell', 'Log-Likelihood l(θ)', 'ML-Schätzer'], [['Bernoulli(π)', 'Σxᵢ·log π + (n − Σxᵢ)·log(1−π)', 'π̂ = x̄ (Anteil)'], ['Binomial B(m, π), n Beob.', 'Σxᵢ log π + (nm − Σxᵢ) log(1−π) + const', 'π̂ = x̄ / m'],
  ['Poisson(λ)', 'Σxᵢ·log λ − nλ − Σ log(xᵢ!)', 'λ̂ = x̄'], ['Exponential(λ)', 'n·log λ − λΣxᵢ', 'λ̂ = 1/x̄'], ['Normal, μ (σ² bekannt)', '−Σ(xᵢ − μ)²/(2σ²) + const', 'μ̂ = x̄'],
  ['Normal, σ² (μ bekannt)', '−(n/2)·log σ² − Σ(xᵢ − μ)²/(2σ²)', 'σ̂² = (1/n) Σ (xᵢ − μ)²'], ['Gleichverteilung U(0, θ)', 'L = θ⁻ⁿ für θ ≥ max xᵢ', 'θ̂ = max(xᵢ) (nicht ableiten!)']], [3, 4.5, 2.5]);
B.box('retter', 'Schritt 1 und 2 gehen IMMER: Produkt hinschreiben, Logarithmus nehmen, Log-Regeln anwenden. Das sind oft schon 3–4 von 10 Punkten – auch wenn das Ableiten schiefgeht.',
  'Konstanten ohne θ (z. B. Σ log xᵢ, Σ log xᵢ!) fallen beim Ableiten weg – trotzdem in l(θ) stehen lassen.');
B.box('falle', 'Produkt ∏, nicht Summe, bei der Likelihood.  ·  log(λ²ⁿ) = 2n·log λ.  ·  Beim Nullsetzen nach θ auflösen, nicht nach xᵢ.  ·  l″ muss für ALLE θ > 0 (oder an θ̂) negativ sein – Vorzeichen begründen („da n > 0 und θ² > 0“).');
B.box('tr', 'Likelihood = olasılıkların çarpımı. Log al → çarpım toplam olur. Türev al, sıfıra eşitle, θ yalnız bırak. İkinci türev negatifse maksimum.');

// ───────────────── 13
B.h1('13  Konfidenzintervalle (V10)');
B.table(['Situation', 'Konfidenzintervall zum Niveau 1 − α'], [
  ['μ, Normalverteilung, σ² bekannt', 'x̄ ± z_{1−α/2} · σ/√n'],
  ['μ, Normalverteilung, σ² unbekannt', 'x̄ ± t_{n−1; 1−α/2} · s*/√n'],
  ['μ, beliebige Verteilung, n groß (approx.)', 'x̄ ± z_{1−α/2} · s*/√n'],
  ['Anteil π (n groß)', 'π̂ ± z_{1−α/2} · √(π̂(1 − π̂)/n)'],
  ['Varianz σ², Normalverteilung', '[ (n−1)s*² / χ²_{n−1; 1−α/2} ;  (n−1)s*² / χ²_{n−1; α/2} ]']], [4, 6]);
B.ul(['Einseitige KI: nur eine Grenze, Quantil z_{1−α} bzw. t_{n−1; 1−α}.', 'KI wird **breiter**, wenn: Niveau 1 − α größer, σ größer, n kleiner.', 'Halbe Breite (Genauigkeit): e = z·σ/√n → benötigtes n = (z·σ/e)².']);
B.box('satz', '„Das 95 %-Konfidenzintervall für die mittlere Füllmenge ist [191.388; 200.612]. Bei wiederholter Stichprobenziehung überdeckt ein so konstruiertes Intervall den wahren Erwartungswert μ in 95 % der Fälle.“');
B.box('falle', 'NICHT: „μ liegt mit 95 % Wahrscheinlichkeit im Intervall“ (μ ist fest, das Intervall ist zufällig).  ·  σ² bekannt → z; σ² unbekannt → t mit n−1 Freiheitsgraden.  ·  √n nicht vergessen!');
B.box('retter', 'Formel allgemein + eingesetzte Zahlen + Intervall in eckigen Klammern [L; U]. Quantile aus der Aufgabe (Hinweis) übernehmen.');

// ───────────────── 14
B.h1('14  Statistische Tests (V11/V12)');
B.box('tipp', '1) Hypothesen H₀ und H₁ aufstellen (die zu beweisende Behauptung in H₁!)', '2) Signifikanzniveau α festlegen', '3) Teststatistik + Verteilung unter H₀ angeben',
  '4) Ablehnbereich (kritischer Wert) bzw. p-Wert bestimmen', '5) Entscheidung: H₀ ablehnen, wenn Teststatistik im Ablehnbereich bzw. p-Wert < α', '6) Antwortsatz im Sachzusammenhang');
B.h2('Hypothesen richtig wählen');
B.table(['Behauptung / Vermutung im Text', 'H₀', 'H₁', 'Ablehnbereich (Gauß-Test)'], [
  ['„weniger als / zu wenig“', 'μ ≥ μ₀', 'μ < μ₀', 'Z < −z_{1−α}'], ['„mehr als / größer“', 'μ ≤ μ₀', 'μ > μ₀', 'Z > z_{1−α}'], ['„unterscheidet sich / ungleich“', 'μ = μ₀', 'μ ≠ μ₀', '|Z| > z_{1−α/2}']], [3.5, 1.5, 1.5, 3]);
B.ul(['Das, was **statistisch abgesichert / nachgewiesen** werden soll, kommt in **H₁**.', 'Gleichheitszeichen (=, ≤, ≥) steht immer in H₀.']);
B.h2('Fehlerarten');
B.table(['', 'H₀ wahr', 'H₁ wahr'], [['H₀ ablehnen', 'Fehler 1. Art (α)', 'richtig'], ['H₀ nicht ablehnen', 'richtig', 'Fehler 2. Art (β)']], [3, 3, 3]);
B.ul(['α = maximale Wahrscheinlichkeit für den Fehler 1. Art (wird kontrolliert).', '**p-Wert:** Wahrscheinlichkeit, unter H₀ einen mindestens so extremen Wert der Teststatistik zu beobachten wie den beobachteten. p < α ⇒ H₀ ablehnen.',
  'Asymmetrie: „H₀ nicht ablehnen“ heißt NICHT „H₀ ist bewiesen“.']);
B.h2('Wichtige Tests');
B.table(['Test', 'Voraussetzung', 'Teststatistik', 'Verteilung unter H₀'], [
  ['Gauß-Test', 'Normalverteilung, σ² bekannt (oder n groß)', 'Z = (x̄ − μ₀) / (σ/√n)', 'N(0, 1)'],
  ['t-Test', 'Normalverteilung, σ² unbekannt', 'T = (x̄ − μ₀) / (s*/√n)', 't(n − 1)'],
  ['Binomialtest (Anteil)', 'n unabhängige Bernoulli-Versuche', 'Z = Anzahl Erfolge', 'B(n, π₀)'],
  ['Approx. Anteilstest', 'n groß', 'Z = (π̂ − π₀) / √(π₀(1 − π₀)/n)', '≈ N(0, 1)'],
  ['Varianztest', 'Normalverteilung', 'χ² = (n − 1)s*² / σ₀²', 'χ²(n − 1)'],
  ['Vorzeichentest (Median)', 'stetige Verteilung', 'Anzahl Beobachtungen > ϑ₀', 'B(n, 0.5)'],
  ['χ²-Anpassungstest', 'erwartete Häufigkeiten nicht zu klein', 'Σ (hⱼ − nπⱼ)² / (nπⱼ)', 'χ²(J − 1)'],
  ['χ²-Unabhängigkeitstest', 'Kontingenztafel', 'Σ Σ (hᵢⱼ − h̃ᵢⱼ)² / h̃ᵢⱼ,  h̃ᵢⱼ = hᵢ•h•ⱼ/n', 'χ²((I − 1)(J − 1))']], [2.4, 2.8, 3.4, 1.8]);
B.ul(['χ²-Tests: H₀ ablehnen, wenn Teststatistik > χ²_{1−α}(df) (immer rechtsseitig).', 'Zweiseitiger Test und KI: H₀: μ = μ₀ wird zum Niveau α abgelehnt ⇔ μ₀ liegt NICHT im (1 − α)-KI.']);
B.h2('R-Output lesen (kommt auch in Teil A vor!)');
B.ul(['`alternative = "less"` ⇔ H₁: μ < μ₀ · `"greater"` ⇔ H₁: μ > μ₀ · `"two.sided"` ⇔ H₁: μ ≠ μ₀.', 'Den Code wählen, dessen `alternative` zu deinem H₁ passt und der die richtigen Daten (`x`) verwendet.', 'Entscheidung über den p-Wert: p-value < α ⇒ H₀ ablehnen.']);
B.box('satz', 'Ablehnen: „Da T = −2 < −1.860 = −t_{8;0.95} (bzw. p = 0.040 < 0.05), wird H₀ zum Niveau 5 % abgelehnt. Es kann statistisch abgesichert werden, dass der Automat im Mittel weniger als 200 ml ausgibt.“',
  'Nicht ablehnen: „Da p = 0.134 > 0.05, kann H₀ nicht abgelehnt werden. Es kann nicht statistisch abgesichert werden, dass die mittlere Trainingsdauer unter 70 Minuten liegt.“');
B.box('falle', 'Vorzeichen beim linksseitigen Test: Vergleich mit −t bzw. −z.  ·  σ vs. σ²: Wurzel ziehen!  ·  t-Test: s* (mit n−1) und Freiheitsgrade n−1.  ·  „H₀ annehmen“ vermeiden → „H₀ kann nicht abgelehnt werden“.');
B.box('retter', 'Hypothesenpaar allein = 2 Punkte. Teststatistik-Formel allgemein + Verteilung (z. B. „T ~ t(8) unter H₀“) = Punkte, auch wenn die Zahl falsch ist. Entscheidung immer mit Vergleich (Zahl vs. kritischer Wert oder p vs. α) begründen.');

// ───────────────── 15
B.h1('15  Interpretations- & Antwortsätze (Sammlung)');
B.table(['Situation', 'Fertiger Satz (Zahlen ersetzen)'], [
  ['Mittelwert', 'Im Durchschnitt bestellen die Befragten 3.667 Pizzen pro Monat.'],
  ['Median', '50 % der Befragten bestellen höchstens 3 Pizzen, 50 % mindestens 3.'],
  ['Quartil', '25 % der Befragten bestellen höchstens 1.5 Pizzen.'],
  ['Varianz/Standardabw.', 'Die Bestellanzahl streut im Mittel um ca. 3.5 Pizzen um den Mittelwert.'],
  ['Korrelation', 'r = 0.997: sehr starker positiver linearer Zusammenhang zwischen Temperatur und Eisverkauf.'],
  ['Regression b', 'Steigt die Temperatur um 1 °C, werden laut Modell im Mittel 3.269 (Hundert) Kugeln mehr verkauft.'],
  ['Kausalität', 'Eine hohe Korrelation belegt keinen kausalen Zusammenhang; es kann eine Drittvariable vorliegen.'],
  ['bedingte W.', 'Mit einer Wahrscheinlichkeit von 10.4 % endet die Ausleihe eines Stadtrads mit einer Panne.'],
  ['Unabhängigkeit', 'Da P(A ∩ B) ≠ P(A)·P(B), sind A und B stochastisch abhängig.'],
  ['Erwartungswert', 'Im Mittel dauert ein Stromausfall 2.25 Stunden.'],
  ['Schätzer', 'Da E(T₂) = μ, ist T₂ erwartungstreu; T₁ ist wegen kleinerer Varianz effizienter.'],
  ['KI', 'Ein so konstruiertes Intervall überdeckt den wahren Parameter in 95 % der Fälle.'],
  ['Test', 'H₀ wird abgelehnt / kann nicht abgelehnt werden; es kann (nicht) statistisch abgesichert werden, dass …'],
  ['nicht sinnvoll', 'Der Median ist für das nominalskalierte Merkmal nicht sinnvoll, da die Ausprägungen keine Ordnung besitzen.']], [2.4, 7.6]);

// ───────────────── 16
B.h1('16  Tabellen: Φ(z), t-Quantile, χ²-Quantile');
B.h2('Standardnormalverteilung Φ(z) = P(Z ≤ z)  —  Zeile: z bis 1. Nachkommastelle, Spalte: 2. Nachkommastelle');
const phi = csv('phi.csv');
B.table(['z', '.00', '.01', '.02', '.03', '.04', '.05', '.06', '.07', '.08', '.09'], phi.map((r, i) => [(i / 10).toFixed(1), ...r.map(v => (+v).toFixed(4))]), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]);
B.p('Für negative z: Φ(−z) = 1 − Φ(z).  Beispiel: Φ(−1.5) = 1 − 0.9332 = 0.0668.');
B.h2('Quantile der t-Verteilung t_{df; p}');
const tq = csv('tq.csv');
B.table(['df', 'p = 0.90', '0.95', '0.975', '0.99', '0.995'], tq.map(r => [r[0], ...r.slice(1).map(v => (+v).toFixed(3))]), [1, 1, 1, 1, 1, 1]);
B.p('Für df → ∞ gehen die t-Quantile in die z-Quantile über (1.282, 1.645, 1.960, 2.326, 2.576).');
B.h2('Quantile der χ²-Verteilung χ²_{df; p}');
const cq = csv('chiq.csv');
B.table(['df', 'p = 0.025', '0.05', '0.95', '0.975'], cq.map(r => [r[0], ...r.slice(1).map(v => (+v).toFixed(3))]), [1, 1, 1, 1, 1]);

B.save(path.join(__dirname, '../../Formelsammlung_Statistik_TeilA.docx')).then(() => console.log('ok'));
