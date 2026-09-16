class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest = 0
        res = None

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                length = (j - i) + 1
                dp[i][j] = (
                    s[i] == s[j] and
                    (length <= 3 or dp[i + 1][j - 1])
                )
                
                if dp[i][j] and length > longest:
                    longest = length
                    res = s[i:j+1]

        return res