class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def numBits(n: int) -> int:
            res = 0
            while n:
                if n & 1:
                    res += 1
                n >>= 1
            return res

        out = []
        for i in range(n + 1):
            out.append(numBits(i))
        return out