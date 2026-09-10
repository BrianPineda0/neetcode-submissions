class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        maxFreq = max(count.values())

        tied = list(count.values()).count(maxFreq)

        return max(len(tasks),(maxFreq-1) * (n + 1) + tied)
