class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = []
        counts = Counter(nums)

        for num, count in counts.items():
            groups.append((-count, num,))
        groups.sort()

        res = []
        for _, num in groups:
            res.append(num)
            if len(res) == k:
                return res
        return []
