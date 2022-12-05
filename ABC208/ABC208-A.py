a,b = map(int, input().split())
if a <= b:
    if a * 6 >= b:
        print("Yes")
    else:
        print("No")
else:
    print("No")