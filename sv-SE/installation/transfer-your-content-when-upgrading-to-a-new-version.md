---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/installation/transfer-your-content-when-upgrading-to-a-new-version
---

# 🟩 Överför ditt innehåll när du uppgraderar till en ny version

Liberation lagrar innehåll i sin arbetsmapp (se [where-to-find-the-working-folder.md](../troubleshooting/where-to-find-the-working-folder.md "mention")), och den ändras vid varje ny versionsutgåva. Om du vill behålla dina arbetsfiler från den gamla versionen i den nya:

1. Öppna den ursprungliga versionen av Liberation
2. Använd _File->Project->Export Project_. Det sparar allt i din Liberation: laserinställningar, timelines, Clip Deck, allt!
3. Stäng den här versionen och öppna sedan den nya versionen av Liberation
4. Använd _File->Project->Import Project_ och välj projektfilen du exporterade i steg 2.

Allt ditt innehåll bör nu finnas i den nya versionen.

#### Behålla flera versioner av Liberation

Innan du installerar en ny version bör du byta namn på den gamla versionen – jag brukar använda versionsnumret, till exempel Liberation103.app (eller .exe på Windows). Du kan behålla hur många versioner av Liberation du vill, men du kan bara köra en åt gången. <br>

#### Om du skrev över din gamla version av Liberation med en nyare version

Det mest tillförlitliga alternativet är att installera om den äldre versionen av Liberation och sedan utföra processen enligt beskrivningen ovan.

Alternativt kan du prova att kopiera din arbetsmapp och byta namn på den till numret för den nya versionen.
