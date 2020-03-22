import random
a = ['A', 'B', 'C', 'D', 'E']
for i in range(4):
    r = random.randint(0, 4-i)
    print(r)
    a[i], a[r] = a[r], a[i]
print(a)