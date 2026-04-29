---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Výplně, mask a řazení podle hloubky

### Tahy, výplně a mask

Všimnete si, že některé Creator nodes mají možnost _Fill state_; můžete je vykreslit tahem (obrysem), jako mask (překrytí prvků pod nimi), nebo obojím.

Když tvar vykreslíte jako mask, chová se, jako by byl vyplněný černou, a vše pod ním bude zakryté.

{% hint style="info" %}
Kreslení čáry (neboli _tahu_) laserem je poměrně jednoduché; laser naskenujete od začátku čáry po její konec. A čára je hotová!

Vyplněné tvary jsou ale složitější. Pokud chcete tvar vyplnit barvou, můžete ho ručně vyšrafovat kreslením čar a vyplněním prostoru mezi nimi, ale Liberation to zatím neumí dělat automaticky. A i kdyby to uměl, pořád by skrz něj byly vidět jiné čáry pod ním.

Co ale umíme, je vyplnit tvary _černou_. Liberation na pozadí provádí všechny výpočty potřebné k odstranění obsahu, který leží pod černě vyplněným tvarem. A věřte mi, je to docela piplačka!

Funguje to ale velmi dobře a vytváří iluzi černě vyplněného tvaru.
{% endhint %}

### Řazení podle hloubky

Protože některé tvary mohou _překrýt_ jiné tvary, Liberation je musí seřadit podle hloubky. Ve výchozím nastavení se prvky řadí podle hloubky podle své polohy na ose Z. Pokud jsou na stejné poloze Z, řadí se podle své pozice ve vrstvě, kterou lze změnit pomocí tlačítek _MOVE TO FRONT_ a _MOVE TO BACK_ uvnitř každého Creator.
