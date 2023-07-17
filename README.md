#### create a conda python environment for search practice

```shell
conda create -n search_trial python=3.11 -y
```

#### activate such python environment

```shell
conda activate search_trial
```

#### set up git (code version tracking)
```shell
git init
```

#### set up your git account
```shell
git config --global user.name "yiding"
git config --global user.email "1yidingwang@gmail.com"
```

#### add all files in the folder to code tracking
```shell
git add .
```

#### install the corresponding packages

```shell
pip install -r requirements.txt
```
#### Decomposition 
```shell
把一个大步骤分解成一个小的步骤，每一个小步骤里面也会有相应的步骤
例如：把大象放进冰箱需要分成三步（大步骤）：
    1. 把冰箱打开
    2. 把大象放进去
    3. 把冰箱关上
每一个大步骤的小步骤：
    把冰箱打开：
        1. 用手握住冰箱把手
        2. 打开冰箱门
    把大象放进去：
        1. 拿起大象
        2. 把大象放进去
    把冰箱关上：
        1. 把手放在冰箱上
        2. 把门关上
分解成每一个小步骤，这就是decomposition
```

####  What  is abstraction:
```shell
隐藏不必要的信息来处理具有复杂性的过程
有些东西我只需要知道怎么运行就好，不需要知道运行的原理是什么
```

#### Whay is function
```shell
def + name + (parameters可以不写，也可以写很多个):
    code
    return(可以有return，也可以没有，没有就会print none)
```

#### Adcantages and disadvantages of writng function
```shell
ad: 如果在这个function我每次都需要重新写一次在main function里面，我
就可以把它放在function里面，每次需要的时候引用特定的function即可，不需要
重新再写一次
disad：如果写在function里面的东西太多，function内存不够，跑不过来，可能
会导致系统崩溃，直接黑屏。
```

#### Global scope & Variable scope
```shell
variable scope： 简单理解为在function里面的定义为variable scope
Global scope: 写在file全局的定义为global scope
```

#### 与tuple相似的四种类型
```shell
 tuple
 list 
 set
 dictionary
```

#### What is tuple (元组)
```shell
Tuple 是基本数据结构之一，元组中元素不允许被修改，因此元组也被称作只读列表
元组使用小括号 "()" 包裹，元素之间使用逗号 “," 分隔。
元组中的元素可以是字符串、数字等数据, 能够储存数据
特点：
    1. tuple元素不能被修改
    2. 不同的tuple可以被整合，相加
    3. 元素不能被删除，但是可以删掉整个tuple
优点：
    1. 由于不可变的特性，不必担心会在code的过程中失误改变值的大小或名称
    2. 性能快：能更快的创建，需要的空间更小
    3. 可以作为dictionary的key，因为key不能被改变
    4. 可以很快的交换数值
缺点：
    1. 不能灵活的改变元素
```
#### 11/07/2023 总结
```shell
tuple is immutable, list is mutable 
list 和 array 在广义上没有任何区别
tuple就是没有key的dictionary
tuple的空间少因为他的function很少，只有tuple.index and tuple.count
list的空间多，因为list.后面的function很多，有count，reserve, insert等
“__定义__"是一个默认变量
计算内存空间：
>>> a = (1,2,3)
>>> a.__sizeof__() <-加括号的原因是因为这是一个function
48
```

#### List
```shell
储存data，用[]书写，元素用逗号分隔。
list.extend可以加多个元素
list.append只能加一个元素
删除元素用del或者list.remove()
del list[]删除索引目标
list.remove删除指定元素
list.pop删除最右面的元素
list.insert(位置，想添加的元素)
list.sort()按照字母顺序或大小排序
list.clear()清除所有element
```
#### 2D List
```shell
有多个list，把他们放在同一个variable里面
第一个index是list，第二个index是list里面的element
比如：
    food = ['ham','noo','rice']
    drink = ['tea','juice','coffee']
    animal = ['mon','cat','dog']
    
    total = [food + drink + animal]
    print(total[0][1]) -> 打印‘noo’
```

#### What is set
```shell
set可以储存data，用大括号{}书写，用逗号，分隔
特点：
1. 不一定会按照顺序书写，意味着元素在索引中是单独储存的
#我理解的是每一个元素都是单独的个体，不像是list一样把所有元素捆绑到一起
2. 里面不能拥有同样的元素，即使有也只会打印一次
3. 跟list一样有很多的method，set.后面
优点：
1. 因为不会有相同的element，所以能够有效的在一组数据中删除重复元素
2. 能够更有效的实现membership test
#membership test就是测试这个set里面有没有我想要的element
#最终结果显示true/false
缺点：
1. 因为是无序的，所以不能被index，只能用pointer
2. set的时间复杂度是logN
```

#### clone and alias的区别：
```shell
clone：create一个新的object跟原来的object value一样
克隆的结果是产生两个值一样，但却有不同标识符的列表。修改a列表的值，b列表不收到影响
alias: 将一个变量赋值给另一个变量，那么这两个变量指向同一个对象。
修改任何一个列表的元素，另一个列表做相同的改变
```

#### what is recursion:
```shell
Recursion is the process of repeating items in a self-similar way.
定义：
Recursion is defined as a process which calls itself directly or indirectly
and the corresponding function is called a recursive function.

特点：
1. 递归是一种解决问题的方法，它把一个问题分解为越来越小的子问题，直到问题的规模小到可
以被很简单直接解决。通常为了达到分解问题的效果，递归过程中要引入一个调用自身的函数。
2. 递归函数必须具有基本情况或停止标准，以避免无限递归。
3. 在内存和性能方面，递归函数可能不如迭代(iteration)解决方案有效

四种类型的recursion：
1. Tail recursion,  
2. Head recursion,  
3. Tree recursion and 
4. Nested recursion.

三大定律：
1. A recursive algorithm must call itself, recursively.
2. A recursive algorithm must have a base case.
3. A recursive algorithm must change its state and move toward the base case.
```
#### Advantages and Disadvantages of Recursion:
```shell
1. Recursion can simplify complex problems by breaking them down into smaller,
more manageable pieces.
2. Recursive code can be more readable and easier to understand 
than iterative code.
3. Recursion is essential for some algorithms and data structures.
Also with recursion, we can reduce the length of code and become 
more readable and understandable to the user/ programmer.

Disadvantages of Recursion:
1. Recursion can be less efficient than iterative solutions in terms of 
memory and performance.
2. Recursive functions can be more challenging to debug and 
understand than iterative solutions.
3. Recursion can lead to stack overflow errors if the 
recursion depth is too high.
```

#### Iteration:
```shell
迭代(iteration)意味着一遍又一遍地执行相同的代码块，可能会执行很多次。
实现迭代的编程结构称为循环。

在编程中，有两种类型的迭代，不定迭代和定迭代：
1. 对于不定迭代(indefinite iteration)，循环执行的次数不会提前明确指定。
相反，只要满足某些条件，就会重复执行指定的块。
2. 对于有限迭代(definite iteration)，指定块将被执行的次数在循环开始时明确指定。
```

#### Difference between iteration and recursion:
```shell
recursion: 由于指定基本条件时出现错误，可能会出现无限递归调用，而基本条件永远不会变为假，
不断调用该函数，这可能会导致系统CPU崩溃。
iteration: 当内存耗尽时，它会停止
                recursion                   iteration
定义            函数调用自身                 重复的执行代码
时间复杂度      很高，一般都是指数              相对来说较低
stop           通过base case            当condition不再被满足时       
speed      慢，因为要update stack       比recursion快，因为不需要utilize the stack
```
#### Tail recursion and non tail recursion
```shell
tail recursion: the recursive call is the last thing done bu the function.
there is no need to keep recoed of the previous state. 
尾递归调用仅涉及一次递归调用，然后立即返回结果，无需进一步处理或计算。

```

#### Object oriented programming (OOP):
```shell
1.	万物皆对象
    1）	可以是具体物体：
        A．	拥有属性：姓名，年龄，身高，体重等
        B．	拥有行为：吃饭，喝水，走路，睡觉等
        C．	把很多零散的东西，组装成一个整体
    2）	python是一门面向对象编程（oop）的语言：
        A．	基本数据类型：int，float，Boolean
        B．	对象类型：string，dictionary
        C．	Python把所有的类型都归类为object

2.	面向过程 & 面向对象 （都是解决问题的思路）：
    1）	面向过程：在解决问题的时候，关注的是解决问题的每一个步骤。
        也就是说我去做这些事情。（施工者）
    2）	面向对象：找解决问题的对象，让对象帮我完成任务。不需要我去完成，
        我只需要找人完成就可以。对象也可以找下一个对象,更清晰（包工头）

3.	面向过程 vs 面向对象
    1）	面向对象就是面向过程的封装。因为步骤是不变的，我还是需要完成所有的步骤，但是我可以把步骤分配给不同的对象。这样的话我可以只面向几个对象就可以完成任务
    2）	面向过程最重要的是划分步骤，把一个任务分解成具体的每一步骤
    3）	面向对象最重要的是划分对象，思考应该把那些步骤分配到哪些对象里面去。确定对象的行为和属性

Class（类） & object（对象）：
    1.	定义：某一个具体对象特征的抽象运用。将数据和功能捆绑在一起的方法。用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    2.	作用：根据类的属性和方法，产生具体的对象。对象的特性都不相同
    3.	一开始的类都是抽象的概念，不具备具体的值
    4.	等建立object的时候才具有具体的属性和行为
    5.	经典类，新式类

#对应类名应该要首字母大写

```