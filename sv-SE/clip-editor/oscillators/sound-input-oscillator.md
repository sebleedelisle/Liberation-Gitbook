---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input-oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Omvandlar ljudingångens nivå till ett egenskapsvärde.

{% hint style="info" %}
Sound input-oscillatorn använder standardljudinterfacet, men du kan ändra det i _Preferences_. Öppna menyn _Liberation -> Preferences._

Under inställningarna för _Sound Input_ kan du välja vilket ljudinterface du vill använda, tillsammans med några andra inställningar för att justera volymnivån.
{% endhint %}

* **range min / range max** - de lägsta och högsta värden som vågformen mappas till
* **channel** - om ditt ljudinterface har fler än en ingångskanal kan du välja här vilken kanal du vill ta upp.

{% hint style="info" %}
En rolig teknik är att ta in flera ljudmatningar från mixerbordet. På så sätt kan du låta olika clips reagera på olika musikinstrument.
{% endhint %}

{% hint style="info" %}
Du kan bara använda ett ljudinterface åt gången för alla _Sound Inputs (_&#x73;om väljs i panelen _App Settings_). Om du vill använda fler än ett interface för detta kan du på macOS [skapa en Aggregate Device](https://support.apple.com/en-gb/HT202000) för att kombinera ingångar till en enda virtuell ljudkälla. (Det finns många appar på Windows som också gör detta, men jag har inte provat dem).
{% endhint %}

* **clamp min / clamp max** - använd detta för att välja vilket nivåområde du vill reagera på. Du ska normalt inte behöva justera detta om inställningarna för gate och limit (i panelen _App Settings_) är rätt justerade, men de kan användas för vissa kreativa effekter.

{% hint style="info" %}
Du ser en liten mikrofonikon på clip-knappen när den har en _Sound Input_-oscillator.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
