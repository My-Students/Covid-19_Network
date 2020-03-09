import matplotlib.pyplot as plt
from networkx import nx

def Matrice(dizionario):
    matrice = []
    for i in range(0, len(dizionario)):
        riga = []
        for j in range(0, len(dizionario)):
            riga.append(0)
        matrice.append(riga)

    for i in range(0, len(dizionario)):
        contagiati = dizionario[str(i)]
        for j in range(0, len(contagiati)):
            matrice[i][int(contagiati[j])] = 1

    return matrice

def readData():
    dizionario = {}
    data = open('data.txt', 'r') 
    linee = data.readlines() 
    for line in linee:
        line=line.replace('\n','')
        contagiati = line.split(" ")
        dizionario[contagiati[0]] = contagiati[1:]
    data.close()
    return dizionario

def pazienti0(matrice):
    pazienti_zero= []
    for i in range(0, len(matrice)):
        malato = 0
        portatori = 0
        while (portatori < len(matrice) and malato == 0):
            if matrice[portatori][i] == 1 :
                malato = 1     
            portatori+=1
                                            
        if malato == 0:
            pazienti_zero.append(i)

    return pazienti_zero
        
def main(): 
    data = readData()
    matrice = Matrice(data)
    print (matrice)
    zero=pazienti0(matrice)
    print (zero)
    
if __name__ == "__main__":
    main()