class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minDist = []

        result = []

        for coords in points:
            x, y = coords
            heapq.heappush(minDist, (-math.sqrt(x**2 + y**2), coords))

            while len(minDist) > k:
                heapq.heappop(minDist)

        while k > 0:

            filler, coords = heapq.heappop(minDist)

            result.append(coords)

            k -= 1

        return result
    



        