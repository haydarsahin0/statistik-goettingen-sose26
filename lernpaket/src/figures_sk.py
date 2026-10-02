"""Abbildungen für den Statistik-Komplettkurs (fig/sk_*.svg), Farbwelt lila."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
from scipy import stats

OUT = os.path.join(os.path.dirname(__file__), "fig")
INK = "#1f2937"; MUT = "#5b6474"; PUR = "#6d28d9"; PURL = "#c4b5fd"; RED = "#d64545"; ORA = "#d9601c"; GRY = "#9aa5b8"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": "#8a94a6", "axes.labelcolor": INK,
    "xtick.color": MUT, "ytick.color": MUT, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 10.5, "svg.fonttype": "path",
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name + ".svg"), bbox_inches="tight")
    plt.close(fig)


# 1 Venn-Diagramm mit vier Bereichen
fig, ax = plt.subplots(figsize=(5.2, 2.9))
ax.add_patch(plt.Rectangle((0, 0), 10, 6, fill=False, ec=INK, lw=1.2))
ax.add_patch(Circle((3.9, 3), 2.2, fc=PURL, ec=PUR, alpha=.45, lw=1.5))
ax.add_patch(Circle((6.1, 3), 2.2, fc="#fbcfe8", ec="#be185d", alpha=.45, lw=1.5))
ax.text(.25, 5.45, "Ω", fontsize=13, color=INK)
ax.text(2.5, 4.9, "A", fontsize=12, color=PUR, weight="bold"); ax.text(7.3, 4.9, "B", fontsize=12, color="#be185d", weight="bold")
ax.text(2.9, 2.85, "A∩B̄\n= A\\B", ha="center", fontsize=8.5); ax.text(5, 2.95, "A∩B", ha="center", fontsize=8.5, weight="bold")
ax.text(7.1, 2.85, "Ā∩B\n= B\\A", ha="center", fontsize=8.5); ax.text(8.9, .5, "Ā∩B̄", ha="center", fontsize=8.5)
ax.set_xlim(-.2, 10.2); ax.set_ylim(-.2, 6.2); ax.axis("off")
ax.set_title("Die vier Bereiche: alles lässt sich daraus zusammensetzen")
save(fig, "sk_venn")

# 2 Baumdiagramm (Lieferdienst)
fig, ax = plt.subplots(figsize=(6.4, 3.3)); ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 6.6)
root = (0.6, 3.3)
lvl1 = [("A₁ Fahrer 1", 5.6, "0.5"), ("A₂ Fahrer 2", 3.3, "0.3"), ("A₃ Fahrer 3", 1.0, "0.2 (=1−0.5−0.3)")]
p_v = ["0.1", "0.2", "0.05"]; p_nv = ["0.9", "0.8", "0.95"]
end = [("0.05", "0.45"), ("0.06", "0.24"), ("0.01", "0.19")]
for (lab, y, p), pv, pnv, (e1, e2) in zip(lvl1, p_v, p_nv, end):
    ax.plot([root[0], 3.4], [root[1], y], color=PUR, lw=1.3)
    ax.text(1.6, (root[1] + y) / 2 + .15, p, color=PUR, fontsize=8.5, weight="bold")
    ax.text(3.45, y - .12, lab, fontsize=8.5)
    for dy, lab2, pp, ee in [(.55, "V (verspätet)", pv, e1), (-.55, "V̄", pnv, e2)]:
        ax.plot([5.2, 6.7], [y, y + dy], color=GRY, lw=1.1)
        ax.text(5.75, y + dy / 2 + (.12 if dy > 0 else -.32), pp, fontsize=8, color=MUT)
        ax.text(6.8, y + dy - .12, lab2, fontsize=8.3)
        ax.text(8.5, y + dy - .12, "= " + ee, fontsize=8.3, color=RED if lab2.startswith("V ") else INK, weight="bold" if lab2.startswith("V ") else None)
ax.plot(*root, "o", color=PUR)
ax.text(5.0, 6.35, "Pfad multiplizieren · passende Pfade addieren", ha="center", fontsize=9, color=INK, weight="bold")
ax.text(8.3, -.15, "P(V) = 0.05+0.06+0.01 = 0.12", fontsize=8.5, color=RED, ha="center")
save(fig, "sk_baum")

# 3 Verteilungsfunktion diskret (x: 0,1,2,4; p .1,.3,.4,.2)
vals = [0, 1, 2, 4]; F = [.1, .4, .8, 1]
fig, ax = plt.subplots(figsize=(5.2, 2.8))
ax.hlines(0, -1, 0, color=PUR, lw=2)
for i, (a, f) in enumerate(zip(vals, F)):
    b = vals[i + 1] if i + 1 < len(vals) else 5.2
    ax.hlines(f, a, b, color=PUR, lw=2); ax.plot(a, f, "o", color=PUR, ms=6)
    prev = F[i - 1] if i else 0
    ax.plot(a, prev, "o", mfc="white", mec=PUR, ms=6)
ax.set_xticks(range(-1, 6)); ax.set_yticks([0, .1, .4, .8, 1])
ax.set_xlabel("x"); ax.set_ylabel("F(x) = P(X ≤ x)"); ax.set_title("Verteilungsfunktion einer diskreten ZV: Treppe")
ax.grid(alpha=.25)
save(fig, "sk_Fdisk")

# 4 Dichte f(x)=2(x-2) auf [2,3], Fläche 2.2..2.8
x = np.linspace(2, 3, 200)
fig, ax = plt.subplots(figsize=(5.2, 2.8))
ax.plot([1.6, 2], [0, 0], color=PUR, lw=2); ax.plot(x, 2 * (x - 2), color=PUR, lw=2); ax.plot([3, 3.4], [0, 0], color=PUR, lw=2)
ax.plot([3, 3], [0, 2], color=PUR, lw=1, ls=":")
xs = np.linspace(2.2, 2.8, 100); ax.fill_between(xs, 2 * (xs - 2), color=ORA, alpha=.45)
ax.text(2.5, .35, "P(2.2 < X < 2.8)\n= F(2.8) − F(2.2) = 0.6", ha="center", fontsize=8.5)
ax.set_xlabel("x"); ax.set_ylabel("f(x)"); ax.set_title("Dichte f(x) = 2(x − 2) auf [2, 3]: Fläche = Wahrscheinlichkeit")
save(fig, "sk_dichte")

# 5 Normalverteilung N(500, 3²): P(496 ≤ X ≤ 502)
x = np.linspace(488, 512, 400); f = stats.norm.pdf(x, 500, 3)
fig, ax = plt.subplots(figsize=(5.8, 2.9))
ax.plot(x, f, color=PUR, lw=2)
xs = np.linspace(496, 502, 200); ax.fill_between(xs, stats.norm.pdf(xs, 500, 3), color=PURL, alpha=.8)
ax.axvline(500, color=GRY, ls=":", lw=1)
for v, z in [(496, "−1.333"), (502, "0.667"), (500, "0")]:
    ax.text(v, -0.012, "z = " + z, ha="center", fontsize=7.5, color=PUR)
ax.text(499, .055, "0.656", ha="center", fontsize=10, weight="bold")
ax.set_xlabel("x (Gramm)"); ax.set_ylabel("f(x)"); ax.set_ylim(-.018, .145)
ax.set_title("X ~ N(500, 9): standardisieren mit z = (x − 500)/3")
save(fig, "sk_norm")

# 6 Ablehnungsbereiche z
x = np.linspace(-4, 4, 400); f = stats.norm.pdf(x)
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.4))
for ax, (tit, regs, lab) in zip(axs, [
        ("linksseitig  H₁: μ < μ₀", [(-4, -1.645)], "−z₁₋α = −1.645"),
        ("rechtsseitig  H₁: μ > μ₀", [(1.645, 4)], "z₁₋α = 1.645"),
        ("zweiseitig  H₁: μ ≠ μ₀", [(-4, -1.96), (1.96, 4)], "±z₁₋α/₂ = ±1.96")]):
    ax.plot(x, f, color=PUR, lw=1.8)
    for a, b in regs:
        xs = np.linspace(a, b, 100); ax.fill_between(xs, stats.norm.pdf(xs), color=RED, alpha=.5)
    ax.set_title(tit, fontsize=9.5); ax.set_yticks([]); ax.set_xticks([-3, -1.96, 0, 1.96, 3]); ax.tick_params(labelsize=7)
    ax.text(0, .05, "H₀ nicht\nverwerfen", ha="center", fontsize=7.5, color=MUT)
    ax.set_xlabel(lab + "  (α = 0.05)", fontsize=8, color=RED)
save(fig, "sk_ab")

# 7 Chi²(11): Ablehnungsbereich α=0.1 (links) und p-Wert für 4.930
x = np.linspace(0, 26, 400); f = stats.chi2.pdf(x, 11)
krit = stats.chi2.ppf(.1, 11)
fig, ax = plt.subplots(figsize=(5.8, 2.9))
ax.plot(x, f, color=PUR, lw=2)
xs = np.linspace(0, krit, 100); ax.fill_between(xs, stats.chi2.pdf(xs, 11), color=PURL, alpha=.9, label="Ablehnungsbereich α = 0.1: [0; %.2f]" % krit)
xs = np.linspace(0, 4.930, 100); ax.fill_between(xs, stats.chi2.pdf(xs, 11), color=RED, alpha=.55, label="p-Wert = P(Z ≤ 4.930) = 0.065")
ax.axvline(4.930, color=RED, lw=1.2); ax.text(4.93, .095, "Z = 4.930", color=RED, fontsize=8, ha="center")
ax.legend(fontsize=7.5, frameon=False, loc="upper right"); ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.set_title("χ²(11) unter H₀: linksseitiger Varianztest")
save(fig, "sk_chi2")

# 8 100 Konfidenzintervalle
rng = np.random.default_rng(7)
mu, s2, n = 176, 51, 15
fig, ax = plt.subplots(figsize=(6.4, 2.7))
miss = 0
for i in range(100):
    xx = rng.normal(mu, np.sqrt(s2), n); m = xx.mean(); h = stats.t.ppf(.975, n - 1) * xx.std(ddof=1) / np.sqrt(n)
    ok = m - h <= mu <= m + h; miss += not ok
    ax.plot([i, i], [m - h, m + h], color=PUR if ok else RED, lw=1.1)
ax.axhline(mu, color=INK, lw=1); ax.text(101, mu, "μ = 176", va="center", fontsize=8)
ax.set_xlabel("Stichprobe Nr."); ax.set_ylabel("95 %-KI"); ax.set_title("100 Stichproben: ca. 95 Intervalle überdecken μ, ca. 5 nicht (rot: %d)" % miss)
save(fig, "sk_ki")

# 9 Kerndichteschätzer: kleine vs. große Bandweite
data = np.array([2, 3, 3.5, 6, 7])
xg = np.linspace(-1, 10, 500)
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.3))
for ax, b in zip(axs, [0.3, 1.0, 3.0]):
    u = (xg[:, None] - data[None, :]) / b
    k = np.where(np.abs(u) < 1, .75 * (1 - u ** 2), 0)
    ax.plot(xg, k.sum(1) / (len(data) * b), color=PUR, lw=1.8)
    ax.plot(data, np.zeros_like(data), "|", color=INK, ms=10)
    ax.set_title("Bandweite b = %.1f" % b, fontsize=9.5); ax.set_yticks([]); ax.tick_params(labelsize=7)
axs[0].set_xlabel("zu klein: zackig", fontsize=8); axs[2].set_xlabel("zu groß: alles glattgebügelt", fontsize=8)
save(fig, "sk_kde")

# 10 Regression mit Residuen
x = np.array([1, 2, 3, 4, 5]); y = np.array([3, 5, 4, 7, 9])
fig, ax = plt.subplots(figsize=(5.2, 2.9))
ax.plot(x, y, "o", color=PUR, ms=7, zorder=3)
xx = np.linspace(0.5, 5.5, 10); ax.plot(xx, 1.4 + 1.4 * xx, color=ORA, lw=2, label="ŷ = 1.4 + 1.4·x")
for xi, yi in zip(x, y):
    ax.plot([xi, xi], [yi, 1.4 + 1.4 * xi], color=RED, lw=1, ls="--")
ax.text(3.08, 4.6, "Residuum\nê₃ = 4 − 5.6 = −1.6", fontsize=7.5, color=RED)
ax.legend(frameon=False, fontsize=8.5); ax.set_xlabel("Werbung x (Tsd. €)"); ax.set_ylabel("Umsatz y (Tsd. €)")
ax.set_title("KQ-Gerade: Summe der quadrierten Residuen minimal")
save(fig, "sk_reg")

# 11 Exponentialverteilung P(X > 10), λ = 1/3
x = np.linspace(0, 16, 300)
fig, ax = plt.subplots(figsize=(5.2, 2.6))
ax.plot(x, stats.expon.pdf(x, scale=3), color=PUR, lw=2)
xs = np.linspace(10, 16, 100); ax.fill_between(xs, stats.expon.pdf(xs, scale=3), color=RED, alpha=.6)
ax.annotate("P(X > 10) = e^(−10/3) = 0.036", xy=(11, .008), xytext=(7.2, .12), arrowprops=dict(arrowstyle="->", color=RED), fontsize=8.5, color=RED)
ax.set_xlabel("Jagdzeit x (Stunden)"); ax.set_ylabel("f(x)"); ax.set_title("X ~ Exp(1/3): Dichte λ·e^(−λx)")
save(fig, "sk_exp")

# 12 Binomialverteilung B(8, 1/3)
k = np.arange(0, 9); p = stats.binom.pmf(k, 8, 1 / 3)
fig, ax = plt.subplots(figsize=(5.2, 2.6))
ax.bar(k, p, color=[ORA if kk <= 2 else PURL for kk in k], edgecolor=PUR, width=.6)
for kk, pp in zip(k, p):
    ax.text(kk, pp + .005, "%.3f" % pp, ha="center", fontsize=7)
ax.set_xticks(k); ax.set_xlabel("y"); ax.set_ylabel("P(Y = y)"); ax.set_title("Y ~ B(8, 1/3): orange = P(Y ≤ 2) = 0.468")
save(fig, "sk_bin")
print("ok")
