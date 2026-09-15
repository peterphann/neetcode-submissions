class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftOf = {')': '(', '}': '{', ']': '['}

        for b in s:
            if b not in leftOf:
                stack.append(b)
            else:
                left = leftOf[b]
                if not stack or stack[-1] != left:
                    return False
                stack.pop()
        return len(stack) == 0
