---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

모든 _Creator_ 노드에는 _Render Profile_ 설정이 있으며, 이 설정은 레이저로 도형을 어떻게 그릴지(또는 _렌더링할지_)를 결정합니다.

**대부분의 용도에서는&#x20;**_**DEFAULT**_**&#x20;설정이면 충분합니다**. 하지만 그래픽이나 복잡한 콘텐츠를 작업하는 경우, 각 도형이 렌더링되는 방식을 더 세밀하게 제어하고 싶을 수 있습니다.

{% hint style="info" %}
대부분의 레이저 소프트웨어와 달리 Liberation은 레이저 컨트롤러로 전달되기 직전에 포인트 스트림을 실시간으로 생성합니다. 따라서 디스크 공간을 크게 절약할 수 있으며, Clip은 미리 렌더링된 MB 단위의 포인트 스트림 대신 몇 kB에 불과합니다.

또한 Clip 자체를 변경하지 않고도, 레이저별로 서로 다른 스캐너 유형에 맞게 동일한 콘텐츠를 조정할 수 있습니다.

자세한 내용은 [◼️ Liberation이 레이저 콘텐츠를 생성하는 방식](../../advanced/how-liberation-generates-laser-content.md)를 참고하세요.
{% endhint %}

미리 설정된 _Render Profiles_는 _DEFAULT_, _FAST_, _DETAIL_ 세 가지입니다.

_**DEFAULT**_ - 대부분의 작업에 가장 적합한 범용 프로파일입니다.

_**FAST** -_ Clip에 콘텐츠가 많고 그중 일부가 매우 단순한 점이나 직선이라면, 이 옵션을 선택했을 때 깜빡임이 줄어들 수 있습니다.

_**DETAIL**_ - 날카로운 모서리가 필요한 도형을 그릴 때 이 옵션을 사용하세요. 다만 스캐너가 더 느리게 움직이므로 출력에 깜빡임이 생길 수 있다는 점을 염두에 두세요.

{% hint style="info" %}
Clip editor 안에서는 Creator를 서로 다른 Render Profile에 할당할 수 있지만, 각 레이저는 스캐너 설정에 따라 이러한 프로파일을 처리합니다. [◼️ 스캐너 프리셋 및 렌더 프로필](../../advanced/scanner-presets.md)를 참고하세요.
{% endhint %}
