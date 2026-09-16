class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        # given i and j, how do i know s[i:j] is a palindrome?
        # => if s[i] == s[j] and s[i+1:j-1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                length = j - i + 1
                dp[i][j] = (
                    s[i] == s[j]
                    and (length <= 3 or dp[i + 1][j - 1])
                )

                if dp[i][j]:
                    res += 1
        
        return res

