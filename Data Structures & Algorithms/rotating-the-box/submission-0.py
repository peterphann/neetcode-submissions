class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [list("*" * m)] * n

        for row in boxGrid:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j] = '.'
                    row[empty] = '#'
                    empty -= 1
        
        res = []
        for j in range(n):
            curr = []
            for i in range(m - 1, -1, -1):
                curr.append(boxGrid[i][j])
            res.append(curr)
        return res

                