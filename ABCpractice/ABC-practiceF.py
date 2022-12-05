n,a,b = map(int, input().split())
work = 0
sum = 0
for i in range(n):
    i = i + 1
    i = str(i)
    l = list(i)
    work = 0
    for j in range(len(l)):
        work = work + int(l[j])
    if a <= work and work <= b:
        sum = sum + int(i)
print(sum)
