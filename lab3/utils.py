
import_path = "../files/"

def inp(file_path, start_line=0, *args):
    file_path = import_path + "input.txt"
    with open(file_path, "r") as k:
        t = k.readline()
        if args[0] == 'task3':
            n, r = map(int, t.split())
            b = k.readline().split(" ")
            s = [int(l) for l in b]
            return (n, r, s)

        elif args[0] == "task4":
            s, p = map(int, t.split())
            segments = [list(map(int, k.readline().split())) for _ in range(s)]
            points = list(map(int, k.readline().split()))
            return (s, p, segments, points)

        elif args[0] == "task5":
            b = t.split(",")
            s = [int(l) for l in b]
            return (s)

        elif args[0] == "task6":
            n, m = map(int, t.split())
            A = list(map(int, k.readline().split()))
            B = list(map(int, k.readline().split()))
            return (n,m,A,B)

        elif args[0] == "task7":
            n, m, k = map(int, t.split())
            data = [k.readline().strip() for _ in range(m)]
            return (n,m,k, data)

        elif args[0] == "task2":
            n = int(t)
            return (n)

        elif " " in str(t):
            n, *list1 = map(int, t.split())
            k, *searchs = map(int, k.readline().split())
            return (n, list1, k, searchs)
        else:
            n = int(t)
            b = k.readline().split(" ")
            s = [int(l) for l in b]
            return (n, s)

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