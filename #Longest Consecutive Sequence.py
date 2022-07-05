#Longest Consecutive Sequence
nums = [100,4,200,1,3,2]
if not nums:
    print(0)
nums.sort()
print(nums)
ml = 0
tl = 1
#print(len(nums) - 1)
for i in range(len(nums) - 1):
    d = nums[i + 1] - nums[i]
    #print(i)
    print(d)
    if d == 0:
        continue
    elif d == 1:
        tl += 1
    else:
        ml = max(ml, tl)
        tl = 1
print(max(ml, tl))