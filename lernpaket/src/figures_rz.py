"""Abbildungen für das Rezeptbuch Tag 1 (fig/rz_*.svg)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "fig")
INK = "#1f2937"; MUT = "#5b6474"; TEAL = "#0f766e"; RED = "#d64545"; BLU = "#1d63c4"; GRY = "#9aa5b8"; ORA = "#d9601c"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": "#8a94a6", "axes.labelcolor": INK,
    "xtick.color": MUT, "ytick.color": MUT, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 10.5, "svg.fonttype": "path",
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name + ".svg"), bbox_inches="tight")
    plt.close(fig)


# 1 Streudiagramm zeichnen
x = [2, 4, 3, 6, 5, 1]; y = [30, 45, 38, 60, 48, 25]
fig, ax = plt.subplots(figsize=(5.2, 3.2))
ax.scatter(x, y, s=40, color=TEAL, zorder=3)
for xi, yi, i in zip(x, y, range(1, 7)):
    ax.annotate(f"Filiale {i}", (xi, yi), textcoords="offset points", xytext=(6, -3), fontsize=7.5, color=MUT)
ax.set_xlabel("Werbeausgaben X (Tsd. €)")
ax.set_ylabel("Umsatz Y (Tsd. €)")
ax.set_title("Streudiagramm: Werbung und Umsatz")
ax.set_xlim(0, 7); ax.set_ylim(20, 65)
ax.grid(alpha=.25)
save(fig, "rz_streu")

# 2 Streudiagramme zuordnen
rng = np.random.default_rng(3)
fig, axs = plt.subplots(1, 5, figsize=(10, 2.2))
n = 40
u = rng.normal(size=n)
cases = []
v = 0.95 * u + np.sqrt(1 - .95 ** 2) * rng.normal(size=n); cases.append(("A", u, v))
v = -0.9 * u + np.sqrt(1 - .81) * rng.normal(size=n); cases.append(("B", u, v))
v = 0.5 * u + np.sqrt(.75) * rng.normal(size=n); cases.append(("C", u, v))
cases.append(("D", u, rng.normal(size=n)))
uu = np.linspace(-2, 2, n); cases.append(("E", uu, uu ** 2 + .15 * rng.normal(size=n)))
for ax, (lab, a, b) in zip(axs, cases):
    ax.scatter(a, b, s=9, color=TEAL)
    ax.set_title(lab); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("x"); ax.set_ylabel("y")
save(fig, "rz_r5")

# 3 ECDF zeichnen (Kaffee)
vals = [0, 1, 2, 3, 4, 6]; F = [.1, .3, .6, .8, .9, 1]
fig, ax = plt.subplots(figsize=(5.4, 3.2))
ax.hlines(0, -1, 0, color=TEAL, lw=2)
ax.plot(0, 0, "o", mfc="white", mec=TEAL, ms=6)
for i, (a, f) in enumerate(zip(vals, F)):
    b = vals[i + 1] if i + 1 < len(vals) else 7.2
    ax.hlines(f, a, b, color=TEAL, lw=2)
    ax.plot(a, f, "o", color=TEAL, ms=6)
    if i + 1 < len(vals):
        ax.plot(b, f, "o", mfc="white", mec=TEAL, ms=6)
    ax.hlines(f, -1, a, color=GRY, lw=.7, ls=":")
ax.annotate("", xy=(7.4, 1), xytext=(6.8, 1), arrowprops=dict(arrowstyle="->", color=TEAL))
ax.annotate("", xy=(-1.3, 0), xytext=(-.7, 0), arrowprops=dict(arrowstyle="->", color=TEAL))
ax.set_yticks([0] + F); ax.set_xticks(range(0, 8))
ax.set_xlim(-1.4, 7.6); ax.set_ylim(-.05, 1.08)
ax.set_xlabel("Tassen Kaffee x"); ax.set_ylabel(r"$\hat F(x)$")
ax.set_title("Empirische Verteilungsfunktion")
ax.axhline(.5, color=RED, lw=.8, ls="--")
ax.text(4.4, .44, "Median: bei 0.5 waagerecht → trifft Stufe x = 2", color=RED, fontsize=7.5)
save(fig, "rz_ecdf")

# 4 Histogramm (Pendelzeiten) mit Fläche 25–45
br = [0, 10, 20, 30, 60, 90]; hts = [.016, .03, .024, .2 / 30, .1 / 30]
fig, ax = plt.subplots(figsize=(5.8, 3.2))
for a, b, hh in zip(br[:-1], br[1:], hts):
    ax.bar(a, hh, width=b - a, align="edge", color=TEAL, alpha=.35, edgecolor=TEAL)
    ax.text((a + b) / 2, hh + .0008, f"{hh:.4f}".rstrip("0"), ha="center", fontsize=7.5, color=INK)
ax.bar(25, .024, width=5, align="edge", color=ORA, alpha=.8)
ax.bar(30, .2 / 30, width=15, align="edge", color=ORA, alpha=.8)
ax.text(46, .016, "Anteil 25–45:\n5·0.024 + 15·0.0067\n= 0.12 + 0.10 = 0.22", color=ORA, fontsize=7.5)
ax.set_xticks(br); ax.set_xlabel("Pendelzeit in Minuten"); ax.set_ylabel("Dichte")
ax.set_title("Normiertes Histogramm (Fläche = Anteil)")
save(fig, "rz_hist")

# 5 Boxplot zeichnen (Lieferzeiten)
fig, ax = plt.subplots(figsize=(6.2, 2.1))
q1, med, q3, lw, uw, out = 3.5, 4.5, 6.5, 2, 9, 14
ax.add_patch(plt.Rectangle((q1, .8), q3 - q1, .4, fc="#e3f3f1", ec=TEAL, lw=1.6))
ax.plot([med, med], [.8, 1.2], color=TEAL, lw=2.4)
ax.plot([lw, q1], [1, 1], color=TEAL, lw=1.4); ax.plot([q3, uw], [1, 1], color=TEAL, lw=1.4)
ax.plot([lw, lw], [.9, 1.1], color=TEAL, lw=1.4); ax.plot([uw, uw], [.9, 1.1], color=TEAL, lw=1.4)
ax.plot(out, 1, "o", mfc="white", mec=RED, ms=7)
for xv, t in [(lw, "unterer\nWhisker 2"), (q1, "x0.25\n3.5"), (med, "Median\n4.5"), (q3, "x0.75\n6.5"), (uw, "oberer\nWhisker 9"), (out, "Ausreißer\n14")]:
    ax.text(xv, 1.28, t, ha="center", fontsize=7.5, color=RED if xv == out else INK)
ax.axvline(11, color=RED, lw=.8, ls=":"); ax.text(11.1, .72, "obere Grenze 11", color=RED, fontsize=7)
ax.set_ylim(.6, 1.6); ax.set_yticks([]); ax.set_xlim(0, 16); ax.set_xticks(range(0, 17, 2))
ax.set_xlabel("Lieferzeit in Tagen"); ax.spines["left"].set_visible(False)
ax.set_title("Boxplot der Lieferzeiten")
save(fig, "rz_box")

# 6 Boxplots lesen / vergleichen
fig, ax = plt.subplots(figsize=(5.6, 2.6))
stats = [dict(med=8, q1=5, q3=20, whislo=2, whishi=40, fliers=[], label="Gruppe A"),
         dict(med=16, q1=14, q3=18, whislo=10, whishi=22, fliers=[35], label="Gruppe B")]
ax.bxp(stats, vert=False, showfliers=True, patch_artist=True,
       boxprops=dict(facecolor="#e3f3f1", edgecolor=TEAL), medianprops=dict(color=TEAL, lw=2),
       whiskerprops=dict(color=TEAL), capprops=dict(color=TEAL), flierprops=dict(mec=RED))
ax.set_xlabel("Kampfzeit in Minuten"); ax.set_xticks(range(0, 45, 5))
ax.set_title("Kampfzeiten nach Gruppe")
save(fig, "rz_box2")
print("ok")
