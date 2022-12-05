a,b,c = map(int, input().split())
if a == b:
    if c == 0:
        print("Aoki")    
    else:
        print("Takahashi")
elif a > b:
    print("Takahashi")
elif b > a:
    print("Aoki")
