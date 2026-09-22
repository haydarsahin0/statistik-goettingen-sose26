# Lernplan Statistik und Data Science I

Ein Lernprogramm von **18 Tagen** (14.09. – 01.10.2026), das den gesamten Stoff
der Vorlesung *Statistik und Data Science I* (SoSe 2026, Universität Göttingen)
Tag für Tag in einfacher Sprache erklärt — mit vielen Beispielen, R-Code und
einem Selbsttest samt Lösungen an jedem Tagesende.

## Kompaktkurs: alles in 5 Tagen

Die schnellste Route zur Klausur. Jeder Kompakt-Tag erklärt ein Stoffpaket von
null an, prüft es mit Klausuraufgaben im Stil der Probeklausur und endet mit einer
**Klausur-Simulation** (46 Punkte, 60 Minuten) samt Punkteschema. Die Aufgaben
sind mindestens so schwer wie die Probeklausur. Die echte Probeklausur bleibt für
die Generalprobe nach Tag 5 unberührt.

Jeder Kompakt-Tag hat außerdem einen **Block E** mit allem, was in Vorlesungen,
Tutorien, Testaten und R-Skripten vorkommt, aber nicht in der Probeklausur — und
am Ende eine **Stoffabdeckungs-Tabelle**, die jede Quelle der passenden Stelle im
PDF zuordnet.

| Datei | Inhalt | Klausurbezug |
|---|---|---|
| `Kompakt_1_Beschreibende_Statistik.pdf` | Skalen, Häufigkeiten, Verteilungsfunktion, Histogramm, klassierte Daten, Lage, Streuung, Quantile, Boxplot, R-Grundlagen | A1, A2, B a–e |
| `Kompakt_2_Zusammenhaenge_und_Wahrscheinlichkeit.pdf` | Kontingenztafel, χ², Kovarianz, Korrelation, Spearman, Kausalität, Mengen, Laplace, bedingte Wahrscheinlichkeit, Bayes | A3, A4, A5 |
| `Kompakt_3_Zufallsvariablen_und_Verteilungen.pdf` | Wahrscheinlichkeits-, Dichte- und Verteilungsfunktion, E und Var, Binomial, Poisson, Exponential, Weibull, Normal, ZGWS, R d/p/q/r, Φ-Tabelle | Basis für A3c, A6–A8, B f |
| Tag 4 (folgt) | Maximum-Likelihood, Schätzgüte, Kerndichte, Konfidenzintervalle | A6, A7, B f–g |
| Tag 5 (folgt) | Tests, p-Wert, `t.test()`, Teil B komplett (Funktionen, Schleifen, `paste`) | A8, B h |

## Die ausführlichen Tages-PDFs

Alles, was du zum Lernen brauchst, liegt in **`pdf/`**:

| Datei | Inhalt |
|---|---|
| `00_Lernplan_Uebersicht.pdf` | Der Gesamtplan: Klausurformat, Punkteverteilung der Probeklausur, alle Tage, Formelsammlung, Fortschrittsliste |
| `Tag_00_Mathe_Fundament.pdf` | Mengen, Summen- und Produktzeichen, Logarithmusregeln, Ableiten, zweite Ableitung, R-Basis (Testat 0) |
| `Tag_01_Daten_und_Merkmalstypen.pdf` | Grundbegriffe, diskret/stetig, Skalenniveaus, Stichproben, R-Grundlagen |
| `Tag_02_Haeufigkeiten_und_Histogramm.pdf` | Absolute/relative Häufigkeiten, Klassen, Säulendiagramm vs. Histogramm, Dichte, empirische Verteilungsfunktion |
| `Tag_03_Lagemasse.pdf` | Mittelwert, Median, Modus, klassierte und geschichtete Daten, Schiefe, lineare Transformation |
| `Tag_04_Quantile_Streuung_Boxplot.pdf` | Quantilregel, Varianz, Verschiebungssatz, S² vs. S²*, IQR, Boxplot und Ausreißer |
| `Tag_05_Kontingenztafel_und_Chi_Quadrat.pdf` | Kontingenztafel, Rand- und bedingte Verteilungen, Unabhängigkeit, erwartete Häufigkeiten, χ²-Koeffizient, `table()`/`cut()` |
| `Tag_06_Korrelation_und_Kausalitaet.pdf` | Streudiagramm, Kovarianz, Bravais-Pearson, Spearman (mit Bindungen), Interpretation, Kausalität, Klausur-Zwilling zu Probeklausur A5 |

**Sprache:** Der Statistikteil ist durchgehend auf Deutsch (einfache Sätze,
Klausurvokabular). Der R-Teil hat zusätzlich türkische Erklärkästen, weil dort
nicht die Statistik, sondern die Syntax die Hürde ist. Beides ist optisch klar
getrennt.

Der Plan ist nach der **Punkteverteilung der Probeklausur** gebaut, nicht nach der
Reihenfolge der Folien. Die Klausur besteht aus Teil A (75 Punkte, 100 Minuten,
handschriftlich) und Teil B (45 Punkte, 60 Minuten, R in ILIAS).

Jedes Tages-PDF hat denselben Aufbau:

1. **Titelseite** mit Lernzielen und Zeitbedarf
2. **Teil 1 · Lernen** — nummerierte Schritte mit Definitionen, Beispielen und Warnungen
3. **R-Ecke** — der passende R-Code zum Thema, jeder Block mit einer
   türkischen Lesehilfe (`TR`-Kasten): jede Funktion und jedes Argument
   Zeile für Zeile erklärt
4. **Wortschatz** und **Spickzettel** — die Zusammenfassung zum Abschreiben
5. **Teil 2 · Test** — Aufgaben im Klausurformat, mit Dezimalpunkt und den Rundungsregeln der Klausur
6. **Teil 3 · Lösungen** — ausführlich gerechnet, mit Selbstauswertung

Ab Tag 5 kommen dazu: eine **Tagesübersicht** (Lernpfad mit Zeitangaben,
Klausur-Radar mit den betroffenen Probeklausur-Punkten, persönlicher Fokus aus
den bisherigen Tests), eine **Kernaussage** am Anfang jedes Schritts, grüne
Kästen **„So schreibst du es in der Klausur“** mit dem Wortlaut der offiziellen
Musterlösung, und im Test ein **eigenes Antwortfeld für jede Teilaufgabe**.

## Grundlage

Die Inhalte folgen den Vorlesungsfolien `SDS1_V01` – `SDS1_V13`, den R-Skripten
`01StatDS-*` – `12StatDS-*`, den Tutorien und Testaten sowie der `Probeklausur_ATeil`,
der `Probeklausur_BTeil` und den Übungsaufgaben `Maximum_Likelihood_*` aus diesem
Repository.

## PDFs neu bauen

Die PDFs werden aus den HTML-Quellen in `src/` erzeugt (Chromium + KaTeX):

```bash
cd lernplan/build
npm install
node build.mjs           # alle PDFs
node build.mjs tag-01    # nur ein Tag
```

Der Pfad zum Chromium-Binary lässt sich über die Umgebungsvariable
`CHROME_PATH` setzen.

## Aufbau des Ordners

```
lernplan/
├── pdf/            fertige PDFs — zum Lernen
├── src/            HTML-Quellen, eine Datei je Tag
└── build/
    ├── build.mjs   Build-Skript (HTML -> PDF)
    ├── theme.css   das Pastell-Design
    └── assets/     eingebettete Schriften und KaTeX-Styles
```
