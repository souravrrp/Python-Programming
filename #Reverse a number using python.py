#Reverse a number using python

n=int(input("Enter a number: "))
rev=0
while(n>0):
    mod=n%10
    rev=rev*10+mod
    n=n//10

print("Reverse of the number is ",rev)