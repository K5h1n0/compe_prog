import itertools
n = int(input())
l = []
for i in range(n):
    l.append(list(input().split()))
l = list(itertools.chain.from_iterable(l))
mountname = []
mountheight = []
for i in range(len(l)):
    if i%2 == 0:
        mountname.append(l[i])
    else:
        mountheight.append(l[i])
mountheight = list(map(int, mountheight))
a = mountheight.index(max(mountheight))
del mountheight[mountheight.index(max(mountheight))]
del mountname[a]
a = mountheight.index(max(mountheight))
print(mountname[a])