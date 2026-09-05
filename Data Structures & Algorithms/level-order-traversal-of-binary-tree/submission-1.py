# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque() # queue
        q.append(root) # adding root to queue

        while q:
            qLen = len(q)                   # length of queue
            level = []                      # sub level array within array
            for i in range(qLen):           # everything withing the length of the qLen is in the same level 
                node = q.popleft()          # take the left most node
                if node:
                    level.append(node.val)  # add to current level
                    q.append(node.left)     # add next level to the queue
                    q.append(node.right)
            if level:                       # dont add an empty array useless
                res.append(level)           # add the level array to the entire array

        return res
