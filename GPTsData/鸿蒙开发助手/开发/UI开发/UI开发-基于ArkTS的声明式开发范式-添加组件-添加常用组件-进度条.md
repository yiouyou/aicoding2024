# 进度条（Progress）

更新时间: 2024-01-15 12:19

Progress是进度条显示组件，显示内容通常为某次目标操作的当前进度。具体用法请参考[Progress](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-progress-0000001427584856-V3)。

## 创建进度条

Progress通过调用接口来创建，接口调用形式如下：

```
Progress(options: {value: number, total?: number, type?: ProgressType})
```

该接口用于创建type样式的进度条，其中value用于设置初始进度值，total用于设置进度总长度，type决定Progress样式。

```
Progress({ value: 24, total: 100, type: ProgressType.Linear }) // 创建一个进度总长为100，初始进度值为24的线性进度条
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.57769289555107438405777389064934:50001231000000:2800:CA6C35423CD14C282D0B8D26E5E8766975294EA2559B0A25A096110707658F4E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 设置进度条样式

Progress有5种可选类型，在创建时通过设置ProgressType枚举类型给type可选项指定Progress类型。其分别为：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  说明

  从API version9开始，组件高度大于宽度的时候自适应垂直显示，相等时仍然保持水平显示。

```
Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.74892607344261232461461445128449:50001231000000:2800:77BD4029B78561D799A8AEC8CB253DCBE111238D03F054E9B99C23F3B2AB5924.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 环形无刻度样式进度条

```
// 从左往右，1号环形进度条，默认前景色为蓝色，默认strokeWidth进度条宽度为2.0vp
Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
// 从左往右，2号环形进度条
Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
    .color(Color.Grey)    // 进度条前景色为灰色
    .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15.0vp
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.05153981671267527681468405862277:50001231000000:2800:8EAFA559C2977E3DE2A27DD98D34E0E3E1B03CBBFFEE81253914D00DA5F57C49.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 环形有刻度样式进度条

```
Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条总刻度数为20，刻度宽度为5vp
Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为5vp
Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 3 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为3vp
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.62226786515688842004266218036776:50001231000000:2800:08FD48609931EBFD68704428B0F0C5EA19C2F6FCEB7D630226817D85BC67D80F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 圆形样式进度条

```
// 从左往右，1号圆形进度条，默认前景色为蓝色
Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
// 从左往右，2号圆形进度条，指定前景色为灰色
Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.42477033744202250277186171981344:50001231000000:2800:99E9AAA81186258DD6DA435581AA4BBE072B996992F990A56FD8026D53F04764.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 胶囊样式进度条

  说明

  1、头尾两端圆弧处的进度展示效果与ProgressType.Eclipse样式相同；

  2、中段处的进度展示效果为矩形状长条，与ProgressType.Linear线性样式相似；

  3、组件高度大于宽度的时候自适应垂直显示。

```
Progress({ value: 10, total: 150, type: ProgressType.Capsule }).width(100).height(50)
Progress({ value: 20, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Grey)
Progress({ value: 50, total: 150, type: ProgressType.Capsule }).width(50).height(100).backgroundColor(Color.Black)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.30662222812426085183035503353677:50001231000000:2800:3D27D44D9226D65700ED5AE4221B3E322A1245C8D8ED86018638A15DCD098392.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景示例

更新当前进度值，如应用安装进度条。可通过点击Button增加progressValue，.value()属性将progressValue设置给Progress组件，进度条组件即会触发刷新，更新当前进度。

```
@Entry
@Component
struct ProgressCase1 { 
  @State progressValue: number = 0    // 设置进度条初始值为0
  build() {
    Column() {
      Column() {
        Progress({value:0, total:100, type:ProgressType.Capsule}).width(200).height(50)
          .style({strokeWidth:50}).value(this.progressValue)
        Row().width('100%').height(5)
        Button("进度条+5")
          .onClick(()=>{
            this.progressValue += 5
            if (this.progressValue > 100){
              this.progressValue = 0
            }
          })
      }
    }.width('100%').height('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.42706131621390699036153271157395:50001231000000:2800:59293A225861A9C56E69F3E2A45FF061413BBD81E14411621B3491E9280CCD4D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

