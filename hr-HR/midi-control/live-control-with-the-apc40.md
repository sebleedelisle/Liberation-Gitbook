---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Live MIDI Controllers

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

Ovo je zadani hardverski controller za Liberation; toplo se preporučuje i može se reći da je Liberation od samog početka osmišljen oko ovog hardvera. Čim priključite APC40, Liberation se odmah automatski povezuje s njim.

{% hint style="warning" %}
_O ne! USB kabel mi se izvukao usred nastupa!_

Bez panike — samo ga ponovno priključite i Liberation će se automatski ponovno povezati, bez problema.
{% endhint %}

### APC40 Mark 1 ili Mark 2?

Ukratko, preporučuje se Mark 2 jer ima tipke u punoj boji koje bolje odgovaraju sučelju Liberation Clip Deck. Verzija Mark 1 može poslužiti ako treba, ali bit će malo zbunjujuća jer se raspored donekle razlikuje od onoga na zaslonu, a tipke mogu svijetliti samo crveno, narančasto ili zeleno, pa neće odgovarati bojama Clips.

{% hint style="info" %}
Izvorni APC40 Mark 1 izašao je 2009. (!) i neki ga i dalje preferiraju zbog metalnog kućišta i robusnog oblika nalik konzoli. Ažurirani Mark 2 izašao je 2014. i, iako je prestao s proizvodnjom 2024., vraća se u proizvodnju 2025. zbog potražnje vizualnih umjetnika (Resolume itd.) i laserista.
{% endhint %}

Za potpuni popis kontrola dostupnih na APC40 pogledajte [Referenca za APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 uključuje i profil za APC Mini. Mapira mrežu Clips 8x5, gumbe za zone, kontrole za preokretanje X/Y za zone, gumbe za grupe, zaustavljanje svih Clips, pomicanje stranica Clip, pomicanje stranica zone, tap tempo, resetiranje takta i fino podešavanje tempa. Njegovi faderi upravljaju razinama efekata, a faderi uz Shift upravljaju parametrima efekata. Zadnji fader upravlja globalnom svjetlinom.

### MIDI Fighter Twister

Profil za MIDI Fighter Twister namijenjen je upravljanju s mnogo enkodera, a ne pokretanju Clips. Jedan red enkodera upravlja parametrom 1 za slotove efekata 1–8, a drugi red prati osam kontekstnih kontrola na panelu Parameters, uključujući pomak za Clip, odgodu zone, globalno okretanje/skaliranje i fadeove grupa.
