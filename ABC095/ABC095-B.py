n,x = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
print(len(l) + (x - sum(l)) // min(l))