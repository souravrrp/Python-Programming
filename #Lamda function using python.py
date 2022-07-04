#Lamda function using python 

def myfunc(n):
    return lambda a : a + n
my_ret = myfunc(3)

x=my_ret(3)
print(x)

