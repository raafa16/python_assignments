from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")


def main():
    # clearDeck()

    for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)

    # showDeck()
    # showHand(PLAYER)
    # showHand(COMP)
