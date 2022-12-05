a, b, c, d = map(int, input().split()) 

ta= a*10000 + b*100
ao= c*10000 + d*100 +1

if ta < ao:
    print("Takahashi")
else:
    print("Aoki")
