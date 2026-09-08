# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        self.res = " "

        def dfs(root):

            if not root:
                return "N,"
            
            self.res += str(root.val)+","

            if not root.left:
                self.res += "N,"
            else:
                dfs(root.left)

            if not root.right:
                self.res += "N,"
            else:
                dfs(root.right)


        dfs(root)


        return self.res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.counter = 0

        self.array = data.split(",")

        if data == " " or data == "N" or not data:
            return

        def dfs():

            nodeVal = self.array[self.counter]
            self.counter += 1

            if nodeVal == "N":
                return

            root = TreeNode(int(nodeVal))


            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()

        



        

