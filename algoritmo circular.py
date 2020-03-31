def main():
    valores = [[14, 0, 1, 0, 0, 0, 0], [16, 0, 2, 0, 0, 0, 0], [7, 0, 3, 0, 0, 0, 0], [9, 0, 4, 0, 0, 0, 0]] #tamanho, tempo, n° do processo, variavelde entrada, varialvel de saida, tempo de espera
    ordenar(valores)
    quantum = 6
    ttc = 3
    executar(valores, ttc, quantum)
    print("O tempo medio de espera dos processos é %.1f"%mediaDeEspera(valores))
    #turnProcessos(valores)
    #mprimirValores(valores)



def ordenar(valores):  # Ordena os processos pelo tempo de entrada
    for j in range(0, len(valores)):
        for i in range(0, len(valores) - 1):
            if valores[i][1] > valores[i + 1][1]:
                auxt = valores[i + 1]
                valores[i + 1] = valores[i]
                valores[i] = auxt


def executar( valores, ttc, quantum): #Simula a gerencia dos processos
    tempoT = 0
    tempoE = 0
    aux = 0
    bool = True
    # print(valores)
    for i in range(len(valores)):
        valores[i][5] =- valores[i][1]
    while aux <= len(valores):
        for i in range(len(valores)):
            bool = False
            if valores[i][0] > 0:
                valores[i][4] = tempoT
            if valores[i][0] > 0:
                valores[i][5] += valores[i][4] - valores[i][3]
            for j in range(quantum):
                if valores[i][0] > 0:
                    valores[i][0] -= 1
                    tempoE += 1
                    tempoT += 1
                    valores[i][3] = tempoT
                    bool = True
                else:
                    aux += 1
                    break

            bool2 = False
            for a in range(len(valores)):
                if valores[a][0] > 0:
                    bool2 = True
            if not bool2:
                aux += 1
                break
            if bool:
                for c in range(ttc):
                    tempoT += 1
                    #print(tempoT)

def mediaDeEspera(valores): #Retorna o valor medio do tempo de espera dos processos
    total = 0
    for i in range(len(valores)):
        total += valores[i][5]
    return total/len(valores)

def turnProcessos(valores): #Descobre o tempo de turnround dos processos
    descobreMaior(valores)
    for i in range(len(valores)):
        valores[i][6] = valores[i][3] - valores[i][1]

def imprimirValores(valores): #imprime valores de turnround dos processos
    for i in range(len(valores)):
        print('O tempo de turnround do processo %d é de %d' % (valores[i][2], valores[i][6]))

def descobreMaior(valores):
    maior = valores[0]
    for i in range(1,len(valores)):
        if valores[i]>maior:
            maior = valores[i]
    maior[3]+=maior[0]
    maior[0]=1



if __name__ == '__main__':
    main()
