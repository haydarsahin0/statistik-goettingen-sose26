from fscommon import Doc

D = Doc(
    key="stat", cls="fs-stat",
    title="Formelsammlung Statistik",
    sub="Teil A · alle Aufgabentypen von V01 bis V13 · Schritt für Schritt",
    chip="SoSe 26 · Göttingen · Teil A",
    intro=("<p>Jede Formel, die in Vorlesung, Tutorien, Testaten und Probeklausuren vorkommt – sortiert nach <b>Aufgabentyp</b>. "
           "Jedes Rezept: <b>Erkennen</b> (Wortlaut in der Aufgabe) → <b>TR</b> (kısa Türkçe açıklama) → <b>Formel</b> → <b>Schritte</b> → <b>Beispiel</b> mit Zahlen → <b>⚠ Falle</b> → <b>✎ Klausursatz</b>.</p>"
           "<p>Alle Beispielzahlen sind mit Python/R nachgerechnet. Diese Sammlung darfst du nicht in die Klausur mitnehmen – sie ist dein Nachschlagewerk zum Üben und die Vorlage für dein handgeschriebenes A4-Blatt.</p>"),
    howto=("<b class='t'>Nasıl kullanılır?</b><ol>"
           "<li>Soruyu oku → <b>{FINDER}</b>'da sorudaki ifadeyi bul → yanındaki numaraya git.</li>"
           "<li>Rezeptte <b>Schritte</b>'yi sırayla uygula, <b>Beispiel</b> ile kendi sayılarını karşılaştır.</li>"
           "<li><b>⚠ Falle</b>'yi oku – puan kaybettiren klasik hata orada. Cevabı <b>✎ Klausursatz</b> kalıbıyla yaz.</li>"
           "<li>Konu tamamen yabancıysa İçindekiler'den bölümün ilk rezeptinden başla.</li></ol>"),
    foot="Formelsammlung Statistik · Teil A · SoSe 26",
    outname="Formelsammlung_Statistik.pdf")
