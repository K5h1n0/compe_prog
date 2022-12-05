n = int(input())
l = list(map(int,input().split()))
if sum(l) % n != 0:
    print(-1)
    exit()
else:
    l2 = [sum(l)//n]*n
    print(l2)