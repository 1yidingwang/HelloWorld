#tail recursion
def dr(x:int):

    if x == 0:
        return 

    print(x)
    dr(x-1)

#head recursion
# def dr(x:int):
#     if x > 0:
#         dr(x-1)
#         print(x)

dr(3)

    





'''
a(n) = f1( b(n) )
b(n) = a(n-1) 

a(n) = f1( f2( f3(  a(n-1) ) ) )
'''