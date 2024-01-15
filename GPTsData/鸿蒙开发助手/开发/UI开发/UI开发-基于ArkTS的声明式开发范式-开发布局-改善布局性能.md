# 改善布局性能

更新时间: 2024-01-15 12:17

Flex为采用弹性布局的容器。容器内部的所有子元素，会自动参与弹性布局。子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸。

在单行布局场景下，容器里子组件的主轴尺寸长度总和可能存在不等于容器主轴尺寸长度的情况。例如，三个子组件的宽均为200px，容器宽为500px，当第一个子组件和第二个子组件布局完成后，为了显示第三个子组件，需要给第二个子组件和第三个子组件设置压缩属性[flexShrink](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)，此时第二个子组件会被再布局一次，导致布局效率下降。

## 场景一

所有子组件未设置[displayPriority](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-layout-constraints-0000001427744784-V3)属性（或displayPriority设置为默认值1）和[layoutWeight](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性（或layoutWeight设置为默认值0）时，所有子组件先按序布局一次。

* 第一次布局子组件主轴尺寸长度总和等于容器主轴尺寸长度，不需要二次布局。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.46818115426235369052238484386518:50001231000000:2800:BB38D3872369CD73B20DFC078BB6968C3F64A05DC2995C18CE3E440C2DDD5203.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 第一次布局子组件主轴尺寸长度总和小于容器主轴尺寸长度，且包含设置有效的[flexGrow](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性的子组件，设置有效的flexGrow属性的子组件会触发二次布局，拉伸布局填满容器。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.56485760498246700612123109539472:50001231000000:2800:4BF2FC641B7366877F6DBCC59AE91CC38DB06CDA296A74EABF236F0196D0EEB4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 第一次布局子组件主轴尺寸长度总和大于容器主轴尺寸长度，且包含设置有效的flexShrink属性（flex子组件默认值为1，为有效值）的子组件，设置有效的flexShrink属性的子组件会触发二次布局，压缩布局填满容器。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.08424079892667659624461236971158:50001231000000:2800:0C9DB66D3FD61E2CF4A754592AAA6F5E47B55B5DD9D41AF60CE5972EDB968E3D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景二

子组件存在设置displayPriority属性，不存在设置layoutWeight属性。

根据displayPriority从大到小顺序，布局每组同displayPriority值的子组件，直到子组件主轴尺寸长度总和最大且不超过容器主轴尺寸长度，舍弃未布局的低优先级displayPriority（可能存在一组临界displayPriority值的子组件布局但未使用的情况）。

* 第一次布局子组件主轴尺寸长度总和等于容器主轴尺寸长度，不需要二次布局。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.79492943016652148945301873629113:50001231000000:2800:59F0E90C21F19340234CEDE653882BC2D4DBB9CDE0BB71B9E36230A2D9E01A49.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 第一次布局子组件主轴尺寸长度总和小于容器主轴尺寸长度，且包含设置有效的flexGrow属性的子组件，设置有效的flexGrow属性的子组件会触发二次布局，拉伸布局填满容器。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.33065224215722752937991080435094:50001231000000:2800:704CFB4261724AEB0D61A9AC7F0C70364655D8011972C9760BE390EE1F01E197.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景三

子组件中存在设置layoutWeight属性。

根据displayPriority从大到小顺序，对设置displayPriority相同值的子组件且不设置layoutWeight属性的子组件进行布局，直到子组件主轴尺寸长度的总和最大且不超过容器主轴尺寸长度。如果子组件主轴尺寸长度的总和超过了容器主轴尺寸长度，舍弃未布局的低优先级displayPriority，可能存在一组临界displayPriority值的子组件布局但未使用的情况。

剩余空间按设置layoutWeight属性的子组件的layoutWeight比例填满容器。

* 两次遍历都只布局一次组件，不会触发二次布局。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.71664618830295189729587921575867:50001231000000:2800:AD9EA72B2E9FAB79F930BEDF2B9094F1B365D57A840031D2A2B4F5FACF0D4446.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 如何优化Flex的布局性能

* 使用Column/Row代替Flex。
* 大小不需要变更的子组件主动设置flexShrink属性值为0。
* 优先使用layoutWeight属性替代flexGrow属性和flexShrink属性。
* 子组件主轴长度分配设置为最常用场景的布局结果，使子组件主轴长度总和等于Flex容器主轴长度。

