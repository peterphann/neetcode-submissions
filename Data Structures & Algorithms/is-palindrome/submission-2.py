class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        accepted = set("abcdefghijklmnopqrstuvwxyz1234567890")
        
        while l < len(s) and s[l].lower() not in accepted:
            l += 1
        while r >= 0 and s[r].lower() not in accepted:
            r -= 1
        
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            while l < len(s) and s[l].lower() not in accepted:
                l += 1
            while r >= 0 and s[r].lower() not in accepted:
                r -= 1
        
        return True
            
