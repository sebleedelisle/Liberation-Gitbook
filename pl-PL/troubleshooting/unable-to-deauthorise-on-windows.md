---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Nie możesz cofnąć autoryzacji w Windows?

#### Nie możesz cofnąć autoryzacji w Windows?

Jeśli nie możesz cofnąć autoryzacji komputera w Windows, najpierw upewnij się, że cofasz autoryzację licencji w tej samej wersji Liberation, w której została ona pierwotnie autoryzowana, zanim autoryzujesz ją ponownie w innej wersji.

Jeśli to nie pomoże, a używasz wersji wcześniejszej niż 1.0, problem prawdopodobnie wynika ze sposobu, w jaki starsze kompilacje Liberation dla Windows identyfikowały komputer. W tych wersjach system generowania identyfikatora maszyny był mniej niezawodny i w niektórych przypadkach identyfikator mógł zmieniać się między ponownymi uruchomieniami, nawet jeśli sprzęt pozornie się nie zmienił.

Jeśli nie możesz cofnąć autoryzacji i nie przełączałeś się między wersjami, skontaktuj się z support@liberationlaser.com, a ręcznie cofniemy autoryzację maszyny.

**Dlaczego tak się dzieje**

We wczesnych kompilacjach Liberation dla Windows (przed wersją 1.0) używaliśmy zalecanej przez Windows metody systemowej do generowania identyfikatora maszyny. Niestety w niektórych sytuacjach okazała się ona niespójna. Z tego powodu w wersji 1.0 system licencjonowania został przepisany tak, aby korzystał z bardziej niezawodnego zestawu metod, który obecnie działa stabilnie.

W rezultacie identyfikator komputera używany przez starsze wersje Liberation może różnić się od tego używanego przez aktualne wersje. Jeśli identyfikator już się zmienił, cofnięciem autoryzacji musi zająć się ręcznie dział pomocy technicznej.

***
