class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def oddEvenList(self):
        if self.head is None or self.head.next is None:
            return

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
ll = LinkedList()

n = int(input("Enter number of nodes: "))

print("Enter node values:")
for i in range(n):
    value = int(input())
    ll.insert(value)

print("Original Linked List:")
ll.display()

ll.oddEvenList()

print("Odd Even Linked List:")
ll.display()