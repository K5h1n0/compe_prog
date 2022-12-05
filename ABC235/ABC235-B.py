n = int(input())
l = list(map(int, input().split()))
a = l[0]
for i in range(n):
    if i == n-1:
        if l[n-2] < l[n-1]:
            print(l[n-1])
        else:
            print(l[n-2])
            break
    elif l[i] < l[i+1]:
        a = l[i+1]
    else:
        print(a)
        break