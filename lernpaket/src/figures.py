"""Erzeugt alle Abbildungen des Lernbuchs als SVG (fig/*.svg)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import comb, factorial, exp, log

OUT = os.path.join(os.path.dirname(__file__), "fig")
os.makedirs(OUT, exist_ok=True)
INK = "#1f2937"; MUT = "#5b6474"
TEAL = "#0f766e"; VIO = "#6d3fc6"; ORA = "#d9601c"; BLU = "#1d63c4"; GRN = "#1f8a4c"; RED = "#d64545"; GRY = "#9aa5b8"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": "#8a94a6", "axes.labelcolor": INK,
    "xtick.color": MUT, "ytick.color": MUT, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 10.5, "svg.fonttype": "path",
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name + ".svg"), bbox_inches="tight")
    plt.close(fig)


def phi(x):
    return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)


# 1 Säulendiagramm vs. Histogramm (ungleiche Klassen)
x = np.array([22,12,8,20,35,20,18,60,15,20,18,13,20,74,15,24,18,18,16,22,13,19,80,27,14,15,15,30,9,67,
              24,20,10,15,77,12,10,9,27,18,9,9,13,25,8,28,11,29,54,28,8,22,7,73,44])
br = [0, 10, 20, 100]
h, _ = np.histogram(x, bins=br)
fig, ax = plt.subplots(1, 2, figsize=(8, 2.8))
w = np.diff(br)
ax[0].bar(br[:-1], h, width=w, align="edge", color=GRY, edgecolor="white")
ax[0].set_title("Säulendiagramm: Höhe = Anzahl"); ax[0].set_xlabel("Wohnraum in qm"); ax[0].set_ylabel("absolute Häufigkeit")
dens = h / len(x) / w
ax[1].bar(br[:-1], dens, width=w, align="edge", color=TEAL, alpha=.85, edgecolor="white")
ax[1].set_title("Histogramm: Fläche = Anteil"); ax[1].set_xlabel("Wohnraum in qm"); ax[1].set_ylabel("Dichte")
for a, b, d, f in zip(br[:-1], br[1:], dens, h / len(x)):
    ax[1].text((a + b) / 2, d + .0015, f"Fläche\n{f:.2f}", ha="center", fontsize=8, color=INK)
ax[1].set_ylim(0, dens.max() * 1.45)
save(fig, "saeule_hist")

# 2 Empirische Verteilungsfunktion (Bier)
vals = [4, 8.5, 12, 15.7]; F = [0.3, 0.7, 0.9, 1.0]
fig, ax = plt.subplots(figsize=(6.2, 2.9))
ax.hlines(0, 0, 4, color=TEAL, lw=2.2)
for i, v in enumerate(vals):
    end = vals[i + 1] if i + 1 < len(vals) else 19
    ax.hlines(F[i], v, end, color=TEAL, lw=2.2)
    ax.plot(v, F[i], "o", color=TEAL, ms=6)
    prev = F[i - 1] if i > 0 else 0
    ax.plot(v, prev, "o", mfc="white", mec=TEAL, ms=6)
ax.annotate("", xy=(19.3, 1), xytext=(18.2, 1), arrowprops=dict(arrowstyle="->", color=TEAL))
ax.set_xlim(0, 19.5); ax.set_ylim(-.05, 1.1)
ax.set_xticks([0, 4, 8.5, 12, 15.7]); ax.set_yticks([0, .3, .7, .9, 1])
ax.set_xlabel("x (Liter Bier)"); ax.set_ylabel(r"$\hat F(x)$")
ax.grid(axis="y", color="#e3e7ee")
ax.text(9.5, .2, "● = Wert gehört dazu\n○ = Wert gehört nicht dazu", fontsize=8.5, color=MUT)
save(fig, "ecdf_bier")

# 3 Boxplot erklärt
data = np.array([1,1,1,1,2,2,3,3,3,4,4,5,6,6,6,6,7,9,13,14])
fig, ax = plt.subplots(figsize=(6.6, 2.4))
ax.boxplot(data, vert=False, widths=.5, patch_artist=True,
           boxprops=dict(facecolor="#e3f3f1", edgecolor=TEAL, lw=1.6), medianprops=dict(color=RED, lw=2.2),
           whiskerprops=dict(color=TEAL, lw=1.5), capprops=dict(color=TEAL, lw=1.5),
           flierprops=dict(marker="o", mec=RED, mfc="white", ms=7))
ax.set_yticks([]); ax.set_xlabel("Semesterzahl")
lab = [(1, "unterer Whisker\n= Min = 1", 1.3), (2, "unteres Quartil\n= 2", .45), (4, "Median = 4", 1.3), (6, "oberes Quartil\n= 6", .45),
       (9, "oberer Whisker = 9\n(größter Wert ≤ 12)", 1.3), (13.5, "Ausreißer\n13, 14", 1.3)]
for xx, t, yy in lab:
    ax.annotate(t, xy=(xx, yy), ha="center", fontsize=7.8, color=INK)
ax.set_ylim(.3, 1.7); ax.set_xlim(0, 15.5)
save(fig, "boxplot")

# 4 Schiefe
fig, ax = plt.subplots(1, 3, figsize=(8.2, 2.3))
xs = np.linspace(0, 1, 400)
from math import gamma as G
def beta(xx, a, b):
    return xx ** (a - 1) * (1 - xx) ** (b - 1) * G(a + b) / (G(a) * G(b))
for a_, (A, B, title) in zip(ax, [(2, 5, "rechtsschief / linkssteil"), (4, 4, "symmetrisch"), (5, 2, "linksschief / rechtssteil")]):
    y = beta(xs, A, B)
    a_.fill_between(xs, y, color="#e5eefb"); a_.plot(xs, y, color=BLU, lw=2)
    mode = (A - 1) / (A + B - 2); mean = A / (A + B)
    from scipy.stats import beta as sb  # noqa
    med = sb.median(A, B)
    for v, c, n in [(mode, GRN, "Modus"), (med, ORA, "Median"), (mean, RED, "Mittel")]:
        a_.axvline(v, color=c, lw=1.6, ls="--")
    a_.set_title(title, fontsize=9.5); a_.set_yticks([]); a_.set_xticks([])
from matplotlib.lines import Line2D
fig.legend([Line2D([0],[0],color=c,ls="--") for c in (GRN, ORA, RED)], ["Modus", "Median", "Mittelwert"],
           loc="lower center", ncol=3, frameon=False, fontsize=8.5, bbox_to_anchor=(.5, -.08))
ax[0].set_xlabel(r"$\bar x > x_{med} > x_{mod}$", fontsize=9)
ax[1].set_xlabel(r"$\bar x \approx x_{med} \approx x_{mod}$", fontsize=9)
ax[2].set_xlabel(r"$\bar x < x_{med} < x_{mod}$", fontsize=9)
save(fig, "schiefe")

# 5 Korrelation
rng = np.random.default_rng(3)
fig, ax = plt.subplots(1, 4, figsize=(8.4, 2.2))
n = 70; u = rng.normal(size=n); e = rng.normal(size=n)
sets = [(u, .9 * u + .35 * e, "r ≈ +0.9 (stark positiv)"), (u, -.6 * u + .8 * e, "r ≈ −0.6 (mittel negativ)"),
        (u, e, "r ≈ 0 (kein Zusammenhang)"), (u, u ** 2 + .15 * e, "r ≈ 0, aber quadratisch!")]
for a_, (xx, yy, t) in zip(ax, sets):
    a_.scatter(xx, yy, s=9, color=TEAL, alpha=.8)
    a_.set_title(t, fontsize=8.3); a_.set_xticks([]); a_.set_yticks([])
    a_.set_xlabel(f"r = {np.corrcoef(xx, yy)[0,1]:.2f}", fontsize=8)
save(fig, "korrelation")

# 6 Baumdiagramm (Franziska)
fig, ax = plt.subplots(figsize=(7.2, 3.3)); ax.axis("off")
def node(x0, y0, t, c=INK):
    ax.text(x0, y0, t, ha="center", va="center", fontsize=9, color=c,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=c, lw=1.2))
def edge(p, q, t):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=GRY, lw=1.2, zorder=0)
    ax.text((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 + .02, t, fontsize=8.3, color=VIO, ha="center",
            bbox=dict(fc="white", ec="none", pad=.5))
S = (0.05, .5); Bn = (.35, .78); Nb = (.35, .22)
node(*S, "Start"); node(*Bn, "B: besteht", VIO); node(*Nb, "B̄: fällt durch", VIO)
edge(S, Bn, "0.7"); edge(S, Nb, "0.3")
for base, ps, sgn in [(Bn, ["0.80", "0.15", "0.05"], "B"), (Nb, ["0.10", "0.20", "0.70"], "B̄")]:
    for k, (p, dy) in enumerate(zip(ps, [.16, 0, -.16])):
        q = (.72, base[1] + dy)
        node(*q, f"A{k+1}")
        edge(base, q, p)
        prob = (0.7 if sgn == "B" else 0.3) * float(p)
        ax.text(.8, q[1], f"P(A{k+1} ∩ {sgn}) = {prob:.3f}", fontsize=8.3, va="center", color=INK)
ax.set_xlim(0, 1.1); ax.set_ylim(0, 1)
save(fig, "baum")

# 7 Dichte + Verteilungsfunktion
xs = np.linspace(-4, 4, 400)
fig, ax = plt.subplots(1, 2, figsize=(8, 2.6))
ax[0].plot(xs, phi(xs), color=VIO, lw=2)
m = (xs >= -.5) & (xs <= 1.2)
ax[0].fill_between(xs[m], phi(xs[m]), color=VIO, alpha=.25)
ax[0].text(.35, .12, "Fläche =\nP(a ≤ X ≤ b)", ha="center", fontsize=8.5)
ax[0].set_xticks([-.5, 1.2]); ax[0].set_xticklabels(["a", "b"]); ax[0].set_title("Dichte f(x)")
from scipy.stats import norm
ax[1].plot(xs, norm.cdf(xs), color=VIO, lw=2); ax[1].set_title("Verteilungsfunktion F(x) = P(X ≤ x)")
ax[1].vlines([-.5, 1.2], 0, norm.cdf([-.5, 1.2]), color=GRY, ls=":")
ax[1].hlines(norm.cdf([-.5, 1.2]), -4, [-.5, 1.2], color=GRY, ls=":")
ax[1].annotate("", xy=(-3.5, norm.cdf(1.2)), xytext=(-3.5, norm.cdf(-.5)), arrowprops=dict(arrowstyle="<->", color=RED))
ax[1].text(-3.3, .55, "F(b) − F(a)", color=RED, fontsize=8.5)
ax[1].set_xticks([-.5, 1.2]); ax[1].set_xticklabels(["a", "b"])
save(fig, "dichte_vf")

# 8 Verteilungsgalerie
fig, ax = plt.subplots(2, 3, figsize=(8.4, 4.6))
k = np.arange(0, 11)
ax[0, 0].bar([0, 1], [.7, .3], color=ORA, width=.35); ax[0, 0].set_title("Bernoulli Be(0.3)"); ax[0, 0].set_xticks([0, 1])
ax[0, 1].bar(k, [comb(10, i) * .25 ** i * .75 ** (10 - i) for i in k], color=ORA); ax[0, 1].set_title("Binomial B(10, 0.25)")
kp = np.arange(0, 13)
ax[0, 2].bar(kp, [3 ** i / factorial(i) * exp(-3) for i in kp], color=ORA); ax[0, 2].set_title("Poisson Po(3)")
xs = np.linspace(-1, 3, 400)
ax[1, 0].plot(xs, np.where((xs >= 0) & (xs <= 2), .5, 0), color=BLU, lw=2); ax[1, 0].set_title("Gleichverteilung U(0, 2)")
xs2 = np.linspace(0, 8, 400)
for lam, c in [(.5, BLU), (1, TEAL), (2, VIO)]:
    ax[1, 1].plot(xs2, lam * np.exp(-lam * xs2), color=c, lw=2, label=f"λ = {lam}")
ax[1, 1].legend(frameon=False, fontsize=8); ax[1, 1].set_title("Exponential Exp(λ)")
xs3 = np.linspace(-5, 7, 400)
for mu, s, c in [(0, 1, BLU), (2, 1, TEAL), (0, 2, VIO)]:
    ax[1, 2].plot(xs3, norm.pdf(xs3, mu, s), color=c, lw=2, label=f"N({mu}, {s**2})")
ax[1, 2].legend(frameon=False, fontsize=8); ax[1, 2].set_title("Normal N(μ, σ²)")
for a_ in ax.flat:
    a_.tick_params(labelsize=8)
fig.text(.01, .75, "diskret", rotation=90, color=ORA, fontweight="bold")
fig.text(.01, .28, "stetig", rotation=90, color=BLU, fontweight="bold")
save(fig, "verteilungen")

# 9 Likelihood Münze
p = np.linspace(.001, .999, 400)
L = comb(20, 6) * p ** 6 * (1 - p) ** 14
fig, ax = plt.subplots(1, 2, figsize=(8, 2.6))
ax[0].plot(p, L, color=ORA, lw=2); ax[0].axvline(.3, color=RED, ls="--"); ax[0].set_title("Likelihood L(π)")
ax[0].set_xlabel("π = P(Wappen)"); ax[0].text(.33, L.max() * .9, "Maximum bei\nπ̂ = 6/20 = 0.3", fontsize=8.5)
ax[1].plot(p, np.log(L), color=ORA, lw=2); ax[1].axvline(.3, color=RED, ls="--"); ax[1].set_title("Log-Likelihood ℓ(π) = log L(π)")
ax[1].set_xlabel("π"); ax[1].set_ylim(-25, 0); ax[1].text(.33, -20, "gleiche Stelle\ndes Maximums!", fontsize=8.5)
save(fig, "likelihood")

# 10 Ablehnungsbereiche
xs = np.linspace(-4, 4, 500)
fig, ax = plt.subplots(1, 3, figsize=(8.4, 2.3))
cfg = [("zweiseitig: H₁: μ ≠ μ₀", [(-4, -1.96), (1.96, 4)], "±z₁₋α/₂"),
       ("linksseitig: H₁: μ < μ₀", [(-4, -1.645)], "−z₁₋α"),
       ("rechtsseitig: H₁: μ > μ₀", [(1.645, 4)], "z₁₋α")]
for a_, (t, regs, lbl) in zip(ax, cfg):
    a_.plot(xs, phi(xs), color=BLU, lw=2)
    for lo, hi in regs:
        m = (xs >= lo) & (xs <= hi)
        a_.fill_between(xs[m], phi(xs[m]), color=RED, alpha=.45)
    a_.set_title(t, fontsize=8.8); a_.set_yticks([])
    ticks = [r[1] if r[0] == -4 else r[0] for r in regs]
    a_.set_xticks(ticks); a_.set_xticklabels([f"{v:.2f}" for v in ticks], fontsize=8)
    a_.text(0, .05, "H₀ beibehalten", ha="center", fontsize=7.5, color=MUT)
fig.text(.5, -.03, "rot = Ablehnungsbereich (Fläche = α; beim zweiseitigen Test je α/2). Beispiel α = 0.05", ha="center", fontsize=8.5, color=MUT)
save(fig, "ablehnung")

# 11 KI-Simulation
rng = np.random.default_rng(7)
mu, sig, n = 34.9, 9.4, 20
fig, ax = plt.subplots(figsize=(7.6, 2.8))
miss = 0
for i in range(50):
    s = rng.normal(mu, sig, n)
    m, sd = s.mean(), s.std(ddof=1)
    half = 2.093 * sd / np.sqrt(n)
    hit = (m - half <= mu <= m + half)
    miss += (not hit)
    ax.plot([i, i], [m - half, m + half], color=BLU if hit else RED, lw=1.8)
    ax.plot(i, m, "o", color=BLU if hit else RED, ms=2.5)
ax.axhline(mu, color=INK, ls="--", lw=1); ax.text(50.5, mu, "wahres μ", va="center", fontsize=8.5)
ax.set_xlabel("Stichprobe Nr."); ax.set_ylabel("95%-KI")
ax.set_title(f"50 Stichproben → 50 Intervalle; {miss} treffen μ nicht (rot) – erwartet ca. 5 %", fontsize=9.5)
save(fig, "ki_sim")

# 12 Chi²-Test Varianz (Umsatzbeispiel)
from scipy.stats import chi2
xs = np.linspace(0.01, 30, 500)
fig, ax = plt.subplots(figsize=(6.4, 2.5))
ax.plot(xs, chi2.pdf(xs, 11), color=BLU, lw=2)
c = chi2.ppf(.1, 11)
m = xs <= c; ax.fill_between(xs[m], chi2.pdf(xs[m], 11), color=RED, alpha=.35, label=f"Ablehnungsbereich [0; {c:.2f}] (α = 0.1)")
m2 = xs <= 4.93; ax.fill_between(xs[m2], chi2.pdf(xs[m2], 11), color=RED, alpha=.55, hatch="///", label="p-Wert = P(Z ≤ 4.93) = 0.065")
ax.axvline(4.93, color=INK, lw=1, ls="--"); ax.text(5.2, .085, "Prüfgröße 4.93", fontsize=8.5)
ax.legend(frameon=False, fontsize=8); ax.set_title("χ²(11)-Dichte unter H₀ (linksseitiger Test)"); ax.set_yticks([])
save(fig, "chi2_test")

# 13 Histogramm vs Kerndichte
rng = np.random.default_rng(11)
d = np.concatenate([rng.normal(-1, .6, 120), rng.normal(1.5, .8, 80)])
from scipy.stats import gaussian_kde
fig, ax = plt.subplots(1, 3, figsize=(8.4, 2.3))
xs = np.linspace(-3.5, 4.5, 400)
for a_, bw, t in zip(ax, [.08, None, 1.0], ["Bandweite zu klein → zu rau", "passende Bandweite", "Bandweite zu groß → zu glatt"]):
    a_.hist(d, bins=20, density=True, color="#e5eefb", edgecolor="white")
    kde = gaussian_kde(d, bw_method=bw)
    a_.plot(xs, kde(xs), color=BLU, lw=2); a_.set_title(t, fontsize=8.8); a_.set_yticks([])
save(fig, "kde")

# 14 Bias / Varianz Zielscheibe
fig, ax = plt.subplots(1, 4, figsize=(8.4, 2.3))
rng = np.random.default_rng(2)
cases = [(0, .15, "unverzerrt,\nkleine Varianz ✓"), (0, .5, "unverzerrt,\ngroße Varianz"),
         (.55, .15, "verzerrt,\nkleine Varianz"), (.55, .5, "verzerrt,\ngroße Varianz")]
for a_, (b, s, t) in zip(ax, cases):
    for r_, c in [(1, "#fdecec"), (.66, "#fbd5d5"), (.33, "#f6b3b3")]:
        a_.add_patch(plt.Circle((0, 0), r_, color=c))
    a_.plot(0, 0, "+", color=RED, ms=10, mew=2)
    pts = rng.normal(0, s, (25, 2)) + np.array([b, b * .6])
    a_.scatter(pts[:, 0], pts[:, 1], s=9, color=BLU)
    a_.set_xlim(-1.2, 1.4); a_.set_ylim(-1.2, 1.4); a_.set_aspect("equal"); a_.axis("off")
    a_.set_title(t, fontsize=8.5)
save(fig, "bias_var")

# 15 Standardnormal Quantile
xs = np.linspace(-4, 4, 400)
fig, ax = plt.subplots(figsize=(6.4, 2.4))
ax.plot(xs, phi(xs), color=BLU, lw=2)
m = xs <= 1.96; ax.fill_between(xs[m], phi(xs[m]), color=BLU, alpha=.15)
ax.axvline(1.96, color=RED, ls="--"); ax.text(2.05, .25, "z₀.₉₇₅ = 1.96\nqnorm(0.975)", fontsize=8.5, color=RED)
ax.text(-.6, .12, "Fläche = 0.975\n= Φ(1.96)\n= pnorm(1.96)", fontsize=8.5, ha="center")
ax.set_yticks([]); ax.set_title("Standardnormalverteilung N(0, 1): p-Funktion ↔ q-Funktion")
save(fig, "quantil")
print("Abbildungen fertig:", len(os.listdir(OUT)))

# 16 Histogramm Wartezeiten Schritt für Schritt
w = np.array([2,3,3,4,5,5,6,7,8,9,10,11,12,14,15,18,22,25,31,38])
br = np.array([0, 5, 10, 20, 40]); cnt, _ = np.histogram(w, bins=br); dens = cnt / len(w) / np.diff(br)
fig, ax = plt.subplots(figsize=(6.8, 2.9))
ax.bar(br[:-1], dens, width=np.diff(br), align="edge", color="#cfe9e5", edgecolor=TEAL, lw=1.4)
for a, b, d, c in zip(br[:-1], br[1:], dens, cnt):
    ax.text((a + b) / 2, d + .002, f"Höhe {d:.2f}\n({c} Werte, f={c/20:.1f})", ha="center", fontsize=7.8)
m15 = (15, 30); ax.axvspan(*m15, color=ORA, alpha=.12); ax.text(22.5, .075, "gesucht: Anteil 15 bis 30", color=ORA, ha="center", fontsize=8.3)
ax.axvline(12.4, color=RED, ls="--", lw=1.4); ax.axvline(9.5, color=GRN, ls="--", lw=1.4)
ax.text(12.9, .062, "x̄ = 12.4", color=RED, fontsize=8.3); ax.text(3.2, .07, "Median = 9.5", color=GRN, fontsize=8.3)
ax.set_xticks(br); ax.set_ylim(0, .085); ax.set_xlabel("Wartezeit in Minuten"); ax.set_ylabel("Dichte")
ax.set_title("Histogramm der 20 Wartezeiten (rechtsschief: x̄ > Median)")
save(fig, "hist_warte")
