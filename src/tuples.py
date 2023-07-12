#元组的索引和相加
tuple_example1 = ("banana", "apple", 100, 200)
tuple_example2 = ("monkey", "bird", 10, 20)
print(tuple_example1[1])
tumple_total = tuple_example1 + tuple_example2
print(tumple_total)
#元组的嵌套，在元组里面可以再加一个小括号
def_tuple = ("milk", ("organe juice", "tea"))
print(def_tuple[1])

#元组的删除（不能删除某个元素）可以删除整个variable
#del def_tuple[1] 会出现错误
del def_tuple

#将其他类型改为tuple类型
num = [1, 2, 3]
print(tuple(num))
print(num)
result = ("A+")
print(result)
print(tuple(result))

#将string的type变成tuple，在括号最后加一个逗号
word = ("yes")
print(type(word))
word1 = ("yes",)
print(type(word1))

#交换数值
x = input("input x: ")
y = input("input y: ")
print("before swap is: ", x, y)
temp = x
x = y 
y = temp
print("after swap is: ", x, y)

#交换数组
a = input("print a: ")
b = input("print b: ")
(a,b) = (b,a)
print("after swap is: ")
print("(a, b): ", a,b)
print("(b, a): ", b,a)

#return more than one value:
def q_and_r(q, r):
    quote = q // r
    remainder = q % r
    return q, r
(quote, remainder) = q_and_r(4,5)
print("print(quote and remainder: ", quote, remainder)

