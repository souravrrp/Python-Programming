#Palindrome number
from audioop import reverse


str="WOW"
print(str)

rev=''.join(reversed(str))
print(rev)
if str==rev:
    print("Palindrome")
else:
    print("Not Palindrome")