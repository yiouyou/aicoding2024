# AppStorage：应用全局的UI状态存储

更新时间: 2024-01-10 11:59

AppStorage是应用全局的UI状态存储，是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。

和AppStorage不同的是，LocalStorage是页面级的，通常应用于页面内的数据共享。而AppStorage是应用级的全局状态共享，还相当于整个应用的“中枢”，[持久化数据PersistentStorage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-persiststorage-0000001474017166-V3)和[环境变量Environment](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-environment-0000001473537710-V3)都是通过和AppStorage中转，才可以和UI交互。

本文仅介绍AppStorage使用场景和相关的装饰器：@StorageProp和@StorageLink。

## 概述

AppStorage是在应用启动的时候会被创建的单例。它的目的是为了提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorage将在应用运行过程保留其属性。属性通过唯一的键字符串值访问。

AppStorage可以和UI组件同步，且可以在应用业务逻辑中被访问。

AppStorage中的属性可以被双向同步，数据可以是存在于本地或远程设备上，并具有不同的功能，比如数据持久化（详见[PersistentStorage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-persiststorage-0000001474017166-V3)）。这些数据是通过业务逻辑中实现，与UI解耦，如果希望这些数据在UI中使用，需要用到[@StorageProp](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-appstorage-0000001524417209-V3#section676113134317)和[@StorageLink](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-appstorage-0000001524417209-V3#section84115526424)。

## @StorageProp

在上文中已经提到，如果要建立AppStorage和自定义组件的联系，需要使用@StorageProp和@StorageLink装饰器。使用@StorageProp(key)/@StorageLink(key)装饰组件内的变量，key标识了AppStorage的属性。

当自定义组件初始化的时候，@StorageProp(key)/@StorageLink(key)装饰的变量会通过给定的key，绑定在AppStorage对应的属性，完成初始化。本地初始化是必要的，因为无法保证AppStorage一定存在给定的key，这取决于应用逻辑，是否在组件初始化之前在AppStorage实例中存入对应的属性。

@StorageProp(key)是和AppStorage中key对应的属性建立单向数据同步，我们允许本地改变的发生，但是对于@StorageProp，本地的修改永远不会同步回AppStorage中，相反，如果AppStorage给定key的属性发生改变，改变会被同步给@StorageProp，并覆盖掉本地的修改。

### 装饰器使用规则说明

| @StorageProp变量装饰器 | 说明                                                                                                                                                                                                                                                                                                                                |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 装饰器参数             | key：常量字符串，必填（字符串需要有引号）。                                                                                                                                                                                                                                                                                         |
| 允许装饰的变量类型     | Object class、string、number、boolean、enum类型，以及这些类型的数组。嵌套类型的场景请参考[观察变化和行为表现](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-appstorage-0000001524417209-V3#section8970810185617)。类型必须被指定，且必须和AppStorage中对应属性相同。不支持any，不允许使用undefined和null。 |
| 同步类型               | 单向同步：从AppStorage的对应属性到组件的状态变量。组件本地的修改是允许的，但是AppStorage中给定的属性一旦发生变化，将覆盖本地的修改。                                                                                                                                                                                                |
| 被装饰变量的初始值     | 必须指定，如果AppStorage实例中不存在属性，则作为初始化默认值，并存入AppStorage中。                                                                                                                                                                                                                                                  |

### 变量的传递/访问规则说明

| 传递/访问            | 说明                                                                                                                     |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| 从父节点初始化和更新 | 禁止，@StorageProp不支持从父节点初始化，只能AppStorage中key对应的属性初始化，如果没有对应key的话，将使用本地默认值初始化 |
| 初始化子节点         | 支持，可用于初始化@State、@Link、@Prop、@Provide。                                                                       |
| 是否支持组件外访问   | 否。                                                                                                                     |

 **图1 ** **@StorageProp初始化规则图示**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211141603.46899708816613521298235117590421:50001231000000:2800:93B8C552C16F0E65A4A51F1DCD99A4E2F1E0DA70E8A92C0D6AA226CFF031FA09.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 观察变化和行为表现

**观察变化**

* 当装饰的数据类型为boolean、string、number类型时，可以观察到数值的变化。
* 当装饰的数据类型为class或者Object时，可以观察到赋值和属性赋值的变化，即Object.keys(observedObject)返回的所有属性。
* 当装饰的对象是array时，可以观察到数组添加、删除、更新数组单元的变化。

**框架行为**

* 当@StorageProp(key)装饰的数值改变被观察到时，修改不会被同步回AppStorage对应属性键值key的属性中。
* 当前@StorageProp(key)单向绑定的数据会被修改，即仅限于当前组件的私有成员变量改变，其他的绑定该key的数据不会同步改变。
* 当@StorageProp(key)装饰的数据本身是状态变量，它的改变虽然不会同步回AppStorage中，但是会引起所属的自定义组件的重新渲染。
* 当AppStorage中key对应的属性发生改变时，会同步给所有@StorageProp(key)装饰的数据，@StorageProp(key)本地的修改将被覆盖。

## @StorageLink

@StorageLink(key)是和AppStorage中key对应的属性建立双向数据同步：

1. 本地修改发生，该修改会被写回AppStorage中；
2. AppStorage中的修改发生后，该修改会被同步到所有绑定AppStorage对应key的属性上，包括单向（@StorageProp和通过Prop创建的单向绑定变量）、双向（@StorageLink和通过Link创建的双向绑定变量）变量和其他实例（比如PersistentStorage）。

### 装饰器使用规则说明

| @StorageLink变量装饰器 | 说明                                                                                                                                                                                                                                                                                                                                 |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 装饰器参数             | key：常量字符串，必填（字符串需要有引号）。                                                                                                                                                                                                                                                                                          |
| 允许装饰的变量类型     | Object、class、string、number、boolean、enum类型，以及这些类型的数组。嵌套类型的场景请参考[观察变化和行为表现](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-appstorage-0000001524417209-V3#section2040243611596)。类型必须被指定，且必须和AppStorage中对应属性相同。不支持any，不允许使用undefined和null。 |
| 同步类型               | 双向同步：从AppStorage的对应属性到自定义组件，从自定义组件到AppStorage对应属性。                                                                                                                                                                                                                                                     |
| 被装饰变量的初始值     | 必须指定，如果AppStorage实例中不存在属性，则作为初始化默认值，并存入AppStorage中。                                                                                                                                                                                                                                                   |

### 变量的传递/访问规则说明

| 传递/访问            | 说明                                                         |
| :--------------------- | :------------------------------------------------------------- |
| 从父节点初始化和更新 | 禁止。                                                       |
| 初始化子节点         | 支持，可用于初始化常规变量、@State、@Link、@Prop、@Provide。 |
| 是否支持组件外访问   | 否。                                                         |

 **图2 ** **@StorageLink初始化规则图示**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211141603.21880068464710391864141291715277:50001231000000:2800:EF21C0ABDC66A642E262034FFB2758CF92C34E1F56632AD6C768D9CE18EAA88A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 观察变化和行为表现

**观察变化**

* 当装饰的数据类型为boolean、string、number类型时，可以观察到数值的变化。
* 当装饰的数据类型为class或者Object时，可以观察到赋值和属性赋值的变化，即Object.keys(observedObject)返回的所有属性。
* 当装饰的对象是array时，可以观察到数组添加、删除、更新数组单元的变化。

**框架行为**

1. 当@StorageLink(key)装饰的数值改变被观察到时，修改将被同步回AppStorage对应属性键值key的属性中。
2. AppStorage中属性键值key对应的数据一旦改变，属性键值key绑定的所有的数据（包括双向@StorageLink和单向@StorageProp）都将同步修改；
3. 当@StorageLink(key)装饰的数据本身是状态变量，它的改变不仅仅会同步回AppStorage中，还会引起所属的自定义组件的重新渲染。

## 使用场景

### 从应用逻辑使用AppStorage和LocalStorage

AppStorage是单例，它的所有API都是静态的，使用方法类似于LocalStorage对应的非静态方法。

```
AppStorage.SetOrCreate('PropA', 47);

let storage: LocalStorage = new LocalStorage({ 'PropA': 17 });
let propA: number = AppStorage.Get('PropA') // propA in AppStorage == 47, propA in LocalStorage == 17
var link1: SubscribedAbstractProperty<number> = AppStorage.Link('PropA'); // link1.get() == 47
var link2: SubscribedAbstractProperty<number> = AppStorage.Link('PropA'); // link2.get() == 47
var prop: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA'); // prop.get() == 47

link1.set(48); // two-way sync: link1.get() == link2.get() == prop.get() == 48
prop.set(1); // one-way sync: prop.get() == 1; but link1.get() == link2.get() == 48
link1.set(49); // two-way sync: link1.get() == link2.get() == prop.get() == 49

storage.get('PropA') // == 17 
storage.set('PropA', 101);
storage.get('PropA') // == 101

AppStorage.Get('PropA') // == 49
link1.get() // == 49
link2.get() // == 49
prop.get() // == 49
```

### 从UI内部使用AppStorage和LocalStorage

@StorageLink变量装饰器与AppStorage配合使用，正如@LocalStorageLink与LocalStorage配合使用一样。此装饰器使用AppStorage中的属性创建双向数据同步。

```
AppStorage.SetOrCreate('PropA', 47);
let storage = new LocalStorage({ 'PropA': 48 });

@Entry(storage)
@Component
struct CompA {
  @StorageLink('PropA') storLink: number = 1;
  @LocalStorageLink('PropA') localStorLink: number = 1;

  build() {
    Column({ space: 20 }) {
      Text(`From AppStorage ${this.storLink}`)
        .onClick(() => this.storLink += 1)

      Text(`From LocalStorage ${this.localStorLink}`)
        .onClick(() => this.localStorLink += 1)
    }
  }
}
```

### 不建议借助@StorageLink的双向同步机制实现事件通知

不建议开发者使用@StorageLink和AppStorage的双向同步的机制来实现事件通知，AppStorage是和UI相关的数据存储，改变会带来UI的刷新，相对于一般的事件通知，UI刷新的成本较大。

TapImage中的点击事件，会触发AppStorage中tapIndex对应属性的改变。因为@StorageLink是双向同步，修改会同步回AppStorage中，所以，所有绑定AppStorage的tapIndex自定义组件都会被通知UI刷新。UI刷新带来的成本是巨大的，因此不建议开发者使用此方式来实现基本的事件通知功能。

```
// xxx.ets
class ViewData {
  title: string;
  uri: Resource;
  color: Color = Color.Black;

  constructor(title: string, uri: Resource) {
    this.title = title;
    this.uri = uri
  }
}

@Entry
@Component
struct Gallery2 {
  dataList: Array<ViewData> = [new ViewData('flower', $r('app.media.icon')), new ViewData('OMG', $r('app.media.icon')), new ViewData('OMG', $r('app.media.icon'))]
  scroller: Scroller = new Scroller()

  build() {
    Column() {
      Grid(this.scroller) {
        ForEach(this.dataList, (item: ViewData, index?: number) => {
          GridItem() {
            TapImage({
              uri: item.uri,
              index: index
            })
          }.aspectRatio(1)

        }, (item: ViewData, index?: number) => {
          return JSON.stringify(item) + index;
        })
      }.columnsTemplate('1fr 1fr')
    }

  }
}

@Component
export struct TapImage {
  @StorageLink('tapIndex') @Watch('onTapIndexChange') tapIndex: number = -1;
  @State tapColor: Color = Color.Black;
  private index: number = 0;
  private uri: Resource = {
    id: 0,
    type: 0,
    moduleName: "",
    bundleName: ""
  };

  // 判断是否被选中
  onTapIndexChange() {
    if (this.tapIndex >= 0 && this.index === this.tapIndex) {
      console.info(`tapindex: ${this.tapIndex}, index: ${this.index}, red`)
      this.tapColor = Color.Red;
    } else {
      console.info(`tapindex: ${this.tapIndex}, index: ${this.index}, black`)
      this.tapColor = Color.Black;
    }
  }

  build() {
    Column() {
      Image(this.uri)
        .objectFit(ImageFit.Cover)
        .onClick(() => {
          this.tapIndex = this.index;
        })
        .border({ width: 5, style: BorderStyle.Dotted, color: this.tapColor })
    }

  }
}
```

开发者可以使用emit订阅某个事件并接收事件回调，可以减少开销，增强代码的可读性。

```
// xxx.ets
import emitter from '@ohos.events.emitter';

let NextID: number = 0;

class ViewData {
  title: string;
  uri: Resource;
  color: Color = Color.Black;
  id: number;

  constructor(title: string, uri: Resource) {
    this.title = title;
    this.uri = uri
    this.id = NextID++;
  }
}

@Entry
@Component
struct Gallery2 {
  dataList: Array<ViewData> = [new ViewData('flower', $r('app.media.icon')), new ViewData('OMG', $r('app.media.icon')), new ViewData('OMG', $r('app.media.icon'))]
  scroller: Scroller = new Scroller()
  private preIndex: number = -1

  build() {
    Column() {
      Grid(this.scroller) {
        ForEach(this.dataList, (item: ViewData) => {
          GridItem() {
            TapImage({
              uri: item.uri,
              index: item.id
            })
          }.aspectRatio(1)
          .onClick(() => {
            if (this.preIndex === item.id) {
              return
            }
            let innerEvent: emitter.InnerEvent = { eventId: item.id }
            // 选中态：黑变红
            let eventData: emitter.EventData = {
              data: {
                "colorTag": 1
              }
            }
            emitter.emit(innerEvent, eventData)

            if (this.preIndex != -1) {
              console.info(`preIndex: ${this.preIndex}, index: ${item.id}, black`)
              let innerEvent: emitter.InnerEvent = { eventId: this.preIndex }
              // 取消选中态：红变黑
              let eventData: emitter.EventData = {
                data: {
                  "colorTag": 0
                }
              }
              emitter.emit(innerEvent, eventData)
            }
            this.preIndex = item.id
          })
        }, (item: ViewData) => JSON.stringify(item))
      }.columnsTemplate('1fr 1fr')
    }

  }
}

@Component
export struct TapImage {
  @State tapColor: Color = Color.Black;
  private index: number = 0;
  private uri: Resource = {
    id: 0,
    type: 0,
    moduleName: "",
    bundleName: ""
  };

  onTapIndexChange(colorTag: emitter.EventData) {
    if (colorTag.data != null) {
      this.tapColor = colorTag.data.colorTag ? Color.Red : Color.Black
    }
  }

  aboutToAppear() {
    //定义事件ID
    let innerEvent: emitter.InnerEvent = { eventId: this.index }
    emitter.on(innerEvent, data => {
      this.onTapIndexChange(data)
    })
  }

  build() {
    Column() {
      Image(this.uri)
        .objectFit(ImageFit.Cover)
        .border({ width: 5, style: BorderStyle.Dotted, color: this.tapColor })
    }
  }
}
```

以上通知事件逻辑简单，也可以简化成三元表达式。

```
// xxx.ets
class ViewData {
  title: string;
  uri: Resource;
  color: Color = Color.Black;

  constructor(title: string, uri: Resource) {
    this.title = title;
    this.uri = uri
  }
}

@Entry
@Component
struct Gallery2 {
  dataList: Array<ViewData> = [new ViewData('flower', $r('app.media.icon')), new ViewData('OMG', $r('app.media.icon')), new ViewData('OMG', $r('app.media.icon'))]
  scroller: Scroller = new Scroller()

  build() {
    Column() {
      Grid(this.scroller) {
        ForEach(this.dataList, (item: ViewData, index?: number) => {
          GridItem() {
            TapImage({
              uri: item.uri,
              index: index
            })
          }.aspectRatio(1)

        }, (item: ViewData, index?: number) => {
          return JSON.stringify(item) + index;
        })
      }.columnsTemplate('1fr 1fr')
    }

  }
}

@Component
export struct TapImage {
  @StorageLink('tapIndex') tapIndex: number = -1;
  @State tapColor: Color = Color.Black;
  private index: number = 0;
  private uri: Resource = {
    id: 0,
    type: 0,
    moduleName: "",
    bundleName: ""
  };

  build() {
    Column() {
      Image(this.uri)
        .objectFit(ImageFit.Cover)
        .onClick(() => {
          this.tapIndex = this.index;
        })
        .border({
          width: 5,
          style: BorderStyle.Dotted,
          color: (this.tapIndex >= 0 && this.index === this.tapIndex) ? Color.Red : Color.Black
        })
    }
  }
}
```

## 限制条件

AppStorage与[PersistentStorage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-persiststorage-0000001474017166-V3)以及[Environment](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-environment-0000001473537710-V3)配合使用时，需要注意以下几点：

* 在AppStorage中创建属性后，调用PersistentStorage.persistProp()接口时，会使用在AppStorage中已经存在的值，并覆盖PersistentStorage中的同名属性，所以建议要使用相反的调用顺序，反例可见[在PersistentStorage之前访问AppStorage中的属性](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-persiststorage-0000001474017166-V3#section15461219591)；
* 如果在AppStorage中已经创建属性后，再调用Environment.envProp()创建同名的属性，会调用失败。因为AppStorage已经有同名属性，Environment环境变量不会再写入AppStorage中，所以建议AppStorage中属性不要使用Environment预置环境变量名。
* 状态装饰器装饰的变量，改变会引起UI的渲染更新，如果改变的变量不是用于UI更新，只是用于消息传递，推荐使用 emitter方式。例子可见[不建议借助@StorageLink的双向同步机制实现事件通知](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-appstorage-0000001524417209-V3#section1077010815149)。

