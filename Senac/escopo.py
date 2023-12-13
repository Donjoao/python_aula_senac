# Escopo / Variavel Global
# As variaveis Globais, aquelas que são criadas direto no corpo do código tem propriedade sobre as variaveis criadas dentro dos escopos.
# Exemplo:

x = "Senac" # Variavel Global

def mostrar():
    print(x)
mostrar()

x = "josé"

def MostrarNome():
    x = "SENAC"
    print(MostrarNome)
