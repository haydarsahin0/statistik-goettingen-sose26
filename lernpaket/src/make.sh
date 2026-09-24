#!/bin/sh
# Baut das Lernbuch-PDF (braucht node, katex, playwright/chromium)
# Beispiel nur Tag 1: PARTS=titel.html,tag1.html OUTNAME=Lernbuch_Tag1.pdf ./make.sh
cd "$(dirname "$0")" && CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome node build.js
