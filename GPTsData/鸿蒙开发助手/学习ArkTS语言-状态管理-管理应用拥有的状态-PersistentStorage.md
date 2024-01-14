# PersistentStorage：持久化存储UI状态

更新时间: 2024-01-10 12:00

前两个小节介绍的LocalStorage和AppStorage都是运行时的内存，但是在应用退出再次启动后，依然能保存选定的结果，是应用开发中十分常见的现象，这就需要用到PersistentStorage。

PersistentStorage是应用程序中的可选单例对象。此对象的作用是持久化存储选定的AppStorage属性，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。

## 概述

PersistentStorage将选定的AppStorage属性保留在设备磁盘上。应用程序通过API，以决定哪些AppStorage属性应借助PersistentStorage持久化。UI和业务逻辑不直接访问PersistentStorage中的属性，所有属性访问都是对AppStorage的访问，AppStorage中的更改会自动同步到PersistentStorage。

PersistentStorage和AppStorage中的属性建立双向同步。应用开发通常通过AppStorage访问PersistentStorage，另外还有一些接口可以用于管理持久化属性，但是业务逻辑始终是通过AppStorage获取和设置属性的。

## 限制条件

PersistentStorage允许的类型和值有：

* number, string, boolean, enum 等简单类型。
* 可以被JSON.stringify()和JSON.parse()重构的对象。例如Date, Map, Set等内置类型则不支持，以及对象的属性方法不支持持久化。

PersistentStorage不允许的类型和值有：

* 不支持嵌套对象（对象数组，对象的属性是对象等）。因为目前框架无法检测AppStorage中嵌套对象（包括数组）值的变化，所以无法写回到PersistentStorage中。
* 不支持undefined 和 null 。

持久化数据是一个相对缓慢的操作，应用程序应避免以下情况：

* 持久化大型数据集。
* 持久化经常变化的变量。

PersistentStorage的持久化变量最好是小于2kb的数据，不要大量的数据持久化，因为PersistentStorage写入磁盘的操作是同步的，大量的数据本地化读写会同步在UI线程中执行，影响UI渲染性能。如果开发者需要存储大量的数据，建议使用数据库api。

PersistentStorage只能在UI页面内使用，否则将无法持久化数据。

## 支持的接口

### PersistProp

static PersistProp `<T>`(key: string, defaultValue: T): void

将AppStorage中key对应的属性持久化到文件中。该接口的调用通常在访问AppStorage之前。

确定属性的类型和值的顺序如下：

1. 如果PersistentStorage文件中存在key对应的属性，在AppStorage中创建对应的propName，并用在PersistentStorage中找到的key的属性初始化。
2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。
3. 如果AppStorage也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值，覆盖掉PersistentStorage文件中的值。由于AppStorage是内存内数据，该行为会导致数据丧失持久化能力。

参数：

| 参数名       | 类型   | 必填 | 参数描述                                                                                         |
| :----------- | :----- | :--- | :----------------------------------------------------------------------------------------------- |
| key          | string | 是   | 属性名。                                                                                         |
| defaultValue | T      | 是   | 在PersistentStorage和AppStorage未查询到时，则使用默认值初始化初始化它。不允许为undefined和null。 |

示例：

```
PersistentStorage.PersistProp('highScore', '0');
```

### DeleteProp

static DeleteProp(key: string): void

将key对应的属性从PersistentStorage删除，后续AppStorage的操作，对PersistentStorage不会再有影响。

参数：

| 参数名 | 类型   | 必填 | 参数描述                      |
| :----- | :----- | :--- | :---------------------------- |
| key    | string | 是   | PersistentStorage中的属性名。 |

示例：

```
PersistentStorage.DeleteProp('highScore');
```

### PersistProps

static PersistProps(properties: {key: string, defaultValue: any;}[]): void

行为和PersistProp类似，不同在于可以一次性持久化多个数据，适合在应用启动的时候初始化。

参数：

| 参数名     | 类型                               | 必填 | 参数描述                                                               |
| :--------- | :--------------------------------- | :--- | :--------------------------------------------------------------------- |
| key        | string                             | 是   | 属性名。                                                               |
| properties | {key: string, defaultValue: any}[] | 是   | 持久化数组，启动key为属性名，defaultValue为默认值。规则同PersistProp。 |

示例：

```
PersistentStorage.PersistProps([{ key: 'highScore', defaultValue: '0' }, { key: 'wightScore', defaultValue: '1' }]);
```

### Keys

static Keys(): Array `<string>`

返回所有持久化属性的key的数组。

返回值：

| 类型               | 描述                            |
| :----------------- | :------------------------------ |
| Array `<string>` | 返回所有持久化属性的key的数组。 |

示例：

```
let keys: Array<string> = PersistentStorage.Keys();
```

## 使用场景

### 从AppStorage中访问PersistentStorage初始化的属性

1. 初始化PersistentStorage：

```
PersistentStorage.PersistProp('aProp', 47);
```

2. 在AppStorage获取对应属性：

```
AppStorage.Get('aProp'); // returns 47
```

  或在组件内部定义：

```
@StorageLink('aProp') aProp: number = 48;
```

完整代码如下：

```
PersistentStorage.PersistProp('aProp', 47);

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'
  @StorageLink('aProp') aProp: number = 48

  build() {
    Row() {
      Column() {
        Text(this.message)
        // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
        Text(`${this.aProp}`)
          .onClick(() => {
            this.aProp += 1;
          })
      }
    }
  }
}
```

说明

当前持久化存储在API9模拟器上暂不支持。

* 新应用安装后首次启动运行：
  1. 调用PersistProp初始化PersistentStorage，首先查询在PersistentStorage本地文件中是否存在“aProp”，查询结果为不存在，因为应用是第一次安装。
  2. 接着查询属性“aProp”在AppStorage中是否存在，依旧不存在。
  3. 在AppStorge中创建名为“aProp”的number类型属性，属性初始值是定义的默认值47。
  4. PersistentStorage将属性“aProp”和值47写入磁盘，AppStorage中“aProp”对应的值和其后续的更改将被持久化。
  5. 在Index组件中创建状态变量@StorageLink('aProp') aProp，和AppStorage中“aProp”双向绑定，在创建的过程中会在AppStorage中查找，成功找到“aProp”，所以使用其在AppStorage找到的值47。

图1 PersistProp初始化流程

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240108115421.45693146978081370354237562406896:50001231000000:2800:4BE07A3C73C5C8582085D2AA35D09F9D51CE7D11503577BF58B318DB1771BF40.png?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 触发点击事件后：
  1. 状态变量@StorageLink('aProp') aProp改变，触发Text组件重新刷新。
  2. @StorageLink装饰的变量是和AppStorage中建立双向同步的，所以@StorageLink('aProp') aProp的变化会被同步回AppStorage中。
  3. AppStorage中“aProp”属性的改变会同步到所有绑定该“aProp”的单向或者双向变量，在本示例中没有其他的绑定“aProp”的变量。
  4. 因为“aProp”对应的属性已经被持久化，所以在AppStorage中“aProp”的改变会触发PersistentStorage将新的改变写入本地磁盘。
* 后续启动应用：
  1. 执行PersistentStorage.PersistProp('aProp', 47)，在首先查询在PersistentStorage本地文件查询“aProp”属性，成功查询到。
  2. 将在PersistentStorage查询到的值写入AppStorage中。
  3. 在Index组件里，@StorageLink绑定的“aProp”为PersistentStorage写入AppStorage中的值，即为上一次退出引用存入的值。

### 在PersistentStorage之前访问AppStorage中的属性

该示例为反例。在调用PersistentStorage.PersistProp或者PersistProps之前使用接口访问AppStorage中的属性是错误的，因为这样的调用顺序会丢失上一次应用程序运行中的属性值：

```
let aProp = AppStorage.SetOrCreate('aProp', 47);
PersistentStorage.PersistProp('aProp', 48);
```

应用在非首次运行时，先执行AppStorage.SetOrCreate('aProp', 47)：属性“aProp”在AppStorage中创建，其类型为number，其值设置为指定的默认值47。'aProp'是持久化的属性，所以会被写回PersistentStorage磁盘中，PersistentStorage存储的上次退出应用的值丢失。

PersistentStorage.PersistProp('aProp', 48)：在PersistentStorage中查找到“aProp”，找到，值为47。

