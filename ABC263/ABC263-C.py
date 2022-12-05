# contest中に初C問題クリア！！
import itertools
n,m = map(int,input().split())
l = []
for i in range(1,m+1):
    l.append(i)
for i in itertools.combinations(l, n):
    print(*i)