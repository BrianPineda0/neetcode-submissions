# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        result = None

        def dfs(root):

            nonlocal count
            nonlocal result

            if not root:
                return

            dfs(root.left)
            count +=1

            if k == count:
                result = root.val
                return

            dfs(root.right)

        dfs(root)

        return result

        