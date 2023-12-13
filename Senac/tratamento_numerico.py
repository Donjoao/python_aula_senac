faturamento = 1500
custo = 500
lucro = faturamento - custo
print(f'o lucro foi de:{lucro:,.2f}')# apresentando ponto(,) como divisor da casa decimal e o porcentagem após a 2 casa decimal

margem = lucro/faturamento
print(f'A margem foi de: {margem:.1%}') # apresentando ponto(.) como divisor da casa decimal e o porcentagem após a 1 casa decimal

#Dica para conversão para modelo de moeda brasileiro

texto_lucro = f"R${lucro:_.2f}" #Adiciona R$ a variavel e transforma o divisor da casa decimal em _ e permanece aparecendo 2 casa decimais.
texto_lucro = texto_lucro.replace(".",",").replace("_", ".") # altera o valor de . por , e o valor de _ por .

# O python tem a limitação de não cosneguir alterar valores simultaneamentes, a = b e b = a não funcionam, é necessario uma variavel temporaria, como o c
# que nesse exemplo utilizado o _ por ser a 3º opção para conseguir estacionar o valor que será ocupado pela solicitação.
print(f"o lucro foi de {texto_lucro}")
