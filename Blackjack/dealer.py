from Player import Player

class Dealer(Player):

    def __init__(self):
        super().__init__("Dealer")
        pass



    def computeScore(self, hand) -> int:
        score = 0
        aces = []
        for c in hand:
            if c == "Ace":
                score = score + 11
                aces.append(c)
            elif c == "King" or c == "Queen" or c == "Jack":
                score = score + 10
            else:
                score = score + c.value
            
        if len(aces) > 1:  
            pass #TODO this could be where double down is called
        
        return score