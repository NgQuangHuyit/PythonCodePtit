class BangDiem:
    id = 1

    def __init__(self, name, points):
        self.name = name
        self.points = points
        if self.id < 10:
            self.id = "HS" + "0" + str(self.id)
        else:
            self.id = "HS" + str(self.id)
        BangDiem.id += 1
        diem = sum(self.points[2:]) + (self.points[0] + self.points[1]) * 2
        self.diem = round(diem/12 + 0.01, 1)
        if self.diem >= 9:
            self.rank = 'XUAT XAC'
        elif self.diem >= 8:
            self.rank = 'GIOI'
        elif self.diem >= 7:
            self.rank = 'KHA'
        elif self.diem >= 5:
            self.rank = 'TB'
        else:
            self.rank = 'YEU'

    def __str__(self):
        return f"{self.id} {self.name} {self.diem:.1f} {self.rank}"


N = int(input())
listStudent = []
for i in range(N):
    name = input()
    points = [float(point) for point in input().split()]
    listStudent.append(BangDiem(name, points))
listStudent.sort(key=lambda x: (-x.diem, x.id))
for student in listStudent:
    print(student)

        
