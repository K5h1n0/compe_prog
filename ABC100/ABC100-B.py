#理解した。100で割ることができるはn%100で判定できるけど、「100で丁度1回割ることができる」と言われたら工夫しなきゃいけない。
d,n = map(int,input().split())
ans = 0
i = 1
while n != 0:
    if d == 0:
        if i%100 != 0:
            n -= 1
            ans = i
    elif d == 1:
        if i%100 == 0 and not (i%10000 == 0):
            n -= 1
            ans = i
    elif d == 2:
        if i%10000 == 0 and not (i%1000000 == 0):
            n -= 1
            ans = i
    i += 1
print(ans)