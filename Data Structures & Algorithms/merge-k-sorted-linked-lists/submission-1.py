# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
                node = node.next

        res = ListNode(0)
        curr = res
        while h:
            val, i, node = heapq.heappop(h)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        return res.next