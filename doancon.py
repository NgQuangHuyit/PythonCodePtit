ds1 = [int(i) for i in input().split()]
ds2 = [int(i) for i in input().split()]
ok = True
for i in range(len(ds2)):
    if ds2[i] not in ds1:
        ok = False
        break
print(ok)
