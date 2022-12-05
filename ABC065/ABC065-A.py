x,a,b = map(int,input().split())
if a-b >= 0:
    print("delicious")
elif x >= abs(a-b):
    print("safe")
else:
    print("dangerous")