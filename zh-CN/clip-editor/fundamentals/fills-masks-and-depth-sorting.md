---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 填充、Masks 与深度排序

### 线条、填充与 masks

你会注意到某些 Creator nodes 有 _Fill state_ 选项；你可以将它们绘制为线条（轮廓）、作为 mask（覆盖下方内容），或两者兼具。&#x20;

当形状以 mask 方式渲染时，就像填充为黑色一样，下面的内容会被遮挡。&#x20;

{% hint style="info" %}
用激光画线（或 _stroke_）很简单：从起点扫描到终点就行了。&#x20;

但填充形状更难；要将形状填满颜色，你可以用交叉线条来手动填充，但 Liberation 还无法自动做到（目前）。即使做到，你仍会看到下面的线条透出。&#x20;

我们能做的是用 _black_ 来填充形状。底层上，Liberation 会计算并移除被黑色填充形状覆盖的内容。相信我，这很复杂！&#x20;

但效果很好，能营造出黑色填充的错觉。&#x20;
{% endhint %}

### 深度排序

由于某些形状会_遮挡_其他形状，Liberation 需要按深度对它们排序。默认情况下，元素会按 z 位置进行深度排序。如果它们位于相同的 z 位置，则会按层级位置排序；你可以在每个 Creator 中使用 _MOVE TO FRONT_ 和 _MOVE TO BACK_ 按钮来调整层级位置。
