print("Enter the number: ")
num=int(input())
for i in range(2, (int(num/2)+1)):
    if num%i==0:
        print(num," is not prime number.")
        print("False")
        break
    else:
        print(num," is prime number")
        print("True")
        break