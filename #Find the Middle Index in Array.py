#Find the Middle Index in Array
nums = [2,3,-1,8,4]
start=0
end=sum(nums)
#print(end)
for i in range(len(nums)):
    end-=nums[i]
    if start==end:
        print(i)
    start+=nums[i]
print(-1)