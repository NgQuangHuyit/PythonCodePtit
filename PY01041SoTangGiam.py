for t in range(int(input())):
    N = list(map(int, list(input())))
    if len(N) < 3:
        print("NO")
        continue
    ok = True
    des = True
    for i in range(1, len(N)):
        if des and N[i] <= N[i]:
            des = False
        elif not des and N[i] >= N[i-1]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")

