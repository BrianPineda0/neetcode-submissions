class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1

        most = 0

        while i < j:
            height = min(heights[i], heights[j])
            length = j-i

            most = max(most, height*length)

            if max(heights[i], heights[j]) == heights[i]:
                j -= 1
            elif max(heights[i], heights[j]) == heights[j]:
                i += 1

        return most