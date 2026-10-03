class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i, targetSum):
            
            if targetSum > target or i >= len(nums):
                return
            if targetSum == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i, targetSum+nums[i])

            subset.pop()
            dfs(i+1, targetSum)

        dfs(0, 0)
        return res