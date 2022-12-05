s = list(input())
n = len(s)
m = len(list(set(s)))
if n == m:
    print("yes")
else:
    print("no")