/* ================= TAG 4 · Schätzen ================= */

L({id:"4.1",day:4,no:1,title:"Die Idee der Likelihood",min:45,rel:3,
src:["V08","R-Skript 08"],
goal:"Du verstehst, was ein statistisches Modell und eine Likelihood ist, und warum wir die Log-Likelihood maximieren.",
blocks:[
{t:"idea",h:"Von der Stichprobe zurück auf die Grundgesamtheit",de:r`
<p>Bisher (Tag 3): Parameter bekannt → wie wahrscheinlich sind Daten? Das ist <b>Wahrscheinlichkeitsrechnung</b>. Jetzt drehen wir um: Daten bekannt → welcher Parameter passt am besten? Das ist <b>Inferenz</b> (induktive Statistik).</p>
<p>Ein <b>statistisches Modell</b> sagt: \(X_1,\dots,X_n\overset{iid}{\sim}F_\vartheta\) — die Daten kommen unabhängig aus derselben Verteilung, nur der Parameter \(\vartheta\) ist unbekannt. Zwei Fehlerquellen: <b>Approximationsfehler</b> (das Modell stimmt nicht genau) und <b>Schätzfehler</b> (die Stichprobe ist zufällig).</p>`,
tr:r`Olasılık hesabı: parametre → veri. Çıkarımsal istatistik: veri → parametre. Model: veriler aynı dağılımdan bağımsız geliyor, sadece parametre bilinmiyor.`},
{t:"formula",h:"Likelihood und Log-Likelihood",tex:r`L(\vartheta)=\prod_{i=1}^{n}f(x_i;\vartheta)\qquad \ell(\vartheta)=\log L(\vartheta)=\sum_{i=1}^{n}\log f(x_i;\vartheta)`,
parts:[[r`f(x_i;\vartheta)`,"Wahrscheinlichkeitsfunktion \\(P(X=x_i)\\) (diskret) oder Dichte (stetig)"],[r`\prod`,"weil iid: gemeinsame W. = Produkt der einzelnen"],[r`\hat\vartheta_{ML}`,"der Wert, der \\(L\\) (und damit \\(\\ell\\)) maximiert"]],
tr:r`Likelihood: gözlenen verinin, parametrenin bir fonksiyonu olarak olasılığı. En büyük yapan parametre = ML tahmini. Logaritma maksimumun yerini değiştirmez.`},
{t:"ex",h:"Münzwurf (V08)",q:r`20 Würfe, 6-mal Wappen. Für welches \(\pi\) sind diese Daten am plausibelsten?`,
steps:[r`Modell: \(X\sim B(20,\pi)\), beobachtet \(x=6\). \(L(\pi)=\binom{20}{6}\pi^6(1-\pi)^{14}\).`,
r`Tabelle: \(L(0.1)=0.009\), \(L(0.2)=0.109\), \(L(0.3)=0.192\), \(L(0.4)=0.124\), \(L(0.5)=0.037\), \(L(0.6)=0.005\).`,
r`Maximum bei \(\pi=0.3\) — genau der Anteil \(6/20\).`],a:r`\(\hat\pi_{ML}=0.3\)`},
{t:"widget",w:"lik"},
{t:"idea",h:"Warum logarithmieren?",de:r`
<ul><li><b>Rechnen:</b> Aus dem Produkt wird eine Summe — Ableiten wird einfach.</li>
<li><b>Gleiches Maximum:</b> \(\log\) ist streng monoton wachsend.</li>
<li><b>Numerik (B-Teil!):</b> Ein Produkt vieler kleiner Zahlen wird in R zu 0 abgerundet — <span class="hl">numerical underflow</span>. Die Summe der Logs bleibt eine normale Zahl.</li></ul>`,
tr:r`Logaritma: çarpımı toplama çevirir, maksimum aynı kalır, R'da çok küçük sayıların 0'a yuvarlanmasını (underflow) önler.`},
{t:"mc",q:r`Warum wird bei der ML-Schätzung in R üblicherweise nicht direkt die Likelihood maximiert? (ML-Probeklausur B, Aufgabe f)`,o:["Weil R keine Produkte berechnen kann.","Weil das Produkt vieler kleiner Dichtewerte zu 0 abgerundet wird (numerical underflow); man logarithmiert deshalb.","Weil die Likelihood immer negativ ist."],k:1,why:r`Musterantwort: „Bei der direkten Optimierung tritt das Problem des numerical underflow auf, wobei sehr kleine Werte zu 0 abgerundet werden. Üblicherweise wird die Likelihood logarithmiert.“`}
]});

L({id:"4.2",day:4,no:2,title:"ML-Schätzer herleiten: diskrete Modelle",min:70,rel:3,
src:["V08","Tutorium 8","Testat 0, 5","Probeklausur B (Witcher)"],
goal:"Du leitest ML-Schätzer mit dem 6-Schritte-Rezept her — für Poisson, Bernoulli, geometrische Verteilung und eigene Tabellen-Verteilungen.",
blocks:[
{t:"rule",k:"Das Rezept · Testat 5, Aufgabe 2",de:r`<b>1.</b> Verteilungsmodell wählen · <b>2.</b> Likelihood \(L=\prod f(x_i)\) aufstellen · <b>3.</b> logarithmieren · <b>4.</b> nach dem Parameter ableiten und gleich 0 setzen · <b>5.</b> nach dem Parameter auflösen · <b>6.</b> Maximum prüfen (2. Ableitung &lt; 0).`,tr:r`1) model seç 2) L=Πf(xᵢ) 3) log al 4) türev = 0 5) parametreyi çöz 6) ikinci türev < 0 kontrol et.`},
{t:"ex",h:"Poisson (Tutorium 8, Aufgabe 2)",q:r`\(X_i\overset{iid}\sim Po(\lambda)\), Stichprobe 2, 3, 2, 5, 7.`,
steps:[r`\(L(\lambda)=\prod\frac{\lambda^{x_i}}{x_i!}e^{-\lambda}=\lambda^{\sum x_i}\,e^{-n\lambda}\prod\frac1{x_i!}\).`,
r`\(\ell(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log(x_i!)\).`,
r`\(\ell'(\lambda)=\frac{\sum x_i}{\lambda}-n\overset!=0\).`,
r`\(\hat\lambda=\frac1n\sum x_i=\bar x=\frac{19}{5}=3.8\).`,
r`Check: \(\ell''(\lambda)=-\frac{\sum x_i}{\lambda^2}\lt0\) → Maximum. ✓`],a:r`\(\hat\lambda_{ML}=\bar x=3.8\)`},
{t:"formula",h:"Standard-Ergebnisse (merken!)",tex:r`Po(\lambda):\ \hat\lambda=\bar x\qquad Be(\pi):\ \hat\pi=\bar x\qquad Geo:\ P(X=x)=(1-p)^xp\ \Rightarrow\ \hat p=\frac{1}{1+\bar x}\qquad Exp(\lambda):\ \hat\lambda=\frac1{\bar x}\qquad N(\mu,\sigma^2):\ \hat\mu=\bar x,\ \hat\sigma^2=S^2`},
{t:"ex",h:"Geometrische Verteilung (Tutorium 8, Aufgabe 1)",q:r`\(P(X=x)=(1-p)^xp\) für \(x=0,1,2,\dots\). Stichprobe: 11, 15, 77, 17, 12.`,
steps:[r`\(L(p)=(1-p)^{11}p\cdot(1-p)^{15}p\cdots=(1-p)^{132}p^5\) (denn \(\sum x_i=132\), \(n=5\)).`,
r`\(\ell(p)=132\log(1-p)+5\log p\).`,
r`\(\ell'(p)=-\frac{132}{1-p}+\frac5p\overset!=0\iff 5(1-p)=132p\iff 5=137p\).`,
r`\(\hat p=\frac{5}{137}=0.036\). Allgemein: \(\hat p=\frac{n}{n+\sum x_i}=\frac{1}{1+\bar x}\).`],a:r`\(\hat p=0.036\)`},
{t:"num",q:r`Testat 5, Aufgabe 4: Träger {1, 2, 3} mit \(P(X=1)=\alpha\), \(P(X=2)=\alpha^2\), \(P(X=3)=1-\alpha-\alpha^2\) (\(0\lt\alpha\le0.618\)). Stichprobe 1, 3, 2, 1. Bestimme \(\hat\alpha\).`,f:[{l:"α̂ =",a:.5}],
why:r`\(L(\alpha)=\alpha\cdot(1-\alpha-\alpha^2)\cdot\alpha^2\cdot\alpha=\alpha^4(1-\alpha-\alpha^2)\).<br>\(\ell=4\log\alpha+\log(1-\alpha-\alpha^2)\), \(\ell'=\frac4\alpha-\frac{1+2\alpha}{1-\alpha-\alpha^2}=0\).<br>\(4(1-\alpha-\alpha^2)=\alpha(1+2\alpha)\iff 6\alpha^2+5\alpha-4=0\iff\alpha=\frac{-5+\sqrt{25+96}}{12}=\frac{6}{12}=0.5\) (die negative Lösung fällt weg).`},
{t:"mc",q:r`Testat 5, Aufgabe 5: \(P(x)=\theta(1-\theta)^x\), \(x=0,1,2,\dots\). Wie lautet die Log-Likelihood?`,o:[r`\(\ell(\theta)=n\log\theta+\sum x_i\log(1-\theta)\)`,r`\(\ell(\theta)=\log\theta+\log(1-\theta)\sum x_i\)`,r`\(\ell(\theta)=\theta^n(1-\theta)^{\sum x_i}\)`],k:0,why:r`\(L=\theta^n(1-\theta)^{\sum x_i}\) (das ist \(L\), nicht \(\ell\)!). Log: \(n\log\theta+\sum x_i\log(1-\theta)\). Ergebnis \(\hat\theta=\frac1{1+\bar x}\) — dieselbe Struktur wie oben.`},
{t:"exam",h:"Übung im Probeklausur-Stil (etwas schwerer)",src:"eigene Aufgabe",q:r`Eine Zufallsvariable nimmt die Werte 0, 1, 2 an mit \(P(X=0)=\theta^2\), \(P(X=1)=2\theta(1-\theta)\), \(P(X=2)=(1-\theta)^2\), \(0\lt\theta\lt1\). Beobachtet: 0 kommt 4-mal, 1 kommt 10-mal, 2 kommt 6-mal vor.`,
parts:[{q:r`(a) Stellen Sie die Likelihood auf und vereinfachen Sie.`,p:3,s:r`\(L(\theta)=(\theta^2)^4\,\big(2\theta(1-\theta)\big)^{10}\,\big((1-\theta)^2\big)^6=2^{10}\,\theta^{18}\,(1-\theta)^{22}\).`},
{q:r`(b) Leiten Sie den ML-Schätzer her und berechnen Sie ihn.`,p:4,s:r`\(\ell=10\log2+18\log\theta+22\log(1-\theta)\). \(\ell'=\frac{18}\theta-\frac{22}{1-\theta}=0\iff18(1-\theta)=22\theta\iff\hat\theta=\frac{18}{40}=0.45\).`},
{q:r`(c) Prüfen Sie die Bedingung zweiter Ordnung.`,p:2,s:r`\(\ell''=-\frac{18}{\theta^2}-\frac{22}{(1-\theta)^2}\lt0\) für alle \(\theta\) → Maximum.`}]},
{t:"r",h:"Likelihood im B-Teil: über ein Raster suchen (Witcher f, g)",code:r`
d$iL20 <- dpois(d$Muenzen, 20)       # individuelle Likelihoods bei lambda = 20
prod(d$iL20)                          # Likelihood aller Beobachtungen
Likelihood.pois <- function(lambda, x) {
  L <- prod(dpois(x, lambda))
  return(L)
}
for (lambda in 17:23) {
  print(Likelihood.pois(lambda, d$Muenzen))
}`,
out:r`
[1] 6.938384e-131
[1] 3.128764e-158
[1] 2.720028e-146
[1] 2.817315e-137
[1] 6.938384e-131
[1] 7.328025e-127
[1] 5.513116e-125
[1] 4.586278e-125`,
notes:[[1,"Neue Spalte im Data Frame mit <code>d$neu &lt;-</code>.",""],[2,"Antwort in der Form \\(X\\times10^Y\\): \\(L(\\lambda=20)=6.938\\times10^{-131}\\).","6.938e-131 = 6.938 × 10^(−131)"],[8,"Größter Wert bei \\(\\lambda=22\\) (5.513e-125 &gt; 4.586e-125). Antwortsatz: „Das Maximum der Likelihood ergibt sich bei λ = 22; somit ist der ML-Schätzer \\(\\hat\\lambda=22\\).“","e-125 ile e-127'yi karşılaştırırken üsse dikkat: −125 daha büyük."]]},
{t:"trap",items:[r`\(L\) und \(\ell\) verwechselt (Aufgabe fragt nach der <b>Log</b>-Likelihood).`,r`Bei \(\prod a^{x_i}\) vergessen: \(=a^{\sum x_i}\), und \(\prod c=c^n\).`,r`Beim Vergleichen von e-Zahlen: \(10^{-125}\gt10^{-127}\).`,r`Schritt 6 (2. Ableitung) weggelassen, obwohl gefragt.`]}
]});

L({id:"4.3",day:4,no:3,title:"ML-Schätzer herleiten: stetige Modelle",min:70,rel:3,
src:["V08","ML-Probeklausur A (Aufgaben 1–3)","Probeklausur A6","Testat 5"],
goal:"Du löst die typischen 10–12-Punkte-Aufgaben: Dichte gegeben → Log-Likelihood vereinfachen → Bedingung → Schätzer. Genau so, wie es in der ML-Probeklausur bewertet wird.",
blocks:[
{t:"ex",h:"Exponential / Weibull mit r = 1 (Probeklausur A6)",q:r`\(f(x;\lambda)=\lambda e^{-\lambda x}\) (Weibull mit \(r=1\)), \(X_1,\dots,X_n\) iid.`,
steps:[r`\(L(\lambda)=\prod\lambda e^{-\lambda x_i}=\lambda^n e^{-\lambda\sum x_i}\).`,r`\(\ell(\lambda)=n\log\lambda-\lambda\sum x_i\).`,r`\(\ell'(\lambda)=\frac n\lambda-\sum x_i\overset!=0\Rightarrow\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}\).`,r`\(\ell''(\lambda)=-\frac{n}{\lambda^2}\lt0\) → Maximum.`],a:r`\(\hat\lambda_{ML}=\dfrac{n}{\sum_{i=1}^nx_i}\)`},
{t:"exam",h:"ML-Probeklausur Aufgabe 1",src:"ML-Probeklausur A-Teil",q:r`Dichte \(f(x)=x^b(b+1)\) für \(0\lt x\le1\), sonst 0; \(b\ge0\). \(X_1,\dots,X_n\) iid.`,
parts:[{q:r`(a) Geben Sie die möglichst weit vereinfachte Log-Likelihood an.`,p:5,s:r`\(L(b)=\prod(b+1)x_i^b=(b+1)^n\prod x_i^b\).<br>\(\ell(b)=n\log(b+1)+b\sum_{i=1}^n\log x_i\).`},
{q:r`(b) Geben Sie die Bedingung an, aus der Sie den Schätzer lösen.`,p:4,s:r`\(\frac{\partial\ell}{\partial b}=\frac{n}{b+1}+\sum\log x_i\). Bedingung: \(\frac{n}{\hat b+1}+\sum_{i=1}^n\log x_i=0\).`},
{q:r`(c) Geben Sie die Schätzfunktion für \(b\) an.`,p:3,s:r`\(\hat b=-1-\dfrac{n}{\sum_{i=1}^n\log x_i}\).`}]},
{t:"num",q:r`Mit dem Ergebnis oben: Stichprobe 0.2, 0.5, 0.7, 0.9. Berechne \(\hat b\).`,f:[{l:"b̂ =",a:.4468532}],why:r`\(\sum\log x_i=-1.6094-0.6931-0.3567-0.1054=-2.7646\). \(\hat b=-1-\frac{4}{-2.7646}=-1+1.4469=0.447\).`},
{t:"exam",h:"ML-Probeklausur Aufgabe 2 (Lognormal)",src:"ML-Probeklausur A-Teil",q:r`Für \(x\gt0\): \(f(x)=\frac{1}{\sqrt{2\pi}\,\sigma x}\exp\Big(-\frac{(\log x-\mu)^2}{2\sigma^2}\Big)\), \(\sigma\gt0\) bekannt.`,
parts:[{q:r`(a) Möglichst weit vereinfachte Log-Likelihood.`,p:7,s:r`\(L(\mu)=\Big(\frac{1}{\sqrt{2\pi}\sigma}\Big)^n\exp\Big(-\frac{1}{2\sigma^2}\sum(\log x_i-\mu)^2\Big)\prod\frac1{x_i}\).<br>\(\ell(\mu)=-n\log(\sqrt{2\pi}\sigma)-\frac{1}{2\sigma^2}\sum_{i=1}^n(\log x_i-\mu)^2-\sum_{i=1}^n\log x_i\).`},
{q:r`(b) ML-Schätzer für \(\mu\).`,p:5,s:r`\(\frac{\partial\ell}{\partial\mu}=-\frac{1}{2\sigma^2}\sum2(\log x_i-\mu)(-1)=\frac1{\sigma^2}\sum(\log x_i-\mu)\overset!=0\).<br>\(\sum\log x_i-n\hat\mu=0\Rightarrow\hat\mu=\frac1n\sum_{i=1}^n\log x_i\).`}]},
{t:"exam",h:"ML-Probeklausur Aufgabe 3",src:"ML-Probeklausur A-Teil",q:r`\(f(x)=\beta\log(2)\,2^{-x\beta}\) für \(x\ge0\), \(\beta\gt0\).`,
parts:[{q:r`(a) Likelihoodfunktion.`,p:3,s:r`\(L(\beta)=\prod\log(2)\,\beta\,2^{-x_i\beta}=(\log 2)^n\beta^n\,2^{-\beta\sum x_i}\).`},
{q:r`(b) Log-Likelihood.`,p:3,s:r`\(\ell(\beta)=n\log(\log2)+n\log\beta-\beta\log(2)\sum x_i\). (Tipp: \(\log 2^{-x\beta}=-x\beta\log2\).)`},
{q:r`(c) ML-Schätzer mit vollständigem Lösungsweg.`,p:4,s:r`\(\ell'(\beta)=\frac n\beta-\log(2)\sum x_i\overset!=0\Rightarrow\hat\beta=\frac{n}{\log(2)\sum x_i}=\frac{1}{\log(2)\,\bar x}\).`}]},
{t:"ex",h:"Normalverteilung: μ bei bekanntem σ² (V08)",q:r`\(X_i\overset{iid}\sim N(\mu,\sigma^2)\), \(\sigma^2\) bekannt.`,
steps:[r`\(\ell(\mu)=-\frac n2\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2\).`,r`\(\ell'(\mu)=\frac1{\sigma^2}\sum(x_i-\mu)=0\Rightarrow\hat\mu=\bar x\).`],a:r`\(\hat\mu=\bar x\); für \(\sigma^2\) wäre der ML-Schätzer \(S^2=\frac1n\sum(x_i-\bar x)^2\) (verzerrt!).`},
{t:"trap",items:[r`Konstanten (\(\log(\log2)\), \(\sum\log x_i\)) beim Ableiten nicht als 0 behandelt.`,r`Minus beim inneren Ableiten von \((\log x_i-\mu)^2\) vergessen.`,r`Endergebnis nicht vereinfacht (z. B. \(\frac{n}{\sum x_i}\) statt \(\frac1{\bar x}\) ist ok, aber \(\frac{n\beta}{\dots}\) mit \(\beta\) auf beiden Seiten nicht).`,r`„Geben Sie den gesamten Lösungsweg an“ → jede Umformung hinschreiben.`]}
]});

L({id:"4.4",day:4,no:4,title:"Gütekriterien: Bias, Varianz, MSE",min:60,rel:3,
src:["V09","Tutorium 9","Testat 5","Probeklausur A7","R-Skript 09"],
goal:"Du prüfst mit Erwartungswert-Regeln, ob ein Schätzer unverzerrt ist, berechnest seine Varianz und kennst MSE, Konsistenz und die Eigenschaften von ML-Schätzern.",
blocks:[
{t:"formula",h:"Bias, Varianz, MSE",tex:r`Bias(\hat\vartheta)=E(\hat\vartheta)-\vartheta\qquad MSE(\hat\vartheta)=E\big[(\hat\vartheta-\vartheta)^2\big]=Bias^2(\hat\vartheta)+Var(\hat\vartheta)`,
parts:[[r`Bias=0`,"erwartungstreu / unverzerrt"],[r`MSE\to0\ (n\to\infty)`,"konsistent"],[r`Bias\to0\ (n\to\infty)`,"asymptotisch erwartungstreu"]],
tr:r`Bias: tahmincinin beklenen değeri ile gerçek değer arasındaki fark. MSE = Bias² + Varyans. n büyüdükçe MSE→0 ise tutarlı (konsistent).`},
{t:"idea",h:"Vier Schätzer für λ = 5 (Simulation aus R-Skript 09, n = 5)",de:r`
<div class="tbl"><table><tr><th class="l">Schätzer</th><th>Bias</th><th>Var</th><th>MSE</th><th class="l">Kommentar</th></tr>
<tr><td class="l">immer 3</td><td>−2</td><td>0</td><td>4</td><td class="l">keine Streuung, aber falsch</td></tr>
<tr><td class="l">\(X_1\) (nur erster Wert)</td><td>0</td><td>5</td><td>5</td><td class="l">unverzerrt, sehr unsicher</td></tr>
<tr><td class="l">\(\bar X\)</td><td>0</td><td>1</td><td>1</td><td class="l">bester: ML-Schätzer</td></tr>
<tr><td class="l">\(2\bar X\)</td><td>5</td><td>4</td><td>29</td><td class="l">verzerrt</td></tr></table></div>
<p>Merke: <b>Unverzerrt allein reicht nicht</b> — \(X_1\) ist unverzerrt, aber schlecht. Ein unverzerrter Schätzer hat <b>nicht immer</b> einen kleineren MSE als ein verzerrter (Testat 5).</p>`,
tr:r`Yansız olmak tek başına yetmez; MSE hem yanlılığı hem varyansı hesaba katar.`},
{t:"ex",h:"Bias eines Schätzers (Tutorium 9, Aufgabe 3)",q:r`\(\hat\mu=\frac2n\sum_{i=1}^nX_i\) für den Erwartungswert \(\mu\).`,
steps:[r`Erwartungswert ist linear: \(E(\hat\mu)=\frac2n\sum E(X_i)\).`,r`\(=\frac2n\cdot n\mu=2\mu\).`,r`\(Bias=2\mu-\mu=\mu\ne0\) (außer \(\mu=0\)).`],a:r`verzerrt, \(Bias(\hat\mu)=\mu\)`},
{t:"ex",h:"Varianz eines Mittelwert-Schätzers (Tutorium 9, Aufgabe 2)",q:r`\(E(X_i)=\frac1\gamma\), \(E(X_i^2)=\frac{2+\gamma}{\gamma}\), Schätzer \(\hat\gamma=\sum\frac{X_i}{n}=\bar X\).`,
steps:[r`\(E(\hat\gamma)=\frac1n\sum\frac1\gamma=\frac1\gamma\ne\gamma\) → verzerrt.`,r`\(Var(X_i)=E(X_i^2)-(EX_i)^2=\frac{2+\gamma}{\gamma}-\frac1{\gamma^2}=\frac{\gamma^2+2\gamma-1}{\gamma^2}\).`,r`\(Var(\hat\gamma)=\frac1{n^2}\sum Var(X_i)=\frac1n Var(X_i)\) (Unabhängigkeit!).`],a:r`\(Var(\hat\gamma)=\dfrac{\gamma^2+2\gamma-1}{n\gamma^2}\)`},
{t:"mc",q:r`Testat 5, Aufgabe 1: \(E(X)=\kappa/2\), Schätzer \(\tilde\kappa=X_1+\frac1{2n}\sum_{i=2}^nX_i\). Welche Aussagen stimmen?`,o:[r`\(\tilde\kappa\) ist erwartungstreu, weil alle Beobachtungen denselben Erwartungswert haben.`,r`\(\tilde\kappa\) ist unverzerrt, weil er alle Daten berücksichtigt.`,r`Der Bias von \(\tilde\kappa\) hängt von \(n\) ab.`,r`Der Bias ist ungleich 0.`,r`Ein erwartungstreuer Schätzer hat immer einen kleineren MSE als \(\tilde\kappa\).`],k:[2,3],
why:r`\(E(\tilde\kappa)=\frac\kappa2+\frac{n-1}{2n}\cdot\frac\kappa2=\frac\kappa2+\frac{(n-1)\kappa}{4n}\). \(Bias=-\frac{(n+1)\kappa}{4n}\) — hängt von \(n\) ab und ist \(\ne0\).`},
{t:"exam",h:"Probeklausur Aufgabe 7",src:"Probeklausur A-Teil",q:r`\(E(X)=\frac\alpha4\), \(X_1,\dots,X_n\) iid. Ist \(\hat\alpha=\dfrac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}+\dfrac{X_n}{\alpha}-\dfrac14\) unverzerrt?`,
parts:[{q:r`Prüfen Sie mit Rechenweg.`,p:5,s:r`Erst kürzen: \(\frac{\prod_{i=2}^{n-1}X_i}{\prod_{i=1}^{n-1}X_i}=\frac1{X_1}\).<br>\(E(\hat\alpha)=E\big(\tfrac1{X_1}\big)+\frac{E(X_n)}{\alpha}-\frac14\). Musterlösung: \(=\frac{1}{\alpha/4}+\frac{\alpha/4}{\alpha}-\frac14=\frac4\alpha\ne\alpha\) → <b>verzerrter Schätzer</b>.<br><small class="muted">Streng genommen gilt \(E(1/X)=1/E(X)\) nicht allgemein; die Musterlösung rechnet aber so, und das Ergebnis „verzerrt“ bleibt richtig.</small>`}]},
{t:"idea",h:"Eigenschaften von ML-Schätzern (Testat 5, Aufgabe 3)",de:r`<p>Für iid-Daten (unter Zusatzannahmen) sind ML-Schätzer:</p><ul><li><b>asymptotisch erwartungstreu</b>: \(Bias\to0\) für \(n\to\infty\),</li><li><b>konsistent</b>: \(MSE\to0\),</li><li><b>asymptotisch normalverteilt</b>.</li></ul><p>Beispiel Bernoulli: \(\hat\pi=\bar X\) ist unverzerrt mit \(Var=\frac{\pi(1-\pi)}{n}\to0\) → konsistent.</p>`,tr:r`ML tahmincileri: asimptotik yansız, tutarlı ve asimptotik normal dağılımlı.`},
{t:"trap",items:[r`\(E(X_1\cdot X_2)=E(X_1)E(X_2)\) nur bei Unabhängigkeit.`,r`Bei \(Var(\frac1n\sum X_i)\) den Faktor \(\frac1{n^2}\) vergessen.`,r`Vor dem Erwartungswert nicht gekürzt (Probeklausur A7!).`]}
]});

L({id:"4.5",day:4,no:5,title:"Histogramm & Kerndichteschätzer",min:40,rel:2,
src:["V09","Tutorium 9","R-Skript 09 (KDE)"],
goal:"Du erklärst Approximations- vs. Schätzfehler beim Histogramm, verstehst die Formel des Kerndichteschätzers und die Rolle der Bandbreite — und zeichnest einen KDE in R.",
blocks:[
{t:"idea",h:"Das Histogramm als Dichteschätzer",de:r`
<p>Ein Histogramm mit \(J\) Klassen hat \(J-1\) freie Parameter. Zwei Fehler (Tutorium 9):</p>
<ul><li><b>Approximationsfehler</b>: die Treppe ist grob — wird kleiner mit <b>mehr / schmaleren Klassen</b>.</li><li><b>Schätzfehler</b>: zufällige Schwankung — wird kleiner mit <b>größerem n</b>.</li></ul>
<p>Mehr Klassen bei gleichem \(n\) → weniger Beobachtungen pro Klasse → größerer Schätzfehler. Das ist der Bias-Varianz-Trade-off.</p>`,tr:r`Az sınıf → kaba (yaklaşım hatası büyük). Çok sınıf ama az veri → oynak (tahmin hatası büyük). n artınca ikisi de iyileşir.`},
{t:"formula",h:"Fließendes Histogramm & Kerndichteschätzer",tex:r`\hat f(x)=\frac{1}{2b}\cdot\frac{\#\{x_i\in(x-b,\,x+b]\}}{n}\qquad \hat f(x)=\frac{1}{nb}\sum_{i=1}^{n}K\Big(\frac{x-x_i}{b}\Big)`,
parts:[["b","Bandbreite (steuert die Glätte)"],["K","Kern: Rechteck \\(\\tfrac12\\) auf [−1,1), Epanechnikov \\(\\tfrac34(1-u^2)\\), Bisquare \\(\\tfrac{15}{16}(1-u^2)^2\\), Gauß (Standardnormaldichte)"]],
tr:r`Çekirdek yoğunluk tahmini: her gözlemin üzerine küçük bir tepe (çekirdek) koy ve ortalamasını al. b büyük → çok düz, b küçük → çok dalgalı.`},
{t:"widget",w:"kde"},
{t:"r",h:"KDE in R",code:r`
x <- rnorm(100)
plot(density(x))                                    # Gauß-Kern, Bandbreite automatisch
plot(density(x, bw = 0.5, kernel = "epanechnikov")) # eigene Wahl
plot(density(d$Y), main = "Sitz 00, Matr.Nr. 31415926, Beispielaufgabe (c)",
     xlab = "Y", ylab = "Dichte")`,
notes:[[2,"<code>density()</code> berechnet den KDE, <code>plot()</code> zeichnet ihn. Genau so in der Beispielaufgabe der Probeklausur B („Visualisieren Sie einen Kerndichteschätzer“).","density() KDE hesaplar."],[3,"<code>bw</code> = Bandbreite, <code>kernel</code> = Kernfunktion.",""]]},
{t:"mc",q:r`Du erhöhst bei konstantem \(n=500\) die Klassenbreite von 0.5 auf 2.5. Was passiert? (Tutorium 9, Aufgabe 1)`,o:["Der Approximationsfehler wird kleiner.","Der Approximationsfehler wird größer, der Schätzfehler kleiner.","Beide Fehler werden kleiner."],k:1,why:r`Breitere Klassen = weniger Parameter → gröbere Form (Approximationsfehler ↑), aber mehr Beobachtungen pro Klasse (Schätzfehler ↓).`}
]});

L({id:"4.6",day:4,no:6,title:"Konfidenzintervalle",min:80,rel:3,
src:["V10","Tutorium 10","Testat 6","R-Skript 10"],
goal:"Du wählst die richtige KI-Formel (σ bekannt / unbekannt / Anteil / Varianz), findest das richtige Quantil, rechnest das Intervall und interpretierst es korrekt.",
blocks:[
{t:"idea",h:"Warum ein Intervall?",de:r`
<p>Ein Punktschätzer trifft den wahren Wert fast nie: bei \(\pi=0.5\) ist \(P(\hat\pi=\pi)\) für \(n=10\) nur 0.246, für \(n=100\) 0.080, für \(n=1000\) 0.025. Bei stetigen Daten ist sie 0. Deshalb gibt man ein <b>Intervall</b> \([L,U]\) an mit \(P(L\le\vartheta\le U)\ge1-\alpha\).</p>
<p><b>Interpretation:</b> Die <span class="hl">Grenzen sind zufällig, der Parameter ist fest</span>. Bei wiederholter Stichprobenziehung überdecken etwa \(100(1-\alpha)\,\%\) der Intervalle den wahren Parameter. <i>Nicht</i>: „Der Parameter fällt mit 95 % ins Intervall.“</p>`,
tr:r`Güven aralığı: sınırlar rastgele, parametre sabit. Çok kez örnek çekersek aralıkların %95'i gerçek değeri kapsar.`},
{t:"widget",w:"ci"},
{t:"formula",h:"KI für μ, σ bekannt (Normalverteilung oder ZGWS)",tex:r`\bar x\pm z_{1-\alpha/2}\,\frac{\sigma}{\sqrt n}`,parts:[["z_{0.95}=1.645","90 %"],["z_{0.975}=1.96","95 %"],["z_{0.995}=2.576","99 %"]]},
{t:"formula",h:"KI für μ, σ unbekannt",tex:r`\bar x\pm t_{n-1,\,1-\alpha/2}\,\frac{s_*}{\sqrt n}\qquad s_*=\sqrt{\tfrac1{n-1}\textstyle\sum(x_i-\bar x)^2}\ \ (\text{R: } sd(x))`,note:r`\(t\)-Verteilung mit \(n-1\) Freiheitsgraden: breiter als die Normalverteilung, für \(n-1\gt30\) fast gleich. Alternativ mit \(S\): \(\bar x\pm t\cdot\frac{S}{\sqrt{n-1}}\) (gleiches Ergebnis).`,tr:r`σ bilinmiyorsa z yerine t kullan, serbestlik derecesi n−1, s* ile (R'daki sd()).`},
{t:"formula",h:"KI für einen Anteil π (approximativ)",tex:r`\hat\pi\pm z_{1-\alpha/2}\sqrt{\frac{\hat\pi(1-\hat\pi)}{n}}`},
{t:"formula",h:"KI für die Varianz σ² (Normalverteilung)",tex:r`\Big[\frac{(n-1)s_*^2}{\chi^2_{n-1,\,1-\alpha/2}}\ ,\ \frac{(n-1)s_*^2}{\chi^2_{n-1,\,\alpha/2}}\Big]\qquad (n-1)s_*^2=nS^2`,note:r`Großes Quantil in den Nenner der <b>unteren</b> Grenze. Das Intervall ist nicht symmetrisch.`,tr:r`Varyans için χ² kullanılır; alt sınırın paydasında BÜYÜK quantil var.`},
{t:"rule",de:r`Welche Formel? <b>Anteil</b> → \(\hat\pi\)-Formel. <b>Varianz</b> → \(\chi^2\). <b>Mittelwert</b>: σ gegeben → \(z\); σ aus der Stichprobe geschätzt → \(t_{n-1}\).`,tr:r`Oran → π̂ formülü; varyans → χ²; ortalama: σ verilmişse z, örnekten tahmin ediliyorsa t.`},
{t:"ex",h:"Glühbirnen (V10)",q:r`\(n=30\), \(\bar x=1092.9\), \(s_*=206.12\), Normalverteilung angenommen. 90 %-KI für \(\mu\)?`,
steps:[r`σ unbekannt → \(t\). \(1-\alpha=0.9\Rightarrow1-\frac\alpha2=0.95\). \(t_{29,0.95}=1.70\).`,r`Halbe Breite: \(1.70\cdot\frac{206.12}{\sqrt{30}}=1.70\cdot37.632=63.97\).`,r`\([1092.9-63.97,\ 1092.9+63.97]\).`],a:r`90 %-KI ≈ [1028.9, 1156.9]; 99 %-KI mit \(t_{29,0.995}=2.756\): [989.2, 1196.6] — breiter.`},
{t:"num",q:r`Tutorium 10, Aufgabe 1: 11 Werte, <code>sum(x_i)</code> = 37.95, <code>var(x_i)</code> = 8.07786. 90 %-KI für \(\mu\) per Hand (\(t_{10,0.95}=1.8125\)).`,f:[{l:"Untergrenze =",a:1.896825,tol:.002},{l:"Obergrenze =",a:5.003175,tol:.002}],why:r`\(\bar x=3.45\). R's <code>var()</code> ist schon \(s_*^2\) → \(s_*=2.8422\). \(3.45\pm1.8125\cdot\frac{2.8422}{\sqrt{11}}=3.45\pm1.5532\) → [1.897, 5.003].`},
{t:"num",q:r`Kaffeebohnen (Testat 6, Aufgabe 1): 80 von 100 perfekt. 95 %-KI für den Anteil, <b>4 Nachkommastellen</b>.`,f:[{l:"Untergrenze =",a:.7216,tol:.00006},{l:"Obergrenze =",a:.8784,tol:.00006}],why:r`\(\hat\pi=0.8\), \(\sqrt{0.8\cdot0.2/100}=0.04\), \(1.96\cdot0.04=0.0784\). R-Befehl obere Grenze: <code>0.8 + qnorm(0.975) * sqrt(0.8*0.2/100)</code>.`},
{t:"num",q:r`Koffein (Testat 6, Aufgabe 2): \(n=30\), <code>var(koffeinwerte)*29</code> = 27.91232. Quantile für df = 29: 0.025 → 16.05, 0.05 → 17.71, 0.95 → 42.56, 0.975 → 45.72. 95 %-KI für \(\sigma^2\)?`,f:[{l:"Untergrenze =",a:27.91232/45.72,tol:.0006},{l:"Obergrenze =",a:27.91232/16.05,tol:.0006}],why:r`\((n-1)s_*^2=27.91232\), df \(=n-1=29\) (die Zeile mit df = 30 ist die Falle!). \(\big[\frac{27.91232}{45.72},\frac{27.91232}{16.05}\big]=[0.611,\ 1.739]\).`},
{t:"num",q:r`Rückwärts (Testat 6, Aufgabe 3): Jemand hat <code>c(3 - 2*qnorm(0.995)/sqrt(100), 3 + 2*qnorm(0.995)/sqrt(100))</code> getippt. Stichprobenmittel, Signifikanzniveau α und Stichprobengröße?`,f:[{l:"x̄ =",a:3,tol:0},{l:"α =",a:.01,tol:0},{l:"n =",a:100,tol:0}],why:r`Form \(\bar x\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}\): \(\bar x=3\), \(\sigma=2\), \(1-\alpha/2=0.995\Rightarrow\alpha=0.01\) (99 %-KI), \(n=100\).`},
{t:"num",q:r`Mate (Testat 6, Aufgabe 4): \(n=15\), \(\bar x=180.5\), \(s_*^2=49\). R-Output: <code>round(qt(c(0.9,0.925,0.95,0.975),15),3)</code> = 1.341 1.517 1.753 2.131 und mit df = 14: 1.345 1.523 1.761 2.145. 95 %-KI für \(\mu\)?`,f:[{l:"Untergrenze =",a:176.623144,tol:.002},{l:"Obergrenze =",a:184.376856,tol:.002}],why:r`df = 14, Quantil 0.975 → 2.145. \(s_*=7\). \(180.5\pm2.145\cdot\frac{7}{\sqrt{15}}=180.5\pm3.877\) → [176.623, 184.377].`},
{t:"num",q:r`Tutorium 10, Aufgabe 4: \(\sigma^2=100\) bekannt, \(\bar x=78.696\), 90 %-KI-Breite \(=3.6781\), \(z_{0.95}=1.6449\). Bestimme \(n\) und die Obergrenze.`,f:[{l:"n =",a:80,tol:0},{l:"Obergrenze =",a:80.535,tol:.002}],why:r`Breite \(=2\cdot1.6449\cdot\frac{10}{\sqrt n}=3.6781\Rightarrow\sqrt n=8.9443\Rightarrow n=80\). Obergrenze \(78.696+\frac{3.6781}{2}=80.535\).`},
{t:"idea",h:"Was macht das KI breiter?",de:r`<ul><li>größeres \(\sigma\) → breiter</li><li>größeres Niveau \(1-\alpha\) → breiter (für \(1-\alpha\to1\) wird es unendlich breit)</li><li>größeres \(n\) → schmaler</li><li>σ unbekannt (t statt z) → tendenziell breiter; bei bekanntem σ sind alle Intervalle gleich lang</li></ul><p>Tutorium 10, Aufgabe 5 (b): Ein Intervall ist breiter als das 98 %-KI → es muss das 99 %-KI sein.</p>`},
{t:"r",h:"KI in R",code:r`
alpha <- 0.1; n <- length(x)
mean(x) + c(-1, 1) * qnorm(1 - alpha/2) * sigma / sqrt(n)     # sigma bekannt
mean(x) + c(-1, 1) * qt(1 - alpha/2, n - 1) * sd(x) / sqrt(n) # sigma unbekannt
t.test(x, conf.level = 0.9)$conf.int                          # dasselbe
(n - 1) * var(x) / qchisq(c(1 - alpha/2, alpha/2), n - 1)     # KI Varianz
p <- 80/100; p + c(-1, 1) * qnorm(0.975) * sqrt(p * (1 - p) / 100)`,
notes:[[3,"<code>qt(p, df)</code>: Quantil der t-Verteilung.",""],[4,"<code>t.test()</code> liefert direkt das KI bei unbekannter Varianz.","t.test σ bilinmiyorken KI verir."],[5,"Achtung Reihenfolge: das große Quantil \\(1-\\alpha/2\\) zuerst → untere Grenze.",""]]},
{t:"trap",items:[r`\(\sigma^2\) statt \(\sigma\) in die Formel (Tutorium 10: häufigster Fehler).`,r`\(t_{n}\) statt \(t_{n-1}\) — bzw. \(\chi^2_{n}\) statt \(\chi^2_{n-1}\).`,r`\(z_{1-\alpha}\) statt \(z_{1-\alpha/2}\) beim zweiseitigen KI.`,r`Für den Varianz-KI die Grenzen vertauscht (untere Grenze &gt; obere).`,r`Interpretation „mit 95 % liegt μ im Intervall“ — besser: „das Verfahren überdeckt μ in 95 % der Wiederholungen“.`]}
]});

L({id:"4.7",day:4,no:7,title:"ML numerisch in R (B-Teil)",min:60,rel:3,
src:["ML-Probeklausur B (Lungenvolumen)","Tutorium 8, Aufgabe 3","R-Skript 08"],
goal:"Du schreibst eine negative Log-Likelihood-Funktion, optimierst sie mit optimize() oder nlm(), transformierst positive Parameter mit exp/log und nutzt die geschätzte Verteilung für Wahrscheinlichkeiten und Quantile.",
blocks:[
{t:"idea",h:"Warum numerisch?",de:r`<p>Nicht jede Likelihood lässt sich per Hand ableiten (z. B. Gamma-Verteilung mit zwei Parametern). R sucht das Optimum dann numerisch. Zwei Werkzeuge:</p><ul><li><code>optimize(f, interval, maximum = TRUE)</code> — ein Parameter, in einem Intervall.</li><li><code>nlm(f, p)</code> — beliebig viele Parameter, <b>minimiert</b> immer, sucht in ganz \(\mathbb R\).</li></ul>`,tr:r`optimize: tek parametre, aralıkta. nlm: her zaman MİNİMİZE eder, bu yüzden negatif log-likelihood yazılır.`},
{t:"r",h:"Ein Parameter: optimize (Tutorium 8, Aufgabe 3)",code:r`
logL <- function(sigma) {
  f <- dnorm(logr, 0, sigma)     # Dichte jeder Beobachtung
  l <- sum(log(f))               # Log-Likelihood
  return(l)
}
max_l <- optimize(logL, c(0, 0.1), maximum = TRUE)
sigma_hat <- max_l$maximum
sigma_hat^2                      # geschätzte Varianz`,out:r`
[1] 0.0004957461`,notes:[[6,"Standard ist Minimieren → <code>maximum = TRUE</code> für die Log-Likelihood. Das Ergebnis steht in <code>$maximum</code>.","optimize varsayılan olarak minimize eder; maximum=TRUE ekle."],[8,"<code>dnorm</code> braucht σ — gefragt war aber σ² → quadrieren.",""]]},
{t:"idea",h:"Das Problem mit restringierten Parametern",de:r`<p>Gamma-Verteilung: \(\alpha\gt0\), \(\beta\gt0\). <code>nlm</code> probiert aber auch negative Werte → <code>dgamma</code> liefert NaN → Fehler. Lösung: <b>transformieren</b>. Wir optimieren über \(\alpha_t=\log\alpha\in\mathbb R\) und rechnen innen zurück: \(\alpha=\exp(\alpha_t)\gt0\).</p>
<p>Musterantwort (g): „Die Parameter sind auf die positiven reellen Zahlen restringiert. nlm sucht im gesamten Raum der reellen Zahlen; bei negativen Werten liefert R Fehler bzw. NaNs. Daher transformieren wir die Parameter.“</p>`,tr:r`Pozitif olması gereken parametreleri log ile tüm reel sayılara taşı, fonksiyonun içinde exp ile geri çevir.`},
{t:"r",h:"Zwei Parameter: nlm mit Transformation (ML-Probeklausur B, h–m)",file:"Lungenvolumen.csv",code:r`
x <- df$Lungenvolumen
neglogL <- function(transformed_param, x) {
  param <- exp(transformed_param)          # zurück in den positiven Bereich
  alpha <- param[1]
  beta  <- param[2]
  logLi <- log(dgamma(x, alpha, beta))     # individuelle Log-Likelihoods
  logL  <- sum(logLi)
  neglogL <- -logL                          # nlm minimiert
  return(neglogL)
}
model <- nlm(neglogL, c(0.01, 0.5), x)      # Startwerte (transformiert)
alpha.hat <- exp(model$estimate[1])
beta.hat  <- exp(model$estimate[2])
alpha.hat; beta.hat
hist(x, freq = FALSE, xlab = "Lungenvolumen", ylab = "Wahrscheinlichkeitsdichte",
     main = "Grafik Aufgabenteil k)", ylim = c(0, 0.4))
x.seq <- seq(0, 8, by = 0.01)
lines(x.seq, dgamma(x.seq, alpha.hat, beta.hat), col = 2)
pgamma(3, alpha.hat, beta.hat)             # P(X <= 3)
qgamma(0.75, alpha.hat, beta.hat)          # ab hier: obere 25 %`,
out:r`
[1] 2.116   (alpha.hat)
[1] 1.090   (beta.hat)
[1] 0.818
[1] 2.603`,
notes:[[3,"<code>exp()</code> macht aus jeder reellen Zahl eine positive.","exp her reel sayıyı pozitif yapar."],[6,"Wie in der Musterlösung: dritter Parameter von <code>dgamma</code> positional. (R interpretiert ihn als <i>rate</i> — für die Klausur zählt der Code der Musterlösung.)",""],[8,"Vorzeichen umdrehen, weil <code>nlm</code> minimiert.",""],[11,"Startwerte sind die <b>transformierten</b> Werte \\(\\alpha_t=0.01\\), \\(\\beta_t=0.5\\). Das dritte Argument wird an die Funktion weitergereicht.",""],[12,"Rücktransformation mit <code>exp()</code> — sonst sind die Schätzer falsch.",""],[19,"„Wahrscheinlichkeit für höchstens 3 Liter“ → Verteilungsfunktion.",""],[20,"„ab welchem Wert gehört man zu den 25 % mit dem größten Volumen“ → 75 %-Quantil.",""]]},
{t:"mc",q:r`Welche Transformation macht einen Parameter \(\beta\gt0\) für nlm geeignet?`,o:[r`\(\beta_t=\log\beta\), innen \(\beta=\exp(\beta_t)\)`,r`\(\beta_t=\beta^2\), innen \(\beta=\sqrt{\beta_t}\)`,r`\(\beta_t=-\beta\)`],k:0,why:r`\(\log\) bildet \((0,\infty)\) auf ganz \(\mathbb R\) ab, \(\exp\) zurück. (\(\sqrt{\beta_t}\) wäre für negative \(\beta_t\) nicht definiert.)`},
{t:"trap",items:[r`<code>nlm</code> mit positiver Log-Likelihood aufgerufen → sucht das Minimum statt Maximum.`,r`Rücktransformation vergessen: <code>model$estimate</code> sind die <b>transformierten</b> Werte.`,r`<code>optimize</code> ohne <code>maximum = TRUE</code>.`,r`Bei \(P(X\le3)\) <code>dgamma</code> statt <code>pgamma</code> verwendet.`]}
]});
