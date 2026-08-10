class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def create_cycle(head, position):
    if position == -1:
        return

    cycle_node = None
    current = head
    index = 0

    while current.next:
        if index == position:
            cycle_node = current
        current = current.next
        index += 1

    current.next = cycle_node


def find_cycle_start(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Main Program
n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter node values: ").split()))

head = create_linked_list(values)

position = int(input("Enter cycle position (-1 for no cycle): "))
create_cycle(head, position)

start = find_cycle_start(head)

if start:
    print("Cycle starts at node:", start.data)
else:
    print("No Cycle Detected")