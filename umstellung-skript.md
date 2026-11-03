# Umstellung LaTeX-Skript → Quarto

Stand: 3. November 2026. Quelle: `../../numMat/01-skript`. Die Kapitel liegen als `skript/skript.qmd` in den Themen
unter `bausteine/`, das Lernpfad-Skript setzt sie zum Book in `lernpfad/skript/c/` zusammen.

## Überblick

| Altes Kapitel | Thema | Kapitel im Skript |
|---|---|---|
| `__s-01-modellbildung` | `01-modellierung` | Modellierung von Stabtragwerken |
| `__s-02-fachwerkstab` bis Abschnitt Stabendkräfte | `02-stabendkraefte` | Fachwerke: Stabendkräfte |
| `__s-02-fachwerkstab` ab Abschnitt Kräftegleichgewicht | `03-berechnung` | Fachwerke: Berechnung |
| `__a-01-eine-unbekannte-funktion` | `04-loesungsverfahren` | |
| `__a-02-dynamik-massepunkt` | `05-massepunkte` | |
| `__a-03-mehrere-unbekannte-funktionen` | `06-systeme-von-differentialgleichungen` | |

## Allgemeine Entscheidungen

- Wie in Mathematik B: Text neben Bild untereinander, Absätze mit `\paragraph` als fetter Anfang, Abbildungen mit
  mehreren Bildern als Quarto-Abbildung mit Unterbildern (`layout`).
- Makros aufgelöst: `\mmund` → `\quad\text{und}\quad`, `\mlin` → `_{\text{lin}}`; `\mmat`, `\R`, `\mtran`, `\SI`
  kommen aus der Extension tinh.
- `\intertext`, `multline` und `align` (nicht in MathJax) als `aligned` bzw. getrennte Gleichungen.
- Zeichnungen per `pdf2svg` aus `*-eps-converted-to.pdf` als SVG, Originale (EPS, PDF) in `skript/bilder/orig/`.
  Rasterbilder in PDFs (`everything-is-3d`, `hoersaal-h9`) mit `pdftoppm -r 300` als PNG. Fotos mit sprechenden
  Namen (`knoten-muengsten.jpg` statt `geruest-06302.jpg` usw.).
- Literatur (`numerische-mathematik-skript.bib`) nach `bausteine/bibliographie.bib`, Literaturverzeichnis in
  `lernpfad/skript/literatur.qmd`.
- Tippfehler und Kommas stillschweigend korrigiert; inhaltliche Korrekturen siehe unten.

## Modellierung von Stabtragwerken

- Listen mit `\pro`/`\con` als Aufzählungen mit $+$ und $-$.

## Fachwerke

- Kapitel geteilt: „Fachwerke: Stabendkräfte“ (Einleitung, Grundidee, Stabendkräfte) und „Fachwerke: Berechnung“
  (Rechenbeispiel, Assemblierungsmatrix, Berechnungsprozedur).
- Korrekturen:
  - Tangentialebene: $f : \R^2 \to \R$ statt $f : \R^2 \to \R^2$.
  - Linearisierte Normalkraft: Summanden in der Reihenfolge $u_{11}, u_{12}, u_{21}, u_{22}$ (vorher $u_{11}, u_{21},
    u_{12}, u_{22}$).
  - Knotenlast: $\mathbf{F}_2 = (0, R_{22})^\top$ statt $(0, R_{12})^\top$.
  - Beitrag von Stab 1: $\mathbf{t}_0$ statt $\mathbf{t}$ und $l_0$ statt $l$; globale Stabendkräfte mit Hut.
  - Normalkraft Stab 2: $\mathbf{d}_0 = (0, 1)^\top$ und Verschiebungsdifferenz $(0.027, 0.0045)^\top$ (vorher
    $(1, 0)^\top$ und $(0.0045, 0)^\top$, Ergebnis 90 kN war richtig). Rechenbeispiel mit Python nachgerechnet.
  - Normalkräfte: Formel und Stabrichtungen (aus der Abbildung) vorangestellt, $EA = 60000$ kN genannt (vorher
    ohne Einheit, während die Verschiebungen in MN gerechnet wurden).
- Beispiel Indexvektor als `#exm-indexvektor`.

## Anfangswertprobleme erster Ordnung

- Kästen mit Rechenvorschriften (`framed`) als Definitionen `#def-euler`, `#def-halbschritt`, `#def-runge-kutta`, Bild
  und Formel untereinander. Anfangswertproblem als `#def-anfangswertproblem`, Beispiele als `#exm-…`.
- Bild `halbschritt-integration-2` war nicht referenziert, jetzt aus dem Beispiel zum Halbschrittverfahren.
- MATLAB-Code (`00-pics/matlab`) und Mathematica-Notebook zum Richtungsfeld in `skript/bilder/orig/`.
- Korrekturen:
  - Beispiel Anfangswertproblem: $F(x, y) = x - y$ statt $y - x$ (passt zur Differentialgleichung und zur Lösung).
  - Leonhard statt Leonard Euler.

## Bewegung von Massepunkten

- Korrekturen:
  - Auto im Kreis: Querbeschleunigung $(625/162)/9.81 \approx 0.39\,g$ statt $0.04\,g$.
  - Dämpfer: Dämpfungskonstante $c$ (wie in der Formel) statt $d$.
  - Doppelpendel, Gleichung (f1): fehlende Klammer ergänzt, rechte Seite
    $-\dot\theta_1^2\cos\theta_1(\tan\theta_1-\tan\theta_2) - \dot\theta_2^2\cos\theta_2(\tan\theta_1-\tan\theta_2) - g/l$
    statt $(2\tan\theta_1+\tan\theta_2)$ bzw. $(\tan\theta_1+\tan\theta_2)$. Mit sympy geprüft: (f2) und die
    Endgleichungen waren richtig.
  - Abschnitt „Dynamik des Massepunktes“ → „Dynamik des Massepunkts“ (wie „Kinematik des Massepunkts“).

## Anfangswertprobleme mit mehreren unbekannten Funktionen

- Abbildungen `flowfield-*` mit dem `trim` aus dem LaTeX (50 75 45 75 bp bei 150 dpi) per `magick -crop`
  zugeschnitten, Originale in `orig/`.
- Rechenvorschrift Euler für Systeme als `#def-euler-system`, Verweis auf das Kapitel zu einer unbekannten
  Funktion mit `@sec-anfangswertprobleme`.
- Abschnitt „Anwendungen“ (SIR-Modell, Massepunktsysteme) weggelassen, im Original nur „TODO“ (siehe `todo.md`).
- Korrekturen:
  - Gebiet „von 20 m auf 10 m“ statt „von 10 m auf 20 m“ (passend zu $[0, 20] \times [-5, 5]$).
  - d'Alembert statt d'Alambert.
  - Bildunterschrift `flowfield-all`: $x_2$-Achse statt $y$-Achse.
  - „Die Rechnung können Sie dem Matlab-File auf Moodle entnehmen“ → „Die Rechnung lässt sich leicht programmieren“.
