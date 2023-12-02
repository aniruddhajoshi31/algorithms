# What a linked list should have
# Add nodes at the beginning, middle and end.
# Delete the first, middle and end node.
# Read a node - first, middle and last

# The Node Class

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# The Linked List Class

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        
        # Case 1: LinkedList is empty
        # Case 2: It has at least one element
        
        if self.head is None:
            self.head = Node(data)
            self.head.next = None

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


my_ll = LinkedList()
my_ll.insert_at_begin('Joshi')
my_ll.insert_at_begin('Aniruddha')
print(my_ll.head.data)
print(my_ll.head.next.data)
print(my_ll.head.next.next)
