---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Stvaranje DMX zones

1. Povežite Art-Net node uređaj i postavite ga prema uputama u [Povezivanje s Art-Net node uređajem](../connecting-to-an-artnet-node.md "mention").
2. Otvorite **DMX Zones** i kliknite **ADD DMX ZONE**.
3. Postavite **Node**, **Universe** i **Address** za zonu tako da odgovaraju rasvjetnom tijelu.
4. Odaberite **Preset** za rasvjetno tijelo. Preset određuje koji DMX kanali primaju fiksne vrijednosti, vrijednosti za uključivanje/isključivanje sadržaja, RGB boju, X/Y položaj, svjetlinu ili izričite DMX Value ulaze.
5. Kliknite **Edit DMX profile/channel mapping** (ikona klizača) za uređivanje mapiranja kanala. Zadani preset započinje kanalom za uključivanje/isključivanje sadržaja i kanalima za RGB boju.
6. Dodijelite Clip sadržaje DMX zone na isti način kao što ih dodjeljujete beam ili canvas zonama.
7. Pritisnite **ARM** kada ste spremni da zona šalje DMX izlaz.

{% hint style="warning" %}
Samo aktivirane DMX zone šalju vrijednosti uživo. Neaktivirane DMX zone brišu svoje mapirane kanale na nulu, što je sigurnije tijekom postavljanja rasvjetnih tijela.
{% endhint %}

DMX izlaz ograničen je i vašom razinom licence. Ako je gumb **ARM** onemogućen, provjerite uključuje li vaša razina DMX izlaz ili je već dosegnut najveći broj aktiviranih DMX zona.
