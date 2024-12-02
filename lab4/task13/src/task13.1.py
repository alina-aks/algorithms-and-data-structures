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
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Stack:", " -> ".join(map(str, elements)) if elements else "empty")


if __name__ == "__main__":
    stack = Stack()

    print("Стек пустой?", stack.isEmpty())
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Стек")
    stack.display()

    print("Удаленный элемент:", stack.pop())
    print("Обновленный стек:")
    stack.display()

    print("Стек пустой?", stack.isEmpty())
