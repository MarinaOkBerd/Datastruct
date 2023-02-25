import unittest
from node import Node, Stack


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_10 = Node(10)

    def test_node_init(self):
        assert self.node_10.data == 10
        assert self.node_10.next_node is None

    def test_node_next_node(self):
        node2 = Node(220, self.node_10)
        assert node2.next_node is self.node_10


