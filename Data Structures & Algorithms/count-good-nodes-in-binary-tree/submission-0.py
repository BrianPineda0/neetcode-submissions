# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def dfs(curr, num):

            nonlocal count
            
            if not curr: return None

            if not num:
                num = curr.val
                count +=1
            elif curr.val >= num:
                count += 1
                num = curr.val
                
            dfs(curr.left, num)
            dfs(curr.right, num)

            return None

        dfs(root, None)

        return count