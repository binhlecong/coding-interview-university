class MyQueue:
    def __init__(self) -> None:
        self.isS1 = True
        self.s1 = []
        self.s2 = []

    def push(self, value):
        if self.isS1:
            self.s1.append(value)
        else:
            self.s2.append(value)

    def pop(self):
        if self.isS1:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
            self.isS1 = False
            return self.s2.pop()
        else:
            while len(self.s2) != 0:
                self.s1.append(self.s2.pop())
            self.isS1 = True
            return self.s1.pop()

    def peek(self):
        if self.isS1:
            return self.s1[-1]
        else:
            return self.s2[-1]

    def isEmpty(self):
        return len(self.s1) == 0 and len(self.s2) == 0
