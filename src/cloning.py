#cloning
colour = ['blue','green','red']
new_color = colour[:]
new_color.append('black')
print("new color is: ", new_color)
print('colour is', colour)

#nested list
warm = ['yellow','orange']
hot = ['red']
new_colors = [warm]
new_colors.append(hot)
print(new_colors)
hot.append("blue")
print(hot)
print(new_colors)

#alias
a = 1
b = a 
print(a)
print(b)

warm = ['red','yellow','orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)