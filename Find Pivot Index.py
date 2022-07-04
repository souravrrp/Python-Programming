
nums = [1,7,3,6,5,6]
start=0
end=sum(nums)
for i in range(len(nums)):
    end-=nums[i]
    if start==end:
        print(i)
    start+=nums[i]
print(-1)