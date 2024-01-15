# 单选框（Radio）

更新时间: 2024-01-15 12:18

Radio是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。具体用法请参考[Radio](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-radio-0000001478181405-V3)。

## 创建单选框

Radio通过调用接口来创建，接口调用形式如下：

```
Radio(options: {value: string, group: string})
```

该接口用于创建一个单选框，其中value是单选框的名称，group是单选框的所属群组名称。checked属性可以设置单选框的状态，状态分别为false和true时，设置为true时表示单选框被选中。Radio仅支持选中和未选中两种样式，不支持自定义颜色和形状。

```
Radio({ value: 'Radio1', group: 'radioGroup' })
  .checked(false)
Radio({ value: 'Radio2', group: 'radioGroup' })
  .checked(true)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183857.58125840987137090703903969184716:50001231000000:2800:7C721A6C327398CB6AA26F14C26160E1ED66471CDBE0C2A994EE72645C95E066.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

除支持[通用事件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-click-0000001477981153-V3)外，Radio通常用于选中后触发某些操作，可以绑定onChange事件来响应选中操作后的自定义行为。

```
  Radio({ value: 'Radio1', group: 'radioGroup' })
    .onChange((isChecked: boolean) => {
      if(isChecked) {
        //需要执行的操作
      }
    })
  Radio({ value: 'Radio2', group: 'radioGroup' })
    .onChange((isChecked: boolean) => {
      if(isChecked) {
        //需要执行的操作
      }
    })
```

## 场景示例

通过点击Radio切换声音模式。

```
// xxx.ets
import promptAction from '@ohos.promptAction';
@Entry
@Component
struct RadioExample {
  build() {
    Row() {
      Column() {
        Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)
          .height(50)
          .width(50)
          .onChange((isChecked: boolean) => {
            if(isChecked) {
              // 切换为响铃模式
              promptAction.showToast({ message: 'Ringing mode.' })
            }
          })
        Text('Ringing')
      }
      Column() {
        Radio({ value: 'Radio2', group: 'radioGroup' })
          .height(50)
          .width(50)
          .onChange((isChecked: boolean) => {
            if(isChecked) {
              // 切换为振动模式
              promptAction.showToast({ message: 'Vibration mode.' })
            }
          })
        Text('Vibration')
      }
      Column() {
        Radio({ value: 'Radio3', group: 'radioGroup' })
          .height(50)
          .width(50)
          .onChange((isChecked: boolean) => {
            if(isChecked) {
              // 切换为静音模式
              promptAction.showToast({ message: 'Silent mode.' })
            }
          })
        Text('Silent')
      }
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183857.83967246863091138556907506453041:50001231000000:2800:64F3902EF615FAD09B39A767C4AAF5FDB514A82C9DB1454C5CA8ED2A255BBB16.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

