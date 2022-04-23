""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")


def clearDeck():
    # puts the number of cards (52) into the deck
    for location in range(NUMCARDS):
        cardLoc[location] == DECK


def showDeck():
    print("Location of all cards")
    print("#          Card             Location")
    card = 0
    for cardNum in cardLoc:
        rank = card % 13
        suit = int(card / 13)
        card = card + 1  # because card location starts from 0 in array

        displayRankName = ' '.join([rankName[rank], "of", suitName[suit]])
        displayLocation = playerName[cardNum]
        print(f"{card}    {displayRankName}            {displayLocation}")


def showHand(USER):
    print(" ")
    print("Displaying", playerName[USER], "hand:")
    for card in range(0, 51):
        if cardLoc[card] == USER:
            rank = card % 13
            suit = int(card / 13)
            displayRankName = ' '.join([rankName[rank], "of", suitName[suit]])
            print(displayRankName)


def assignCard(USER):
    keepGoing = True
    while keepGoing:
        card = random.randint(0, 51)
        if cardLoc[card] == DECK:
            cardLoc[card] = USER
            keepGoing = False


def main():
    clearDeck()

    for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)

    showDeck()
    showHand(PLAYER)
    showHand(COMP)


if __name__ == "__main__":
    main()
