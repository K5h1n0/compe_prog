#解説見ながらAC メモ化再帰の使い方について良く知ること。
from functools import lru_cache

@lru_cache
def f(k):
    if k == 0:
        return 1
    else:
        return f(k//2)+f(k//3)

n = int(input())
print(f(n))