"""Führt alle R-Beispiele der Formelsammlung in einer R-Sitzung aus und setzt den echten Output ein."""
import os, re, shutil, subprocess, html
from fscommon import SRC

WD = os.path.join(SRC, "rwork", "fsr")


def _code_line(line):
    """Code-Zeile einfärben: Kommentar ab # (außerhalb von Anführungszeichen) grau."""
    q = None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == "#":
            return html.escape(line[:i]) + '<span class="c">' + html.escape(line[i:]) + "</span>"
    return html.escape(line)


def fmt(text, run=True):
    out = []
    for ln in text.rstrip("\n").split("\n"):
        if not run:
            out.append(_code_line(ln))
        elif ln.startswith("> ") or ln.startswith("+ ") or ln in (">", "+"):
            out.append(_code_line(ln))
        else:
            out.append('<span class="o">%s</span>' % html.escape(ln))
    return '<pre class="r">%s</pre>' % "\n".join(out)


def run_all(doc):
    os.makedirs(WD, exist_ok=True)
    shutil.copy(os.path.join(SRC, "..", "uebungsdaten", "Taverne.csv"), WD)
    ents = [e for s in doc.secs for e in s["entries"] if e.get("r")]
    for e in ents:
        if not e.get("run", True):
            e["rhtml"] = fmt(e["r"], run=False)
    chunks = [e for e in ents if e.get("run", True)]
    L = ['invisible(Sys.setlocale("LC_ALL", "C.UTF-8"))', "options(width = 74, warn = 1)",
         'sink(stdout(), type = "message")']
    for k, e in enumerate(chunks):
        if e.get("setup"):
            L.append(e["setup"])
        L.append('cat("@@B%d@@\\n")' % k)
        L.append('try(source(textConnection(r"---(%s)---"), echo = TRUE, max.deparse.length = Inf, '
                 'prompt.echo = "> ", continue.echo = "+ ", spaced = FALSE, keep.source = TRUE))' % e["r"].strip("\n"))
        L.append('cat("@@E%d@@\\n")' % k)
    open(os.path.join(WD, "run.R"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    r = subprocess.run(["Rscript", "run.R"], cwd=WD, capture_output=True, text=True)
    out = r.stdout
    for k, e in enumerate(chunks):
        try:
            seg = out.split("@@B%d@@\n" % k, 1)[1].split("@@E%d@@" % k, 1)[0]
        except IndexError:
            raise SystemExit("R-Chunk %s fehlt im Output:\n%s\n%s" % (e["no"], out[-2000:], r.stderr[-2000:]))
        if re.search(r"(^|\n)Error", seg) and not e.get("err_ok"):
            raise SystemExit("R-Fehler in %s:\n%s" % (e["no"], seg))
        e["rhtml"] = fmt(seg)
    return len(chunks)
