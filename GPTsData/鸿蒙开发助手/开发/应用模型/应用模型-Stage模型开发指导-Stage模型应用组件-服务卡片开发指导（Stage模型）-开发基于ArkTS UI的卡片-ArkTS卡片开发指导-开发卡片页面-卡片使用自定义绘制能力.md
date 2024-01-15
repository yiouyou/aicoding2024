# 卡片使用自定义绘制能力

更新时间: 2024-01-15 12:24

ArkTS卡片开放了自定义绘制的能力，在卡片上可以通过[Canvas](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-components-canvas-canvas-0000001427744852-V3)组件创建一块画布，然后通过[CanvasRenderingContext2D](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3)对象在画布上进行自定义图形的绘制，如下示例代码实现了在画布的中心绘制了一个笑脸。

```
@Entry
@Component
struct Card {
  private canvasWidth: number = 0;
  private canvasHeight: number = 0;
  // 初始化CanvasRenderingContext2D和RenderingContextSettings
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Row() {
        Canvas(this.context)
          .margin('5%')
          .width('90%')
          .height('90%')
          .onReady(() => {
            console.info('[ArkTSCard] onReady for canvas draw content');
            // 在onReady回调中获取画布的实际宽和高
            this.canvasWidth = this.context.width;
            this.canvasHeight = this.context.height;
            // 绘制画布的背景
            this.context.fillStyle = 'rgba(203, 154, 126, 1.00)';
            this.context.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
            // 在画布的中心绘制一个红色的圆
            this.context.beginPath();
            let radius = this.context.width / 3
            let circleX = this.context.width / 2
            let circleY = this.context.height / 2
            this.context.moveTo(circleX - radius, circleY);
            this.context.arc(circleX, circleY, radius, 2 * Math.PI, 0, true);
            this.context.closePath();
            this.context.fillStyle = 'red';
            this.context.fill();
            // 绘制笑脸的左眼
            let leftR = radius / 4
            let leftX = circleX - (radius / 2)
            let leftY = circleY - (radius / 3.5)
            this.context.beginPath();
            this.context.arc(leftX, leftY, leftR, 0, Math.PI, true);
            this.context.strokeStyle = '#ffff00'
            this.context.lineWidth = 10
            this.context.stroke()
            // 绘制笑脸的右眼
            let rightR = radius / 4
            let rightX = circleX + (radius / 2)
            let rightY = circleY - (radius / 3.5)
            this.context.beginPath();
            this.context.arc(rightX, rightY, rightR, 0, Math.PI, true);
            this.context.strokeStyle = '#ffff00'
            this.context.lineWidth = 10
            this.context.stroke()
            // 绘制笑脸的嘴巴
            let mouthR = radius / 2.5
            let mouthX = circleX
            let mouthY = circleY + (radius / 3)
            this.context.beginPath();
            this.context.arc(mouthX, mouthY, mouthR, Math.PI, 0, true);
            this.context.strokeStyle = '#ffff00'
            this.context.lineWidth = 10
            this.context.stroke()
          })
      }
    }.height('100%').width('100%')
  }
}
```

运行效果如下图所示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183818.58694057328028931819074222153116:50001231000000:2800:D0C9D6067BBC4274904A3414E4F718E02E087BC2E0A782817CC78965E3D5A73B.jpeg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

