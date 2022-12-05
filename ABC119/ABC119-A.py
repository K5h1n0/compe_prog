s = input()
m = int(s[5])*10 + int(s[6])
d = int(s[8])*10 + int(s[9])
if m >= 5:
    print("TBD")
elif m < 4:
    print("Heisei")
else:
    if d > 30:
        print("TBD")
    else:
        print("Heisei")