# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O Programa vai perguntar o VALOR DA CASA, o SALARIO do comprador e em quantos ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder os 30% do Salário se exceder deve-se cancelar
# o empréstimo e comunicar o comprador.

# print('Seja Bem-vindo(a) ao Banco do Don')
# print('Você deseja realizar um empréstimo, certo? Precisamos de algumas informações para aprova-lo!')

# casa = float(input('Insira o valor da casa: R$'))
# sal = float(input('Insira aqui o Total de seu salário para calcularmos: R$'))
# print('1 ano: 12 meses, 2 anos: 24 meses, 3 anos: 36 meses, 4 anos: 48 meses, 5 anos: 60 meses.')
# ano = int(input(' O pagamento deste empréstimo deve acontecer em quantos meses? '))


# parcela = casa/ano 

# if parcela <= sal * 30/100:
#     print('Podemos realizar o empréstimo! As prestações serão de: {:.2f} durante {} meses.'.format(parcela, ano))
# else:
#     print('O valor não pode ser negociado, o valor que você pagará ao mês é maior que 30% de seu salário. As prestações seriam de: R${:.2f}'.format(parcela))


# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# Categoria de acordo com sua idade.
#  0 a 9 MIRIM
# 9  a 14 infantil
# 14 a 19 junior
# 19 a 25 senior
# 25 ++ é Master
# #
# from datetime import date
# atual = date.today().year
# n = int(input('Quantas datas de nascimento vamos testar hoje? '))
# nasc = int(input('Ano de Nascimento: '))
# idade = atual - nasc
# cont = 0 

 
# while cont != n:
#     if idade <= 9:
#         print('O Atleta tem {} anos de idade.'.format(idade))
#         print('Faz parte da equipe: Mirim')
#     elif idade > 9 and idade <= 14:
#         print('Faz parte da equipe: Infantil')
#         print('O Atleta tem {} anos de idade.'.format(idade))
#     elif idade > 15 and idade <= 19:
#         print('Faz parte da equipe: Júnior')
#         print('O Atleta tem {} anos de idade.'.format(idade))
#     elif idade > 20 and idade <= 25:
#         print('Faz parte da equipe: Sênior')
#         print('O Atleta tem {} anos de idade.'.format(idade))
#     else:
#         print('Faz parte da equipe: Master')
#         print('O Atleta tem {} anos de idade.'.format(idade))
#     cont = cont + 1
#     idade = atual - int(input('Ano de Nascimento: '))
# print('O Atleta tem {} anos de idade.'.format(idade))
# print('Fim do serviço!')


# ## Inserindo os lados de um triangulo, faça um programa que identifique que tipo de triangulo pode ser formado com
# ## Os dados inseridos:
# """
#     Equilátero = Todos os lados são iguais
#     Isóceles = dois lados são iguais
#     Escaleno = todos os lados são diferentes
# """
# n1 = float(input('Insira o valor da primeira reta: '))
# n2 = float(input('Insira o valor da segunda reta: '))
# n3 = float(input('Insira o valor da terceira reta: ')) 

# if n1 == n2 == n3:
#     print('Todos os lados são iguais, pode-se formar o Triângulo Equilátero.')
# elif n1 == n2 or n2 == n3 or n1 == n3:
#     print('Apenas dois lados são iguais, pode-se formar o Triângulo Isóceles.')
# else:
#     print('Todos os lados são diferentes, pode-se formar o Triângulo Escaleno.')



# Desafio 37 - faça ele
""""""

# Desafio 38-  Escreva um prorama que leia dois números inteiros e os compare, mostrando na tela uma mensagem
# o primeiro é um valor maior, o segundo é uum valor maior, ou não existe valor maior, são iguais.

# n1 = float(input('Insira um número: '))
# n2 = float(input('Insira outro número: '))

# if n1 > n2:
#     print('\nO primeiro número é maior!', n1, '!')
# elif n2 > n1:
#     print('\nO segundo número é maior!', n2, '!')
# else:
#     print('Não existe valor maior, eles são iguais! Olha só: ', n1, n2, '!')

# Desafio 39 - Faça um programa  que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# Se ele ainda vai se alistar, se é o ano de se alistamento, ou se já passou. o programa também deve mostrar o tempo
# que falta para o alistamento ou se ja passou, quantos anos está atrasado.

# from datetime import date
# atual = date.today().year
# nasc = int(input('Insira qual ano que você nasceu:  '))
# gen = input('O seu RG te identifica como Homem ou Mulher?')
# idade = atual - nasc
# atraso = idade - 18
# adiantado = 18 - idade


# if gen in ['H', 'Homem', 'homem', 'homi', 'cara', 'menino', 'Masculino','masculino','macho','h']:
#     alis = input('Você já se alistou? Responda com S ou N: ')
#     if idade > 18 and alis == 'N':
#         print('Você está atrasado! Fazem {} anos que deveria ter se alistado!'.format(atraso))
#     elif idade < 18:
#         print('Você ainda tem tempo, faltam {} anos para você se alistar. Fique atento.'.format(adiantado))
#     elif idade == 18:
#         print('É este ano! Corre!')
#     else:
#         print('Parabéns')
# else: 
#     print('Não precisa se alistar!')        


# Desafio 40 - notas e médias.

# ava = int(input('Insira quantas avaliações você teve no semestre: '))
# cont = 1
# soma = 0
# while cont <= ava:
#     n = float(input('Insira a nota da prova: '))
#     soma = soma + n
#     cont = cont + 1

# media = soma / ava

# if media < 3:
#     print('Reprovado! :( ')
# elif media >= 3 and media < 5:
#     print('Você está de recuperação! :S ')
# else:
#     print('Você está aprovado(a)! :D ')


# n = float(input('Insira a nota da prova, negativo p terminar: '))
# notas=[]
# while n >= 0:
#     notas = notas + [n]
#     n = float(input('Insira a nota da prova, negativo p terminar: '))

# media = sum(notas)/len(notas)

# if media < 3:
#     print('Reprovado! :( ')
# elif media >= 3 and media < 5:
#     print('Você está de recuperação! :S ')
# else:
#     print('Você está aprovado(a)! :D ')
