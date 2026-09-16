from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        # f(i) = max(nums[i] + f(i+2), f(i+1))

        dp = [0] * (len(nums) + 2)
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0] 
        