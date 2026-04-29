---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Nelze deautorizovat ve Windows?

#### Nelze deautorizovat ve Windows?

Pokud se vám nedaří deautorizovat počítač ve Windows, nejprve se ujistěte, že licenci deautorizujete ve stejné verzi Liberation, ve které byla původně autorizována, a teprve potom ji znovu autorizujte v jiné verzi.

Pokud to nepomůže a používáte verzi starší než 1.0, problém pravděpodobně souvisí s tím, jak starší sestavení Liberation pro Windows identifikovala počítač. V těchto verzích byl systém používaný ke generování ID počítače méně spolehlivý a v některých případech se ID mohlo mezi restarty změnit, i když se hardware zjevně nezměnil.

Pokud se nemůžete z deautorizace dostat a nepřepnuli jste mezi verzemi, kontaktujte prosím support@liberationlaser.com a počítač vám můžeme deautorizovat ručně.

**Proč k tomu dochází**

V raných sestaveních Liberation pro Windows (před verzí 1.0) jsme pro generování ID počítače používali doporučenou systémovou metodu Windows. Bohužel se v některých situacích ukázala jako nekonzistentní. Proto byl licenční systém pro verzi 1.0 přepsán tak, aby používal robustnější kombinaci metod, která nyní funguje spolehlivě.

V důsledku toho se ID počítače používané staršími verzemi Liberation může lišit od ID používaného aktuálními verzemi. Pokud se ID už změnilo, musí deautorizaci provést ručně podpora.

***
