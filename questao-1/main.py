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
    visitado = [linha,"-",coluna]
    #prox.append([linha-1,coluna]
    try:
        if ((linha-1) > 0 and (labirinto[linha-1][coluna] != 0)):
            print('1')
            proximo(visitado, linha-1, coluna)
        if ((coluna-1) > 0 and (labirinto[linha][coluna-1] != 0)):
            print('2')
            proximo(visitado, linha, coluna-1)
        if ((linha+1) < len(labirinto) and (labirinto[linha+1][coluna] != 0)):
            print('3')
            proximo(visitado, linha+1, coluna)
        if ((coluna+1) < len(labirinto[linha]) and (labirinto[linha][coluna+1] != 0)):
            print('4')
            proximo(visitado, linha, coluna+1)
    except:
        print("except on pontoPartida")
        #return []
    
def proximo(lista, linha, coluna):
    print(linha, coluna)
    lista.append([linha,"-",coluna])
    try:
        if ( not [linha-1,"-",coluna] in lista and linha-1 > 0 and labirinto[linha-1][coluna] != 0):
            proximo(lista, linha-1, coluna)
            print('1v')
        if ( not [linha,"-",coluna-1] in lista and coluna-1 > 0 and labirinto[linha][coluna-1] != 0):
            proximo(lista, linha, coluna-1)
            print('2v')
        if ( not [linha+1,"-",coluna] in lista and (linha+1) < len(labirinto) and (labirinto[linha+1][coluna] != 0)):
            proximo(lista, linha+1, coluna)
            print('3v')
        if ( not ([linha,"-",coluna+1] in lista) and (coluna+1) < len(labirinto[linha]) and (labirinto[linha][coluna+1] != 0)):
            proximo(lista, linha, coluna+1)
            print('4v')
    except:
        print("expection on proximo")
        #return []
    
if __name__ == '__main__':
    main()