# 层叠布局（Stack）

更新时间: 2024-01-15 12:18

## 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-stack-0000001427584888-V3)容器组件实现位置的固定定位与层叠，容器中的子元素（子组件）依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素（子组件）的顺序为Item1->Item2->Item3。

图1 层叠布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.74169199830606561229130479303704:50001231000000:2800:C900AE70985C74FE2C4847C2C4CDD3B0F47E262CBE9652711016626E2D1CC15C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 开发布局

Stack组件为容器组件，容器内可包含各种子组件。其中子组件默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

```
Column(){
  Stack({ }) {
    Column(){}.width('90%').height('100%').backgroundColor('#ff58b87c')
    Text('text').width('60%').height('60%').backgroundColor('#ffc3f6aa')
    Button('button').width('30%').height('30%').backgroundColor('#ff8ff3eb').fontColor('#000')
  }.width('100%').height(150).margin({ top: 50 })
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.65811578815629624853158685265382:50001231000000:2800:14CAEC331AE003730B810F2AFDEAFA93427D441B6DF0C40EDB814D8E9F0BA8B7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 对齐方式

Stack组件通过[alignContent参数](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__alignment)实现位置的相对移动。如图2所示，支持九种对齐方式。

图2 Stack容器内元素的对齐方式
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.52776776731691091772205695450275:50001231000000:2800:C57F38D5D8DA5A8A80731A4B990E99CA43F207986AD0BE87D6D71C54080E6A03.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-z-order-0000001478181381-V3)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

```
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    Text('Stack子元素1').textAlign(TextAlign.End).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306)

  Column() {
    Text('Stack子元素2').fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink)

  Column() {
    Text('Stack子元素3').fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.margin({ top: 100 }).width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.98205936597258763776022376443932:50001231000000:2800:19C8CAF25BEA6524187F43FF1046FA981440B61C42D9895800FF6FE2987C7300.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1，子元素2的zIndex属性后，可以将元素展示出来。

```
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    Text('Stack子元素1').fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)

  Column() {
    Text('Stack子元素2').fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)

  Column() {
    Text('Stack子元素3').fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.margin({ top: 100 }).width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.84274098820616013062971574976199:50001231000000:2800:7579D8D488EF68035F60CCBC9511CD19ADF4C8A6111471E643E635F968E1924E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 场景示例

使用层叠布局快速搭建手机页面显示模型。

```
@Entry
@Component
struct StackSample {
  private arr: string[] = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'];

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Flex({ wrap: FlexWrap.Wrap }) {
        ForEach(this.arr, (item) => {
          Text(item)
            .width(100)
            .height(100)
            .fontSize(16)
            .margin(10)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }, item => item)
      }.width('100%').height('100%')

      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        Text('联系人').fontSize(16)
        Text('设置').fontSize(16)
        Text('短信').fontSize(16)
      }
      .width('50%')
      .height(50)
      .backgroundColor('#16302e2e')
      .margin({ bottom: 15 })
      .borderRadius(15)
    }.width('100%').height('100%').backgroundColor('#CFD0CF')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.28766386625006672473341686670243:50001231000000:2800:6FE6D3838EF2565CE7D4DF01CF03B6B1C22B99A8F9BF9ED945549BAFF9CA870D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

