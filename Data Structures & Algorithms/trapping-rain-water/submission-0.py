class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        i, j = 0, len(height)-1
        leftMax, rightMax = height[i], height[j]
        answer = 0

        while i < j:
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                answer += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                answer += rightMax - height[j]

        return answer