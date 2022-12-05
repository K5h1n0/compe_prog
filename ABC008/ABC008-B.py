import copy

n = int(input())
l1 = []
for i in range(n):
    l1.append(input())
l2 = copy.copy(l1)
l2 = list(set(l2))
l3 = [0]*len(l2)
l4 = dict(zip(l2,l3))
for i in range(len(l1)):
    l4[l1[i]] += 1
print(max(l4,key=l4.get))