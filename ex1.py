import random as r
lista = []

for item in range(20):
    lista.append(r.randrange(0,200))
    
def maiorValor(lista):
    return max(lista, key=int)

m = maiorValor(lista)
print(lista)
print(f'O maior numero eh {m}')
     