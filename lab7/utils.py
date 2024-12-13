
import_path = "../files/"

def inp(file_path, start_line=0, *args):
    file_path = import_path + "input.txt"
    with open(file_path, "r") as k:
        if args[0] == "task4":
            n = int(k.readline())
            y = k.readline().split(" ")
            a = [int(l) for l in y]
            m = int(k.readline())
            u = k.readline().split(" ")
            b = [int(l) for l in u]
            return (n, a, m, b)
        elif args[0] == "task5":
            n = int(k.readline())
            y = k.readline().split(" ")
            a = [int(l) for l in y]
            m = int(k.readline())
            u = k.readline().split(" ")
            b = [int(l) for l in u]
            l = int(k.readline())
            o = k.readline().split(" ")
            c = [int(l) for l in o]
            return (n, a, m, b, l, c)
        elif args[0] == "task1":
            t = k.readline()
            n, p = map(int, t.split())
            u = k.readline().split(" ")
            b = [int(l) for l in u]
            return (n, p, b)
        else:
            t = k.readline()
            n = int(t)
            u = k.readline().split(" ")
            b = [int(l) for l in u]
            return (n, b)

def caption(taskN, res):
    if isinstance(res, float):
        a = (f"Time: {res}"+"\n")+"--"*15+"\n"
    else:
        a = "--"*15+"\n"+(f"LAB7 Task {taskN}\n")+(f"Output: \n{res}\n")
    return a


def outp(file_path, res):
    file_path = import_path + "output.txt"
    with open(file_path, "w") as k:
        k.write(res)