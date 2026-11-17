# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            count = (node is p) + (node is q)

            right = dfs(node.right)
            left = dfs(node.left)

            count += (right + left)

            if count == 2 and ans is None:
                ans = node

            return count

        dfs(root)
        return ans

