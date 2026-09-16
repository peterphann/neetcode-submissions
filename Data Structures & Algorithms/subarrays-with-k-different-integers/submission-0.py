class Solution:

    def atMostK(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        counts = defaultdict(int)

        for r in range(len(nums)):
            counts[nums[r]] += 1

            while len(counts) > k:
                counts[nums[l]] -= 1
                if counts[nums[l]] == 0:
                    del counts[nums[l]]
                l += 1
            
            res += (r - l + 1)

        return res
            

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)