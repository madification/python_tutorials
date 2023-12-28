import deck
import Player
import random

from play_actions import actions


class Game:

    def __init__(self, numDecks, numPlayers, playerNames):
        self.numDecks = numDecks
        self.numPlayers = numPlayers
        self.players = []
        for i in range(numPlayers):
            self.players.append(Player.Player(playerNames[i]))
        self.deck = deck.Deck()
        self.buildGameDeck()
        self.discardPile = []

    def setupGame(self):
        self.deal()
        #TODO setup dealer
        pass


    def playGame(self):
        for player in self.players:
            action = player.play()
            match action:
                case actions.HIT:
                    pass
                case actions.STAY:
                    pass
                case actions.BUST:
                    self.discardPile = self.discardPile + player.hand
                    self.players.remove(player)
                    pass
                case actions.WIN:
                    pass
            
            

    def deal(self):
        proceedDealing = True
        playersDealt = 0
        while(proceedDealing):
            
            for player in self.players:

                if len(player.hand) == 2:
                    playersDealt = playersDealt + 1
                    continue

                if len(self.deck.cards) == 0:
                    self.replenishDeck()
                
                player.receiveCard(self.deck.cards.pop(-1))
                
            if playersDealt == self.numPlayers:
                proceedDealing = False
        

    def buildGameDeck(self):
        for n in range(1, self.numDecks): # we start with one deck by default
            self.deck.combineDecks(deck.Deck())

        random.shuffle(self.deck.cards)

    def replenishDeck(self):
        random.shuffle(self.discardPile)
        self.deck = self.deck + self.discardPile
        self.discardPile = []
