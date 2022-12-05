n = int(input())
s = list(input())
tmp = 0
maximum = 0
for i in range(n):
    if s[i] == "I":
        tmp += 1
    else:
        tmp -= 1
    if maximum < tmp:
        maximum = tmp
print(maximum)