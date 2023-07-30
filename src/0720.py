#Write a while loop that adds all the numbers up to 100 (inclusive).

counter=0
total=0

#Construct your while loop here.
while counter < 100:
    
    counter += 1
    total = total + counter
    
print(total)

#Define a function that accepts 2 values and return its sum, subtraction and multiplication.

def result(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    print(f"Sum is {sum}, Sub is {sub}, & Multiply is {mul}")

a = int(input("Enter value of a: "))  # 7
b = int(input("Enter value of b: "))  # 5
result(a,b)

#Define a function in python that accepts 3 values and returns the maximum of three numbers.
def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum among all")
    elif b > a and b > c:
        print(f"{b} is maximum among all")
    else:
        print(f"{c} is maximum among all")

max(30,22,18)




#Define a function in python that accepts 3 values and returns the maximum of three numbers.
def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
        else:
            con = con + 1

    print("Count of vowels is ",vov)
    print("Count of consonant is ",con)

x = input("Enter Value: ") # pythonlobby
count(x)

#Define a function that accepts radius and returns the area of a circle.
def area(radius):
    area = 3.14*radius*radius
    return area

radius = int(input("Enter Radius: ")) 
print(area(radius))


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)
                count += 1
print("there are total {} times".format(count))               


# Using a while loop, len function, an if statement and the str() function; 
# iterate through the given list and if there is a 100, assign a notification message to the variable my_message with the index of 100.

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

my_message=""

#Type your code here.




print(my_message)

