class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = float("-inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.smallest = val

        else:
            self.stack.append(val - self.smallest)
            self.smallest = min(self.smallest, val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.smallest = self.smallest - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.smallest
        else:
            return self.smallest

    def getMin(self) -> int:
        return self.smallest
