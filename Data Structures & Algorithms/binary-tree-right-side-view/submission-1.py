# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        out = []

        while q:
            rightmost = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightmost:
                out.append(rightmost.val)

        return out
