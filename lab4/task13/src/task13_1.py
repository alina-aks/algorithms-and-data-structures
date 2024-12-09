class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("ошибка")
        value = self.top.value
        self.top = self.top.next
        return value

    def printstack(self):
        if self.isEmpty():
            print('Стек пустой')
        else:
            curr = self.top
            while curr:
                print(curr.value)
                curr = curr.next
