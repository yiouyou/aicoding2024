# 文本显示（Text/Span）

更新时间: 2024-01-10 11:33

Text是文本组件，通常用于展示用户的视图，如显示文章的文字。具体用法可参考[Text](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-text-0000001477981201-V3)。

## 创建文本

Text可通过以下两种方式来创建：

* string字符串
```
Text('我是一段文本')
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.93429348121794113363964533464803:50001231000000:2800:B4F99044A8271D5DB3D1B709634820972A5708BBCEC3F89DDF8C71F0C9ECBAE9.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 引用Resource资源资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json。

```
Text($r('app.string.module_desc'))
  .baselineOffset(0)
  .fontSize(30)
  .border({ width: 1 })
  .padding(10)
  .width(300)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.92424685450543855036200257527709:50001231000000:2800:D7406C178FB04D518025FFE8A1888357FBB8F1D245C14E089E0FD96009B01AE2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 添加子组件

[Span](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-span-0000001478181409-V3)只能作为Text组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

* 创建Span。Span组件需要写到Text组件内，单独写Span组件不会显示信息，Text与Span同时配置文本内容内容时，Span内容覆盖Text内容。

```
Text('我是Text') {
  Span('我是Span')
}
.padding(10)
.borderWidth(1)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.77919587967963993642568719202596:50001231000000:2800:CA7CE04AFD390D4E64E90980D0FA79FBF57933B423A91F3D3DFD31FB3937F697.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 设置文本装饰线及颜色。通过decoration设置文本装饰线及颜色。

```
Text() {
  Span('我是Span1，').fontSize(16).fontColor(Color.Grey)
    .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
  Span('我是Span2').fontColor(Color.Blue).fontSize(16)
    .fontStyle(FontStyle.Italic)
    .decoration({ type: TextDecorationType.Underline, color: Color.Black })
  Span('，我是Span3').fontSize(16).fontColor(Color.Grey)
    .decoration({ type: TextDecorationType.Overline, color: Color.Green })
}
.borderWidth(1)
.padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.48233267578523794365253382904643:50001231000000:2800:44DA649656316086B06CA1E2B32B273CE08C88A112C30CA6B2E17651475395BE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过textCase设置文字一直保持大写或者小写状态。

```
Text() {
  Span('I am Upper-span').fontSize(12)
    .textCase(TextCase.UpperCase)
}
.borderWidth(1)
.padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.68306206760767372955690251208521:50001231000000:2800:727D4C08C59BF816C431335D12E3FE4BAA3B158DCF2E322228175492BA3ACB20.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 添加事件。由于Span组件无尺寸信息，事件仅支持点击事件onClick。

```
Text() {
  Span('I am Upper-span').fontSize(12)
    .textCase(TextCase.UpperCase)
    .onClick(()=>{
      console.info('我是Span——onClick')
    })
}
```

## 自定义文本样式

* 通过textAlign属性设置文本对齐样式。

```
Text('左对齐')
  .width(300)
  .textAlign(TextAlign.Start)
  .border({ width: 1 })
  .padding(10)
Text('中间对齐')
  .width(300)
  .textAlign(TextAlign.Center)
  .border({ width: 1 })
  .padding(10)
Text('右对齐')
  .width(300)
  .textAlign(TextAlign.End)
  .border({ width: 1 })
  .padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.35461854621184576358902865027043:50001231000000:2800:2760D979D312DF05111B44C58913A2FD720AB681D0C680072ACCB1E71FB8D682.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 通过textOverflow属性控制文本超长处理，textOverflow需配合maxLines一起使用（默认情况下文本自动折行）。

```
Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow to None text content. This is the setting of textOverflow to Clip text content This is the setting of textOverflow to None text content.')
  .width(250)
  .textOverflow({ overflow: TextOverflow.None })
  .maxLines(1)
  .fontSize(12)
  .border({ width: 1 }).padding(10)
Text('我是超长文本，超出的部分显示省略号。I am an extra long text, with ellipses displayed for any excess。')
  .width(250)
  .textOverflow({ overflow: TextOverflow.Ellipsis })
  .maxLines(1)
  .fontSize(12)
  .border({ width: 1 }).padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.25244512426491378048069280903281:50001231000000:2800:2A9D2E3374CD402343DA71815EBEF1715E6D9F08CAF35B104EC1266D99B449CE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过lineHeight属性设置文本行高。

```
Text('This is the text with the line height set. This is the text with the line height set.')
  .width(300).fontSize(12).border({ width: 1 }).padding(10)
Text('This is the text with the line height set. This is the text with the line height set.')
  .width(300).fontSize(12).border({ width: 1 }).padding(10)
  .lineHeight(20)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.80508978597073240927005799174452:50001231000000:2800:655722990AAD035FD5EA5D4A1BC978D65DA28536E957F18306102669975AA1DB.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过decoration属性设置文本装饰线样式及其颜色。

```
Text('This is the text')
  .decoration({
    type: TextDecorationType.LineThrough,
    color: Color.Red
  })
  .borderWidth(1).padding(10).margin(5)
Text('This is the text')
  .decoration({
    type: TextDecorationType.Overline,
    color: Color.Red
  })
  .borderWidth(1).padding(10).margin(5)
Text('This is the text')
  .decoration({
    type: TextDecorationType.Underline,
    color: Color.Red
  })
  .borderWidth(1).padding(10).margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.81035767760278503071548795344886:50001231000000:2800:6D37F0D3C776D2D5777736A852E765D49F632BFC971F76A4CBA8C53998600BA5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过baselineOffset属性设置文本基线的偏移量。

```
Text('This is the text content with baselineOffset 0.')
  .baselineOffset(0)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
Text('This is the text content with baselineOffset 30.')
  .baselineOffset(30)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)

Text('This is the text content with baselineOffset -20.')
  .baselineOffset(-20)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.36220935520643711697530009641168:50001231000000:2800:B13C408A1DC0166D585ED91796EC154D6427AA0893B4E15E4ED13CCA2381CDEB.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过letterSpacing属性设置文本字符间距。

```
Text('This is the text content with letterSpacing 0.')
  .letterSpacing(0)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
Text('This is the text content with letterSpacing 3.')
  .letterSpacing(3)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
Text('This is the text content with letterSpacing -1.')
  .letterSpacing(-1)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.25095992223348752830318534501455:50001231000000:2800:A01CC27BFAF1251220687B8756B1581F3351171D1DBBA0EAEC339FE492AE73C1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过minFontSize与maxFontSize自适应字体大小，minFontSize设置文本最小显示字号，maxFontSize设置文本最大显示字号，minFontSize与maxFontSize必须搭配同时使用，以及需配合maxline或布局大小限制一起使用，单独设置不生效。

```
Text('我的最大字号为30，最小字号为5，宽度为250，maxLines为1')
  .width(250)
  .maxLines(1)
  .maxFontSize(30)
  .minFontSize(5)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
Text('我的最大字号为30，最小字号为5，宽度为250，maxLines为2')
  .width(250)
  .maxLines(2)
  .maxFontSize(30)
  .minFontSize(5)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
Text('我的最大字号为30，最小字号为15，宽度为250,高度为50')
  .width(250)
  .height(50)
  .maxFontSize(30)
  .minFontSize(15)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
Text('我的最大字号为30，最小字号为15，宽度为250,高度为100')
  .width(250)
  .height(100)
  .maxFontSize(30)
  .minFontSize(15)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.92952318650253509979306874741004:50001231000000:2800:1CC189B1B255B57B4989089BBCE8DE00E7EB56A7CD751980B1A525E1DE2B6B37.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过textCase属性设置文本大小写。

```
Text('This is the text content with textCase set to Normal.')
  .textCase(TextCase.Normal)
  .padding(10)
  .border({ width: 1 })
  .padding(10)
  .margin(5)

// 文本全小写展示
Text('This is the text content with textCase set to LowerCase.')
  .textCase(TextCase.LowerCase)
  .border({ width: 1 })
  .padding(10)
  .margin(5)

// 文本全大写展示
Text('This is the text content with textCase set to UpperCase.')
  .textCase(TextCase.UpperCase)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.67046622923529261862633076150055:50001231000000:2800:5B3667382BD88B6F0B8F50CC02B390B97929222314B4547AB6A0BDCEDA1FED26.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过copyOption属性设置文本是否可复制粘贴。

```
Text("这是一段可复制文本")
  .fontSize(30)
  .copyOption(CopyOptions.InApp)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.75275001077786483108250391280735:50001231000000:2800:52AE3A08C98393E8F50998FE780B7C763E77839AAE5CCEEFA78FC585A68C12D2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

Text组件可以添加通用事件，可以绑定onClick、onTouch等事件来响应操作。

```
Text('点我')
  .onClick(()=>{
      console.info('我是Text的点击响应事件');
   })
```

## 场景示例

```
// xxx.ets
@Entry
@Component
struct TextExample {
  build() {
    Column() {
      Row() {
        Text("1").fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
        Text("我是热搜词条1")
          .fontSize(12)
          .fontColor(Color.Blue)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .fontWeight(300)
        Text("爆")
          .margin({ left: 6 })
          .textAlign(TextAlign.Center)
          .fontSize(10)
          .fontColor(Color.White)
          .fontWeight(600)
          .backgroundColor(0x770100)
          .borderRadius(5)
          .width(15)
          .height(14)
      }.width('100%').margin(5)

      Row() {
        Text("2").fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
        Text("我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2")
          .fontSize(12)
          .fontColor(Color.Blue)
          .fontWeight(300)
          .constraintSize({ maxWidth: 200 })
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        Text("热")
          .margin({ left: 6 })
          .textAlign(TextAlign.Center)
          .fontSize(10)
          .fontColor(Color.White)
          .fontWeight(600)
          .backgroundColor(0xCC5500)
          .borderRadius(5)
          .width(15)
          .height(14)
      }.width('100%').margin(5)

      Row() {
        Text("3").fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })
        Text("我是热搜词条3")
          .fontSize(12)
          .fontColor(Color.Blue)
          .fontWeight(300)
          .maxLines(1)
          .constraintSize({ maxWidth: 200 })
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        Text("热")
          .margin({ left: 6 })
          .textAlign(TextAlign.Center)
          .fontSize(10)
          .fontColor(Color.White)
          .fontWeight(600)
          .backgroundColor(0xCC5500)
          .borderRadius(5)
          .width(15)
          .height(14)
      }.width('100%').margin(5)

      Row() {
        Text("4").fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })
        Text("我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4")
          .fontSize(12)
          .fontColor(Color.Blue)
          .fontWeight(300)
          .constraintSize({ maxWidth: 200 })
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
      }.width('100%').margin(5)
    }.width('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.37405728115610030654692687321589:50001231000000:2800:FF6B1ACE7E8394703159D8A972464EC920589B6378E4FEBD1AC95B65A49AB5B2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

