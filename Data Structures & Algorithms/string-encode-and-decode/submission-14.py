class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "/"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []
        while l < len(s):
            while r < len(s) and s[r] != "/":
                r += 1
            length = int(s[l:r])
            res.append(s[r + 1:r + length + 1])
            l, r = r + length + 1, r + length + 1

        return res
        

            
        
