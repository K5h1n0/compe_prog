#pythoでの四捨五入のやり方は覚えないと行けない
# from decimal import Decimal, ROUND_HALF_UP

def roundup(kazu,keta):
    b = 10**(keta-1)
    a = kazu//b
    tmp = a * b
    print(a)
    print(tmp)
    if kazu - a >= 5:
        return a + 10
    else:
        return a


def roundup1(kazu,keta):
    if keta >= 2:
        keta -= 1
        kazu = kazu // 10 ** keta
        print(kazu)
    print("元々の数",kazu)
    print("一の位を取り出したい！")
    hikizann = kazu // 10 ** keta * 10 ** keta
    print("引くための数",hikizann)
    sonoketa = kazu - hikizann
    print("一の位", sonoketa)
    if sonoketa >= 5:
        return hikizann * 10 ** keta + 10 ** keta
    else:
        return hikizann * 10 ** (keta - 1)

x,k = map(int,input().split())
print(roundup1(x,k))