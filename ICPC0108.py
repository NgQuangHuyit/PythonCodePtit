for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    for i in range(len(arr)):
        dic[arr[i]] = i
    cnt = 0
    for i in range(N - 2):
        for j in range(i+1, N - 1):
            if dic.get(-(arr[i] + arr[j]), -1) > j:
                cnt += 1
    print(cnt)
