class MinStack:

    def __init__(self):
        self.stack = [] # [1, 2, 0]
        self.min_stack = [] # [1, 2, 0]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = None
        if self.stack:
            val = self.stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return -1 if not self.min_stack else self.min_stack[-1]
        
