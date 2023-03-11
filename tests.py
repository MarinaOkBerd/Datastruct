import unittest
from node import Node, Stack
from custom_queue import Queue
from linked_list import LinkedList


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_10 = Node(10)

    def test_node_init(self):
        assert self.node_10.data == 10
        assert self.node_10.next_node is None

    def test_node_next_node(self):
        node2 = Node(220, self.node_10)
        assert node2.next_node is self.node_10


class TestStack(unittest.TestCase):
    def test_Stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.pop(), 'data2')


class TestQueue(unittest.TestCase):
    def test_Queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)


class TestLinkedList(unittest.TestCase):
    def test_LinkedList(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.print_ll(), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


