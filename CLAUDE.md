# Vorlesungsunterlagen Numerische Mathematik – Bachelor Bauingenieurwesen und Bau- und Umweltingenieurwesen

## Kontext

Dieses Projekt enthält die Lehrveranstaltungsunterlagen für das Modul **Numerische Mathematik** in den Bachelorstudiengängen **Bauingenieurwesen** und **Bau- und Umweltingenieurwesen** an der **Hochschule Bochum**.

Die Python-Einführung für die Studierenden (Ordner `python-und-jupyter-notebooks/`) liegt außerhalb dieses Projekts unter `https://github.com/matthiasbaitsch/qs-numerik`.

Die Veranstaltung basiert auf der ersten Fassung `../../numMat` (LaTeX, MATLAB) und dem ersten Neuorganisationsversuch `../../numMat_2.0` (Quarto, Julia und Python). Eine Übersicht über deren Inhalte steht in `bestandsaufnahme-vorgaenger.md`.

Aufbau und Werkzeuge folgen **Numerik partieller Differentialgleichungen** (`../../numPDE_2.1/unterlagen`), das wiederum dem Informatik-Projekt (`../../informatik-master_2.0/unterlagen`) folgt. Die Projekte sollen sich möglichst wenig unterscheiden – bei Strukturfragen erst in numPDE nachsehen und dessen Lösung übernehmen. Der wesentliche Unterschied: Programmiert wird hier in **Python** (Umgebung mit uv), nicht in Julia; die Skripte in `skripte/` bleiben Julia.

## Projektstruktur

- Inhalte liegen in `bausteine/NN-thema/` mit `about.yaml` (Titel, Teil, Inhalt, Dauer, target), `folien/folien.qmd`, `aufgaben/*.qmd` und jeweils `bilder/`.
- **Namensregel:** Von Hand vergebene Namen beschreiben nur den Inhalt (ohne Teil, ohne Baustein); alles, was vom Ort abhängt, erzeugt ein Skript. Bausteinordner `NN-slug`, Aufgaben `NN-inhalt.qmd`.
- Die Bausteine sind über das Feld `teil` in `about.yaml` gruppiert: `Fachwerke` (01–04), `Anfangswertprobleme` (05–07), `Wärmeleitung` (08–09). Ordnernamen und Nummern enthalten den Teil bewusst nicht; das Skript bildet daraus den Folientitel „Teil: Titel“ und die Slugs. Bausteintitel deshalb so wählen, dass sie den Teil nicht wiederholen. Geplante Bausteine stehen in `todo.md`.
- **Stabilität** wird bei den Anfangswertproblemen nur als Phänomen gezeigt (Van der Pol), systematisch (Testgleichung, Schrittweitenbeschränkung, implizites Euler-Verfahren) erst bei der Wärmeleitung, wo die Schrittweitengrenze anschaulich wird.
- **Notebooks:** Notebooks werden als `.qmd` gepflegt (Code-Zellen ` ```{python} `, ohne YAML-Kopf und ohne Titelzeile) und erst vom Lernpfad-Skript nach `.ipynb` gerendert (Extension tinh, Format `tinh-notebook-ipynb`, Filter `solution-scaffold.lua`; Kernel `python3` setzt das Skript im Kopf). Ablauf, Gerüst und Lösung (`.tinh-solution`, `.tinh-scaffold`, `target` in `about.yaml`), ein Notebook `notebook.qmd` je Projekt in `folien/projekt` und `aufgaben/projekt`, Aufgaben als Abschnitte `## Aufgabentitel`, keine Nummern in Überschriften und Texten: alles wie in numPDE (`../../numPDE_2.1/unterlagen/CLAUDE.md`, Abschnitt Projektstruktur). Weil Pandoc den Markdown neu schreibt, keine Zeilen, die wie Listen aussehen, aber keine sein sollen.
- **Auslieferung:** wie in numPDE – das Lernpfad-Skript zippt jedes Notebook einzeln (`…-folien.zip`, `…-aufgaben.zip`, Lösungen mit Hash). Die Studierenden richten einen Ordner `numerische-mathematik/` mit `folien/`, `aufgaben/`, `projekt-folien/` und `projekt-aufgaben/` ein, beschrieben im Foliensatz `lernpfad/veranstaltung/ordner-einrichten` (Struktur unter `zip/numerische-mathematik/`). Die Pakete installieren die Studierenden mit `uv sync` im jeweiligen Projektordner – keine `pip`-Zellen in den Notebooks.
- Musterlösungen zu Programmieraufgaben liegen in `aufgaben/projekt/` (`notebook.qmd` und `src/`). `src/` enthält den Code-Stand nach Bearbeitung des Blatts (z.B. `truss.py`, `odesolve.py`); Dateien aus früheren Bausteinen werden kopiert und weiterentwickelt, Änderungen vorerst von Hand in spätere Kopien übertragen. Die Notebooks laden `src/` mit `%load_ext autoreload` und `%autoreload 2` und importieren daraus (`from src.truss import …`), jeweils in derselben Zelle, damit jeder Aufgabenabschnitt auch für sich läuft.
- Musterlösungen zu Papieraufgaben, Ausprobier-Notebooks (`projekt-playground`), Vorlesungsnotebooks (`folien/projekt/`), `aufgaben/reserve/`: wie in numPDE.
- In `lernpfad/` werden nur die Unterordner `c/` automatisch generiert (`skripte/make-learning-path.jl`, aufgerufen über `make prepare-render`) – nie manuell bearbeiten, alle inhaltlichen Änderungen gehen in `bausteine/`. Die `_metadata.yml` in `lernpfad/folien/`, `lernpfad/aufgaben/` sind eingecheckt und dürfen bearbeitet werden.
- `pyproject.toml`, `uv.lock` und `.code-workspace` in allen Projektordnern (`bausteine/*/*/projekt*` und `lernpfad/veranstaltung/*/zip/*/projekt-*`) kommen aus `bausteine/00-templates` und werden mit `make copy-templates` (`skripte/copy-templates.jl`) verteilt – Änderungen nur in der Vorlage, danach `uv lock` in der Vorlage. Der Workspace-Name wird aus dem Ordner gebildet und immer neu geschrieben.
- **Folien** der Bausteine werden nur als PDF ausgeliefert (`tinh-slides-typst`). Inhalt sind vorerst die handschriftlichen Notizen (deutsch, PDF im Querformat) in `bausteine/NN/folien/notizen/`, seitenweise eingebunden mit `#notiz("notizen/x.pdf", 3)` wie in numPDE. Jedes Notiz-PDF beginnt mit einem Abschnitt `# Thema`, der die handschriftliche Titelseite ersetzt. Eigene Folien (`## Titel`) lassen sich beliebig dazwischen ergänzen. Die Folien zur Veranstaltung (`lernpfad/veranstaltung/`) dürfen Reveal.js sein.
- `lernpfad/veranstaltung/` enthält Folien, die nur zu dieser Veranstaltung gehören (Einführung, Ordner einrichten), ein Ordner je Foliensatz mit `folien.qmd`.
- Aussehen kommt aus der Quarto-Extension `tinh` (`~/sciebo/lehrveranstaltungen/quarto-tinh`), Logo aus der Brand der Hochschule Bochum, beide aktualisiert mit `make update-extension` – `_extensions/` und `_brand/` nicht von Hand bearbeiten.
- Skripte (Julia) liegen in `skripte/` und dürfen direkt bearbeitet werden. Stil: kein `continue` und kein `break`. `skripte/make-learning-path.jl` ist eine Kopie aus numPDE; Unterschiede nur `SITE_URL`, `COURSE_TITLE` und der Kernel im Notebook-Kopf. Verbesserungen möglichst in beiden Kopien nachziehen.
- `bestandsaufnahme-vorgaenger.md` – Bestandsaufnahme von `../../numMat` und `../../numMat_2.0`

## Technischer Aufbau

- **Format:** Quarto (`.qmd`), Deutsch
- **Programmierung:** Python mit numpy, scipy, matplotlib (Umgebung mit uv, Vorlage in `bausteine/00-templates`)
- Python-Code in Folien und Aufgaben ist **statisch** (` ```{.python} `, wird beim Rendern nicht ausgeführt). Ausnahme: Zellen ` ```{python} ` werden beim Rendern ausgeführt (`engine: jupyter`, `execute: echo: false`). Die Umgebung ist eine Kopie der Vorlage im Wurzelordner (`pyproject.toml`, `uv.lock`, erzeugt von `make copy-templates`, nicht eingecheckt); der `Makefile` rendert mit `uv run --group render quarto`. Gemeinsame Einstellungen stehen in `_setup.py`; die erste ausgeführte Zelle lädt sie mit `import sys; from pathlib import Path; exec(open(Path(sys.prefix).parent / "_setup.py").read())`. Gerendert wird nur vom Nutzer.
- Veröffentlicht wird über GitHub Pages unter `https://matthiasbaitsch.github.io/numMat2` (Workflow `.github/workflows/build.yaml`).

## Zusammenarbeit mit dem Nutzer

- Den Nutzer duzen
- Auf Fragen („wie geht…?", „kann ich…?", „warum…?") zuerst nur erklären – Dateien erst ändern, wenn der Nutzer ausdrücklich darum bittet
- Vor jeder Änderung an Dateien erst erklären, was geplant ist, und auf Zustimmung warten – auch wenn die Aufgabe klar scheint

## Hinweise zur Zusammenarbeit

- Notizen und Erinnerungen gehören in diese Datei (`CLAUDE.md`)
- Kein Memory-Verzeichnis anlegen – weder im Projekt noch anderswo. Das eingebaute auto-memory-System nicht verwenden.

## Inhaltliche Richtlinien

- Alle Texte auf **Deutsch** (Siezen: „Sie"), auch die Folien
- Folien: Titel ist das Thema, `subtitle` immer der Veranstaltungstitel „Numerische Mathematik“ (bei Bausteinen setzt ihn das Lernpfad-Skript, bei `lernpfad/veranstaltung/*/folien.qmd` von Hand)
