---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Latenzeinstellung

Im _Settings_-Panel (_Liberation->Settings_ oder CMD/CTRL ,) siehst du einen Schieberegler mit der Beschriftung _Latency(ms)._ (In älteren Versionen von Liberation befand sich dieser im Laser Overview-Panel)

{% hint style="info" %}
Die standardmäßige Latenzeinstellung von 150 ms sollte in den meisten Fällen passen. Wenn du jedoch Netzwerkprobleme hast, kannst du versuchen, den Wert zu erhöhen.
{% endhint %}

### Die ausführlichere Erklärung

Diese „Frame-Latenz“-Einstellung ist die maximale Zeit zwischen dem Erzeugen eines Frames durch Liberation und dem Beginn der Ausgabe durch den Laser. Wenn du diesen Wert erhöhst, bemerkst du möglicherweise eine leichte Verzögerung zwischen Liberation und deiner Laserausgabe.

Der Vorteil einer längeren Frame-Latenz ist, dass Liberation die Puffer der Laser-Controller so früh wie möglich mit Inhalt füllen kann. Wenn es im Netzwerk zu Engpässen kommt, ist die Wahrscheinlichkeit geringer, dass dem Controller die Punkte ausgehen.

Das gilt normalerweise nur für Netzwerk-DACs. Eine Einstellung von 100 ms sollte ein guter Kompromiss zwischen Geschwindigkeit und Schutz vor Netzwerkverzögerungen sein. Wenn du ein wirklich starkes Netzwerk hast, solltest du den Wert auf 50 ms reduzieren können.&#x20;
