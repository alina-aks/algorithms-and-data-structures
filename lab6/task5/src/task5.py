import time
import os
from lab6.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def count_votes(s):
    votes = {}

    for i in range(len(s)):
        parts = s[i].split()
        candidate_name = parts[0]
        number_of_votes = int(parts[1])

        if candidate_name in votes:
            votes[candidate_name] += number_of_votes
        else:
            votes[candidate_name] = number_of_votes

    return votes


def task1():
    s = inp(PATH_INPUT, 0, 'task5')
    res = str(count_votes(s))
    global task_numb
    task_numb = 5
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))