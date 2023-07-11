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
