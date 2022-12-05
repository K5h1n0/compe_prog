a,b = map(int,input().split())
if b % a == 0: #ここのaとbを反対にしていた
    print(a+b)
else:
    print(b-a)