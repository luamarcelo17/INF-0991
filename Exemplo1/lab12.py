//comentário teste 1
//comentário teste 2
def desenhar(listaNum, maior):
    for i in range(maior+2):
        if i == 0 or i == (maior+1):
            print('.'*(len(listaNum)+2))
        else:
            print('.', end='')
            for j in range(len(listaNum)):
                if i-1 + listaNum[j] >= maior:
                    print('|', end='')
                else:
                    print(' ', end='')
            print('.')


def bublleSort(listaNum, maior):
    desenhar(listaNum, maior)
    troca = False
    #print("Original: ", listaNum)
    for j in range(len(listaNum)-1):
    #for j in range(len(listaNum)-1,0,-1):
        for i in range(len(listaNum)-1):
            if listaNum[i] > listaNum[i+1]:
                troca = True
                temp = listaNum[i]
                listaNum[i] = listaNum[i+1]
                listaNum[i+1] = temp
            if troca:
                #print(listaNum)
                desenhar(listaNum, maior)
            troca = False
        #if troca:
        #    desenhar(listaNum, maior)
            #print()
        #print(listaNum)
        troca = False


maior = int(listaStr[0])
for n in listaStr:  # converte string em inteiro
    num = int(n)
    listaNum.append(num)
    if num > maior:
        maior = num

bublleSort(listaNum, maior)
