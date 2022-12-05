#スマートじゃないと思う
h,w = map(int,input().split())
l = []
h2 = h
for i in range(h):
    tmp = list(input())
    cnt = 0
    for j in range(w):
        if tmp[j] == ".":
            cnt += 1
    if cnt == w:
        h2 -= 1
    else:
        l.append(tmp)
#全部"."の列を検索
l2 = []
for i in range(w):
    cnt = 0
    for j in range(h2):
        if l[j][i] == ".":
            cnt += 1
    if cnt == h2:
        l2.append(i)
l2.sort(reverse=True)
for i in l2:
    for j in range(h2):
        l[j].pop(i)

for i in range(h2):
    s = ""
    for j in range(len(l[i])):
        s += str(l[i][j])
    print(s)


#https://img.atcoder.jp/arc101/editorial.pdf
#解説が天才か？