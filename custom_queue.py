class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head == None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next_node
        return data






queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


