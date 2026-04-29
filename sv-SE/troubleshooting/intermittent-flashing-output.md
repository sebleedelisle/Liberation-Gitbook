---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Intermittent / blinkande output

Öppna panelen _Laser Overview_ och titta på anslutningslampan bredvid den laser du har problem med.

**Om anslutningslampan INTE lyser konstant grönt:**\
Då har du antingen ett problem med nätverket eller med CPU-prestandan:

**Nätverksprestanda -**

* Se till att du inte är ansluten till ett wifi-nätverk. Du bör alltid använda en kabelanslutning. Kontrollera att operativsystemet prioriterar det trådbundna nätverket framför wifi, eller stäng av wifi om du är osäker
* kontrollera din nätverksadapter – och prova en annan USB-C-adapter
* Windows-användare – kontrollera / uppdatera nätverksdrivrutinerna och kör lämpliga nätverkstestverktyg
* kontrollera all kabeldragning, switchar och routrar. Byt metodiskt ut och testa varje kabel.
* starta om all nätverksutrustning, inklusive switchar, routrar och varje Ether Dream.

**CPU-prestanda**

Om du har en gammal dator eller en dator med låga specifikationer kan den vara för långsam för att köra Liberation. Kontrollera bildfrekvensindikatorn på höger sida av ikonraden.

Där finns två värden – den faktiska bildfrekvensen och målfrekvensen. Om den faktiska bildfrekvensen sjunker under 30 kan du få problem.

Följande åtgärder kan hjälpa:

* ta bort lasrar som inte används, dvs. om du bara har en laser ansluten, ta bort de andra.
* Växla till Output- eller Canvas-vyn
* Stäng alla andra program, kontrollera nätverkets brandväggsinställningar, stäng antivirus, Dropbox osv.
* Sänk skärmupplösningen och gör Liberation-fönstret mindre

Om inget av detta fungerar bör du överväga att uppgradera datorn.

***

**Om anslutningslampan lyser konstant grönt:**

Då är det troligen ett maskinvaruproblem. Detta ligger utanför den här manualens omfattning, men du kan prova följande åtgärder:

* Inaktivera SFS-systemet (Scan Fail Safety). Vissa lasrar har en funktion som inaktiverar output om skannrarna slutar röra sig, dvs. om de skapar en stark statisk stråle. De kan vara lite för försiktiga / opålitliga.

{% hint style="danger" %}
Var extremt försiktig när du inaktiverar scan fail safety-systemet. Starka statiska strålar kan orsaka brännskador! Se till att du har en stoppknapp och en brandsläckare till hands.
{% endhint %}

* Kontrollera säkerhetsförreglingskablar och säkerhetsförreglingssystem
* Kontrollera all kabeldragning mellan controllern och lasern.

En [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) kan vara ett ovärderligt verktyg vid felsökning av laserproblem.
