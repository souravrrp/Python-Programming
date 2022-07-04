# Check the number palindrome or not

n = int(input("Enter the number: "))
temp = n
rev = 0
while(n > 0):
    mod = n % 10
    rev = rev*10+mod
    n = n//10
if (temp == rev):
    print("Yes")
else:
    print("No")
