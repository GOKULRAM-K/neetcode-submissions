class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = []
        for i in range(len(position)):
            t = (target-position[i]) / speed[i]
            l.append((position[i], t))
        l.sort(reverse=True)

        prev_time = 0
        fleets = 0
        for car, time in l:
            if time > prev_time:
                prev_time = time
                fleets += 1
        return fleets




