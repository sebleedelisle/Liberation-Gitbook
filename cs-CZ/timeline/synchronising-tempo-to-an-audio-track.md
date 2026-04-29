---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Synchronizace tempa se zvukovou stopou

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchronizace tempa se zvukovou stopou" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Časová osa v Liberation je navržená tak, aby fungovala s pevným i měnícím se tempem. Spolehlivá synchronizace ale vždy začíná nalezením správného tempa a správným zarovnáním zvuku. Tato část popisuje doporučený postup.

#### 1. Zarovnejte první těžkou dobu

Přidejte zvukovou stopu na časovou osu a ujistěte se, že je přichycena k době tak, aby **první hudební těžká doba** stopy přesně odpovídala začátku taktu.

Tento krok je zásadní.

Pokud zvuk přirozeně nezačíná na těžké době, máte dvě možnosti:

* **Upravte zpoždění Clip**\
  Klikněte pravým tlačítkem na zvukový Clip a upravte hodnotu Delay, dokud se první těžká doba nezarovná se značkou doby nebo taktu.
* **Ořízněte zvuk externě**\
  Upravte zvukový soubor v externím editoru, například Audacity, aby soubor začínal přesně na první těžké době, a poté ho znovu importujte.

{% hint style="info" %}
**Důležité:**\
Pokud začátek zvuku není zarovnaný na dobu nebo takt, bude se při změně tempa vnímaná počáteční pozice hudby posouvat dozadu a dopředu. Přesné sladění tempa je pak velmi obtížné.
{% endhint %}

#### 2. Nastavte počáteční tempo

Pokud máte přibližnou představu o BPM, zadejte ji do ovládání tempa na časové ose a spusťte přehrávání od začátku.

Během přehrávání stopy pečlivě sledujte značky dob a taktů.

* Pokud se značky posouvají před hudbu, tempo mírně snižte.
* Pokud zaostávají, tempo mírně zvyšte.
* Zastavte přehrávání, upravte tempo a zkuste to znovu.

U většiny moderní hudby je tempo pevná celočíselná hodnota BPM. Jakmile najdete správnou hodnotu, měla by zůstat přesná po celou dobu stopy.

#### 3. Použijte průběh zvuku jako vizuální vodítko

Zvuková vlna je užitečná reference při slaďování tempa.

* Transienty a špičky by se měly zarovnávat se svislými značkami taktů.
* Přibližte si časovou osu a zkontrolujte zarovnání přes více taktů.

**Tip:**\
K přiblížení časové osy použijte kolečko myši nebo gesto na trackpadu. K posunu doleva a doprava použijte vodorovné kolečko nebo gesto. Práce při větším přiblížení výrazně usnadňuje malé úpravy.

#### 4. Stopy s neceločíselným BPM

Pokud stopa nepoužívá celočíselné BPM, posun bude pozvolnější.

* Přibližte si časovou osu více.
* Používejte menší úpravy tempa.
* Kontrolujte zarovnání na delších částech stopy, ne jen na prvních několika taktech.

#### 5. Hudba se změnami tempa

Pokud hudba zrychluje nebo zpomaluje, použijte Tempo Map:

* Pusťte stopu a sledujte značky dob.
* Jakmile bude posun patrný, přidejte v daném místě změnu tempa.
* Upravte tempo nové části, dokud se znovu nezarovná.

Tento postup zopakujte pro každou změnu tempa v hudbě.

#### 6. Externí analýza tempa (volitelné)

Jako poslední možnost můžete stopu analyzovat v DAW, například Logic Pro, a vygenerovat mapu tempa automaticky. Počítejte s tím, že tím často vznikne velké množství změn tempa, někdy i jedna na každý takt, což může být pro většinu show zbytečně podrobné.
