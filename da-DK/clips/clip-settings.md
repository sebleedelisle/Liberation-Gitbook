---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip-indstillinger

### Panelet Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Panelet Clip settings</p></figcaption></figure>

Skift clippets outputstørrelse med _Scale X_ og _Scale Y_. De er låst sammen, medmindre du holder _SHIFT_-tasten nede.

Skift clippets vandrette og lodrette placering med _Shift X_ og _Shift Y_.

_Zone Delay/Chase_ er så sjov en funktion, at den har fået sit eget afsnit. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters panel

Panelet til højre for Clip Deck viser otte kontekstafhængige parametre. Når et Clip er valgt, er de første kontroller det valgte Clips _Shift X_, _Shift Y_ og _Zone Delay_, efterfulgt af de globale kontroller _Spin_ og _Scale_.

De samme parametre spejles til understøttede MIDI-controllere. Hvis der ikke er valgt et Clip, er de Clip-specifikke pladser tomme. Hvis du holder en gruppeknap nede, skifter de første to kontroller til gruppens fade ind- og fade ud-tider.

### Låsning af clips

Hvis et clip er låst, kan det ikke flyttes eller slettes. Du låser et clip med afkrydsningsfeltet _Locked_ i højreklikmenuen. I panelet Clip settings får du nogle flere muligheder.

* _UNLOCK ALL -_ låser alle clips op i clip decket.
* _AUTO-LOCK_ - når _Auto-Lock_ er slået til, bliver alle clips, der afspilles automatisk (enten med tidslinjen eller MIDI record/playback-systemet), låst. Det er nyttigt, hvis du har programmeret et show i Logic Pro (eller lignende) og ikke vil risikere at redigere de clips, der bruges i showet, ved et uheld.
* _LOCKED CLIPS ZONES_ - hvis dette er slået til, kan du ikke ændre zonerne for nogen låste clips.
* _LOCKED CLIPS PARAMS_ - hvis dette er slået til, kan du ikke ændre parametrene (scale, shift osv.) for nogen låste clips.

### Højreklikmenu

Hvis du højreklikker på et Clip, vises en menu med nogle af indstillingerne for det Clip. Se [Introduktion til Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Clip-indstillinger](clip-settings.md "mention") og [Clip-grupper](groups.md "mention") for mere om de første punkter i denne menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips er som standard sat til _retrigger_. Det betyder, at uanset hvornår du trykker på et clip, begynder det at køre fra det tidspunkt. Så hvis du starter det for sent, vil clippets animation være en smule forsinket og ude af takt.

{% hint style="info" %}
Hvis du bruger _Tap Tempo_, mens et retriggered clip kører, vil systemet "kvantisere" clippet, så det kommer i takt, selv om du ikke startede det præcist på slaget.
{% endhint %}

Hvis _Retrigger_ ikke er slået til, vil clippet altid være i takt - som om clippet blev startet helt fra urets begyndelse. Det er godt, når du er perfekt synkroniseret med musikken via et eksternt clock-signal.

{% hint style="info" %}
Clips er ofte designet til at loope for evigt, men du kan designe dem, så de kun kører én gang eller nogle få gange rundt. Sørg for at lade dem være sat til _retrigger_, ellers starter de ikke forfra!
{% endhint %}

### Ind-/udtoningstid (fade)

Clips kan indstilles til at fade ind og ud med en varighed målt i sekunder. Som standard arves fade-tiden fra gruppens indstillinger (og den kan ændres ved at højreklikke på gruppeknappen).

Hvis du vil have en anden fade-varighed end clippets gruppe, skal du først slå knappen _USE GROUP DEFAULT_ fra og derefter justere clippets skydere _In time_ og _Out time_.
