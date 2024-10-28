import time
def inp(file_path):
    with open(file_path, "r") as k:
        t = k.readline()
        if len(t) < 4 :
            n = int(t)
            b = k.readline().split(" ")
            s = [int(l) for l in b]
            return (n, s)
        else:
            n, *list1 = map(int, t.split())
            k, *searchs = map(int, k.readline().split())
            return (n, list1, k, searchs)

def outp(file_path, res):
    with open(file_path, "w") as k:
        k.write(res)
