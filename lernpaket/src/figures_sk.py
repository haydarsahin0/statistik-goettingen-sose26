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
    "font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": "#8a94a6", "axes.labelcolor": INK,
    "xtick.color": MUT, "ytick.color": MUT, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 11.5, "axes.labelsize": 11, "lines.linewidth": 2.2, "svg.fonttype": "path",
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


# ================= neue Lern-Abbildungen =================
from matplotlib.patches import FancyArrowPatch, Rectangle

def box(ax, x, y, w, h, txt, fc, ec, fs=9.5, bold=False):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=fc, ec=ec, lw=1.6))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, weight="bold" if bold else None, color=INK, wrap=True)

def arrow(ax, a, b, lab=None, side=0.0):
    ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=MUT, lw=1.4, shrinkA=2, shrinkB=2))
    if lab:
        ax.text((a[0] + b[0]) / 2 + side, (a[1] + b[1]) / 2, lab, fontsize=8.8, color=PUR, weight="bold", ha="center", va="center",
                bbox=dict(fc="white", ec="none", pad=0.6))

# A Entscheidungsbaum Verteilung
fig, ax = plt.subplots(figsize=(10, 4.6)); ax.axis("off"); ax.set_xlim(-0.2, 10.3); ax.set_ylim(0.3, 6)
box(ax, 5, 5.5, 3.6, .65, "Was ist X?", "#ede9fe", PUR, 11, True)
box(ax, 2.4, 4.2, 3.0, .7, "eine ANZAHL (zählen)\n0, 1, 2, …", "#f5f3ff", PUR)
box(ax, 7.6, 4.2, 3.0, .7, "ein MESSWERT (stetig)\nZeit, Gewicht, Länge", "#f5f3ff", PUR)
arrow(ax, (4.2, 5.2), (2.9, 4.6)); arrow(ax, (5.8, 5.2), (7.1, 4.6))
box(ax, 1.25, 2.7, 2.3, .8, "feste Zahl n\nVersuche, je ja/nein", "white", GRY, 9)
box(ax, 3.75, 2.7, 2.3, .8, "keine Obergrenze,\n„pro Zeitraum“", "white", GRY, 9)
box(ax, 6.3, 2.7, 2.1, .8, "Warte-/Lebens-\ndauer", "white", GRY, 9)
box(ax, 8.15, 2.7, 1.45, .8, "Messwert um\nein Mittel", "white", GRY, 9)
box(ax, 9.65, 2.7, 1.1, .8, "gleich\nwahrsch.\nin [a,b]", "white", GRY, 8)
for a, b in [((2.0, 3.85), (1.25, 3.1)), ((2.8, 3.85), (3.75, 3.1)), ((7.0, 3.85), (6.3, 3.1)), ((7.6, 3.85), (8.2, 3.1)), ((8.3, 3.85), (9.65, 3.1))]:
    arrow(ax, a, b)
res = [(0.55, "n = 1:\nBernoulli\nBe(π)"), (1.85, "Binomial\nB(n, π)"), (3.75, "Poisson\nPo(λ)\nλ = Mittel"), (6.3, "Exponential\nExp(λ)\nλ = 1/Mittel"),
       (8.15, "Normal\nN(μ, σ²)"), (9.65, "Gleich\nU(a, b)")]
for x, t in res:
    box(ax, x, 1.15, 1.1 if x in (0.55, 1.85) else 1.45 if x != 9.65 else 1.1, 1.15, t, "#ddd6fe", PUR, 9, True)
for x0, x1 in [(1.0, .55), (1.5, 1.85), (3.75, 3.75), (6.3, 6.3), (8.15, 8.15), (9.65, 9.65)]:
    arrow(ax, (x0, 2.3), (x1, 1.75))
ax.set_title("Welche Verteilung? – Frage für Frage", fontsize=12.5)
save(fig, "sk_baum_vert")

# B Entscheidungsbaum Test
fig, ax = plt.subplots(figsize=(10, 4.5)); ax.axis("off"); ax.set_xlim(-0.3, 10.3); ax.set_ylim(0.25, 6)
box(ax, 5, 5.5, 4.4, .65, "Worüber soll etwas gezeigt werden?", "#ede9fe", PUR, 11, True)
top = [(1.0, "Mittelwert μ"), (2.9, "Anteil π"), (4.7, "Varianz σ²"), (6.4, "Median"), (8.6, "zwei kategoriale\nMerkmale / Verteilung")]
for x, t in top:
    box(ax, x, 4.1, 1.6 if x != 8.6 else 2.2, .75, t, "#f5f3ff", PUR, 9.5, True); arrow(ax, (5, 5.15), (x, 4.5))
box(ax, .4, 2.6, 1.0, .8, "σ bekannt", "white", GRY, 9); box(ax, 1.55, 2.6, 1.0, .8, "σ un-\nbekannt", "white", GRY, 9)
arrow(ax, (.8, 3.7), (.4, 3.0)); arrow(ax, (1.2, 3.7), (1.55, 3.0))
box(ax, 7.75, 2.6, 1.35, .8, "Kreuztabelle", "white", GRY, 9); box(ax, 9.45, 2.6, 1.4, .8, "vorgegebene\nVerteilung", "white", GRY, 8.5)
arrow(ax, (8.3, 3.7), (7.75, 3.0)); arrow(ax, (8.9, 3.7), (9.45, 3.0))
res = [(.4, "Gauß-Test\nZ ~ N(0,1)"), (1.55, "t-Test\nT ~ t(n−1)"), (2.9, "Binomialtest\n(approx.)\nZ ~ N(0,1)"), (4.7, "χ²-Varianz-\ntest\nχ²(n−1)"),
       (6.4, "Vorzeichen-\ntest\nB(n; 0.5)"), (7.75, "χ²-Unab-\nhängigkeit\nχ²((J−1)(K−1))"), (9.45, "χ²-Anpas-\nsung\nχ²(J−1)")]
for x, t in res:
    box(ax, x, 1.05, 1.0 if x < 2 else 1.3, 1.25, t, "#ddd6fe", PUR, 8.6, True)
for x in [.4, 1.55, 7.75, 9.45]:
    arrow(ax, (x, 2.2), (x, 1.7))
for x in [2.9, 4.7, 6.4]:
    arrow(ax, (x, 3.7), (x, 1.7))
ax.set_title("Welcher Test? – dann immer das 5-Schritte-Schema", fontsize=12.5)
save(fig, "sk_baum_test")

# C Zielscheiben: Bias / Varianz
rng = np.random.default_rng(3)
fig, axs = plt.subplots(1, 4, figsize=(10, 2.9))
cfg = [("kein Bias, kleine Varianz\n(ideal)", 0, .25), ("kein Bias, große Varianz", 0, .8), ("Bias, kleine Varianz", .9, .25), ("Bias, große Varianz", .8, .55)]
for ax, (t, b, s_) in zip(axs, cfg):
    for r, c in [(2, "#f5f3ff"), (1.4, "#ede9fe"), (.8, "#ddd6fe"), (.3, PURL)]:
        ax.add_patch(Circle((0, 0), r, fc=c, ec=PUR, lw=.8))
    pts = rng.normal(0, s_, (14, 2)) + [b, b * .6]
    ax.plot(pts[:, 0], pts[:, 1], "o", color=RED, ms=5, mec="white", mew=.6)
    ax.plot(0, 0, "+", color=INK, ms=12, mew=2)
    ax.set_xlim(-2.1, 2.1); ax.set_ylim(-2.1, 2.1); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(t, fontsize=9.5)
fig.suptitle("Mitte = wahrer Parameter ϑ · Punkt = Schätzung aus einer Stichprobe", fontsize=10.5, color=MUT, y=.04)
save(fig, "sk_ziel")

# D Likelihood-Kurve Münze 6 von 20
pi = np.linspace(.01, .99, 400); L = stats.binom.pmf(6, 20, pi); ll = np.log(L)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.0))
axs[0].plot(pi, L, color=PUR); axs[0].axvline(.3, color=RED, ls="--", lw=1.3); axs[0].text(.32, L.max() * .95, "Maximum bei π̂ = 0.3", color=RED, fontsize=9.5)
axs[0].set_xlabel("π"); axs[0].set_ylabel("L(π)"); axs[0].set_title("Likelihood L(π): 6 Wappen in 20 Würfen")
axs[1].plot(pi, ll, color=ORA); axs[1].axvline(.3, color=RED, ls="--", lw=1.3); axs[1].set_ylim(-25, 0)
axs[1].set_xlabel("π"); axs[1].set_ylabel("log L(π)"); axs[1].set_title("log L(π): gleiches Maximum")
save(fig, "sk_lik")

# E Normalverteilung 68-95-99.7 + Symmetrie
x = np.linspace(-4, 4, 500)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.0))
ax = axs[0]; ax.plot(x, stats.norm.pdf(x), color=PUR)
for k, c, lab in [(3, "#f5f3ff", "99.7 %"), (2, "#ddd6fe", "95 %"), (1, PURL, "68 %")]:
    xs = np.linspace(-k, k, 200); ax.fill_between(xs, stats.norm.pdf(xs), color=c)
for k, y, lab in [(1, .22, "68 %"), (2, .1, "95 %"), (3, .025, "99.7 %")]:
    ax.annotate("", xy=(k, y), xytext=(-k, y), arrowprops=dict(arrowstyle="<->", color=INK, lw=1)); ax.text(0, y + .012, lab, ha="center", fontsize=9)
ax.set_xticks([-3, -2, -1, 0, 1, 2, 3]); ax.set_xticklabels(["μ−3σ", "μ−2σ", "μ−σ", "μ", "μ+σ", "μ+2σ", "μ+3σ"], fontsize=8.5); ax.set_yticks([])
ax.set_title("Faustregel der Normalverteilung")
ax = axs[1]; ax.plot(x, stats.norm.pdf(x), color=PUR)
xs = np.linspace(-4, -1.2, 100); ax.fill_between(xs, stats.norm.pdf(xs), color=RED, alpha=.55)
xs = np.linspace(1.2, 4, 100); ax.fill_between(xs, stats.norm.pdf(xs), color=ORA, alpha=.55)
ax.text(-2.6, .09, "Φ(−z)", color=RED, fontsize=11, weight="bold"); ax.text(1.7, .09, "1 − Φ(z)", color=ORA, fontsize=11, weight="bold")
ax.set_xticks([-1.2, 0, 1.2]); ax.set_xticklabels(["−z", "0", "z"]); ax.set_yticks([])
ax.set_title("Symmetrie: Φ(−z) = 1 − Φ(z)")
save(fig, "sk_norm2")

# F diskret vs. stetig
fig, axs = plt.subplots(1, 2, figsize=(10, 2.9))
k = np.array([0, 1, 2]); pk = [.2, .5, .3]
axs[0].vlines(k, 0, pk, color=PUR, lw=5); axs[0].plot(k, pk, "o", color=PUR, ms=8)
for kk, pp in zip(k, pk):
    axs[0].text(kk, pp + .03, str(pp), ha="center", fontsize=10)
axs[0].set_xticks(k); axs[0].set_ylim(0, .65); axs[0].set_xlabel("x"); axs[0].set_ylabel("P(X = x)")
axs[0].set_title("DISKRET: Wahrscheinlichkeit = Höhe des Stabs")
x = np.linspace(0, 6, 300); f = stats.gamma.pdf(x, 3, scale=.8)
axs[1].plot(x, f, color=PUR); xs = np.linspace(1.5, 3, 100); axs[1].fill_between(xs, stats.gamma.pdf(xs, 3, scale=.8), color=PURL)
axs[1].text(2.25, .08, "Fläche =\nP(1.5 ≤ X ≤ 3)", ha="center", fontsize=9.5)
axs[1].set_xlabel("x"); axs[1].set_ylabel("f(x)"); axs[1].set_title("STETIG: Wahrscheinlichkeit = Fläche")
save(fig, "sk_diskstet")

# G ZGWS
rng = np.random.default_rng(1)
fig, axs = plt.subplots(1, 3, figsize=(10, 2.7))
for ax, n in zip(axs, [1, 5, 30]):
    m = rng.exponential(1, (20000, n)).mean(1)
    ax.hist(m, bins=60, density=True, color=PURL, edgecolor="white")
    if n > 1:
        xx = np.linspace(m.min(), m.max(), 200); ax.plot(xx, stats.norm.pdf(xx, 1, 1 / np.sqrt(n)), color=RED, lw=1.8)
    ax.set_title("Mittelwert aus n = %d" % n, fontsize=10.5); ax.set_yticks([])
axs[0].set_xlabel("schiefe Einzelwerte"); axs[2].set_xlabel("fast normal, schmal (σ/√n)")
save(fig, "sk_zgws")

# H p-Wert anschaulich
x = np.linspace(-4, 4, 400)
fig, ax = plt.subplots(figsize=(7.5, 2.9))
ax.plot(x, stats.norm.pdf(x), color=PUR)
xs = np.linspace(1.645, 4, 100); ax.fill_between(xs, stats.norm.pdf(xs), color=PURL, label="Ablehnungsbereich: Fläche α = 0.05")
xs = np.linspace(2.0, 4, 100); ax.fill_between(xs, stats.norm.pdf(xs), color=RED, alpha=.6, label="p-Wert: Fläche rechts von z = 2 → 0.023")
ax.axvline(1.645, color=PUR, ls=":"); ax.axvline(2.0, color=RED)
ax.text(1.645, .3, "kritischer Wert\n1.645", ha="center", fontsize=8.5, color=PUR); ax.text(2.35, .17, "beobachtet\nz = 2", fontsize=8.5, color=RED)
ax.legend(frameon=False, fontsize=8.5, loc="upper left"); ax.set_yticks([]); ax.set_xlabel("Teststatistik unter H₀ ~ N(0, 1)")
ax.set_title("p ≤ α ⇔ Teststatistik im Ablehnungsbereich → H₀ verwerfen")
save(fig, "sk_pwert")

# I Bedingte Wahrscheinlichkeit: Welt verkleinern
fig, ax = plt.subplots(figsize=(7.5, 2.2)); ax.axis("off"); ax.set_xlim(0, 7.6); ax.set_ylim(0, 2.2)
for i in range(6):
    inB = i < 3; ev = (i + 1) % 2 == 0
    ax.add_patch(FancyBboxPatch((.3 + i * 1.2, .55), .9, .9, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=(PURL if inB else "#f3f4f6"), ec=(PUR if inB else GRY), lw=2 if inB else 1))
    ax.text(.75 + i * 1.2, 1.0, str(i + 1), ha="center", va="center", fontsize=16, weight="bold" if ev and inB else None,
            color=(RED if ev and inB else (INK if inB else GRY)))
ax.add_patch(Rectangle((.15, .4), 3.7, 1.2, fill=False, ec=PUR, lw=2.2, ls="--"))
ax.text(2.0, 1.82, "neue Welt B = {1, 2, 3}", ha="center", color=PUR, weight="bold", fontsize=10)
ax.text(5.9, 1.82, "fällt weg", ha="center", color=GRY, fontsize=10)
ax.text(3.8, .12, "P(gerade | B) = 1 von 3 = 1/3", ha="center", color=RED, fontsize=10.5, weight="bold")
save(fig, "sk_bedingt")

# J KI-Bauform
fig, ax = plt.subplots(figsize=(7.5, 1.7)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 2)
ax.plot([1, 9], [1, 1], color=GRY, lw=1)
ax.plot([2.5, 7.5], [1, 1], color=PUR, lw=6, solid_capstyle="butt")
ax.plot(5, 1, "o", color=RED, ms=10)
for xv, t in [(2.5, "L = x̄ − Quantil · SE"), (5, "x̄ (Schätzer)"), (7.5, "U = x̄ + Quantil · SE")]:
    ax.text(xv, 1.35 if xv == 5 else .45, t, ha="center", fontsize=10, color=RED if xv == 5 else PUR, weight="bold")
ax.annotate("", xy=(7.5, 1.6), xytext=(5, 1.6), arrowprops=dict(arrowstyle="<->", color=INK)); ax.text(6.25, 1.75, "halbe Breite = Quantil × Standardfehler", ha="center", fontsize=8.8)
save(fig, "sk_kibau")
print("ok")
