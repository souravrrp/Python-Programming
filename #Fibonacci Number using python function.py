#Fibonacci Number using python function
a=0
b=1
i=1
c=0
if n==0:
    return 0
elif n==1:
    return 1
else:
    for i in range(n-1):
        c=a+b
        a=b
        b=c
return c