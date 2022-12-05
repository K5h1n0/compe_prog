l = input()
a=l[0]
b=l[1]
c=l[2]
if a == b and b == c:
    print(1)
elif a != b and b != c and a != c:
    print(6)
elif a == b or b == c or a == c:
    print(3)
