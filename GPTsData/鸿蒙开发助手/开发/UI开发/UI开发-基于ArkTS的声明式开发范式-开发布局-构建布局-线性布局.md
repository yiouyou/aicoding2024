# 线性布局（Row/Column）

更新时间: 2024-01-15 12:17

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-row-0000001478061717-V3)和[Column](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-column-0000001478341157-V3)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Column容器内子元素按照垂直方向排列，Row容器内子元素按照水平方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

图1 Column容器内子元素排列示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.10408821819796528460105427538245:50001231000000:2800:7020D904725885BBB8DFA97F7000B1169B0F03A003752ADCC599FFA926F9231B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

图2 Row容器内子元素排列示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.67453062900729220136229791216409:50001231000000:2800:97A61FC171EA973D934D73CFA99CAF2A23088CCAB0CFC76AAFB236A93EFA5920.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 基本概念

* 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。

* 布局子元素：布局容器内部的元素。
* 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向。
* 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向。
* 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

图3 Column容器内排列方向的间距图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.57122332191520882936947620133261:50001231000000:2800:9331A877C0A83673D9B660E76C57559C7890E1BF63C740D4EE5E39DADEB52C17.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.26566956029801473769458710622477:50001231000000:2800:08C7FC016BE6A1C0D87C8E0FE34A7E020F1A292CF78C805F5EF7AC94A2DC3DB0.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### Row容器内排列方向上的间距

图4 Row容器内排列方向的间距图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.14653192204704273583449566542332:50001231000000:2800:006412CCDC5303BB7D1F7CF111C2315C0F38128C09A89554D1F1A6B50FAFF103.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.60008031670206980167100142966498:50001231000000:2800:6FA78A91778FA4BC90D79C2F36B4A81482D4DCD58F0CA8470890ECF25EA8386E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过alignItems属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式。且在各类尺寸屏幕中，表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign类型](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__verticalalign)，水平方向取值为[HorizontalAlign](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__horizontalalign)。

alignSelf属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

图5 Column容器内子元素在水平方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.85069341221009462031012466664099:50001231000000:2800:5D8175B50CA5F4B3D234CB0BB2A81B30AB6EB90B6863F910FCB3F716AA8446FA.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* HorizontalAlign.Start：子元素在水平方向左对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.60951629222264030433705976305174:50001231000000:2800:9E9A896D07D7E19C07B4137A0AB249AAF4AB7BFB0842EB583FAC6A3823DEBF16.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* HorizontalAlign.Center：子元素在水平方向居中对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.02134079336841605583329835444114:50001231000000:2800:6D5DAA3F87B85B51042B8EBA041A1FD6702B10D4D4E596A7822D337868DAC3B4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* HorizontalAlign.End：子元素在水平方向右对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.45977768659527231097394444575888:50001231000000:2800:C067AC79F73961F45A5860428F3596B2814A102962D336BA7D6035A46E9C3165.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### Row容器内子元素在垂直方向上的排列

图6 Row容器内子元素在垂直方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.11789049186891385222200526959821:50001231000000:2800:C166B0BF4B4CEF0453196C4D650D763AAC5C92B44CEC87359F987B90A7C8183D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* VerticalAlign.Top：子元素在垂直方向顶部对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.16676977917735074478869270523658:50001231000000:2800:A6A23DBCC69D796D458C94696CBCA7BC4BBB7BCDCF601CC0BF9AF95ED30D385F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* VerticalAlign.Center：子元素在垂直方向居中对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.19153990809444775569322940073601:50001231000000:2800:119E759DFF1B6AD6D63037EBCDA276D71885FF1D70F67AE60DD1B7D5F9E64D0D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* VerticalAlign.Bottom：子元素在垂直方向底部对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.61859652681513152160987592817819:50001231000000:2800:AAA223331C500D69E20D4A9EC86D0752851E16DE89ADB01FE229A2CDE3532668.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过justifyContent属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

图7 Column容器内子元素在垂直方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.26654709287413811372252601970942:50001231000000:2800:B3BFBA1BC5E0BE898C885784C1F112810D4D96439358BA8A9BDA1BCB9962EE10.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* justifyContent(FlexAlign.Start)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.16919978921459680606731764702340:50001231000000:2800:089440C547E1C002A54FE208B6D4F704AF7D29C788A18E1CE52740954C05F1C2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.94226725638737143810610474432326:50001231000000:2800:295AAE1FDDCB4E46A01F1F71B7E8792AE0238218BD120AC6DB998AD6FEA359F7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.02730687251544179186517905762202:50001231000000:2800:749AD10E32BF7D0A9698730FD175222030C52D1E8F8DBA3D716399B45C1B53FC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Spacebetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.65545086411708198430241459937849:50001231000000:2800:9DDE9E6951ADA63CBD806CDF9A1DD6727C74A40F3820D19FF55CF5CB16D452E1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.77447620657285171184570238222776:50001231000000:2800:DB8B19E25F12C92F6BB7D08FF5992D6D2EA9440AA307D38FBA35987BC357B97B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.76673581595146875257832359880967:50001231000000:2800:5B83349842D8821502294DF4FABA5829502AF57D4C1010AC27194C7A54EAFB6F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### Row容器内子元素在水平方向上的排列

图8 Row容器内子元素在水平方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.46416226973241546619287224558714:50001231000000:2800:B435DD840998053EE65DE53DAF76825218D215205E5CDBA96B2969986231DA62.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* justifyContent(FlexAlign.Start)：元素在水平方向方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.27302699606028731415014500799823:50001231000000:2800:1FC38B85067630BEAFB1C15B48BDA2DF6B5C7686C6AB86300D0E9F024669E158.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Center)：元素在水平方向方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.36573290726626741597352920096217:50001231000000:2800:A05EE09C326620F5A77296033B1467E6F7141E2C38CAEAF639E93DE632652AD1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.End)：元素在水平方向方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.71669053867342696874701662628156:50001231000000:2800:7F1173B64AE71324570E63610750FEC453D3D3FB459EA8A31565F489C7B4DCA6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Spacebetween)：水平方向方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.14665410400511619407800357179280:50001231000000:2800:1DA244465B28A4934DF2A242CE95FC76CC68E02D0DE8C5F17A8F7C2A848610A1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceAround)：水平方向方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.04812205397561032060805302466837:50001231000000:2800:5AABC9F08188AAA041A750B701E89C49C30BAE6A0EA5ED3D4F4B788BF515DDA5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceEvenly)：水平方向方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.41653287622649410605452468673100:50001231000000:2800:8A68DE795AE9E835393A604A42CFD711B8D68B1C73E0BF9C64156113B0523BA4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-blank-0000001428061724-V3)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

```
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch, isOn: true })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}
```

图9 竖屏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.52760781496991050161589218676053:50001231000000:2800:C79F70E4EEE5129F738431C4C9F4C76268107F4F5D43797AA93C209E0EBDF559.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

图10 横屏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.86168917853442316155687297983039:50001231000000:2800:002F0960889940584D82C0CE483EA03FE63ACF6E38C83AC04EF6B9FDA535D82E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自适应缩放

自适应缩放是指子组件随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

* 父容器尺寸确定时，使用layoutWeight属性设置子组件和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

```
@Entry
@Component
struct layoutWeightExample {
  build() {
    Column() {
      Text('1:2:3').width('100%')
      Row() {
        Column() {
          Text('layoutWeight(1)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('layoutWeight(2)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('layoutWeight(3)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')

      }.backgroundColor(0xffd306).height('30%')

      Text('2:5:3').width('100%')
      Row() {
        Column() {
          Text('layoutWeight(2)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('layoutWeight(5)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('layoutWeight(3)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
      }.backgroundColor(0xffd306).height('30%')
    }
  }
}
```

  图11 横屏![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.49888199209215082288559229745576:50001231000000:2800:D06F04BDEDBA457CAFA43E0F8F060DC4143A59EBDDAAA4CBC79227363ED51678.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

  图12 竖屏![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.29623377163851288313519380242426:50001231000000:2800:C5034AB85E841274A2585BA9501B039AAE0EEAA24DB24CDBB363FBD14A6951BF.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 父容器尺寸确定时，使用百分比设置子组件和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

```
@Entry
@Component
struct WidthExample {
  build() {
    Column() {
      Row() {
        Column() {
          Text('left width 20%')
            .textAlign(TextAlign.Center)
        }.width('20%').backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('center width 50%')
            .textAlign(TextAlign.Center)
        }.width('50%').backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('right width 30%')
            .textAlign(TextAlign.Center)
        }.width('30%').backgroundColor(0xF5DEB3).height('100%')
      }.backgroundColor(0xffd306).height('30%')
    }
  }
}
```

  图13 横屏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.62776757713572784142451637775733:50001231000000:2800:A969A4D1E3C2AFFCF6C6FCFE751F1FD2099237032C147806BA010DAC14074997.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  图14 竖屏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.16464389118435932158162742955810:50001231000000:2800:6764773A441B7AECD50CBE2395B251AC9769925AD642A4359D0EEA0D08351569.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。这种方法适用于线性布局中内容无法一屏展示的场景。通常有以下两种实现方式。

* [在List中添加滚动条](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section1958410178617)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过scrollBar属性设置滚动条的常驻状态，edgeEffect属性设置拖动到内容最末端的回弹效果。
* 使用Scroll组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。
  垂直方向布局中使用Scroll组件：

```
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item) => {
          Text(item.toString())
            .width('90%')
            .height(150)
            .backgroundColor(0xFFFFFF)
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .margin({ top: 10 })
        }, item => item)
      }.width('100%')
    }
    .backgroundColor(0xDCDCDC)
    .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.56030495400687142568072148103673:50001231000000:2800:29AA3194299D769D928177D9112ED779950C517E9F6EF3DC5B540978C4A9E054.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
  水平方向布局中使用Scroll组件：

```
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Scroll(this.scroller) {
      Row() {
        ForEach(this.arr, (item) => {
          Text(item.toString())
            .height('90%')
            .width(150)
            .backgroundColor(0xFFFFFF)
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .margin({ left: 10 })
        })
      }.height('100%')
    }
    .backgroundColor(0xDCDCDC)
    .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.06286462041112147965873459754906:50001231000000:2800:044EDFB9E3AF3665D6C4682B9D58ADE5C80652A386FED2ABAFD30F211E38E56B.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

