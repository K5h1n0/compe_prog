l = list(map(int,input().split()))
l.pop(l.index(max(l)))
print(sum(l))