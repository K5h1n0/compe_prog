n = input()
a,b = n.split(".")
b = int(b)
if 0 <= b <= 2:
    c = "-"
elif 7 <= b <=9:
    c = "+"
else:
    c = ""
d = str(a) + str(c)
print(d)
