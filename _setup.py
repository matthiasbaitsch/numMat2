# Setup for executed {python} cells in assignments and slides, loaded in the first cell with
# import sys; from pathlib import Path; exec(open(Path(sys.prefix).parent / "_setup.py").read())
# (sys.prefix is the .venv in the root folder, works from bausteine and from lernpfad/*/c)
import numpy as np
import matplotlib.pyplot as plt

# Minimal look, without frame at the top and on the right
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.3
