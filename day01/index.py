#
# Python是一种优雅而健壮的编程语言，崇尚优美、明确、
# 简单，是一种优秀并广泛使用的语言，它继承了传统编译语言的
# 强大性和通用性，同时也借鉴了简单脚本和解释语言的易用性。
# 它可以帮您完成任意想完成的工作，只有想不到，没有Python做不到。

# 数据类型
# 数字类型 整数 实数 复数

a = 1

print(type(a))
b = 1

b = 3e14

a = 2

a = 3 + 4j

b = 4 + 4j

print(type(a))

print(a + b)

print(id(b))

# 数值操作符
a = 1
c = a * a

print(c)
print(type(c))

print('hello  world \"xxx\"')

print('''
asdsadasdas
asdasdass
asdadas
''')

str = "__sadasd"

print(str.removeprefix("__"))

print(str.capitalize())

list1 = [1, 2, 3]

list4 = list([1, 2, 3])

print(list4)

print(list1[-1:-4:1])

print(id(list1))

list3 = list1 * 2

print(sum(list3))

list4 = list((1, (2, 23,), 3, {'1': 2}))

print(list4)

xx = list4[3]

print(xx.get('1'))

a, b, c, d = [1, 2, 3, 4]

print(a, b, c, d)

dict1 = {'a': 1}

print(dict1.get('b') == None)

dict1['a'] = 3

print(dict1['a'])

del dict1['a']


print(dict1)

dict2 = dict(name="jinhui", age=23)

dict3 = dict(school="致富小学")

dict2.update(dict3)

print(type(dict2.items()))

for k,v in dict2.items():
    print("k %s, v %s"%(k,v))

alis = dict2.copy()

alis['name'] = "FangJinHui"

for k,v in dict2.items():
    print("k %s, v %s"%(k,v))

for k,v in alis.items():
    print("k %s, v %s"%(k,v))


def 字符频率(str:""):
    dict5 = {}
    for i in str:
        dict5[i] = dict5.get(i,0) + 1
    return dict5

dict6 = 字符频率("ASDCXSAASSXXXXXXX")

dict7 = list(dict6.items())

dict7.sort(reverse=True)

import operator
sorted_dict = dict(sorted(dict7, key=operator.itemgetter(1),reverse=True))

print(sorted_dict)

# 数字类型



