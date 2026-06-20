class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashtable = {}

        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            elif hashtable[num] == 1:
                return True
        
        return False