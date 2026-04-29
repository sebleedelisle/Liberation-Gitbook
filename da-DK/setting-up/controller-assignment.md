---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Tildeling af controllere

Når du har sat laserne op i Liberation, kan du tildele hver enkelt til en lasercontroller i den virkelige verden. (Se [Kompatible lasere og controllere (DACs)](../hardware/compatible-lasers-and-controllers-dacs.md "mention") for at tjekke, hvilken hardware du kan bruge). Controllerne vil enten være tilsluttet via USB eller over netværket.

* Åbn panelet _Controller Assignment_ via menupunktet _View -> Controller Assignment_. (Alternativt kan du bruge knappen _ASSIGN LASER CONTROLLERS_ i panelet _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment-panel"><figcaption></figcaption></figure>

* Panelet er delt i to med en liste over lasere til venstre og listen over tilgængelige controllere til højre. Hvis du ikke kan se din lasercontroller på listen, skal du trykke på knappen _REFRESH_. Hvis du stadig har problemer, se [Fejlfinding](../troubleshooting/ "mention").
* For at tildele en controller til en laser skal du klikke og trække fra højre over på en ledig laserplads til venstre. Det fortæller Liberation, hvilken controller der skal bruges til hvilken laser. (Hvis du ændrer mening, kan du frit trække controllerne op og ned fra én laser til en anden.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Liste over controllere" width="375"><figcaption></figcaption></figure>

* Hvis du ser en grøn firkant ved siden af controlleren, betyder det, at Liberation har oprettet forbindelse til den.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>En Ether Dream og en Helios DAC tildelt henholdsvis laser 2 og 3</p></figcaption></figure>

{% hint style="info" %}
Bemærk, at hver gang du opretter forbindelse til en controller, bliver laseren automatisk sat i disarmed-tilstand.
{% endhint %}

* En orange firkant 🟧 betyder, at controlleren har periodiske forbindelsesproblemer. Det skyldes normalt et netværksproblem; se [Fejlfinding](../troubleshooting/ "mention").
* En rød firkant 🟥 betyder, at controlleren ikke kan nås; se [Fejlfinding](../troubleshooting/ "mention").
* _disconnect button_ (X) afbryder forbindelsen til controlleren, men fjerner den ikke fra lasertildelingen. Du kan derefter bruge _reconnect button_ (ikon med opdateringspil) til at oprette forbindelse igen, eller klikke på _disconnect button_ igen for at fjerne tildelingen.
* _Avanceret funktion:_ Åbn controllerens analysepanel ved at klikke på knappen, der ligner et diagram. Dette er en avanceret funktion, der giver dig detaljerede oplysninger om datastrømmen og kan hjælpe med fejlfinding. (Denne indstilling er muligvis ikke tilgængelig for alle controllertyper.)
* Du kan bruge _rename button_ (blyant) til at omdøbe denne controller til hvad du vil. Det giver mening at navngive den på en måde, der gør den nem at forbinde med bestemt hardware. Hvis den er indbygget i en laser, kan du navngive den derefter, f.eks. _LaserCube Ultra #1_ eller _Triton T5 #3._ Disse navne gemmes sammen med din Liberation-installation og vises fremover; det kan være en stor hjælp, når du hurtigt skal identificere dine lasere.

{% hint style="info" %}
Pro-tip - **dobbeltklik** på en controller til højre for automatisk at tildele den til den næste ledige laser til venstre. Det kan spare meget tid, hvis du har mange lasere, der skal tildeles!
{% endhint %}

Du kan bruge knapperne _DISCONNECT ALL_ og _RECONNECT ALL_ til hurtigt at nulstille alle forbindelser. Det er nyttigt, hvis du har netværksproblemer.
