def LeiaMatrizLocal(sudokutxt):

    #abre o arquivo e cria a matriz
    try:
        arq = open(sudokutxt, 'r')
    except:
        return []

    mat=[]
    for linha in arq:
        lin = linha.split()
        if lin != []:
            mat += [lin]
        if len(lin) != 9 and lin != []:
            return []
    if len(mat) != 9:
        return []
    arq.close()

    #transforma os elementos de str para int
    for i in range(len(mat)):
        for j, el in enumerate(mat[i]):
            try:
                mat[i][j] = int(el)
            except:
                return []

    #checa consistências iniciais
   # if not TestaMatrizLida(mat):
    #    return[]

    #se deu tudo certo, retorna a matriz
    return mat

#print(LeiaMatrizLocal("sudoku1.txt"))


def EncontrarElemento(lista, digito):
    pos=[]
    for i, elemento in enumerate(lista):
        if elemento == digito:
            pos.append(i)
        
    return pos

#print(EncontrarElemento(l,0))


def EncontrarElementoLinha(Matriz,Linha,Digito):
    for i,elemento in enumerate(Matriz[Linha]):
        if elemento == Digito:
            return i
    return -1

#print(EncontrarElementoLinha(mat,6,7))


def EncontrarELementoColuna(Matriz,Coluna,Digito):
    for i in range(9):
        if Digito == (Matriz[i][Coluna]):
            return i
    return -1
        
#print(EncontrarELementoColuna(mat,8,0))


def ProcuraElementoQuadrado (Matriz, Linha, Coluna, Digito):
#Preciso delimitar os espaços dentro da matriz, de acordo com a Linha e a Coluna.
#A divisão por inteiro(3) "Cria" mini matrizes de 3 po 3. A multiplicação por (3) me diz a localização do primeiro digito dessa submatriz.
    pos_linha = (Linha//3) * 3
    pos_coluna = (Coluna//3) * 3
    for L in range(pos_linha, pos_linha + 3):    # Range(Start(Inclusivo, inicia no número indicado), Stop(Exclusivo para um antes do número indicado), Step)
        for C in range(pos_coluna, pos_coluna +3):
            if Matriz[L][C] == Digito:
                return (L,C)
    return (-1,-1)

#print(ProcuraElementoQuadrado(mat,5,5,0))


#Devolve True se a matriz lida Mat está com as casas já preenchidas com os valores corretos.
#Não há repetições na linha, na coluna ou no quadrado interno, se os elementos são de 0 a 9.

def TestaMatrizLida(Matriz):
    

#mat = LeiaMatrizLocal('sudoku5.txt')