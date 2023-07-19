#1. 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)
                count += 1
print("there are total {} times".format(count))               

#
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
print("the duplicated number is :", s1&s2)

#find the maximum value
def two( x, y ):
    if x > y:
        return x
    return y
def three( x, y, z ):
    return two( x, two( y, z ) )
print(three(3, 6, -5))

#add all the numbers in a list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((1,2,3,4,5,-6)))

# multiply all the numbers in a list
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((1,2,3,4,5,-6)))

#check whether a number falls within a given range.
def num(n):
    if n in range(3,9):
        print( "{} is in the range".format(n))
    else :
        print("{} is outside the given range.".format(n))
num(5)
num(14)

#Write a Python function that accepts a string and counts the number of upper and lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')



#problem set1 A
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))

r = 0.04
portion_down_payment = 0.25*total_cost
current_savings  = 0.0
monthly_salary = annual_salary/12

num_of_month = 0
while (current_savings<portion_down_payment):
    current_savings = current_savings + monthly_salary*portion_saved + current_savings*r/12
    num_of_month += 1

print('Number of months:%d' %(num_of_month))

#problem set1 B:
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))

r = 0.04
portion_down_payment = 0.25*total_cost
current_savings  = 0.0
monthly_salary = annual_salary/12

num_of_month = 0
while (current_savings<portion_down_payment):
    if ((num_of_month != 0)and(num_of_month%6 == 0)):
        annual_salary = annual_salary*(1+semi_annual_raise)
        monthly_salary = annual_salary/12
    current_savings = current_savings + monthly_salary*portion_saved + current_savings*r/12
    num_of_month += 1

print('Number of months:%d' %(num_of_month))

