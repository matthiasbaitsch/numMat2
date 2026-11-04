# TODO

## Grundgerüst

- [X]  Rendern mit Python testen
- [X]  Notebook-Erzeugung mit Python prüfen (Kernel `python3` im `.ipynb`, Gerüst `# ...`)
- [ ]  GitHub-Repo `numMat2` anlegen, Pages aktivieren
- [ ]  Einführung ausbauen (Material: `../../numMat/02-folien/00-einfuehrung`), Video „NM 01 Begrüßung“
  (https://youtu.be/MbV3t8TYWRU, 16:50) einbinden
- [X]  Lernpfad-Skript: Skript-Book in `lernpfad/skript/c/` erzeugen, `make render-skript`
- [X]  Skript-Book rendern (HTML und PDF mit Typst)

## Themen

| Nr. | Teil | Titel | Skript (LaTeX) | Notizen | Aufgaben aus |
|---|---|---|---|---|---|
| 01 | Stabtragwerke | Modellierung | `s-01` | S 01 | – |
| 02 | Stabtragwerke | Stabendkräfte | `s-02` bis Stabendkräfte | S 02–05 | 1.0 Blatt 1, 2.0 Blatt 2 |
| 03 | Stabtragwerke | Berechnung | `s-02` ab Kräftegleichgewicht | S 06 | 2.0 Blätter 3 und 4 |
| 04 | Anfangswertprobleme | Lösungsverfahren | `a-01` | vor-corona `02-awps` | 2.0 Blatt 5 |
| 05 | Anfangswertprobleme | Massepunkte | `a-02` | vor-corona `03-dynamik` | 1.0 Blatt 6 |
| 06 | Anfangswertprobleme | Systeme von Differentialgleichungen | `a-03` | – | 1.0 Blatt 8 |
| 07 | Anfangswertprobleme | Genauigkeit und Startwerte | – | NM A 5 | 2.0 Blatt 6 (Van der Pol als Phänomen) |
| 08 | Wärmeleitung | Grundlagen | – | NM W 01–03 | 2.0 Blatt 7 |
| 09 | Wärmeleitung | Stabilität | – | NM W 04 | 2.0 Blatt 7 (implizites Euler) |

Je Thema: Skript · Folien · Aufgaben (mit Python-Musterlösung)

- [X]  01 Modellierung: ~~Skript~~ · ~~Folien~~
- [X]  02 Stabendkräfte: ~~Skript~~ · ~~Folien~~ · ~~Aufgaben~~
- [X]  03 Berechnung: ~~Skript~~ · ~~Folien~~ · ~~Aufgaben~~
- [ ]  04 Lösungsverfahren: ~~Skript~~ · Folien · Aufgaben
- [ ]  05 Massepunkte: ~~Skript~~ · Folien · Aufgaben
- [ ]  06 Systeme von Differentialgleichungen: ~~Skript~~ (ohne Anwendungen) · Folien · Aufgaben
- [ ]  07 Genauigkeit und Startwerte: Folien · Aufgaben
- [ ]  08 Wärmeleitung Grundlagen: Folien · Aufgaben
- [ ]  09 Wärmeleitung Stabilität: Folien · Aufgaben

## Inhalte langfristig

- [ ]  Skripttexte für 07–09 schreiben (bisher nur Notizen)
- [ ]  Skript 06: Abschnitt Anwendungen schreiben (SEIR-Modell, Massepunktsysteme wie Zweimassenschwinger und
  Doppelpendel als System erster Ordnung), Material: Videos A 4, 1.0 Blatt 8
- [ ]  Videos für 04 Lösungsverfahren aufnehmen (fehlen in der Playlist)
- [ ]  Videos mit Matlab (A 4.2.3, A 4.2.5, A 5.2.2, A 5.2.4) durch Python-Fassungen ersetzen
- [ ]  Zusatzthemen aus der Playlist einordnen: „NM Z 01 FVM 2D“ (https://youtu.be/ter-OxxZZqU, 4:36),
  „NM Z 02 1 Akustik FVM 1D“ (https://youtu.be/oiUoPpKUwr8, 33:39), z.B. für Studienarbeiten
- [ ]  MATLAB-/Mathematica-Grafiken im Skript als Python-Code neu erzeugen

## Extension `tinh`

- [ ]  Schlichteres Book-Layout für `tinh-notes-typst` (todo in quarto-tinh), danach `make update-extension`
