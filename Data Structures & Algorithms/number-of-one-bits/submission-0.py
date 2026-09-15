class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        for i in range(32):
            if (1 << i) & n:
                num += 1
        return num