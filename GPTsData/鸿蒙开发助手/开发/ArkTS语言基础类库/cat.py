p = [
    'UI开发-ArkTS语言基础类库-ArkTS语言基础类库概述.md',
    'UI开发-ArkTS语言基础类库-并发-并发概述.md',
    'UI开发-ArkTS语言基础类库-并发-使用异步并发能力进行开发-异步并发概述.md',
    'UI开发-ArkTS语言基础类库-并发-使用异步并发能力进行开发-单次IO任务开发指导.md',
    'UI开发-ArkTS语言基础类库-并发-使用多线程并发能力进行开发-多线程并发概述.md',
    'UI开发-ArkTS语言基础类库-并发-使用多线程并发能力进行开发-TaskPool和Worker的对比.md',
    'UI开发-ArkTS语言基础类库-并发-使用多线程并发能力进行开发-Concurrent装饰器.md',
    'UI开发-ArkTS语言基础类库-并发-使用多线程并发能力进行开发-CPU密集型任务开发指导.md',
    'UI开发-ArkTS语言基础类库-并发-使用多线程并发能力进行开发-IO密集型任务开发指导.md',
    'UI开发-ArkTS语言基础类库-并发-使用多线程并发能力进行开发-同步任务开发指导.md',
    'UI开发-ArkTS语言基础类库-容器类库-容器类库概述.md',
    'UI开发-ArkTS语言基础类库-容器类库-线性容器.md',
    'UI开发-ArkTS语言基础类库-容器类库-非线性容器.md',
    'UI开发-ArkTS语言基础类库-XML生成解析与转换-XML概述.md',
    'UI开发-ArkTS语言基础类库-XML生成解析与转换-XML生成.md',
    'UI开发-ArkTS语言基础类库-XML生成解析与转换-XML解析.md',
    'UI开发-ArkTS语言基础类库-XML生成解析与转换-XML转换.md',
]


# for i in p:
#     with open(i, 'w', encoding='utf-8') as f:
#         f.write('')
# exit()

def readF(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        # li = f.readlines()
        # for i in li:
        #     if i.startswith('  图'):
        #         print(fn, i)
        out = f.read()
        out1 = out.replace('[]()[]()', '')
        out2 = out.replace('**', '')
        if out != out1:
            print(fn, '[]()[]()')
        if out != out2:
            print(fn, '**')
        return out
                
str = ''
for i in p:
    # print(i)
    str += readF(i) + "\n\n"

# print(str)

with open('cat.txt', 'w', encoding='utf-8') as f:
    f.write(str)

