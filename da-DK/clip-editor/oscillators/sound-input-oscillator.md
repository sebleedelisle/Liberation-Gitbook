---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input-oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Konverterer lydinputniveauet til en egenskabsværdi.

{% hint style="info" %}
Sound input-oscillatoren bruger standardlydinterfacet, men du kan ændre det i _Preferences_. Åbn menuen _Liberation -> Preferences._

Under indstillingerne for _Sound Input_ kan du vælge, hvilket lydinterface du vil bruge, sammen med nogle andre indstillinger til justering af lydstyrkeniveauet.
{% endhint %}

* **range min / range max** - de minimums- og maksimumsværdier, som bølgeformen mappes til
* **channel** - hvis dit lydinterface har mere end én inputkanal, kan du her vælge, hvilken kanal du vil bruge.

{% hint style="info" %}
En sjov teknik er at hente flere lydfeeds fra mixerpulten. På den måde kan du få forskellige clips til at reagere på forskellige musikinstrumenter.
{% endhint %}

{% hint style="info" %}
Du kan kun bruge ét lydinterface ad gangen på tværs af alle _Sound Inputs (_&#x73;om vælges i panelet _App Settings_). Hvis du vil bruge mere end ét interface til dette, kan du på macOS [oprette en Aggregate Device](https://support.apple.com/en-gb/HT202000), som kombinerer inputs til én virtuel lydkilde. (Der findes også mange apps på Windows, der kan gøre dette, men jeg har ikke prøvet dem).
{% endhint %}

* **clamp min / clamp max** - brug dette til at vælge, hvilket niveauområde du vil reagere på. Du bør ikke behøve at justere dette, hvis gate- og limit-indstillingerne (i panelet _App Settings_) er korrekt justeret, men de kan bruges til kreative effekter.

{% hint style="info" %}
Du ser et lille mikrofonikon på clip-knappen, når den har en _Sound Input_-oscillator.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
