class Rectangle:
    def __init__(self, chieuDai: int, chieuRong: int, mauSac: int):
        self.color = mauSac.capitalize()
        self.perimeter = (chieuDai + chieuRong) * 2
        self.area = chieuRong * chieuDai


if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
