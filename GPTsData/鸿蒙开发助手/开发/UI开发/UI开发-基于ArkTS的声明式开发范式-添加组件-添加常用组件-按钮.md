# 按钮（Button）

更新时间: 2024-01-15 12:18

Button是按钮组件，通常用于响应用户的点击操作，其类型包括胶囊按钮、圆形按钮、普通按钮。Button当做为容器使用时可以通过添加子组件实现包含文字、图片等元素的按钮。具体用法请参考[Button](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-button-0000001427584848-V3)。

## 创建按钮

Button通过调用接口来创建，接口调用有以下两种形式：

* 创建不包含子组件的按钮。

```
Button(label?: string, options?: { type?: ButtonType, stateEffect?: boolean })
```

  该接口用于创建不包含子组件的按钮，其中label用来设置按钮文字，type用于设置Button类型，stateEffect属性设置Button是否开启点击效果。

```
Button('Ok', { type: ButtonType.Normal, stateEffect: true }) 
  .borderRadius(8) 
  .backgroundColor(0x317aff) 
  .width(90)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.68709774846202841087444365394519:50001231000000:2800:52B7059DCCF7E6AC85F1A1450D47C6A9F9506D66C1CB248674F496E72F4B4E01.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 创建包含子组件的按钮。

```
Button(options?: {type?: ButtonType, stateEffect?: boolean})
```

  该接口用于创建包含子组件的按钮，只支持包含一个子组件，子组件可以是[基础组件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-alphabet-indexer-0000001427744828-V3)或者[容器组件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-badge-0000001478181417-V3)。

```
Button({ type: ButtonType.Normal, stateEffect: true }) {
  Row() {
    Image($r('app.media.loading')).width(20).height(40).margin({ left: 12 })
    Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
  }.alignItems(VerticalAlign.Center)
}.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.77462936499010173006258252660667:50001231000000:2800:4A9785EA34DCB7AD0D001BB08AEE9C0FAC35B900422E282D14F92F105457D38B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 设置按钮类型

Button有三种可选类型，分别为Capsule（胶囊类型）、Circle（圆形按钮）和Normal（普通按钮），通过type进行设置。

* 胶囊按钮（默认类型）此类型按钮的圆角自动设置为高度的一半，不支持通过borderRadius属性重新设置圆角。

```
Button('Disable', { type: ButtonType.Capsule, stateEffect: false }) 
  .backgroundColor(0x317aff) 
  .width(90)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.43897344296160030375834797868039:50001231000000:2800:7065BBC85FAC39DE3A102338F066768B717D92837B8D25286A644874478E9EF5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 圆形按钮此类型按钮为圆形，不支持通过borderRadius属性重新设置圆角。

```
Button('Circle', { type: ButtonType.Circle, stateEffect: false }) 
  .backgroundColor(0x317aff) 
  .width(90) 
  .height(90)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.39309621427301997008480624930043:50001231000000:2800:2AE57915B2B6D8085A360A45529881F85C8CEC9A32910FFD5779911498212BFD.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 普通按钮此类型的按钮默认圆角为0，支持通过borderRadius属性重新设置圆角。

```
Button('Ok', { type: ButtonType.Normal, stateEffect: true }) 
  .borderRadius(8) 
  .backgroundColor(0x317aff) 
  .width(90)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.04967863439339643038556997288712:50001231000000:2800:3BEEDA76DFDDA1E8795CA716E6A16DEC3962AFB455A146F1ACDFFB0B01440D4A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

* 设置边框弧度。
  一般使用通用属性来自定义按钮样式。例如通过borderRadius属性设置按钮的边框弧度。

```
Button('circle border', { type: ButtonType.Normal }) 
  .borderRadius(20)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.86691812017673344410264576273998:50001231000000:2800:6A38C8F8A5E6E1E9ACCF6FCCE08306003E09B653A60986CE52FFA4E7FF871909.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 设置文本样式。通过添加文本样式设置按钮文本的展示样式。

```
Button('font style', { type: ButtonType.Normal }) 
  .fontSize(20) 
  .fontColor(Color.Pink) 
  .fontWeight(800)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.98642942182022718477123684670093:50001231000000:2800:EEA589743B581A9582014D8F79EF90C4CA1C57550A917AC5E073F31902E69CB1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 设置背景颜色。添加backgroundColor属性设置按钮的背景颜色。

```
Button('background color').backgroundColor(0xF55A42)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.06644360513315284049135432917299:50001231000000:2800:D847B7366DA4A974CD4FF5F0FC6424A81C83769D53567E88A1ED40350C97F29E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 用作功能型按钮。为删除操作创建一个按钮。

```
Button({ type: ButtonType.Circle, stateEffect: true }) { 
  Image($r('app.media.ic_public_delete_filled')).width(30).height(30) 
}.width(55).height(55).margin({ left: 20 }).backgroundColor(0xF55A42)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.96215170762646281150232692214340:50001231000000:2800:4D303C5C92F9821D74C388B8BDBF5FABDEC706475E41585268644ADDE0CF289E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

Button组件通常用于触发某些操作，可以绑定onClick事件来响应点击操作后的自定义行为。

```
Button('Ok', { type: ButtonType.Normal, stateEffect: true }) 
  .onClick(()=>{ 
    console.info('Button onClick') 
  })
```

## 场景示例

* 用于启动操作。可以用按钮启动任何用户界面元素，按钮会根据用户的操作触发相应的事件。例如，在List容器里通过点击按钮进行页面跳转。

```
// xxx.ets
import router from '@ohos.router';
@Entry
@Component
struct ButtonCase1 {
  build() {
    List({ space: 4 }) {
      ListItem() {
        Button("First").onClick(() => {
          router.pushUrl({ url: 'pages/first_page' })
        })
          .width('100%')
      }
      ListItem() {
        Button("Second").onClick(() => {
          router.pushUrl({ url: 'pages/second_page' })
        })
          .width('100%')
      }
      ListItem() {
        Button("Third").onClick(() => {
          router.pushUrl({ url: 'pages/third_page' })
        })
          .width('100%')
      }
    }
    .listDirection(Axis.Vertical)
    .backgroundColor(0xDCDCDC).padding(20)
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.73825096193515558546306278881215:50001231000000:2800:BE8B7E861DA9EC2C7FC4068AF6ADEECF5C9D965A64F77639CF0D7A9B08FECD96.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* 用于表单的提交。在用户登录/注册页面，使用按钮进行登录或注册操作。

```
// xxx.ets
@Entry
@Component
struct ButtonCase2 {
  build() {
    Column() {
      TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
      TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
      Button('Register').width(300).margin({ top: 20 })
        .onClick(() => {
          // 需要执行的操作
        })
    }.padding(20)
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.37608849491344976073238734219957:50001231000000:2800:E00B577B162EBF780613216DDFCEAD650CA916DC5373E5685917DAA91D195055.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 悬浮按钮在可以滑动的界面，滑动时按钮始终保持悬浮状态。

```
// xxx.ets
@Entry
@Component
struct HoverButtonExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  build() {
    Stack() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, item => item)
      }.width('90%')
      Button() {
        Image($r('app.media.ic_public_add'))
          .width(50)
          .height(50)
      }
      .width(60)
      .height(60)
      .position({x: '80%', y: 600})
      .shadow({radius: 10})
      .onClick(() => {
        // 需要执行的操作
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.77706157243493821898075978653236:50001231000000:2800:78066818C07B509664B6B8730518F7A78630302F1CD2236056FEC004AA0AC3C7.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

