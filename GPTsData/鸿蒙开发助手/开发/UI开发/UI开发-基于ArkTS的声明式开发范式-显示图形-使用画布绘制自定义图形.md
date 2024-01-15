# 使用画布绘制自定义图形（Canvas）

更新时间: 2024-01-15 12:19

Canvas提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 使用画布组件绘制自定义图形

可以由以下三种形式在画布绘制自定义图形：

* 使用[CanvasRenderingContext2D对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3)在Canvas画布上绘制。

```
@Entry
@Component
struct CanvasExample1 {
  //用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  //用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      //在canvas中调用CanvasRenderingContext2D对象。
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() => {
          //可以在这里绘制内容。
          this.context.strokeRect(50, 50, 200, 150);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.47468295442360551339405751229852:50001231000000:2800:DDD1CA54B71E4C2A2B53568FBA45C0B0827D7F2CABA8CFE6464408034441D2D7.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 离屏绘制是指将需要绘制的内容先绘制在缓存区，再将其转换成图片，一次性绘制到Canvas上，加快了绘制速度。过程为：

  1. 通过transferToImageBitmap方法将离屏画布最近渲染的图像创建为一个ImageBitmap对象。
  2. 通过CanvasRenderingContext2D对象的transferFromImageBitmap方法显示给定的ImageBitmap对象。

  具体使用参考[OffscreenCanvasRenderingContext2D对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-offscreencanvasrenderingcontext2d-0000001427902492-V3)。

```
@Entry
@Component
struct CanvasExample2 {
//用来配置CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。true表明开启抗锯齿
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
//用来创建OffscreenCanvasRenderingContext2D对象，width为离屏画布的宽度，height为离屏画布的高度。通过在canvas中调用OffscreenCanvasRenderingContext2D对象来绘制。
  private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)
 
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() =>{
          //可以在这里绘制内容
          this.offContext.strokeRect(50, 50, 200, 150);
          //将离屏绘值渲染的图像在普通画布上显示
          let image = this.offContext.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.42524196131382221037681668799167:50001231000000:2800:71040F4F1F22853BCA439DD50F551AD082BE31F0FC98E5159D2D7C566A513956.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  说明

  在画布组件中，通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制时调用的接口相同，另接口参数如无特别说明，单位均为vp。
* 在Canvas上加载Lottie动画时，需要先按照如下方式下载Lottie。

```
import lottie from '@ohos/lottie'
```

  具体接口和示例请参考[Lottie](https://ohpm.openharmony.cn/#/cn/detail/@ohos/lottie)。

## 初始化画布组件

onReady(event: () => void)是Canvas组件初始化完成时的事件回调，调用该事件后，可获取Canvas组件的确定宽高，进一步使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象调用相关API进行图形绘制。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() => {
    this.context.fillStyle = '#0097D4';
    this.context.fillRect(50, 50, 100, 100);
  })
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.26891313029588282994912948303573:50001231000000:2800:7141A51FA4E195018B4149A6C82457A364D255848CDFE24C642D0E180234807D.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 画布组件绘制方式

在Canvas组件生命周期接口onReady()调用之后，开发者可以直接使用canvas组件进行绘制。或者可以脱离Canvas组件和onready生命周期，单独定义Path2d对象构造理想的路径，并在onready调用之后使用Canvas组件进行绘制。

* 通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象直接调用相关API进行绘制。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
    this.context.beginPath();
    this.context.moveTo(50, 50);
    this.context.lineTo(280, 160);
    this.context.stroke();
   })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.69468094294715342608204515898987:50001231000000:2800:BE6DC35A3F0B5ED96F9148F183B00578F7F1AE7C653411D9CE90AD850E34BD2F.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 先单独定义path2d对象构造理想的路径，再通过调用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的stroke接口或者fill接口进行绘制，具体使用可以参考[Path2D对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-components-canvas-path2d-0000001428061772-V3)。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     let region = new Path2D();
     region.arc(100, 75, 50, 0, 6.28);
     this.context.stroke(region);
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.11524447272073294339877526018215:50001231000000:2800:C8098EBA37AFFB9DD044D36ACAA4AD15D0A480ACC82A9824BEE6F53EA0E2B8B2.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 画布组件常用方法

OffscreenCanvasRenderingContext2D对象和CanvasRenderingContext2D对象提供了大量的属性和方法，可以用来绘制文本、图形，处理像素等，是Canvas组件的核心。常用接口有[fill](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__fill)(对封闭路径进行填充）、[clip](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__clip)(设置当前路径为剪切路径)、[stroke](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-components-canvas-canvasrenderingcontext2d-0000001428061816-V3#ZH-CN_TOPIC_0000001574128621__stroke)（进行边框绘制操作）等等，同时提供了[fillStyle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__fillstyle)（指定绘制的填充色）、[globalAlpha](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__globalalpha)（设置透明度）与[strokeStyle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__strokestyle)（设置描边的颜色）等属性修改绘制内容的样式。将通过以下几个方面简单介绍画布组件常见使用方法：

* 基础形状绘制。
  可以通过[arc](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__arc)（绘制弧线路径）、 [ellipse](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__ellipse)（绘制一个椭圆）、[rect](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__rect)（创建矩形路径）等接口绘制基础形状。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     //绘制矩形
     this.context.beginPath();
     this.context.rect(100, 50, 100, 100);
     this.context.stroke();
     //绘制圆形
     this.context.beginPath();
     this.context.arc(150, 250, 50, 0, 6.28);
     this.context.stroke();
     //绘制椭圆
     this.context.beginPath();
     this.context.ellipse(150, 450, 50, 100, Math.PI * 0.25, Math.PI * 0, Math.PI * 2);
     this.context.stroke();
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.76418334241656038967035814198246:50001231000000:2800:4019A204DD491EC9EDFD2B7401BDC62C6201DD1A2378EB603450CC17B6098BCB.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 文本绘制。
  可以通过[fillText](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__filltext)（绘制填充类文本）、[strokeText](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__stroketext)（绘制描边类文本）等接口进行文本绘制。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     //绘制填充类文本
     this.context.font = '50px sans-serif';
     this.context.fillText("Hello World!", 50, 100);
     //绘制描边类文本
     this.context.font = '55px sans-serif';
     this.context.strokeText("Hello World!", 50, 150);
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.49673793291355990078220821223727:50001231000000:2800:BFE812D46B987036EE0436287284379638B2B720F22BE1E4BCB965E6DDD674B5.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 绘制图片和图像像素信息处理。
  可以通过[drawImage](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__drawimage)（图像绘制）、[putImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__putimagedata)（使用[ImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-components-canvas-image-0000001427584952-V3)数据填充新的矩形区域）等接口绘制图片，通过[createImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__createimagedata)（创建新的ImageData 对象）、[getPixelMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__getpixelmap)（以当前canvas指定区域内的像素创建[PixelMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-image-0000001477981401-V3#ZH-CN_TOPIC_0000001523648994__pixelmap7)对象）、[getImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__getimagedata)（以当前canvas指定区域内的像素创建ImageData对象）等接口进行图像像素信息处理。

```
@Entry
@Component
struct GetImageData {
 private settings: RenderingContextSettings = new RenderingContextSettings(true)
 private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
 private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)
 private img:ImageBitmap = new ImageBitmap("/common/images/1234.png")
 
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() =>{
          // 使用drawImage接口将图片画在（0，0）为起点，宽高130的区域
          this.offContext.drawImage(this.img,0,0,130,130);
          // 使用getImageData接口，获得canvas组件区域中，（50，50）为起点，宽高130范围内的绘制内容
          let imagedata = this.offContext.getImageData(50,50,130,130);
          // 使用putImageData接口将得到的ImageData画在起点为（150， 150）的区域中
          this.offContext.putImageData(imagedata,150,150);
          // 将离屏绘制的内容画到canvas组件上
          let image = this.offContext.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.20074442686946558048719322116242:50001231000000:2800:2D55310586F6641A9FC2934225D2B8B0475263074577E36FF98A121087DD3451.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 其他方法。Canvas中还提供其他类型的方法。渐变（[CanvasGradient对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-components-canvas-canvasgradient-0000001478341177-V3)）相关的方法：[createLinearGradient](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__createlineargradient)（创建一个线性渐变色）、[createRadialGradient](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__createradialgradient)（创建一个径向渐变色）等。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     //创建一个径向渐变色的CanvasGradient对象
     let grad = this.context.createRadialGradient(200,200,50, 200,200,200)
     //为CanvasGradient对象设置渐变断点值，包括偏移和颜色
     grad.addColorStop(0.0, '#E87361');
     grad.addColorStop(0.5, '#FFFFF0');
     grad.addColorStop(1.0, '#BDDB69');
     //用CanvasGradient对象填充矩形
     this.context.fillStyle = grad;
     this.context.fillRect(0, 0, 400, 400);
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.48900326339694978662019483576721:50001231000000:2800:A8DB6956E7663CA604E89C8C897A1EFB86EA874A734D82E4C8A59D15E082C226.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 场景示例

* 规则基础形状绘制：

```
@Entry
@Component
struct ClearRect {
 private settings: RenderingContextSettings = new RenderingContextSettings(true);
 private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
 
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() =>{
          // 设定填充样式，填充颜色设为蓝色
          this.context.fillStyle = '#0097D4';
          // 以(50, 50)为左上顶点，画一个宽高200的矩形
          this.context.fillRect(50,50,200,200);
          // 以(70, 70)为左上顶点，清除宽150高100的区域
          this.context.clearRect(70,70,150,100);
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.25174415228801472017747227145886:50001231000000:2800:6A410675FC2C4E388256348F59C201396621E230A44232A513D8B8AFEF8C99E6.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 不规则图形绘制。

```
@Entry
@Component
struct Path2d {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Row() {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#F5DC62')
          .onReady(() =>{
            // 使用Path2D的接口构造一个五边形
            let path = new Path2D();
            path.moveTo(150, 50);
            path.lineTo(50, 150);
            path.lineTo(100, 250);
            path.lineTo(200, 250);
            path.lineTo(250, 150);
            path.closePath();
            // 设定填充色为蓝色
            this.context.fillStyle = '#0097D4';
            // 使用填充的方式，将Path2D描述的五边形绘制在canvas组件内部
            this.context.fill(path);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.44226074908851811461676159441079:50001231000000:2800:7FA74834316AFB5912BAD80390F5563690C01B92FEE492F10C3CA8426C6B5AFF.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

