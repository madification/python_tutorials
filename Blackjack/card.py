class card:

    def __init__(self, value) -> None:
        self.value = value
        pass

    def computeScore(self, hand) -> int:
        score = 0
        aces = []
        for c in hand:
            if c == "Ace":
                aces = aces + c
                continue

            if c == "King" | c == "Queen" | c == "Jack":
                score = score + 10
            elif c > 2 | c < 11:
                score = score + c
            
        if len(aces) == 1:
            if score + 11 > 21:
                score = score + 1
        elif len(aces) > 1:  #TODO this could be where double down is called
            for a in aces:
                score = score + 1
        
        return score