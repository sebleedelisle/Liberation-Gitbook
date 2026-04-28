---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Använda Liberation med Capture

Liberation stöder [Capture](https://capture.se) som extern visualiserare (från version 1.0.3). Om du redan använder Capture i ditt arbetsflöde kan du använda det för att visualisera Liberations liveutmatning för laser i din 3D-scen.

### Så fungerar det

Det krävs ingen särskild anslutningsprocess eller manuell länkning.

Så länge:

* Liberation och Capture finns på samma nätverk
* Din brandvägg tillåter anslutningen

…kommer alla lasrar du har konfigurerat i Liberation automatiskt att visas i Capture som mediekällor. Du behöver inte konfigurera IP-adresser eller aktivera något särskilt – de dyker bara upp.

### Se lasrar i Capture

Alla konfigurerade lasrar i Liberation visas i Capture som tillgängliga mediekällor.

För att faktiskt se utmatning:

* Lasern måste vara armerad i Liberation
* Källan måste vara kopplad till en laserarmatur i Capture

När lasern är armerad visualiserar Capture liveströmmen från Liberation. Om en laser avarmeras i Liberation fortsätter den att visas i Capture som källa, men den matar inte ut något.

Se dokumentationen på [capture.se](https://www.capture.se/) för fler instruktioner och support för att konfigurera lasrar i Capture. <br>

### Licensgränser och armerade lasrar

Anslutningar till Capture hanteras på exakt samma sätt som fysiska laserutgångar.

Det innebär:

* Du kan bara armera så många lasrar som din licensnivå tillåter
* Endast armerade lasrar skickar aktivt data till Capture

### Behöver jag Capture?

Nej, inte alls.

Liberation innehåller en inbyggd 3D Visualiser, som alltid är tillgänglig och inte beror på din licensnivå. Du kan designa och förhandsgranska shower direkt i Liberation utan någon extern programvara.

Capture är helt enkelt ett extra alternativ om du redan använder det för ljus- eller showdesign.

### Felsökning

Om lasrar inte visas i Capture:

* Kontrollera att båda programmen finns på samma nätverk
* Kontrollera dina brandväggsinställningar
* Se till att lasern är armerad i Liberation
