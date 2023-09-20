N, K = map(int, input().split())
arr = list(map(int, input().split()))
A = [0]
for i in range(N):
    A.append(A[i] + arr[i])
for i in range(N):
    for j in range(i+1, N+1):
        if (A[j] - A[i]) % K == 0:
            print(arr[i:j])

