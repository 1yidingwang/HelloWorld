class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

class Person:
		pass
#根据类创建一个对象：
p = Person()
#给p增加对象：
p.age = 18
p.height = 180

print(p.age)
print(p.height)
print(p.__dict__) #打印所有值
del p.age

class Animal:
	def __init___(self, types, ages, cuteness):
		self.types = types
		self.ages = ages
		self.cuteness = cuteness
animal1 = Animal("jinmao", 18, 10)
print(animal1.ages)
