---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator 노드

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

단일 점/빔을 만듭니다.

* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **Colour** - 점의 색상입니다. [색상 설정 및 HSB](fundamentals/colour-settings-and-hsb.md "mention") 참조
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

선/시트를 만듭니다.

* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **Size** - 선의 길이입니다.
* **Colour** - 선의 색상입니다. [색상 설정 및 HSB](fundamentals/colour-settings-and-hsb.md "mention") 참조
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* **rotation** - 선의 각도입니다. 단위는 도입니다.
* **resolution** - [Resolution](fundamentals/resolution.md "mention") 참조
* **alignment** - _LEFT / CENTRE / RIGHT -_ 선의 시작점과 회전 중심을 결정합니다.
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

원/콘을 만듭니다.

* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **radius** - 원의 반지름입니다.
* **Colour** - 원의 색상입니다. [색상 설정 및 HSB](fundamentals/colour-settings-and-hsb.md "mention") 참조
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* **resolution** - [Resolution](fundamentals/resolution.md "mention") 참조
* **Fill state** - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

삼각형, 사각형, 오각형 등 정다각형을 만듭니다.

* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **size** - 중심에서 각 꼭짓점까지의 거리입니다.
* **Colour** - 다각형의 색상입니다. [색상 설정 및 HSB](fundamentals/colour-settings-and-hsb.md "mention") 참조
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* **rotation** - 도형이 회전된 각도입니다. 단위는 도입니다.
* **resolution** - [Resolution](fundamentals/resolution.md "mention") 참조
* **Fill state** - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

사용자 지정 도형용 SVG 파일을 불러옵니다.

{% hint style="warning" %}
Liberation은 _SVGTiny_ 형식과 호환됩니다. InkScape 사용을 권장하지만, 대부분의 벡터 그래픽 앱에서도 이 형식으로 내보낼 수 있습니다. 내보내기 전에 모든 텍스트를 도형으로 변환하세요. Liberation은 스트로크를 렌더링하며, 선택적으로 채우기를 마스크로 사용할 수 있습니다. 선이 검은색이면 colour modifier 없이는 보이지 않으므로 주의하세요!
{% endhint %}

* **Import SVG** - 디스크에서 SVG 파일을 불러옵니다.

{% hint style="info" %}
SVG가 로드되면 콘텐츠가 변환되어 clip 안에 저장됩니다. 따라서 나중에 마스크 설정을 변경하려는 경우가 아니라면 원본 파일을 계속 참조할 필요가 없습니다.
{% endhint %}

* **Use fills as masks** - 채워진 도형을 마스크로 처리합니다. 즉 검은색으로 채워진 것으로 처리됩니다. SVG에 채워진 도형이 있으면 자동으로 설정됩니다. 채워진 도형이 없으면 비활성화됩니다. [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조
* **Add outlines to filled shapes** - SVG의 도형에 윤곽선이 없으면 그릴 수 없습니다! 이 옵션은 채워진 도형에 윤곽선(또는 _stroke_)을 추가합니다. SVG에 스트로크가 있는 도형이 없으면 자동으로 설정됩니다. 채워진 도형이 없으면 비활성화됩니다.
* **Invert black lines** - SVG의 모든 선이 검은색이면 보이지 않습니다! 이 옵션은 선을 흰색으로 바꿉니다. SVG에 검은색 도형만 있으면 자동으로 설정되지만, 해당 도형이 없으면 비활성화됩니다.
* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **scale** - SVG의 크기를 조정합니다. SVG가 로드될 때 이미지가 보이도록 자동 계산되지만, 이후 수동으로 편집할 수 있습니다.
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* **rotation** - 이미지가 회전된 각도입니다. 단위는 도입니다.
* **resolution** - [Resolution](fundamentals/resolution.md "mention") 참조
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

SVG 파일 시퀀스로 애니메이션을 만듭니다.

* **Import SVG Sequence** - 모든 SVG 파일이 들어 있는 폴더를 선택합니다. 파일은 영숫자 순서로 로드됩니다.

{% hint style="info" %}
SVG 시퀀스가 로드되면 콘텐츠가 변환되어 clip 안에 저장됩니다. 따라서 나중에 마스크 설정을 변경하려는 경우가 아니라면 원본 파일을 계속 참조할 필요가 없습니다.
{% endhint %}

* **Use fills as masks** - 채워진 도형을 마스크로 처리합니다. 즉 검은색으로 채워진 것으로 처리됩니다. SVG 중 하나라도 채워진 도형이 있으면 자동으로 설정됩니다. 채워진 도형이 하나도 없으면 비활성화됩니다. [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조
* **Add outlines to filled shapes** - SVG의 도형에 윤곽선이 없으면 그릴 수 없습니다! 이 옵션은 채워진 도형에 윤곽선(또는 _stroke_)을 추가합니다. SVG에 스트로크가 있는 도형이 없으면 자동으로 설정됩니다. 채워진 도형이 하나도 없으면 비활성화됩니다.
* **Invert black lines** - SVG의 모든 선이 검은색이면 보이지 않습니다! 이 옵션은 선을 흰색으로 바꿉니다. SVG에 검은색 도형만 있으면 자동으로 설정되지만, 해당 도형이 없으면 비활성화됩니다.
* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **scale** - 이미지의 크기를 조정합니다.
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* **rotation** - 이미지가 회전된 각도입니다. 단위는 도입니다.
* **resolution** - [Resolution](fundamentals/resolution.md "mention") 참조
* **speed** - 전체 애니메이션의 길이입니다. 단위는 마디입니다.
* **time per frame** - 이 옵션을 설정하면 duration이 전체 애니메이션 길이가 아니라 프레임별 길이로 적용됩니다. 따라서 _speed_가 ¼로 설정되어 있으면 각 프레임은 1비트가 됩니다.
* **animation direction** -
  * _FORWARDS_ - 애니메이션이 정방향으로 실행된 뒤 처음으로 돌아가 반복됩니다.
  * _BACKWARDS_ - 애니메이션이 역방향으로 실행된 뒤 끝으로 돌아가 반복됩니다.
  * _PINGPONG_ - 애니메이션이 정방향으로 실행된 뒤 역방향으로 실행되며 반복됩니다.
  * _MANUAL_ - 현재 프레임을 _position manual_ 설정으로 지정합니다.
* **position manual** - 현재 프레임을 설정합니다. 0%는 첫 번째 프레임, 100%는 마지막 프레임입니다. 수동으로 설정하거나 외부 oscillator로 설정할 수 있습니다.
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

TrueType 또는 OpenType 글꼴을 사용해 텍스트를 만듭니다.

* **Text** - 여기에 원하는 텍스트를 입력합니다.
* **Font** - 원하는 글꼴을 선택합니다.

{% hint style="info" %}
Liberation에 글꼴을 더 추가하려면 .ttf 또는 .otf 파일을 Liberation 작업 폴더 안의 `data/fonts` 폴더에 복사한 다음 Liberation을 다시 시작하세요.
{% endhint %}

* **Render profile** - [Render profile](fundamentals/render-profile.md "mention") 참조
* **horizontal alignment** - 텍스트 정렬을 선택하려면 _LEFT_, _CENTRE_, 또는 _RIGHT_를 선택합니다.
* **Fill state** - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조
* **size** - 텍스트 크기입니다.
* **monospace** - 모든 문자를 같은 너비로 그립니다. 숫자가 바뀔 때 텍스트가 좌우로 흔들리지 않으므로 타이머와 카운터에 유용합니다.
* **character spacing** - 문자 사이의 간격을 조정합니다. 자간을 넓히려면 값을 높이고, 텍스트를 더 촘촘하게 만들려면 값을 낮추세요.
* **colour -** [색상 설정 및 HSB](fundamentals/colour-settings-and-hsb.md "mention") 참조
* **x** 및 **y** position - [좌표계](fundamentals/co-ordinate-system.md "mention") 참조
* **rotation** - 이미지가 회전된 각도입니다. 단위는 도입니다.
* **resolution** - [Resolution](fundamentals/resolution.md "mention") 참조
* **reveal** - 텍스트를 한 글자씩 서서히 표시할 때 사용합니다. 값이 0~50% 사이이면 텍스트가 왼쪽에서 오른쪽으로 점차 나타납니다. 50~100% 사이이면 텍스트가 왼쪽에서 오른쪽으로 사라집니다. 이 소켓에 oscillator를 연결해 애니메이션을 만들 수 있습니다.
* **reveal by word** - 설정하면 _reveal_이 문자 단위가 아니라 단어 단위로 동작합니다.
* **countdown** - 입력한 텍스트를 카운트다운으로 대체합니다. 카운트다운이 0에 도달하면 일반 **Text** 값이 표시됩니다.
* **use seconds** - 실제 초 단위로 셉니다. 이 옵션이 꺼져 있으면 카운트다운은 비트 기준으로 동작합니다. 두 비트가 1초로 계산되므로 120bpm에서 실제 초와 일치합니다.
* **show minutes/seconds** - 남은 시간을 분과 초로 표시합니다. 1시간을 넘으면 시간도 함께 표시합니다.
* **countdown to date/time** - 숫자에서 줄여 세는 대신 특정 UTC 날짜와 시간까지 카운트다운합니다.
* **countdown datetime** - **countdown to date/time**이 켜져 있을 때 UTC 대상 날짜/시간을 설정합니다.
* **start number** - **countdown to date/time**이 꺼져 있을 때의 시작 숫자입니다.
* _MOVE TO FRONT / MOVE TO BACK_ - [채우기, 마스크, 깊이 정렬](fundamentals/fills-masks-and-depth-sorting.md "mention") 참조

{% hint style="info" %}
글꼴 드롭다운 메뉴가 열려 있으면 위쪽 및 아래쪽 화살표 키로 사용 가능한 글꼴을 차례로 선택할 수 있습니다.
{% endhint %}
