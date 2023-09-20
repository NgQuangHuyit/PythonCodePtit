import math

a, b, c = map(int, input('nhap vao he so a, b, c cua phuong trinh (ax^2 + bx + c = 0)\n').split())   # ax^2 + bx + c = 0
if a == 0:
    if b == 0:
        if c == 0:
            print('Vo so nghiem')
        else:
            print('Vo nghiem')
    else:
        print(f"Co nghiem duy nhat x = {(-c/b):.2f}")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Vo nghiem')
    elif delta == 0:
        print(f'Nghiem duy nhat x = {(-b/2*a):.2f}')
    else:
        print(f"phuong trinh co 2 nghiem phan biet x1 = {(-b + math.sqrt(delta))/ 2 * a:.2f} va x2 = {(-b - math.sqrt(delta))/ 2 * a:.2f}")
