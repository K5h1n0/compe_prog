H, W = map(int, input().split())   #Hは縦マス、Wは横マス
R, C = map(int, input().split())   #RとCは現在のXとYマス

masu = 4

if R == 1 :
    masu = masu - 1
if R == H :
    masu = masu - 1
if C == 1 :
    masu = masu - 1
if C == W :
    masu = masu - 1

print(masu)
