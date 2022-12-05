import copy

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l2 = copy.copy(l)
first = max(l)
l.remove(first)
second = max(l)
if first == second:
    for i in range(n):
        print(first)
else:
    for i in range(len(l2)):
        if l2[i] == first:
            print(second)
        else:
            print(first)