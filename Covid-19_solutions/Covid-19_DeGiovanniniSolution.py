"""
Alessia De Giovannini
4°A ROB
1) Il programma deve costruire il dizionario delle adiacenze che corrisponde al grafo del contagio.
2) Usando le funzioni sviluppate nelle precedenti esercitazioni, creare la matrice di adiacenza.
3) Trovare i pazienti 0 (per usare un termine tanto in voga tra i media), ovvero coloro dai quali è partito il contagio!
"""
import matplotlib.pyplot as plt
from networkx import nx

def read():
    data = open('data.txt', 'r') 
    lines = data.readlines() 
    diz = {}
    for line in lines:
        campi = line.replace('\n', '').split(" ")
        diz['nodo ' + campi[0]] = campi[1:]
    data.close()
    return diz

def toMatrice(diz):
    matr = []
    for i in range(0, len(diz)):
        vet = []
        for j in range(0, len(diz)):
            vet.append(0)
        matr.append(vet)

    for i in range(0, len(diz)):
        adiacenze = diz['nodo ' + str(i)]
        for j in range(0, len(adiacenze)):
            matr[i][int(adiacenze[j])] = 1
    return matr

def paz0(matr):
    for i in range(0, len(matr)):
        troj = False
        portatore = False
        for j in range(0, len(matr)):
            if matr[i][j] != 0:
                portatore = True
        if portatore:
            k = 0
            while (k < len(matr) and troj == False):
                if matr[k][i] == 0 :
                    k = k + 1
                else:
                    troj = True
            if troj == False:
                print(i)
        i+=1
        

def main(): 
    diz = read()
    matr = toMatrice(diz)
    paz0(matr)
    

if __name__ == "__main__":
    main()