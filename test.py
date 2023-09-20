import re

s = ""
regex = '[\w\s,:]+\.?\??\!?'
s = '''Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
moi    CAC BAN danG ky     thaM giA !'''
'''while True:
    try:
        s += input()
    except EOFError:
        break'''

s = re.findall(regex, s)
for i in s:
    i = i.strip()
    m = i.split(sep='\n')
    if len(m) == 1:
        x = i.lower().split()
        x[0] = x[0].title()
        res = ' '.join(x)
        res = res.strip()
        if (res[-1] != "." and res[-1] != '?' and res[-1] != '!'):
            res += '.'
        else:
            res = res[0:len(res) - 1].strip() + res[-1]
        print(res)
    else:
        for comp in m:
            x = comp.lower().split()
            x[0] = x[0].title()
            res = ' '.join(x)
            res = res.strip()
            if (res[-1]!="." and res[-1]!='?' and res[-1] != '!'):
                res += '.'
            else:
                res = res[0:len(res)-1].strip() + res[-1]
            print(res)
