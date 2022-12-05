n,k,q = map(int,input().split())
participant = [k-q]*n
for i in range(q):
    a = int(input())
    participant[a-1] += 1
for i in range(n):
    if participant[i] > 0:
        print("Yes")
    else:
        print("No")