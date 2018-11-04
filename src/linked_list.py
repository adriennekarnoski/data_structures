"""Linked List: consists of Nodes, each of which contains some data and a pointer to the next node.

Attributes: Nodes, LinkedList.

Operations: insert(val), pop(), """


class Node(object):
    """Create a Node object for storing data and a pointer to the next Node."""

    def __init__(self, data=None, next=None):
        """Initialize data and a pointer to the next Node."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Build a Linked List."""

    def __init__(self):
        """Initialize a Linked List."""
        self.head = None
        self._counter = 0

    def push(self, val):
        """Add a new Node to the head of the Linked List"""
        new_head = Node(val, self.head)
        self.head = new_head
        self._counter += 1

    def pop(self):
        """Remover the Node at the head of the Linked List and return the value."""
        output = self.head.data
        self.head = self.head.next
        return output

    def size(self):
        """Return the size of the Linked List."""
        return self._counter
