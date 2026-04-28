---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input-oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Konverterer lydinngangsnivået til en egenskapsverdi.

{% hint style="info" %}
Sound input-oscillatoren bruker standard lydgrensesnitt, men du kan endre dette i _Preferences_. Åpne menyen _Liberation -> Preferences._

Under innstillingene for _Sound Input_ kan du velge hvilket lydgrensesnitt du vil bruke, sammen med noen andre innstillinger for å justere volumnivået.
{% endhint %}

* **range min / range max** - minimums- og maksimumsverdiene som bølgeformen mappes til
* **channel** - Hvis lydgrensesnittet ditt har mer enn én inngangskanal, kan du velge her hvilken kanal du vil hente inn.

{% hint style="info" %}
En morsom teknikk er å hente flere lydsignaler fra miksepulten. Da kan du få ulike Clip-er til å reagere på ulike musikkinstrumenter.
{% endhint %}

{% hint style="info" %}
Du kan bare bruke ett lydgrensesnitt om gangen på tvers av alle _Sound Inputs_ (valgt i _App Settings_-panelet). Hvis du vil bruke mer enn ett grensesnitt til dette, kan du på macOS [create an Aggregate Device](https://support.apple.com/en-gb/HT202000) for å kombinere innganger til én virtuell lydkilde. (Det finnes mange apper på Windows som også kan gjøre dette, men jeg har ikke prøvd dem).
{% endhint %}

* **clamp min / clamp max** - bruk dette til å velge hvilket nivåområde du vil reagere på. Du skal normalt ikke trenge å justere dette hvis gate- og limit-innstillingene (i _App Settings_-panelet) er riktig justert, men de kan brukes til enkelte kreative effekter.

{% hint style="info" %}
Du ser et lite mikrofonikon på Clip-knappen når den har en _Sound Input_-oscillator.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
