import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


# -----------------------------------------------------------------------------
# Stabendkräfte und Elementsteifigkeitsmatrix eines Fachwerkstabs
# -----------------------------------------------------------------------------
#
def truss_p(EA, x1, x2, u1, u2):
    """Vektor der Stabendkräfte nach der geometrisch exakten Formulierung"""
    l0 = np.linalg.norm(x2 - x1)
    l = np.linalg.norm(x2 + u2 - (x1 + u1))
    d = (x2 + u2 - (x1 + u1)) / l
    t = np.concatenate((-d, d))
    return EA * (l - l0) / l0 * t


def truss_ke(EA, x1, x2):
    """Elementsteifigkeitsmatrix"""
    l0 = np.linalg.norm(x2 - x1)
    d0 = (x2 - x1) / l0
    t0 = np.concatenate((-d0, d0))
    return EA / l0 * np.outer(t0, t0)


def truss_n(EA, x1, x2, u1, u2):
    """Normalkraft nach der Formulierung für kleine Verformungen"""
    l0 = np.linalg.norm(x2 - x1)
    d0 = (x2 - x1) / l0
    return EA / l0 * np.dot(u2 - u1, d0)


def truss_p_lin(EA, x1, x2, u1, u2):
    """Vektor der Stabendkräfte nach der Formulierung für kleine Verformungen"""
    K = truss_ke(EA, x1, x2)
    u = np.concatenate((u1, u2))
    return K @ u


# -----------------------------------------------------------------------------
# Darstellung von Stabtragwerken
# -----------------------------------------------------------------------------
#
def draw_system(s):
    """System zeichnen"""
    plt.quiver(
        s.nodes[0, :], s.nodes[1, :], s.forces[0, :], s.forces[1, :], color="red"
    )

    for i in range(0, s.elements.shape[1]):
        n = s.elements[:, i]
        plt.plot(s.nodes[0, n], s.nodes[1, n], color="black")

    plt.scatter(
        s.nodes[0, s.supports[0, :]],
        s.nodes[1, s.supports[0, :]],
        marker=5,
        s=200,
        c="hotpink",
    )
    plt.scatter(
        s.nodes[0, s.supports[1, :]],
        s.nodes[1, s.supports[1, :]],
        marker=6,
        s=200,
        c="hotpink",
    )
    plt.scatter(s.nodes[0, :], s.nodes[1, :], color="black")

    plt.axis("equal")
    plt.show()


# -----------------------------------------------------------------------------
# Berechnung
# -----------------------------------------------------------------------------
#
def solve(s):
    """Verschiebungen, je Spalte der Verschiebungsvektor eines Knotens"""
    Ne = s.elements.shape[1]
    Nn = s.nodes.shape[1]
    N = 2 * Nn

    # Systemsteifigkeitsmatrix
    K_hat = np.zeros((N, N))
    for e in range(Ne):
        n1 = s.elements[0, e]
        n2 = s.elements[1, e]
        x1 = s.nodes[:, n1]
        x2 = s.nodes[:, n2]
        Ke = truss_ke(s.EA, x1, x2)
        Ie = [2 * n1, 2 * n1 + 1, 2 * n2, 2 * n2 + 1]
        K_hat[np.ix_(Ie, Ie)] += Ke

    # System-Lastvektor
    F_hat = np.reshape(s.forces, -1, order="F")

    # Randbedingungen
    S_hat = np.reshape(s.supports, -1, order="F")
    for i in range(N):
        if S_hat[i]:
            K_hat[i, :] = 0
            K_hat[i, i] = 1
            F_hat[i] = 0

    # LGS lösen
    u_hat = np.linalg.solve(K_hat, F_hat)

    # Als umsortierte Matrix zurückgeben
    return np.reshape(u_hat, (2, -1), order="F")


"""Normalkräfte aller Stäbe aus den Verschiebungen s.u_hat"""


def member_forces(s):
    Ne = s.elements.shape[1]
    N = np.zeros(Ne)

    for e in range(0, Ne):
        n1 = s.elements[0, e]
        n2 = s.elements[1, e]
        x1 = s.nodes[:, n1]
        x2 = s.nodes[:, n2]
        u1 = s.u_hat[:, n1]
        u2 = s.u_hat[:, n2]
        N[e] = truss_n(s.EA, x1, x2, u1, u2)

    return N


# -----------------------------------------------------------------------------
# Darstellung der Ergebnisse
# -----------------------------------------------------------------------------
#
def struct_size(s):
    """Maß für die Abmessungen des Tragwerks"""
    width = np.max(s.nodes[0, :]) - np.min(s.nodes[0, :])
    height = np.max(s.nodes[1, :]) - np.min(s.nodes[1, :])
    if width * height == 0:
        return max(width, height)
    return np.sqrt(width * height)


def draw_deformation(s):
    """Verformtes System (schwarz) über dem unverformten (grau)"""
    scale = 0.15 * struct_size(s) / np.max(np.abs(s.u_hat))
    nu = s.nodes + scale * s.u_hat

    for e in range(s.elements.shape[1]):
        n = s.elements[:, e]
        plt.plot(s.nodes[0, n], s.nodes[1, n], color="gray", zorder=-5)
        plt.plot(nu[0, n], nu[1, n], color="black")
    plt.scatter(nu[0, :], nu[1, :], color="black", zorder=2, s=15)

    plt.axis("equal")
    plt.show()


def draw_member_forces(s):
    """Normalkräfte als Flächen senkrecht zum Stab, Zug rot, Druck blau"""
    patches = []
    scale = 0.15 * struct_size(s) / np.max(np.abs(s.N))
    for e in range(s.elements.shape[1]):
        n1, n2 = s.elements[:, e]
        x1 = s.nodes[:, n1]
        x2 = s.nodes[:, n2]

        # d0 um 90° gedreht, mit der Normalkraft skaliert
        d0 = (x2 - x1) / np.linalg.norm(x2 - x1)
        o = scale * s.N[e] * np.array([d0[1], -d0[0]])
        patches.append(Polygon(np.vstack((x1, x2, x2 + o, x1 + o))))

        plt.plot([x1[0], x2[0]], [x1[1], x2[1]], color="black")

    n_max = np.max(np.abs(s.N))
    pc = PatchCollection(patches, edgecolor="black", alpha=0.6, cmap="bwr")
    pc.set_array(s.N)
    pc.set_clim(-n_max, n_max)
    plt.gca().add_collection(pc)
    plt.colorbar(pc, label="N")

    plt.axis("equal")
    plt.show()


def print_results(s):
    """Verschiebungen und Normalkräfte als Tabellen (Knoten und Stäbe ab 1 gezählt)"""
    print("Verschiebungen")
    print(f"{'Knoten':>8}{'u1':>14}{'u2':>14}")
    for n in range(s.nodes.shape[1]):
        print(f"{n + 1:>8}{s.u_hat[0, n]:>14.6f}{s.u_hat[1, n]:>14.6f}")
    print()
    print("Normalkräfte")
    print(f"{'Stab':>8}{'N':>14}")
    for e in range(s.elements.shape[1]):
        print(f"{e + 1:>8}{s.N[e]:>14.3f}")
