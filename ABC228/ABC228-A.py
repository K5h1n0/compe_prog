s,t,x = map(float, input().split())
x = x + 0.5
if s <= t:
    if s <= x <= t:
        print("Yes")
    else:
        print("No")
elif s > t:
    if s <= x <= 24:
        print("Yes")
    elif 0 <= x <= t:
        print("Yes")
    else:
        print("No")
