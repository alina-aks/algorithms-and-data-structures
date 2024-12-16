
import_path = "../files/"

def inp(file_path, start_line=0, *args):
    file_path = import_path + "input.txt"
    with open(file_path, "r") as k:
        t = k.readline()
        if args[0] == 'task7':
            n = int(t)
            b = k.readline().split(" ")
            s = [int(l) for l in b]
            m = int(k.readline())
            return (n, s, m)
        else:
            m = int(t)
            c = [line.strip() for line in k.readlines()]
            return (m, c)

def caption(taskN, res):
    if isinstance(res, float):
        a = (f"Time: {res}"+"\n")+"--"*15+"\n"
    else:
        a = "--"*15+"\n"+(f"LAB5 Task {taskN}\n")+(f"Output: \n{res}\n")
    return a


def outp(file_path, res):
    file_path = import_path + "output.txt"
    with open(file_path, "w") as k:
        k.write(res)