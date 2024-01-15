# 弹性布局（Flex）

更新时间: 2024-01-15 12:18

## 概述

弹性布局（[Flex](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-flex-0000001427902472-V3)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。弹性布局在开发场景中用例特别多，比如页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等等。

图1 主轴为水平方向的Flex容器示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.41098908374020862675743668937095:50001231000000:2800:274648DD02D0CC3CB745723ADDCE77D55DCEE14C135B7F80D0E092329503EE65.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。

* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置参数direction，可以决定主轴的方向，从而控制子组件的排列方向。

图2 弹性布局方向图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.60021406997536400704277300397495:50001231000000:2800:86A3B13B0D090964887A285B96967660DC266825B93ED1F81F03924998F1ECEE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* FlexDirection.Row（默认值）：主轴为水平方向，子组件从起始端沿着水平方向开始排布。

```
Flex({ direction: FlexDirection.Row }) {
  Text('1').width('33%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('33%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.46970331529008185416727905484219:50001231000000:2800:93D85884A880BA799E89414B897F2BBF540715BD5ECC421E667D89B4BB3638AA.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexDirection.RowReverse：主轴为水平方向，子组件从终点端沿着FlexDirection. Row相反的方向开始排布。

```
Flex({ direction: FlexDirection.RowReverse }) {
  Text('1').width('33%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('33%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.91834465828141973882040833489017:50001231000000:2800:1DAEA2C0D2D3CD3C0829080E96EFB0568F09E9EC087767F1273622B37DC9F445.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexDirection.Column：主轴为垂直方向，子组件从起始端沿着垂直方向开始排布。

```
Flex({ direction: FlexDirection.Column }) {
  Text('1').width('100%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('100%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('100%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.08016024279592011872238833420256:50001231000000:2800:81A6377ABC081A2AD2AF9E1903A10457580EDC8F718343399A05EA782A86E9EC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexDirection.ColumnReverse：主轴为垂直方向，子组件从终点端沿着FlexDirection. Column相反的方向开始排布。

```
Flex({ direction: FlexDirection.ColumnReverse }) {
  Text('1').width('100%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('100%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('100%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.09309466297851093339936954889449:50001231000000:2800:6A6F90B157CC72C44DCBD503E2E5A744C36C032C68281B7A067E3C10B236D65D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行堆叠方向。

* FlexWrap. NoWrap（默认值）：不换行。如果子组件的宽度总和大于父元素的宽度，则子组件会被压缩宽度。

```
Flex({ wrap: FlexWrap.NoWrap }) {
  Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
} 
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.28261167876429188617788866218985:50001231000000:2800:AA9C91A65A0D79C6486619765C5CAD10C8184C93C60FDBBC25E43401810A63E8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexWrap. Wrap：换行，每一行子组件按照主轴方向排列。

```
Flex({ wrap: FlexWrap.Wrap }) {
  Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('50%').height(50).backgroundColor(0xD2B48C)
} 
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.63161945379946973975327620051755:50001231000000:2800:5440EF940795E7AB146CF99B60457809D47A08A200446DAA61CC7E615475C40C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexWrap. WrapReverse：换行，每一行子组件按照主轴反方向排列。

```
Flex({ wrap: FlexWrap.WrapReverse}) {
  Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.79558311872469624950014388902696:50001231000000:2800:7E97BCBB041CFEB6F958422BDE143BCCC7CAAC0E725BDC66612AC832890AA6C4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 主轴对齐方式

通过justifyContent参数设置在主轴方向的对齐方式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.06974291234020504015090768435272:50001231000000:2800:563A7A66126DB6094173B36EC56735E0A8A0A881FEE8B2C083A669E6E9C73D65.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* FlexAlign.Start（默认值）：子组件在主轴方向起始端对齐， 第一个子组件与父元素边沿对齐，其他元素与前一个元素对齐。

```
Flex({ justifyContent: FlexAlign.Start }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)    
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.95464514466420734294902746063409:50001231000000:2800:AA67B5B8BB01D720F8C2382CB5C9BEEC32B5BB3398787EBAD3B9548E0961DD47.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.Center：子组件在主轴方向居中对齐。

```
Flex({ justifyContent: FlexAlign.Center }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.97028034996780382958321313386590:50001231000000:2800:905CA05A65754598A3D887C11921FE629EAED1B57A1C34B1C9C224C82103745A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.End：子组件在主轴方向终点端对齐, 最后一个子组件与父元素边沿对齐，其他元素与后一个元素对齐。

```
Flex({ justifyContent: FlexAlign.End }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.76833920579798885135580709349469:50001231000000:2800:FFE63B7800379C9E624D2658629EB16F363319C9064612C7B1AFBF260B6C5CD8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子组件之间距离相同。第一个子组件和最后一个子组件与父元素边沿对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.95963156913340983848797451470535:50001231000000:2800:F53A7B3348FEFDB5EE27DAB3E6D915AF55F140DAA35DF44245975BBB75F0D3E3.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子组件之间距离相同。第一个子组件到主轴起始端的距离和最后一个子组件到主轴终点端的距离是相邻元素之间距离的一半。

```
Flex({ justifyContent: FlexAlign.SpaceAround }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.87592983601492168352144706875584:50001231000000:2800:5BE887DE026F8B2663A78AD33B4529C2320ABC30608B3EFFCC0C551EF6965868.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子组件之间的间距、第一个子组件与主轴起始端的间距、最后一个子组件到主轴终点端的间距均相等。

```
Flex({ justifyContent: FlexAlign.SpaceEvenly }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.77728741360322784810337463378001:50001231000000:2800:023FE36E02E5F21B701D7C234171D823B9A6DAD1DC3C4AB56BED27A81C59AF19.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过Flex组件的alignItems参数设置子组件在交叉轴的对齐方式。

* ItemAlign.Auto：使用Flex容器中默认配置。

```
Flex({ alignItems: ItemAlign.Auto }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.23278915116746187733363571948310:50001231000000:2800:667743AFC513819C5832ECE23877FD96A62B35A5A9FC8F1A1680A1F2A0B1DFBD.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.Start：交叉轴方向首部对齐。

```
Flex({ alignItems: ItemAlign.Start }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.70694756306687989087245254218698:50001231000000:2800:7D60EC9F000F32B414A5401A39E258D82CDACC1A37164AA514B8C164417475E6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.Center：交叉轴方向居中对齐。

```
Flex({ alignItems: ItemAlign.Center }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.87592845340755307375145954416047:50001231000000:2800:D76322476A52968D1CAFAEF87BBD9487B11EF132DF030CBFEE198D31F73B7C44.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.End：交叉轴方向底部对齐。

```
Flex({ alignItems: ItemAlign.End }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.88133592144840009949703573338443:50001231000000:2800:909307D8227E921FA69D1D861610FCCBE7785A4E52E162FA116F7B0363D4FAAD.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。

```
Flex({ alignItems: ItemAlign.Stretch }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.04897240815671459005780517393137:50001231000000:2800:8578B4F8A137BAD24B2626BD29D10703EF2EBDD6849E84ECAF72E6E78118A962.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign. Baseline：交叉轴方向文本基线对齐。

```
Flex({ alignItems: ItemAlign.Baseline }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.44901746859068267151276034528449:50001231000000:2800:3A8AD1EEE2658A9C2649EF801910A864A2A9E33B2F6E4C2026E96F484024CE53.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 子组件设置交叉轴对齐

子组件的[alignSelf](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性也可以设置子组件在父容器交叉轴的对齐格式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

```
Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) { // 容器组件设置子组件居中
  Text('alignSelf Start').width('25%').height(80)
    .alignSelf(ItemAlign.Start)
    .backgroundColor(0xF5DEB3)
  Text('alignSelf Baseline')
    .alignSelf(ItemAlign.Baseline)
    .width('25%')
    .height(80)
    .backgroundColor(0xD2B48C)
  Text('alignSelf Baseline').width('25%').height(100)
    .backgroundColor(0xF5DEB3)
    .alignSelf(ItemAlign.Baseline)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor(0xD2B48C)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor(0xF5DEB3)

}.width('90%').height(220).backgroundColor(0xAFEEEE)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.58967021566928478019773387587842:50001231000000:2800:6DCA546B2F15254EBB9C4114A56C48D6AE24F2E341C1677D9B3F20BD9CB65C3D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

上例中，Flex容器中alignItems设置交叉轴子组件的对齐方式为居中，子组件自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-flex-0000001427902472-V3)参数设置子组件各行在交叉轴剩余空间内的对齐方式，只在多行的flex布局中生效，可选值有：

* FlexAlign.Start：子组件各行与交叉轴起点对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.33300533070591199790569141830855:50001231000000:2800:BF393B0052EE1884EFDCF373BDF79F51020A74DFCD80E5460DC6C1DC2D336940.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.Center：子组件各行在交叉轴方向居中对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.05882808582582916152351736660192:50001231000000:2800:EBB4F6194AED80E5F11CC4CA1ED1ADA1309BDC55CD2592C9C722BBC1E987306F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.End：子组件各行与交叉轴终点对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.01807846917610542985277911102807:50001231000000:2800:C405840577DC6137F465C964CB95546A58EFC2B4EAF229B9A269D9F65C138775.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceBetween：子组件各行与交叉轴两端对齐，各行间垂直间距平均分布。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.53014585466231773856389118137867:50001231000000:2800:F359070A9EECCDB4D737E69A73D2B871C24721AE2B58CAD16D7EAB270B49BF7A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceAround：子组件各行间距相等，是元素首尾行与交叉轴两端距离的两倍。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.64742442774703922888861312312600:50001231000000:2800:2703BB9CD03E5AF471AA69842B3D1FAD791661D8A5F45C30AFED42E11AD16F91.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceEvenly: 子组件各行间距，子组件首尾行与交叉轴两端距离都相等。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.75219968475760655489964056165598:50001231000000:2800:F77B3D6DD0A2A6DA646BC7726D5D2A25AE4C7ECF43BDB310E7A7C816A3D75AEF.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自适应拉伸

在弹性布局父组件尺寸不够大的时候，通过子组件的下面几个属性设置其在父容器的占比，达到自适应布局能力。

* flexBasis：设置子组件在父容器主轴方向上的基准尺寸。如果设置了该值，则子项占用的空间为设置的值；如果没设置该属性，那子项的空间为width/height的值。

```
Flex() {
  Text('flexBasis("auto")')
    .flexBasis('auto') // 未设置width以及flexBasis值为auto，内容自身宽松
    .height(100)
    .backgroundColor(0xF5DEB3)
  Text('flexBasis("auto")' + ' width("40%")')
    .width('40%')
    .flexBasis('auto') //设置width以及flexBasis值auto，使用width的值
    .height(100)
    .backgroundColor(0xD2B48C)

  Text('flexBasis(100)') // 未设置width以及flexBasis值为100，宽度为100vp
    .fontSize(15)
    .flexBasis(100)
    .height(100)
    .backgroundColor(0xF5DEB3)

  Text('flexBasis(100)')
    .fontSize(15)
    .flexBasis(100)
    .width(200) // flexBasis值为100，覆盖width的设置值，宽度为100vp
    .height(100)
    .backgroundColor(0xD2B48C)
}.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.45892628655925830306481185553379:50001231000000:2800:E2F7F28D3BD23DA61E8CDED03604250C06DA5EB49CBA6FBF86CB2DF0719A7857.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* flexGrow：设置父容器的剩余空间分配给此属性所在组件的比例。用于“瓜分”父组件的剩余空间。

```
Flex() {
Text('flexGrow(2)')
  .flexGrow(2) 
  .width(100)
  .height(100)
  .backgroundColor(0xF5DEB3)

Text('flexGrow(3)')
  .flexGrow(3)
  .width(100)
  .height(100)
  .backgroundColor(0xD2B48C)

Text('no flexGrow')
  .width(100) 
  .height(100)
  .backgroundColor(0xF5DEB3)
}.width(420).height(120).padding(10).backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.83092017588361824585277293797023:50001231000000:2800:09DA40E437B3BF6BF0983D0B0E87105BE802DC17A72F3DCC2487797C2D430F20.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
  父容器宽度420vp，三个子元素原始宽度为100vp，左右padding为20vp，总和320vp，剩余空间100vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与“瓜分”。
  第一个元素以及第二个元素以2:3分配剩下的100vp。第一个元素为100vp+100vp*2/5=140vp，第二个元素为100vp+100vp*3/5=160vp。
* flexShrink: 当父容器空间不足时，子组件的压缩比例。

```
Flex({ direction: FlexDirection.Row }) {
  Text('flexShrink(3)')
    .fontSize(15)
    .flexShrink(3)
    .width(200)
    .height(100)
    .backgroundColor(0xF5DEB3)

  Text('no flexShrink')
    .width(200)
    .height(100)
    .backgroundColor(0xD2B48C)

  Text('flexShrink(2)')
    .flexShrink(2)
    .width(200)
    .height(100)
    .backgroundColor(0xF5DEB3)
}.width(400).height(120).padding(10).backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.55220725202123017979460093498862:50001231000000:2800:FDD3112C7D4C61F0DDB3BE38F0E7B82AAF634277559CDB63E1FBEC807C0AC5C2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 相关实例

使用弹性布局，可以实现子组件沿水平方向排列，两端对齐，子组件间距平分，竖直方向上子组件居中的效果。

```
@Entry  
@Component
struct FlexExample {
  build() {
    Column() {
      Column({ space: 5 }) {
        Flex({ direction: FlexDirection.Row, wrap: FlexWrap.NoWrap, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
          Text('1').width('30%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('30%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('30%').height(50).backgroundColor(0xF5DEB3)
        }
        .height(70)
        .width('90%')
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%') 
 }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.06523227728508759286492936853514:50001231000000:2800:50F78944F7006F0EC88A1C03E6663CC53A8F35459D176004DAC80B492D143137.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

