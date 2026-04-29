---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Používání Liberation s Capture

Liberation podporuje [Capture](https://capture.se) jako externí vizualizér (od verze 1.0.3). Pokud už Capture používáte ve svém workflow, můžete jej využít k vizualizaci živého laserového výstupu z Liberation ve své 3D scéně.

### Jak to funguje

Není potřeba žádný speciální postup připojení ani ruční propojení.

Stačí, aby:

* Liberation a Capture byly ve stejné síti
* váš firewall připojení povoloval

…a všechny lasery nastavené v Liberation se automaticky zobrazí v Capture jako zdroje médií. Nemusíte konfigurovat IP adresy ani nic speciálně zapínat – prostě se objeví.

### Zobrazení laserů v Capture

Všechny nakonfigurované lasery v Liberation se v Capture zobrazí jako dostupné zdroje médií.

Aby byl výstup skutečně vidět:

* laser musí být v Liberation ve stavu armed
* zdroj musí být v Capture připojen k laserovému fixture

Jakmile je laser ve stavu armed, Capture bude vizualizovat živý výstupní stream z Liberation. Pokud je laser v Liberation ve stavu disarmed, zůstane v Capture viditelný jako zdroj, ale nebude nic vysílat.

Další pokyny a podporu pro nastavení laserů v Capture najdete v dokumentaci na webu [capture.se](https://www.capture.se/). <br>

### Limity licence a lasery ve stavu armed

Připojení Capture se počítají úplně stejně jako fyzické laserové výstupy.

To znamená:

* ve stavu armed můžete mít jen tolik laserů, kolik dovoluje vaše licenční úroveň
* data do Capture budou aktivně odesílat pouze lasery ve stavu armed

### Potřebuji Capture?

Vůbec ne.

Liberation obsahuje vestavěný 3D vizualizér, který je vždy k dispozici a nezávisí na vaší licenční úrovni. Show můžete navrhovat a prohlížet přímo v Liberation bez jakéhokoli externího softwaru.

Capture je jednoduše další možnost, pokud jej už používáte pro návrh světel nebo show.

### Řešení problémů

Pokud se lasery v Capture nezobrazují:

* zkontrolujte, že jsou obě aplikace ve stejné síti
* zkontrolujte nastavení firewallu
* ujistěte se, že je laser v Liberation ve stavu armed
