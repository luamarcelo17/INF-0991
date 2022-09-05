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
#comentário c1
#comentário c2
#comentário C5