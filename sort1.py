a = [4, 3, 5, 1, 2]
for i in range(4):
    for j in range(4-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)