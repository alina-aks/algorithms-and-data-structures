
import_path = "../files/"

def inp(file_path):
    file_path = import_path + "input.txt"
    with open(file_path, "r") as k:
        t = k.readline()
        m = int(t)
        b = k.readline().split(" ")
        s = [int(l) for l in b]
        return (m, s)

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