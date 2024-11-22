import_path = "../files/"

def inp(file_path):
    file_path = import_path + "input.txt"
    with open(file_path, "r") as k:
        t = k.readline()
        if " " in str(t):
            n, *list1 = map(int, t.split())
            k, *searchs = map(int, k.readline().split())
            return (n, list1, k, searchs)
        else:
            n = int(t)
            b = k.readline().split(" ")
            s = [int(l) for l in b]
            return (n, s)

def outp(file_path, res):
    file_path = import_path + "output.txt"
    with open(file_path, "w") as k:
        k.write(res)

