f = open("input.txt")
a,b = map(int, f.readline().split())
if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
    summ = str(a+b)
    k = open("output.txt", "w")
    k.write(summ)
    print(a+b)
else:
    print("Условия для чисел не выполнены")