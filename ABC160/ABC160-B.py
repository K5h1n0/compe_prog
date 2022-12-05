x = int(input())
cnt = 0
while x >= 500:
    x -= 500
    cnt += 1000
while x >= 5:
    x -= 5
    cnt += 5
print(cnt)