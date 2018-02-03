#!/usr/bin/python3

'''

A program to attempt to create the same Bash program to play Tic-Tac-Toe,
but scripted in Python instead.
 - Working on using a dictionary to store board status and map it to 
   keys representing each square
 - Use time library to import the sleep function to build in appropriate delays
 - Use os library to interact with the console screen
 - Working to use functions and comments appropriately

10 Jan 2018
Ba$h3R

'''

''' Import the time and os modules to interact with the console '''
from time import sleep
import os

def welcomePlayer():
    ''' Initialize screen and set first player to X or O '''
    os.system("clear")
    print("\n")
    print("Welcome to Tic-Tac-Toe!")
    playerFlag = input("Would Player 1 like to be X or O: ")
    if (playerFlag == "x") or (playerFlag == "X"):
        playerFlag = 1
    elif (playerFlag == "o") or (playerFlag == "O"):
        playerFlag = 2
    return playerFlag

def R1C1(statusFlag):
    ''' Top left square '''
    switcher = {
        0:" ___|",
        1:" _X_|",
        2:" _O_|"
    }
    print(switcher[statusFlag], end='')

def R1C2(statusFlag):
    ''' Top middle square '''
    switcher = {
        0:"___|",
        1:"_X_|",
        2:"_O_|"
    }
    print(switcher[statusFlag], end='')

def R1C3(statusFlag):
    ''' Top right square '''
    switcher = {
        0:"___",
        1:"_X_",
        2:"_O_"
    }
    print(switcher[statusFlag])

def R2C1(statusFlag):
    ''' Middle left square '''
    switcher = {
        0:" ___|",
        1:" _X_|",
        2:" _O_|"
    }
    print(switcher[statusFlag], end='')

def R2C2(statusFlag):
    ''' Center square '''
    switcher = {
        0:"___|",
        1:"_X_|",
        2:"_O_|"
    }
    print(switcher[statusFlag], end='')

def R2C3(statusFlag):
    ''' Middle right square '''
    switcher = {
        0:"___",
        1:"_X_",
        2:"_O_"
    }
    print(switcher[statusFlag])

def R3C1(statusFlag):
    ''' Bottom left square '''
    switcher = {
        0:"    |",
        1:"  X |",
        2:"  O |"
    }
    print(switcher[statusFlag], end='')

def R3C2(statusFlag):
    ''' Bottom center square '''
    switcher = {
        0:"   |",
        1:" X |",
        2:" O |"
    }
    print(switcher[statusFlag], end='')

def R3C3(statusFlag):
    ''' Bottom right square '''
    switcher = {
        0:"   ",
        1:" X ",
        2:" O "
    }
    print(switcher[statusFlag])

def printBoard(boardStatus):
    ''' Call functions to print entire board '''
    os.system("clear")
    print("\n")
    R1C1(boardStatus["tl"])
    R1C2(boardStatus["tm"])
    R1C3(boardStatus["tr"])
    R2C1(boardStatus["ml"])
    R2C2(boardStatus["mm"])
    R2C3(boardStatus["mr"])
    R3C1(boardStatus["bl"])
    R3C2(boardStatus["bm"])
    R3C3(boardStatus["br"])

def initBoardStatus():
    ''' Initialize board status to blank '''
    boardStatus = {
        "tl":0,
        "tm":0,
        "tr":0,
        "ml":0,
        "mm":0,
        "mr":0,
        "bl":0,
        "bm":0,
        "br":0
    }
    return boardStatus

def printPlayer(playerFlag):
    ''' Print the player whose turn it is '''
    if playerFlag == 1:
        print("Player X")
    elif playerFlag == 2:
        print("Player O")
    else:
        print("Player flag error! Exiting...DONE.")
        exit()

def getMove():
    ''' Read the move '''
    playerMove = input("Please enter a move: ")
    return playerMove

def incrBoardStatus(playerFlag, playerMove, boardStatus):
    ''' Update board status dictionary based on player move '''
    if playerFlag == 1:
        boardStatus[playerMove] += 1
    elif playerFlag == 2:
        boardStatus[playerMove] += 2
    else:
        print("Player error! Exiting...DONE.")
        exit()
    return boardStatus

def switchPlayer(playerFlag):
    ''' Rotate player after each turn '''
    if playerFlag == 1:
        playerFlag = 2
    elif playerFlag == 2:
        playerFlag = 1
    else:
        print("Player error! Exiting...DONE.")
        exit()
    return playerFlag

def checkDraw(drawFlag, boardStatus):
    ''' Check if all squares are filled '''
    sum = 0
    for i in boardStatus.values():
        sum += i
    if sum >= 13:
        drawFlag = 1
    return drawFlag

def checkWin(winFlag, boardStatus):
    ''' Check if a winning move has been played '''
    if boardStatus["tl"] == boardStatus["tm"] == boardStatus["tr"] != 0:
        winFlag = 1
    elif boardStatus["ml"] == boardStatus["mm"] == boardStatus["mr"] != 0:
        winFlag = 1
    elif boardStatus["bl"] == boardStatus["bm"] == boardStatus["br"] != 0:
        winFlag = 1
    elif boardStatus["tl"] == boardStatus["ml"] == boardStatus["bl"] != 0:
        winFlag = 1
    elif boardStatus["tm"] == boardStatus["mm"] == boardStatus["bm"] != 0:
        winFlag = 1
    elif boardStatus["tr"] == boardStatus["mr"] == boardStatus["br"] != 0:
        winFlag = 1
    elif boardStatus["tl"] == boardStatus["mm"] == boardStatus["br"] != 0:
        winFlag = 1
    elif boardStatus["tr"] == boardStatus["mm"] == boardStatus["bl"] != 0:
        winFlag = 1
    else:
        winFlag = 0
    return winFlag

def validateMove(playerMove, boardStatus):
    ''' Check if the player is attempting to change an invalid square '''
    if boardStatus[playerMove] != 0:
        print("Invalid move! Exiting...DONE.")
        exit()

def main():
    ''' Main gameplay '''
    drawFlag = 0
    winFlag = 0
    playerFlag = welcomePlayer()
    boardStatus = initBoardStatus()
    printBoard(boardStatus)
    while drawFlag == 0 and winFlag == 0:
        print('')
        printPlayer(playerFlag)
        playerMove = getMove()
        validateMove(playerMove, boardStatus)
        boardStatus = incrBoardStatus(playerFlag, playerMove, boardStatus)    
        printBoard(boardStatus)
        playerFlag = switchPlayer(playerFlag)
        drawFlag = checkDraw(drawFlag, boardStatus)
        winFlag = checkWin(winFlag, boardStatus)
    printBoard(boardStatus)
    print('')
    print("Game complete! Thanks for playing!")
    x = input("Press ENTER to quit.")
    os.system("clear")

''' Execute main function '''
main()
