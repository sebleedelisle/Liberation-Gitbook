---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Panelen Laser output settings

Öppna inställningspanelen _Laser output_ via menyn _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Då visas inställningarna för den laser som är vald för tillfället. Du kan byta laser:

* via dess nummerknapp i panelen _Laser overview_
* med en siffertangent på tangentbordet, tangenterna 1 till 0 öppnar laser 1–10
* med tangenten `Tab` för att bläddra mellan lasrarna (`Shift + Tab` går bakåt).

Längst upp i panelen ser du:

* en nummerknapp – klicka på den för att aktivera/avaktivera denna laser. Den är röd när lasern är aktiverad.
* ett _Brightness_-reglage enbart för denna laser. Observera att detta kombineras med den globala ljusstyrkan.
* _Test Pattern_-växling och mönsterväljare. Här kan du välja ett specifikt testmönster enbart för denna laser. (Dessa kontroller speglas i verktygsfältet i Output-vyn).

### Korrigering av output-orientering / spegling

Nästa delar används för att korrigera inställningen av din laser så att den beter sig konsekvent i Liberation.

* **Flip horizontal / vertical** – de här alternativen låter dig korrigera laserutgången

{% hint style="info" %}
Du ska normalt inte behöva ändra inställningarna för horizontal / vertical flip om inte lasern är felkopplad, eller om den har X/Y flip-knappar på baksidan som inte är rätt inställda. Om du vill att output ska vara speglad för ett visst Clip kan du göra det direkt på klippet.
{% endhint %}

* **Orientation** – om lasern är monterad på sidan eller upp och ned kan du korrigera rotationen med den här inställningen.
* **Fine position adjustments** – kan användas för att korrigera mycket små förskjutningar/rotationer. Avsett för att korrigera drift/sättning om en laser har stått över natten eller under längre perioder.

{% hint style="info" %}
Observera att korrigeringar för orientation / mirroring inte ändrar något i 3D Visualiser. De ska användas för att justera den faktiska laserns output så att den matchar det som visas i 3D Visualiser!
{% endhint %}

### Copy laser settings

Se [#copy-laser-settings](laser-settings.md#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Inställningen Speed avgör hur snabbt scanners rör sig.

{% hint style="danger" %}
Även om standardinställningarna är ganska försiktiga kan du ändå skada dina scanners om du driver dem för snabbt. Var försiktig, särskilt när du ökar hastigheten.
{% endhint %}

{% hint style="info" %}
Den här Speed-inställningen ändrar inte point rate, utan justerar i stället hur utspridda punkterna är. Mer information finns i [◼️ Så genererar Liberation laserinnehåll](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Strålen byter färg och slås på och av medan scanners flyttar runt den, och de här två sakerna är vanligtvis inte helt synkade med varandra. Justera den här inställningen för att få dem i linje igen.

{% hint style="info" %}
Detta kallas ibland _blank shift_, men personligen föredrar jag termen _scanner sync_ – den är lite mer exakt eftersom den justerar tajmingen för alla färgändringar i förhållande till scannerrörelsen.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-"svansar" – Colour shift är inte korrekt inställt</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Inga laser-"svansar"! Colour shift är bra!</p></figcaption></figure></div>

Om du ser små "svansar" i laserutgången beror det sannolikt på att scanner sync behöver justeras. Om svansarna fortfarande visas oavsett inställning driver du troligen dina scanners/laserdrivrutiner snabbare än de klarar av. Prova att sänka scannerhastigheten.

#### Scanner presets

Använd detta för att välja en fördefinierad scannerinställning. Standardalternativet fungerar oftast bra, så du ska normalt inte behöva ändra den här inställningen om du inte har särskilt dåliga (eller bra) scanners. Om du vill gå djupare, se [◼️ Skannerförinställningar och renderprofiler](../advanced/scanner-presets.md "mention")

#### Colour calibration

Du kan använda det här systemet för att korrigera laserljusstyrkans kurva och vitbalans. Se [Färgkalibrering](../advanced/colour-calibration.md "mention")

#### Advanced settings

Du ska inte behöva ändra de här inställningarna, men om du är nyfiken kan du läsa mer i [◼️ Avancerade laserinställningar](../advanced/advanced-laser-settings.md "mention")
