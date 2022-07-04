from typing import final


nums = [0,1,0,3,12]
result=[]
last=[]
for i in nums:
    if i==0:
        print(i)
        last=0
        print(last)
    else:
        result=i

print(last.append(result))
