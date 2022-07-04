print("Enter two numbers")
num1=int(input())
n1=num1
num2=int(input())
n2=num2
while(num1!=num2):
    if num1>num2:
        num1-=num2
    else:
        num2-=num1
print("HCF/GCD of two number: ",num1)
print("LCM of two number: ",int((n1*n2)/num1))