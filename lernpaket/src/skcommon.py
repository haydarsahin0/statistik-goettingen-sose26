"""Gemeinsame Helfer für den Statistik-Komplettkurs (gen_skurs.py)."""
from fractions import Fraction as Fr
import math

C = []      # Karten und Abschnitte in Reihenfolge
LOG = []    # Kontrollwerte (werden beim Bauen ausgegeben)


def sec(t, intro=None, wissen=None):
    """Neuer Abschnitt. wissen = Liste von HTML-Punkten für den Kasten 'Das musst du wissen'."""
    C.append(dict(kind="sec", t=t, intro=intro, wissen=wissen))


def card(title, p, auf, steps, loes, warn=None, fig=None, bsp=None, figw=62):
    C.append(dict(kind="card", title=title, p=p, auf=auf, steps=steps, loes=loes,
                  warn=warn, fig=fig, bsp=bsp, figw=figw))


def T(_tpl, **kw):
    """Platzhalter «name» durch Werte ersetzen (LaTeX-Klammern bleiben unberührt)."""
    for k, v in kw.items():
        _tpl = _tpl.replace("«%s»" % k, str(v))
    assert "«" not in _tpl, _tpl
    return _tpl


def r3(x):
    """Kaufmännisch auf 3 Nachkommastellen (wie in der Klausur verlangt)."""
    return "%.3f" % (math.floor(x * 1000 + 0.5 + 1e-12) / 1000 if x >= 0 else -math.floor(-x * 1000 + 0.5 + 1e-12) / 1000)


def r4(x):
    return "%.4f" % (math.floor(x * 10000 + 0.5 + 1e-12) / 10000 if x >= 0 else -math.floor(-x * 10000 + 0.5 + 1e-12) / 10000)


def r2(x):
    return "%.2f" % (math.floor(x * 100 + 0.5 + 1e-12) / 100 if x >= 0 else -math.floor(-x * 100 + 0.5 + 1e-12) / 100)


def fr(x):
    """Bruch als LaTeX: \\frac{a}{b} (ganze Zahl ohne Bruch)."""
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator)
    s = "-" if x < 0 else ""
    return r"%s\frac{%d}{%d}" % (s, abs(x.numerator), x.denominator)


def log(name, val):
    LOG.append((name, val))
