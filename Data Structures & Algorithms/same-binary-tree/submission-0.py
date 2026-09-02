# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        flag = True

        def dfs(p, q):

            nonlocal flag

            if not p and not q:
                return flag
            elif not (p and q): 
                flag = False
                return flag

            if p.val != q.val:
                flag = False
                return flag

            flag1 = dfs(p.left, q.left)
            flag2 = dfs(p.right, q.right)

            if flag1 != flag2: return False

            return flag

        flag = dfs(p,q)

        return flag

