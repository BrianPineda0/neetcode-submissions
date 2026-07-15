class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        answer = ""
        values = self.store.get(key, [])

        hi, lo = len(values)-1, 0

        while hi >= lo:
            mid = (hi+lo)//2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                answer = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return answer
