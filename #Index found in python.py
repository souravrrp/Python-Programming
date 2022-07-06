#Index found in python
s = "abc"
t = "ahbgdc"
left = 0
for char in list(s):
    left=t.index(char,left)+1
    print(left)