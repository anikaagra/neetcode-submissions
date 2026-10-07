# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(h, node.val)
                node = node.next

        res = ListNode(0)
        curr = res
        while h:
            curr.next = ListNode(heapq.heappop(h))
            curr = curr.next

        return res.next