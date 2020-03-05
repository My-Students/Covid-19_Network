# Covid-19_Network
Esercizio sui grafi orientati.

Scaricare il file data.txt.
Esso contiente i dati (inventati) di 200 contagiati dal virus Covid-19. Ciascun contagiato è identificato da un numero che va da 0 a 199.

Ad esempio le prime 5 righe del file:
'''
0
1 184 121 114 53
2 129 198 23
3
4 136 162 76
'''

vanno lette in questa maniera: il paziente 0 non ha contagiato nessuno, il paziente 1 ha contagiato i pazienti 184, 121, 114, 53 e così via...

Scrivere un programma python3 che legga il file data.txt. Per chi non si ricordasse come leggere i file ecco uno snippet di codice:
'''python
data = open('data.txt', 'r') 
lines = data.readlines() 
for line in lines: 
    #do something
data.close()
'''

Il programma deve costruire il dizionario delle adiacenze che corrisponde al grafo del contagio.
Usando le funzioni sviluppate nelle precedenti esercitazioni, creare la matrice di adiacenza.
Trovare i pazienti 0, ovvero coloro dai quali è partito il contagio!
