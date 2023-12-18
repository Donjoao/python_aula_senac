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

print(LeiaMatrizLocal("sudoku1.txt"))