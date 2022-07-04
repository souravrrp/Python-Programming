nums = [0,1,0,3,12]
"""
length = len(nums)
i,j = 0,0
while(i < length):
    if nums[j] == 0:
        del nums[j]
        nums.append(0)
        i += 1
        continue
    j += 1
    i += 1
print(nums)
"""
ptrs = [i for i, value in enumerate(nums) if value != 0]
print(len(ptrs))
for i, j in enumerate(ptrs):
    nums[i] = nums[j]
for i in range(len(ptrs), len(nums)):
    nums[i] = 0
print(nums)