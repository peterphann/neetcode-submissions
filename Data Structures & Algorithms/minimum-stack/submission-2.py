class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = float('inf')

    def push(self, val: int) -> None:
        self.currMin = min(val, self.currMin)
        self.stack.append((val, self.currMin,))

    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            self.currMin = self.stack[-1][1]
        else:
            self.currMin = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.currMin
