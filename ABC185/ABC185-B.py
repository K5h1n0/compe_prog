ryou,kaisuu,kitaku = map(int,input().split())
l = [list(map(int, input().split())) for _ in range(kaisuu)]
flg = "Yes"
manntann = ryou
for i in range(kaisuu):
    if i == 0:
        ryou = ryou - l[i][0]
    else:
        ryou = ryou - (l[i][0] - l[i-1][1])
    if ryou <= 0:
        flg = "No"
        break
    ryou = ryou + l[i][1] - l[i][0]
    if ryou >= manntann:
        ryou = manntann
ryou = ryou - (kitaku - l[-1][1])
if ryou <= 0:
    flg = "No"
print(flg)