s = list(input())
s = list(set(s))
if len(s) == 4:
    print("Yes")
elif len(s) == 2:
    if "N" in s or "S" in s and "N" in s and "S" in s:
        print("Yes")
        exit()
    if "W" in s or "E" in s and "W" in s and "E" in s:
        print("Yes")
        exit()
    else:
        print("No")
else:
    print("No")