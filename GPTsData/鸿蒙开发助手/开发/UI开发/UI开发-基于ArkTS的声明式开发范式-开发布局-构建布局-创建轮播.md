# 创建轮播（Swiper）

更新时间: 2024-01-15 12:23

[Swiper](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-swiper-0000001427744844-V3)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。通常，在一些应用首页显示推荐的内容时，需要用到轮播显示的能力。

## 布局与约束

Swiper作为一个容器组件，在自身尺寸属性未被设置时，会自动根据子组件的大小设置自身的尺寸。如果开发者对Swiper组件设置了固定的尺寸，则在轮播显示过程中均以该尺寸生效；否则，在轮播过程中，会根据子组件的大小自动调整自身的尺寸。

## 循环播放

通过loop属性控制是否循环播放，该属性默认值为true。

当loop为true时，在显示第一页或最后一页时，可以继续往前切换到前一页或者往后切换到后一页。如果loop为false，则在第一页或最后一页时，无法继续向前或者向后切换页面。

loop为true：

```
...
private swiperController: SwiperController = new SwiperController()
...
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Blue)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.loop(true)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.31642353669443233164328904499980:50001231000000:2800:52B054264F875BE2A556116825910CB57C3213F1355110ED8F9D7D390851A28D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

loop为false：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Blue)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.loop(false)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.91103852937824746641345124342516:50001231000000:2800:D192C4557FFB0F67A2192FFD6E8CC125053F68FF7790518990ECC401954C100E.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自动轮播

Swiper通过设置autoPlay属性，控制是否自动轮播子组件。该属性默认值为false。

autoPlay为true时，会自动切换播放子组件，子组件与子组件之间的播放间隔通过interval属性设置。interval属性默认值为3000，单位毫秒。

autoPlay为true：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.loop(true)
.autoPlay(true)
.interval(1000)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.81202262964629428224310900061593:50001231000000:2800:50FD16A3116BB34A04A3206ADA0CB1C61C9729B889B044EF5685A315E44A9D5A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 导航点样式

Swiper提供了默认的导航点样式，导航点默认显示在Swiper下方居中位置，开发者也可以通过indicatorStyle属性自定义导航点的位置和样式。

通过indicatorStyle属性，开发者可以设置导航点相对于Swiper组件上下左右四个方位的位置，同时也可以设置每个导航点的尺寸、颜色、蒙层和被选中导航点的颜色。

导航点使用默认样式：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.09650938221009313693657688266528:50001231000000:2800:2DA6BFFC441F36B340CA027DA81DB27DD986F7ED4E3B1E8068BACFFB46CDEE11.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

自定义导航点样式（示例：导航点直径设为30VP，左边距为0，导航点颜色设为红色）：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.indicatorStyle({
  size: 30,
  left: 0,
  color: Color.Red
})
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.50494487807687429218644629228349:50001231000000:2800:21DE4742102A1274E852B52D9C32215D3C8EF59617379BD8FC6727B9512A015F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 页面切换方式

Swiper支持三种页面切换方式：手指滑动、点击导航点和通过控制器。

通过控制器切换页面：

```
@Entry
@Component
struct SwiperDemo {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        Text("0")
          .width(250)
          .height(250)
          .backgroundColor(Color.Gray)
          .textAlign(TextAlign.Center)
          .fontSize(30)
        Text("1")
          .width(250)
          .height(250)
          .backgroundColor(Color.Green)
          .textAlign(TextAlign.Center)
          .fontSize(30)
        Text("2")
          .width(250)
          .height(250)
          .backgroundColor(Color.Pink)
          .textAlign(TextAlign.Center)
          .fontSize(30)
      }
      .indicator(true)

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext(); // 通过controller切换到后一页
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious(); // 通过controller切换到前一页
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.93289871911183688478456436794437:50001231000000:2800:DDCD6EBB3EE0C1081E411ADF35C8D1009510396C157DB505FA1DEBA7E61EA734.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 轮播方向

Swiper支持水平和垂直方向上进行轮播，主要通过vertical属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

设置水平方向上轮播：

```
Swiper(this.swiperController) {
  ...
}
.indicator(true)
.vertical(false)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.48512939215655935695074689242255:50001231000000:2800:CE932C0858A2F8E260CECBAAA31B0A9FD192FA4834A8057890874709052C13A8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

设置垂直方向轮播：

```
Swiper(this.swiperController) {
  ...
}
.indicator(true)
.vertical(true)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.38349886946585687700614295700064:50001231000000:2800:7AB2C0ABDC9621973880C97F95232A143B93ABCDA0D617BA45A361374C582E2A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 每页显示多个子页面

Swiper支持在一个页面内同时显示多个子组件，通过[displayCount](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-swiper-0000001427744844-V3)属性设置。

设置一个页面内显示两个子组件：

```
Swiper(this.swiperController) {
  Text("0")
    .width(250)
    .height(250)
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)
  Text("1")
    .width(250)
    .height(250)
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)
  Text("2")
    .width(250)
    .height(250)
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
  Text("3")
    .width(250)
    .height(250)
    .backgroundColor(Color.Blue)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.indicator(true)
.displayCount(2)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.65234031092017077969679844708564:50001231000000:2800:014BF58C5F6550A5F2AEDD767DA591482F8C8B75B9B391B4A3FC82D70F5F52DF.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

