"""
#通らなかった
n = int(input())
s = input()
length = len(s)
accessory = "b"
if len(s) == 1 and s == accessory:
    print(0)
    exit()
elif len(s) == 1 and s != accessory:
    print(-1)
    exit()
for i in range(1,100):
    if i % 3 == 1:
        accessory = "a" + accessory + "c"
    elif i % 3 == 2:
        accessory = "c" + accessory + "a"
    elif i % 3 == 0:
        accessory = "b" + accessory + "b"
    if s == accessory:
        print(i)
        exit()
    if i > length:
        print(-1)
        exit()
"""