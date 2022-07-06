#Climbing Stairs
n = 5
steps=[1,2]
a=1
b=2
c=0
for i in range(n):
    c=a+b
    a=b
    b=c
    steps.append(c)
print(steps)
if n==0:
    print(0)
else:
    print(steps[n-1])