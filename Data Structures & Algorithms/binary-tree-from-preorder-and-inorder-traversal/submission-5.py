# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        idx = {v: i for i, v in enumerate(inorder)}
        self.pre = 0

        def build(left, right):        # bounds in inorder
            if left > right:
                return None
            val = preorder[self.pre]
            self.pre += 1
            node = TreeNode(val)
            mid = idx[val]
            node.left  = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(inorder) - 1)