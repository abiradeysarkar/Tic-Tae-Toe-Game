from array import *

boardScreen = {'7': ' ', '8': ' ', '9': ' ',
               '4': ' ', '5': ' ', '6': ' ',
               '1': ' ', '2': ' ', '3': ' '}


def displayBoard(board):
    #print(board['7'] + '|' + board['8'] + ' |' + board['9'])
    #print('-+-+-')
    #print(board['4'] + '|' + board['5'] + '|' + board['6'])
    #print('-+-+-')
    #print(board['1'] + '|' + board['2'] + '|' + board['3'])

    printBlankLine()
    printelementIn(' ', 'X', '')
    printHorizontal()
    printBlankLine()
    printelementIn('0','X','')
    printHorizontal()
    printBlankLine()
    printelementIn(' ', 'X', '')
    printBlankLine()



def printBlankLine():
    print("     |      |     ")


def printelementIn(arg1, arg2, arg3):
    print(f"  {arg1}  |   {arg2}  |  {arg3}  ")

def printHorizontal():
    print("_____|______|_____")
displayBoard(boardScreen)
