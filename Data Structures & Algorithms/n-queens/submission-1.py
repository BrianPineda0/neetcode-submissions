class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        tracker = set()
        diag = set()
        antiDiag = set()
        

        def dfs(i, curr):
            if len(curr) == n:
                res.append(curr.copy())
                return

            j = 0
            while (j < n):
                if j in tracker or (i - j) in diag or (i + j) in antiDiag:
                    j += 1
                    continue
                curr.append((i,j))
                tracker.add(j)
                diag.add(i-j)
                antiDiag.add(i+j)

                dfs(i+1, curr)

                curr.pop()
                tracker.discard(j)
                diag.discard(i-j)
                antiDiag.discard(i+j)

                

                j += 1


        dfs(0, [])

        ans = []

        for lst in res:
            newList = []
            for i, j in lst:
                string = n * "."
                newList.append(string[:j] + "Q" + string[j+1:])

            ans.append(newList)

        return ans