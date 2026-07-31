from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.put(x)

        while not self.q1.empty():
            self.q2.put(self.q1.get())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            print("Stack is Empty")
        else:
            print("Popped:", self.q1.get())

    def top(self):
        if self.q1.empty():
            print("Stack is Empty")
        else:
            print("Top:", self.q1.queue[0])


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.top()
s.pop()
s.top()