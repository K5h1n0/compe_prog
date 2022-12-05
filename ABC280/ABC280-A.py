h,w = map(int,input().split())
cnt = 0
for i in range(h):
    tmp = input()
    cnt += tmp.count("#")
print(cnt)