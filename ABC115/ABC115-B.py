n =  int(input())
l = []
maximum = 0
for i in range(n):
    l.append(int(input()))
    if l[i] > maximum:
        maximum = l[i]
l[l.index(maximum)] = l[l.index(maximum)]//2
print(sum(l))