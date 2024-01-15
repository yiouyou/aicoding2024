# 绘制几何图形（Shape）

更新时间: 2024-01-15 12:18

绘制组件用于在页面绘制图形，Shape组件是绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。具体用法请参考[Shape](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-shape-0000001428061768-V3)。

## 创建绘制组件

绘制组件可以由以下两种形式创建：

* 绘制组件使用Shape作为父组件，实现类似SVG的效果。接口调用为以下形式：

```
Shape(value?: PixelMap)
```

  该接口用于创建带有父组件的绘制组件，其中value用于设置绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。

```
Shape() {
  Rect().width(300).height(50)
}
```
* 绘制组件单独使用，用于在页面上绘制指定的图形。有7种绘制类型，分别为[Circle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-circle-0000001427584896-V3)（圆形）、[Ellipse](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-ellipse-0000001427744848-V3)（椭圆形）、[Line](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-line-0000001478181437-V3)（直线）、[Polyline](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-polyline-0000001478341173-V3)（折线）、[Polygon](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-polygon-0000001478061725-V3)（多边形）、[Path](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-path-0000001477981225-V3)（路径）、[Rect](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-rect-0000001427902488-V3)（矩形）。以Circle的接口调用为例：

```
Circle(options?: {width?: string | number, height?: string | number}
```

  该接口用于在页面绘制圆形，其中width用于设置圆形的宽度，height用于设置圆形的高度，圆形直径由宽高最小值确定。

```
Circle({ width: 150, height: 150 })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.78136929670533928090594734757152:50001231000000:2800:94ECF5E2940B5B640B7D44835822C59BE6A356B0D4953B7A8D13B3694417DB3A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 形状视口viewport

```
viewPort{ x?: number | string, y?: number | string, width?: number | string, height?: number | string }
```

形状视口viewport指定用户空间中的一个矩形，该矩形映射到为关联的 SVG 元素建立的视区边界。viewport属性的值包含x、y、width和height四个可选参数，x 和 y 表示视区的左上角坐标，width和height表示其尺寸。

以下3个示例讲解Viewport具体用法：

* 通过形状视口对图形进行放大与缩小。

```
// 画一个宽高都为150的圆
Text('原始尺寸Circle组件')
Circle({width: 75, height: 75}).fill('#E87361')

Row({space:10}) {
  Column() {
    // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为75的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个直径为75的圆。
    // 绘制结束，viewport会根据组件宽高放大两倍
    Text('shape内放大的Circle组件')
    Shape() {
      Rect().width('100%').height('100%').fill('#0097D4')
      Circle({width: 75, height: 75}).fill('#E87361')
    }
    .viewPort({x: 0, y: 0, width: 75, height: 75})
    .width(150)
    .height(150)
    .backgroundColor('#F5DC62')
  }
  Column() {
    // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为300的viewport。用一个绿色的矩形来填充viewport，在viewport中绘制一个直径为75的圆。
    // 绘制结束，viewport会根据组件宽高缩小两倍。
    Text('Shape内缩小的Circle组件')
    Shape() {
      Rect().width('100%').height('100%').fill('#BDDB69')
      Circle({width: 75, height: 75}).fill('#E87361')
    }
    .viewPort({x: 0, y: 0, width: 300, height: 300})
    .width(150)
    .height(150)
    .backgroundColor('#F5DC62')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.27632915883378190726610759818057:50001231000000:2800:889C15BA0EAEFC56347812B78F207DCEF6C2B25B42466ECFB64001B056BC5A15.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 创建一个宽高都为300的shape组件，背景色为黄色，一个宽高都为300的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个半径为75的圆。

```
Shape() {
  Rect().width("100%").height("100%").fill("#0097D4")
  Circle({ width: 150, height: 150 }).fill("#E87361")
}
  .viewPort({ x: 0, y: 0, width: 300, height: 300 })
  .width(300)
  .height(300)
  .backgroundColor("#F5DC62")
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.64179552777583720438997968478456:50001231000000:2800:13327F3392C2ED70E585BAF3239EA21815224E1D13541955DFB90F18B318D55A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个半径为75的圆，将viewport向右方和下方各平移150。

```
Shape() {
  Rect().width("100%").height("100%").fill("#0097D4")
  Circle({ width: 150, height: 150 }).fill("#E87361")
}
  .viewPort({ x: -150, y: -150, width: 300, height: 300 })
  .width(300)
  .height(300)
  .backgroundColor("#F5DC62")
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.13793240393822639957610790020266:50001231000000:2800:CCEF2B0E391DCF2E202A5021DC0C15F297D4877E18C6DF00EA674BE40A2DE7FB.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

绘制组件支持通过各种属性对组件样式进行更改。

* 通过fill可以设置组件填充区域颜色。

```
Path()
  .width(100)
  .height(100)
  .commands('M150 0 L300 300 L0 300 Z')
  .fill("#E87361")
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.77262557094866243853163530469643:50001231000000:2800:3DEAEF28F8E57FEE7A0E5ACC89FDB915429A6A57DF2A30AE865208FEDA01AED0.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过stroke可以设置组件边框颜色。

```
Path()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .commands('M150 0 L300 300 L0 300 Z')
  .stroke(Color.Red)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.95553119255264091231684341299450:50001231000000:2800:5B14B787B6EFCE69E2565CD461B7C7F07CFE8A8C0320EB2E263905E98BCF5A59.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过strokeOpacity可以设置边框透明度。

```
Path()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .commands('M150 0 L300 300 L0 300 Z')
  .stroke(Color.Red)
  .strokeWidth(10)
  .strokeOpacity(0.2)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.99186807267582956783438232424736:50001231000000:2800:62C87ACE36CC38659E62C6763F09E32E9825F2058784D32FA407C1A73CB9022A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过strokeLineJoin可以设置线条拐角绘制样式。拐角绘制样式分为Bevel(使用斜角连接路径段)、Miter(使用尖角连接路径段)、Round(使用圆角连接路径段)。

```
Polyline()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .stroke(Color.Red)
  .strokeWidth(8)
  .points([[20, 0], [0, 100], [100, 90]])
   // 设置折线拐角处为圆弧
  .strokeLineJoin(LineJoinStyle.Round)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.10320095066369038881528492242480:50001231000000:2800:AE0BD18F562101B53F61FE8519DC8D3C0BA2D260DE1C4A0797ADDFB746B76F77.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过strokeMiterLimit设置斜接长度与边框宽度比值的极限值。
  斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。strokeMiterLimit取值需大于等于1，且在strokeLineJoin属性取值LineJoinStyle.Miter时生效。

```
Polyline()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .stroke(Color.Red)
  .strokeWidth(10)
  .points([[20, 0], [20, 100], [100, 100]])
  // 设置折线拐角处为尖角
  .strokeLineJoin(LineJoinStyle.Miter)
  // 设置斜接长度与线宽的比值
  .strokeMiterLimit(1/Math.sin(45))
Polyline()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .stroke(Color.Red)
  .strokeWidth(10)
  .points([[20, 0], [20, 100], [100, 100]])
  .strokeLineJoin(LineJoinStyle.Miter)
  .strokeMiterLimit(1.42)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.03928496003306153883688413289504:50001231000000:2800:B9FB96760F8E92C7370E3F7EC2FC6691D172F0363D05F253DD04D3C335982197.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过antiAlias设置是否开启抗锯齿，默认值为true（开启抗锯齿）。

```
//开启抗锯齿
Circle()
  .width(150)
  .height(200)
  .fillOpacity(0)
  .strokeWidth(5)
  .stroke(Color.Black)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.19813619572308854368922564124744:50001231000000:2800:93457386F1F1B2D41E25029AFF96DD38CC5D463DBABAF9C0741E1612D27838D7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
//关闭抗锯齿
Circle()
  .width(150)
  .height(200)
  .fillOpacity(0)
  .strokeWidth(5)
  .stroke(Color.Black)
  .antiAlias(false)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.71091467993133181863078438767460:50001231000000:2800:512B6DB3D7F97444FBFFD2EE1973AEC245FE0B1E9D6970ED4AC9029374BFD7FD.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 场景示例

* 在Shape的(-80, -5)点绘制一个封闭路径，填充颜色0x317AF7,线条宽度10,边框颜色红色,拐角样式锐角（默认值）。

```
@Entry
@Component
struct ShapeExample {
  build() {
    Column({ space: 10 }) {
      Shape() {
        Path().width(200).height(60).commands('M0 0 L400 0 L400 150 Z')
      }
      .viewPort({ x: -80, y: -5, width: 500, height: 300 })
      .fill(0x317AF7)
      .stroke(Color.Red)
      .strokeWidth(3)
      .strokeLineJoin(LineJoinStyle.Miter)
      .strokeMiterLimit(5)
    }.width('100%').margin({ top: 15 })
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.12221313042066034567406844717340:50001231000000:2800:609D2EC5E6CF482F3D2683E515DFF652DC5ED51131C372ED440C74A16FC8558B.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 绘制一个直径为150的圆，和一个直径为150、线条为红色虚线的圆环（宽高设置不一致时以短边为直径）。

```
@Entry
@Component
struct CircleExample {
  build() {
    Column({ space: 10 }) {
      //绘制一个直径为150的圆
      Circle({ width: 150, height: 150 })
      //绘制一个直径为150、线条为红色虚线的圆环
      Circle()
        .width(150)
        .height(200)
        .fillOpacity(0)
        .strokeWidth(3)
        .stroke(Color.Red)
        .strokeDashArray([1, 2])
    }.width('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.57628415286340532337756764752801:50001231000000:2800:5460C6769BC27A268BF4C7EC99E534926F8F85B9E0BD436A8CB46CFBB7D358F3.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

