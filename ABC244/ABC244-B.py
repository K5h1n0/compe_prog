n = int(input())
t = input()
a = 0 #南1,西2,北3
x,y = 0,0
for i in t:
    if i =="S":
        if a ==0:
            x += 1
        elif a == 1:
            y -= 1
        elif a == 2:
            x -= 1
        else:
            y += 1
    else:
        a = (a + 1)%4
print(x,y)