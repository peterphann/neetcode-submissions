class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            curr = i + 1
            while dp[curr] != 0 and temperatures[curr] <= temperatures[i]:
                curr += dp[curr]
            
            if temperatures[curr] > temperatures[i]:
                dp[i] = curr - i
        
        return dp