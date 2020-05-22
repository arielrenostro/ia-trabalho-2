# coding: utf-8
# 0 = false
# i = inicio
# f = fim

#from array import *
labirinto = [ ["i", 1, 0, "f"],
              [  2, 2, 0,   5],
              [  6, 7, 8,   2] ]

def main():
    print('----------------------------------------------------')
    print(' FURB 2020/01')
    print(' IA - Trabalho 2 - Questão 1')
    print(' Ariel, Bruno Gabriel Curbani, Gabriel Lepkoski')
    print('----------------------------------------------------')
    print(' Algoritmo A * para problema do labirinto ')
    print('----------------------------------------------------')
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if (labirinto[linha][coluna] == "i"):
                pontoPartida(linha,coluna)

def pontoPartida(linha, coluna):
    visitado = []
    retorno = []
    novo = []

    if (linha-1 >= 0 and labirinto[linha-1][coluna] != 0):
        retorno = proximo(visitado, linha-1, coluna)
    if (coluna-1 >= 0 and labirinto[linha][coluna-1] != 0):
        novo = proximo(visitado, linha, coluna-1)
        if(retorno != [] and novo != []):
            retorno = compara(retorno, novo)
        elif (novo != []):
            retorno = novo
    if (linha+1 < len(labirinto) and labirinto[linha+1][coluna] != 0):
        novo = proximo(visitado, linha+1, coluna)
        if(retorno != [] and novo != []):
            retorno = compara(retorno, novo)
        elif (novo != []):
            retorno = novo
    if (coluna+1 < len(labirinto[linha]) and labirinto[linha][coluna+1] != 0):
        novo = proximo(visitado, linha, coluna+1)
        if(retorno != [] and novo != []):
            retorno = compara(retorno, novo)
        elif (novo != []):
            retorno = novo
    #print(" caminho total: ", retorno)
    
def proximo(lista, linha, coluna):
    print(linha, coluna)
    lista.append([linha,coluna])
    if labirinto[linha][coluna] == "f":
        print("caminho para o f:", lista)
        return lista
    retorno = []
    novo = []
    try:
        if (not [linha-1,coluna] in lista and linha-1 >= 0 and labirinto[linha-1][coluna] != 0):
            retorno = proximo(lista, linha-1, coluna)
        if (not [linha,coluna-1] in lista and coluna-1 >= 0 and labirinto[linha][coluna-1] != 0):
            novo = proximo(lista, linha, coluna-1)
            if(retorno != [] and novo != []):
                retorno = compara(retorno, novo)
            elif (novo != []):
                retorno = novo
        if (not [linha+1,coluna] in lista and (linha+1) < len(labirinto) and (labirinto[linha+1][coluna] != 0)):
            novo = proximo(lista, linha+1, coluna)
            if(retorno != [] and novo != []):
                retorno = compara(retorno, novo)
            elif (novo != []):
                retorno = novo
        if (not [linha,coluna+1] in lista and (coluna+1) < len(labirinto[linha]) and (labirinto[linha][coluna+1] != 0)):
            novo = proximo(lista, linha, coluna+1)
            if(retorno != [] and novo != []):
                retorno = compara(retorno, novo)
            elif (novo != []):
                retorno = novo
        return []
    except:
        print("expection on proximo")
    
def compara(velho, novo):
    velhoCount = 0
    novoCount = 0
    for linha in range(len(velho)):
        if(isinstance(labirinto[velho[linha][0]][velho[linha][1]], int) ):
            velhoCount = velhoCount + labirinto[velho[linha][0]][velho[linha][1]]
    for linha in range(len(novo)):
        if(isinstance(labirinto[velho[linha][0]][velho[linha+0][1]], int) ):
            novoCount = novoCount + labirinto[velho[linha][0]][velho[linha+0][1]]
    print()
    if(novoCount < velhoCount):
        return novo
    return velho

if __name__ == '__main__':
    main()