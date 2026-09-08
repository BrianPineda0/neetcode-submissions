# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.best = float("-inf")

        def dfs(root):

            if not root:
                return 0

            leftTree = max(dfs(root.left), 0) # 10

            rightTree = max(dfs(root.right), 0) # 40

            chainVal = root.val + leftTree + rightTree  # -15 + 10 + 40 = 35

            self.best = max(self.best, chainVal)  # ADD: track the answer

            return root.val + max(leftTree, rightTree)  # CHANGE: return chain (job B)

        dfs(root)
        return self.best
