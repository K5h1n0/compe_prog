n = int(input())
l = list(map(int, input().split())) 
l2 = [0] * (n+1)
for i in l:
    l2[i] += 1
l2.pop(0)
print((l2.index(3))+1)



"""
n = int(input())
l = list(map(int, input().split())) 
l2 = list(set(l))
l2.sort()
l.sort()
for i in range(n):
    for j in range(3):
        l.remove(i+1)
for i in range(len(l2)):
    if l2[i] not in l:
        print(l2[i])
        break
"""