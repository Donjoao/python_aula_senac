""" Basico de Variaveis
str = "textos"
int = 10
float = 10.5
boolean = true/false

#inserindo valor em variavel.
nome = 'jose'
print(nome)
#mostrando o tipo da variavel.
print(type(nome))
#quantos caracteres na variavel.
print(len(nome))
#Altera para MAIUSCULA a variavel, se String.
print(nome.upper())
# For.
for x in nome:
    print(x)

print(nome[5::])
"""
"""a,b,c = 40,35,10
print(type(a))

print(a,b,c)
a = "João"
print('Variavel "A" alterada, agora ela é: ')
print(type(a))
print(a,b,c)
a = 3.5
print('Variavel "A" alterada, agora ela é: ')
print(type(a))
print(a,b,c)
a = 40
print('Variavel "A" alterada, agora ela é: ')
print(type(a))
print(a,b,c)
"""
# É possível alterar o valor e type da variavel e retornar como se nada tivesse acontecido.

nomeCompleto = "João Gabriel de Macedo Aquino Santos"

print(nomeCompleto[0:10])# Da primeira posição até uma anterior à 10.
print(nomeCompleto[-1])  # A ultima posição.
print(nomeCompleto[3:10])# Da terceira à décima.
print(nomeCompleto[5::]) # Da quinta posição à última.
print(nomeCompleto[-6::])# Da -6 posição à última.tw


cpf = ("47973008845")
print(cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9::]) # Como adicionar formatação utilizando os campos de texto de uma var.
