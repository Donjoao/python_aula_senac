'''
                                                            Lista de Exercícios

#Exercicio 1
numb1 = float(input("Insira 1 número: "))
numb2 = float(input("Insira 2 número: "))
soma = numb1 + numb2
print("A soma dos valores é:{:.2f} ".format(soma))



#Exercicio 2
n1 = float(input("Insira 1 número: "))
n2 = float(input("Insira 1 número: "))
soma = n1 + n2
div = n1 / n2
mult = n1 * n2
sub = n1 - n2

print('A Soma desses números é: ', soma)
print('A Divisão desses números é: ', div)
print('A Multiplicação desses números é: ', mult)
print('A Subtração desses números é: ', sub)


#Exercício 3 
distancia_total = float(input("Insira a distância total percorrida pelo automóvel em km: "))
combustivel_gasto = float(input("Insira o total de combustível gasto em litros: "))

consumo_medio = distancia_total / combustivel_gasto
print(f"O consumo médio do automóvel é de {consumo_medio:.2f} km/l.")



#Exercício 4
nome = input('Insira o nome do vendedor: ')
salario = int(input(f'Qual o salário em R$ de {nome}: '))
total_vendas = int(input(f'Valor em R$ vendido por {nome}: '))
comissao = 0.15 * total_vendas
salario_final = salario + comissao
print(f"{nome} possui o salário de: {salario}, com a comissão receberá o total de: {salario_final}!")


#Exercício 5 
aluno_nome = input('Qual nome do aluno? ')
avaliacoes = int(input('Insira quantas avaliações teve no semestre: '))
cont = 1
soma = 0
while cont <= avaliacoes:
    n = float(input('Insira a nota da prova: '))
    soma = soma + n
    cont = cont + 1

media = soma / avaliacoes
print(f'A média de {aluno_nome} foi: {media:.2f}')


#Exercíco 6
n1 = input('Insira um valor para A: ')
n2 = input('Insira um valor para B: ')

print(f'Valores antes de trocar: A: {n1}, B:{n2} ')
# Trocar os valores usando uma variável temporária
temp = n1
n1 = n2
n2 =  temp

print(f"Agora alterados A:{n1} B:{n2}")


#Exercício 7

print("Vamos converter temperatura de Graus Celsius para Graus Fahrenheit!")
celsius = float(input('Insirao valor de Graus Celsius para conversão: '))
fahren = (9*celsius+160)/5
print(f'º{celsius}C convertidos para Fahrenheit são: º{fahren}F')



#Execício 8

dolar_cota = float(input("Qual a cotação do dólar hoje para Real: "))
dolar_dispo = float(input("Insira quantos dólares você tem disponível: "))

real = dolar_dispo * dolar_cota

print(f"O valor em reais é R$ {real:.2f}")



#Exercício 9
valor_caixa = float(input('Insira o valor que foi depositado no caixa: '))
rendimento = valor_caixa * 0.007
novo_valor = rendimento + valor_caixa
print(f"Após um mês de rendimento o valor em caixa é de : R${novo_valor:.2f}")



#Exercício 10
compras_total = float(input('Insira o valor total das compras em R$: '))
parcelamento = compras_total/5
print(f"Serão 5 parcelas de R${parcelamento:.2f}")



#Exercício 11
valor_prod = float(input('Valor do produto: '))
acrescimo = float(input('Insira o acréscimo em % '))
conversao = valor_prod * (1 + acrescimo/100)
novo_valor = conversao

print(f'O produto será vendido por: {novo_valor:.2f}')



#Exercício 12

custo_fabrica = float(input('Insira o valor do carro na fábrica: R$'))

imposto_distribuidor = custo_fabrica * (28/100)
imposto_imposto = custo_fabrica * (45/100)
custo_consumidor = custo_fabrica + imposto_distribuidor + imposto_imposto

print(f"O valor do carro somado aos impostos é de: R${custo_consumidor:.2f}")

#Exercício 13

n1 = float(input("Insira um número: "))
if n1 > 10:
    print('Este número é maior que 10!')
elif 10 == 10:
    print("Esse é o número 10!")
else:
    print('Esse número é menor que 10!')'''

#Exercício 14
"""a1 = float(input('Insira um valor para A1: '))
a2 = float(input('Insira um valor para A2: '))

if a1 > a2:
    print('a1 é maior que A2!')
else:
    print('a2 é maior que A1!')
"""

""""
#Exercício 15
numero = float(input("Insira um número: "))
if numero > 100 and numero < 200:
    print("O número está entre 100 e 200!")
elif numero < 100:
    print("O número é menor que 100!")
else:
    print("O número é maior que 200!")


#Exercício 16
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
    """



#Exercício 17
"""numeros = []
for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    #print(numeros)
contador = 0
for x in numeros:
    if 10 <= x <= 150:  
        contador += 1
print(f"Número(s) no intervalo entre 10 e 150 (inclusive): {contador}")
numeros.sort()
print(numeros)
"""


#Exercício 18
"""idade = []
for i in range(15):
    numero = int(input(f"Digite a idade do {i + 1}º: "))
    idade.append(numero)
    print(idade)
    if numero >= 18:
        print("Maior de Idade!")
    else:
        print("Menor de idade!")"""

#Exercício 19
total_homens = 0
total_mulheres = 0
total_naocis = 0

for i in range (5):
    nome = input(f"Digite o nome do {i+1}º: ")
    sexo = input(f"Digite o sexo de {nome} (M para masculino, F para feminino, N  não se identifica com gêneros CIS): ").upper()
    if sexo == 'M':
        print(f"{nome} é homem.")
        total_homens += 1
    elif sexo == 'F':
        print(f"{nome} é mulher.")
        total_mulheres += 1
    else:
        print(f"{nome} não se identifica com gêneros CIS.")
        total_naocis += 1

print(f"Total de homens é: {total_homens}")
print(f"Total de mulheres é: {total_mulheres}")
print(f"Total de não-cis é: {total_naocis}")


#Exercício 20
