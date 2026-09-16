class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        curr = 0
        events = []

        for p, r in lights:
            events.append((p - r, 1,))
            events.append((p + r + 1, -1,))
        events.sort()

        brightest = 0
        res = 0

        for time, change in events:
            curr += change

            if curr > brightest:
                brightest = curr
                res = time
        return res