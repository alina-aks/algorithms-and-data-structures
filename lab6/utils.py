
import_path = "../files/"

def inp(file_path, start_line=0, *args):
    file_path = import_path + "input.txt"
    with open(file_path, "r") as k:
        if args[0] == 'task2':
            t = k.readline()
            n = int(t)
            b = k.readlines()
            s = []
            for line in b:
                parts = line.split()
                operation = parts[0]
                if operation == "add":
                    s.append([operation, parts[1], parts[2]])
                elif operation in {"del", "find"}:
                    s.append([operation, parts[1]])
            return (n, s)
        elif args[0] == 'task5':
            b = k.readlines()
            s = [line.strip() for line in b]
            return (s)
        elif args[0] == "task7":
            t = k.readline()
            n, p = map(int, t.split())
            s = str(k.readline())
            b = k.readlines()
            l = [line.strip() for line in b]
            return (n, p, s, l)
        elif args[0] == "task8":
            t = k.readline()
            n, x, a, b = map(int, t.split())
            A_c, B_c, A_d, B_d  = map(int, k.readline().split())
            return (n, x, a, b, A_c, B_c, A_d, B_d)
        else:
            t = k.readline()
            n = int(t)
            b = k.readlines()
            s = [[r[0], r[2:]] for r in b]
            return (n, s)

def caption(taskN, res):
    if isinstance(res, float):
        a = (f"Time: {res}"+"\n")+"--"*15+"\n"
    else:
        a = "--"*15+"\n"+(f"LAB6 Task {taskN}\n")+(f"Output: \n{res}\n")
    return a


def outp(file_path, res):
    file_path = import_path + "output.txt"
    with open(file_path, "w") as k:
        k.write(res)