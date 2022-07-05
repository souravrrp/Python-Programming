#Two Sum
nums = [3,2,4]
target = 6
s={}
print(s)
for i, n in enumerate(nums):
    if (target-n) in s:
        print(target-n)
        print(s[target-n],i)
    else:
        s[n]=i
        print(s[n])
        #print(s[n])
print(s)
