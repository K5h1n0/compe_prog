a,b,c = map(int,input().split())
if (a == b or b == c or c == a) and not a == b == c:
    print("Yes")
else:
    print("No")