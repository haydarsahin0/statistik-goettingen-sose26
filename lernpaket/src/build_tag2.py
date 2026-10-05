"""Baut Tag2_Zufall_und_Modelle.pdf aus gen_tag2 (Seiten 1–10) und tag2_rest (Rest)."""
import os, subprocess
import gen_tag2
import tag2_rest  # noqa: F401  (hängt die restlichen Seiten an)

for d in gen_tag2.P:
    if d["nxt"] == "Weiter: c bestimmen" and "Die Fläche <em>ist</em>" in d["body"]:
        d["nxt"] = "Weiter: Integral-Crashkurs"
import re
html = gen_tag2.render_pages()
# inline-Brüche groß setzen (auf Papier und Handy besser lesbar)
html = re.sub(r"\\\((.+?)\\\)", lambda m: "\\(" + re.sub(r"\\t?frac(?![a-z])", r"\\dfrac", m.group(1)) + "\\)", html, flags=re.S)
open(os.path.join(gen_tag2.SRC, "content", "tag2.html"), "w", encoding="utf-8").write(html)
r = subprocess.run(["node", "build_day.js"], cwd=gen_tag2.SRC, capture_output=True, text=True,
                   env=dict(os.environ, PART="tag2.html", OUTNAME="Tag2_Zufall_und_Modelle.pdf", TITLE="Tag 2 · Zufall & Modelle"))
print(len(gen_tag2.P), "Seiten", r.stdout.strip(), r.stderr[-1500:])
