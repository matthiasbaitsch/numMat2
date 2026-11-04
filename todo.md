# TODO

## Grundgerüst

- [X]  Rendern mit Python testen
- [X]  Notebook-Erzeugung mit Python prüfen (Kernel `python3` im `.ipynb`, Gerüst `# ...`)
- [X]  GitHub-Repo `numMat2` anlegen, Pages aktivieren
- [ ]  Einführung ausbauen (Material: `../../numMat/02-folien/00-einfuehrung`), Video „NM 01 Begrüßung“
  (https://youtu.be/MbV3t8TYWRU, 16:50) einbinden
- [X]  Lernpfad-Skript: Skript-Book in `lernpfad/skript/c/` erzeugen, `make render-skript`
- [X]  Skript-Book rendern (HTML und PDF mit Typst)

## Themen

| Nr. | Teil | Titel | Skript (LaTeX) | Notizen | Aufgaben aus |
|---|---|---|---|---|---|
| 01 | Stabtragwerke | Modellierung | `s-01` | S 01 | – |
| 02 | Stabtragwerke | Stabendkräfte | `s-02` bis Stabendkräfte | S 02–05 | 1.0 Blatt 1, 2.0 Blatt 2 |
| 03 | Stabtragwerke | Datenstrukturen und Visualisierung | – | – | 2.0 Blatt 2 (Erzeugung und Darstellung) |
| 04 | Stabtragwerke | Berechnung | `s-02` ab Kräftegleichgewicht | S 06 | 2.0 Blätter 3 und 4 |
| 05 | Anfangswertprobleme | Lösungsverfahren | `a-01` | vor-corona `02-awps` | 2.0 Blatt 5 |
| 06 | Anfangswertprobleme | Massepunkte | `a-02` | vor-corona `03-dynamik` | 1.0 Blatt 6 |
| 07 | Anfangswertprobleme | Systeme von Differentialgleichungen | `a-03` | – | 1.0 Blatt 8 |
| 08 | Anfangswertprobleme | Genauigkeit und Startwerte | – | NM A 5 | 2.0 Blatt 6 (Van der Pol als Phänomen) |
| 09 | Wärmeleitung | Grundlagen | – | NM W 01–03 | 2.0 Blatt 7 |
| 10 | Wärmeleitung | Stabilität | – | NM W 04 | 2.0 Blatt 7 (implizites Euler) |

Je Thema: Skript · Folien · Aufgaben (mit Python-Musterlösung)

- [X]  01 Modellierung: ~~Skript~~ · ~~Folien~~
- [X]  02 Stabendkräfte: ~~Skript~~ · ~~Folien~~ · ~~Aufgaben~~
- [ ]  03 Datenstrukturen und Visualisierung: Skript · ~~Aufgaben~~
- [ ]  04 Berechnung: ~~Skript~~ (ohne Postprocessing) · ~~Folien~~ · ~~Aufgaben~~
- [X]  05 Lösungsverfahren: ~~Skript~~ · ~~Folien~~ · ~~Aufgaben~~
- [X]  06 Massepunkte: ~~Skript~~ · ~~Folien~~ · ~~Aufgaben~~
- [ ]  07 Systeme von Differentialgleichungen: ~~Skript~~ (ohne Anwendungen) · Folien · Aufgaben
  - Folien: `../../numMat/99-vor-corona/03-notizen/03-dynamik-massepunkte.pdf` Seiten 3, 4 (Einmassenschwinger als
    System erster Ordnung, Beispiel) und 9 (Mehrmassenschwinger) als eigene Datei, z.B.
    `NM A 3 Massepunktsysteme.pdf` (Dateinamen in `c/notizen` müssen eindeutig sein)
  - Aufgaben: 1.0 Blatt 8 (SEIR-Modell, Zweimassenschwinger, Musterlösung in `uebungsblatt-08/`); 2.0 Blatt 6
    Abschnitt "Erweiterung Programmcode" (Löser für Systeme)
  - Python: `odesolve.py` aus 05 kopieren, die Löser können schon Vektoren als Anfangswert; Einmassenschwinger aus
    `../../numMat_2.0/01-uebungsaufgaben/musterloesungen/anfangswertprobleme-julia/einmassenschwinger.qmd`
- [ ]  08 Genauigkeit und Startwerte: Folien · Aufgaben
  - Folien: Notiz NM A 5 Eigenschaften (`../../numMat/03-notizen-videos/NM A 5 Eigenschaften.pdf`), Seite 16 von
    `03-dynamik-massepunkte.pdf` (Abhängigkeit von Startwerten)
  - Aufgaben: 2.0 Blatt 6 (Genauigkeit mit Zykloide, Stabilität mit Van der Pol nur als Phänomen, Startwerte mit
    Lorenz), 1.0 Blatt 7; Python-Lösungen in `../../numMat_2.0/01-uebungsaufgaben/musterloesungen/anfangswertprobleme-python`
    (`01-genauigkeit.ipynb`, `02-stabilitaet.ipynb`, `03-startwerte.ipynb`)
- [ ]  09 Wärmeleitung Grundlagen: Folien · Aufgaben
  - Folien: NM W 01–03 (`../../numMat/03-notizen-videos/`)
  - Aufgaben: 2.0 Blatt 7 ohne Stabilität, 1.0 Blatt 9; Python-Lösungen `instationaer-1.*.ipynb`,
    `instationaer_ar.py`, `instationaer_hilfsfunktionen.py`
- [ ]  10 Wärmeleitung Stabilität: Folien · Aufgaben
  - Folien: NM W 04
  - Aufgaben: 2.0 Blatt 7 Abschnitte "Stabilität des Lösungsverfahrens" und "Implizites Euler-Verfahren"
  - Systematisch: Testgleichung, Schrittweitenbeschränkung, implizites Euler-Verfahren (siehe CLAUDE.md)

## Inhalte langfristig

- [ ]  Skripttexte für 08–10 schreiben (bisher nur Notizen)
- [ ]  Skript 07: Abschnitt Anwendungen schreiben (SEIR-Modell, Massepunktsysteme wie Zweimassenschwinger und
  Doppelpendel als System erster Ordnung), Material: Videos A 4, 1.0 Blatt 8
- [ ]  Neue Notizen für 05 Lösungsverfahren und 06 Massepunkte: die Folien nutzen vorerst blasse Bleistiftseiten
  aus `../../numMat/99-vor-corona/03-notizen/` (`02-awps.pdf` Seiten 1–6, `03-dynamik-massepunkte.pdf` Seiten 1, 2,
  12, 13; Hochformat, schlecht lesbar)
- [ ]  Videos für 05 Lösungsverfahren aufnehmen (fehlen in der Playlist)
- [ ]  Videos mit Matlab (A 4.2.3, A 4.2.5, A 5.2.2, A 5.2.4) durch Python-Fassungen ersetzen
- [ ]  Zusatzthemen aus der Playlist einordnen: „NM Z 01 FVM 2D“ (https://youtu.be/ter-OxxZZqU, 4:36),
  „NM Z 02 1 Akustik FVM 1D“ (https://youtu.be/oiUoPpKUwr8, 33:39), z.B. für Studienarbeiten
- [ ]  MATLAB-/Mathematica-Grafiken im Skript als Python-Code neu erzeugen

## Extension `tinh`

- [ ]  Schlichteres Book-Layout für `tinh-notes-typst` (todo in quarto-tinh), danach `make update-extension`
