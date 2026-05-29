class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []

        self.d[key].append((timestamp, value))       

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.d:
            return ""

        arr = self.d[key]

        b = 0
        e = len(arr) - 1

        ans = ""

        while b <= e:

            mid = (b + e) // 2

            if arr[mid][0] <= timestamp:

                ans = arr[mid][1]

                b = mid + 1

            else:

                e = mid - 1

        return ans