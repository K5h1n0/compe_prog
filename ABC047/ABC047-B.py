w,h,n = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
ulx = 0
uly = h
lrx = w
lry = 0
for i in range(n):
    if l[i][2] == 1:
        ulx = max(ulx,l[i][0]) #この方法良いな～
    elif l[i][2] == 2:
        lrx = min(lrx,l[i][0])
    elif l[i][2] == 3:
        lry = max(lry,l[i][1])
    elif l[i][2] == 4:
        uly = min(uly,l[i][1])
print(max(0,(lrx-ulx))*max(0,(uly-lry)))