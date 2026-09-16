class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        a, b = 1, 0 if s[0] == "0" else 1
        for i in range(1, n):
            c = 0
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) <= 26:
                c += a
            if s[i] != "0":
                c += b
            a, b = b, c
        return b