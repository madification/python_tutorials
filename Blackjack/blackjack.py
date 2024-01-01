import card
import dealer
import deck
import Player
import random

from play_actions import actions
from game_state import GameState


class Game:

    def __init__(self, numDecks, numPlayers, playerNames):
        self.numDecks = numDecks
        self.numPlayers = numPlayers
        self.players = []
        for i in range(numPlayers):
            self.players.append(Player.Player(playerNames[i]))
        self.dealer = dealer.Dealer()
        self.deck = deck.Deck()
        self.buildGameDeck()
        self.discardPile = []
        self.state = GameState.SETUP


    def playGame(self):
        exitPlay = False
        while not exitPlay:
            match self.state:
                case GameState.SETUP:
                    self.deal()
                    print("Setup complete")
                    self.state = GameState.IN_GAME
                case GameState.IN_GAME:
                    print("Begin gameplay")
                    for player in self.players:
                        currentPlayerTurn = True

                        while currentPlayerTurn:
                            print("--- next turn ---")

                            action = player.play()

                            match action:
                                case actions.HIT:
                                    print(player.name, " hits")
                                    player.receiveCard(self.dealCard())
                                    pass
                                case actions.STAY:
                                    print(player.name, " stays")
                                    currentPlayerTurn = False # next player's turn
                                case actions.BUST:
                                    print(player.name, " busts")
                                    self.discardPile = self.discardPile + player.hand
                                    self.players.remove(player)
                                    currentPlayerTurn = False
                                    pass
                                case actions.WIN:
                                    print(player.name, ", Blackjack!")
                                    currentPlayerTurn = False
                                    pass

                            self.displayGame()
                    print("All player turns complete")

                    print("Begin dealer play: ")
                    action = self.dealer.play()
                    while action == actions.HIT:
                        print(action)
                        self.dealer.receiveCard(self.dealCard())
                        action = self.dealer.play()
                    print("Final dealer play: ", action)

                    print("Enter end game")
                    self.state = GameState.END_GAME

                            
                case GameState.END_GAME:
                    self.displayGame()
                    userSelection = input("Play again? y or n")
                    if userSelection == "n":
                        exitPlay = True
                    else:
                        self.state = GameState.SETUP
                    pass
                
        print("Thanks for playing!")
            
            

    def deal(self):
        proceedDealing = True
        playersDealt = 0
        while(proceedDealing):
            
            for player in self.players:

                if len(player.hand) == 2:
                    playersDealt = playersDealt + 1
                    continue
                
                player.receiveCard(self.dealCard())
            #end for
            
            
            if len(self.dealer.hand) < 2:
                self.dealer.receiveCard(self.dealCard())
                
            if playersDealt == self.numPlayers:
                proceedDealing = False
        

    def buildGameDeck(self):
        for n in range(1, self.numDecks): # we start with one deck by default
            self.deck.combineDecks(deck.Deck())

        random.shuffle(self.deck.cards)

    def dealCard(self) -> card:
        if len(self.deck.cards) == 0:
            self.replenishDeck()

        return self.deck.cards.pop(-1)
        

    def replenishDeck(self):
        random.shuffle(self.discardPile)
        self.deck = self.deck + self.discardPile
        self.discardPile = []

    
    def displayGame(self):

        match self.state:
            case GameState.SETUP:
                pass
            case GameState.IN_GAME:
                print("dealer")
                for i in range(1, len(self.dealer.hand)): #skip the first card
                    print("## ", self.dealer.hand[i].type, end=" ")
                print()
                for p in self.players:
                    print(p.name)
                    for c in p.hand:
                        print(c.type, end=" ")
                    print()

            case GameState.END_GAME:
                print("dealer")
                for c in self.dealer.hand:
                    print(c.type, end=" ")
                print()
                for p in self.players:
                    print(p.name)
                    for c in p.hand:
                        print(c.type, end=" ")
                    print()

        
        
