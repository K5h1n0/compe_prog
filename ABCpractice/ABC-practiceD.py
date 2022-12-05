n = int(input())
l = list(map(int, input().split()))
a = 0
b = 0
while a == 0:
    for i in range(n):
            if l[i] % 2 ==0:
                a += 0
            elif l[i] % 2 == 1:
                a += 1
    if a == 0:
        for i in range(n):
            l[i] = l[i]//2
        b = b + 1
    elif a >= 1:
        print(b)
        break
   
