k = open("input.txt")
n = int(k.readline())
f1,f2 = 0,1
if 0<=n<=45:
    for i in range(2,n+1):
        f1,f2 = f2, (f1+f2)
    y = open("output.txt", "w")
    y.write(str(f2))
else:
    print("Условия для чисел не выполнены")
print(f2)
