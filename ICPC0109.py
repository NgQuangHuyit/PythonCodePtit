for t in range(int(input())):
    N = input()
    min_values = [100000000, 100000000, 100000000]
    for num in map(int, input().split()):
        for i in range(3):
            if num < min_values[i]:
                min_values.insert(i, num)
                min_values.pop()
                break
    print(sum(min_values))