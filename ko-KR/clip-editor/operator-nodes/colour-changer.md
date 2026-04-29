---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

설명

* **hue, saturation, brightness** - 색상 값입니다. [색상 설정 및 HSB](../fundamentals/colour-settings-and-hsb.md)를 참고하세요.
* **hue mode** -
  * OFF - hue가 변경되지 않습니다.
  * FIXED - 요소의 hue가 hue 값으로 설정됩니다.
  * SHIFT - 요소의 hue가 해당 값만큼 오프셋됩니다. 따라서 서로 다른 색상의 요소는 서로 다른 상태를 유지하면서 hue 값에 따라 이동됩니다.
* **saturation mode** -
  * OFF - saturation이 변경되지 않습니다.
  * FIXED - saturation이 지정한 값으로 고정됩니다.
* **brightness mode** -
  * OFF - brightness가 변경되지 않습니다.
  * FIXED - 요소의 brightness가 brightness 값으로 설정됩니다.
  * MULTIPLY - 요소의 brightness가 brightness 값과 결합됩니다. 따라서 깜빡이는 요소는 계속 깜빡이지만, 여기서 지정한 brightness까지만 표시됩니다.
* **blend** - Colour changer가 적용되는 강도입니다. 0%는 전혀 적용하지 않음, 100%는 완전히 적용함, 50%는 기존 색상과 새 값을 조합한 상태입니다.
