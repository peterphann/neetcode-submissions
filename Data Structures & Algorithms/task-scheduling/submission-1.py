class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        heap = []
        queue = deque()

        for task, count in Counter(tasks).items():
            heapq.heappush(heap, (-count, task))
        
        while heap or queue:
            cycles += 1

            while queue and cycles - queue[0][0] - 1 >= n:
                _, count, task = queue.popleft()
                heapq.heappush(heap, (-count, task))

            if heap:
                negCount, task = heapq.heappop(heap)
                negCount += 1
                if negCount < 0:
                    queue.append((cycles, -negCount, task))

        return cycles
