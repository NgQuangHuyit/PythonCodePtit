def check(array):
    for i in range(len(array) - 1):
        if (array[i] + array[i + 1]) % 2 == 0:
            return i
    return -1


N = int(input())
arr = list(map(int, input().split()))
while True:
    i = check(arr)
    if i == -1:
        break
    del arr[i:i+2]
print(len(arr))
