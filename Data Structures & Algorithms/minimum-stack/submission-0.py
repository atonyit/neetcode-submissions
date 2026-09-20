class MinStack:
    # TC: O(1) for all SC: O(2n)
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #We can optimize for less space usage here since currently were always adding
        #the min onto the stack, even if it isn't a new minimum
        if self.minStack:
            current_min = min(val, self.minStack[-1])
        else:
            current_min = val

        self.minStack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
