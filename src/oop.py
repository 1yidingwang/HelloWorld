#encapsulation
class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score
        
bart = Student('Bart Simpson', 59)
print(bart.__name) # 'Student' object has no attribute '__name'
print(bart._Student__name) # Bart Simpson
bart.set_score(88)
print(bart.get_score()) #88



#heritage
class Animal(object):
    __age=1
    def run(self):
        print('Animal is running...')
    
    def set_age(self,age):
        self.__age=age
    
    def get_age(self):
        return self.__age
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
d=Dog()
d.run()
d.set_age(2)
print(d.get_age())
print(d.__age)

def print_again( func ):

    def inner():

        print("Greed is good")

        func()
    
    return inner

def ord():

    print("hello world")

dec = print_again(ord)

