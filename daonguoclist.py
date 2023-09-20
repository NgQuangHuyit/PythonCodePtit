ls = list(map(int, input().split()))
for i in range(len(ls)//2):
    ls[i], ls[len(ls) - 1 - i] = ls[len(ls) - 1 - i], ls[i]
print(*ls)
