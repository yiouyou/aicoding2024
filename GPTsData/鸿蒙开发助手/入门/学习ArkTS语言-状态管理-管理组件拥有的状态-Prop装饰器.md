# @Prop装饰器：父子单向同步

更新时间: 2024-01-10 11:59

@Prop装饰的变量可以和父组件建立单向的同步关系。@Prop装饰的变量是可变的，但是变化不会同步回其父组件。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Prop装饰的变量和父组件建立单向的同步关系：

* @Prop变量允许在本地修改，但修改后的变化不会同步回父组件。
* 当父组件中的数据源更改时，与之相关的@Prop装饰的变量都会自动更新。如果子组件已经在本地修改了@Prop装饰的相关变量值，而在父组件中对应的@State装饰的变量被修改后，子组件本地修改的@Prop装饰的相关变量值将被覆盖。

## 限制条件

@Prop装饰器不能在@Entry装饰的自定义组件中使用。

## 装饰器使用规则说明

| @Prop变量装饰器    | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 装饰器参数         | 无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 同步类型           | 单向同步：对父组件状态变量值的修改，将同步给子组件@Prop装饰的变量，子组件@Prop变量的修改不会同步到父组件的状态变量上                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 允许装饰的变量类型 | string、number、boolean、enum类型。不支持any，不允许使用undefined和null。必须指定类型。在父组件中，传递给@Prop装饰的值不能为undefined或者null，反例如下所示。CompA ({ aProp: undefined })CompA ({ aProp: null })@Prop和[数据源](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-state-management-overview-0000001524537145-V3#section127619262713)类型需要相同，有以下三种情况（数据源以@State为例）：* @Prop装饰的变量和父组件状态变量类型相同，即@Prop : S和@State : S，示例请参考[父组件@State到子组件@Prop简单数据类型同步](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-prop-0000001473537702-V3#section614118685518)。* 当父组件的状态变量为数组时，@Prop装饰的变量和父组件状态变量的数组项类型相同，即@Prop : S和@State : Array`<S>`，示例请参考[父组件@State数组中的项到子组件@Prop简单数据类型同步](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-prop-0000001473537702-V3#section99561777591)；* 当父组件状态变量为Object或者class时，@Prop装饰的变量和父组件状态变量的属性类型相同，即@Prop : S和@State : { propA: S }，示例请参考[从父组件中的@State类对象属性到@Prop简单类型的同步](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-prop-0000001473537702-V3#section1381944312202)。 |
| 被装饰变量的初始值 | 允许本地初始化。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## 变量的传递/访问规则说明

| 传递/访问          | 说明                                                                                                                                                                                                                         |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 从父组件初始化     | 如果本地有初始化，则是可选的。没有的话，则必选，支持父组件中的常规变量、@State、@Link、@Prop、@Provide、@Consume、@ObjectLink、@StorageLink、@StorageProp、@LocalStorageLink和@LocalStorageProp去初始化子组件中的@Prop变量。 |
| 用于初始化子组件   | @Prop支持去初始化子组件中的常规变量、@State、@Link、@Prop、@Provide。                                                                                                                                                        |
| 是否支持组件外访问 | @Prop装饰的变量是私有的，只能在组件内访问。                                                                                                                                                                                  |

**图1 **初始化规则图示

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231220141802.35462091367785710523209700204534:50001231000000:2800:C0ADD24289C89BF971C7200ADB9176E786FE19793483D8DD9DB91E0173E701C0.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 观察变化和行为表现



### 观察变化

@Prop装饰的数据可以观察到以下变化。

* 当装饰的类型是允许的类型，即string、number、boolean、enum类型都可以观察到的赋值变化；
```
// 简单类型
@Prop count: number;
// 赋值的变化可以被观察到
this.count = 1;
```

对于@State和@Prop的同步场景：

* 使用父组件中@State变量的值初始化子组件中的@Prop变量。当@State变量变化时，该变量值也会同步更新至@Prop变量。
* @Prop装饰的变量的修改不会影响其数据源@State装饰变量的值。
* 除了@State，数据源也可以用@Link或@Prop装饰，对@Prop的同步机制是相同的。
* 数据源和@Prop变量的类型需要相同。

### 框架行为

要理解@Prop变量值初始化和更新机制，有必要了解父组件和拥有@Prop变量的子组件初始渲染和更新流程。

1. 初始渲染：
   1. 执行父组件的build()函数将创建子组件的新实例，将数据源传递给子组件；
   2. 初始化子组件@Prop装饰的变量。
2. 更新：
   1. 子组件@Prop更新时，更新仅停留在当前子组件，不会同步回父组件；
   2. 当父组件的数据源更新时，子组件的@Prop装饰的变量将被来自父组件的数据源重置，所有@Prop装饰的本地的修改将被父组件的更新覆盖。

## 使用场景



### 父组件@State到子组件@Prop简单数据类型同步



以下示例是@State到子组件@Prop简单数据同步，父组件ParentComponent的状态变量countDownStartValue初始化子组件CountDownComponent中@Prop装饰的count，点击“Try again”，count的修改仅保留在CountDownComponent，不会同步给父组件ParentComponent。

ParentComponent的状态变量countDownStartValue的变化将重置CountDownComponent的count。

```
@Component
struct CountDownComponent {
  @Prop count: number;
  costOfOneAttempt: number = 1;

  build() {
    Column() {
      if (this.count > 0) {
        Text(`You have ${this.count} Nuggets left`)
      } else {
        Text('Game over!')
      }
      // @Prop装饰的变量不会同步给父组件
      Button(`Try again`).onClick(() => {
        this.count -= this.costOfOneAttempt;
      })
    }
  }
}

@Entry
@Component
struct ParentComponent {
  @State countDownStartValue: number = 10;

  build() {
    Column() {
      Text(`Grant ${this.countDownStartValue} nuggets to play.`)
      // 父组件的数据源的修改会同步给子组件
      Button(`+1 - Nuggets in New Game`).onClick(() => {
        this.countDownStartValue += 1;
      })
      // 父组件的修改会同步给子组件
      Button(`-1  - Nuggets in New Game`).onClick(() => {
        this.countDownStartValue -= 1;
      })

      CountDownComponent({ count: this.countDownStartValue, costOfOneAttempt: 2 })
    }
  }
}
```

在上面的示例中：

1. CountDownComponent子组件首次创建时其@Prop装饰的count变量将从父组件@State装饰的countDownStartValue变量初始化；
2. 按“+1”或“-1”按钮时，父组件的@State装饰的countDownStartValue值会变化，这将触发父组件重新渲染，在父组件重新渲染过程中会刷新使用countDownStartValue状态变量的UI组件并单向同步更新CountDownComponent子组件中的count值；
3. 更新count状态变量值也会触发CountDownComponent的重新渲染，在重新渲染过程中，评估使用count状态变量的if语句条件（this.count > 0），并执行true分支中的使用count状态变量的UI组件相关描述来更新Text组件的UI显示；
4. 当按下子组件CountDownComponent的“Try again”按钮时，其@Prop变量count将被更改，但是count值的更改不会影响父组件的countDownStartValue值；
5. 父组件的countDownStartValue值会变化时，父组件的修改将覆盖掉子组件CountDownComponent中count本地的修改。

### 父组件@State数组项到子组件@Prop简单数据类型同步

父组件中@State如果装饰的数组，其数组项也可以初始化@Prop。以下示例中父组件Index中@State装饰的数组arr，将其数组项初始化子组件Child中@Prop装饰的value。

```
@Component
struct Child {
  @Prop value: number;

  build() {
    Text(`${this.value}`)
      .fontSize(50)
      .onClick(()=>{this.value++})
  }
}

@Entry
@Component
struct Index {
  @State arr: number[] = [1,2,3];

  build() {
    Row() {
      Column() {
        Child({value: this.arr[0]})
        Child({value: this.arr[1]})
        Child({value: this.arr[2]})

        Divider().height(5)

        ForEach(this.arr, 
          item => {
            Child({value: item})
          }, 
          item => item.toString()
        )
        Text('replace entire arr')
        .fontSize(50)
        .onClick(()=>{
          // 两个数组都包含项“3”。
          this.arr = this.arr[0] == 1 ? [3,4,5] : [1,2,3];
        })
      }
    }
  }
}
```

初始渲染创建6个子组件实例，每个@Prop装饰的变量初始化都在本地拷贝了一份数组项。子组件onclick事件处理程序会更改局部变量值。

如果点击界面上的“1”、“2”、“3”，将所有变量的本地取值都变为“7”。

```
7
7
7
----
7
7
7
```

单击replace entire arr后，屏幕将显示以下信息，为什么？

```
3
4
5
----
7
4
5
```

* 在子组件Child中做的所有的修改都不会同步回父组件Index组件，所以即使6个组件显示都为7，但在父组件Index中，this.arr保存的值依旧是[1,2,3]。
* 点击replace entire arr，this.arr[0] == 1成立，将this.arr赋值为[3, 4, 5]；
* 因为this.arr[0]已更改，Child({value: this.arr[0]})组件将this.arr[0]更新同步到实例@Prop装饰的变量。Child({value: this.arr[1]})和Child({value: this.arr[2]})的情况也类似。
* this.arr的更改触发ForEach更新，this.arr更新的前后都有数值为3的数组项：[3, 4, 5] 和[1, 2, 3]。根据diff算法，数组项“3”将被保留，删除“1”和“2”的数组项，添加为“4”和“5”的数组项。这就意味着，数组项“3”的组件不会重新生成，而是将其移动到第一位。所以“3”对应的组件不会更新，此时“3”对应的组件数值为“7”，ForEach最终的渲染结果是“7”，“4”，“5”。

### 从父组件中的@State类对象属性到@Prop简单类型的同步

如果图书馆有一本图书和两位用户，每位用户都可以将图书标记为已读，此标记行为不会影响其它读者用户。从代码角度讲，对@Prop图书对象的本地更改不会同步给图书馆组件中的@State图书对象。

```
class Book {
  public title: string;
  public pages: number;
  public readIt: boolean = false;

  constructor(title: string, pages: number) {
    this.title = title;
    this.pages = pages;
  }
}

@Component
struct ReaderComp {
  @Prop title: string;
  @Prop readIt: boolean;

  build() {
    Row() {
      Text(this.title)
      Text(`... ${this.readIt ? 'I have read' : 'I have not read it'}`)
        .onClick(() => this.readIt = true)
    }
  }
}

@Entry
@Component
struct Library {
  @State book: Book = new Book('100 secrets of C++', 765);

  build() {
    Column() {
      ReaderComp({ title: this.book.title, readIt: this.book.readIt })
      ReaderComp({ title: this.book.title, readIt: this.book.readIt })
    }
  }
}
```

### @Prop本地初始化不和父组件同步

为了支持@Component装饰的组件复用场景，@Prop支持本地初始化，这样可以让@Prop是否与父组件建立同步关系变得可选。当且仅当@Prop有本地初始化时，从父组件向子组件传递@Prop的数据源才是可选的。

下面的示例中，子组件包含两个@Prop变量：

* @Prop customCounter没有本地初始化，所以需要父组件提供数据源去初始化@Prop，并当父组件的数据源变化时，@Prop也将被更新；
* @Prop customCounter2有本地初始化，在这种情况下，@Prop依旧允许但非强制父组件同步数据源给@Prop。

```
@Component
struct MyComponent {
  @Prop customCounter: number;
  @Prop customCounter2: number = 5;

  build() {
    Column() {
      Row() {
        Text(`From Main: ${this.customCounter}`).fontColor('#ff6b6565').margin({ left: -110, top: 12 })
      }

      Row() {
        Button('Click to change locally !')
          .width(288)
          .height(40)
          .margin({ left: 30, top: 12 })
          .fontColor('#FFFFFF，90%')
          .onClick(() => {
            this.customCounter2++
          })
      }

      Row() {
        Text(`Custom Local: ${this.customCounter2}`).fontColor('#ff6b6565').margin({ left: -110, top: 12 })
      }
    }
  }
}

@Entry
@Component
struct MainProgram {
  @State mainCounter: number = 10;

  build() {
    Column() {
      Row() {
        Column() {
          // customCounter必须从父组件初始化，因为MyComponent的customCounter成员变量缺少本地初始化；此处，customCounter2可以不做初始化。
          MyComponent({ customCounter: this.mainCounter })
          // customCounter2也可以从父组件初始化，父组件初始化的值会覆盖子组件customCounter2的本地初始化的值
          MyComponent({ customCounter: this.mainCounter, customCounter2: this.mainCounter })
        }
      }

      Row() {
        Column() {
          Button('Click to change number')
            .width(288)
            .height(40)
            .margin({ left: 30, top: 12 })
            .fontColor('#FFFFFF，90%')
            .onClick(() => {
              this.mainCounter++
            })
        }
      }
    }
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231220141802.90402567982312873020133749586551:50001231000000:2800:94B9B0FBBEE9CD6F6681A00578BE780083D3A5636F5AEA1ADD05F243670FDE42.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

