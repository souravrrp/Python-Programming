#462. Minimum Moves to Equal Array Elements II
nums = [1,2,3,4]
nums.sort()
n=len(nums)
print(n)
if n%2==1:
	mid=(n//2)
	c=0
	for i in nums:
		print(abs(nums[mid]-i))
        #c+=abs(nums[mid]-i)
	#print(c)
else:
	m=n//2
	mid=(nums[m]+nums[m-1])//2
	c=0
	for i in nums:
		c+=abs(mid-i)
        #print(abs(mid-i))
	print(c)
print(m)
print(mid)