#Merge Two Sorted Lists
list1 = [1,2,4]
list2 = [1,3,4]
#list1 = []
#list2 = []
#list1 = []
#list2 = [0]

"""
list3=list1+list2
list3.sort()
print(list3)

list3=list1.append(list2)
print(list3)
"""


if not list1:
    print(list2)
elif not list2:
    print(list1)
else:
    if list1.val <= list2.val:
        merged_list = ListNode(val=list1.val)
        merged_list.next = self.mergeTwoLists(list1.next, list2)
    else:
        merged_list = ListNode(val=list2.val)
        merged_list.next = self.mergeTwoLists(list1, list2.next)
    
return merged_list