class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            adjList[prereq].add(course)
            indegrees[course] += 1
        
        res = []
        queue = deque([c for c in range(numCourses) if indegrees[c] == 0])
        
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for nei in adjList[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []

