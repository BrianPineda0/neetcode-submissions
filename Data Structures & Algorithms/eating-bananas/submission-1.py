class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1

        while lo != hi:
            mid = (hi + lo)//2
            

            hours = sum((p + mid - 1)//mid for p in piles)

            if hours > h:
                lo = mid+1
            elif hours <= h:
                hi = mid

        return lo