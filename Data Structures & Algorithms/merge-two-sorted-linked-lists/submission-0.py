# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = out = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                out.next = list1
                list1 = list1.next
            else:
                out.next = list2
                list2 = list2.next
            out = out.next
        
        out.next = list1 or list2
        
        return res.next