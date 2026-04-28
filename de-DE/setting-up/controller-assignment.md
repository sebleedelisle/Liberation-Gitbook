---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Controller-Zuweisung

Nachdem du die Laser in Liberation eingerichtet hast, kannst du jeden davon einem Laser-Controller in der realen Welt zuweisen. (Siehe [compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md "mention"), um zu prüfen, welche Hardware du verwenden kannst.) Die Controller sind entweder per USB oder über das Netzwerk verbunden.

* Öffne das _Controller Assignment_-Panel über den Menüpunkt _View -> Controller Assignment_. (Alternativ kannst du im _Laser Overview_-Panel den Button _ASSIGN LASER CONTROLLERS_ verwenden.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment-Panel"><figcaption></figcaption></figure>

* Das Panel ist zweigeteilt: links siehst du die Liste der Laser, rechts die Liste der verfügbaren Controller. Wenn dein Laser-Controller nicht in der Liste angezeigt wird, drücke den Button _REFRESH_. Wenn weiterhin Probleme auftreten, siehe [troubleshooting](../troubleshooting/ "mention").
* Um einen Controller einem Laser zuzuweisen, klicke ihn rechts an und ziehe ihn auf einen freien Laser-Slot links. Damit teilst du Liberation mit, welchen Controller es für welchen Laser verwenden soll. (Wenn du es dir anders überlegst, kannst du die Controller jederzeit frei nach oben oder unten von einem Laser zu einem anderen ziehen.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Liste der Controller" width="375"><figcaption></figcaption></figure>

* Wenn neben dem Controller ein grünes Quadrat angezeigt wird, bedeutet das, dass Liberation erfolgreich eine Verbindung zu ihm hergestellt hat.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ein Ether Dream und ein Helios DAC, die Laser 2 bzw. 3 zugewiesen sind</p></figcaption></figure>

{% hint style="info" %}
Beachte, dass der Laser automatisch deaktiviert wird, sobald du eine Verbindung zu einem Controller herstellst.
{% endhint %}

* Ein orangefarbenes Quadrat 🟧 bedeutet, dass beim Controller zeitweise Verbindungsprobleme auftreten. Das wird normalerweise durch ein Netzwerkproblem verursacht, siehe [troubleshooting](../troubleshooting/ "mention").
* Ein rotes Quadrat 🟥 bedeutet, dass der Controller nicht erreichbar ist, siehe [troubleshooting](../troubleshooting/ "mention").
* Der _disconnect button_ (X) trennt die Verbindung zum Controller, entfernt ihn aber nicht aus der Laser-Zuweisung. Du kannst ihn anschließend mit dem _reconnect button_ (Aktualisieren-Pfeilsymbol) erneut verbinden oder stattdessen noch einmal auf den _disconnect button_ klicken, um die Zuweisung zu löschen.
* _Erweiterte Funktion:_ Öffne das Controller-Analytics-Panel, indem du auf den Button klickst, der wie ein Diagramm aussieht. Dies ist eine erweiterte Funktion, die dir detaillierte Informationen zum Datenstream liefert und bei der Fehlersuche helfen kann. (Diese Option ist möglicherweise für einige Controller-Typen nicht verfügbar.)
* Mit dem _rename button_ (Stift) kannst du diesen Controller beliebig umbenennen. Es ist sinnvoll, einen Namen zu wählen, der eine einfache Zuordnung zu bestimmter Hardware ermöglicht. Wenn er in einen Laser eingebaut ist, kannst du ihn entsprechend benennen, z. B. _LaserCube Ultra #1_ oder _Triton T5 #3._ Diese Namen werden mit deiner Liberation-Installation gespeichert und ab jetzt angezeigt; das kann sehr hilfreich sein, um deine Laser schnell zu identifizieren.

{% hint style="info" %}
Profi-Tipp: **Doppelklicke** rechts auf einen Controller, um ihn automatisch dem nächsten verfügbaren Laser links zuzuweisen. Das kann viel Zeit sparen, wenn du viele Laser zuweisen musst!
{% endhint %}

Mit den Buttons _DISCONNECT ALL_ und _RECONNECT ALL_ kannst du schnell alle Verbindungen zurücksetzen. Das ist nützlich, wenn Netzwerkprobleme auftreten.
