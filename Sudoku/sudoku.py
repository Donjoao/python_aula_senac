def LeiaMatrizLocal(NomeArquivo):
 # retorna a matriz lida se ok ou uma lista vazia senão
 # abrir o arquivo para leitura
    #try:
    arq = open(NomeArquivo, "r")
   # except:
        #return [] # retorna lista vazia se deu erro
 # inicia matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
 # ler cada uma das linhas do arquivo
    i = 0
    for linha in arq:
        v = linha.split()
 # verifica se tem 9 elementos e se são todos entre '1' e '9'
# . . .
# transforma de texto para int
    for j in range(len(v)):
        mat[i][j] = int(v[j])
 # faz as consistências iniciais da matriz dada
 # . . .
    i = i + 1
 # fechar arquivo e retorna a matriz lida e consistida
    arq.close()
    return mat

mat = [9 * [0] for k in range(9)]
print(LeiaMatrizLocal("sudoku4.txt"))