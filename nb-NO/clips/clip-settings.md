---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Clip settings-panel

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings-panelet</p></figcaption></figure>

Endre utgangsstørrelsen på klippet med _Scale X_ og _Scale Y_. De er låst sammen med mindre du holder nede _SHIFT_-tasten.

Endre den horisontale og vertikale plasseringen av klippet med _Shift X_ og _Shift Y_.

_Zone Delay/Chase_ er en så morsom funksjon at den får sin egen seksjon. [Soneforsinkelse / chase](zone-delay-chase.md "mention")

### Parameters panel

Panelet til høyre for Clip Deck viser åtte kontekstbaserte parametere. Når en Clip er valgt, er de første kontrollene _Shift X_, _Shift Y_ og _Zone Delay_ for den valgte Clip, etterfulgt av de globale kontrollene _Spin_ og _Scale_.

De samme parameterne speiles til støttede MIDI-kontrollere. Hvis ingen Clip er valgt, er plassene for Clip-spesifikke kontroller tomme. Hvis du holder inne en gruppeknapp, endres de to første kontrollene til gruppens fade inn- og fade ut-tider.

### Låse klipp

Hvis et klipp er låst, kan det ikke flyttes eller slettes. For å låse et klipp bruker du avkrysningsboksen _Locked_ i høyreklikkmenyen. I Clip settings-panelet får du noen flere valg.

* _UNLOCK ALL -_ låser opp alle klipp i Clip Deck.
* _AUTO-LOCK_ - når _Auto-Lock_ er på, låses alle klipp som spilles av automatisk (enten med tidslinjen eller MIDI record/playback-systemet). Dette er nyttig hvis du har programmert et show i Logic Pro (eller lignende) og ikke vil redigere klippene som brukes i showet ved et uhell.
* _LOCKED CLIPS ZONES_ - hvis dette er på, kan du ikke endre sonene for låste klipp.
* _LOCKED CLIPS PARAMS_ - hvis dette er på, kan du ikke endre parameterne (scale, shift osv.) for låste klipp.

### Høyreklikkmeny

Hvis du høyreklikker på en Clip, vises en meny med noen av valgene for den Clip. Se [Introduksjon til Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Clip settings](clip-settings.md "mention") og [Clip-grupper](groups.md "mention") for mer om de første elementene i denne menyen.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Klipp er som standard satt til _retrigger_. Det betyr at uansett når du trykker på det, starter klippet fra det øyeblikket. Hvis du starter det for sent, vil animasjonen i klippet derfor ligge litt etter og være ute av takt.

{% hint style="info" %}
Hvis du bruker _Tap Tempo_ mens et retriggeret klipp kjører, vil systemet «kvantisere» klippet slik at det kommer i takt, selv om du ikke startet det nøyaktig på slaget.
{% endhint %}

Hvis _Retrigger_ ikke er aktivert, vil klippet alltid være i takt – som om klippet ble startet helt i begynnelsen av klokken. Dette er nyttig når du er perfekt synkronisert med musikken via et eksternt klokkesignal.

{% hint style="info" %}
Klipp er ofte laget for å loope for alltid, men du kan utforme dem slik at de bare kjører én gang eller noen få runder. Pass på at disse fortsatt står på _retrigger_, ellers starter de ikke på nytt!
{% endhint %}

### Transition in/out time (fade)

Clips kan settes til å fade inn og ut med en varighet målt i sekunder. Som standard arves fade-tiden fra gruppeinnstillingene (og kan endres ved å høyreklikke på gruppeknappen).

Hvis du vil ha en annen fade-varighet enn den som er satt for klippets gruppe, slår du først av _USE GROUP DEFAULT_-knappen og justerer deretter sliderne _In time_ og _Out time_ for klippet.
