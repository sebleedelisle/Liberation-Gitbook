---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Að búa til DMX zones

1. Tengdu Art-Net node og settu hann upp í [Tengjast Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Opnaðu **DMX Zones** og smelltu á **ADD DMX ZONE**.
3. Stilltu **Node**, **Universe** og **Address** fyrir zone þannig að þau passi við búnaðinn.
4. Veldu **Preset** fyrir búnaðinn. Forsniðið skilgreinir hvaða DMX-rásir fá föst gildi, gildi fyrir kveikt/slökkt á efni, RGB-lit, X/Y-staðsetningu, birtustig eða skýr DMX Value-inntök.
5. Smelltu á **Edit DMX profile/channel mapping** (sleðatákn) til að breyta rásavörpuninni. Sjálfgefna forsniðið byrjar með rás fyrir kveikt/slökkt á efni og RGB-litarásum.
6. Úthlutaðu Clips á DMX zone á sama hátt og þú úthlutar þeim á beam zone eða canvas zone.
7. Ýttu á **ARM** þegar þú ert tilbúin(n) að láta zone senda DMX út.

{% hint style="warning" %}
Aðeins virkjaðar DMX zones senda lifandi gildi. Óvirkjaðar DMX zones hreinsa varpaðar rásir sínar í núll, sem er öruggara þegar búnaður er settur upp.
{% endhint %}

DMX-úttak takmarkast líka af leyfisstiginu þínu. Ef **ARM**-hnappurinn er óvirkur skaltu athuga hvort leyfisstigið þitt innihaldi DMX-úttak eða hvort hámarksfjölda virkjaðra DMX zones hafi þegar verið náð.
