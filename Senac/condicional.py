# If , Else e Elif
# Condições | a>b | a<b | a<=b | a>=b | a!=b | a==b | 

"""
a = False
print(type(a))

if a:
    print('Verdadeiro')
else:
    print('Falso')
"""

"""
n1 = 5
n2 = 12
if n1 > n2:
    print('n1 é maior que n2!')
else:
    print('n1 é menor que n2!')
"""

"""
nome = input('Insira um nome: ')
if nome == "João":
    print('é igual!')
else:
    print('é diferente!')"""


nome = input("Insira o nome do aluno: ")

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1+nota2+nota3)/3
print("A média de {} foi de: {:.2}".format(nome,media))

if media >= 7:
    print(nome, "está aprovado(a)!")
elif media <5:
    print(nome, "está reprovado(a)!")
else:
    print(nome, "Está de recuperação!")
    