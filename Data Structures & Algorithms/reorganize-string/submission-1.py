class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        counts = Counter(s)

        for letter, count in counts.items():
            heapq.heappush(heap, (-count, letter,))
        
        res = ""
        prev = None
        while heap:
            count, letter = heapq.heappop(heap)
            res += letter

            if prev:
                heapq.heappush(heap, prev)
            prev = (count + 1, letter) if -count > 1 else None
        
        return res if len(res) == len(s) else ""