/* ================= TAG 5 · Testen & Generalprobe ================= */

L({id:"5.1",day:5,no:1,title:"Die Logik statistischer Tests",min:60,rel:3,
src:["V11","Tutorium 11","R-Skript 11"],
goal:"Du formulierst H₀ und H₁ richtig herum, kennst Fehler 1. und 2. Art, verstehst Ablehnbereich und p-Wert und schreibst eine korrekte Testentscheidung.",
blocks:[
{t:"idea",h:"Was ein Test macht",de:r`
<p>Wir wollen eine Behauptung über einen Parameter mit Daten <b>statistisch absichern</b>. Dazu stellen wir zwei sich ausschließende Hypothesen auf: die <b>Nullhypothese \(H_0\)</b> und die <b>Alternativhypothese \(H_1\)</b>. Eine <b>Teststatistik</b> (Prüfgröße) misst, wie stark die Daten gegen \(H_0\) sprechen. Liegt sie im <b>Ablehnbereich</b>, verwerfen wir \(H_0\).</p>`,
tr:r`Test: H₀ (sıfır hipotezi) ile H₁ (alternatif) karşılaştırılır. Test istatistiği ret bölgesine düşerse H₀ reddedilir.`},
{t:"rule",k:"Die wichtigste Regel",de:r`Was <b>bewiesen / abgesichert</b> werden soll, gehört in \(H_1\). Nur \(H_1\) kann statistisch bewiesen werden; \(H_0\) kann man nur „nicht verwerfen“ (schwache Aussage). Das Gleichheitszeichen steht immer in \(H_0\).`,tr:r`Kanıtlamak istediğin şey H₁'e yazılır. Eşittir işareti (=, ≤, ≥) her zaman H₀'dadır. H₀ „kabul edilmez“, sadece „reddedilemez“.`},
{t:"idea",h:"Zwei mögliche Fehler",de:r`
<div class="tbl"><table><tr><th></th><th>Entscheidung: \(H_0\) verwerfen</th><th>\(H_0\) nicht verwerfen</th></tr>
<tr><th class="l">\(H_0\) wahr</th><td style="color:var(--bad)"><b>Fehler 1. Art (α-Fehler)</b></td><td>richtig</td></tr>
<tr><th class="l">\(H_0\) falsch</th><td>richtig</td><td style="color:var(--bad)"><b>Fehler 2. Art (β-Fehler)</b></td></tr></table></div>
<p>Man kann nicht beide klein halten: \(\alpha_{max}+\beta_{max}=1\). Deshalb <b>asymmetrisch</b>: wir begrenzen nur den Fehler 1. Art durch das <b>Signifikanzniveau</b> \(\alpha\) (üblich 0.1, 0.05, 0.01). Der Fehler 2. Art kann groß sein.</p>`,
tr:r`1. tür hata: H₀ doğruyken reddetmek (α ile sınırlandırılır). 2. tür hata: H₀ yanlışken reddetmemek (büyük olabilir).`},
{t:"formula",h:"p-Wert",tex:r`p=P_{H_0}\big(\text{Teststatistik mindestens so extrem wie } z_{obs}\big)\qquad p\le\alpha\ \Rightarrow\ H_0\ \text{verwerfen}`,
parts:[["p_{links}","\\(P(Z\\le z_{obs})\\)"],["p_{rechts}","\\(P(Z\\ge z_{obs})=1-P(Z\\le z_{obs})\\)"],["p_{zweiseitig}","\\(2\\cdot\\min(p_{links},p_{rechts})\\)"]],
note:r`Andere Deutung: der p-Wert ist das <b>kleinste Signifikanzniveau</b>, zu dem \(H_0\) gerade noch verworfen werden kann.`,tr:r`p-değeri: H₀ doğruysa gözlenenden daha uç bir değer görme olasılığı. p ≤ α ise H₀ reddedilir.`},
{t:"widget",w:"test"},
{t:"ex",h:"Binomialtest: Impfstoff (V11)",q:r`Behauptung: 50 % zeigen Antikörper. Von \(n=20\) zeigen 15 Antikörper. \(H_0:\pi=0.5\) vs. \(H_1:\pi\ne0.5\), \(\alpha=0.05\).`,
steps:[r`Teststatistik \(Z\) = Anzahl mit Reaktion, unter \(H_0\): \(Z\sim B(20,0.5)\). Zweiseitig → \(\alpha/2=0.025\) auf jeder Seite.`,
r`Ablehnbereich: \(P(Z\le5)=0.0207\le0.025\), \(P(Z\ge15)=0.0207\le0.025\) (aber \(P(Z\ge14)=0.058\)). Also \(A=\{0,\dots,5\}\cup\{15,\dots,20\}\). <small class="muted">(Auf der Folie steht 14 — nachgerechnet ist es 15; am Ergebnis ändert das nichts.)</small>`,
r`p-Wert: \(P_{H_0}(Z\ge15)=\) <code>1-pbinom(14,20,0.5)</code> \(=0.0207\le0.025\) → verwerfen.`,
r`KI: \(\hat\pi=0.75\), \(0.75\pm1.96\sqrt{\frac{0.75\cdot0.25}{20}}=[0.56,\,0.94]\) enthält 0.5 nicht → verwerfen.`],a:r`Alle drei Wege führen zur selben Entscheidung: \(H_0\) verwerfen.`},
{t:"idea",h:"Drei gleichwertige Wege zur Entscheidung",de:r`<ol><li><b>Teststatistik + Ablehnbereich</b>: liegt \(z_{obs}\) in \(A\)?</li><li><b>p-Wert</b>: ist \(p\le\alpha\)?</li><li><b>Konfidenzintervall</b> (nur zweiseitig): \(H_0:\vartheta=\vartheta_0\) wird zum Niveau \(\alpha\) verworfen genau dann, wenn das \((1-\alpha)\)-KI \(\vartheta_0\) <b>nicht</b> enthält.</li></ol>`},
{t:"rule",k:"Musterformulierung Testentscheidung",de:r`„Da der p-Wert = 0.014 &lt; α = 0.05 ist, wird \(H_0\) verworfen. Die Alternative ist zum Niveau 5 % statistisch abgesichert.“ — bzw. „Da p = 0.158 &gt; α = 0.1, kann \(H_0\) nicht verworfen werden.“`,tr:r`Karar cümlesi: sayı + karşılaştırma + sonuç. „H₀ kabul edildi“ yazma; „H₀ reddedilemez“ yaz.`},
{t:"mc",q:r`Im letzten Jahr waren 10 % der Studierenden mit der Mensa unzufrieden. Der Speiseplan wurde geändert. Man möchte zeigen, dass der Anteil <b>gesunken</b> ist. Welches Hypothesenpaar? (Tutorium 11)`,o:[r`\(H_0:p\le0.1\) vs. \(H_1:p\gt0.1\)`,r`\(H_0:p\ge0.1\) vs. \(H_1:p\lt0.1\)`,r`\(H_0:p=0.1\) vs. \(H_1:p\ne0.1\)`],k:1,why:r`Was abgesichert werden soll („gesunken“, also \(p\lt0.1\)), kommt in \(H_1\).`},
{t:"mc",q:r`Ein Test liefert p = 0.2715. Welche Aussage stimmt? (Tutorium 11, Aufgabe 3)`,o:["H₀ ist bewiesen.","H₀ kann zu keinem der gängigen Niveaus verworfen werden; man kann aber nicht sagen, dass H₀ gilt.","H₁ ist zum Niveau 5 % abgesichert."],k:1,why:r`Nicht verwerfen heißt nicht bestätigen. Erst ab \(\alpha\ge0.2715\) würde man verwerfen — ein sinnloses Niveau.`}
]});

L({id:"5.2",day:5,no:2,title:"Gauß-Test & t-Test für μ",min:70,rel:3,
src:["V12","Tutorium 12","Testat 6","Probeklausur A8","R-Skript 12"],
goal:"Du führst den Test für den Erwartungswert komplett durch (Hypothesen, Prüfgröße, Verteilung, Ablehnbereich, p-Wert, Entscheidung) — per Hand und mit t.test in R.",
blocks:[
{t:"formula",h:"Gauß-Test (σ bekannt)",tex:r`Z=\frac{\bar X-\mu_0}{\sigma}\sqrt n\ \overset{H_0}{\sim}\ N(0,1)`},
{t:"formula",h:"t-Test (σ unbekannt)",tex:r`T=\frac{\bar X-\mu_0}{S_*}\sqrt n\ \overset{H_0}{\sim}\ t(n-1)`},
{t:"idea",h:"Ablehnbereiche (Tabelle aus Tutorium 11/12)",de:r`
<div class="tbl"><table><tr><th class="l">\(H_1\)</th><th>Name</th><th>Gauß-Test: verwerfen, wenn</th><th>t-Test: verwerfen, wenn</th><th>p-Wert</th></tr>
<tr><td class="l">\(\mu\lt\mu_0\)</td><td>linksseitig</td><td>\(z\le-z_{1-\alpha}\)</td><td>\(t\le-t_{n-1,1-\alpha}\)</td><td>\(P(Z\le z)\)</td></tr>
<tr><td class="l">\(\mu\gt\mu_0\)</td><td>rechtsseitig</td><td>\(z\ge z_{1-\alpha}\)</td><td>\(t\ge t_{n-1,1-\alpha}\)</td><td>\(1-P(Z\le z)\)</td></tr>
<tr><td class="l">\(\mu\ne\mu_0\)</td><td>zweiseitig</td><td>\(|z|\ge z_{1-\alpha/2}\)</td><td>\(|t|\ge t_{n-1,1-\alpha/2}\)</td><td>\(2(1-P(Z\le|z|))\)</td></tr></table></div>`,
tr:r`H₁'deki işaret, ret bölgesinin yönünü gösterir: „<“ → sol, „>“ → sağ, „≠“ → iki taraf (α/2).`},
{t:"ex",h:"Bleistiftlänge (V12)",q:r`Soll: 17 cm. Gemessen: 19.2, 17.4, 18.5, 16.5, 18.9 (\(\bar x=18.1\)). \(H_0:\mu=17\) vs. \(H_1:\mu\ne17\), \(\alpha=0.01\).`,
steps:[r`<b>σ² = 2.25 bekannt</b>: \(z=\frac{18.1-17}{1.5}\sqrt5=1.64\). Kritischer Wert \(z_{0.995}=2.576\). \(|1.64|\lt2.576\) → nicht verwerfen.`,
r`p-Wert: \(2(1-\Phi(1.64))=0.10\gt0.01\). KI 99 %: \(18.1\pm2.576\cdot\frac{1.5}{\sqrt5}=[16.37,\,19.83]\ni17\).`,
r`<b>σ unbekannt</b>: \(s_*^2=1.265\), \(t=\frac{18.1-17}{\sqrt{1.265}}\sqrt5=2.187\). \(t_{4,0.995}=4.604\). \(|2.187|\lt4.604\) → nicht verwerfen.`],a:r`In beiden Fällen: \(H_0\) kann zum Niveau 1 % nicht verworfen werden.`},
{t:"num",q:r`Lucky Luke (Tutorium 12, Aufgabe 1): Schatten-Zeiten 218, 169, 238, 183 ms (\(\bar x=202\)), \(\sigma^2=400\) bekannt. Absichern, dass der Schatten <b>langsamer als 180 ms</b> ist. Prüfgröße und p-Wert?`,f:[{l:"z =",a:2.2},{l:"p =",a:.013903,tol:.0006}],why:r`\(H_0:\mu\le180\) vs. \(H_1:\mu\gt180\). \(z=\frac{202-180}{20}\sqrt4=2.2\sim N(0,1)\). Rechtsseitig: <code>1-pnorm(2.2)</code> = 0.014. → Verwerfen bei α = 10 % und 5 %, nicht bei 1 %.`},
{t:"num",q:r`Cappuccino (Testat 6, Aufgabe 5): Preis in Göttingen \(N(3.50,\,0.40^2)\). Ein Kaffee kostete 4.28 €. Zweiseitig, α = 0.05, \(n=1\). Prüfgröße, p-Wert und Grenzen des 95 %-KI um 4.28?`,f:[{l:"z =",a:1.95},{l:"p =",a:.051176,tol:.0006},{l:"KI unten =",a:3.496},{l:"KI oben =",a:5.064}],why:r`\(H_0:\mu=3.5\) vs. \(H_1:\mu\ne3.5\). \(z=\frac{4.28-3.5}{0.4}=1.95\). \(p=2(1-\Phi(1.95))=0.051\gt0.05\). KI \(4.28\pm1.96\cdot0.4=[3.496,\,5.064]\) enthält 3.5 → \(H_0\) nicht verwerfen: Man kann nicht absichern, dass der Kaffee nicht aus Göttingen war.`},
{t:"r",h:"t.test lesen (Testat 6, Aufgabe 6)",code:r`
aufgaben <- c(18, 28, 19, 22, 20, 23, 17, 24, 19, 21)
t.test(aufgaben, mu = 20, alternative = "g", conf.level = 0.9)
qt(0.9, df = 9)            # kritischer Wert für alpha = 0.1, rechtsseitig`,
out:r`
	One Sample t-test
data:  aufgaben
t = 1.0601, df = 9, p-value = 0.1584
alternative hypothesis: true mean is greater than 20
90 percent confidence interval:
 19.66493      Inf
sample estimates:
mean of x
     21.1
[1] 1.383029`,
notes:[[2,"<code>alternative</code>: <code>\"two.sided\"</code> (Standard), <code>\"less\"</code>/<code>\"l\"</code> (\\(H_1:\\mu\\lt\\mu_0\\)), <code>\"greater\"</code>/<code>\"g\"</code> (\\(H_1:\\mu\\gt\\mu_0\\)). Die Richtung von \\(H_1\\)!","alternative = H₁'in yönü: less, greater veya two.sided."],[3,"Ablehnbereich \\(A=[1.383,\\infty)\\). \\(t=1.060\\notin A\\), \\(p=0.158\\gt0.1\\) → \\(H_0:\\mu\\le20\\) wird nicht verworfen.",""]]},
{t:"exam",h:"Probeklausur Aufgabe 8 — Skispringen",src:"Probeklausur A-Teil",q:r`Stahlbichler: 130, 134, 129.5, 132.5 (\(\bar x=131.5\)); \(\sigma^2=16\) bekannt, Normalverteilung. Statistisch absichern, dass Stahlbichler <b>nicht weiter als 133.5 m</b> springt.`,
parts:[{q:r`(a) Hypothesenpaar.`,p:2,s:r`\(H_0:\mu\ge133.5\) vs. \(H_1:\mu\lt133.5\).`},
{q:r`(b) Prüfgröße und ihre Verteilung.`,p:3,s:r`\(Z=\frac{\bar X-\mu_0}{\sigma}\sqrt n=\frac{131.5-133.5}{4}\sqrt4=-1\sim N(0,1)\).`},
{q:r`(c) Welcher R-Code: (1) Fiedler-Daten mit "l", p = 0.5; (2) Stahlbichler mit "l", p = 0.07791; (3) Stahlbichler mit "g", p = 0.9221? Testentscheidung zum Niveau 10 % mit Begründung.`,p:3,s:r`Code <b>(2)</b>: richtige Daten, linksseitige Alternative. Da \(p=0.07791\lt0.1\), wird \(H_0\) verworfen: Es ist zum Niveau 10 % abgesichert, dass Stahlbichler im Mittel weniger als 133.5 m springt.`}]},
{t:"trap",items:[r`\(\bar X\) und \(\mu_0\) vertauscht → falsches Vorzeichen.`,r`Zweiseitig getestet, aber \(z_{1-\alpha}\) statt \(z_{1-\alpha/2}\) genommen.`,r`Bei einseitigem Test den p-Wert der falschen Seite berechnet (<code>pnorm(z)</code> vs. <code>1-pnorm(z)</code>).`,r`Verteilung der Prüfgröße nicht angegeben (kostet 1 Punkt).`]}
]});

L({id:"5.3",day:5,no:3,title:"Tests für Anteil, Varianz & Median",min:60,rel:3,
src:["V12","Tutorium 11, 12","Testat 6"],
goal:"Du testest einen Anteil (Normalapproximation und binom.test), eine Varianz (χ²) und einen Median (Vorzeichentest).",
blocks:[
{t:"formula",h:"Test für einen Anteil (Normalapproximation)",tex:r`Z=\frac{X-n\pi_0}{\sqrt{n\pi_0(1-\pi_0)}}=\frac{\hat\pi-\pi_0}{\sqrt{\pi_0(1-\pi_0)/n}}\ \overset{a}{\sim}\ N(0,1)`,parts:[["X","Anzahl Erfolge"],["\\pi_0","Wert aus \\(H_0\\) — im Nenner steht \\(\\pi_0\\), nicht \\(\\hat\\pi\\)!"]]},
{t:"num",q:r`Iran (Tutorium 11, Aufgabe 2): 74 877 Fälle, 4683 Todesfälle. Absichern, dass die Letalität <b>kleiner</b> als der globale Wert 0.064 ist. Prüfgröße und p-Wert?`,f:[{l:"Z =",a:-1.62942,tol:.0015},{l:"p =",a:.051612,tol:.0006}],why:r`\(H_0:\pi\ge0.064\) vs. \(H_1:\pi\lt0.064\). \(Z=\frac{4683-74877\cdot0.064}{\sqrt{74877\cdot0.064\cdot0.936}}=\frac{-109.128}{66.973}=-1.629\). Ablehnbereiche: 1 %: \((-\infty,-2.326]\), 5 %: \((-\infty,-1.645]\), 10 %: \((-\infty,-1.282]\) → nur zum Niveau 10 % verwerfen. \(p=\Phi(-1.629)=0.052\).`},
{t:"r",h:"Exakter Binomialtest in R (Tutorium 11, Aufgabe 3)",code:r`
binom.test(23476, 578268, p = 0.04, alternative = "two.sided")
binom.test(23476, 578268, p = 0.04, alternative = "greater")
binom.test(3254, 127584, p = 0.026)`,
out:r`
p-value = 0.02079   95 percent confidence interval: 0.04008 0.04110
p-value = 0.01046
p-value = 0.2715`,
notes:[[1,"USA, \\(H_1:\\pi\\ne0.04\\): verwerfen bei 5 % (p = 0.021 &lt; 0.05, und 0.04 liegt nicht im KI), <b>nicht</b> bei 2 % (0.021 &gt; 0.02).","İki taraflı test %2 düzeyinde reddedemez."],[2,"Einseitig (\\(H_1:\\pi\\gt0.04\\)): p = 0.010 &lt; 0.02 → jetzt verwerfen. Die Formulierung der Hypothese ändert die Entscheidung!","Aynı veri, farklı hipotez → farklı karar."]]},
{t:"formula",h:"χ²-Test für die Varianz",tex:r`X=\frac{(n-1)S_*^2}{\sigma_0^2}=\frac{nS^2}{\sigma_0^2}\ \overset{H_0}{\sim}\ \chi^2(n-1)`,parts:[["H_1:\\sigma^2\\lt\\sigma_0^2","verwerfen, wenn \\(X\\le\\chi^2_{\\alpha}(n-1)\\)"],["H_1:\\sigma^2\\gt\\sigma_0^2","verwerfen, wenn \\(X\\ge\\chi^2_{1-\\alpha}(n-1)\\)"],["H_1:\\sigma^2\\ne\\sigma_0^2","\\(X\\le\\chi^2_{\\alpha/2}\\) oder \\(X\\ge\\chi^2_{1-\\alpha/2}\\)"]],note:r`In R: <b>nicht</b> <code>chisq.test</code> (das ist der Unabhängigkeitstest)!`},
{t:"ex",h:"Umsatzschwankung (Tutorium 12, Aufgabe 2)",q:r`Alte Varianz 71 479.11. 12 neue Monatsumsätze: 970, 812, 601, 623, 500, 541, 475, 399, 531, 766, 689, 902. Ist die Schwankung signifikant <b>kleiner</b> geworden? α = 0.1.`,
steps:[r`\(H_0:\sigma^2\ge71479.11\) vs. \(H_1:\sigma^2\lt71479.11\).`,r`\(\bar x=650.75\), \(S^2=29368.02\), \(S_*^2=32037.84\).`,r`\(X=\frac{11\cdot32037.84}{71479.11}=4.930\sim\chi^2(11)\).`,r`Kritischer Wert <code>qchisq(0.1, 11)</code> = 5.58 → \(A=[0;\,5.58]\). \(4.930\in A\) → verwerfen. p-Wert <code>pchisq(4.930, 11)</code> = 0.065 &lt; 0.1.`],a:r`\(H_1\) abgesichert: die Umsatzschwankung ist kleiner geworden (α = 10 %).`},
{t:"num",q:r`Kaffeemaschine (Testat 6, Aufgabe 7): Füllmengen 0.32, 0.35, 0.34, 0.37, 0.36 l. Soll: \(\sigma\lt0.08\). (1) unverzerrte Varianz (4 NK), (3) Prüfgröße (mit ungerundetem \(s_*^2\)). α = 0.01, \(\chi^2_{0.01}(4)=0.297\).`,f:[{l:"s*² =",a:.0004,tol:.00005},{l:"X =",a:.23125,tol:.002}],why:r`\(\bar x=0.348\), \(\sum(x_i-\bar x)^2=0.00148\), \(s_*^2=0.00037\approx0.0004\). \(H_0:\sigma^2\ge0.0064\) vs. \(H_1:\sigma^2\lt0.0064\) (\(0.08^2\)!). \(X=\frac{4\cdot0.00037}{0.0064}=0.231\lt0.297\) → \(H_0\) verwerfen: die neue Maschine füllt gleichmäßiger.`},
{t:"idea",h:"Vorzeichentest für den Median (V12)",de:r`<p>Ohne Verteilungsannahme: \(Z\) = Anzahl der Beobachtungen \(\le\vartheta_0\). Unter \(H_0:x_{med}=\vartheta_0\) gilt \(Z\sim B(n,0.5)\) — ein Binomialtest.</p><p>Beispiel Genesungsdauer: 49, 58, 75, 110, 112, 132, 151, 276, 281, 362 Wochen; \(H_0:x_{med}=200\). \(z=7\) Werte ≤ 200. \(p=P(Z\le3)+P(Z\ge7)=2\cdot0.1719=0.344\gt0.05\) → nicht verwerfen.</p>`,tr:r`İşaret testi: medyan hakkında dağılım varsayımı olmadan; ≤θ₀ olan gözlem sayısı B(n, 0.5).`}
]});

L({id:"5.4",day:5,no:4,title:"χ²-Unabhängigkeits- & Anpassungstest",min:45,rel:2,
src:["V12","R-Skript 12"],
goal:"Du testest mit einer Kontingenztafel auf Unabhängigkeit und prüfst, ob Daten zu vorgegebenen Wahrscheinlichkeiten passen — Freiheitsgrade inklusive.",
blocks:[
{t:"formula",h:"χ²-Unabhängigkeitstest",tex:r`Z=\sum_{j=1}^{J}\sum_{k=1}^{K}\frac{(h_{jk}-\tilde h_{jk})^2}{\tilde h_{jk}}\ \overset{a}{\sim}\ \chi^2\big((J-1)(K-1)\big)\qquad \tilde h_{jk}=\frac{h_{j\bullet}h_{\bullet k}}{n}`,note:r`\(H_0\): X und Y unabhängig. Verwerfen, wenn \(Z\gt\chi^2_{1-\alpha}(df)\). Immer rechtsseitig. Voraussetzung: keine erwartete Häufigkeit zu klein.`,tr:r`Bağımsızlık testi: Tag 2'deki χ² katsayısı + serbestlik derecesi (J−1)(K−1). Her zaman sağ taraflı.`},
{t:"ex",h:"Sonntagsfrage (V12)",q:r`Geschlecht (2) × Partei (7), \(n=1000\). Z = 3.832.`,steps:[r`\(df=(2-1)(7-1)=6\).`,r`\(\chi^2_{0.95}(6)=12.59\).`,r`\(3.832\lt12.59\) → \(H_0\) nicht verwerfen.`],a:r`Kein Zusammenhang zwischen Geschlecht und Parteipräferenz nachweisbar.`},
{t:"formula",h:"χ²-Anpassungstest",tex:r`Z=\sum_{j=1}^{J}\frac{(h_j-n\pi_j)^2}{n\pi_j}\ \overset{a}{\sim}\ \chi^2(J-1)`,note:r`Werden Parameter geschätzt, verringern sich die Freiheitsgrade um deren Anzahl.`},
{t:"num",q:r`Masterarbeiten (V12): Kategorien 1/2/3 mit \(h\) = 4, 12, 18 (\(n=34\)). \(H_0:\pi_1=\pi_2=\pi_3=\frac13\). Prüfgröße, Freiheitsgrade und Entscheidung (α = 0.05, \(\chi^2_{0.95}(2)=5.99\))?`,f:[{l:"Z =",a:8.705882,tol:.002},{l:"df =",a:2,tol:0}],why:r`Erwartet je \(34/3=11.33\). \(Z=\frac{(4-11.33)^2+(12-11.33)^2+(18-11.33)^2}{11.33}=8.706\gt5.99\) → \(H_0\) verwerfen: unterschiedliche Wahrscheinlichkeiten nachweisbar.`},
{t:"r",h:"In R",code:r`
tafel <- matrix(c(140,144, 80,91, 21,19, 57,64, 43,53, 101,85, 47,55), nrow = 2)
test <- chisq.test(tafel)
test$expected; test$statistic; test$p.value
qchisq(0.95, df = 6)
chisq.test(c(4, 12, 18), p = c(1/3, 1/3, 1/3))   # Anpassungstest`,
out:r`
X-squared 3.832216
[1] 0.69937
[1] 12.59159`}
]});

L({id:"5.5",day:5,no:5,title:"Lineare Regression (Ausblick)",min:50,rel:1,
src:["V13","Tutorium 13"],
goal:"Du rechnest eine Regressionsgerade per KQ-Methode, interpretierst Koeffizienten (ceteris paribus), machst Prognosen und liest summary(lm()).",
blocks:[
{t:"idea",h:"Das Modell",de:r`<p>\(y_i=\beta_0+\beta_1x_i+\varepsilon_i\): Zielgröße = linearer Zusammenhang + Störgröße. Die <b>Methode der kleinsten Quadrate</b> (KQ) wählt \(\hat\beta_0,\hat\beta_1\) so, dass \(\sum(y_i-\beta_0-\beta_1x_i)^2\) minimal wird. Residuen: \(\hat\varepsilon_i=y_i-\hat y_i\).</p><p class="muted">Relevanz: V13 ist die Zusammenfassung mit Ausblick; Tutorium 13 übt es aber. Lerne die Formeln und die Interpretation — mehr nicht.</p>`,tr:r`En küçük kareler: hata karelerinin toplamını minimize eden doğru. Katsayı yorumu: x bir birim artarsa y ortalama β kadar değişir (diğerleri sabitken).`},
{t:"formula",h:"KQ-Schätzer",tex:r`\hat\beta_1=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}=\frac{\sum x_iy_i-n\bar x\bar y}{\sum x_i^2-n\bar x^2}\qquad \hat\beta_0=\bar y-\hat\beta_1\bar x\qquad R^2=\frac{\sum(\hat y_i-\bar y)^2}{\sum(y_i-\bar y)^2}`},
{t:"ex",h:"Handgelenk und Körperfett (Tutorium 13, Aufgabe 2)",q:r`\(x\): 18.7, 16.5, 18.8, 19.0, 18.5 · \(y\): 29.6, 25.3, 13.5, 12.9, 22.1.`,
steps:[r`\(\sum x_iy_i=1878.72\), \(\bar x=18.3\), \(\bar y=20.68\), \(\sum x_i^2=1678.63\).`,r`\(\hat\beta_1=\frac{1878.72-5\cdot18.3\cdot20.68}{1678.63-5\cdot18.3^2}=\frac{-13.5}{4.18}=-3.230\).`,r`\(\hat\beta_0=20.68+3.2297\cdot18.3=79.783\).`,r`\(\hat y=19.388, 26.493, 19.065, 18.419, 20.034\); Residuen \(10.212, -1.193, -5.565, -5.519, 2.066\); \(R^2=0.203\).`],a:r`\(\hat y=79.783-3.230x\); nur 20.3 % der Streuung erklärt. Mit ungerundeten Werten weiterrechnen!`},
{t:"num",q:r`Sparguthaben-Modell (Tutorium 13, Aufgabe 3): \(\hat y=16.592685+3.010589\cdot\text{Kredit}+5.398822\cdot\text{Einkommen}+0.763068\cdot\text{Bildung}-3.483219\cdot\text{Geschlecht}\). Prognose für eine Frau (Geschlecht = 0), Kredit 70, Einkommen 2500, Bildung 16?`,f:[{l:"ŷ =",a:13736.598,tol:.01}],why:r`\(16.592685+3.010589\cdot70+5.398822\cdot2500+0.763068\cdot16=13736.598\) Euro. Interpretation Kredit: „Steigt der Kreditscore um einen Punkt, steigt das Sparguthaben im Durchschnitt ceteris paribus um 3.011 Euro.“`},
{t:"r",h:"summary(lm()) lesen",code:r`
mod <- lm(BIP ~ Einkommen)
summary(mod)
confint(mod, level = 0.99)
2 * (1 - pt(2.204, 245))      # p-Wert zweiseitig für t = 2.204, df = 245`,
notes:[[1,"<code>lm(y ~ x)</code>: zuerst die Zielgröße.",""],[2,"<b>Estimate</b> = \\(\\hat\\beta\\); <b>Std. Error</b> = Standardfehler; <b>t value</b> = Estimate / Std. Error (Test \\(H_0:\\beta=0\\)); <b>Pr(&gt;|t|)</b> = p-Wert; df = \\(n-p-1\\); <b>R-squared</b> = erklärter Streuungsanteil.","t değeri = tahmin / standart hata; H₀: β=0 testi."],[3,"KI: \\(\\hat\\beta_1\\pm t_{1-\\alpha/2,n-2}\\cdot SE\\), z. B. \\(1.299\\pm2.977\\cdot0.1435=[0.872,1.726]\\).",""]]}
]});

L({id:"5.6",day:5,no:6,title:"Generalprobe: Klausur unter Zeitdruck",min:120,rel:3,
src:["alle Vorlesungen","neue Aufgaben im Probeklausur-Stil"],
goal:"Du schreibst eine gemischte A-Teil-Probe (58 Punkte, ca. 75 Minuten) mit neuen Zahlen, bewertest dich nach der Musterlösung und gehst die B-Teil-Checkliste durch.",
blocks:[
{t:"idea",h:"So gehst du vor",de:r`<ol><li>Stell dir einen Timer auf 75 Minuten. Papier, Kugelschreiber, Taschenrechner, dein Formelblatt.</li><li>Rechne alle Aufgaben <b>ohne</b> die Lösungen zu öffnen.</li><li>Danach jede Teilaufgabe aufdecken und dich ehrlich bewerten (voll / halb / falsch). Unten siehst du deine Punktzahl.</li><li>Alles mit „halb“ oder „falsch“: zurück in die Lektion (Nummer steht in der Aufgabe).</li></ol>`,tr:r`75 dakikalık süre tut, çözümlere bakmadan hepsini çöz, sonra dürüstçe puanla. Hatalı konulara ilgili derse geri dön.`},
{t:"exam",h:"G1 · Wartezeiten an der Mensa (→ 1.4, 1.5)",src:"neu",kind:"Generalprobe A-Teil",q:r`Wartezeiten in Minuten: 4, 7, 2, 9, 4, 12, 5, 4, 30, 3.`,
parts:[{q:r`(a) Skalenniveau und Merkmalstyp?`,p:1,s:r`Kardinal (metrisch), stetig.`},
{q:r`(b) Modus, Median, arithmetisches Mittel.`,p:3,s:r`Sortiert: 2, 3, 4, 4, 4, 5, 7, 9, 12, 30. \(x_{mod}=4\), \(x_{med}=\frac{4+5}{2}=4.5\), \(\bar x=\frac{80}{10}=8\).`},
{q:r`(c) Empirische Varianz \(S^2\) (Nenner \(n\)).`,p:2,s:r`\(\overline{x^2}=\frac{1260}{10}=126\), \(S^2=126-64=62\).`},
{q:r`(d) Quartile, IQR und Ausreißer nach der 1.5·IQR-Regel. Wie ist die Verteilung geformt?`,p:4,s:r`\(10\cdot0.25=2.5\) → Platz 3 → \(x_{0.25}=4\); \(10\cdot0.75=7.5\) → Platz 8 → \(x_{0.75}=9\). \(IQR=5\). Obere Grenze \(9+7.5=16.5\) → <b>30 ist Ausreißer</b>, Whisker bei 12. Untere Grenze \(-3.5\) → Whisker bei 2. \(\bar x\gt x_{med}\gt x_{mod}\) → rechtsschief / linkssteil.`}]},
{t:"exam",h:"G2 · Retouren im Online-Shop (→ 2.4, 2.5, 3.4)",src:"neu",kind:"Generalprobe A-Teil",q:r`Bestellungen: 50 % App, 30 % Webseite, 20 % Telefon. Retourenquote: App 10 %, Webseite 20 %, Telefon 5 %.`,
parts:[{q:r`(a) \(P(\text{Retoure})\).`,p:2,s:r`\(0.1\cdot0.5+0.2\cdot0.3+0.05\cdot0.2=0.05+0.06+0.01=0.12\).`},
{q:r`(b) Eine Bestellung wird retourniert. Mit welcher Wahrscheinlichkeit kam sie über die App?`,p:2,s:r`\(P(\text{App}\mid R)=\frac{0.05}{0.12}=0.417\).`},
{q:r`(c) Sind „App“ und „Retoure“ unabhängig? Begründen Sie mit Zahlen.`,p:2,s:r`Nein: \(P(R\mid\text{App})=0.1\ne0.12=P(R)\) (gleichwertig: \(P(R\cap\text{App})=0.05\ne0.5\cdot0.12=0.06\)).`},
{q:r`(d) 8 unabhängige Bestellungen. Wahrscheinlichkeit für mindestens 2 Retouren?`,p:3,s:r`\(X\sim B(8,0.12)\). \(P(X\ge2)=1-P(0)-P(1)=1-0.88^8-8\cdot0.12\cdot0.88^7=1-0.3596-0.3923=0.248\).`}]},
{t:"exam",h:"G3 · Stetige Zufallsvariable (→ 3.1, 3.2)",src:"neu",kind:"Generalprobe A-Teil",q:r`\(f(x)=c\,x^2\) für \(0\le x\le3\), sonst 0.`,
parts:[{q:r`(a) Bestimmen Sie \(c\).`,p:2,s:r`\(\int_0^3cx^2dx=c\cdot9=1\Rightarrow c=\frac19\).`},
{q:r`(b) \(E(X)\) und \(Var(X)\).`,p:4,s:r`\(E(X)=\int_0^3\frac{x^3}{9}dx=\frac{81}{36}=2.25\). \(E(X^2)=\int_0^3\frac{x^4}{9}dx=\frac{243}{45}=5.4\). \(Var=5.4-2.25^2=0.338\) (genau 0.3375).`},
{q:r`(c) Verteilungsfunktion (vollständig), \(P(X\gt2)\) und der Median.`,p:4,s:r`\(F(x)=0\) für \(x\lt0\); \(\frac{x^3}{27}\) für \(0\le x\le3\); 1 für \(x\gt3\). \(P(X\gt2)=1-\frac{8}{27}=0.704\). Median: \(\frac{x^3}{27}=0.5\Rightarrow x=\sqrt[3]{13.5}=2.381\).`}]},
{t:"exam",h:"G4 · Maximum-Likelihood (→ 4.3, 4.4)",src:"neu, etwas schwerer",kind:"Generalprobe A-Teil",q:r`\(f(x;\theta)=\frac{x}{\theta^2}e^{-x/\theta}\) für \(x\gt0\), \(\theta\gt0\). \(X_1,\dots,X_n\) iid. Bekannt: \(E(X)=2\theta\), \(Var(X)=2\theta^2\).`,
parts:[{q:r`(a) Vereinfachte Log-Likelihood.`,p:3,s:r`\(L=\prod x_i\cdot\theta^{-2n}e^{-\sum x_i/\theta}\). \(\ell(\theta)=\sum\log x_i-2n\log\theta-\frac1\theta\sum x_i\).`},
{q:r`(b) ML-Schätzer mit Lösungsweg; Wert für die Stichprobe 1.2, 3.0, 2.4, 1.8.`,p:4,s:r`\(\ell'=-\frac{2n}\theta+\frac{\sum x_i}{\theta^2}\overset!=0\Rightarrow\hat\theta=\frac{\sum x_i}{2n}=\frac{\bar x}{2}\). Stichprobe: \(\bar x=2.1\Rightarrow\hat\theta=1.05\).`},
{q:r`(c) Ist \(\hat\theta\) erwartungstreu? Bestimmen Sie \(Var(\hat\theta)\). Konsistent?`,p:3,s:r`\(E(\hat\theta)=\frac12E(\bar X)=\frac12\cdot2\theta=\theta\) → unverzerrt. \(Var(\hat\theta)=\frac14\cdot\frac{2\theta^2}{n}=\frac{\theta^2}{2n}\to0\) → MSE → 0 → konsistent.`}]},
{t:"exam",h:"G5 · Konfidenzintervalle (→ 4.6)",src:"neu",kind:"Generalprobe A-Teil",q:r`Füllmengen von \(n=16\) Packungen, normalverteilt: \(\bar x=498.2\) g, \(s_*=4.4\) g. Außerdem: 18 von 150 Packungen waren unterfüllt.`,
parts:[{q:r`(a) 95 %-KI für \(\mu\) (\(t_{15,0.975}=2.131\)).`,p:3,s:r`σ unbekannt → \(t\). \(498.2\pm2.131\cdot\frac{4.4}{4}=498.2\pm2.344\) → [495.856, 500.544].`},
{q:r`(b) 95 %-KI für den Anteil unterfüllter Packungen.`,p:3,s:r`\(\hat\pi=0.12\), \(\sqrt{\frac{0.12\cdot0.88}{150}}=0.0265\), \(1.96\cdot0.0265=0.052\) → [0.068, 0.172].`},
{q:r`(c) Wie ändert sich die Breite aus (a), wenn man 99 % statt 95 % wählt? Begründen.`,p:1,s:r`Breiter, weil das Quantil \(t_{15,0.995}\) größer ist als \(t_{15,0.975}\).`}]},
{t:"exam",h:"G6 · Hypothesentest (→ 5.1, 5.2)",src:"neu",kind:"Generalprobe A-Teil",q:r`Ein Hersteller behauptet, die mittlere Akkulaufzeit sei mindestens 20 h. Eine Verbraucherorganisation will das Gegenteil absichern. \(\sigma=3\) h bekannt, \(n=36\), \(\bar x=19.1\) h, Normalverteilung.`,
parts:[{q:r`(a) Hypothesenpaar.`,p:2,s:r`\(H_0:\mu\ge20\) vs. \(H_1:\mu\lt20\).`},
{q:r`(b) Prüfgröße mit Verteilung unter \(H_0\).`,p:3,s:r`\(Z=\frac{19.1-20}{3}\sqrt{36}=-1.8\sim N(0,1)\).`},
{q:r`(c) Ablehnbereich für α = 0.05, p-Wert und Entscheidung (Begründung).`,p:4,s:r`\(A=(-\infty;-1.645]\). \(-1.8\in A\). \(p=\Phi(-1.8)=0.036\lt0.05\) → \(H_0\) verwerfen: Die Laufzeit liegt im Mittel signifikant unter 20 h.`},
{q:r`(d) Entscheidung bei α = 0.01?`,p:1,s:r`\(p=0.036\gt0.01\) (bzw. \(-1.8\gt-2.326\)) → nicht verwerfen.`}]},
{t:"exam",h:"G7 · χ²-Unabhängigkeit (→ 2.1, 5.4)",src:"neu",kind:"Generalprobe A-Teil",q:r`100 Studierende: Sport ja/nein × Lerngruppe ja/nein mit Häufigkeiten 30, 20 (Sport ja) und 20, 30 (Sport nein).`,
parts:[{q:r`(a) Erwartete Häufigkeiten unter Unabhängigkeit und Teststatistik.`,p:3,s:r`Alle Randsummen 50 → \(\tilde h=\frac{50\cdot50}{100}=25\) in jeder Zelle. \(Z=4\cdot\frac{(5)^2}{25}=4\).`},
{q:r`(b) Freiheitsgrade und Entscheidung (α = 0.05, \(\chi^2_{0.95}(1)=3.84\)).`,p:2,s:r`\(df=(2-1)(2-1)=1\). \(4\gt3.84\) → \(H_0\) (Unabhängigkeit) verwerfen.`}]},
{t:"idea",h:"B-Teil-Checkliste (60 Minuten, 45 Punkte)",de:r`
<ol>
<li><code>setwd(path.expand("~"))</code> — Datei im Ordner Dokumente.</li>
<li>Datei in einem Editor anschauen: Trennzeichen? <code>sep = ","</code> oder <code>";"</code>, Dezimal <code>dec = "."</code> oder <code>","</code>. Einlesen mit <code>read.csv</code>, dann <code>head(d)</code>, <code>str(d)</code>.</li>
<li>Typen: <code>typeof()</code> / <code>class()</code> → Antwortsatz.</li>
<li>Kennzahlen: <code>mean, median, var, sd, range, quantile, IQR, summary</code> — immer <code>round(…, 3)</code> (oder wie verlangt).</li>
<li>Grafik: <code>pdf("Name.pdf")</code> → <code>hist(…, freq = FALSE, breaks, right, main, xlab, ylab)</code> / <code>plot(density(…))</code> / <code>plot(x, y)</code> → <code>dev.off()</code>.</li>
<li>Likelihood: <code>dpois/dbinom/dnorm/dexp/dgamma</code>, <code>prod</code> vs. <code>sum(log(…))</code>, eigene <code>function</code>, <code>for</code>-Schleife über ein Raster.</li>
<li>Numerisch: <code>optimize(…, maximum = TRUE)</code> oder <code>nlm(neglogL, start, x)</code> mit <code>exp()</code>-Transformation; Rücktransformation!</li>
<li>Wahrscheinlichkeiten/Quantile aus dem Modell: <code>p…()</code> und <code>q…()</code>.</li>
<li>Tests/KI: <code>t.test(x, mu, alternative, conf.level)</code>, <code>binom.test</code>, <code>chisq.test</code>, <code>qt, qnorm, qchisq, pt, pnorm, pchisq</code>.</li>
<li>Jede Teilaufgabe: Code + Output in Kästchen 1, voller Antwortsatz in Kästchen 2. Fehlerhaften Code löschen.</li></ol>`,tr:r`B bölümü kontrol listesi: çalışma klasörü, doğru sep/dec ile okuma, tip, yuvarlanmış istatistikler, PDF grafik (dev.off!), likelihood fonksiyonu, optimize/nlm, p/q fonksiyonları, testler. Her alt soruda kod + tam cümle.`},
{t:"exam",h:"B-Teil-Probe · Mensa-Daten (Code auf Papier schreiben)",src:"neu",kind:"Generalprobe B-Teil",q:r`Datei <code>Mensa.csv</code> (Semikolon als Trennzeichen, Komma als Dezimalzeichen) mit den Variablen <code>Standort</code> (Text), <code>Wartezeit</code> (Minuten, Kommazahl) und <code>Gerichte</code> (Anzahl verkaufter Gerichte pro Stunde).`,
parts:[{q:r`(a) Einlesen als <code>d</code>, erste 6 Zeilen.`,p:3,s:r`<code>setwd(path.expand("~"))</code><br><code>d &lt;- read.csv("Mensa.csv", sep = ";", dec = ",", header = TRUE)</code><br><code>head(d)</code>`},
{q:r`(b) Median und unverzerrte Varianz der Wartezeit, 3 Nachkommastellen, mit Antwortsatz.`,p:3,s:r`<code>round(median(d$Wartezeit), 3)</code>; <code>round(var(d$Wartezeit), 3)</code> + „Der Median der Wartezeit beträgt … Minuten, die unverzerrte Varianz …“.`},
{q:r`(c) Normiertes Histogramm der Wartezeit mit Klassen (0,5], (5,10], (10,30], beschriftet, als <code>Wartezeit.pdf</code>.`,p:6,s:r`<code>pdf("Wartezeit.pdf")</code><br><code>hist(d$Wartezeit, freq = FALSE, breaks = c(0, 5, 10, 30), right = TRUE, main = "Sitz …, Matr.Nr …, Aufgabenteil c)", xlab = "Wartezeit (Minuten)", ylab = "Dichte")</code><br><code>dev.off()</code>`},
{q:r`(d) Nehmen Sie <code>Gerichte</code> ~ Po(λ) an. Schreiben Sie <code>logL.pois(lambda, x)</code> (Log-Likelihood) und bestimmen Sie den ML-Schätzer numerisch im Intervall (0, 200).`,p:6,s:r`<code>logL.pois &lt;- function(lambda, x) { l &lt;- sum(log(dpois(x, lambda))); return(l) }</code><br><code>opt &lt;- optimize(logL.pois, c(0, 200), x = d$Gerichte, maximum = TRUE)</code><br><code>round(opt$maximum, 3)</code> — Kontrolle: muss ≈ <code>mean(d$Gerichte)</code> sein, denn \(\hat\lambda=\bar x\).`},
{q:r`(e) Mit dem geschätzten λ: Wahrscheinlichkeit für mehr als 60 Gerichte in einer Stunde.`,p:2,s:r`<code>1 - ppois(60, opt$maximum)</code> — „mehr als 60“ = \(1-P(X\le60)\).`},
{q:r`(f) Testen Sie zum Niveau 5 %, ob die mittlere Wartezeit größer als 8 Minuten ist. Entscheidung im Satz.`,p:4,s:r`<code>t.test(d$Wartezeit, mu = 8, alternative = "greater")</code>. \(H_0:\mu\le8\) vs. \(H_1:\mu\gt8\). „Da der p-Wert … kleiner/größer als 0.05 ist, wird \(H_0\) verworfen / nicht verworfen.“`}]},
{t:"rule",k:"Letzter Tipp",de:r`Am Ende jeder Aufgabe: <b>Buchstaben abhaken</b> (a, b, c …), <b>Rundung prüfen</b> (3 Nachkommastellen), <b>Begründung mit Zahl oder Regel</b>. So holst du die Punkte, die du schon verdient hast.`,tr:r`Her sorunun sonunda: tüm alt şıklar yapıldı mı, yuvarlama doğru mu, gerekçe sayı veya kural içeriyor mu? Kontrol et.`}
]});
