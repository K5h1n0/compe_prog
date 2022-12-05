s = input()
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    tmp = s[a-1:b]
    tmp = tmp[::-1]
    end = s[b:]
    start = s[:a-1]
    s = start + tmp + end
print(s)