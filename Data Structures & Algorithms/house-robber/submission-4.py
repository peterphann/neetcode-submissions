from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        a, b = 0, 0
        for i in range(len(nums) -1, -1, -1):
            a, b = max(nums[i] + b, a), a
        return a
