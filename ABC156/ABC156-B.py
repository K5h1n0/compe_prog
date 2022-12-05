import numpy as np
n,k = map(int,input().split())
print(len(list(np.base_repr(n, k))))