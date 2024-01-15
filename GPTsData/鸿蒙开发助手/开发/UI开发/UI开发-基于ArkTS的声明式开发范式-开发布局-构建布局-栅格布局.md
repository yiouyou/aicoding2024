# 栅格布局（GridRow/GridCol）

更新时间: 2024-01-10 11:33

## 概述

栅格布局是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。主要优势包括：

1. 提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
2. 统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
3. 灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
4. 自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。

[GridRow](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-gridrow-0000001478181425-V3)为栅格容器组件，需与栅格子组件[GridCol](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-gridcol-0000001427744832-V3)在栅格布局场景中联合使用。

## 栅格容器GridRow

### 栅格系统断点

栅格系统以设备的水平宽度（[屏幕密度像素值](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-pixel-units-0000001478341189-V3)，单位vp）作为断点依据，定义设备的宽度类型，形成了一套断点规则。开发者可根据需求在不同的断点区间实现不同的页面布局效果。

栅格系统默认断点将设备宽度分为xs、sm、md、lg四类，尺寸范围如下：

| 断点名称 | 取值范围（vp） | 设备描述           |
| :------- | :------------- | :----------------- |
| xs       | [0, 320）      | 最小宽度类型设备。 |
| sm       | [320, 520)     | 小宽度类型设备。   |
| md       | [520, 840)     | 中等宽度类型设备。 |
| lg       | [840, +∞)     | 大宽度类型设备。   |

在GridRow栅格组件中，允许开发者使用breakpoints自定义修改断点的取值范围，最多支持6个断点，除了默认的四个断点外，还可以启用xl，xxl两个断点，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备的布局设置。

| 断点名称 | 设备描述           |
| :------- | :----------------- |
| xs       | 最小宽度类型设备。 |
| sm       | 小宽度类型设备。   |
| md       | 中等宽度类型设备。 |
| lg       | 大宽度类型设备。   |
| xl       | 特大宽度类型设备。 |
| xxl      | 超大宽度类型设备。 |

* 针对断点位置，开发者根据实际使用场景，通过一个单调递增数组设置。由于breakpoints最多支持六个断点，单调递增数组长度最大为5。

```
breakpoints: {value: ['100vp', '200vp']}
```

  表示启用xs、sm、md共3个断点，小于100vp为xs，100vp-200vp为sm，大于200vp为md。

```
breakpoints: {value: ['320vp', '520vp', '840vp', '1080vp']}
```

  表示启用xs、sm、md、lg、xl共5个断点，小于320vp为xs，320vp-520vp为sm，520vp-840vp为md，840vp-1080vp为lg，大于1080vp为xl。
* 栅格系统通过监听窗口或容器的尺寸变化进行断点，通过reference设置断点切换参考物。 考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。

例如，使用栅格的默认列数12列，通过断点设置将应用宽度分成六个区间，在各区间中，每个栅格子元素占用的列数均不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow({
  breakpoints: {
    value: ['200vp', '300vp', '400vp', '500vp', '600vp'],
    reference: BreakpointsReference.WindowSize
  }
}) {
   ForEach(this.bgColors, (color, index) => {
     GridCol({
       span: {
         xs: 2, // 在最小宽度类型设备上，栅格子组件占据的栅格容器2列。
         sm: 3, // 在小宽度类型设备上，栅格子组件占据的栅格容器3列。
         md: 4, // 在中等宽度类型设备上，栅格子组件占据的栅格容器4列。
         lg: 6, // 在大宽度类型设备上，栅格子组件占据的栅格容器6列。
         xl: 8, // 在特大宽度类型设备上，栅格子组件占据的栅格容器8列。
         xxl: 12 // 在超大宽度类型设备上，栅格子组件占据的栅格容器12列。
       }
     }) {
       Row() {
         Text(`${index}`)
       }.width("100%").height('50vp')
     }.backgroundColor(color)
   })
}                                                                     
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.47257113918867463806512134720145:50001231000000:2800:149B0F881763D6D6ED10FA321724669A5A5A8EC181B55286ADE3831A74725314.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

* columns默认值为12，即在未设置columns时，任何断点下，栅格布局被分成12列。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown,Color.Red, Color.Orange, Color.Yellow, Color.Green];
...
GridRow() {
  ForEach(this.bgColors, (item, index) => {
    GridCol() {
      Row() {
        Text(`${index + 1}`)
      }.width('100%').height('50')
    }.backgroundColor(item)
  })
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.00410689426142383404918933116451:50001231000000:2800:502E73ABEBF9416768903341512CF895F5851E7D7F6C4B7F82160931AB51011B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当columns为自定义值，栅格布局在任何尺寸设备下都被分为columns列。下面分别设置栅格布局列数为4和8，子元素默认占一列，效果如下：

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
@State currentBp: string = 'unknown';
...
Row() {
  GridRow({ columns: 4 }) {
    ForEach(this.bgColors, (item, index) => {
      GridCol() {
        Row() {
          Text(`${index + 1}`)
        }.width('100%').height('50')
      }.backgroundColor(item)
    })
  }
  .width('100%').height('100%')
  .onBreakpointChange((breakpoint) => {
    this.currentBp = breakpoint
  })
}
.height(160)
.border({ color: Color.Blue, width: 2 })
.width('90%')

Row() {
  GridRow({ columns: 8 }) {
    ForEach(this.bgColors, (item, index) => {
      GridCol() {
        Row() {
          Text(`${index + 1}`)
        }.width('100%').height('50')
      }.backgroundColor(item)
    })
  }
  .width('100%').height('100%')
  .onBreakpointChange((breakpoint) => {
    this.currentBp = breakpoint
  })
}
.height(160)
.border({ color: Color.Blue, width: 2 })
.width('90%')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.90921119564142117547384004964985:50001231000000:2800:D942D1007F7D92F14F60D046C374D00EB60B0D08544727A3EEFA8FE5C7634433.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当columns类型为GridRowColumnOption时，支持下面六种不同尺寸（xs, sm, md, lg, xl, xxl）设备的总列数设置，各个尺寸下数值可不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown]
GridRow({ columns: { sm: 4, md: 8 }, breakpoints: { value: ['200vp', '300vp', '400vp', '500vp', '600vp'] } }) {
  ForEach(this.bgColors, (item, index) => {
    GridCol() {
      Row() {
        Text(`${index + 1}`)
      }.width('100%').height('50')
    }.backgroundColor(item)
  })
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.62184789942767538067176035049534:50001231000000:2800:495B27BE74C81A17C454EB2902D2FA839491C445EDA6DB86CDC0C600E6653C02.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

  若只设置sm, md的栅格总列数，则较小的尺寸使用默认columns值12，较大的尺寸使用前一个尺寸的columns。这里只设置sm:4, md:8，则较小尺寸的xs:12，较大尺寸的参照md的设置，lg:8, xl:8, xxl:8。

### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为GridRowDirection.Row（从左往右排列）或GridRowDirection.RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

* 子组件默认从左往右排列。

```
GridRow({ direction: GridRowDirection.Row }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.60471278343580648315078478778372:50001231000000:2800:033FFA9031A400CC64AFB03C84BAA79148AA9F9D7703CEA488F8263EE44EA463.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 子组件从右往左排列。

```
GridRow({ direction: GridRowDirection.RowReverse }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.60393311084538399996696648905407:50001231000000:2800:E941ADDFADE115A0217544381C84CEE2C44FE1CAAC9CD9819D26CE0D02D57797.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

* 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。

```
GridRow({ gutter: 10 }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.20323338812210863272015753595221:50001231000000:2800:18868826C939EF2E4F4BE06C3E8B28C4A96286968929C182A51528E233FF6A24.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当gutter类型为GutterOption时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。

```
GridRow({ gutter: { x: 20, y: 50 } }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.99405762733586829804400600801889:50001231000000:2800:4BA972814D5CD4631A80281097BB7F3E113CBCF5F2057D410EA03FF5A3106D36.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

* 设置span。
```
GridCol({ span: 2 }){}
GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){}
GridCol(){}.span(2)
GridCol(){}.span({ xs: 1, sm: 2, md: 3, lg: 4 })
```
* 设置offset。
```
GridCol({ offset: 2 }){}
GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 } }){}
GridCol(){}.offset(2)
GridCol(){}.offset({ xs: 1, sm: 2, md: 3, lg: 4 }) 
```
* 设置order。
```
GridCol({ order: 2 }){}
GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 } }){}
GridCol(){}.order(2)
GridCol(){}.order({ xs: 1, sm: 2, md: 3, lg: 4 })
```

### span

子组件占栅格布局的列数，决定了子组件的宽度，默认为1。

* 当类型为number时，子组件在所有尺寸设备下占用的列数相同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow({ columns: 8 }) {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ span: 2 }) {      
      Row() {
        Text(`${index}`)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.63830234683969399106860496900929:50001231000000:2800:8AAB1FC0FCBD19AF83A61CE3B68EBEA972A34F16D695DED3BD9CEFD5F693E684.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件所占列数设置,各个尺寸下数值可不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow({ columns: 8 }) {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }) {      
      Row() {
        Text(`${index}`)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.84333160929084705655923710553369:50001231000000:2800:6BDA024E3EF190B6C7FD5535B494C7AD506693BA690395792316693628C38E8C.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

* 当类型为number时，子组件偏移相同列数。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow() {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ offset: 2 }) {      
      Row() {
        Text('' + index)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.89795367088709185858383045251957:50001231000000:2800:B64F82890C87A03CBEED0E4BBBE8E9DE0E5D63B9D9C293C2271AD22387B26B2D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  栅格默认分成12列，每一个子组件默认占1列，偏移2列，每个子组件及间距共占3列，一行放四个子组件。
* 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件所占列数设置,各个尺寸下数值可不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...

GridRow() {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ offset: { xs: 1, sm: 2, md: 3, lg: 4 } }) {      
      Row() {
        Text('' + index)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                 
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.62895421863468669487381498262473:50001231000000:2800:943CDB13414B821BAA206AED9B2EB6BA4ACD2F7458B3600BAB2E8864A9D452C2.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

* 当类型为number时，子组件在任何尺寸下排序次序一致。

```
GridRow() {
  GridCol({ order: 4 }) {
    Row() {
      Text('1')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Red)
  GridCol({ order: 3 }) {
    Row() {
      Text('2')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Orange)
  GridCol({ order: 2 }) {
    Row() {
      Text('3')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Yellow)
  GridCol({ order: 1 }) {
    Row() {
      Text('4')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Green)
}            
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.22437510525828855543769750680122:50001231000000:2800:327F9EFE39A8948A729D70874049A46A8F28B1F1DBC08B675DF2FC6F5848EDA2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。

```
GridRow() {
  GridCol({ order: { xs:1, sm:5, md:3, lg:7}}) {
    Row() {
      Text('1')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Red)
  GridCol({ order: { xs:2, sm:2, md:6, lg:1} }) {
    Row() {
      Text('2')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Orange)
  GridCol({ order: { xs:3, sm:3, md:1, lg:6} }) {
    Row() {
      Text('3')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Yellow)
  GridCol({ order: { xs:4, sm:4, md:2, lg:5} }) {
    Row() {
      Text('4')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Green)
} 
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.63400501599078180678215127730409:50001231000000:2800:A886B3584A007541EF13E2878C2A2DCBA20378267616FDE824CA6D496271C7E4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 栅格组件的嵌套使用

栅格组件也可以嵌套使用，完成一些复杂的布局。

以下示例中，栅格把整个空间分为12份。第一层GridRow嵌套GridCol，分为中间大区域以及“footer”区域。第二层GridRow嵌套GridCol，分为“left”和“right”区域。子组件空间按照上一层父组件的空间划分，粉色的区域是屏幕空间的12列，绿色和蓝色的区域是父组件GridCol的12列，依次进行空间的划分。

```
@Entry
@Component
struct GridRowExample {
  build() {
    GridRow() {
      GridCol({ span: { sm: 12 } }) {
        GridRow() {
          GridCol({ span: { sm: 2 } }) {
            Row() {
              Text('left').fontSize(24)
            }
            .justifyContent(FlexAlign.Center)
            .height('90%')
          }.backgroundColor('#ff41dbaa')

          GridCol({ span: { sm: 10 } }) {
            Row() {
              Text('right').fontSize(24)
            }
            .justifyContent(FlexAlign.Center)
            .height('90%')
          }.backgroundColor('#ff4168db')
        }
        .backgroundColor('#19000000')
        .height('100%')
      }

      GridCol({ span: { sm: 12 } }) {
        Row() {
          Text('footer').width('100%').textAlign(TextAlign.Center)
        }.width('100%').height('10%').backgroundColor(Color.Pink)
      }
    }.width('100%').height(300)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.32228766180311627932140020469160:50001231000000:2800:E46CE96D120781EA9CB8529FDDD2F12C097F46C3E3360DD41746F8BF616DC685.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

综上所述，栅格组件提供了丰富的自定义能力，功能异常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。

