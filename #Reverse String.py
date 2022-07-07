#Reverse String
str = "-123"
alpha = ""
nmb = ""
num = ""
special = ""
for i in range(len(str)):
    if (str[i].isdigit()):
        num = num+ str[i]
        
    elif((str[i] >= 'A' and str[i] <= 'Z') or
            (str[i] >= 'a' and str[i] <= 'z')):
        alpha += str[i]
    else:
        special += str[i]
nmb = num[::-1]
print(alpha)
print(num )
print(special+nmb)