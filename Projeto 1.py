# Projeto de Calculo de nervura
# Para calcular nervura eu preciso do tamanho do oposto da viga mais 0.40 cm de dobra, com esse valor total eu multiplico
# por 4,divido por 12 e multiplico por 1.1

# ferro = float(input('Espessura do ferro: '))
# oposto = float(input('Insira a metragem oposta do oposto: '))
# quantidade = int(input('Quantidade de nervura: '))
# nervura = ((oposto + 0.4) * 4) * quantidade
# barras = (nervura / 12) * 1.1
# print('Espessura do ferro: {} | Nervura em M: {} | Quantas barras de 12m: {:.2f}'.format(ferro, nervura, barras))


viga = float(input('Insira o tamanho da viga: '))
oposto = float(input('Qual o oposto? '))
esp_viga = float(input('Qual o vão do oposto? É 0.42 ou 0.49? '))

quant_viga = round(oposto / esp_viga)
print('\n A quantidade de vigas é: {:.2f}'.format(quant_viga))

tam_negativo = ((viga/3)+ 0.1)
print('\n O tamanho do negativo com a dobra de 0.10 é: {:.2f}'.format((tam_negativo)))

metros_ferro = quant_viga * tam_negativo
print('\n Vamos precisar de {:.2f}m de ferro.'.format((metros_ferro)))

quant_barras_ferro = (metros_ferro / 12) * 1.1
print('\n Serão necessárias {:.2f} barras de ferro.'.format(round(quant_barras_ferro)))
print('\n')

