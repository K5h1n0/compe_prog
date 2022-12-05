n = int(input())
l = sorted(list(map(int,input().split())))
if l[len(l)//2-1] == l[len(l)//2]:
    print(0)
else:
    print(l[len(l)//2] - l[len(l)//2-1])