h,m = input().split()
h = h.zfill(2)
m = m.zfill(2)
while True:
    if 0 <= int(h[0])*10+int(m[0]) <= 23 and 0 <= int(h[1])*10 + int(m[1]) <= 59:
        print(h,m)
        break
    if int(m) == 59:
        m = "00"
        h = int(h) + 1
        if int(h) == 24:
            h = "00"
        h = str(h).zfill(2)
    else:
        m = int(m) + 1
        m = str(m).zfill(2)