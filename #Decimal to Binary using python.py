#Decimal to Binary using python

def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num%2,end='')

number=int(input("Enter the number: "))

dectobin(number)