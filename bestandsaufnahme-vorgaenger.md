# Bestandsaufnahme der Vorgängerversionen

Stand: 2026-11-03. Überblick über die Materialien in `../../numMat` (erste Fassung) und `../../numMat_2.0` (erster Neuorganisationsversuch) als Grundlage für numMat 2.1.

## Überblick

| | numMat (1.0) | numMat_2.0 |
|---|---|---|
| Sprache | Deutsch | Deutsch (Siezen) |
| Textformat | LaTeX (Skript, Beamer, Übungsblätter) | Quarto (`.qmd`) |
| Programmierung | MATLAB (+ Mathematica) | Julia und Python parallel (Tabs) |
| Gliederung | Skript in zwei Teilen, neun Übungsblätter | Aufgabenblätter 02–07 |
| Versionskontrolle | nein | Git |

## numMat (erste Fassung)

### Skript – `01-skript/`

LaTeX-Buch `numerische-mathematik-skript.tex`, zwei Teile:

1. **Finite Elemente für Stabtragwerke**
   - `__s-01-modellbildung`: Stabtragwerke, dimensionsreduzierte Modelle, Rechenmethoden
   - `__s-02-fachwerkstab`: Grundidee, Stabendkräfte (geometrisch exakt, kleine Verformungen), Kräftegleichgewicht und Systemgrößen, Rechenbeispiel Fachwerk aus drei Stäben, Assemblierungsmatrix, Berechnungsprozedur
2. **Numerische Lösung von Anfangswertproblemen**
   - `__a-01-eine-unbekannte-funktion`: Grundlagen, explizites Euler-Verfahren, numerische Integration, Halbschrittverfahren, Runge-Kutta 4
   - `__a-02-dynamik-massepunkt`: Kinematik und Dynamik des Massepunkts, Einmassenschwinger, Doppelpendel
   - `__a-03-mehrere-unbekannte-funktionen`: Partikel in Strömung, Systeme von DGLn, SIR-Modell, Massepunktsysteme

### Handschriftliche Notizen

- `03-notizen-videos/`: NM S 01–06 (Modellierung von Stabtragwerken, Fachwerke, Stabendkräfte, geometrisch exakte Formulierung, kleine Verformungen, Kräftegleichgewicht/Systemgrößen/Verschiebungen), NM W 01–04 (Vorbemerkungen, physikalische Grundlagen, Wärmeleitung 1D, Stabilität von Lösungsverfahren), NM A 5 Eigenschaften, Akustik 1D mit FVM; Seiten auch als JPG
- `99-vor-corona/03-notizen/`: `01-matlab`, `02-awps` (33 S.), `03-dynamik-massepunkte` (16 S.), `04-optimierung` (49 S.), `05-waermeleitung` (25 S.)

### Übungsblätter – `04-uebungsaufgaben/`

LaTeX, `uebungsblatt-01` bis `-09` mit `01-musterloesung/`:

1. Grundidee der direkten Steifigkeitsmethode, Stabendkräfte exakt und vereinfacht, alternative Herleitung der Elementsteifigkeitsmatrix, Programmierung
2. Erzeugung und Darstellung von Stabtragwerken, Anwendungsbeispiel (Bogenträger)
3. Berechnung von Verschiebungen und Schnittgrößen
4. Darstellung von Berechnungsergebnissen, Anwendungen
5. Anfangswertprobleme: Grundlagen, Lösungsverfahren, Umsetzung
6. Kinematik, Kinetik
7. Genauigkeit, Stabilität, Abhängigkeit von Startwerten
8. SEIR-Modell, Zweimassenschwinger
9. Wärmeleitung 1D, implizites Euler-Verfahren (freiwillig)

### Weiteres

- `02-folien/`: Beamer; `00-einfuehrung` aktiv, mit `x` alt: Optimierung von Stabtragwerken, Anfangswertprobleme, Dynamik von Massenpunktsystemen, Wärmeleitung
- `05-matlab/`: Live-Scripts und Funktionen Stabtragwerke (`trussKe.m`, `solve.m`, `drawSystem.m`, …), Anfangswertprobleme
- `06-mathematica/`, `98-julia/`, `97-fachwerk-nichtlinear/`, `08-software/`
- `09-studienarbeiten/` 2015–2024

## numMat_2.0

- `aufgaben/NN-thema/NN-thema.qmd`: 02 Visualisierung Tragwerke, 03 Berechnung, 04 Darstellung Berechnungsergebnisse, 05 Anfangswertprobleme, 06 Systeme von DGLn (Genauigkeit mit Zykloide, Stabilität mit Van der Pol, Startwerte mit Lorenz), 07 Wärmeleitung transient (Kontrollvolumen, Stabilität, implizites Euler freiwillig); `01-stabendkraefte` leer
- `01-uebungsaufgaben/musterloesungen/`: `fachwerk-python` und `fachwerk-julia` (`structures.*`, `truss.*`, Notebooks Blatt 1–3), `anfangswertprobleme-python` und `-julia` (`odesolve.*`, Notebooks Genauigkeit, Stabilität, Startwerte, instationäre Wärmeleitung)
- `folien/paket-0.qmd`: Anfang einer Einführung (Revealjs, Julia), übernommen nach `lernpfad/veranstaltung/einfuehrung`
- `work/`: Python-Umgebung mit uv (Vorlage für `bausteine/00-templates`), `truss.py`, Notebooks zu Blatt 1 und 2
- `studienarbeiten/`: Hochhaus (Erdbeben, El Centro), Akustik 2D
- `wise-2026-27.md`: Notizen zu den Terminen im Wintersemester 2026/27
