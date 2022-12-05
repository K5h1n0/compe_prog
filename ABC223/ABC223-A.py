x = int(input())
a = x % 100
if x <= 99 or (x >= 100 and a != 0):
    print("No")
else:
    print("Yes")
