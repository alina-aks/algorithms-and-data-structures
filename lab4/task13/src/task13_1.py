import time
from lab4.utils import caption
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

    def display(self):
        if self.isEmpty():
            return
        current = self.top
        while current:
            print(current.value)
            current = current.next

def task1():
    global task_numb
    task_numb = 13.1
    a = "--"*15+"\n"+(f"LAB5 Task {task_numb}\n")+(f"Output: \n")
    print(a)

    stack = Stack()
    print("Стек пуст:", stack.isEmpty())
    print("Добавленно:", end="")
    stack.push(10)
    stack.display()
    print("Извлечён элемент:", stack.pop())
    stack.display()
    print("Стек пуст:", stack.isEmpty())
    print('\n')

if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))
