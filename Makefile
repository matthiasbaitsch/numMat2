render: render-aufgaben render-folien render-veranstaltung render-skript

# Executed {python} cells run in the Python environment of the root folder (copy of the template, see copy-templates)
QUARTO = uv run --group render quarto

prepare-render:
	cd skripte && julia -t1 --project make-learning-path.jl || exit 1

render-aufgaben: prepare-render
	$(QUARTO) render lernpfad/aufgaben/c

render-folien: prepare-render
	$(QUARTO) render lernpfad/folien/c

render-veranstaltung: prepare-render
	$(QUARTO) render lernpfad/veranstaltung/c

# Book with its own _quarto.yml in c/ (generated from lernpfad/skript/quarto-template.yml)
render-skript: prepare-render
	$(QUARTO) render lernpfad/skript/c

# Update extension tinh (_extensions/) and brand of Hochschule Bochum (_brand/)
update-extension:
	quarto update matthiasbaitsch/quarto-tinh --no-prompt
	quarto use brand matthiasbaitsch/hsbo-brand --force

# Copy pyproject.toml, uv.lock and workspace file from bausteine/00-templates to all project folders, including the
# folder structure for the students (lernpfad/veranstaltung/*/zip/*/projekt-*), and pyproject.toml and uv.lock to
# the root folder. Workspace name in bausteine from folder and block without number (aufgaben-grundlagen), in the
# folder structure like the folder.
copy-templates:
	julia skripte/copy-templates.jl

# At the start of the semester: update package versions in the template lock file and distribute
update-packages:
	cd bausteine/00-templates && uv lock --upgrade
	julia skripte/copy-templates.jl

clean:
	rm -rf lernpfad/*/c
	rm -rf __output
	rm -rf _freeze
