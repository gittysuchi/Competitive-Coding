class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if stack.pop() != slow.data:
            return False
        slow = slow.next

    return True

n = int(input("Enter number of nodes: "))

head = None
tail = None

for i in range(n):
    data = int(input("Enter node value: "))
    newNode = Node(data)

    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode

if isPalindrome(head):
    print("Palindrome")
else:
    print("Not Palindrome")