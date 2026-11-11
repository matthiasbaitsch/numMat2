import numpy as np


# Numerische Lösung von Anfangswertproblemen y' = F(x, y), y(x0) = y0 auf dem Intervall I = [x0, xe] mit der
# Schrittweite h. Rückgabe sind die Stellen x_0, ..., x_N und die Näherungen y_0, ..., y_N. Ist y0 ein Vektor
# (System von Differentialgleichungen), dann enthält jede Zeile von y die Näherung an einer Stelle.


def grid(I, h, y0):
    """Stellen x_0, ..., x_N und Feld für die Näherungen mit y_0 in der ersten Zeile"""
    N = round((I[1] - I[0]) / h)
    x = I[0] + h * np.arange(N + 1)
    y = np.zeros((N + 1,) + np.shape(y0))
    y[0] = y0
    return x, y


def euler(F, I, h, y0):
    """Explizites Euler-Verfahren"""
    x, y = grid(I, h, y0)
    for i in range(len(x) - 1):
        k = F(x[i], y[i])
        y[i + 1] = y[i] + h * k
    return x, y


def halbschritt(F, I, h, y0):
    """Halbschrittverfahren"""
    x, y = grid(I, h, y0)
    for i in range(len(x) - 1):
        k1 = F(x[i], y[i])
        k2 = F(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
        y[i + 1] = y[i] + h * k2
    return x, y


def rungekutta(F, I, h, y0):
    """Runge-Kutta-Verfahren vierter Ordnung"""
    x, y = grid(I, h, y0)
    for i in range(len(x) - 1):
        k1 = F(x[i], y[i])
        k2 = F(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
        k3 = F(x[i] + 0.5 * h, y[i] + 0.5 * h * k2)
        k4 = F(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, y


def plot_slope_field(F, xrange, yrange, delta, ax=None):
    """Richtungsfeld: an den Punkten eines Gitters mit Abstand delta kurze Strecken mit Steigung F(x, y)"""
    import matplotlib.pyplot as plt

    ax = ax or plt.gca()
    x, y = np.meshgrid(np.arange(xrange[0], xrange[1] + delta / 2, delta),
                       np.arange(yrange[0], yrange[1] + delta / 2, delta))
    slope = F(x, y)

    # Strecken der Länge 0.7 * delta in Richtung (1, F) / |(1, F)|
    length = np.sqrt(1 + slope**2)
    dx = 0.35 * delta / length
    dy = 0.35 * delta * slope / length
    ax.plot(np.array([x - dx, x + dx]).reshape(2, -1), np.array([y - dy, y + dy]).reshape(2, -1),
            color="tab:blue", linewidth=1)
    ax.set_aspect("equal")
    return ax
