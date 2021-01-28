#
# @Andrea Mattone
#

from typing import List
#Per i colori della scacchiera
import colorama
from colorama import Fore, Style


#Classe che implementa la scacchiera
class GameBoard:

    #Costruttore, gli attributi della classe sono quelli contenuti nell'init
    def __init__(self, boardSize, player1, player2):
        #sarà una board quadrata
        self.rows = boardSize
        self.columns = boardSize

        #imposto i nomi dei player
        self.player1 = player1
        self.player2 = player2

        #Inizializzo l'oggetto che contiene la matrice
        self.mainLine = List[List[int]] #matrice
        self.mainLine = [] #la dichiaro vuota inizialmente per inizializzarla dopo

        #Inizializzo la scacchiera
        self.buildBoard()



    #Creazione della scacchiera, la valorizzo con i numeri
    def buildBoard(self):
        #Inizializzo la scacchiera
        for row in range(0,self.rows):
            self.mainLine.append([-1] * self.columns) #inserisco "-1" self.columns volte per ogni riga della matrice


        #print(self.mainLine)
        #inserisco i vari numeri in tutte le celle della matrice
        i = 1
        for row in range(0,self.rows):
            for col in range(0, self.columns):
                if(i<10):
                    t = "00" + str(i) #metto due zeri davanti ai numeri minori di 10
                    self.mainLine[row][col] = str(t)
                elif(i<100 and i>9):
                    z = "0" + str(i) #metto uno zero davanti ai numeri minori di 100
                    self.mainLine[row][col] = str(z)
                else:
                    self.mainLine[row][col] = str(i)
                i=i+1
        #print(self.mainLine)



    #Stampa la scacchiera su terminale
    #PER TOGLIERE I COLORI BASTA LEVARE QUA FORE.
    #PER FAR TORNARE A COME PRIMA
    #for row in range(0, self.rows):
    #   print self.mainLine[row]
    def printBoard(self):
        for row in range(0, self.rows):
            for col in range(0,self.columns):
                if self.mainLine[row][col] == " X ":
                    print(Fore.BLUE + self.mainLine[row][col] + " ", end='')
                elif self.mainLine[row][col] == " O ":
                    print(Fore.RED + self.mainLine[row][col] + " ", end='')
                else:
                    print(Fore.WHITE + self.mainLine[row][col] + " ", end='')
            print("\n")
        #for row in range(0, self.rows):
        #   print(self.mainLine[row])

    #Questa funzione prende come input la stringa contenente la coordinata inserita
    #dall'utente, e da questa estrae la posizione in matrice della coordinata stessa
    #se il numero fornito dall'utente non è accettabile oppure se una pedina è gia presente
    #in quella coordinata la funzione restituisce -1,-1 come coordinate, le coordinate esatte altrimenti
    def extractCoordinates(self,temp1):
        for row in range(0,self.rows):
            for col in range(0, self.columns):
                if(self.mainLine[row][col] == temp1): #se è occupata scorrendo la scacchiera non trova il numero, quindi -1,-1
                    return row, col
        return -1,-1


    #Funzioni di inserimento delle pedine all'interno della scacchiera
    #Inserisce la pedina in coordinate [x][y]
    def insertPlayer1pawn(self,x,y):
        self.mainLine[x][y] =" X "
    def insertPlayer2pawn(self,x,y):
        self.mainLine[x][y] =" O "


    #Verifico se i player hanno fatto dei punti
    # 0 punti per counter <=2
    # 2 punti per counter=3
    # 10 punti per counter=4
    # 50 punti per counter>=5
    def checkPlayer1points(self,player1):
        player1[1] = 0
        #Controllo se ha fatto punti in orizzontale
        for row in range(0,self.rows):
            counterO = 0
            for col in range(0, self.columns):
                if(self.mainLine[row][col] == " X "):
                    counterO=counterO+1
            if(counterO==3):
                player1[1]= player1[1] + 2
            elif(counterO==4):
                player1[1] = player1[1] + 10
            elif(counterO>4):
                player1[1]= player1[1] + 50
            else:
                player1[1] = player1[1]
        #Controllo se ha fatto punti in verticale
        for col in range(0,self.columns):
            counterV = 0
            for row in range(0, self.rows):
                if(self.mainLine[row][col] == " X "):
                    counterV=counterV+1
            if (counterV == 3):
                player1[1] = player1[1] + 2
            elif (counterV == 4):
                player1[1] = player1[1] + 10
            elif (counterV > 4):
                player1[1] = player1[1] + 50
            else:
                player1[1] = player1[1]

        #Controllo se ha fatto punti in diagonale

        #Mi salvo innanzitutto in due vettori le diagonali sinistre e destre
        max_col = len(self.mainLine[0])
        max_row = len(self.mainLine)
        cols = [[] for _ in range(max_col)]
        rows = [[] for _ in range(max_row)]
        fdiag = [[] for _ in range(max_row + max_col -1)]
        bdiag = [[] for _ in range(len(fdiag))]
        min_bdiag = -max_row + 1
        for x in range(max_col):
            for y in range(max_row):
                fdiag[x+y].append(self.mainLine[y][x])
                bdiag[x-y-min_bdiag].append(self.mainLine[y][x])
        #A questo punto faccio il check dei punteggi
        # fdiag -> diagonale /
        #print(fdiag)
        # bdiag -> diagonale \
        # print(bdiag)

        #Verifico la bdiag \
        for i in range(len(bdiag)):
            lenTmp = len(bdiag[i])
            z=0
            counterDf=0
            while z < lenTmp:
                #print(bdiag[i][z])
                if(bdiag[i][z]==" X "):
                    counterDf=counterDf+1
                z=z+1
            if (counterDf == 3):
                player1[1] = player1[1] + 2
            elif (counterDf == 4):
                player1[1] = player1[1] + 10
            elif (counterDf > 4):
                player1[1] = player1[1] + 50
            else:
                player1[1] = player1[1]

        #Verifico la fdiag /
        for i in range(len(fdiag)):
            lenTmp = len(fdiag[i])
            z=0
            counterDf=0
            while z < lenTmp:
                #print(fdiag[i][z])
                if(fdiag[i][z]==" X "):
                    counterDf=counterDf+1
                z=z+1
            if (counterDf == 3):
                player1[1] = player1[1] + 2
            elif (counterDf == 4):
                player1[1] = player1[1] + 10
            elif (counterDf > 4):
                player1[1] = player1[1] + 50
            else:
                player1[1] = player1[1]
    def checkPlayer2points(self,player2):
        player2[1] = 0
        # Controllo se ha fatto punti in orizzontale
        for row in range(0, self.rows):
            counterO = 0
            for col in range(0, self.columns):
                if (self.mainLine[row][col] == " O "):
                    counterO = counterO + 1
            if (counterO == 3):
                player2[1] = player2[1] + 2
            elif (counterO == 4):
                player2[1] = player2[1] + 10
            elif (counterO > 4):
                player2[1] = player2[1] + 50
            else:
                player2[1] = player2[1]
        # Controllo se ha fatto punti in verticale
        for col in range(0, self.columns):
            counterV = 0
            for row in range(0, self.rows):
                if (self.mainLine[row][col] == " O "):
                    counterV = counterV + 1
            if (counterV == 3):
                player2[1] = player2[1] + 2
            elif (counterV == 4):
                player2[1] = player2[1] + 10
            elif (counterV > 4):
                player2[1] = player2[1] + 50
            else:
                player2[1] = player2[1]

        # Controllo se ha fatto punti in diagonale

        # Mi salvo innanzitutto in due vettori le diagonali sinistre e destre
        max_col = len(self.mainLine[0])
        max_row = len(self.mainLine)
        cols = [[] for _ in range(max_col)]
        rows = [[] for _ in range(max_row)]
        fdiag = [[] for _ in range(max_row + max_col - 1)]
        bdiag = [[] for _ in range(len(fdiag))]
        min_bdiag = -max_row + 1
        for x in range(max_col):
            for y in range(max_row):
                fdiag[x + y].append(self.mainLine[y][x])
                bdiag[x - y - min_bdiag].append(self.mainLine[y][x])
        # A questo punto faccio il check dei punteggi
        # fdiag -> diagonale /
        # print(fdiag)
        # bdiag -> diagonale \
        # print(bdiag)

        # Verifico la bdiag \
        for i in range(len(bdiag)):
            lenTmp = len(bdiag[i])
            z = 0
            counterDf = 0
            while z < lenTmp:
                # print(bdiag[i][z])
                if (bdiag[i][z] == " O "):
                    counterDf = counterDf + 1
                z = z + 1
            if (counterDf == 3):
                player2[1] = player2[1] + 2
            elif (counterDf == 4):
                player2[1] = player2[1] + 10
            elif (counterDf > 4):
                player2[1] = player2[1] + 50
            else:
                player2[1] = player2[1]

        # Verifico la fdiag /
        for i in range(len(fdiag)):
            lenTmp = len(fdiag[i])
            z = 0
            counterDf = 0
            while z < lenTmp:
                # print(fdiag[i][z])
                if (fdiag[i][z] == " O "):
                    counterDf = counterDf + 1
                z = z + 1
            if (counterDf == 3):
                player2[1] = player2[1] + 2
            elif (counterDf == 4):
                player2[1] = player2[1] + 10
            elif (counterDf > 4):
                player2[1] = player2[1] + 50
            else:
                player2[1] = player2[1]


    #Verifico la vittoria dei player
    def checkPlayer1win(self,player1):
        if player1[1] >= 50:
            return False
        else:
            return True
    def checkPlayer2win(self,player2):
        if player2[1]>=50:
            return False
        else:
            return True
