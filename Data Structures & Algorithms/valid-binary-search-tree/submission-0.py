# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_order = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            in_order.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        for i in range(len(in_order) - 1):
            if in_order[i] >= in_order[i + 1]:
                return False
        return True
        