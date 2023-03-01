class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        pop_node = self.top
        pop_data = pop_node.data
        self.top = pop_node.next_node
        return pop_data


stack = Stack()
stack.push('data1')
data = stack.pop()

# стэк стал пустой
print(stack.top)
#None

# pop() удаляет элемент и возвращает данные удаленного элемента
print(data)
#'data1'


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
#'data1'

# данные удаленного элемента
print(data)
#'data2'