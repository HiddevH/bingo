"""
Bingo
Play the Game Bingo the lazy way, just insert your card and the drawn numbers into the program.
The program will update the card for you.

by: Hidde van Heijst - github.com/HiddevH
"""

import numpy as np
def createBingoCard(card_shape: tuple= (5, 5)):
    """
    Creates a Bingo Card in given shape.
    :param card_shape: - the shape of the bingoCard (rows, columns)
    """

    rows = card_shape[0]  # Assign row shape
    columns = card_shape[1]  # Assign column shape
    bcard = np.zeros((rows, columns)) # Create a matrix shaped array (bingocard) filled with zeroes in given shape

    for i in range(rows):
        for n in range(columns):
            pos_number = int(input(f'Please give the number for position {i+1}, {n+1}: '))
            bcard[i,n] = pos_number  # insert given positional number into the bingocard
            print(f'\n{bcard}\n')

    return bcard


def checkDrawumber(bingocard, number):
    """
    Given a bingocard and drawn number, this function will check if drawn number occurs on the Bingocard. If so, it will mark the number with a zero.
    Zeroes are used as the numpy array is of type integer.
    """
    # Check if number is present, mark position of number with X
    if number in bingocard:
        x, y = np.where(bingocard == number)
        bingocard[x, y] = 0
    else:
        print('Not in here!')


def playBingo():
    """
    Main function of the script.
    Will ask user to give how many bingocards/rounds there are and allows player to fill in a card for each round.
    Will ask user for the shape of given card.

    When a number has been drawn, the user can insert this in the dialog, where the program will mark the drawn number if exists on user's card.
    """
    
    n_rounds = int(input('How many bingocards do you have?: '))
    card_shape = tuple(map(int, input('What shape does your card have (rows,columns): ').split(',')))  # Retrieve shape and conver to tuple

    # Build the bingocards
    bingocard = dict()
    for i in range(n_rounds):
        print(f'=== BingoCard {i+1} ===')
        bingocard[i] = createBingoCard(card_shape)  
    
    # Play the game for n rounds
    for i in range(n_rounds):
        print(f'=== BingoCard {i+1} ===')
        while True:
            draw_number = input('What number has been drawn? - Leave blank to stop: ')
            if draw_number == "":
                verify = input('Are you sure? Type "yes" to continue to the next card or quit if none available: ')
                if verify:
                    break
            else:
                checkDrawumber(bingocard[i], int(draw_number))
            print(f'\n{bingocard[i]}\n')


if __name__ == "__main__":
    playBingo()