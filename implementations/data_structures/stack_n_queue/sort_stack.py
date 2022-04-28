from random import randint


class MyStack:
    def __init__(self):
        self.memo = []

    def push(self, value):
        self.memo.append(value)

    def pop(self):
        return self.pop()

    def peek(self):
        return self.memo[-1]

    def print(self):
        print(self.memo)


def sort_stack(st):
    helper = []
    
    while len(st.memo) != 0:
        value = st.pop()
        while len(helper) != 0 and value < helper[-1]:
            st.push(helper.pop())
        helper.append(value)
    
    while len(helper) != 0:
        st.push(helper.pop())

s = MyStack()
for i in range(20):
    s.push(randint(0, 50))
