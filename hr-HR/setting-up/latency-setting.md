---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Postavka latencije

U panelu _Settings_ (_Liberation->Settings_ ili CMD/CTRL ,) vidjet ćete klizač s oznakom _Latency(ms)._ (U starijim verzijama Liberationa to se nalazilo u panelu Laser Overview)

{% hint style="info" %}
Zadana postavka latencije od 150 ms trebala bi biti dobra u većini slučajeva, ali ako imate problema s mrežom, možete je pokušati povećati.
{% endhint %}

### Složenije objašnjenje

Ova postavka “frame latency” određuje maksimalno vrijeme između trenutka kada Liberation stvori frame i trenutka kada ga laser počne prikazivati. Ako povećate ovu vrijednost, možete primijetiti blago kašnjenje između Liberationa i izlaza lasera.

Prednost dulje latencije framea jest to što Liberation može što prije napuniti međuspremnike kontrolera lasera sadržajem; ako dođe do zagušenja mreže, manja je vjerojatnost da će kontroleru ponestati točaka.

To se obično odnosi samo na DAC uređaje na mreži, a postavka od 100 ms trebala bi biti dobra ravnoteža između brzine i zaštite od mrežnih kašnjenja. Ako imate zaista stabilnu mrežu, trebali biste je moći smanjiti na 50 ms.&#x20;
