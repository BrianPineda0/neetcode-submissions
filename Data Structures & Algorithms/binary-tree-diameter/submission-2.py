# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 0
        
        def dfs(curr):

            if not curr: return 0

            l = dfs(curr.left)
            r = dfs(curr.right)

            nonlocal result

            result = max(result, l+r)

            return 1 + max(l,r)

        dfs(root)

        return result