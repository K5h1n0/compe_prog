s = input()
while len(s) != 0:
    tmp5 = s[-5:]
    tmp6 = s[-6:]
    tmp7 = s[-7:]
    if len(s) >= 5 and tmp5 == "dream" or tmp5 == "erase":
        s = s[:-5]
    elif tmp6 == "eraser":
        s = s[:-6]
    elif tmp7 == "dreamer":
        s = s[:-7]
    else:
        print("NO")
        exit()
print("YES")