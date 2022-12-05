k = list(bin(int(input()))[2:])
for i in range(len(k)):
    if k[i] == "1":
        k[i] = "2"
print(*k,sep="")