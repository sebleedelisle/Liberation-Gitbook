---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI note

## MIDI note

Stvara efekte u stilu „laserske harfe”, gdje dolazne MIDI note pokreću zrake ili oblike unutar zadanog raspona. Node za svaku notu koristi sadržaj koji mu proslijedite kao _izvor_ — pošaljite mu točku i dobit ćete niz točaka. Pošaljite mu oblik poput kruga i dobit ćete niz krugova, a složeniji oblici replicirat će se na isti način.

MIDI sučelje koje Liberation sluša možete odabrati u **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – MIDI kanal koji se sluša (0 = svi kanali, 1–16 = određeni kanal)
* **width** – ukupna širina preko koje se note raspoređuju.
* **midi note min / max** – najniža i najviša vrijednost MIDI note u rasponu.
* **ignore out of range notes** – filtrira sve note izvan postavljenog raspona. Ako je isključeno, note izvan raspona „prikvačuju” se na najbližu dostupnu notu (visoke note pokreću vrh raspona, niske note pokreću dno).
* **auto extend range** – automatski proširuje raspon ako se odsviraju note izvan njega.

{% hint style="info" %}
Niste sigurni koji raspon nota dobivate? Uključite **auto extend range**, postavite **midi note min** vrlo visoko, a **midi note max** vrlo nisko, zatim odsvirajte svoje note. Sustav će ih sve uhvatiti i proširiti raspon umjesto vas. Kada dobijete sve što trebate, samo isključite **auto extend range** da biste ga zaključali.
{% endhint %}

* **leave all notes visible** – stvara zrake ili oblike za sve note u rasponu, bez obzira na to sviraju li se ili ne, čime dobivate efekt „laserske harfe”.
* **hit colour** – boja koja se pojavljuje kada se nota pokrene.
* **hit colour hold time** – koliko dugo boja okidanja ostaje na punoj svjetlini prije nego što počne blijedjeti. Vrijednost je u sekundama (0–1). _100% = 1 sekunda._
* **hit colour decay time** – koliko je vremena potrebno da se boja okidanja vrati nakon vremena zadržavanja. Vrijednost je u sekundama (0–1). _100% = 1 sekunda._

{% hint style="info" %}
Ako je vaš sadržaj već potpuno bijel, postavljanje boje okidanja na bijelu neće ništa promijeniti. Za najbolje rezultate upotrijebite zasićenu boju za sadržaj i postavite boju okidanja na bijelu — to daje vrlo lijep efekt bljeska kada se note pokrenu.
{% endhint %}

* **note off fade out time** – koliko dugo nota blijedi nakon što se otpusti. Vrijednost je u sekundama (0–1). _100% = 1 sekunda._
* **hit scale factor** – koliko se nota poveća kada se pokrene (npr. 2 = dvostruka veličina).
* **hit scale hold time** – koliko dugo nota ostaje povećana prije nego što se vrati na izvornu veličinu. Vrijednost je u sekundama (0–1). _100% = 1 sekunda._
* **hit scale decay time** – koliko je vremena potrebno da se nota vrati na izvornu veličinu. Vrijednost je u sekundama (0–1). _100% = 1 sekunda._
* **note off shrink time** – koliko je vremena potrebno da se nota smanji na izvornu veličinu nakon što je otpuštena. Vrijednost je u sekundama (0–1). _100% = 1 sekunda._ (Nema učinka kada je uključeno **leave all notes visible**.)

{% hint style="info" %}
Skaliranje — imajte na umu da skaliranje neće imati učinka ako je vaš sadržaj samo jedna točka!
{% endhint %}
