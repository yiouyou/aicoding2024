# 创建网格（Grid/GridItem）

更新时间: 2024-01-15 12:21

## 概述

网格布局是由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。网格布局具有较强的页面均分能力，子组件占比控制能力，是一种重要自适应布局，其使用场景有九宫格图片展示、日历、计算器等。

ArkUI提供了[Grid](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-grid-0000001478341161-V3)容器组件和子组件[GridItem](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-griditem-0000001478061713-V3)，用于构建网格布局。Grid用于设置网格布局相关参数，GridItem定义子组件相关特征。Grid组件支持使用条件渲染、循环渲染、懒加载等[渲染控制](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-overview-0000001543911149-V3)方式生成子组件。

## 布局与约束

Grid组件为网格容器，其中容器内每一个条目对应一个GridItem组件，如下图所示。

图1 Grid与GridItem组件关系
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.75534080997090101453601173782938:50001231000000:2800:792F9AB0800C826E903DF641CA1DB79809DAB5FFB9E0234F818968028617C045.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

说明

Grid的子组件必须是GridItem组件。

网格布局是一种二维布局。Grid组件支持自定义行列数和每行每列尺寸占比、设置子组件横跨几行或者几列，同时提供了垂直和水平布局能力。当网格容器组件尺寸发生变化时，所有子组件以及间距会等比例调整，从而实现网格布局的自适应能力。根据Grid的这些布局能力，可以构建出不同样式的网格布局，如下图所示。

图2 网格布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.89903509019269690386990147418336:50001231000000:2800:EF1D47CF147D5862D2B384210F38F264AB94CCEA0BE10DA0154C9FFD1AAAC935.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果Grid组件设置了宽高属性，则其尺寸为设置值。如果没有设置宽高属性，Grid组件的尺寸默认适应其父组件的尺寸。

Grid组件根据行列数量与占比属性的设置，可以分为三种布局情况：

* 行、列数量与占比同时设置：Grid只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。（推荐使用该种布局方式）
* 只设置行、列数量与占比中的一个：元素按照设置的方向进行排布，超出的元素可通过滚动的方式展示。
* 行列数量与占比都不设置：元素在布局方向上排布，其行列数由布局方向、单个网格的宽高等多个属性共同决定。超出行列容纳范围的元素不展示，且Grid不可滚动。

## 设置排列方式



### 设置行列数量与占比

通过设置行列数量与尺寸占比可以确定网格布局的整体排列方式。Grid组件提供了rowsTemplate和columnsTemplate属性用于设置网格布局行列数量与尺寸占比。

rowsTemplate和columnsTemplate属性值是一个由多个空格和'数字+fr'间隔拼接的字符串，fr的个数即网格布局的行或列数，fr前面的数值大小，用于计算该行或列在网格布局宽度上的占比，最终决定该行或列的宽度。

图3 行列数量占比示例
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.04327925987458971666528865187345:50001231000000:2800:E55F6F6727F1DC8D505DFD9E31C0FFEA0BA776B3C6CD485D8917460CD008D69E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如上图所示，构建的是一个三行三列的的网格布局，其在垂直方向上分为三等份，每行占一份；在水平方向上分为四等份，第一列占一份，第二列占两份，第三列占一份。

只要将rowsTemplate的值为'1fr 1fr 1fr'，同时将columnsTemplate的值为'1fr 2fr 1fr'，即可实现上述网格布局。

```
Grid() {
  ...
}
.rowsTemplate('1fr 1fr 1fr')
.columnsTemplate('1fr 2fr 1fr')
```

说明

当Grid组件设置了rowsTemplate或columnsTemplate时，Grid的layoutDirection、maxCount、minCount、cellLength属性不生效，属性说明可参考[Grid-属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-grid-0000001478341161-V3#ZH-CN_TOPIC_0000001574128969__%E5%B1%9E%E6%80%A7)。

### 设置子组件所占行列数

除了大小相同的等比例网格布局，由不同大小的网格组成不均匀分布的网格布局场景在实际应用中十分常见，如下图所示。在Grid组件中，通过设置GridItem的rowStart、rowEnd、columnStart和columnEnd可以实现如图所示的单个网格横跨多行或多列的场景。

图4 不均匀网格布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.73808496517871292442533164851382:50001231000000:2800:DEA0A7406A2D9C497F7F9B97749FBACF75F3B7301992F6AC4FE9C22AECE86147.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

例如计算器的按键布局就是常见的不均匀网格布局场景。如下图，计算器中的按键“0”和“=”，按键“0”横跨第一、二两列，按键“=”横跨第五、六两行。使用Grid构建的网格布局，其行列标号从1开始，依次编号。

图5 计算器
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.96743220453375348691778926410350:50001231000000:2800:72F02A9B70149EFFD0CFC33EC2BEF8D6AB5108E89BFE0B159B9F200C919E9EFC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在单个网格单元中，rowStart和rowEnd属性表示指定当前元素起始行号和终点行号，columnStart和columnEnd属性表示指定当前元素的起始列号和终点列号。

所以“0”按键横跨第一列和第二列，只要将“0”对应GridItem的columnStart和columnEnd设为1和2，将“=”对应GridItem的的rowStart和rowEnd设为5和6即可。

```
GridItem() {
  Text(key)
    ...
}
.columnStart(1)
.columnEnd(2)
```

“=”按键横跨第五行和第六行，只要将将“=”对应GridItem的的rowStart和rowEnd设为5和6即可。

```
GridItem() {
  Text(key)
    ...
}
.rowStart(5)
.rowEnd(6)
```

### 设置主轴方向

使用Grid构建网格布局时，若没有设置行列数量与占比，可以通过layoutDirection可以设置网格布局的主轴方向，决定子组件的排列方式。此时可以结合minCount和maxCount属性来约束主轴方向上的网格数量。

图6 主轴方向示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.75504242616292487682681940935036:50001231000000:2800:09E52DFFB119F35607E2862605D091084E01A261666F588BABFB95B126D023D6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

当前layoutDirection设置为Row时，先从左到右排列，排满一行再排一下一行。当前layoutDirection设置为Column时，先从上到下排列，排满一列再排一下一列，如上图所示。此时，将maxCount属性设为3，表示主轴方向上最大显示的网格单元数量为3。

```
Grid() {
  ...
}
.maxCount(3)
.layoutDirection(GridDirection.Row)
```

说明

1. layoutDirection属性仅在不设置rowsTemplate和columnsTemplate时生效，此时元素在layoutDirection方向上排列。
2. 仅设置rowsTemplate时，Grid主轴为水平方向，交叉轴为垂直方向。
3. 仅设置columnsTemplate时，Grid主轴为垂直方向，交叉轴为水平方向。

## 在网格布局中显示数据

网格布局采用二维布局的方式组织其内部元素，如下图所示。

图7 通用办公服务
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.17529420672506068665163981444203:50001231000000:2800:A919C273AAE96440BCE7B595156D9BCBF4A63481A3822B13607FB0AB139DBE96.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

Grid组件可以通过二维布局的方式显示一组GridItem子组件。

```
Grid() {
  GridItem() {
    Text('会议')
      ...
  }

  GridItem() {
    Text('签到')
      ...
  }

  GridItem() {
    Text('投票')
      ...
  }

  GridItem() {
    Text('打印')
      ...
  }
}
.rowsTemplate('1fr 1fr')
.columnsTemplate('1fr 1fr')
```

对于内容结构相似的多个GridItem，通常更推荐使用[循环渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)ForEach语句中嵌套GridItem的形式，来减少重复代码。

```
@Component
struct OfficeService {
  @State services: Array<string> = ['会议', '投票', '签到', '打印']
  ...

  build() {
    Column() {
      Grid() {
        ForEach(this.services, service => {
          GridItem() {
            Text(service)
              ...
          }
        }, service => service)
      }
      .rowsTemplate('1fr 1fr')
      .columnsTemplate('1fr 1fr')
      ...
    }
    ...
  }
}
```

## 设置行列间距

在两个网格单元之间的网格横向间距称为行间距，网格纵向间距称为列间距，如下图所示。

图8 网格的行列间距
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.11661572535337771444048654269564:50001231000000:2800:1A025E6381CCD84D0886F5919535895BD5BFDDE5F1EC2AA61834BA665DB16F1B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")通过Grid的rowsGap和columnsGap可以设置网格布局的行列间距。在图5所示的计算器中，行间距为15vp，列间距为10vp。

```
Grid() {
  ...
}
.columnsGap(10)
.rowsGap(15)
```

## 构建可滚动的网格布局

可滚动的网格布局常用在文件管理、购物或视频列表等页面中，如下图所示。在设置Grid的行列数量与占比时，如果仅设置行、列数量与占比中的一个，即仅设置rowsTemplate或仅设置columnsTemplate属性，网格单元按照设置的方向排列，超出Grid显示区域后，Grid拥有可滚动能力。

图9 横向可滚动网格布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.76180846287498201880108753731669:50001231000000:2800:0FDAB20AB6E4CAF3603B5A9A82ED96ABEC786200721EACED5CA3B2CF679843BD.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

如果设置的是columnsTemplate，Grid的滚动方向为垂直方向；如果设置的是rowsTemplate，Grid的滚动方向为水平方向。

如上图所示的横向可滚动网格布局，只要设置rowsTemplate属性的值且不设置columnsTemplate属性，当内容超出Grid组件宽度时，Grid可横向滚动进行内容展示。

```
@Component
struct Shopping {
  @State services: Array<string> = ['直播', '进口', ...]
  ...

  build() {
    Column({ space: 5 }) {
      Grid() {
        ForEach(this.services, (service: string, index) => {
          GridItem() {
            ...
          }
          .width('25%')
        }, service => service)
      }
      .rowsTemplate('1fr 1fr') // 只设置rowsTemplate属性，当内容超出Grid区域时，可水平滚动。
      .rowsGap(15)
      ...
    }
    ...
  }
}
```

## 控制滚动位置

与新闻列表的返回顶部场景类似，控制滚动位置功能在网格布局中也很常用，例如下图所示日历的翻页功能。

图10 日历翻页
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.82949552411824461323389842112811:50001231000000:2800:48DE205FBF1D60BF6E86739C50AAA5090F8D64F1E885AC4B4D741B8F8B2B6BEB.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

Grid组件初始化时，可以绑定一个[Scroller](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-scroll-0000001427902480-V3#ZH-CN_TOPIC_0000001523648790__scroller)对象，用于进行滚动控制，例如通过Scroller对象的[scrollPage](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-scroll-0000001427902480-V3#ZH-CN_TOPIC_0000001523648790__scrollpage)方法进行翻页。

```
private scroller: Scroller = new Scroller()
```

在日历页面中，用户在点击“下一页”按钮时，应用响应点击事件，通过指定scrollPage方法的参数next为true，滚动到下一页。

```
Column({ space: 5 }) {
  Grid(this.scroller) {
    ...
  }
  .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr 1fr')
  ...
 
 Row({space: 20}) {
   Button('上一页')
     .onClick(() => {
       this.scroller.scrollPage({
         next: false
       })
     })

   Button('下一页')
     .onClick(() => {
       this.scroller.scrollPage({
         next: true
       })
     })
 }
}
...
```

## 性能优化

与[长列表的处理](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section94148431926)类似，[循环渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)适用于数据量较小的布局场景，当构建具有大量网格项的可滚动网格布局时，推荐使用[数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)方式实现按需迭代加载数据，从而提升列表性能。

关于按需加载优化的具体实现可参考[数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)章节中的示例。

当使用懒加载方式渲染网格时，为了更好的滚动体验，减少滑动时出现白块，Grid组件中也可通过cachedCount属性设置GridItem的预加载数量，只在懒加载LazyForEach中生效。

设置预加载数量后，会在Grid显示区域前后各缓存cachedCount*列数个GridItem，超出显示和缓存范围的GridItem会被释放。

```
Grid() {
  LazyForEach(this.dataSource, item => {
    GridItem() {
      ...
    }
  })
}
.cachedCount(3)
```

说明

cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。

