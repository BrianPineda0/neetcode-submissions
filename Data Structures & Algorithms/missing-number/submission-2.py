class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        answer = 0

        for i in range(len(nums)+1):
            answer += i

        for num in nums:
            answer -= num

        return answer