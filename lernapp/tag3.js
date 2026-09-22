/* ================= TAG 3 · Zufallsvariablen & Verteilungen ================= */

L({id:"3.1",day:3,no:1,title:"Zufallsvariable, Dichte & Verteilungsfunktion",min:65,rel:3,
src:["V05","Tutorium 5, 6","Testat 4"],
goal:r`Du unterscheidest Wahrscheinlichkeitsfunktion (diskret) und Dichte (stetig), bestimmst Normierungskonstanten, leitest \(F(x)\) her und rechnest damit Wahrscheinlichkeiten.`,
blocks:[
{t:"idea",h:"Vom Merkmal zur Zufallsvariable",de:r`
<p>Eine <b>Zufallsvariable</b> \(X\) ordnet jedem Ergebnis eines Zufallsexperiments eine Zahl zu (z. B. Summe zweier Würfel). Sie ist das theoretische Gegenstück zum Merkmal:</p>
<div class="tbl"><table><tr><th class="l">Deskriptive Statistik (Daten)</th><th class="l">Wahrscheinlichkeitsrechnung (Modell)</th></tr><tr><td class="l">Merkmal</td><td class="l">Zufallsvariable</td></tr><tr><td class="l">Ausprägungen</td><td class="l">Träger \(T\) (mögliche Werte)</td></tr><tr><td class="l">relative Häufigkeiten</td><td class="l">Wahrscheinlichkeiten</td></tr><tr><td class="l">\(\bar x\), \(S^2\)</td><td class="l">\(E(X)\), \(Var(X)\)</td></tr></table></div>`,
tr:r`Rastgele değişken, bir deneyin sonucunu sayıya çevirir. Veri tarafındaki „Merkmal“ın teorik karşılığıdır.`},
{t:"formula",h:"Diskret: Wahrscheinlichkeitsfunktion",tex:r`P(X=x_i)=p_i,\quad 0\le p_i\le1,\quad \sum_i p_i=1,\qquad P(a\le X\le b)=\sum_{a\le x_i\le b}p_i`},
{t:"formula",h:"Stetig: Dichte",tex:r`f(x)\ge0,\quad \int_{-\infty}^{\infty}f(x)\,dx=1,\qquad P(a\le X\le b)=\int_a^b f(x)\,dx,\qquad P(X=x)=0`,note:r`Bei stetigen \(X\) ist es egal, ob \(\lt\) oder \(\le\). \(f(x)\gt1\) ist erlaubt! Eine Dichte ist <b>keine</b> Wahrscheinlichkeit.`,tr:r`Sürekli değişkende tek bir noktanın olasılığı 0'dır; olasılık = yoğunluğun altındaki alan. f(x) 1'den büyük olabilir.`},
{t:"formula",h:"Verteilungsfunktion (für beide Fälle)",tex:r`F(x)=P(X\le x),\qquad P(a\lt X\le b)=F(b)-F(a),\qquad P(X\gt a)=1-F(a),\qquad F(x)=\int_{-\infty}^{x}f(t)\,dt`,note:r`Beim Herleiten von \(F\): Integrationsvariable umbenennen (\(t\)), \(x\) ist die obere Grenze. Und \(F\) für alle drei Bereiche angeben (0 / Formel / 1).`},
{t:"mc",q:r`Welche Eigenschaften muss eine gültige Dichte erfüllen? (Testat 4, Aufgabe 4)`,o:[r`\(\int_{-\infty}^{\infty}f(x)\,dx=1\)`,r`\(f(x)\ge0\) für alle \(x\)`,r`\(f(x)\le1\) für alle \(x\)`,r`\(P(X=x)=f(x)\)`,r`\(f\) ist stetig und monoton`],k:[0,1],why:r`Nur Normierung und Nicht-Negativität. Eine Dichte darf größer als 1 sein, \(P(X=x)=0\), und sie muss weder stetig noch monoton sein.`},
{t:"ex",h:"Konstante c finden (Tutorium 6, Aufgabe 1)",q:r`\(P(X=x)=\frac xc\) für \(x\in\{1,2,3,4\}\), sonst 0.`,steps:[r`Summe muss 1 sein: \(\frac1c+\frac2c+\frac3c+\frac4c=\frac{10}{c}=1\).`,r`Also \(c=10\).`],a:r`\(c=10\)`},
{t:"num",q:r`Testat 4, Aufgabe 5: \(f(x)=c(x-2)\) für \(2\le x\le3\), sonst 0. Bestimme \(c\), \(E(X)\) und \(E(X^2)\).`,f:[{l:"c =",a:2},{l:"E(X) =",a:8/3},{l:"E(X²) =",a:43/6}],why:r`\(\int_2^3 c(x-2)dx=c\big[\tfrac{(x-2)^2}{2}\big]_2^3=\tfrac c2=1\Rightarrow c=2\).<br>\(E(X)=\int_2^3 x\cdot2(x-2)dx=2\big[\tfrac{x^3}{3}-x^2\big]_2^3=2\big(0-(-\tfrac43)\big)=\tfrac83=2.667\).<br>\(E(X^2)=\int_2^3 2x^2(x-2)dx=2\big[\tfrac{x^4}{4}-\tfrac{2x^3}{3}\big]_2^3=2\big(2.25+\tfrac43\big)=\tfrac{43}{6}=7.167\).`},
{t:"ex",h:"Verteilungsfunktion herleiten (Tutorium 6, Aufgabe 2)",q:r`\(f(x)=\frac12(x-4)\) für \(4\le x\le6\), sonst 0.`,
steps:[r`Dichte prüfen: \(f\ge0\) auf [4,6] und \(\int_4^6\frac12(x-4)dx=\big[\tfrac14x^2-2x\big]_4^6=(9-12)-(4-8)=1\). ✓`,
r`Für \(4\le x\le6\): \(F(x)=\int_4^x\frac12(t-4)\,dt=\big[\tfrac14t^2-2t\big]_4^x=\tfrac14x^2-2x+4\).`,
r`Komplett: \(F(x)=0\) für \(x\lt4\); \(\tfrac14x^2-2x+4\) für \(4\le x\le6\); \(1\) für \(x\gt6\).`,
r`\(P(X\gt5.2)=1-F(5.2)=1-0.36=0.64\). \(P(4.5\lt X\lt5.5)=F(5.5)-F(4.5)=0.5625-0.0625=0.5\).`],a:r`\(E(X)=\tfrac{16}{3}=5.333\), \(Var(X)=\tfrac29=0.222\)`},
{t:"num",q:r`Mit \(F(x)=\frac14x^2-2x+4\) von oben: \(P(X\lt5.1)\)?`,f:[{l:"P(X<5.1) =",a:.3025,tol:.0006}],why:r`\(F(5.1)=6.5025-10.2+4=0.3025\approx0.303\) (stetig: \(\lt\) und \(\le\) gleich).`},
{t:"idea",h:"Quantile einer Zufallsvariable",de:r`
<p>Das \(\alpha\)-Quantil \(q_\alpha\) löst bei stetigen \(X\) die Gleichung \(F(q_\alpha)=\alpha\). Beispiel Anrufdauer (V05): \(F(x)=1-e^{-0.006x}\). \(95\,\%\)-Quantil: \(1-e^{-0.006q}=0.95\iff q=\frac{-\log 0.05}{0.006}=499.3\) Sekunden — nur 5 % der Anrufe dauern länger.</p>
<p>In R: <code>q…()</code> ist die Umkehrfunktion von <code>p…()</code>: <code>qnorm(pnorm(0.3))</code> gibt 0.3 zurück.</p>`,tr:r`Quantil: F(q)=α denklemini çöz. R'da q-fonksiyonu p-fonksiyonunun tersidir.`},
{t:"idea",h:"Unabhängige und identisch verteilte Zufallsvariablen (iid)",de:r`
<p>\(X_1,\dots,X_n\) sind <b>iid</b>, wenn sie stochastisch unabhängig sind <b>und</b> dieselbe Verteilung haben. Das entsteht bei unabhängiger Wiederholung eines Experiments oder beim Ziehen mit Zurücklegen. <span class="hl">iid ist die Grundannahme für alle Schätzer an Tag 4.</span></p>`,tr:r`iid: bağımsız ve aynı dağılımlı. 4. gündeki tüm tahminlerin temel varsayımı.`},
{t:"trap",items:[r`Dichtewerte als Wahrscheinlichkeiten aufsummiert (z. B. <code>sum(dexp(1:6, 1/3))</code> für \(P(1\lt Y\lt6)\) — falsch! Richtig: <code>pexp(6,1/3) - pexp(1,1/3)</code>).`,r`Bei diskreten \(X\): \(P(X\lt4)=P(X\le3)\) — nicht \(F(4)\).`,r`\(F(x)\) nur für den mittleren Bereich angegeben.`]}
]});

L({id:"3.2",day:3,no:2,title:"Erwartungswert & Varianz",min:60,rel:3,
src:["V06","Tutorium 6","Testat 4"],
goal:r`Du berechnest \(E(X)\) und \(Var(X)\) (diskret und stetig) und wendest die Rechenregeln für lineare Transformationen und Summen sicher an — die Basis für Bias und MSE an Tag 4.`,
blocks:[
{t:"formula",h:"Erwartungswert",tex:r`E(X)=\sum_x x\,P(X=x)\ \ \text{(diskret)}\qquad E(X)=\int x\,f(x)\,dx\ \ \text{(stetig)}\qquad E(g(X))=\sum g(x)P(X=x)\ \text{bzw.}\int g(x)f(x)dx`,note:r`\(E(X)\) ist der Schwerpunkt der Verteilung. Gesetz der großen Zahlen: \(\bar X\to E(X)\) für \(n\to\infty\). Achtung: meist \(E(g(X))\ne g(E(X))\).`,tr:r`Beklenen değer: ağırlık merkezi. Çok tekrar edilirse ortalama beklenen değere yaklaşır.`},
{t:"formula",h:"Varianz",tex:r`Var(X)=E\big[(X-E(X))^2\big]=E(X^2)-\big(E(X)\big)^2,\qquad sd(X)=\sqrt{Var(X)}`,note:r`Verschiebungssatz — fast immer der schnellere Weg.`},
{t:"formula",h:"Rechenregeln (auswendig!)",tex:r`E(aX+b)=aE(X)+b\qquad Var(aX+b)=a^2Var(X)\qquad E\Big(\sum a_iX_i\Big)=\sum a_iE(X_i)\qquad Var\Big(\sum a_iX_i\Big)\overset{\text{unabh.}}{=}\sum a_i^2Var(X_i)`,
parts:[[r`E(XY)=E(X)E(Y)`,"nur bei Unabhängigkeit"],[r`Var(X+Y)=Var X+Var Y+2Cov(X,Y)`,"allgemein"],[r`Var\big(\tfrac1n\sum X_i\big)=\tfrac{\sigma^2}{n}`,"für iid mit \\(Var(X_i)=\\sigma^2\\)"]],
tr:r`Sabit çarpan varyanstan KARESİ ile çıkar; sabit toplam varyansı değiştirmez. Toplamın varyansı = varyansların toplamı (sadece bağımsızsa).`},
{t:"num",q:r`Tutorium 6, Aufgabe 1: \(P(X=x)=x/10\), \(x\in\{1,2,3,4\}\). Berechne \(E(X)\) und \(Var(X)\). Weiter: \(Z=0.5X+Y\), \(X,Y\) unabhängig, \(E(Z)=8.5\), \(Var(Y)=1\). Berechne \(E(Y)\) und \(Var(Z)\).`,
f:[{l:"E(X) =",a:3},{l:"Var(X) =",a:1},{l:"E(Y) =",a:7},{l:"Var(Z) =",a:1.25}],why:r`\(E(X)=\frac{1+4+9+16}{10}=3\), \(E(X^2)=\frac{1+8+27+64}{10}=10\), \(Var(X)=10-9=1\).<br>\(8.5=0.5\cdot3+E(Y)\Rightarrow E(Y)=7\). \(Var(Z)=0.5^2\cdot1+1=1.25\) (Unabhängigkeit → keine Kovarianz).`},
{t:"num",q:r`Testat 4, Aufgabe 6: \(f(y)=\frac y6\) für \(0\le y\le2\), \(f(y)=\frac{6-y}{12}\) für \(2\lt y\le6\), sonst 0. Bestimme \(E(Y)\).`,f:[{l:"E(Y) =",a:8/3}],why:r`\(\int_0^2\frac{y^2}{6}dy=\frac{8}{18}=0.4444\). \(\int_2^6\frac{y(6-y)}{12}dy=\frac1{12}\big[3y^2-\tfrac{y^3}{3}\big]_2^6=\frac1{12}(36-9.3333)=2.2222\). Summe \(=\frac83=2.667\). Stückweise Dichte → Integral in Stücke teilen.`},
{t:"ex",h:"Gleicher Erwartungswert, anderes Risiko (Chuck-a-Luck, V06)",q:r`Drei Würfel, Einsatz 1 € auf die 6. Gewinn \(G\): 3 (1/216), 2 (15/216), 1 (75/216), −1 (125/216).`,
steps:[r`\(E(G)=\frac{3+30+75-125}{216}=-\frac{17}{216}=-0.0787\) — im Mittel 7.9 % Verlust.`,r`\(Var(G)=\sum(g-E G)^2P(G=g)=1.2392\).`,r`Strategie „doppelter Einsatz“: \(Var(2X_6)=4\cdot1.2392=4.9567\). Strategie „zweimal spielen“ (unabhängig): \(Var(X_6+Y_6)=2\cdot1.2392=2.4784\).`,r`Alle drei Strategien haben \(E=-\frac{34}{216}\), aber sehr verschiedene Varianz.`],a:r`Der Faktor \(a\) geht als \(a^2\) in die Varianz — deshalb ist „alles auf einmal“ am riskantesten.`},
{t:"mc",q:r`\(X\sim Po(2)\), \(V=2X+1\). Welche Aussage stimmt? (Tutorium 7, Aufgabe 2)`,o:[r`\(E(V)=5\), \(Var(V)=8\), \(V\) ist nicht poissonverteilt`,r`\(E(V)=5\), \(Var(V)=5\), \(V\) ist poissonverteilt`,r`\(E(V)=4\), \(Var(V)=4\)`],k:0,why:r`\(E=2\cdot2+1=5\), \(Var=2^2\cdot2=8\). Bei Poisson gilt immer \(E=Var\) — hier nicht, also keine Poissonverteilung.`},
{t:"trap",items:[r`\(Var(aX)=a\,Var(X)\) geschrieben — richtig ist \(a^2\).`,r`\(Var(X-Y)=Var X-Var Y\) — falsch! Bei Unabhängigkeit \(Var X+Var Y\).`,r`\(E(X^2)\) mit \((E X)^2\) verwechselt.`]}
]});

L({id:"3.3",day:3,no:3,title:"Gemeinsame Verteilungen & Unabhängigkeit",min:50,rel:2,
src:["V06","Tutorium 5, 6"],
goal:"Du bestimmst aus einer gemeinsamen Verteilung Randverteilungen, bedingte Verteilungen, Kovarianz und prüfst Unabhängigkeit — diskret per Tabelle, stetig per Integral.",
blocks:[
{t:"formula",h:"Diskret",tex:r`P(X=x)=\sum_y P(X=x,Y=y)\qquad P(X=x\mid Y=y)=\frac{P(X=x,Y=y)}{P(Y=y)}`,note:r`Unabhängig ⇔ \(P(X=x,Y=y)=P(X=x)P(Y=y)\) für <b>alle</b> Paare.`},
{t:"num",q:r`Gehalt \(X\) (1: &lt;2500 €, 2: 2500–4000 €, 3: &gt;4000 €) und Alter \(Y\) (1–4). Gemeinsame Wahrscheinlichkeiten (Tutorium 5, Aufgabe 1):
<div class="tbl"><table><tr><th>X \ Y</th><th>1</th><th>2</th><th>3</th><th>4</th></tr><tr><th>1</th><td>0.13</td><td>0.08</td><td>0.05</td><td>0.03</td></tr><tr><th>2</th><td>0.07</td><td>0.21</td><td>0.07</td><td>0.09</td></tr><tr><th>3</th><td>0.00</td><td>0.05</td><td>0.10</td><td>0.12</td></tr></table></div>
Bestimme \(P(X=1)\), \(P(Y=2)\), \(P(X=2\mid Y=1)\), \(P(Y=2\mid X=3)\).`,
f:[{l:"P(X=1) =",a:.29},{l:"P(Y=2) =",a:.34},{l:"P(X=2 | Y=1) =",a:.35},{l:"P(Y=2 | X=3) =",a:.05/.27}],why:r`Zeilensumme 1: 0.29. Spaltensumme 2: 0.34. \(P(X=2\mid Y=1)=\frac{0.07}{0.20}=0.35\). \(P(Y=2\mid X=3)=\frac{0.05}{0.27}=0.185\).`},
{t:"formula",h:"Stetig",tex:r`f_X(x)=\int f(x,y)\,dy\qquad f_{X|Y}(x\mid y)=\frac{f(x,y)}{f_Y(y)}\qquad X,Y\ \text{unabh.}\iff f(x,y)=f_X(x)\,f_Y(y)`,note:r`Randdichte von \(x\): nach \(y\) integrieren (und umgekehrt).`},
{t:"ex",h:"Faktorisierende Dichte (Tutorium 6, Aufgabe 3)",q:r`\(f(x,y)=12x^3(1-y)^2\) für \(0\le x,y\le1\).`,
steps:[r`\(f_X(x)=\int_0^1 12x^3(1-y)^2dy=12x^3\big[-\tfrac{(1-y)^3}{3}\big]_0^1=4x^3\).`,r`\(f_Y(y)=\int_0^1 12x^3(1-y)^2dx=3(1-y)^2\).`,r`\(f_X\cdot f_Y=12x^3(1-y)^2=f(x,y)\) → unabhängig → \(\rho=0\).`,r`\(E(X)=\int_0^1 x\cdot4x^3dx=\tfrac45\). \(P(X\lt\tfrac12,Y\lt\tfrac14)=\big(\tfrac12\big)^4\cdot\big(1-\tfrac{27}{64}\big)=0.036\).`],a:r`unabhängig, \(E(X)=0.8\)`},
{t:"formula",h:"Kovarianz & Korrelation von Zufallsvariablen",tex:r`Cov(X,Y)=E(XY)-E(X)E(Y)\qquad \rho(X,Y)=\frac{Cov(X,Y)}{sd(X)\,sd(Y)}`,note:r`Unabhängig ⇒ unkorreliert. Umgekehrt <b>nicht</b> (Ausnahme: gemeinsame Normalverteilung).`},
{t:"num",q:r`Zwei Maschinen, Ausfälle pro Tag (Tutorium 3, Aufgabe 5), relative Häufigkeiten:
<div class="tbl"><table><tr><th>X \ Y</th><th>0</th><th>1</th><th>2</th><th>Σ</th></tr><tr><th>0</th><td>0.30</td><td>0.14</td><td>0.02</td><td>0.46</td></tr><tr><th>1</th><td>0.18</td><td>0.10</td><td>0.02</td><td>0.30</td></tr><tr><th>2</th><td>0.12</td><td>0.06</td><td>0.06</td><td>0.24</td></tr><tr><th>Σ</th><td>0.60</td><td>0.30</td><td>0.10</td><td>1</td></tr></table></div>
Berechne \(\bar X\), \(\bar Y\) und die Kovarianz.`,f:[{l:"X̄ =",a:.78},{l:"Ȳ =",a:.5},{l:"Cov =",a:.11}],why:r`\(\bar X=0.30+2\cdot0.24=0.78\), \(\bar Y=0.30+2\cdot0.10=0.5\). \(\overline{XY}=1\cdot1\cdot0.10+1\cdot2\cdot0.02+2\cdot1\cdot0.06+2\cdot2\cdot0.06=0.50\). \(Cov=0.50-0.78\cdot0.5=0.11\). Mit \(s_X=0.807\), \(s_Y=0.671\): \(\rho=0.203\) (schwach positiv).`}
]});

L({id:"3.4",day:3,no:4,title:"Bernoulli, Binomial & Poisson",min:65,rel:3,
src:["V07","Tutorium 7","Testat 4","R-Skript 07"],
goal:"Du erkennst am Text, welches diskrete Modell passt, rechnest Wahrscheinlichkeiten per Hand und mit d/p-Befehlen in R — ohne ≤/&lt;-Fehler.",
blocks:[
{t:"terms",h:"Welches Modell?",items:[
["Bernoulli \\(Be(\\pi)\\)","Bernoulli","Ein Versuch, zwei Ausgänge: 1 (Erfolg, W. \\(\\pi\\)) oder 0."],
["Binomial \\(B(n,\\pi)\\)","binom","Anzahl Erfolge in \\(n\\) <b>unabhängigen</b> Bernoulli-Versuchen (Ziehen <b>mit</b> Zurücklegen)."],
["Poisson \\(Po(\\lambda)\\)","Poisson","Anzahl von Ereignissen in einem Zeitraum/Gebiet, ohne feste Obergrenze (Tore pro Spiel, Schadensmeldungen pro Jahr)."]]},
{t:"formula",h:"Bernoulli & Binomial",tex:r`P(X=x)=\binom nx\pi^x(1-\pi)^{n-x},\ x=0,\dots,n\qquad E(X)=n\pi\qquad Var(X)=n\pi(1-\pi)`,parts:[[r`\binom nx=\frac{n!}{x!(n-x)!}`,"Anzahl Möglichkeiten, x Erfolge auf n Plätze zu verteilen"],[r`n=1`,"Bernoulli: \\(E=\\pi\\), \\(Var=\\pi(1-\\pi)\\)"]],tr:r`Binom: n bağımsız denemede başarı sayısı. E=nπ, Var=nπ(1−π).`},
{t:"formula",h:"Poisson",tex:r`P(X=x)=\frac{\lambda^x}{x!}e^{-\lambda},\ x=0,1,2,\dots\qquad E(X)=Var(X)=\lambda`},
{t:"fig",kind:"bars",h:"B(10, 0.25) — P(Y ≤ 2) in Rot",x:[-.5,10.5],y:[0,.3],xt:[0,1,2,3,4,5,6,7,8,9,10],xl:"y",pts:[[0,.0563],[1,.1877],[2,.2816],[3,.2503],[4,.146],[5,.0584],[6,.0162],[7,.0031],[8,.0004],[9,0],[10,0]],hi:[0,1,2],cap:"Summe der roten Stäbe = pbinom(2, 10, 0.25) = 0.526."},
{t:"ex",h:"Würfelsumme durch 4 teilbar (Tutorium 7, Aufgabe 1)",q:r`Zwei Würfel; \(X=1\), wenn die Summe durch 4 teilbar ist. Es wird 10-mal geworfen, \(Y\) = Anzahl solcher Würfe.`,
steps:[r`Summen 4, 8, 12: (1,3),(2,2),(3,1) · (2,6),(3,5),(4,4),(5,3),(6,2) · (6,6) → 9 von 36 → \(\pi=0.25\). Also \(X\sim Be(0.25)\).`,r`\(Y\sim B(10,\,0.25)\): \(E(Y)=2.5\), \(Var(Y)=10\cdot0.25\cdot0.75=1.875\).`,r`\(P(Y=1)=\binom{10}{1}0.25^1\,0.75^9=0.188\); \(P(Y=2)=\binom{10}{2}0.25^2\,0.75^8=0.282\).`,r`\(P(Y\le2)=P(0)+P(1)+P(2)=0.056+0.188+0.282=0.526\).`]},
{t:"num",q:r`Gleiche Situation, jetzt mit R-Denken: \(P(Y\lt4)\), \(P(Y\gt5)\), \(P(2\lt Y\lt6)\).`,f:[{l:"P(Y<4) =",a:.775875},{l:"P(Y>5) =",a:.019728},{l:"P(2&lt;Y&lt;6) =",a:.454679}],why:r`<code>pbinom(3,10,0.25)</code> = 0.776 (denn \(Y\lt4\iff Y\le3\)). <code>1-pbinom(5,10,0.25)</code> = 0.020. <code>pbinom(5,10,0.25)-pbinom(2,10,0.25)</code> = 0.455 (\(3\le Y\le5\)).`},
{t:"rule",k:"Übersetzungstabelle für diskrete X",de:r`\(P(X\le k)=F(k)\) · \(P(X\lt k)=F(k-1)\) · \(P(X\gt k)=1-F(k)\) · \(P(X\ge k)=1-F(k-1)\)`,tr:r`Kesikli değişkende < ile ≤ farklıdır! P(X&lt;k)=F(k−1).`},
{t:"num",q:r`Fußball (Tutorium 7): Statistik-Lehrstuhl schießt Tore mit \(\lambda=2\), Ökonometrie mit \(\lambda=1.8\) pro Spiel. Berechne \(P(X=3)\) (Statistik), \(P(X\ge2)\) (Statistik) und \(P(Y\lt1)\) (Ökonometrie).`,f:[{l:"P(X=3) =",a:.180447},{l:"P(X≥2) =",a:.593994},{l:"P(Y<1) =",a:.165299}],why:r`\(\frac{2^3}{3!}e^{-2}=\frac86\cdot0.1353=0.180\). \(1-P(0)-P(1)=1-e^{-2}(1+2)=0.594\) → <code>1-ppois(1,2)</code>. \(P(Y=0)=e^{-1.8}=0.165\).`},
{t:"mc",q:r`\(Y\) = Anzahl Gewittertage im Monat, im Schnitt 2. Mit welchem R-Befehl bekommst du \(P(Y\gt2)\)? (Testat 4, Aufgabe 3)`,o:["dpois(2, 2)","1-dpois(2, 2)","ppois(2, 2)","1-ppois(2, 2)","1-ppois(3, 2)"],k:3,why:r`\(P(Y\gt2)=1-P(Y\le2)\) = <code>1-ppois(2,2)</code> = 0.323. Gleichwertig: <code>1-dpois(0,2)-dpois(1,2)-dpois(2,2)</code>.`},
{t:"num",q:r`Sack mit 60 schwarzen und 20 gelben Kugeln, 5-mal <b>mit</b> Zurücklegen. \(X\) = Anzahl gelb. \(P(X\gt4)\)? (Testat 4, Aufgabe 2)`,f:[{l:"P(X>4) =",a:.0009765625,tol:.00005}],why:r`\(X\sim B(5,\,0.25)\) (20 von 80). \(P(X\gt4)=P(X=5)=0.25^5=0.000977\approx0.001\). R-Simulation: <code>x &lt;- rbinom(10000, size = 5, prob = 0.25)</code>.`},
{t:"r",h:"Die vier Buchstaben d · p · q · r",code:r`
dbinom(x = 2, size = 10, prob = 0.25)   # P(X = 2)
pbinom(q = 2, size = 10, prob = 0.25)   # P(X <= 2)
qbinom(p = 0.5, size = 10, prob = 0.25) # Quantil (Median)
rbinom(n = 5, size = 10, prob = 0.25)   # 5 Zufallszahlen
dpois(3, lambda = 2); 1 - ppois(1, lambda = 2)`,
out:r`
[1] 0.2815676
[1] 0.5255928
[1] 2`,
notes:[[1,"<b>d</b> = density / Wahrscheinlichkeitsfunktion: \\(P(X=x)\\).","d: tam olarak x olma olasılığı."],[2,"<b>p</b> = probability / Verteilungsfunktion: \\(P(X\\le q)\\).","p: x'e kadar (≤) birikimli olasılık."],[3,"<b>q</b> = Quantil (Umkehrung von p).",""],[4,"<b>r</b> = random: Zufallszahlen ziehen.",""]]},
{t:"idea",h:"Randnotiz: Lotto (hypergeometrisch, V05)",de:r`<p>Ziehen <b>ohne</b> Zurücklegen: \(P(X=x)=\binom nx\binom{N-n}{n-x}/\binom Nn\). 3 Richtige aus 49: ≈ 0.0177, \(E(X)=0.735\). Wichtig ist vor allem: <b>ohne</b> Zurücklegen ist <b>nicht</b> binomial.</p>`}
]});

L({id:"3.5",day:3,no:5,title:"Gleich- & Exponentialverteilung",min:40,rel:2,
src:["V07","Tutorium 7","Testat 0, 4"],
goal:"Du kennst Dichte, Verteilungsfunktion, Erwartungswert und Varianz der beiden einfachen stetigen Modelle und rechnest Wartezeit-Aufgaben.",
blocks:[
{t:"formula",h:"Gleichverteilung U(a, b)",tex:r`f(x)=\frac1{b-a}\ \ (a\le x\le b)\qquad F(x)=\frac{x-a}{b-a}\qquad E(X)=\frac{a+b}{2}\qquad Var(X)=\frac{(b-a)^2}{12}`},
{t:"formula",h:"Exponentialverteilung Exp(λ)",tex:r`f(x)=\lambda e^{-\lambda x}\ (x\ge0)\qquad F(x)=1-e^{-\lambda x}\qquad P(X\gt x)=e^{-\lambda x}\qquad E(X)=\frac1\lambda\qquad Var(X)=\frac1{\lambda^2}`,note:r`Modell für <b>Wartezeiten/Dauern</b> (stetig). Poisson zählt Ereignisse, Exponential misst die Zeit dazwischen.`,tr:r`Üstel dağılım: bekleme süresi. Ortalama 3 ay ise λ = 1/3.`},
{t:"fig",kind:"density",h:"Exp(1/3): P(Y > 4) ist die Fläche rechts von 4",dist:"exp",p:{rate:1/3},x:[0,15],y:[0,.36],xl:"Monate",shade:[[4,15,"a"]],cap:"e^{−4/3} = 0.264"},
{t:"num",q:r`Gewitter (Tutorium 7, Aufgabe 3): im Mittel alle 3 Monate. \(Y\) = Zeit bis zum nächsten Gewitter. Bestimme \(\lambda\), \(Var(Y)\), \(P(Y\gt4)\) und \(P(1\lt Y\lt6)\).`,
f:[{l:"λ =",a:1/3},{l:"Var(Y) =",a:9},{l:"P(Y>4) =",a:.263597},{l:"P(1&lt;Y&lt;6) =",a:.581196}],why:r`\(E(Y)=3=\frac1\lambda\Rightarrow\lambda=\frac13\), \(Var=9\). \(P(Y\gt4)=e^{-4/3}=0.264\) → <code>1-pexp(4, 1/3)</code>. \(P(1\lt Y\lt6)=e^{-1/3}-e^{-2}=0.717-0.135=0.581\) → <code>pexp(6,1/3)-pexp(1,1/3)</code>.`},
{t:"num",q:r`Ein Fuchs braucht im Mittel 3 Stunden, bis er eine Gans fängt. \(P\)(länger als 10 Stunden)? (Testat 4, Aufgabe 8)`,f:[{l:"P(X>10) =",a:.035674}],why:r`\(X\sim Exp(1/3)\), \(P(X\gt10)=e^{-10/3}=0.036\).`},
{t:"r",h:"Eigene Funktion (Tutorium 7)",code:r`
predict_thunder <- function(y, lambda) {
  res <- 1 - pexp(y, lambda)     # P(Y > y)
  return(res)
}
predict_thunder(1, 1/3)
predict_thunder(6, 1/3)
hist(verteilung1, freq = FALSE)
curve(dexp(x, 1/3), add = TRUE)   # Dichte ins Histogramm`,
out:r`
[1] 0.7165313
[1] 0.1353353`,notes:[[1,"Aufbau jeder R-Funktion: <code>name &lt;- function(argumente) { … return(ergebnis) }</code>. Kommt im B-Teil fast immer vor.","Fonksiyon yapısı: isim <- function(argümanlar) { ... return(sonuç) }"],[8,"<code>add = TRUE</code> zeichnet in die bestehende Grafik.",""]]}
]});

L({id:"3.6",day:3,no:6,title:"Normalverteilung & Zentraler Grenzwertsatz",min:70,rel:3,
src:["V07","Tutorium 5, 7","Testat 4"],
goal:"Du standardisierst jede Normalverteilung, liest Φ ab (auch negative z), kennst die wichtigen Quantile und nutzt den ZGWS für Mittelwerte — die Grundlage für Konfidenzintervalle und Tests.",
blocks:[
{t:"formula",h:"Normalverteilung N(μ, σ²)",tex:r`f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)\qquad E(X)=\mu,\quad Var(X)=\sigma^2`,note:r`Die Verteilungsfunktion hat keine Formel → Tabelle für \(\Phi\) oder R.`},
{t:"formula",h:"Standardisieren",tex:r`Z=\frac{X-\mu}{\sigma}\sim N(0,1)\qquad F(x)=\Phi\Big(\frac{x-\mu}{\sigma}\Big)\qquad \Phi(-z)=1-\Phi(z)`,tr:r`Standartlaştırma: ortalamayı çıkar, standart sapmaya böl (varyansa DEĞİL!).`},
{t:"widget",w:"norm"},
{t:"ex",h:"Flugzeit (V07)",q:r`\(X\sim N(183,\,14^2)\) Minuten. \(P(180\lt X\lt190)\)?`,
steps:[r`\(F(190)=\Phi\big(\frac{190-183}{14}\big)=\Phi(0.5)=0.6915\).`,r`\(F(180)=\Phi\big(\frac{180-183}{14}\big)=\Phi(-0.21)=1-\Phi(0.21)=1-0.5832=0.4168\).`,r`\(0.6915-0.4168=0.2747\).`],a:r`≈ 0.275 (R exakt: 0.276, weil −0.2143 nicht auf −0.21 gerundet wird)`},
{t:"formula",h:"Wichtige Quantile der Standardnormalverteilung",tex:r`z_{0.75}=0.67\quad z_{0.90}=1.28\quad z_{0.95}=1.645\quad z_{0.975}=1.96\quad z_{0.99}=2.33\quad z_{0.995}=2.58\qquad z_\alpha=-z_{1-\alpha}\qquad q_\alpha=\mu+\sigma z_\alpha`,note:r`Diese sechs Zahlen gehören auf dein Formelblatt — sie tauchen in jedem KI und jedem Test auf.`},
{t:"num",q:r`Mehlpackungen \(X\sim N(500,\,9)\) (Testat 4, Aufgabe 9). \(P(X\gt500)\), \(P(X\ge505)\), \(P(496\le X\le502)\).`,f:[{l:"P(X>500) =",a:.5},{l:"P(X≥505) =",a:.04779,tol:.0006},{l:"P(496≤X≤502) =",a:.656296,tol:.002}],why:r`\(\sigma=\sqrt9=3\) (nicht 9!). \(P(X\gt500)=0.5\) (Symmetrie). \(1-\Phi(\frac53)=1-\Phi(1.67)=0.048\). \(\Phi(\frac23)-\Phi(-\frac43)=0.7475-0.0912=0.656\). R: <code>pnorm((502-500)/3) - pnorm((496-500)/3)</code>.`},
{t:"num",q:r`Körpergröße \(X\sim N(175,\,9.5^2)\) (Tutorium 7, Aufgabe 4). Wahrscheinlichkeit, dass die Größe den Erwartungswert um mehr als 2 Standardabweichungen übersteigt?`,f:[{l:"P(X>194) =",a:.02275}],why:r`\(175+2\cdot9.5=194\). \(1-\Phi(2)=0.023\). R: <code>1-pnorm(194, 175, 9.5)</code> — in R gibst du <b>σ</b> an, nicht σ².`},
{t:"formula",h:"Transformation & Summen",tex:r`aX+b\sim N(a\mu+b,\ a^2\sigma^2)\qquad X\perp Y:\ X+Y\sim N(\mu_X+\mu_Y,\ \sigma_X^2+\sigma_Y^2)`},
{t:"idea",h:"Zentraler Grenzwertsatz (ZGWS)",de:r`
<p>Egal wie \(X_1,\dots,X_n\) (iid, \(E=\mu\), \(Var=\sigma^2\)) verteilt sind — der Mittelwert ist für großes \(n\) <b>näherungsweise normalverteilt</b>:</p>`,tr:r`Merkezi limit teoremi: n büyükse örnek ortalaması, verinin dağılımı ne olursa olsun yaklaşık normal dağılır.`},
{t:"formula",h:"ZGWS",tex:r`\bar X\overset{a}{\sim}N\Big(\mu,\ \frac{\sigma^2}{n}\Big)\qquad\sqrt n\,\frac{\bar X-\mu}{\sigma}\overset{a}{\sim}N(0,1)`},
{t:"mc",q:r`\(X\sim U(a,b)\), \(E(X)=4\), Stichprobe \(n=100\) iid. \(P(\bar X\lt4)\)? (Testat 4, Aufgabe 7)`,o:["0.25","0.5","0.95","nicht bestimmbar ohne a und b"],k:1,why:r`ZGWS: \(\bar X\overset a\sim N(4,\sigma^2/100)\), symmetrisch um 4 → \(P(\bar X\lt4)=0.5\) — egal wie groß \(\sigma^2\) ist.`},
{t:"idea",h:"Bivariate Normalverteilung (kurz)",de:r`<p>\((X,Y)\sim N(\mu_x,\mu_y,\sigma_x^2,\sigma_y^2,\rho)\). Randverteilungen sind normal: \(X\sim N(\mu_x,\sigma_x^2)\). Bedingt: \(X\mid Y=y\sim N\big(\mu_x+\rho\frac{\sigma_x}{\sigma_y}(y-\mu_y),\ \sigma_x^2(1-\rho^2)\big)\). <b>Nur hier</b> gilt: unkorreliert ⇔ unabhängig.</p>`},
{t:"r",h:"Normalverteilung in R",code:r`
pnorm(190, mean = 183, sd = 14) - pnorm(180, mean = 183, sd = 14)
qnorm(0.975)                       # z_0.975
1 - pnorm(505, 500, 3)
rnorm(50, 175, 9.5)                # 50 Zufallszahlen
pnorm(seq(-1.5, 1.5, 0.5))         # Standard: mean = 0, sd = 1`,
out:r`
[1] 0.2763003
[1] 1.959964
[1] 0.04779035`,notes:[[1,"Immer <code>sd</code> übergeben, nicht die Varianz.","R'da her zaman standart sapma verilir."],[5,"Ohne Parameter rechnet R mit N(0,1).",""]]},
{t:"trap",items:[r`Varianz statt Standardabweichung eingesetzt: \(\frac{x-\mu}{\sigma^2}\).`,r`\(\Phi(-z)\) direkt in der Tabelle gesucht — die Tabelle hat meist nur positive \(z\): \(\Phi(-z)=1-\Phi(z)\).`,r`Bei „mehr als“ vergessen, \(1-\Phi\) zu nehmen.`]}
]});
