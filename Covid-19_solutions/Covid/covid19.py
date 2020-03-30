
def readFile(): #Lettura del file 
    data = open("C:\Users\singh\OneDrive\Desktop\Karni\TPIST\Python\Covid\dati.txt", 'r')  # Carico il testo in data
    
    lines = data.readlines()
    virtual_File = {}
    
    for line in lines:
        elements = line.split(' ')
        kay  = elements[0]
        for v in elements:
            if(v != 0):    
                value.append(v)
        virtual_File[kay] = value

    data.close()
    return virtual_File

def dirtToMatrix(virFile):
    matrix = []

    for key, value in dict.items():  # Posiziono un "1" dove i due nodi si collegano
        matrix[key]
        for l in value:
            matrix[key][l] = 1

    return matrix



def pazZero(virMatrix):   # Cerca il paziente zero controllando la riga del paziente per vedere se è stato infetto da altro
    catturato = True
    list_Zero = []
    for r in len(virMatrix):
        for c in len(virMatrix):
            if(virMatrix[r][c]==0):
                catturato = True 
            
            if(catturato == True): # le la riga del paziente è pulita, allora è il paziente zero
                list_Zero.append(r)
    
    return list_Zero
                

if __name__ == "__main__":
    
    
    matrice=dirtToMatrix(readFile())
    print(pazZero(matrice))
