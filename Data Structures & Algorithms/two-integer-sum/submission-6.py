class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashtable = {}

        for i, num in enumerate(nums):
            hashtable[num] = i

        for i, num in enumerate(nums):
            result = target - num

            if result not in hashtable:
                continue
            elif hashtable[result] == i:
                continue
            else:
                return [i, hashtable[result]]