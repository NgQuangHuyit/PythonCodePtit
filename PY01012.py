s1 = list(input())
s2 = input()
p = int(input())
s1.insert(p-1, s2)
print(''.join(s1))