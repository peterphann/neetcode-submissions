from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache()
        def dfs(i):
            if i >= len(nums):
                return 0
            
            return max(
                nums[i] + dfs(i + 2),
                nums[i] + dfs(i + 3)
            )
        
        return max(
            dfs(0),
            dfs(1)
        )