class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A

        length = len(A) + len(B)

        half = (length + 1) // 2

        hi, lo = len(A), 0

        while hi >= lo:
            mid = (hi + lo)//2
            Bmid = half - mid

            Aleft = A[mid-1] if mid > 0 else float('-inf')
            Bleft = B[Bmid-1] if Bmid > 0 else float('-inf')

            Aright = A[mid] if mid < len(A) else float('inf')
            Bright = B[Bmid] if Bmid < len(B) else float('inf')

            if Aleft <= Bright and Aright >= Bleft:
                if length % 2 == 0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                return max(Aleft,Bleft)
            elif Aleft > Bright:
                hi = mid - 1
            else:
                lo = mid + 1






