#Prime number between interval
print("Please enter the first number: ")
f=int(input())
print("Please enter the last number: ")
l=int(input())
while(f<l):
    for i in range(2, (int(f/2)+1)):
        if f%i==0:
            print(f," is not prime number.")
            print("False")
            break
        else:
            print(f," is prime number")
            print("True")
            break