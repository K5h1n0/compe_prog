#もう少しスマートに書けそうだけど
n,a,b = map(int,input().split())
now = 0
for i in range(n):
    s,d = input().split()
    if int(d) < a:
        d = a
    elif b < int(d):
        d = b
    if s == "East":
        now += int(d)
    elif s == "West":
        now -= int(d)
if now == 0:
    print(now)
elif now < 0:
    print("West",-now)
else:
    print("East",now)