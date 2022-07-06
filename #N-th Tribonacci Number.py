#N-th Tribonacci Number
n = 3
a=0
b=1
c=1
d=0
i=3
if n==0:
    print(a)
elif n==1:
    print(b)
elif n==2:
    print(c)
else:
    for i in range(n-2):
        d=a+b+c
        a=b
        b=c
        c=d
print(d)
