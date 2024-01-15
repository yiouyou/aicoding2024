# 切换按钮（Toggle）

更新时间: 2024-01-15 12:19

Toggle组件提供状态按钮样式，勾选框样式及开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-toggle-0000001478061705-V3)。

## 创建切换按钮

Toggle通过调用接口来创建，接口调用形式如下：

```
Toggle(options: { type: ToggleType, isOn?: boolean })
```

该接口用于创建切换按钮，其中ToggleType为开关类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态，接口调用有以下两种形式：

* 创建不包含子组件的Toggle。当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle：

```
Toggle({ type: ToggleType.Checkbox, isOn: false })
Toggle({ type: ToggleType.Checkbox, isOn: true })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.63359999959084338946341552977337:50001231000000:2800:E269DE4D840B020037BD611A278806471C97F7656CC06FF1214C5D1CAA004731.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
Toggle({ type: ToggleType.Switch, isOn: false })
Toggle({ type: ToggleType.Switch, isOn: true })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.69258225389488419026499656703181:50001231000000:2800:E73F64436F7EA6516A9D7EECBCE43DE3F5FC18B313B391B7197D4DD9497D4AA2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 创建包含子组件的Toggle。当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮内部。

```
Toggle({ type: ToggleType.Button, isOn: false }) {
  Text('status button')
  .fontColor('#182431')
  .fontSize(12)
}.width(100)
Toggle({ type: ToggleType.Button, isOn: true }) {
  Text('status button')
  .fontColor('#182431')
  .fontSize(12)
}.width(100)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.88367328583453750101839410377391:50001231000000:2800:26B356CAFCBC3D87CE7A3F05096D693E435D14D5AEDF9426FE60F77EECF12955.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

* 通过selectedColor属性设置Toggle打开选中后的背景颜色。

```
Toggle({ type: ToggleType.Button, isOn: true }) {
  Text('status button')
  .fontColor('#182431')
  .fontSize(12)
}.width(100).selectedColor(Color.Pink)
Toggle({ type: ToggleType.Checkbox, isOn: true })
  .selectedColor(Color.Pink)
Toggle({ type: ToggleType.Switch, isOn: true })
  .selectedColor(Color.Pink)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.67975277303320854612047822255134:50001231000000:2800:A7BA0E5642706178AAF7C49DC342187ECCC44149170D30DE17C4D4134B8DBE95.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。

```
Toggle({ type: ToggleType.Switch, isOn: false })
  .switchPointColor(Color.Pink)
Toggle({ type: ToggleType.Switch, isOn: true })
  .switchPointColor(Color.Pink)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.96429584369034224847932645394359:50001231000000:2800:489F4A053400A329AC1CAEECB9AE0677E4FF2E3F7CDBC43E897B5B94265AC219.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

除支持通用事件外，Toggle通常用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```
Toggle({ type: ToggleType.Switch, isOn: false })
  .onChange((isOn: boolean) => {
      if(isOn) {
        // 需要执行的操作
      }
  })
```

## 场景示例

Toggle可用于切换蓝牙开关状态。

```
// xxx.ets
import promptAction from '@ohos.promptAction';
@Entry
@Component
struct ToggleExample {
  build() {
    Column() {
      Row() {
        Text("Bluetooth Mode")
        .height(50)
        .fontSize(16)
      }
      Row() {
        Text("Bluetooth")
          .height(50)
          .padding({left: 10})
          .fontSize(16)
          .textAlign(TextAlign.Start)
          .backgroundColor(0xFFFFFF)
        Toggle({ type: ToggleType.Switch })
          .margin({left: 200, right: 10})
          .onChange((isOn: boolean) => {
            if(isOn) {
              promptAction.showToast({ message: 'Bluetooth is on.' })
            } else {
              promptAction.showToast({ message: 'Bluetooth is off.' })
            }
          })
      }
      .backgroundColor(0xFFFFFF)
    }
    .padding(10)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.24657703002271897332137543889719:50001231000000:2800:2BBA9EF7681A4DAA6451E9E6AC0BFE2158CFDDBF6BC2BD8BCEF0C984D68B0C9C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

