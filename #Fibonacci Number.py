#Fibonacci Number
n = 6
a=0
b=1
if n==0 and n==1:
    print(0)
else:
    for i in range(n-1):
        c=a+b
        a=b
        b=c
print(c)