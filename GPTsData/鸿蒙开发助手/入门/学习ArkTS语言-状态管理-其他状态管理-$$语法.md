# $$语法：内置组件双向同步

更新时间: 2024-01-10 11:59

$$
运算符为系统内置组件提供TS变量的引用，使得TS变量和系统内置组件的内部状态保持同步。

内部状态具体指什么取决于组件。例如，[Refresh](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-refresh-0000001478181429-V3)组件的refreshing参数。

## 使用规则

* 当前$$支持基础类型变量，以及@State、@Link和@Prop装饰的变量。
* 当前$$仅支持[Refresh](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-refresh-0000001478181429-V3)组件的refreshing参数。
* $$绑定的变量变化时，会触发UI的同步刷新。

## 使用示例

以[Refresh](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-refresh-0000001478181429-V3)组件的refreshing参数为例：

当使用了$$符号绑定isRefreshing状态变量时，页面进行下拉操作，isRefreshing会变成true。

同时，Text中的isRefreshing状态也会同步改变为true，如果不使用$$符号绑定，则不会同步改变。

```
// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false
  @State counter: number = 0

  build() {
    Column() {
      Text('Pull Down and isRefreshing: ' + this.isRefreshing)
        .fontSize(30)
        .margin(10)

      Refresh({ refreshing: $$this.isRefreshing, offset: 120, friction: 100 }) {
        Text('Pull Down and refresh: ' + this.counter)
          .fontSize(30)
          .margin(10)
      }
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus)
      })
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103845.31784077069351637038313299207894:50001231000000:2800:4BA993E30C8318F3810907A75AF7615E615A0E01640EFD741CE6188DAF2A4917.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

