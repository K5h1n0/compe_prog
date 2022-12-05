#解説AC 難しい

from functools import lru_cache

n,x,y = map(int, input().split())

@lru_cache(maxsize=100000000)
def gem(level,is_red,cnt):
    if level == 1:
        if is_red == False:
            return cnt
        else:
            return 0
    if is_red == True:
        return gem(level-1,True,cnt) + gem(level,False,cnt*x)
    else:
        return gem(level-1,True,cnt) + gem(level-1,False,cnt*y)

print(gem(n,True,1))