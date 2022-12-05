#先輩方に手伝ってもらった
import math
l = []
l2 = []
saidai = 0
for i in range(5):
    l.append(int(input()))
    l2.append(math.ceil(l[i]/10)*10)
    if l2[i]-l[i]  > l2[saidai]-l[saidai]:
        saidai = i
l2[saidai]=l[saidai]
print(sum(l2))