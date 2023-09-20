arr = [int(i) for i in input().split()]
minSum_of_subArr = 99999999999999999999999
subArr = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        localSum = sum(arr[i:j + 1])
        if localSum < minSum_of_subArr:
            minSum_of_subArr = localSum
            subArr = arr[i:j + 1]


print(subArr)
print(minSum_of_subArr)