class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter = [0] * 26
        target = [0] * 26
        convert = lambda letter: ord(letter) - ord('a')

        for letter in s1:
            target[convert(letter)] += 1

        for r in range(n - 1, len(s2)):
            l = r - n + 1
            substring = s2[l:r + 1]

            if l == 0:
                for letter in substring:
                    counter[convert(letter)] += 1
            else:
                counter[convert(s2[l - 1])] -= 1
                counter[convert(s2[r])] += 1
            
            if counter == target:
                return True

        return False


