#while文で書き直したい。
h,w = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(h)]
ans = "Yes"
i,j,k,l = 0,0,0,0
flg = 0
while flg == 0 and i <= h-1:
    while flg == 0 and j <= w-1:
        print("---------始点","(",i,",",j,")")





        while flg == 0 and k <= h:

            
            while flg == 0 and l <= w:
                print("終点","(",l,",",w,")")
                l += 1
            l = l + i
            k += 1




        j += 1
    j = 0
    i += 1
    



"""
for i in range(h-1):
    for j in range(w-1):
        for k in range(i+1,h):
            for l in range(j+1,w):
                if list[i][j] + list[k][l] <= list[i][l] + list[k][j]:
                    pass
                else:
                    ans = "No"
                    break
print(ans)
"""

"""
#AC
h,w = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(h)]
a = 0
ans = "Yes"
for i in range(h-1):
    for j in range(w-1):
        for k in range(i+1,h):
            for l in range(j+1,w):
                if list[i][j] + list[k][l] <= list[i][l] + list[k][j]:
                    pass
                else:
                    ans = "No"
                    break
print(ans)
"""

"""
h,w = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(h)]
print(list)
a = 0
ans = "Yes"
for i in range(h-1):
    for j in range(w-1):
        print("---------始点","(",i,",",j,")")
        for k in range(i+1,h):
            for l in range(j+1,w):
                print("終点","(",k,",",l,")")
                if list[i][j] + list[k][l] <= list[i][l] + list[k][j]:
                    pass
                else:
                    ans = "No"
                    break
print(ans)
"""
