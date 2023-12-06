# Print the last third element of a linked list.

# nodes -> each node has 2 different attributes
# 1. value -> can be anything like strings, integer, objects etc..
# 2. the next node

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


def print_last_third(head):

    if head is None:
        print("List is empty")
        return

    length = 0
    current = head

    while current:
        length += 1
        current = current.next

    if length < 3:
        print("List is less than 3 elements")
        return

    current = head

    for _ in range(length - 3):
        current = current.next

    print("The last third element is :", current.data)


linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

linked_list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print_last_third(linked_list.head)
