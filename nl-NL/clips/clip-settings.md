---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Paneel Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Het paneel Clip settings</p></figcaption></figure>

Wijzig de uitvoergrootte van de clip met _Scale X_ en _Scale Y_. Ze zijn aan elkaar gekoppeld, tenzij je de _SHIFT_-toets indrukt.

Wijzig de horizontale en verticale positie van de clip met _Shift X_ en _Shift Y_.

_Zone Delay/Chase_ is zo’n leuke functie dat die een eigen sectie krijgt. [Zone delay / chase](zone-delay-chase.md "mention")

### Parameters panel

Het paneel rechts van het Clip Deck toont acht contextuele parameters. Als er een Clip is geselecteerd, zijn de eerste regelaars _Shift X_, _Shift Y_ en _Zone Delay_ van de geselecteerde Clip, gevolgd door de globale regelaars _Spin_ en _Scale_.

Dezezelfde parameters worden ook gespiegeld naar ondersteunde MIDI-controllers. Als er geen Clip is geselecteerd, blijven de Clip-specifieke posities leeg. Als je een groepsknop ingedrukt houdt, veranderen de eerste twee regelaars naar de fade-in- en fade-outtijden van die groep.

### Clips vergrendelen

Als een clip vergrendeld is, kan die niet worden verplaatst of verwijderd. Gebruik het selectievakje _Locked_ in het rechtsklikmenu om een clip te vergrendelen. In het paneel Clip settings krijg je nog wat extra opties.

* _UNLOCK ALL -_ ontgrendelt elke clip in de Clip Deck.
* _AUTO-LOCK_ - wanneer _Auto-Lock_ aan staat, wordt elke clip die automatisch wordt afgespeeld (via de tijdlijn of het MIDI-opname-/afspeelsysteem) vergrendeld. Dit is handig als je een show hebt geprogrammeerd in Logic Pro (of iets vergelijkbaars) en niet per ongeluk de clips wilt bewerken die in de show worden gebruikt.
* _LOCKED CLIPS ZONES_ - als dit aan staat, kun je de zones van vergrendelde clips niet wijzigen.
* _LOCKED CLIPS PARAMS_ - als dit aan staat, kun je de parameters (Scale, Shift enz.) van vergrendelde clips niet wijzigen.

### Rechtsklikmenu

Als je met de rechtermuisknop op een Clip klikt, verschijnt er een menu met enkele opties voor die Clip. Zie [Introductie tot de Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Clip settings](clip-settings.md "mention") en [Clipgroepen](groups.md "mention") voor meer informatie over de eerste items in dit menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips staan standaard ingesteld op _retrigger_. Dit betekent dat de clip begint te lopen vanaf het moment dat je erop drukt, ongeacht wanneer dat is. Dus als je de clip te laat start, loopt de animatie van de clip ook iets te laat en uit de maat.

{% hint style="info" %}
Als je _Tap Tempo_ gebruikt terwijl een geretriggerde clip loopt, zal het systeem de clip “kwantiseren” zodat die in de maat loopt, zelfs als je hem niet precies op de tel hebt gestart.
{% endhint %}

Als _Retrigger_ niet is ingeschakeld, loopt de clip altijd in de maat — alsof de clip helemaal aan het begin van de klok is gestart. Dit is handig wanneer je perfect met de muziek bent gesynchroniseerd via een extern kloksignaal.

{% hint style="info" %}
Clips zijn vaak ontworpen om eindeloos te loopen, maar je kunt ze ook zo ontwerpen dat ze maar één keer of een paar keer rondlopen. Zorg dat je die op _retrigger_ laat staan, anders starten ze niet opnieuw!
{% endhint %}

### In-/out-transitiontijd (fade)

Clips kunnen zo worden ingesteld dat ze infaden en uitfaden met een duur in seconden. Standaard wordt de fadelengte overgenomen uit de groepsinstellingen (en die kun je wijzigen door met de rechtermuisknop op de groepsknop te klikken).

Als je voor de clip een andere fadelengte wilt dan die van de groep, schakel je eerst de knop _USE GROUP DEFAULT_ uit. Pas daarna de schuifregelaars _In time_ en _Out time_ van de clip aan.
