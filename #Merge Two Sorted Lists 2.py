#Merge Two Sorted Lists 2
listone = [1, 2, 3]
listtwo = [4, 5, 6]

newlist = listone + listtwo
print(newlist)

# 2nd easiest method
newlist = listone.copy()
newlist.extend(listtwo)
print(newlist)