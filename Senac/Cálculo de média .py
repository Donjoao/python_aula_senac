#tenstando o FOR e While e If tudo num só
from statistics import mean
posicao = 1
notas = [] 
soma = 0
while True:
    ra = int(input('Insira o RA do aluno: '))
    if ra == 0:
        print("Agradecemos por ter utilizado nosso sistema! :D")
        break
    quant_avaliacoes = int(input(f'Quantas avaliações {ra} realizou? '))
    for posicao in  range (quant_avaliacoes):
        avaliacoes = float(input(f'Insira o valor da {posicao + 1}º nota: '))
        notas.append(avaliacoes)
    soma_notas= mean(notas)
    if soma_notas >= 6:
        print(f'A média final de {ra} foi: {soma_notas:.2f}, APROVADO(A)!')
    elif soma_notas < 5:
        print(f'A média final de {ra} foi: {soma_notas:.2f}, REPROVADO(A)!')
    else:
        print(f'A média final de {ra} foi: {soma_notas:.2f}, RECUPERAÇÃO(A)!')
    print('Digite 0 para encerrar o calculo de média! :D')