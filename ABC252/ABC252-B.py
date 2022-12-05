N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
saidai = max(A)

l = [0] * N

for i in range(len(A)):
    if A[i] == saidai:
        l[i] = 1
    else:
        l[i] = 0

q = 0
for i in range(len(B)):
    B[i] = B[i] - 1
    if l[B[i]] == 1:
        q = 1

if q == 1:
    print("Yes")
elif q == 0:
    print("No")

