#
# @Andrea Mattone
# Progetto python per l'esame di IUM-TWEB
#
# Tic-Tac-Toe con campo da gioco NxN
#
from game_board import GameBoard
import colorama
from colorama import Fore, Style




def startGame(mGb):
    myGameBoard = mGb
    gameBool = True #se è true continu a giocare

    # All'interno di questo while si svolgerà tutta la fase di gioco
    while gameBool:

        # TURNO GIOCATORE 1
        print("\n")
        print("--------------------------------------------------------")
        print("Punteggio di " + player1[0] + " :" + player1[1].__str__())
        print("Punteggio di " + player2[0] + " :" + player2[1].__str__())
        print("TURNO PLAYER: " + player1[0])
        print("\n")
        #stampo lo stato attuale della scacchiera
        myGameBoard.printBoard()

        # Fase di gioco del player 1
        x = -1
        y = -1
        while (x == -1 and y == -1):
            temp1 = input(">>> " + player1[0] + " inserisci il numero della casella in cui vuoi inserire [X]: ")
            x, y = myGameBoard.extractCoordinates(temp1)
            if (x == -1 and y == -1):
                print("\nErrore: Inserisci una coordinata accettabile.")
        myGameBoard.insertPlayer1pawn(x, y)
        print("--------------------------------------------------------")
        #Verifico se il player 1 con questa mossa ha fatto dei punti
        #Se ne ha fatti aggiorno lo stato dei punti
        #successivamente verifico se il player 1 ha vinto
        myGameBoard.checkPlayer1points(player1)
        gameBool = myGameBoard.checkPlayer1win(player1)






        if gameBool == True: #ovvero se il player 1 non ha vinto durante questo turno
            # TURNO GIOCATORE 2
            print("\n")
            print("--------------------------------------------------------")
            print("Punteggio di " + player1[0] + " :" + player1[1].__str__())
            print("Punteggio di " + player2[0] + " :" + player2[1].__str__())
            print("TURNO PLAYER: " + player2[0])
            print("\n")
            myGameBoard.printBoard()
            # Fase di gioco del player 1
            x = -1
            y = -1
            while (x == -1 and y == -1):
                print("\n")
                temp1 = input(">>> " + player1[0] + " inserisci il numero della casella in cui vuoi inserire [O]: ")
                x, y = myGameBoard.extractCoordinates(temp1)
                if (x == -1 and y == -1):
                    print("\nErrore: Inserisci una coordinata accettabile.")
            myGameBoard.insertPlayer2pawn(x, y)
            print("--------------------------------------------------------")
            myGameBoard.checkPlayer2points(player2)
            gameBool = myGameBoard.checkPlayer2win(player2)



    #Se arrivo qua uno dei due player ha vinto perchè sono uscito dal while
    #Gestisco la vittoria
    if player1[1]>=50:
        winnerPlayer = player1
    else:
        winnerPlayer = player2

    print("HA VINTO " + winnerPlayer[0] + "!!!")



#Funzione adibita ad ottenere dall'utente la dimensione della scacchiera e i nomi dei giocatori
def getBoardAndGameInfo():
    # Chiedo all'utente di inserire la dimensione della scacchiera, la funzione inputp permette di inserire
    # dati da scacchiera (scanf del c)
    boardSize = int(input("Inserire la dimensione della scacchiera [valore minimo = 3]: "))


    # La dimensione minima della scacchierà dovrà essere 3x3, quindi se l'utente ne inserisce una minore imposto
    # in automatico a 3
    if (boardSize < 3):
        boardSize = 3

    #Chiedo all'utente il nome dei giocatori finchè non ne inseriscono uno valido, ovvero qualsiasi nome
    #che non sia la stringa vuota, i due giocatori non possono avere lo stesso nome
    while True:
        player1 = input("Inserire il nome del Giocatore 1 [X]: ")
        if(len(player1)!=0): #se è valido allora esco dal while
            break
    while True:
        player2 = input("Inserire il nome del Giocatore 2 [O]: ")
        if(len(player2)!=0 and player2!=player1):
            break
    return boardSize, player1, player2





#Entry point del programma
if __name__ == "__main__":
    boardSize = None



    #player1 e player2 sono due array contenenti come campi il nome del giocatore e il suo punteggio
    #durante la partita
    player1 = [None, 0]
    player2 = [None, 0]

    print("Tic-Tac-Toe")
    print("@author Andrea Mattone\n\n")

    #Ottengo dal/dai giocatore/i le informazioni sulla partita, ovvero la dimensione della scacchiera
    #e i nomi dei players
    boardSize, player1[0], player2[0] = getBoardAndGameInfo()
    ##print(boardSize, player1, player2)

    print("Che il gioco abbia inizio!")
    print("\n")

    #Inizializzo il gioco costruendo la GameBoard traite la classe game_board
    myGameBoard = GameBoard(boardSize,player1,player2)
    #print(myGameBoard.mainLine[3][2])


    #Inizio il gioco
    startGame(myGameBoard)



