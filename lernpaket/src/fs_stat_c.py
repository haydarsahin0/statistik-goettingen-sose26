"""Formelsammlung Statistik – Abschnitte 10–15 (Schätzer, ML, KI, Tests, Regression, Anhang)."""
from scipy.stats import norm, t as tdist, chi2
from fs_stat_doc import D

# =====================================================================
D.S("10", "Schätzer und ihre Güte, Dichteschätzung (V09)",
    "Probeklausur 2022'de 5 puan: „Schätzer unverzerrt mi?“ Beklenen değer kurallarıyla (8.9) çözülür.")

D.E("10.1", "Begriffe: Schätzer, Bias, erwartungstreu",
    sig="„Schätzer“, „unverzerrt“, „erwartungstreu“, „Bias“, „verzerrt“",
    ne="Tahminci = örneklemin bir fonksiyonu, kendisi de rastgele değişken. Bias = E(tahminci) − gerçek parametre. Bias = 0 → erwartungstreu.",
    fm=r"\[Bias(\hat\vartheta)=E(\hat\vartheta)-\vartheta\qquad\text{erwartungstreu (unverzerrt)}\iff E(\hat\vartheta)=\vartheta\qquad\text{asymptotisch erwartungstreu: }Bias\to0\ (n\to\infty)\]")

D.E("10.2", "Erwartungstreue prüfen (Rezept)",
    sig="„Testen Sie, ob der Schätzer … ein unverzerrter Schätzer für α ist“",
    ne="Tahmincinin beklentisini hesapla: E'yi toplamların içine dağıt, sabitleri dışarı al, E(X<sub>i</sub>) yerine ver. Sonuç parametreye eşit mi?",
    fm=r"\[E\Big(\sum a_iX_i+b\Big)=\sum a_iE(X_i)+b\qquad E(\bar X)=\mu\qquad E(X_iX_j)=E(X_i)E(X_j)\ (i\ne j,\ \text{unabh.})\qquad E(X_i^2)=Var(X_i)+E(X_i)^2\]",
    st=["Schätzer erst vereinfachen (Brüche kürzen, Produkte kürzen: \\(\\frac{\\prod_{i=2}^{n-1}X_i}{\\prod_{i=1}^{n-1}X_i}=\\frac1{X_1}\\)).",
        "E auf jeden Summanden anwenden, Konstanten herausziehen.", "\\(E(X_i)\\) aus der Aufgabe einsetzen (z. B. \\(\\frac\\alpha4\\)).",
        "Vergleichen: = Parameter → erwartungstreu; sonst Bias angeben."],
    bsp=r"\(E(X)=\frac\theta2\): \(\hat\theta_1=2\bar X\) → \(E=2\cdot\frac\theta2=\theta\) erwartungstreu · \(\hat\theta_2=\bar X+1\) → \(E=\frac\theta2+1\), \(Bias=1-\frac\theta2\) · \(\hat\mu=\frac{X_1+3X_2}{4}\) → \(E=\frac{\mu+3\mu}4=\mu\)",
    fa="\\(E\\left(\\frac1X\\right)\\ne\\frac1{E(X)}\\) und \\(E(X^2)\\ne E(X)^2\\) im Allgemeinen (die Probeklausur-Lösung 2022 benutzt in A7 trotzdem \\(\\frac1{E(X)}\\)).",
    ks="„Da \\(E(\\hat\\theta)=\\theta\\) für alle θ gilt, ist \\(\\hat\\theta\\) ein unverzerrter Schätzer für θ.“")

D.E("10.3", "Varianz eines Schätzers",
    sig="„Bestimmen Sie \\(Var(\\hat\\vartheta)\\)“",
    ne="Bağımsız X<sub>i</sub>'ler için: katsayıların karesi × varyans, topla. Sabitler varyansa katkı vermez.",
    fm=r"\[Var\Big(\sum a_iX_i+b\Big)=\sum a_i^2\,Var(X_i)\ \text{(unabh.)}\qquad Var(\bar X)=\frac{\sigma^2}{n}\qquad Var(c\bar X)=c^2\frac{\sigma^2}n\]",
    bsp=r"\(Var(2\bar X)=\frac{4\sigma^2}n\) · \(Var\left(\frac{X_1+3X_2}4\right)=\frac{1+9}{16}\sigma^2=0.625\,\sigma^2\)",
    fa="Falls nur \\(E(X_i^2)\\) gegeben ist: zuerst \\(Var(X_i)=E(X_i^2)-E(X_i)^2\\).")

D.E("10.4", "MSE, Effizienz, Konsistenz – Schätzer vergleichen",
    sig="„Welcher Schätzer ist vorzuziehen?“, „konsistent“, „MSE“, „effizienter“",
    ne="MSE = Bias² + Varyans (küçük olan iyi). İkisi de yansızsa varyansı küçük olan daha etkin. Tutarlı: n→∞ iken MSE→0.",
    fm=r"\[MSE(\hat\vartheta)=E\big[(\hat\vartheta-\vartheta)^2\big]=Bias^2+Var(\hat\vartheta)\qquad\text{konsistent: }MSE\to0\ \text{für }n\to\infty\]",
    bsp=r"A: Bias 0, Var 4 → MSE 4; B: Bias 1, Var 2 → MSE 3 → B besser (obwohl verzerrt) · \(\bar X\): MSE \(=\frac{\sigma^2}n\to0\) konsistent; \(\frac{X_1+X_2}2\): MSE \(=\frac{\sigma^2}2\) hängt nicht von n ab → nicht konsistent",
    fa="„Ein erwartungstreuer Schätzer hat immer den kleineren MSE“ ist falsch.")

D.E("10.5", "Kerndichteschätzer an einer Stelle berechnen",
    sig="„Berechnen Sie den Kerndichteschätzer an der Stelle x mit Rechteckkern/Epanechnikov-Kern und Bandweite b“",
    ne="Her gözlem için u = (x − x<sub>i</sub>)/b; −1 ≤ u < 1 ise çekirdek değeri, değilse 0. Topla, n·b'ye böl.",
    fm=r"\[\hat f(x)=\frac1{n\,b}\sum_{i=1}^n K\!\left(\frac{x-x_i}{b}\right)\qquad\text{Rechteck: }K(u)=\tfrac12\qquad\text{Epanechnikov: }K(u)=\tfrac34(1-u^2)\qquad(-1\le u<1,\ \text{sonst }0)\]",
    st=["Für jedes \\(x_i\\): \\(u_i=(x-x_i)/b\\).", "Nur \\(-1\\le u_i&lt;1\\) zählt; Kern einsetzen.", "Summe durch \\(n\\cdot b\\)."],
    bsp=r"Daten 1, 2, 2.5, 4; x = 2; b = 1: \(u=1,\ 0,\ -0.5,\ -2\) · Rechteck: \(\frac{0.5+0.5}{4}=0.25\) (u = 1 zählt nicht) · Epanechnikov: \(\frac{0.75+0.5625}{4}=0.328\)",
    fa="Größere Bandweite → glattere Schätzung (Details verschwinden); kleinere → zackig. Der Kern aus der Aufgabe (Grenzen!) gilt.")

D.E("10.6", "Bias-Varianz bei Histogramm/KDE, Eigenschaften von ML-Schätzern",
    sig="„Approximationsfehler“, „Schätzfehler“, „asymptotisch …“, „wie viele Parameter hat ein Histogramm?“",
    ne="Daha çok parametre (sınıf / küçük bant genişliği): yaklaşım hatası ↓, tahmin hatası ↑. Daha çok veri: tahmin hatası ↓.",
    st=["Histogramm mit J Klassen: J − 1 freie Parameter (Fläche muss 1 sein).",
        "Mehr Klassen / kleinere Bandweite: Approximationsfehler ↓, Schätzfehler ↑. Größeres n: Schätzfehler ↓.",
        "ML-Schätzer sind (unter Annahmen) <b>asymptotisch erwartungstreu</b>, <b>konsistent</b> und <b>asymptotisch normalverteilt</b> – aber nicht immer erwartungstreu."])

# =====================================================================
D.S("11", "Maximum-Likelihood-Schätzung per Hand (V08)",
    "Her sınavda ~10 puan, reçete hep aynı. Takıldığında 0.2 (log kuralları) ve 0.4 (türev) bölümlerine bak.")

D.E("11.1", "Grundrezept (6 Schritte)",
    sig="„Stellen Sie die (Log-)Likelihood auf“, „Bestimmen Sie den ML-Schätzer“, „Bedingung zweiter Ordnung“",
    ne="Gözlenen verinin en olası olduğu parametreyi bul: L → log L → türev → 0'a eşitle → çöz → (ikinci türev < 0).",
    fm=r"\[L(\vartheta)=\prod_{i=1}^n f(x_i;\vartheta)\ \text{bzw.}\ \prod P(X=x_i)\qquad\ell(\vartheta)=\log L(\vartheta)=\sum_{i=1}^n\log f(x_i;\vartheta)\qquad\ell'(\hat\vartheta)\overset!=0\qquad\ell''(\hat\vartheta)<0\]",
    st=["<b>Likelihood</b>: Dichte/Wahrscheinlichkeitsfunktion mit \\(x_i\\) aufschreiben und das Produkt bilden; vereinfachen (0.3: \\(\\prod c=c^n\\), \\(\\prod a^{x_i}=a^{\\sum x_i}\\)).",
        "<b>Log-Likelihood</b>: log anwenden → Produkt wird Summe (0.2). So weit wie möglich vereinfachen.",
        "<b>Ableiten</b> nach dem Parameter (0.4); Terme ohne Parameter fallen weg.",
        "<b>Null setzen</b> und nach dem Parameter auflösen → \\(\\hat\\vartheta\\) (mit Dach!). Möglichst mit \\(\\bar x\\) schreiben.",
        "<b>2. Ableitung</b> bilden; < 0 → Maximum.",
        "Falls Zahlen gegeben: einsetzen (ln!)."],
    fa="Reihenfolge (Testat 5): Modell wählen → Likelihood → Log-Likelihood → ableiten und null setzen → auflösen → Maximum prüfen.")

D.E("11.2", "Likelihood für eine konkrete Stichprobe",
    sig="„Beobachtet wurden 2, 0, 3, 1. Stellen Sie die Likelihood auf“",
    ne="Her gözlem için olasılığı yaz, çarp, aynı tabanlı kuvvetleri topla.",
    bsp=r"Poisson, Daten 2, 0, 3, 1: \(L(\lambda)=\frac{\lambda^2e^{-\lambda}}{2!}\cdot\frac{\lambda^0e^{-\lambda}}{0!}\cdot\frac{\lambda^3e^{-\lambda}}{3!}\cdot\frac{\lambda^1e^{-\lambda}}{1!}=\frac{\lambda^6e^{-4\lambda}}{12}\) · \(\ell=6\log\lambda-4\lambda-\log12\) · \(\ell'=\frac6\lambda-4=0\Rightarrow\hat\lambda=1.5\)",
    fa="Geometrisch mit 3, 0, 5, 2: \\(L(p)=p^4(1-p)^{10}\\) – Exponent von \\((1-p)\\) ist die Summe der Daten.")

D.E("11.3", "ML: Poissonverteilung",
    sig="\\(X_i\\sim Po(\\lambda)\\), Anzahlen",
    ne="Sonuç: \\(\\hat\\lambda=\\bar x\\).",
    fm=r"\[L(\lambda)=\prod\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}=\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}\qquad\ell(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log(x_i!)\]"
       r"\[\ell'(\lambda)=\frac{\sum x_i}{\lambda}-n\overset!=0\ \Rightarrow\ \hat\lambda=\frac{\sum x_i}{n}=\bar x\qquad\ell''(\lambda)=-\frac{\sum x_i}{\lambda^2}<0\]")

D.E("11.4", "ML: Bernoulli und Binomial (Anteil)",
    sig="„6 von 20 Würfen“, Anteilswert π, \\(X_i\\sim Be(\\pi)\\)",
    ne="Sonuç: \\(\\hat\\pi\\) = başarı sayısı / deneme sayısı = \\(\\bar x\\).",
    fm=r"\[L(\pi)=\pi^{k}(1-\pi)^{n-k}\ (k=\textstyle\sum x_i)\qquad\ell'(\pi)=\frac k\pi-\frac{n-k}{1-\pi}\overset!=0\Rightarrow\hat\pi=\frac kn=\bar x\qquad\ell''=-\frac k{\pi^2}-\frac{n-k}{(1-\pi)^2}<0\]",
    bsp=r"6 von 20: \(\hat\pi=0.3\) · Binomial \(B(m,\pi)\) mit bekanntem m, n Beobachtungen: \(\hat\pi=\frac{\sum x_i}{n\,m}=\frac{\bar x}{m}\)",
    fa="Beim Auflösen über Kreuz multiplizieren: \\(k(1-\\hat\\pi)=(n-k)\\hat\\pi\\).")

D.E("11.5", "ML: Exponentialverteilung (= Weibull mit r = 1)",
    sig="\\(f(x)=\\lambda e^{-\\lambda x}\\), Wartezeiten, „Weibull … r = 1“",
    ne="Sonuç: \\(\\hat\\lambda=1/\\bar x\\).",
    fm=r"\[L(\lambda)=\lambda^n e^{-\lambda\sum x_i}\qquad\ell(\lambda)=n\log\lambda-\lambda\sum x_i\qquad\ell'=\frac n\lambda-\sum x_i\overset!=0\Rightarrow\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}\qquad\ell''=-\frac n{\lambda^2}<0\]",
    fa="Weibull mit r = 1: \\(f=1\\cdot\\lambda(\\lambda x)^0e^{-\\lambda x}=\\lambda e^{-\\lambda x}\\) – erst r einsetzen, dann rechnen.")

D.E("11.6", "ML: geometrische Verteilung",
    sig="\\(P(X=x)=\\theta(1-\\theta)^x\\), x = 0, 1, 2, …",
    ne="Sonuç: \\(\\hat\\theta=1/(1+\\bar x)\\).",
    fm=r"\[L(\theta)=\theta^n(1-\theta)^{\sum x_i}\qquad\ell=n\log\theta+\sum x_i\log(1-\theta)\qquad\ell'=\frac n\theta-\frac{\sum x_i}{1-\theta}\overset!=0\Rightarrow\hat\theta=\frac n{n+\sum x_i}=\frac1{1+\bar x}\]",
    bsp=r"Daten 3, 0, 5, 2 (\(\bar x=2.5\)): \(\hat\theta=\frac1{3.5}=\frac27=0.286\)")

D.E("11.7", "ML: Normalverteilung (μ bzw. σ²)",
    sig="\\(N(\\mu,\\sigma^2)\\) mit bekanntem σ bzw. bekanntem μ, Log-Normal",
    ne="\\(\\hat\\mu=\\bar x\\) · σ² için (μ biliniyorsa): \\(\\hat\\sigma^2=\\frac1n\\sum(x_i-\\mu)^2\\). Log-normalde x yerine log x.",
    fm=r"\[\ell(\mu)=-n\log(\sqrt{2\pi}\sigma)-\frac1{2\sigma^2}\sum(x_i-\mu)^2\qquad\ell'(\mu)=\frac1{\sigma^2}\sum(x_i-\mu)\overset!=0\Rightarrow\hat\mu=\bar x\]"
       r"\[\text{μ bekannt, }v=\sigma^2:\ \ \ell'(v)=-\frac n{2v}+\frac{\sum(x_i-\mu)^2}{2v^2}\overset!=0\Rightarrow\hat\sigma^2=\frac1n\sum(x_i-\mu)^2\qquad\text{Log-Normal: }\hat\mu=\frac1n\sum\log x_i\]",
    bsp=r"Log-Normal mit Daten 1, e, e²: \(\hat\mu=\frac{0+1+2}3=1\)")

D.E("11.8", "ML: spezielle Dichten (Übungsklausur-Typen)",
    sig="ungewöhnliche Dichte mit Parameter, z. B. \\((b+1)x^b\\), \\(\\theta^2xe^{-\\theta x}\\), \\(\\frac{\\beta\\log2}{2^{x\\beta}}\\)",
    ne="Reçete aynı (11.1). Parametre üsteyse log onu öne indirir: log(x<sup>b</sup>) = b·log x.",
    extra=("<table class='t'><tr><th>Dichte</th><th>Log-Likelihood</th><th>ML-Schätzer</th></tr>"
           "<tr><td>\\((b+1)x^b,\\ 0&lt;x&lt;1\\)</td><td>\\(n\\log(b+1)+b\\sum\\log x_i\\)</td><td>\\(\\hat b=-1-\\frac{n}{\\sum\\log x_i}\\)</td></tr>"
           "<tr><td>\\(\\theta^2x\\,e^{-\\theta x},\\ x&gt;0\\)</td><td>\\(2n\\log\\theta+\\sum\\log x_i-\\theta\\sum x_i\\)</td><td>\\(\\hat\\theta=\\frac{2n}{\\sum x_i}=\\frac2{\\bar x}\\)</td></tr>"
           "<tr><td>\\(\\frac{\\beta\\log2}{2^{x\\beta}},\\ x\\ge0\\)</td><td>\\(n\\log(\\log2)+n\\log\\beta-\\beta\\log2\\sum x_i\\)</td><td>\\(\\hat\\beta=\\frac1{\\log(2)\\,\\bar x}\\)</td></tr></table>"),
    bsp=r"\((b+1)x^b\) mit Daten 0.5, 0.8, 0.9, 0.6: \(\sum\log x_i=-0.6931-0.2231-0.1054-0.5108=-1.5325\) → \(\hat b=-1+\frac4{1.5325}=1.610\)",
    fa="Terme ohne Parameter (\\(\\sum\\log x_i\\) bei \\(\\theta^2xe^{-\\theta x}\\)) beim Ableiten weglassen, aber in der Log-Likelihood hinschreiben.")

D.E("11.9", "ML aus einer Wahrscheinlichkeitstabelle",
    sig="„\\(P(X=1)=\\alpha,\\ P(X=2)=\\alpha^2,\\dots\\)“ und konkrete Beobachtungen",
    ne="Her gözlem için tablodaki olasılığı yaz, çarp, log al, türev → çoğu zaman ikinci derece denklem.",
    bsp=r"\(P(1)=\alpha,\ P(2)=\alpha^2,\ P(3)=1-\alpha-\alpha^2\); Daten 1, 3, 2, 1: \(L=\alpha^4(1-\alpha-\alpha^2)\) → \(\frac4\alpha=\frac{1+2\alpha}{1-\alpha-\alpha^2}\) → \(6\alpha^2+5\alpha-4=0\) → \(\alpha=\frac{-5\pm11}{12}\) → \(\hat\alpha=0.5\)",
    fa="Lösungen außerhalb des erlaubten Bereichs (negative Wahrscheinlichkeit) verwerfen und das begründen.")

D.E("11.10", "Typische ML-Fehler",
    sig="Kontrolle vor dem Abgeben",
    ne="En sık puan kaybettiren hatalar.",
    st=["\\(\\prod\\lambda=\\lambda^n\\) (nicht \\(n\\lambda\\)); \\(\\log(\\lambda^n)=n\\log\\lambda\\).",
        "Nach dem <b>Parameter</b> ableiten, nicht nach x.",
        "Dach \\(\\hat{\\ }\\) beim Ergebnis nicht vergessen; Ergebnis mit \\(\\bar x\\) vereinfachen.",
        "2. Ableitung: Vorzeichen begründen („da n > 0 und θ² > 0“).",
        "Zahlen: ln benutzen, nicht log₁₀."])

# =====================================================================
D.S("12", "Konfidenzintervalle (V10)",
    "Formül tablodan seçilir: ortalama mı (σ biliniyor mu?), oran mı, varyans mı?")

D.E("12.1", "Idee und richtige Interpretation",
    sig="„Welche Aussagen sind richtig?“, „Interpretieren Sie das Konfidenzintervall“",
    ne="Aralığın sınırları rastgele, parametre sabit. Doğru yorum: çok tekrarda aralıkların %95'i gerçek değeri kapsar.",
    st=["Richtig: „Bei vielen Wiederholungen überdecken etwa 95 % der so konstruierten Intervalle den wahren Parameter.“",
        "Falsch: „μ liegt mit 95 % Wahrscheinlichkeit in [176.6; 184.4]“ (nach der Berechnung ist μ drin oder nicht).",
        "Größeres n → schmaler · höheres Niveau (99 %) → breiter · größeres σ → breiter. Doppelte Genauigkeit braucht vierfaches n.",
        "Zusammenhang mit Tests: Wert außerhalb des (1 − α)-KI → zweiseitiger Test zum Niveau α verwirft \\(H_0\\)."])

D.E("12.2", "KI für μ, σ bekannt (oder n groß)",
    sig="„Varianz bekannt“, „σ = …“, Normalverteilung",
    ne="\\(\\bar x\\pm z\\cdot\\sigma/\\sqrt n\\), z = z<sub>1−α/2</sub> (95 % → 1.96).",
    fm=r"\[\left[\bar x-z_{1-\alpha/2}\frac{\sigma}{\sqrt n};\ \ \bar x+z_{1-\alpha/2}\frac{\sigma}{\sqrt n}\right]\]",
    bsp=r"n = 25, \(\bar x=50\), σ = 10, 95 %: \(50\pm1.96\cdot\frac{10}{5}=50\pm3.92\) → \([46.08;\ 53.92]\)",
    fa="Quantil zweiseitig: \\(1-\\alpha/2\\) (95 % → 0.975 → 1.96), nicht 1.645.")

D.E("12.3", "KI für μ, σ unbekannt (t-Verteilung)",
    sig="„Varianz unbekannt“, nur \\(s\\) bzw. \\(s_*\\) aus der Stichprobe, qt(…) im R-Output",
    ne="σ yerine s*, z yerine t<sub>n−1; 1−α/2</sub>.",
    fm=r"\[\left[\bar x\pm t_{n-1;\,1-\alpha/2}\,\frac{s_*}{\sqrt n}\right]\qquad s_*=\sqrt{\frac1{n-1}\sum(x_i-\bar x)^2}\]",
    bsp=r"n = 16, \(\bar x=20\), \(s_*=4\), 95 %: \(t_{15;0.975}=2.131\) → \(20\pm2.131\cdot1\) → \([17.869;\ 22.131]\)",
    fa="Ist nur die empirische Varianz \\(s^2\\) (Nenner n) gegeben: \\(s_*^2=\\frac n{n-1}s^2\\).")

D.E("12.4", "KI für einen Anteilswert π",
    sig="„Von 200 Befragten …“, „Anteil“, „Prozent“",
    ne="\\(\\hat\\pi\\pm z\\sqrt{\\hat\\pi(1-\\hat\\pi)/n}\\).",
    fm=r"\[\left[\hat\pi\pm z_{1-\alpha/2}\sqrt{\frac{\hat\pi(1-\hat\pi)}{n}}\right]\qquad\hat\pi=\frac{\text{Anzahl}}{n}\]",
    bsp=r"60 von 200: \(\hat\pi=0.3\), \(\sqrt{0.3\cdot0.7/200}=0.0324\) → \(0.3\pm1.96\cdot0.0324\) → \([0.236;\ 0.364]\)")

D.E("12.5", "KI für die Varianz σ² (χ²-Verteilung)",
    sig="„Konfidenzintervall für die Varianz“, qchisq(…) im Output",
    ne="Pay (n−1)s*², paydada χ² kantilleri — <b>büyük kantil alt sınıra</b> gider.",
    fm=r"\[\left[\frac{(n-1)s_*^2}{\chi^2_{n-1;\,1-\alpha/2}};\ \ \frac{(n-1)s_*^2}{\chi^2_{n-1;\,\alpha/2}}\right]\qquad(n-1)s_*^2=n\,s^2\]",
    bsp=r"n = 10, \(s_*^2=4\), 95 %: \(\chi^2_{9;0.975}=19.023\), \(\chi^2_{9;0.025}=2.700\) → \(\left[\frac{36}{19.023};\ \frac{36}{2.700}\right]=[1.892;\ 13.331]\)",
    fa="Nicht symmetrisch um \\(s_*^2\\). Für die Standardabweichung: Wurzel aus beiden Grenzen.")

D.E("12.6", "Länge, nötiger Stichprobenumfang, Rückwärtsrechnen",
    sig="„Wie groß muss n sein, damit das KI höchstens … breit ist?“, „Was steckt in diesem R-Befehl?“",
    ne="Uzunluk L = 2·z·σ/√n → n'i çöz, <b>yukarı</b> yuvarla.",
    fm=r"\[L=2\,z_{1-\alpha/2}\frac{\sigma}{\sqrt n}\qquad n\ge\left(\frac{2\,z_{1-\alpha/2}\,\sigma}{L}\right)^2\]",
    bsp=r"σ = 10, 95 %, Länge höchstens 2: \(n\ge(19.6)^2=384.16\) → n = 385 · R-Befehl c(3 - 2*qnorm(0.995)/sqrt(100), …): \(\bar x=3\), Niveau 99 %, σ = 2, n = 100")

# =====================================================================
D.S("13", "Statistische Tests (V11–V12)",
    "Her test sorusunda aynı 5 adım (13.14). Önce doğru testi seç (13.13), sonra hipotezleri metinden kur (13.1).")

D.E("13.1", "Hypothesen aus dem Text aufstellen",
    sig="„statistisch absichern“, „nachweisen“, „Vermutung“, „Behauptung überprüfen“",
    ne="Kanıtlamak istediğin şey <b>H₁</b>'e gider. H₀ tersidir ve eşitliği içerir (=, ≤, ≥).",
    extra=("<table class='t'><tr><th>Text</th><th>\\(H_0\\)</th><th>\\(H_1\\)</th><th>Art</th></tr>"
           "<tr><td>„… ist größer als 500“ absichern</td><td>\\(\\mu\\le500\\)</td><td>\\(\\mu&gt;500\\)</td><td>rechtsseitig</td></tr>"
           "<tr><td>„zu wenig abgefüllt“ / „kleiner als“</td><td>\\(\\mu\\ge500\\)</td><td>\\(\\mu&lt;500\\)</td><td>linksseitig</td></tr>"
           "<tr><td>„weicht ab“, „ungleich“, „verändert“</td><td>\\(\\mu=500\\)</td><td>\\(\\mu\\ne500\\)</td><td>zweiseitig</td></tr>"
           "<tr><td>„springt nicht weiter als 133.5“ absichern</td><td>\\(\\mu\\ge133.5\\)</td><td>\\(\\mu&lt;133.5\\)</td><td>linksseitig</td></tr></table>"),
    fa="Behauptung des Herstellers („mindestens 500 g“) ist meist \\(H_0\\); die Vermutung des Prüfers („zu wenig“) ist \\(H_1\\).")

D.E("13.2", "Fehler 1. und 2. Art",
    sig="„Beschreiben Sie den Fehler 1./2. Art im Sachzusammenhang“",
    ne="1. tür hata: H₀ doğruyken reddetmek (olasılığı ≤ α). 2. tür: H₁ doğruyken H₀'ı reddetmemek (kontrol edilmez).",
    extra=("<table class='t c' style='width:auto'><tr><th></th><th>\\(H_0\\) wahr</th><th>\\(H_1\\) wahr</th></tr>"
           "<tr><th>\\(H_0\\) verworfen</th><td>Fehler 1. Art (α)</td><td>richtig</td></tr>"
           "<tr><th>\\(H_0\\) nicht verworfen</th><td>richtig</td><td>Fehler 2. Art (β)</td></tr></table>"),
    bsp="Rauchmelder, H₀: „es brennt nicht“: Fehler 1. Art = Fehlalarm; Fehler 2. Art = kein Alarm, obwohl es brennt. Kleineres α → mehr Fehler 2. Art.")

D.E("13.3", "Ablehnungsbereich bestimmen",
    sig="„Bestimmen Sie den Ablehnungsbereich“, „kritischer Wert“",
    ne="H₁ hangi yöndeyse ret bölgesi o kuyrukta. Çift yönlü: α/2 her iki tarafa.",
    extra=("<table class='t'><tr><th>unter \\(H_0\\)</th><th>linksseitig (\\(H_1\\): &lt;)</th><th>rechtsseitig (\\(H_1\\): &gt;)</th><th>zweiseitig (≠)</th></tr>"
           "<tr><td>N(0, 1)</td><td>\\((-\\infty;\\,-z_{1-\\alpha}]\\)</td><td>\\([z_{1-\\alpha};\\,\\infty)\\)</td><td>\\(|z|\\ge z_{1-\\alpha/2}\\)</td></tr>"
           "<tr><td>t(df)</td><td>\\((-\\infty;\\,-t_{df;1-\\alpha}]\\)</td><td>\\([t_{df;1-\\alpha};\\,\\infty)\\)</td><td>\\(|t|\\ge t_{df;1-\\alpha/2}\\)</td></tr>"
           "<tr><td>χ²(df)</td><td>\\([0;\\,\\chi^2_{df;\\alpha}]\\)</td><td>\\([\\chi^2_{df;1-\\alpha};\\,\\infty)\\)</td><td>\\([0;\\chi^2_{df;\\alpha/2}]\\cup[\\chi^2_{df;1-\\alpha/2};\\infty)\\)</td></tr></table>"),
    bsp="α = 5 %, Gauß-Test: linksseitig \\((-\\infty;-1.645]\\), rechtsseitig \\([1.645;\\infty)\\), zweiseitig \\(|z|\\ge1.96\\)")

D.E("13.4", "p-Wert berechnen und entscheiden",
    sig="„Berechnen Sie den p-Wert“, „Entscheiden Sie zu α = 1 %, 5 %, 10 %“",
    ne="p-değeri = H₀ altında gözlenen kadar veya daha uç sonuç alma olasılığı. <b>p ≤ α → H₀ reddedilir.</b>",
    fm=r"\[\text{links: }p=P(T\le t)\qquad\text{rechts: }p=P(T\ge t)=1-P(T\le t)\qquad\text{zweiseitig (symm.): }p=2\,P(T\ge|t|)\]",
    bsp=r"z = −1.629, linksseitig: \(p=\Phi(-1.629)=0.052\) → verwerfen nur für α = 10 % · p = 0.014: verwerfen für 5 % und 10 %, nicht für 1 %",
    ks="„Da der p-Wert 0.014 kleiner als α = 0.05 ist, wird H₀ verworfen; H₁ ist zum Niveau 5 % statistisch abgesichert.“")

D.E("13.5", "Gauß-Test (μ, σ bekannt)",
    sig="„Varianz bekannt“, „σ² = 16“, normalverteilte Messwerte",
    ne="\\(z=\\frac{\\bar x-\\mu_0}{\\sigma/\\sqrt n}\\), H₀ altında N(0,1).",
    fm=r"\[Z=\frac{\bar X-\mu_0}{\sigma/\sqrt n}=\frac{\bar X-\mu_0}{\sigma}\sqrt n\ \overset{H_0}{\sim}\ N(0,1)\]",
    bsp=r"\(H_0:\mu\le100\), \(H_1:\mu>100\), n = 36, \(\bar x=103\), σ = 9: \(z=\frac{3}{1.5}=2>1.645\) → \(H_0\) verwerfen · \(p=1-\Phi(2)=0.023\)",
    fa="σ = Wurzel aus der Varianz (σ² = 16 → σ = 4).")

D.E("13.6", "t-Test (μ, σ unbekannt)",
    sig="„Varianz unbekannt“, t.test-Output, „df = n − 1“",
    ne="Gauß testi gibi ama s* ve t<sub>n−1</sub> ile. R çıktısında: t, df, p-value.",
    fm=r"\[T=\frac{\bar X-\mu_0}{S_*/\sqrt n}\ \overset{H_0}{\sim}\ t(n-1)\]",
    bsp=r"\(H_0:\mu=50\), \(H_1:\mu\ne50\), n = 9, \(\bar x=52\), \(s_*=3\): \(t=\frac{2}{1}=2<t_{8;0.975}=2.306\) → \(H_0\) nicht verwerfen (p = 0.081)",
    extra=("<p class='small'><b>R-Output lesen:</b> <code>t.test(x, mu = 30, alternative = \"greater\")</code> → richtig bei \\(H_1:\\mu&gt;30\\); "
           "\"less\" bei \\(H_1:\\mu&lt;\\dots\\); ohne alternative = zweiseitig. Der Code mit der zu \\(H_1\\) passenden alternative und den richtigen Daten ist der richtige; dann p ≤ α prüfen.</p>"))

D.E("13.7", "Approximativer Binomialtest (Anteil, n groß)",
    sig="„Anteil“, „Prozent“, „Normalapproximation“, n groß",
    ne="X = başarı <b>sayısı</b> (oran değil!). z = (X − nπ₀)/√(nπ₀(1−π₀)).",
    fm=r"\[Z=\frac{X-n\pi_0}{\sqrt{n\pi_0(1-\pi_0)}}\ \overset{a}{\sim}\ N(0,1)\qquad\text{gleich: }\frac{\hat\pi-\pi_0}{\sqrt{\pi_0(1-\pi_0)/n}}\]",
    bsp=r"\(H_0:\pi\le0.5\), \(H_1:\pi>0.5\), n = 400, X = 220: \(z=\frac{220-200}{\sqrt{100}}=2>1.645\) → \(H_0\) verwerfen",
    fa="Im Nenner steht \\(\\pi_0\\) (aus \\(H_0\\)), nicht \\(\\hat\\pi\\) – anders als beim KI.")

D.E("13.8", "Exakter Binomialtest (n klein)",
    sig="kleines n, „Gegeben: \\(P(Z\\le4)=0.9672\\) für \\(Z\\sim B(10;0.2)\\)“",
    ne="Test istatistiği = başarı sayısı, H₀ altında B(n, π₀). p-değerini doğrudan binom olasılıklarıyla hesapla.",
    fm=r"\[Z=\text{Anzahl}\ \overset{H_0}{\sim}\ B(n,\pi_0)\qquad\text{rechtsseitig: }p=P(Z\ge z)=1-P(Z\le z-1)\]",
    bsp=r"\(H_0:\pi\le0.5\), \(H_1:\pi>0.5\), n = 8, z = 7: \(p=P(Z\ge7)=\frac{8+1}{256}=0.035\le0.05\) → \(H_0\) verwerfen",
    fa="„≥ 7“ = 1 − P(Z ≤ 6), nicht 1 − P(Z ≤ 7).")

D.E("13.9", "χ²-Varianztest",
    sig="„Streuung zu groß“, „Varianz größer als …“, Normalverteilung",
    ne="χ² = (n−1)s*²/σ₀², H₀ altında χ²(n−1).",
    fm=r"\[\chi^2=\frac{(n-1)S_*^2}{\sigma_0^2}=\frac{n\,S^2}{\sigma_0^2}\ \overset{H_0}{\sim}\ \chi^2(n-1)\]",
    bsp=r"\(H_0:\sigma^2\le4\), \(H_1:\sigma^2>4\), n = 11, \(s_*^2=6\): \(\chi^2=\frac{10\cdot6}{4}=15<\chi^2_{10;0.95}=18.307\) → nicht verwerfen",
    fa="Linksseitig: Ablehnung bei kleinen Werten \\([0;\\chi^2_{df;\\alpha}]\\).")

D.E("13.10", "Vorzeichentest (Median, ohne Verteilungsannahme)",
    sig="„ohne Verteilungsannahme“, „Median“, „\\(P(Z\\le3)\\) für \\(Z\\sim B(10;0.5)\\)“",
    ne="Z = θ₀'dan küçük-eşit gözlem sayısı, H₀ altında B(n; 0.5). Çift yönlüde p-değeri iki taraftan.",
    fm=r"\[Z=\#\{x_i\le\vartheta_0\}\ \overset{H_0}{\sim}\ B(n;\,0.5)\qquad\text{zweiseitig: }p=2\cdot\min\{P(Z\le z),\,P(Z\ge z)\}\]",
    bsp=r"n = 10, \(H_1:x_{med}\ne\vartheta_0\), z = 2: \(p=2\cdot P(Z\le2)=2\cdot\frac{1+10+45}{1024}=0.109>0.05\) → nicht verwerfen")

D.E("13.11", "χ²-Unabhängigkeitstest",
    sig="„Testen Sie, ob die Merkmale unabhängig sind“, Kontingenztafel",
    ne="5.3'teki χ² ile aynı hesap; df = (J−1)(K−1); her zaman sağ kuyruk.",
    fm=r"\[\chi^2=\sum_j\sum_k\frac{(h_{jk}-\tilde h_{jk})^2}{\tilde h_{jk}}\ \overset{H_0}{\sim}\ \chi^2\big((J-1)(K-1)\big),\qquad A=[\chi^2_{df;1-\alpha};\infty)\]",
    bsp=r"Tafel aus 5.1: \(\chi^2=1.587<\chi^2_{1;0.95}=3.841\) → \(H_0\) (Unabhängigkeit) nicht verwerfen",
    ks="„H₀: Geschlecht und Rauchen sind unabhängig. Da 1.587 < 3.841, wird H₀ nicht verworfen; ein Zusammenhang kann zum Niveau 5 % nicht nachgewiesen werden.“")

D.E("13.12", "χ²-Anpassungstest",
    sig="„Ist der Würfel fair?“, „passt die vorgegebene Verteilung?“",
    ne="Beklenen = n·π<sub>j</sub> (H₀'daki oranlarla). df = J − 1 (tahmin edilen parametre varsa onları da çıkar).",
    fm=r"\[\chi^2=\sum_{j=1}^J\frac{(h_j-n\pi_j)^2}{n\pi_j}\ \overset{H_0}{\sim}\ \chi^2(J-1)\]",
    bsp=r"\(H_0\): Anteile 50/30/20 %, n = 100, beobachtet 45, 35, 20: \(\chi^2=\frac{25}{50}+\frac{25}{30}+0=1.333<\chi^2_{2;0.95}=5.991\) → nicht verwerfen")

D.E("13.13", "Welcher Test passt? (Entscheidungstabelle)",
    sig="„Welcher Test ist geeignet?“, Zuordnungsaufgaben",
    ne="Ne test ediliyor? Ortalama → Gauß/t · oran → binom · varyans → χ² · iki kategorik → bağımsızlık · verilen dağılım → uyum · varsayımsız medyan → işaret testi.",
    extra=("<table class='t'><tr><th>Worum geht es?</th><th>Bedingung</th><th>Test</th><th>Rezept</th></tr>"
           "<tr><td>Mittelwert μ</td><td>σ bekannt</td><td>Gauß-Test</td><td>13.5</td></tr>"
           "<tr><td>Mittelwert μ</td><td>σ unbekannt</td><td>t-Test</td><td>13.6</td></tr>"
           "<tr><td>Anteil π</td><td>n groß</td><td>approx. Binomialtest</td><td>13.7</td></tr>"
           "<tr><td>Anteil π</td><td>n klein</td><td>exakter Binomialtest</td><td>13.8</td></tr>"
           "<tr><td>Varianz σ²</td><td>Normalverteilung</td><td>χ²-Varianztest</td><td>13.9</td></tr>"
           "<tr><td>Median</td><td>keine Verteilungsannahme</td><td>Vorzeichentest</td><td>13.10</td></tr>"
           "<tr><td>2 kategoriale Merkmale</td><td>Kontingenztafel</td><td>χ²-Unabhängigkeitstest</td><td>13.11</td></tr>"
           "<tr><td>vorgegebene Verteilung</td><td>Häufigkeiten je Kategorie</td><td>χ²-Anpassungstest</td><td>13.12</td></tr>"
           "<tr><td>Regressionskoeffizient β</td><td>lm-Output</td><td>t-Test (\\(H_0:\\beta=0\\))</td><td>14.4</td></tr></table>"))

D.E("13.14", "Antwortschema für jede Testaufgabe",
    sig="jede Aufgabe mit „Testen Sie …“",
    ne="Bu 5 adımı her zaman yaz; her biri puan getirir.",
    st=["\\(H_0\\) und \\(H_1\\) (13.1).", "Teststatistik: Formel + Zahlen + Ergebnis.", "Verteilung unter \\(H_0\\) mit Freiheitsgraden.",
        "Ablehnungsbereich (13.3) oder p-Wert (13.4).", "Entscheidung als Satz im Sachzusammenhang."],
    ks="„H₀ wird verworfen. Zum Signifikanzniveau 5 % ist statistisch abgesichert, dass … .“ bzw. „H₀ kann nicht verworfen werden; … kann nicht statistisch abgesichert werden.“ Nie: „H₀ ist bewiesen.“")

# =====================================================================
D.S("14", "Lineare Regression (V13)", "KQ doğrusu, yorum, tahmin, R² ve lm çıktısı.")

D.E("14.1", "KQ-Gerade per Hand",
    sig="„Bestimmen Sie die Regressionsgerade nach der Methode der kleinsten Quadrate“",
    ne="Eğim b = s<sub>xy</sub>/s<sub>x</sub>², kesişim \\(a=\\bar y-b\\,\\bar x\\).",
    fm=r"\[\hat\beta_1=b=\frac{s_{xy}}{s_x^2}=\frac{\sum x_iy_i-n\bar x\bar y}{\sum x_i^2-n\bar x^2}\qquad\hat\beta_0=a=\bar y-b\,\bar x\qquad\hat y=a+b\,x\]",
    bsp=r"x = 1, …, 5; y = 2, 4, 5, 4, 5: \(s_{xy}=1.2,\ s_x^2=2\) → \(b=0.6\), \(a=4-0.6\cdot3=2.2\) → \(\hat y=2.2+0.6x\)",
    fa="Zuerst b, dann a. \\(s_{xy}\\) und \\(s_x^2\\) mit demselben Nenner.")

D.E("14.2", "Interpretation, Prognose, Residuen",
    sig="„Interpretieren Sie \\(\\hat\\beta_1\\)“, „Welcher Wert wird für x = … prognostiziert?“, „Residuum“",
    ne="Eğim: x bir birim artınca y ortalama b birim değişir. Tahmin: x'i doğruya koy. Kalıntı = gözlenen − tahmin.",
    fm=r"\[\hat y_i=a+bx_i\qquad\hat\varepsilon_i=y_i-\hat y_i\qquad\sum\hat\varepsilon_i=0\]",
    bsp=r"\(\hat y(6)=2.2+0.6\cdot6=5.8\) · Residuen: \(\hat y=2.8;3.4;4.0;4.6;5.2\) → \(\hat\varepsilon=-0.8;\ 0.6;\ 1.0;\ -0.6;\ -0.2\)",
    ks="„Steigt x um eine Einheit, steigt y im Durchschnitt um 0.6 Einheiten (ceteris paribus).“ Prognosen weit außerhalb der Daten sind unsicher.")

D.E("14.3", "Bestimmtheitsmaß R²",
    sig="„Berechnen und interpretieren Sie R²“",
    ne="R² = açıklanan varyans oranı (0–1). Basit regresyonda R² = r².",
    fm=r"\[R^2=\frac{\sum(\hat y_i-\bar y)^2}{\sum(y_i-\bar y)^2}=1-\frac{\sum\hat\varepsilon_i^2}{\sum(y_i-\bar y)^2}=r_{xy}^2\]",
    bsp=r"\(\sum\hat\varepsilon^2=2.4\), \(\sum(y_i-\bar y)^2=6\) → \(R^2=1-0.4=0.6\) (= 0.775²)",
    ks="„60 % der Streuung von y werden durch das Modell (durch x) erklärt.“")

D.E("14.4", "lm-Output lesen: Signifikanz und KI für β",
    sig="R-Output „Coefficients: Estimate, Std. Error, t value, Pr(&gt;|t|)“",
    ne="Estimate = \\(\\hat\\beta\\), Std. Error = \\(\\hat\\sigma_{\\hat\\beta}\\), t value = Estimate/Std. Error, Pr(>|t|) = çift yönlü p-değeri (H₀: β = 0).",
    fm=r"\[T=\frac{\hat\beta_j}{\hat\sigma_{\hat\beta_j}}\ \overset{H_0}{\sim}\ t(n-p-1)\qquad\text{KI: }\hat\beta_j\pm t_{n-p-1;\,1-\alpha/2}\,\hat\sigma_{\hat\beta_j}\qquad n=df+p+1\]",
    bsp=r"Lernstunden: Estimate 2.031, Std. Error 0.173, df = 37 → \(t=11.73\), p < 0.001 → signifikant · 95 %-KI \(2.031\pm2.026\cdot0.173=[1.680;\ 2.382]\) · Dummy Vorkurs 8.743: Teilnehmer haben im Mittel 8.743 Punkte mehr (c. p.)",
    fa="p ist zweiseitig. Freiheitsgrade stehen bei „Residual standard error: … on 37 degrees of freedom“.")

# =====================================================================
D.S("15", "Anhang: Tabellen und Checkliste",
    "Sınavda kantiller genelde verilir; bu tablolar alıştırma ve kontrol için.")

rows = ['<tr><th>z</th>' + ''.join('<th>%.2f</th>' % (j / 100) for j in range(10)) + '</tr>']
for i in range(31):
    rows.append('<tr><th>%.1f</th>' % (i / 10) + ''.join('<td>%.4f</td>' % norm.cdf(i / 10 + j / 100) for j in range(10)) + '</tr>')
D.E("15.1", "Verteilungsfunktion Φ(z) der Standardnormalverteilung",
    sig="Zeile = z bis zur 1. Nachkommastelle, Spalte = 2. Nachkommastelle",
    ne="Örnek: Φ(1.64) → satır 1.6, sütun 0.04 = 0.9495. Negatif z: Φ(−z) = 1 − Φ(z).",
    extra='<table class="t phi">' + ''.join(rows) + '</table>', long=True)

ps = [0.90, 0.95, 0.975, 0.99, 0.995]
dfs = list(range(1, 31)) + [40, 60, 100]
trow = ['<tr><th>df</th>' + ''.join('<th>%s</th>' % p for p in ps) + '</tr>']
for d in dfs:
    trow.append('<tr><th>%d</th>' % d + ''.join('<td>%.3f</td>' % tdist.ppf(p, d) for p in ps) + '</tr>')
trow.append('<tr><th>∞</th>' + ''.join('<td>%.3f</td>' % norm.ppf(p) for p in ps) + '</tr>')
D.E("15.2", "Quantile \\(t_{df;\\,p}\\) der t-Verteilung",
    sig="KI für μ mit σ unbekannt, t-Test",
    ne="Örnek: t<sub>15; 0.975</sub> = 2.131. df büyüdükçe z değerlerine yaklaşır (son satır).",
    extra='<table class="t phi">' + ''.join(trow) + '</table>', long=True)

cps = [0.01, 0.025, 0.05, 0.10, 0.90, 0.95, 0.975, 0.99]
crow = ['<tr><th>df</th>' + ''.join('<th>%s</th>' % p for p in cps) + '</tr>']
for d in list(range(1, 31)):
    crow.append('<tr><th>%d</th>' % d + ''.join('<td>%.3f</td>' % chi2.ppf(p, d) for p in cps) + '</tr>')
D.E("15.3", "Quantile \\(\\chi^2_{df;\\,p}\\) der χ²-Verteilung",
    sig="KI für σ², Varianztest, χ²-Unabhängigkeits- und Anpassungstest",
    ne="Örnek: χ²<sub>9; 0.975</sub> = 19.023, χ²<sub>9; 0.025</sub> = 2.700.",
    extra='<table class="t phi">' + ''.join(crow) + '</table>', long=True)

D.E("15.4", "Checkliste vor dem Abgeben",
    sig="letzte 5 Minuten",
    ne="Teslim etmeden önce her kutuyu bu listeyle kontrol et.",
    st=["Jede Teilfrage beantwortet (auch „Begründen Sie“, „Interpretieren Sie“, „Welche Annahme?“)?",
        "Wahrscheinlichkeiten zwischen 0 und 1? Varianz ≥ 0? |r| ≤ 1? χ² ≥ 0? Summe der Wahrscheinlichkeiten = 1?",
        "Richtige Varianz (1/n oder 1/(n − 1))? Richtiger Nenner bei bedingten Anteilen?",
        "3 Nachkommastellen bzw. gekürzter Bruch; Dezimalpunkt; nur eine Lösung im Kästchen.",
        "Tests: H₀/H₁, Teststatistik, Verteilung, Ablehnungsbereich/p-Wert, Satz im Sachkontext.",
        "ML: Dach auf dem Schätzer, 2. Ableitung, ln statt log₁₀.",
        "Kein Kästchen leer: Formel und Ansatz bringen Teilpunkte."])
