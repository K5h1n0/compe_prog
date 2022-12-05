import itertools
n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
l = list(itertools.permutations(list(range(1,n+1))))
print(abs(l.index(p) - l.index(q)))