n = int(input())
a,b = map(int,input().split())
k = int(input())
l = list(map(int,input().split()))
if len(l) == len(list(set(l))) and a not in l and b not in l:
    print("YES")
else:
    print("NO")