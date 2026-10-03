class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i, totalSum):

            if target == totalSum:
                res.append(subset.copy())
                return
            if i >= len(candidates) or totalSum > target:
                return

            subset.append(candidates[i])
            dfs(i+1, totalSum + candidates[i])

            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, totalSum)

        candidates.sort()
        dfs(0,0)
        return res
            