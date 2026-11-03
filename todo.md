# TODO

## Grundgerüst

- [ ]  Rendern mit Python testen: `make copy-templates`, `uv sync --group render`, `make render`
- [ ]  Notebook-Erzeugung mit Python prüfen (Kernel `python3` im `.ipynb`, Gerüst `# ...`)
- [ ]  GitHub-Repo `numMat2` anlegen, Pages aktivieren
- [ ]  Einführung ausbauen (Material: `../../numMat/02-folien/00-einfuehrung`)
- [ ]  Foliensatz zur Python-Einführung bzw. Ordner `python-und-jupyter-notebooks` klären (in `ordner-einrichten` erwähnt)

## Bausteine

| Nr. | Teil | Titel | Notizen | Aufgaben aus |
|---|---|---|---|---|
| 01 | Fachwerke | Grundlagen (Modellbildung, Stabendkräfte) | NM S 01–05 | 1.0 Blatt 1 |
| 02 | Fachwerke | Erzeugung und Darstellung | – | 2.0 Blatt 2 |
| 03 | Fachwerke | Berechnung | NM S 06 | 2.0 Blatt 3 |
| 04 | Fachwerke | Ergebnisse und Anwendungen | – | 2.0 Blatt 4 |
| 05 | Anfangswertprobleme | Lösungsverfahren | vor-corona `02-awps` | 2.0 Blatt 5 |
| 06 | Anfangswertprobleme | Systeme und Massepunkte | vor-corona `03-dynamik` | 1.0 Blätter 6 und 8 |
| 07 | Anfangswertprobleme | Genauigkeit und Startwerte | NM A 5 | 2.0 Blatt 6 (Van der Pol als Phänomen) |
| 08 | Wärmeleitung | Grundlagen | NM W 01–03 | 2.0 Blatt 7 |
| 09 | Wärmeleitung | Stabilität | NM W 04 | 2.0 Blatt 7 (Schrittweite, implizites Euler) |

- [ ]  01 Grundlagen
- [ ]  02 Erzeugung und Darstellung
- [ ]  03 Berechnung
- [ ]  04 Ergebnisse und Anwendungen
- [ ]  05 Lösungsverfahren
- [ ]  06 Systeme und Massepunkte
- [ ]  07 Genauigkeit und Startwerte
- [ ]  08 Wärmeleitung: Grundlagen
- [ ]  09 Wärmeleitung: Stabilität

## Extension `tinh`

- [ ]  `notebook.lua` und `solution-scaffold.lua`: Kernel für Python (`python3` statt `python`) in der Extension
  setzen, dann den `jupyter`-Eintrag im Kopf in `render_notebook` (`skripte/make-learning-path.jl`) entfernen
