class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        count = [-x for x in count.values()]

        heapq.heapify(count)

        time = 0

        q = deque()

        while count or q:
            time +=1

            if count:
                cnt = heapq.heappop(count) + 1
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(count, q.popleft()[0])

        return time