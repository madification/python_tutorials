import card

from play_actions import actions


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        self.score = 0

    def play(self) -> actions:
        if (card.computeScore(self.hand) == 21):
            return actions.WIN
        elif(card.computeScore(self.hand) < 17):
            return actions.HIT
        elif(card.computeScore(self.hand) > 21):
            return actions.BUST
        elif(card.computeScore(self.hand) >= 17):
            return actions.STAY
        else:
            print("Error selection player action: issue with player hand or computing score")    
        pass
    

    def receiveCard(self, card):
        self.hand.append(card)

    