# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calcDepth(node):
            if not node:
                return 0
            if not node.left:
                return calcDepth(node.right) + 1
            if not node.right:
                return calcDepth(node.left) + 1
            return max(calcDepth(node.left) + 1, calcDepth(node.right) + 1)
        return calcDepth(root)