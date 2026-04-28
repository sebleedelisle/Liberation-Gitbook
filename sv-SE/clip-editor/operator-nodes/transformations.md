---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformationer

## &#x20;Translate

Flyttar allt innehåll längs x-, y- och/eller z-axeln. Observera att koordinatsystemet är centrerat och sträcker sig till +/-200 på x- och y-axeln. Se [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **x** - avståndet som ska flyttas längs x-axeln (vänster - höger).
* **y** - avståndet som ska flyttas längs y-axeln (upp - ned).

#### 3D-alternativ (tillgängliga när 3D är valt)

* **z** - avståndet som ska flyttas längs z-axeln (bakåt och framåt in i skärmen).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Roterar allt innehåll. Värden anges i grader. Se [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - hur mycket innehållet roteras medurs, i grader. Allt roteras runt origo (0,0), mitten.
* **pivot point x / pivot point y** - använd dessa värden för att förskjuta rotationens origo.

#### 3D-alternativ (tillgängliga när 3D är valt)

* **rotation x** - rotation runt x-axeln (pitch).
* **rotation y** - rotation runt y-axeln (yaw).
* **pivot point z** - rotationens förskjutningsposition på z-axeln.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skalar allt innehåll.

* **scale** - skalningsprocenten.
* **scale x / scale y** - använd dessa alternativ om du vill skala horisontellt och/eller vertikalt.

{% hint style="warning" %}
När något skalas till 0% på någon axel försvinner det!
{% endhint %}
