#Map function using python

def myfunction(a):
    return len(a)

x=map(myfunction,('Sourav','Paul','Singer','Bangladesh','Limited'))

print(x)

print(list(x))