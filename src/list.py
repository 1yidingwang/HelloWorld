L1 = [1,2,3,4]
L1.extend([0,6])
print(L1)
L1.append(5)
print(L1)
L1.append([2,3,4])
print(L1)
del L1[1:3]
print(L1)
L1.remove(5)
print(L1)
L1.pop()
print(L1)

#replacement
food = ["pizza", 'noodle','hambuger', 'rice']
print(food)
food[0] = 'hot dog'
print('the element is: ', food[0])

#2d list
food = ['ham','noo','rice']
drink = ['tea','juice','coffee']
animal = ['mon','cat','dog']

total = [food + drink + animal]
print("the element is: ", total[0][1]) 
