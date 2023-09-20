from math import sqrt


def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


for t in range(int(input())):
    N = input()
    number = int(N[-4:])
    if isPrime(number):
        print("YES")
    else:
        print("NO")
