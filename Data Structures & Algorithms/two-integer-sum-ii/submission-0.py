class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashtable = {}

        for i, num in enumerate(numbers):
            hashtable[num] = i

        for i, num in enumerate(numbers):
            result = target - num

            if result not in hashtable:
                continue
            elif hashtable[result] == i:
                continue
            else:
                return [i+1, hashtable[result]+1]