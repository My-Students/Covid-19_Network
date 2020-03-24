import networkx as nx
import matplotlib.pyplot as plt


def caricaDati(nomeFile):
    data = open(nomeFile, 'r')
    lines = data.readlines()
    dict={}
    for line in lines:
        lineSplit = line.split(' ')
        chiave = int(lineSplit.pop(0))
        nodi = [int(n) for n in lineSplit]
        dict[chiave]=nodi
    data.close()
    return dict


def creaMatriceDaDict(dict):
    matrix = []
    for key, val in dict.items():
        colonna = [0 for dim in range(0, len(dict))]
        for link in val:
            colonna[link - 1] = 1
        matrix.append(colonna)

    return matrix


def stampaMatrice(matrix):
    for r in range(0, len(matrix)):
        print(" ")
        for c in range(0, len(matrix)):
            print(matrix[c][r], end=' ')


def stampaDict(dict):
    print("\n{")
    for key, val in dict.items():
        print(f"\t{key}: {val},")

    print("}")


def drawGrafo(dict):
    G = nx.Graph()
    for key, val in dict.items():
        G.add_node(key)
        for i in val:
            G.add_edge(int(key), int(i))
    print(f"\n{nx.info(G)}")
    nx.draw(G)
    plt.show()


def Elimina(lista):
     for i in lista:
         if lista.count(i) > 1:
             lista.remove(i)
             Elimina(lista)
     return lista


def trovaPazienteZero(dict):
    listaPazientiZero=[]
    for p in range(0, len(dict)): listaPazientiZero.append(trova(p, dict))
    return Elimina(listaPazientiZero)


def trova(find, dict):
    tro = False
    for key, val in dict.items():
        if find in val:
            tro = True
            return trova(key, dict)
    if tro == False: return find


def main():
    d = caricaDati("data.txt")
    #stampaDict(d)
    #m = creaMatriceDaDict(d)
    #stampaMatrice(m)
    #drawGrafo(d)
    lista = trovaPazienteZero(d)
    print(lista)



if __name__ == '__main__':
    main()