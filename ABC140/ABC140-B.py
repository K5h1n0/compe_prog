n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
total = 0
record = -10
for i in a:
    total += b[i-1]
    if i == record + 1:
        total += c[record-1]
    record = i
print(total)
