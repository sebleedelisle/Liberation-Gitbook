# ✅ Panelen Laser output settings

Öppna inställningspanelen _Laser output_ via menyn _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Det visar inställningarna för den laser som är vald just nu, och du kan byta laser:

* via dess sifferknapp i panelen _Laser overview_
* med en siffertangent på tangentbordet; tangenterna 1 till 0 öppnar laser 1–10
* med `Tab` för att växla mellan lasrarna (`Shift + Tab` går bakåt).

Längst upp i panelen ser du:

* en sifferknapp – klicka på den för att armera/avarmera lasern. Den är röd när lasern är armerad.
* ett _Brightness_-reglage endast för den här lasern. Observera att detta kombineras med den globala ljusstyrkan.
* _Test Pattern_-växling och mönsterväljare. Här kan du välja ett specifikt testmönster endast för den här lasern. (Dessa kontroller speglas i verktygsfältet i Output-vyn).

### Utgångsorientering / korrigering av spegling

Nästa inställningar används för att korrigera laseruppsättningen så att den beter sig konsekvent i Liberation.

* **Flip horizontal / vertical** – med dessa alternativ kan du korrigera laserutgången

{% hint style="info" %}
Du ska normalt inte behöva ändra inställningarna för horisontell/vertikal spegling om inte lasern är felkopplad eller har X/Y-speglingknappar på baksidan som inte är korrekt inställda. Om du vill spegla utgången för en viss clip kan du göra det direkt på clippen.
{% endhint %}

* **Orientation** – om lasern har riggats på sidan eller upp och ned kan du korrigera rotationen med den här inställningen.
* **Fine position adjustments** – kan användas för att korrigera mycket små förskjutningar/rotationer. Avsett för att korrigera drift/sättning om en laser har stått över natten eller under längre perioder.

{% hint style="info" %}
Observera att korrigeringar för orientering/spegling inte ändrar något i 3D Visualiser. De ska användas för att korrigera utgången från den faktiska lasern så att den matchar det som visas i 3D Visualiser!
{% endhint %}

### Kopiera laserinställningar

Se [#copy-laser-settings](./#copy-laser-settings "mention").

### Skannerinställningar

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Inställningen för hastighet avgör hur snabbt skannrarna rör sig.

{% hint style="danger" %}
Även om standardinställningarna är ganska försiktiga kan du fortfarande skada skannrarna om du driver dem för snabbt. Var försiktig, särskilt när du ökar hastigheten.
{% endhint %}

{% hint style="info" %}
Den här hastighetsinställningen ändrar inte punktfrekvensen, utan justerar i stället hur utspridda punkterna är. Mer information finns i [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Strålen byter färg och slås på och av medan skannrarna flyttar runt den, och dessa två saker är vanligtvis inte perfekt synkroniserade med varandra. Justera den här inställningen för att få dem i linje igen.

{% hint style="info" %}
Detta kallas ibland _blank shift_, men jag föredrar personligen termen _scanner sync_ – den är lite mer korrekt eftersom den justerar timingen för alla färgändringar i förhållande till skannerrörelsen.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-”svansar” – Colour shift är inte korrekt inställt</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Inga laser-”svansar”! Colour shift är bra!</p></figcaption></figure></div>

Om du ser små ”svansar” i laserutgången beror det troligen på att scanner sync behöver justeras. Om svansarna fortfarande syns oavsett inställning driver du sannolikt skannrarna/laserdrivarna snabbare än de klarar av. Prova att sänka skannerhastigheten.

#### Scanner presets

Använd detta för att välja en fördesignad skannerinställning. Standardalternativet fungerar vanligtvis bra, så du ska inte behöva ändra den här inställningen om du inte har särskilt dåliga (eller bra) skannrar. Om du vill fördjupa dig, se [scanner-presets.md](../../advanced/scanner-presets.md "mention")

#### Colour calibration

Du kan använda detta system för att korrigera ljusstyrkekurvan och vitbalansen för din laser. Se [colour-calibration.md](../../advanced/colour-calibration.md "mention")

#### Advanced settings

Du ska normalt inte behöva ändra dessa, men om du är nyfiken kan du läsa [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md "mention")
