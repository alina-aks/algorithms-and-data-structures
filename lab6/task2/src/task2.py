import time
import os
from lab6.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def Phonebook(n, operations):
    phonebook = {}
    result = []

    for operation in operations:
        if operation[0] == "add":
            number, name = operation[1], operation[2]
            phonebook[number] = name
        elif operation[0] == "del":
            number = operation[1]
            phonebook.pop(number, None)
        elif operation[0] == "find":
            number = operation[1]
            result.append(phonebook.get(number, "not found"))

    return result


def task1():
    n, s = inp(PATH_INPUT, 0, 'task2')
    res = str(Phonebook(n, s))
    global task_numb
    task_numb = 2
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))

