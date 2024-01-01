from play_actions import actions


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        self.score = 0
        self.lastAction = actions.WAITING_FOR_GAME

    def play(self) -> actions:
        if (self.computeScore(self.hand) == 21):
            return actions.WIN
        elif(self.computeScore(self.hand) < 17):
            return actions.HIT
        elif(self.computeScore(self.hand) > 21):
            return actions.BUST
        elif(self.computeScore(self.hand) >= 17):
            return actions.STAY
        else:
            print("Error selection player action: issue with player hand or computing score")    
        pass
    

    def receiveCard(self, card):
        self.hand.append(card)

    
    def computeScore(self, hand) -> int:
        score = 0
        aces = []
        for c in hand:
            if c.type == "Ace":
                aces.append(c)
                continue
            else:
                score = score + c.value

            
        if len(aces) == 1:
            if score + 11 > 21:
                score = score + 1
            else:
                score = score + aces[0].value
        elif len(aces) > 1:  #TODO this could be where double down is called
            for a in aces:
                score = score + 1
        
        return score

    