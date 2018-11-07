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


def test_linked_list_head_is_none_and_count_is_zero():
    """Test Linked List head is None and counter is zero."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.head is None
    assert ll._counter is 0


def test_linked_list_push_value_becomes_head_and_counter_is_one():
    """Test push(val) to Linked List becomes head and counter is one."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data is 5
    assert ll._counter is 1


def test_second_push_value_becomes_head_and_counter_is_two():
    """Test second push(val) to Linked List becomes head and counter is two."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    ll.push(10)
    assert ll.head.data is 10
    assert ll._counter is 2


def test_head_node_points_to_next_node():
    """Test the head Node points to next Node."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    ll.push(10)
    assert ll.head.next.data is 5


def test_pop_method_returns_value_and_updates_counter():
    """Test pop() method returns the value of popped Node and counter is zero"""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    popped = ll.pop()
    assert popped is 5
    assert ll._counter is 0


def test_head_updated_after_pop():
    """Test head Node is updated after pop() method."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    ll.push(10)
    ll.pop()
    assert ll.head.data is 5


def test_size_method_returns_counter_value():
    """Test size method returns the value of the counter."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(5)
    ll.push(10)
    count = ll.size()
    assert count is 2


def test_empty_linked_list_pop_raises_exception():
    """Test pop method on empty Linked List raises exception."""
    from linked_list import LinkedList
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.pop()