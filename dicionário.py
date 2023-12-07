# Criando um dicionário
"""usuario = {
    "nome" : "joão",
    "sobrenome" : "Aquino",
    "fone" : 1298771043,
    "email" : "santos.jgma@gmail.com"
}

print(usuario["nome"], usuario["fone"]) # Apresentando o que tem em seus campos
      
nome = "joão"
print(nome.upper())
print(type(usuario["nome"])) # Apresentando o tipo da variavel dentro do dicionário
"""

"""produto = {
    "nome" : "camiseta", #Criando a KEY "NOME" e adicionando a ela as propriedades a partir do dois pontos : "Camiseta" é sua propriedade
    "cores" : ["branca","preto","cinza"], #Criando lista dentro de um dicionário
    "tamanhos" : ["P","M","G","XG"] #Criando lista dentro de um dicionário
}

print(produto)
produto.update({"nome" : "shrots"}) # Redefiniu a variavel "camiseta" para "shorts"
produto.update({"marca" : "HD"}) #Gerou uma nova variavel dentro do dicionário
print(produto)


print(produto["cores"][0]) #Printando o produto, especificamente a key(cores) especificamente a posição(0)
print(produto["tamanhos"][2]) #Printando o produto, especificamente a key(tamanhos) especificamente a posição(2)
produto["tamanhos"] = "XXG" # CUIDADO dessa forma transformo uma lista em uma única string
print(produto)

produto["tamanhos"] = ["P","M","G","XG"] #Inserindo o valor de lista a Key Tamanhos do dicionário produto 
print(produto)

produto["tamanhos"].append("XXG")# Para adicionar str 
produto["cores"].pop() #para remover o último da lista ou (apontar o campo que desejo remover)
print(produto)
produto["marca"] = ["HD", "Samsung"]
print(produto["marca"])
produto["marca"][0] = "SSD" #Alterando a propriedade da key marca na posição 0.
print(produto["marca"])
produto["marca"].append("Burley")
print(produto["marca"])
produto.sort()
print(produto["marca"])"""

produtos = {
    "cocalata" : {
        "quantidade" : "250ml",
        "valor" : 5.00
    },
    "guarana" : {
        "quantidade" : "350ml",
        "valor" : 6.00
    },
    "coxinha" : {
        "tamanho" : "medio",
        "valor" : 5.00
    }
}
print(produtos)
produtos["cocalata"]["quantidade"] = ["400ml", "250ml", "210ml",]
produtos["coxinha"]["tamanho"] = ["pequena", "media", "grande", "larica"]
produtos["coxinha"]["valor"] = [5.00 , 6.00, 7.50, 8.50]
produtos.update({
    "café" {
        "tipo" : "torrado"
    }
})
print(produtos)
