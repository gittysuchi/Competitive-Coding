stack1 = []
stack2 = []

def enqueue(x):
    stack1.append(x)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())

    if not stack2:
        print("Queue is Empty")
    else:
        print("Deleted:", stack2.pop())

def front():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())

    if stack2:
        print("Front:", stack2[-1])
    else:
        print("Queue is Empty")


enqueue(10)
enqueue(20)
enqueue(30)

front()
dequeue()
front()