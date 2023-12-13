produtos = ["AbD019 ", " abd141", "ADc101 ", "JpaD109 "]
texto = ""

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)
    print(produto) 
    

