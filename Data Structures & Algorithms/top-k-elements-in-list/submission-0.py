class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        answer = {}

        for digit in nums:
            answer[digit] = answer.get(digit, 0) + 1

        answer_desc = sorted(answer, key=answer.get, reverse=True)
        
        top_k = answer_desc[:k]

        return top_k