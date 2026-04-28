---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Trasformazioni

## &#x20;Translate

Sposta tutto il contenuto lungo gli assi x, y e/o z. Tieni presente che il sistema di coordinate è centrato e si estende fino a +/-200 sugli assi x e y. Vedi [co-ordinate-system.md](../fundamentals/co-ordinate-system.md).

* **x** - la distanza di spostamento lungo l’asse x (sinistra - destra).
* **y** - la distanza di spostamento lungo l’asse y (alto - basso).

#### Opzioni 3D (disponibili quando 3D è selezionato)

* **z** - la distanza di spostamento lungo l’asse z (indietro e in avanti dentro lo schermo).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Ruota tutto il contenuto. I valori sono espressi in gradi. Vedi [co-ordinate-system.md](../fundamentals/co-ordinate-system.md).

* **rotation** - la quantità di rotazione del contenuto in senso orario, in gradi. Tutto viene ruotato attorno all’origine (0,0), cioè il centro.
* **pivot point x / pivot point y** - usa questi valori per spostare l’origine della rotazione.

#### Opzioni 3D (disponibili quando 3D è selezionato)

* **rotation x** - rotazione attorno all’asse x (pitch).
* **rotation y** - rotazione attorno all’asse y (yaw).
* **pivot point z** - posizione di offset della rotazione sull’asse z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Scala tutto il contenuto.

* **scale** - la percentuale di scala.
* **scale x / scale y** - se vuoi scalare in orizzontale e/o in verticale, usa queste opzioni.

{% hint style="warning" %}
Quando qualcosa viene scalato allo 0% su un qualsiasi asse, scompare!
{% endhint %}
