# kwargs inlcudes : 
#   1
#   2

def f(**kwargs):
    for key, value in kwargs.items():
        value +=1 
        print(value)

if __name__ == "__main__" :

    f(price=1,inflation=1)