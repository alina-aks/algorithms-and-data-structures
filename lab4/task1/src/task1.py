import time
import random
import os
from lab4.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')
task_numb = 1


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def process_stack_commands(commands):
    stack = Stack()
    output = []

    for command in commands:
        command = command.strip()
        if command.startswith('+'):
            _, value = command.split()
            stack.push(int(value))
        elif command == '-':
            if not stack.is_empty():
                output.append(stack.pop())
    return output


def task1():
    m, commands = inp(PATH_INPUT,0,'task1')
    res = str(process_stack_commands(commands))
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))

if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))
