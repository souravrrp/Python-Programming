#Factorial using python


def Factorial(n):
    if n<=1:
        return 1
    else:
        return (n*Factorial(n-1))
n=int(input("Enter the number: "))
print("Factorial of the number is : ",Factorial(n))