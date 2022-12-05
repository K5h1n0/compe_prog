a500 = int(input())
b100 = int(input())
c50 = int(input())
x = int(input())
cnt = 0
sum = 0
if a500 > 0 and b100 > 0 and c50 > 0:
    for i in range(a500 + 1):
        sum = 0
        for j in range(b100 + 1):
            sum = 0
            for k in range(c50 + 1):
                sum = 0
                sum = sum + 500 * i
                sum = sum + 100 * j
                sum = sum + 50 * k
                if sum == x:
                    cnt = cnt + 1
elif a500 == 0 and b100 > 0 and c50 > 0:
    for j in range(b100 + 1):
        sum = 0
        for k in range(c50 + 1):
            sum = 0
            sum = sum + 100 * j
            sum = sum + 50 * k
            if sum == x:
                cnt = cnt + 1
elif a500 > 0 and b100 == 0 and c50 > 0:
    for i in range(a500 + 1):
        sum = 0
        for k in range(c50 + 1):
            sum = 0
            sum = sum + 500 * i
            sum = sum + 50 * k
            if sum == x:
                cnt = cnt + 1
elif a500 > 0 and b100 > 0 and c50 == 0:
    for i in range(a500 + 1):
        sum = 0
        for j in range(b100 + 1):
            sum = 0
            sum = sum + 500 * i
            sum = sum + 100 * j
            if sum == x:
                cnt = cnt + 1
elif a500 > 0 and b100 == 0 and c50 == 0:
    for i in range(a500 + 1):
        sum = 0
        sum = sum + 500 * i
        if sum == x:
            cnt = cnt + 1
elif a500 == 0 and b100 > 0 and c50 == 0:
    for j in range(b100 + 1):
        sum = 0
        sum = 0
        sum = sum + 100 * j
        if sum == x:
            cnt = cnt + 1
elif a500 == 0 and b100 == 0 and c50 > 0:
    for k in range(c50 + 1):
        sum = 0
        sum = sum + 50 * k
        if sum == x:
            cnt = cnt + 1
print(cnt)
