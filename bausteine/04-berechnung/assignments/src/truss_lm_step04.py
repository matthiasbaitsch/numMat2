import numpy as np
import matplotlib.pyplot as plt


# Stabendkräfte und Elementsteifigkeitsmatrix eines Fachwerkstabs


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


# Darstellung von Stabtragwerken


def draw_system(s):
    """Knoten, Stäbe, Kräfte und Auflager zeichnen"""
    # Stäbe
    for e in range(s.elements.shape[1]):
        n = s.elements[:, e]
        plt.plot(s.nodes[0, n], s.nodes[1, n], color="black")

    # Knoten
    plt.scatter(s.nodes[0, :], s.nodes[1, :], color="black", zorder=2, s=15)

    # Kräfte
    plt.quiver(
        s.nodes[0, :], s.nodes[1, :],
        s.forces[0, :], s.forces[1, :],
        color="red", angles="xy", width=0.004,
    )

    # Auflager, Dreiecke in Richtung der gesperrten Verschiebung
    sx = s.supports[0, :]
    plt.scatter(s.nodes[0, sx], s.nodes[1, sx], marker=5, s=150, color="tab:blue")
    sy = s.supports[1, :]
    plt.scatter(s.nodes[0, sy], s.nodes[1, sy], marker=6, s=150, color="tab:blue")

    plt.axis("equal")
    plt.show()


# Berechnung


def solve(s):
    """Verschiebungen, je Spalte der Verschiebungsvektor eines Knotens"""
    Nn = s.nodes.shape[1]
    Ne = s.elements.shape[1]
    N = 2 * Nn

    # Globale Steifigkeitsmatrix
    K = np.zeros((N, N))
    for e in range(Ne):
        n1, n2 = s.elements[:, e]
        Ke = truss_ke(s.EA, s.nodes[:, n1], s.nodes[:, n2])
        I = [2 * n1, 2 * n1 + 1, 2 * n2, 2 * n2 + 1]
        K[np.ix_(I, I)] += Ke

    # Lastvektor, spaltenweise aus der Matrix der Kräfte
    F = np.reshape(s.forces, N, order="F").astype(float)

    # Auflager: Zeile gleich null, eins auf der Diagonalen
    fixed = np.reshape(s.supports, N, order="F")
    F[fixed] = 0
    K[fixed, :] = 0
    K[fixed, fixed] = 1

    u = np.linalg.solve(K, F)
    return np.reshape(u, (2, Nn), order="F")


def member_forces(s):
    """Normalkräfte aller Stäbe aus den Verschiebungen s.u_hat"""
    Ne = s.elements.shape[1]
    N = np.zeros(Ne)
    for e in range(Ne):
        n1, n2 = s.elements[:, e]
        N[e] = truss_n(s.EA, s.nodes[:, n1], s.nodes[:, n2], s.u_hat[:, n1], s.u_hat[:, n2])
    return N
