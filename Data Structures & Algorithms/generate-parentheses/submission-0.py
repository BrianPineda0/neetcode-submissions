class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, curr):
            if len(curr) == n*2:
                res.append("".join(curr))
                return

            if openP < n:
                curr.append("(")
                dfs(openP + 1, closeP, curr)
                curr.pop()

            if closeP < openP:
                curr.append(")")
                dfs(openP, closeP + 1, curr)
                curr.pop()
            
        dfs(0 , 0 ,[])
        return res
