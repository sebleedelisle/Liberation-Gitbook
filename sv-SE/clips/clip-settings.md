---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip-inställningar

### Clip settings-panelen

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings-panelen</p></figcaption></figure>

Ändra clipets utmatningsstorlek med _Scale X_ och _Scale Y_. De är låsta till varandra om du inte håller ned _SHIFT_-tangenten.

Ändra clipets horisontella och vertikala position med _Shift X_ och _Shift Y_.

_Zone Delay/Chase_ är en så rolig funktion att den får ett eget avsnitt. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters-panel

Panelen till höger om Clip Deck visar åtta kontextuella parametrar. När ett Clip är markerat är de första kontrollerna det markerade clipets _Shift X_, _Shift Y_ och _Zone Delay_, följt av de globala kontrollerna _Spin_ och _Scale_.

Samma parametrar speglas till MIDI-controllers som stöds. Om inget Clip är markerat är de clip-specifika platserna tomma. Om du håller ned en gruppknapp ändras de två första kontrollerna till gruppens tider för fade in och fade out.

### Låsa clips

Om ett clip är låst kan det inte flyttas eller tas bort. För att låsa ett clip använder du kryssrutan _Locked_ i högerklicksmenyn. I Clip settings-panelen får du några fler alternativ.

* _UNLOCK ALL -_ låser upp alla clips i Clip Deck.
* _AUTO-LOCK_ - när _Auto-Lock_ är på låses alla clips som spelas upp automatiskt (antingen via tidslinjen eller MIDI-systemet för inspelning/uppspelning). Det är användbart om du har programmerat en show i Logic Pro (eller liknande) och inte vill råka redigera de clips som används i showen.
* _LOCKED CLIPS ZONES_ - om detta är på kan du inte ändra zonerna för något låst clip.
* _LOCKED CLIPS PARAMS_ - om detta är på kan du inte ändra parametrarna (scale, shift osv.) för något låst clip.

### Högerklicksmeny

Om du högerklickar på ett Clip visas en meny med några av alternativen för det Clipet. Se [Introduktion till Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Clip-inställningar](clip-settings.md "mention") och [Clip groups](groups.md "mention")för mer om de första objekten i den här menyn.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips är som standard inställda på _retrigger_. Det betyder att oavsett när du trycker på clipet börjar det spelas från det ögonblicket. Så om du startar det sent kommer clipets animation att ligga lite sent och ur takt.

{% hint style="info" %}
Om du använder _Tap Tempo_ medan ett retriggat clip körs kommer systemet att ”kvantisera” clipet så att det ligger i takt, även om du inte startade det exakt på slaget.
{% endhint %}

Om _Retrigger_ inte är aktiverat kommer clipet alltid att ligga i takt – det är som om clipet startades precis i början av klockan. Det är bra när du är perfekt synkroniserad med musiken via en extern klocksignal.

{% hint style="info" %}
Clips är ofta utformade för att loopa för alltid, men du kan skapa dem så att de bara körs en gång eller några få varv. Se till att ha dem inställda på _retrigger_, annars startar de inte om!
{% endhint %}

### Transition in/out time (fade)

Clips kan ställas in så att de tonas in och ut med en varaktighet som mäts i sekunder. Som standard ärvs fade-tiden från gruppens inställningar (och kan ändras genom att högerklicka på gruppknappen).

Om du vill ha en annan fade-varaktighet än clipets grupp, stäng först av knappen _USE GROUP DEFAULT_ och justera sedan clipets reglage _In time_ och _Out time_.
