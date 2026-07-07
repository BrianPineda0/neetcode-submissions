class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix)*len(matrix[0])-1

        while hi >= lo:
            mid = (hi + lo) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                lo = mid + 1
            elif target < matrix[row][col]:
                hi = mid - 1
        
        return False