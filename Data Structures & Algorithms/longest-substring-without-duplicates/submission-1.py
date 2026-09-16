class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currMax = 0
        chars = set()

        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            currMax = max(currMax, r - l + 1)
        return currMax