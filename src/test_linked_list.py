"""Testing the linked_list module."""
import pytest


def test_for_instance_of_node():
    """Test node variable is instnace of Node()."""
    from linked_list import Node
    n = Node()
    assert isinstance(n, Node)


def test_for_instance_of_linked_list():
    """Test variable is instnace of ()."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_linked_list_head_is_none():
    """Test Linked List head is None."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.head is None


def test_linked_list_count_is_zero():
    """Test Linked List value is zero."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll._counter is 0


def test_linked_list_push_value_becomes_head():
    """Test push(val) to Linked List becomes head."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data is 5


def test_linked_list_counter_is_one_after_push_value():
    """Test Linked List counter is one after push(val)."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    assert ll._counter is 1