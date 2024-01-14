# ForEach：循环渲染

更新时间: 2024-01-11 09:52

ForEach接口基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为[List组件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-list-0000001477981213-V3)。

说明

从API version 9开始，该接口支持在ArkTS卡片中使用。

## 接口描述

```
ForEach(
  arr: Array,
  itemGenerator: (item: any, index?: number) => void,
  keyGenerator?: (item: any, index?: number) => string
)
```

| 参数名        | 参数类型                              | 必填 | 参数描述                                                                                                                                                                                                                                                                                                                                                 |
| :------------ | :------------------------------------ | :--- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| arr           | Array                                 | 是   | 数据源，为Array类型的数组。说明 ：- 可以设置为空数组，此时不会创建子组件。- 可以设置返回值为数组类型的函数，例如arr.slice(1, 3)，但设置的函数不应改变包括数组本身在内的任何状态变量，例如不应使用Array.splice(),Array.sort()或Array.reverse()这些会改变原数组的函数。                                                                          |
| itemGenerator | (item: any, index?: number) => void   | 是   | 组件生成函数。- 为数组中的每个元素创建对应的组件。- item参数：arr数组中的数据项。- index参数（可选）：arr数组中的数据项索引。说明 ：- 组件的类型必须是ForEach的父容器所允许的。例如，ListItem组件要求ForEach的父容器组件必须为List组件。                                                                                                       |
| keyGenerator  | (item: any, index?: number) => string | 否   | 键值生成函数。- 为数据源arr的每个数组项生成唯一且持久的键值。函数返回值为开发者自定义的键值生成规则。- item参数：arr数组中的数据项。- index参数（可选）：arr数组中的数据项索引。说明 ：- 如果函数缺省，框架默认的键值生成函数为(item: T, index: number) => { return index + '__' + JSON.stringify(item); }- 键值生成函数不应改变任何组件状态。 |

说明

* ForEach的itemGenerator函数可以包含if/else条件渲染逻辑。另外，也可以在if/else条件渲染语句中使用ForEach组件。
* 在初始化渲染时，ForEach会加载数据源的所有数据，并为每个数据项创建对应的组件，然后将其挂载到渲染树上。如果数据源非常大或有特定的性能需求，建议使用LazyForEach组件。

## 键值生成规则

在ForEach循环渲染过程中，系统会为每个数组元素生成一个唯一且持久的键值，用于标识对应的组件。当这个键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。

ForEach提供了一个名为keyGenerator的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: any, index: number) => { return index + '__' + JSON.stringify(item); }。

ArkUI框架对于ForEach的键值生成有一套特定的判断规则，这主要与itemGenerator函数的第二个参数index以及keyGenerator函数的第二个参数index有关，具体的键值生成规则判断逻辑如下图所示。

图1 ForEach键值生成规则
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.16130798199373503491694458654771:50001231000000:2800:142630CA8434DA7D7B9C1A02BCE11E520D8CC08D4B08DF1B5F865B8CF90F477F.png?needInitFileName=true?needInitFileName=true "点击放大")

说明

ArkUI框架会对重复的键值发出警告。在UI更新的场景下，如果出现重复的键值，框架可能无法正常工作，具体请参见[渲染结果非预期](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section223mcpsimp)。

## 组件创建规则

在确定键值生成规则后，ForEach的第二个参数itemGenerator函数会根据键值生成规则为数据源的每个数组项创建组件。组件的创建包括两种情况：[ForEach首次渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section159mcpsimp)和[ForEach非首次渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section169mcpsimp)。

### 首次渲染

在ForEach首次渲染时，会根据前述键值生成规则为数据源的每个数组项生成唯一键值，并创建相应的组件。

```
@Entry
@Component
struct Parent {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Row() {
      Column() {
        ForEach(this.simpleList, (item: string) => {
          ChildItem({ item: item })
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

运行效果如下图所示。

图2 ForEach数据源不存在相同值案例首次渲染运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.45620177961881589253099737640561:50001231000000:2800:E084B598772BFFB3ACC834B40C3F81DEE8E32121292C59062BB1FFF4C2882DE2.png?needInitFileName=true?needInitFileName=true "点击放大")

在上述代码中，键值生成规则是keyGenerator函数的返回值item。在ForEach渲染循环时，为数据源数组项依次生成键值one、two和three，并创建对应的ChildItem组件渲染到界面上。

当不同数组项按照键值生成规则生成的键值相同时，框架的行为是未定义的。例如，在以下代码中，ForEach渲染相同的数据项two时，只创建了一个ChildItem组件，而没有创建多个具有相同键值的组件。

```
@Entry
@Component
struct Parent {
  @State simpleList: Array<string> = ['one', 'two', 'two', 'three'];

  build() {
    Row() {
      Column() {
        ForEach(this.simpleList, (item: string) => {
          ChildItem({ item: item })
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

运行效果如下图所示。

图3 ForEach数据源存在相同值案例首次渲染运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.23533213074863515961891346641854:50001231000000:2800:BE4D5E710E4F8B18DC07EB1FFB957113AE6C91CDB87BDED1EAEB08C37BF1D7CD.png?needInitFileName=true?needInitFileName=true "点击放大")

在该示例中，最终键值生成规则为item。当ForEach遍历数据源simpleList，遍历到索引为1的two时，按照最终键值生成规则生成键值为two的组件并进行标记。当遍历到索引为2的two时，按照最终键值生成规则当前项的键值也为two，此时不再创建新的组件。

### 非首次渲染

在ForEach组件进行非首次渲染时，它会检查新生成的键值是否在上次渲染中已经存在。如果键值不存在，则会创建一个新的组件；如果键值存在，则不会创建新的组件，而是直接渲染该键值所对应的组件。例如，在以下的代码示例中，通过点击事件修改了数组的第三项值为"new three"，这将触发ForEach组件进行非首次渲染。

```
@Entry
@Component
struct Parent {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Row() {
      Column() {
        Text('点击修改第3个数组项的值')
          .fontSize(24)
          .fontColor(Color.Red)
          .onClick(() => {
            this.simpleList[2] = 'new three';
          })

        ForEach(this.simpleList, (item: string) => {
          ChildItem({ item: item })
            .margin({ top: 20 })
        }, (item: string) => item)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(30)
  }
}
```

运行效果如下图所示。

图4 ForEach非首次渲染案例运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.17460204640259301359757476130390:50001231000000:2800:D4874FCE88EB1266103D4C33C8C8D18F09B2CDC65FF2D00EF9D21AC829C69F19.gif?needInitFileName=true?needInitFileName=true "点击放大")

从本例可以看出@State 能够监听到简单数据类型数组数据源 simpleList 数组项的变化。

1. 当 simpleList 数组项发生变化时，会触发 ForEach 进行重新渲染。
2. ForEach 遍历新的数据源 ['one', 'two', 'new three']，并生成对应的键值one、two和new three。
3. 其中，键值one和two在上次渲染中已经存在，所以 ForEach 复用了对应的组件并进行了渲染。对于第三个数组项 "new three"，由于其通过键值生成规则 item 生成的键值new three在上次渲染中不存在，因此 ForEach 为该数组项创建了一个新的组件。

## 使用场景

ForEach组件在开发过程中的主要应用场景包括：[数据源不变](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section182mcpsimp)、[数据源数组项发生变化](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section189mcpsimp)（如插入、删除操作）、[数据源数组项子属性变化](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section15662921144118)。

### 数据源不变

在数据源保持不变的场景中，数据源可以直接采用基本数据类型。例如，在页面加载状态时，可以使用骨架屏列表进行渲染展示。

```
@Entry
@Component
struct ArticleList {
  @State simpleList: Array<number> = [1, 2, 3, 4, 5];

  build() {
    Column() {
      ForEach(this.simpleList, (item: string) => {
        ArticleSkeletonView()
          .margin({ top: 20 })
      }, (item: string) => item)
    }
    .padding(20)
    .width('100%')
    .height('100%')
  }
}

@Builder
function textArea(width: number | Resource | string = '100%', height: number | Resource | string = '100%') {
  Row()
    .width(width)
    .height(height)
    .backgroundColor('#FFF2F3F4')
}

@Component
struct ArticleSkeletonView {
  build() {
    Row() {
      Column() {
        textArea(80, 80)
      }
      .margin({ right: 20 })

      Column() {
        textArea('60%', 20)
        textArea('50%', 20)
      }
      .alignItems(HorizontalAlign.Start)
      .justifyContent(FlexAlign.SpaceAround)
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

运行效果如下图所示。

图5 骨架屏运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.56954558907334525894558351540203:50001231000000:2800:CE259F1577A420BBD751D5FA57D7D7F0E5CF9DE310FC44B2483AB6D6199ED504.png?needInitFileName=true?needInitFileName=true)

在本示例中，采用数据项item作为键值生成规则，由于数据源simpleList的数组项各不相同，因此能够保证键值的唯一性。

### 数据源数组项发生变化

在数据源数组项发生变化的场景下，例如进行数组插入、删除操作或者数组项索引位置发生交换时，数据源应为对象数组类型，并使用对象的唯一ID作为最终键值。例如，当在页面上通过手势上滑加载下一页数据时，会在数据源数组尾部新增新获取的数据项，从而使得数据源数组长度增大。

```
@Entry
@Component
struct ArticleListView {
  @State isListReachEnd: boolean = false;
  @State articleList: Array<Article> = [
    new Article('001', '第1篇文章', '文章简介内容'),
    new Article('002', '第2篇文章', '文章简介内容'),
    new Article('003', '第3篇文章', '文章简介内容'),
    new Article('004', '第4篇文章', '文章简介内容'),
    new Article('005', '第5篇文章', '文章简介内容'),
    new Article('006', '第6篇文章', '文章简介内容')
  ]

  loadMoreArticles() {
    this.articleList.push(new Article('007', '加载的新文章', '文章简介内容'));
  }

  build() {
    Column({ space: 5 }) {
      List() {
        ForEach(this.articleList, (item: Article) => {
          ListItem() {
            ArticleCard({ article: item })
              .margin({ top: 20 })
          }
        }, (item: Article) => item.id)
      }
      .onReachEnd(() => {
        this.isListReachEnd = true;
      })
      .parallelGesture(
        PanGesture({ direction: PanDirection.Up, distance: 80 })
          .onActionStart(() => {
            if (this.isListReachEnd) {
              this.loadMoreArticles();
              this.isListReachEnd = false;
            }
          })
      )
      .padding(20)
      .scrollBar(BarState.Off)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ArticleCard {
  @Prop article: Article;

  build() {
    Row() {
      Image($r('app.media.icon'))
        .width(80)
        .height(80)
        .margin({ right: 20 })

      Column() {
        Text(this.article.title)
          .fontSize(20)
          .margin({ bottom: 8 })
        Text(this.article.brief)
          .fontSize(16)
          .fontColor(Color.Gray)
          .margin({ bottom: 8 })
      }
      .alignItems(HorizontalAlign.Start)
      .width('80%')
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

初始运行效果（左图）和手势上滑加载后效果（右图）如下图所示。

图6 数据源数组项变化案例运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.58709380209645434377123107107143:50001231000000:2800:18485E5441C4C84C2F3E452C86D36D12CA73FE486FA10AB7855B7B1B254F7D2A.png?needInitFileName=true?needInitFileName=true "点击放大")

在本示例中，ArticleCard组件作为ArticleListView组件的子组件，通过@Prop装饰器接收一个Article对象，用于渲染文章卡片。

1. 当列表滚动到底部时，如果手势滑动距离超过指定的80，将触发loadMoreArticle()函数。此函数会在articleList数据源的尾部添加一个新的数据项，从而增加数据源的长度。
2. 数据源被@State装饰器修饰，ArkUI框架能够感知到数据源长度的变化，并触发ForEach进行重新渲染。

### 数据源数组项子属性变化

当数据源的数组项为对象数据类型，并且只修改某个数组项的属性值时，由于数据源为复杂数据类型，ArkUI框架无法监听到@State装饰器修饰的数据源数组项的属性变化，从而无法触发ForEach的重新渲染。为实现ForEach重新渲染，需要结合@Observed和@ObjectLink装饰器使用。例如，在文章列表卡片上点击“点赞”按钮，从而修改文章的点赞数量。

```
@Entry
@Component
struct ArticleListView {
  @State articleList: Array<Article> = [
    new Article('001', '第0篇文章', '文章简介内容', false, 100),
    new Article('002', '第1篇文章', '文章简介内容', false, 100),
    new Article('003', '第2篇文章', '文章简介内容', false, 100),
    new Article('004', '第4篇文章', '文章简介内容', false, 100),
    new Article('005', '第5篇文章', '文章简介内容', false, 100),
    new Article('006', '第6篇文章', '文章简介内容', false, 100),
  ];

  build() {
    List() {
      ForEach(this.articleList, (item: Article) => {
        ListItem() {
          ArticleCard({
            article: item
          })
            .margin({ top: 20 })
        }
      }, (item: Article) => item.id)
    }
    .padding(20)
    .scrollBar(BarState.Off)
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ArticleCard {
  @ObjectLink article: Article;

  handleLiked() {
    this.article.isLiked = !this.article.isLiked;
    this.article.likesCount = this.article.isLiked ? this.article.likesCount + 1 : this.article.likesCount - 1;
  }

  build() {
    Row() {
      Image($r('app.media.icon'))
        .width(80)
        .height(80)
        .margin({ right: 20 })

      Column() {
        Text(this.article.title)
          .fontSize(20)
          .margin({ bottom: 8 })
        Text(this.article.brief)
          .fontSize(16)
          .fontColor(Color.Gray)
          .margin({ bottom: 8 })

        Row() {
          Image(this.article.isLiked ? $r('app.media.iconLiked') : $r('app.media.iconUnLiked'))
            .width(24)
            .height(24)
            .margin({ right: 8 })
          Text(this.article.likesCount.toString())
            .fontSize(16)
        }
        .onClick(() => this.handleLiked())
        .justifyContent(FlexAlign.Center)
      }
      .alignItems(HorizontalAlign.Start)
      .width('80%')
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

上述代码的初始运行效果（左图）和点击第1个文章卡片上的点赞图标后的运行效果（右图）如下图所示。

图7 数据源数组项子属性变化案例运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.82043625174503665138198963538268:50001231000000:2800:E026AE3E13E406CD10167262270DAAB49C1A43FCDF1559F51AC2490309D9FF01.png?needInitFileName=true?needInitFileName=true "点击放大")

在本示例中，Article类被@Observed装饰器修饰。父组件ArticleListView传入Article对象实例给子组件ArticleCard，子组件使用@ObjectLink装饰器接收该实例。

1. 当点击第1个文章卡片上的点赞图标时，会触发ArticleCard组件的handleLiked函数。该函数修改第1个卡片对应组件里article实例的isLiked和likesCount属性值。
2. 由于子组件ArticleCard中的article使用了@ObjectLink装饰器，父子组件共享同一份article数据。因此，父组件中articleList的第1个数组项的isLiked和likedCounts数值也会同步修改。
3. 当父组件监听到数据源数组项属性值变化时，会触发ForEach重新渲染。
4. 在此处，ForEach键值生成规则为数组项的id属性值。当ForEach遍历新数据源时，数组项的id均没有变化，不会新建组件。
5. 渲染第1个数组项对应的ArticleCard组件时，读取到的isLiked和likesCount为修改后的新值。

## 使用建议

* 尽量避免在最终的键值生成规则中包含数据项索引index，以防止出现[渲染结果非预期](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section223mcpsimp)和[渲染性能降低](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section234mcpsimp)。如果业务确实需要使用index，例如列表需要通过index进行条件渲染，开发者需要接受ForEach在改变数据源后重新创建组件所带来的性能损耗。

* 为满足键值的唯一性，对于对象数据类型，建议使用对象数据中的唯一id作为键值。
* 基本数据类型的数据项没有唯一ID属性。如果使用基本数据类型本身作为键值，必须确保数组项无重复。因此，对于数据源会发生变化的场景，建议将基本数据类型数组转化为具备唯一ID属性的对象数据类型数组，再使用ID属性作为键值生成规则。

## 不推荐案例

开发者在使用ForEach的过程中，若对于键值生成规则的理解不够充分，可能会出现错误的使用方式。错误使用一方面会导致功能层面问题，例如[渲染结果非预期](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section223mcpsimp)，另一方面会导致性能层面问题，例如[渲染性能降低](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section234mcpsimp)。

### 渲染结果非预期

在本示例中，通过设置ForEach的第三个参数KeyGenerator函数，自定义键值生成规则为数据源的索引index的字符串类型值。当点击父组件Parent中“在第1项后插入新项”文本组件后，界面会出现非预期的结果。

```
@Entry
@Component
struct Parent {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Column() {
      Button() {
        Text('在第1项后插入新项').fontSize(30)
      }
      .onClick(() => {
        this.simpleList.splice(1, 0, 'new item');
      })

      ForEach(this.simpleList, (item: string) => {
        ChildItem({ item: item })
      }, (item: string, index: number) => index.toString())
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(30)
  }
}
```

上述代码的初始渲染效果（左图）和点击“在第1项后插入新项”文本组件后的渲染效果（右图）如下图所示。

图8 渲染结果非预期运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.26829023044205909951190383285753:50001231000000:2800:A1EC7305D27E528FFF4EFE081987B0FD8747125D731A0491AFE5366D22F6FE1D.gif?needInitFileName=true?needInitFileName=true)

ForEach在首次渲染时，创建的键值依次为"0"、"1"、"2"。

插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。

ForEach依次遍历新数据源，遍历数据项"one"时生成键值"0"，存在相同键值，因此不创建新组件。继续遍历数据项"new item"时生成键值"1"，存在相同键值，因此不创建新组件。继续遍历数据项"two"生成键值"2"，存在相同键值，因此不创建新组件。最后遍历数据项"three"时生成键值"3"，不存在相同键值，创建内容为"three"的新组件并渲染。

从以上可以看出，当最终键值生成规则包含index时，期望的界面渲染结果为['one', 'new item', 'two', 'three']，而实际的渲染结果为['one', 'two', 'three', 'three']，渲染结果不符合开发者预期。因此，开发者在使用ForEach时应尽量避免最终键值生成规则中包含index。

### 渲染性能降低

在本示例中，ForEach的第三个参数KeyGenerator函数处于缺省状态。根据上述[键值生成规则](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3#section147mcpsimp)，此例使用框架默认的键值生成规则，即最终键值为字符串index + '__' + JSON.stringify(item)。当点击“在第1项后插入新项”文本组件后，ForEach将需要为第2个数组项以及其后的所有项重新创建组件。

```
@Entry
@Component
struct Parent {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Column() {
      Button() {
        Text('在第1项后插入新项').fontSize(30)
      }
      .onClick(() => {
        this.simpleList.splice(1, 0, 'new item');
        console.log(`[onClick]: simpleList is ${JSON.stringify(this.simpleList)}`);
      })

      ForEach(this.simpleList, (item: string) => {
        ChildItem({ item: item })
      })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ChildItem {
  @Prop item: string;

  aboutToAppear() {
    console.log(`[aboutToAppear]: item is ${this.item}`);
  }

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

以上代码的初始渲染效果（左图）和点击"在第1项后插入新项"文本组件后的渲染效果（右图）如下所示。

图9 渲染性能降低案例运行效果图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.70569445534251363222431133658361:50001231000000:2800:B0FEBE7B40F72CF3AE21E4616D95A7D65CEEB33E56E29935C96307093DF2F15E.gif?needInitFileName=true?needInitFileName=true)

点击“在第1项后插入新项”文本组件后，IDE的日志打印结果如下所示。

图10 插入新项后渲染效果
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113019.17410119382834838142228048902557:50001231000000:2800:140EBFABEC22BE411F20BF79C9873F7BEBD86A03733C18F5857E829A1754627D.png?needInitFileName=true?needInitFileName=true "点击放大")插入新项后，ForEach为new item、 two、 three三个数组项创建了对应的组件ChildItem，并执行了组件的[aboutToAppear()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/arkts-custom-component-lifecycle-0000001482395076-V3)生命周期函数。这是因为：

1. 在ForEach首次渲染时，创建的键值依次为0__one、1__two、2__three。
2. 插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，ArkUI框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。
3. ForEach依次遍历新数据源，遍历数据项one时生成键值0__one，键值已存在，因此不创建新组件。继续遍历数据项new item时生成键值1__new item，不存在相同键值，创建内容为new item的新组件并渲染。继续遍历数据项two生成键值2__two，不存在相同键值，创建内容为two的新组件并渲染。最后遍历数据项three时生成键值3__three，不存在相同键值，创建内容为three的新组件并渲染。

尽管此示例中界面渲染的结果符合预期，但每次插入一条新数组项时，ForEach都会为从该数组项起后面的所有数组项全部重新创建组件。当数据源数据量较大或组件结构复杂时，由于组件无法得到复用，将导致性能体验不佳。因此，除非必要，否则不推荐将第三个参数KeyGenerator函数处于缺省状态，以及在键值生成规则中包含数据项索引index。

