# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        targetNodes = []

        if not root and not subRoot: return True

        def findSubRoot(root):
            if not root:
                return None
            
            left = findSubRoot(root.left)
            right = findSubRoot(root.right)

            if root.val == subRoot.val:
                nonlocal targetNodes
                targetNodes.append(root)
                return root

            if left: return left
            return right


        def isSameTree(p, q):
            if not p and not q:
                return True

            elif not (p and q): 
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        blah = findSubRoot(root)

        for node in targetNodes:

            if isSameTree(node, subRoot):
                return True

        return False

