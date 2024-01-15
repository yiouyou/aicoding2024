# 绑定手势方法

更新时间: 2024-01-15 12:21

通过给各个组件绑定不同的手势事件，并设计事件的响应方式，当手势识别成功时，ArkUI框架将通过事件回调通知组件手势识别的结果。

## gesture（常规手势绑定方法）

```
.gesture(gesture: GestureType, mask?: GestureMask)
```

gesture为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。

例如，可以将点击手势TapGesture通过gesture手势绑定方法绑定到Text组件上。

```
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        // 采用gesture手势绑定方法绑定TapGesture
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
  }
}
```

## priorityGesture（带优先级的手势绑定方法）

```
.priorityGesture(gesture: GestureType, mask?: GestureMask)。
```

priorityGesture是带优先级的手势绑定方法，可以在组件上绑定优先识别的手势。

在默认情况下，当父组件和子组件使用gesture绑定同类型的手势时，子组件优先识别通过gesture绑定的手势。当父组件使用priorityGesture绑定与子组件同类型的手势时，父组件优先识别通过priorityGesture绑定的手势。

例如，当父组件Column和子组件Text同时绑定TapGesture手势时，父组件以带优先级手势priorityGesture的形式进行绑定时，优先响应父组件绑定的TapGesture。

```
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('Text TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
    // 设置为priorityGesture时，点击文本区域会忽略Text组件的TapGesture手势事件，优先响应父组件Column的TapGesture手势事件
    .priorityGesture(
      TapGesture()
        .onAction(() => {
          console.info('Column TapGesture is onAction');
        }), GestureMask.IgnoreInternal)
  }
}
```

## parallelGesture（并行手势绑定方法）

```
.parallelGesture(gesture: GestureType, mask?: GestureMask)
```

parallelGesture是并行的手势绑定方法，可以在父子组件上绑定可以同时响应的相同手势。

在默认情况下，手势事件为非冒泡事件，当父子组件绑定相同的手势时，父子组件绑定的手势事件会发生竞争，最多只有一个组件的手势事件能够获得响应。而当父组件绑定了并行手势parallelGesture时，父子组件相同的手势事件都可以触发，实现类似冒泡效果。

```
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('Text TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
    // 设置为parallelGesture时，点击文本区域会同时响应父组件Column和子组件Text的TapGesture手势事件
    .parallelGesture(
      TapGesture()
        .onAction(() => {
          console.info('Column TapGesture is onAction');
        }), GestureMask.IgnoreInternal)
  }
}
```

说明

当父组件和子组件同时绑定单击手势事件和双击手势事件时，父组件和子组件均只响应单击手势事件。

