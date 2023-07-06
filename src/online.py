#返回return里面的字符串
def f():
    return 'foo'
s = f()
print(s)

#对return里面的字符串进行切片
def f():
    return 'goodjob'
print(f()[2:4])

#在function里面运算，在外面进行赋值
def add(a,b):
    result = a + b
    return result

value = add(1,2)
print(value)

#在function里面加if statement
def f(x):
    if x < 0:
        return
    if x > 100:
        return
    print(x)

f(-2)
f(188)
f(65)

#无赋值，无字符串，print none
def f():
    print("i'm eating nothing")

print(f())

#global scope and variable scope
a = 12
def func():
    a = 5 
    print("variable scope: ", a)
    return

print(func())
print("Global scope: ", a)


