# Implementation of Tic Tae Toe game in python

boardScreen = {'7': ' ', '8': ' ', '9': ' ',
               '4': ' ', '5': ' ', '6': ' ',
               '1': ' ', '2': ' ', '3': ' '}
player_details = {'X': 'player1', '0': 'player2'}
board_keys = []

for key in boardScreen:
    board_keys.append(key)


def displayBoard(board: dict):
    printBlankLine()
    print_element_In(board['7'], board['8'], board['9'])
    printHorizontal()
    printBlankLine()
    print_element_In(board['4'], board['5'], board['6'])
    printHorizontal()
    printBlankLine()
    print_element_In(board['1'], board['2'], board['3'])
    printBlankLine()


def printBlankLine():
    print("     |      |     ")


def print_element_In(arg1, arg2, arg3):
    print(f"  {arg1}  |   {arg2}  |  {arg3}  ")


def printHorizontal():
    print("_____|______|_____")


# main game functionality in this method

def game():
    player1 = input("Enter player1 name: ")
    print(player1)
    player2 = input("Enter player2 name: ")
    print(player2)
    player = player1
    turn = 'X'
    count = 0
    for r in range(10):
        displayBoard(boardScreen)
        print(player + " it's your turn " + turn + ". Which position you want to move?")

        move = input()

        if boardScreen[move] == ' ':
            boardScreen[move] = turn
            count += 1
        else:
            print("the selected place is full.\nDo you want to choose another move?")
            continue

        # Will check the player has won or not, for every move after 5 moves
        if count >= 5:
            if boardScreen['7'] == boardScreen['8'] == boardScreen['9'] != ' ':
                displayBoard(boardScreen)
                print(" Game Over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['4'] == boardScreen['5'] == boardScreen['6'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['1'] == boardScreen['2'] == boardScreen['3'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['1'] == boardScreen['4'] == boardScreen['7'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['2'] == boardScreen['5'] == boardScreen['8'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['3'] == boardScreen['6'] == boardScreen['9'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['7'] == boardScreen['5'] == boardScreen['3'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break
            elif boardScreen['1'] == boardScreen['5'] == boardScreen['9'] != ' ':
                displayBoard(boardScreen)
                print(" Game over \n")
                print("Bingo!!! " + player + " you won the game")
                break

        # If no one wins and the board is full, declare it as tie
        if count == 9:
            print(" Game is over \n")
            print(" It is TIE")
            break

        # change the player and turn after every move
        if turn == 'X' and player == player1:
            turn = '0'
            player = player2
        else:
            turn = 'X'
            player = player1

    # Will ask the player if they want to play again

    restart = input("Do you want to play again? (y/n)")
    if restart == 'y' or restart == "Y" or restart == "yes":
        for key in board_keys:
            boardScreen[key] = " "

        game()


if __name__ == '__main__':
    game()
