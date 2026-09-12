# Lernplan Statistik und Data Science I

Ein Lernprogramm von **19 Tagen** (12.09. – 30.09.2026), das den gesamten Stoff
der Vorlesung *Statistik und Data Science I* (SoSe 2026, Universität Göttingen)
Tag für Tag in einfacher Sprache erklärt — mit vielen Beispielen, R-Code und
einem Selbsttest samt Lösungen an jedem Tagesende.

## Die fertigen PDFs

Alles, was du zum Lernen brauchst, liegt in **`pdf/`**:

| Datei | Inhalt |
|---|---|
| `00_Lernplan_Uebersicht.pdf` | Der Gesamtplan: alle 19 Tage, Tagesablauf, Fortschrittsliste |
| `Tag_01_Daten_und_Merkmalstypen.pdf` | Grundbegriffe, diskret/stetig, Skalenniveaus, Stichproben, R-Grundlagen |
| `Tag_02_Haeufigkeiten_und_Histogramm.pdf` | Absolute/relative Häufigkeiten, Klassen, Säulendiagramm vs. Histogramm, Dichte |

Jedes Tages-PDF hat denselben Aufbau:

1. **Titelseite** mit Lernzielen und Zeitbedarf
2. **Teil 1 · Lernen** — nummerierte Schritte mit Definitionen, Beispielen und Warnungen
3. **R-Ecke** — der passende R-Code zum Thema
4. **Wortschatz** und **Spickzettel** — die Zusammenfassung zum Abschreiben
5. **Teil 2 · Test** — Aufgaben (20 Punkte)
6. **Teil 3 · Lösungen** — ausführlich gerechnet, mit Selbstauswertung

## Grundlage

Die Inhalte folgen den Vorlesungsfolien `SDS1_V01` – `SDS1_V13`, den R-Skripten
`01StatDS-*` – `12StatDS-*` sowie den Tutorien und Testaten aus diesem Repository.

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
