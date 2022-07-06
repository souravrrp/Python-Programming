from http.client import FOUND


#s = "abc"
#t = "ahbgdc"

s="axc"
t="ahbgdc"
"""
try:
    fullstring.index(substring)
except ValueError:
    print("Not found!")
else:
    print("Found!")
"""

"""
for i,c in enumerate(s):
    f = t.find(c)
    print(t,c,f)
    if f > -1:
        t = t[f+1:]
        #print(t)
        print(f)
    else:
        print("Not Found")
print("Found")
"""

"""
left = 0
for char in list(s):
    try: 
        left = t.index(char, left) + 1
        print(left)
    except: 
        print("Not Found")
print("Found")
"""

for char in list(s):
    if t.index(char) is not None:
        f=+1
    else:
        nf=+1
if nf is not None:
    print("Not Found")
else:
    print("Found")