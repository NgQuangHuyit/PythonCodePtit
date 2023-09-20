from decimal import Decimal
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        dist = sqrt((self.x - p.stepCnt) ** 2 + (self.y - p.y) ** 2)
        return dist


class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    def chuVi(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        if max(a, b, c) * 2 >= a + b + c:
            print('INVALID')
        else:
            print('{:.3f}'.format(a + b + c))


data = []
t = int(input())
for x in range(t):
    data += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triangle = Triangle(Point(data[i], data[i + 1]), Point(data[i + 2], data[i + 3]), Point(data[i + 4], data[i + 5]))
    triangle.chuVi()
    i += 6