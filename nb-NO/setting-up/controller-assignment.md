---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Kontrollertildeling

Når du har konfigurert laserne i Liberation, kan du tildele hver av dem til en fysisk laserkontroller. (Se [compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md "mention") for å sjekke hvilken maskinvare du kan bruke.) Kontrollerne er enten koblet til via USB eller over nettverket.

* Åpne _Controller Assignment_-panelet via menyvalget _View -> Controller Assignment_. (Alternativt kan du bruke knappen _ASSIGN LASER CONTROLLERS_ i _Laser Overview_-panelet.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment-panel"><figcaption></figcaption></figure>

* Panelet er delt i to, med en liste over lasere til venstre og listen over tilgjengelige kontrollere til høyre. Hvis du ikke ser laserkontrolleren din i listen, trykker du på _REFRESH_-knappen. Hvis du fortsatt har problemer, se [troubleshooting](../troubleshooting/ "mention").
* For å tildele en kontroller til en laser klikker og drar du fra høyre side til en ledig laserplass på venstre side. Dette forteller Liberation hvilken kontroller som skal brukes til hvilken laser. (Hvis du ombestemmer deg, kan du fritt dra kontrollerne opp og ned fra én laser til en annen.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Liste over kontrollere" width="375"><figcaption></figcaption></figure>

* Hvis du ser en grønn firkant ved siden av kontrolleren, betyr det at Liberation har koblet til den.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>En Ether Dream og en Helios DAC tildelt henholdsvis laser 2 og 3</p></figcaption></figure>

{% hint style="info" %}
Merk at hver gang du kobler til en kontroller, blir laseren automatisk deaktivert.
{% endhint %}

* En oransje firkant 🟧 betyr at kontrolleren har uregelmessige tilkoblingsproblemer. Dette skyldes vanligvis et nettverksproblem, se [troubleshooting](../troubleshooting/ "mention").
* En rød firkant 🟥 betyr at kontrolleren ikke kan nås, se [troubleshooting](../troubleshooting/ "mention").
* _disconnect button_ (X) kobler fra kontrolleren, men fjerner den ikke fra lasertildelingen. Du kan deretter bruke _reconnect button_ (ikon med oppdateringspil) for å koble den til igjen, eller klikke på _disconnect button_ én gang til for å fjerne tildelingen.
* _Avansert funksjon:_ Åpne analysepanelet for kontrolleren ved å klikke på knappen som ser ut som et diagram. Dette er en avansert funksjon som gir deg detaljert informasjon om datastrømmen og kan hjelpe deg med å feilsøke problemer. (Dette alternativet er kanskje ikke tilgjengelig for enkelte kontrollertyper.)
* Du kan bruke _rename button_ (blyant) til å gi denne kontrolleren et valgfritt navn. Det er lurt å gi den et navn som gjør det enkelt å knytte den til bestemt maskinvare. Hvis den er innebygd i en laser, kan du navngi den deretter, f.eks. _LaserCube Ultra #1_ eller _Triton T5 #3._ Disse navnene lagres med Liberation-installasjonen din og vises fra nå av. Det kan være svært nyttig når du raskt skal identifisere laserne dine.

{% hint style="info" %}
Profftips – **dobbeltklikk** på en kontroller til høyre for automatisk å tildele den til neste tilgjengelige laser til venstre. Dette kan spare mye tid hvis du har mange lasere som skal tildeles!
{% endhint %}

Du kan bruke knappene _DISCONNECT ALL_ og _RECONNECT ALL_ til raskt å tilbakestille alle tilkoblingene. Dette er nyttig hvis du har nettverksproblemer.
