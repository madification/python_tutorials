import random

class Deck:
    cardOptions = list(range(2, 11))+(["Jack", "Queen", "King", "Ace"])
    cards = []

    def __init__(self) -> None:
        for i in range(4):
            self.cards = self.cards + self.cardOptions
    

    def shuffle(self, numTimes):
        oneHalf = []
        otherHalf = []
        for t in range(numTimes):
            oneHalf = self.cards[0:int(0.5*len(self.cards))]
            otherHalf = self.cards[int(0.5*len(self.cards)):len(self.cards)]

            halfSize = max(len(oneHalf), len(otherHalf))
            newOrder = []
            for c in range(halfSize):
                newOrder.append(oneHalf[c])
                newOrder.append(otherHalf[c])
            self.cards = newOrder            

    
    def combineDecks(self, deck):
        self.cards = self.cards + deck.cards


