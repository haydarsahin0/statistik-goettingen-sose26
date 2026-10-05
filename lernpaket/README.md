# Lernpaket Statistik (SoSe 26)

- `Lernbuch_Tag1.pdf` – Lernbuch zum Lesen und Rechnen (Tag 1: deskriptive Statistik + R-Kurs von null an): Erklärungen, Aufgabentypen-Katalog (Typ 1–54 mit Musterlösungen), Zusatzübungen Z1–Z7, Klausurtraining nach jedem Thema, Generalprobe und ausführliche Lösungen
- `hoertexte/` – ältere Sprechtexte (nicht mehr nötig; das Lernbuch funktioniert allein)
- `uebungsdaten/Taverne.csv` – Übungsdatensatz für den R-Kurs; `uebungsdaten/R_Kurs_Tag1.R` – alle R-Befehle aus Abschnitt 1.9
- `src/` – Quellen (HTML-Inhalte, CSS, Abbildungen). Neu bauen:
  `PARTS=titel.html,tag1.html,tag1_r.html,tag1_loes.html OUTNAME=Lernbuch_Tag1.pdf src/make.sh`
- `Probeklausur2_TeilA.pdf` / `Probeklausur2_TeilB.pdf` – Generalprobe für den Zweittermin im Klausurformat (Teil A: 100 min, 75 P, Stoff V01–V13; Teil B: R, 60 min, 45 P, Daten `uebungsdaten/Bibliothek.csv`); `Probeklausur2_Loesung.pdf` – Musterlösung mit Bewertungsschlüssel und R-Code. Neu bauen: `PARTS=pk2_a.html OUTNAME=Probeklausur2_TeilA.pdf src/make.sh` (analog `pk2_b.html`, `pk2_loes.html`); Daten: `src/rwork/pk2_data.R`, R-Lösung: `src/rwork/pk2_loes.R`
