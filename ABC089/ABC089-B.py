n = int(input())
s = list(input().split())
s = len(list(set(s)))
if s == 4:
    print("Four")
else:
    print("Three")