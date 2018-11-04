"""Linked List: consists of Nodes, each of which contains some data and a pointer to the next node."""


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

    def push(self, val):
        """Add a new Node to the head of the Linked List"""
        new_head = Node(val, self.head)
        self.head = new_head