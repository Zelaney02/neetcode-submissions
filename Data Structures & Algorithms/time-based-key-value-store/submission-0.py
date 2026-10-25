class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, []).append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        values = self.data[key]
        low = 0
        high = len(values) - 1
        result = "" # at this point still possible to have null result if timestamp < all values

        while low <= high:
            mid = (low + high) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1] # keep solution but keep looking
                low = mid + 1
            else:
                high = mid - 1
        return result

