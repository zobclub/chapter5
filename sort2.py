a = [4, 3, 5, 1, 2]
for i in range(4):
    j = i+1
    while (j > 0) and (a[j-1] > a[j]):
        a[j-1], a[j] = a[j], a[j-1]
        j-=1
        print(a)
 