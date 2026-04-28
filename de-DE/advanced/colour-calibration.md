---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Farbkalibrierung

Die Farbkalibrierung sorgt dafür, dass die roten, grünen und blauen Laser deines Projektors bei allen Helligkeitsstufen gleichmäßig und vorhersehbar Licht ausgeben. Unterschiedliche Projektoren können nichtlineare Helligkeitskurven haben. Das bedeutet, dass 50% Rot deutlich heller oder dunkler wirken können als die halbe Intensität von 100% Rot. Die Kalibrierung korrigiert das, damit Farben sauber gemischt werden, Verläufe gleichmäßig aussehen und Weiß ausgewogen ist.

#### Deinen Projektor aufwärmen

Laserdioden verändern ihr Verhalten, während sie warm werden. Lass deinen Projektor vor der Kalibrierung immer erst stabilisieren:

* Projiziere mindestens **15–20 Minuten** lang ein helles Frame, zum Beispiel das **White rectangle test pattern (11)**.
* Dadurch bleibt die eingestellte Farbbalance während einer Show konsistent.

#### So funktioniert der Kalibrierungstest

Verwende die Testbilder für die Kalibrierung (siehe [test-patterns.md](../output-view/test-patterns.md "mention"))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Jedes dieser Testbilder zeigt vier bewegte Linien:

* **Obere Linie** – 100% Helligkeit bei voller Geschwindigkeit
* **Zweite Linie** – 75% Helligkeit bei 75% Geschwindigkeit
* **Dritte Linie** – 50% Helligkeit bei 50% Geschwindigkeit
* **Vierte Linie** – 25% Helligkeit bei 25% Geschwindigkeit

Da sowohl Helligkeit _als auch Geschwindigkeit_ gemeinsam skaliert werden, sollten alle Linien gleich hell aussehen. Wenn eine Linie heller oder dunkler wirkt, passe den entsprechenden Slider an, bis sie übereinstimmen.

Jedes Testbild hat außerdem eine fünfte Linie mit **0% Helligkeit**, die nicht sichtbar sein sollte. Damit wird korrigiert, wenn Laser bei sehr niedrigen Pegeln kein Licht ausgeben. Wenn dein Laser bei niedriger Helligkeit unsichtbar bleibt, erhöhe die **0%-Einstellung** schrittweise, bis die Linie gerade sichtbar wird. Reduziere sie dann wieder leicht, bis sie erneut verschwindet. Ziel ist es, den Schwellenwert zu finden, bei dem der Laser zu leuchten beginnt, und knapp darunter zu bleiben – damit deine Fades natürlich starten, ohne den unteren Bereich abzuschneiden.

#### Das Colour Calibration-Panel verwenden

Das Panel bietet dir unabhängige Regler für jeden Kanal (Rot, Grün, Blau) bei den Pegeln 100, 75, 50, 25 und 0%.

1. **Wähle ein Testbild aus** (beginne mit Rot).
2. **Passe die Slider an**, bis die Linien bei 100, 75, 50 und 25% gleich hell aussehen.
3. **Stimme den 0%-Slider fein ab**, falls die „Aus“-Linie noch schwach sichtbar ist.
4. **Wiederhole den Vorgang für Grün und Blau.**
5. Wechsle zum **White test pattern (8)**. Alle vier Linien sollten gleich hell aussehen, und das Weiß sollte neutral wirken (ohne Farbstich).

#### Weißabgleich anpassen

Du kannst dieses System auch zum Anpassen des **Weißabgleichs** verwenden. Nachdem du jeden Kanal einzeln kalibriert hast, wechsle zum **White test pattern (8)**. Wenn die Ausgabe farbstichig aussieht (zum Beispiel zu grün oder zu blau), passe die relativen Pegel der roten, grünen und blauen Kanäle an, bis die Linien neutral weiß wirken. Selbst wenn sich die Leistung deiner Laser deutlich unterscheidet, hilft die Kalibrierung dabei, sie näher zusammenzubringen und eine sauberere, ausgewogenere Farbmischung zu erzeugen.

#### Kalibrierung speichern

* Verwende **Store**, um das aktuelle Preset zu überschreiben.
* Verwende **Store As**, um ein neues Preset zu erstellen (nützlich, wenn du mit mehreren Lasern arbeitest).
