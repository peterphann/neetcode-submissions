class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 0 if s[0] == "0" else 1

        for i in range(1, n):
            if s[i - 1] != "0" and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2] if i > 1 else 1
            if s[i] != "0":
                dp[i] += dp[i - 1]
        
        return dp[-1]