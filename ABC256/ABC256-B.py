n = int(input())
l = list(map(int, input().split())) 
lista = []
b = 0
for i in range(n):
    lista.append(1)
    for j in range(len(lista)):
        lista[j] = lista[j]+l[i]
for i in range(n):
    if lista[i] > 4:
        b = b + 1
print(b)