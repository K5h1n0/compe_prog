#全然知らない
x,y = map(int,input().split())
g4 = {x,y}
g1 = {1,3,5,7,8,10,12}
g2 = {4,6,9,11}
g3 = {2}
if g4<=g1 or g4<=g2 or g4<=g3: #これも初めて見た
    print("Yes")
else:
    print("No")