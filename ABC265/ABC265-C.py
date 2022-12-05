h,w = map(int,input().split())
l = []
flgzu = []
for i in range(h):
    l.append(input())
    flgzu.append([0 for __ in range(w)])
xima = 0
yima = 0
for i in range(h*w+1):
    if flgzu[xima][yima] == 1:
        print(-1)
        exit()
    flgzu[xima][yima] = 1
    if l[xima][yima] == "R":
        if yima == w-1:
            print(xima+1,yima+1)
            exit()
        yima += 1

    elif l[xima][yima] == "L":
        if yima == 0:
            print(xima+1,yima+1)
            exit()
        yima -= 1
        
    elif l[xima][yima] == "D":
        if xima == h-1:
            print(xima+1,yima+1)
            exit()
        xima += 1
        
    elif l[xima][yima] == "U":
        if xima == 0:
            print(xima+1,yima+1)
            exit()
        xima -= 1