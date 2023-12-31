cube = 1000
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guess = 0

while (abs(guess ** 3 - cube) >= epsilon) and (guess < cube):

    guess += increment
    num_guess += 1

print("num_guess = ", num_guess)

if abs(guess ** 3 - cube ) >= epsilon:

    print('Failed on cube root of ', cube)

else:

    print(guess, "is close to the cube root of ", cube)
