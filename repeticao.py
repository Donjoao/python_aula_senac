#Comandos de repetição
"""for x in range(5,11):
    print(x)

listanomes = ["Maria", "Ana", "Pedro", "João"]
for x in listanomes:
    print(x)
numeros = (3,6,4,9)
soma = 0
for x in numeros:
    soma += x
    print(soma) #Mostra a soma toda vrez que passa pelo for
print(soma)
i=0
while i<10:
    print(i)
    i+=1
lista = ["a","b","c","d","e","f"]
i=0
while i<len(lista):
    print(i, " - ", lista[i])
    i+=1


for x in listaCarros:
    print(x)

i = 0 

while i < len(listaCarros):
        if listaCarros[i] == "Omega":
            print(i, '-', listaCarros[i])
            break
        i = i+1

i = 0

while i<len(listaCarros):
    print(i, '-', listaCarros[i])
    if listaCarros[i] == "Omega":
        break
        
    i = i+1

i = 0
for x in listaCarros:
    if x == "Omega":
        continue
    print(x)

while i <len(listaCarros):
    print(i, "-", listaCarros)
    if listaCarros[i] == "Omega":
        break
    i = i + 1

while i <len(listaCarros):
    print(listaCarros[i])
    i = i + 1

print(listaCarros)



#Exercício para identificar em que posição está o Mustang dentro da lista, depois criar uma segunda lista com os objetos  do Mustang em diante.
listaCarros = ["Opala", "Chevelle", "Mustang", "Omega", "Astra" ,"Fusca", "Uno com escada", "Kadetásso"]
listaNovaCarros = []
listaCarros.sort()
i = 0
while i <len(listaCarros):
    print(i, "-", listaCarros[i])
    if listaCarros[i] == "Mustang":
        break
    i = i + 1

while i <len(listaCarros):
    listaNovaCarros.append(listaCarros[i])
    i = i + 1

print(listaCarros)
print(listaNovaCarros)
"""

#conversão de Tupla em list
tuplafrutas = ('frutaa','frutab','frutac')
print(type(tuplafrutas))
x = list(tuplafrutas)
print(type(x))
tuplafrutas = tuple(x)
print(type(tuplafrutas))