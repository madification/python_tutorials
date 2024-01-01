import unittest
import card
import deck
import blackjack
import Player
from game_state import GameState

class TestBlackjackMethods(unittest.TestCase):

    # def test_deck_shuffle(self):
    #     myDeck = deck.Deck()
    #     print(myDeck.cards)
    #     myDeck.shuffle(7)
    #     # print("shuffled: ", myDeck.cards)
    #     # print("card selection: ", myDeck.cards[5])
        
    # def test_player(self):
    #     myPlayer = Player.Player("APlayer")
    #     myPlayer.receiveCard(card.Card("Ace"))
    #     myPlayer.receiveCard(card.Card(5))

    #     computed = myPlayer.computeScore(myPlayer.hand)
    #     assert(computed == 16)

    def test_game(self):
        myGame = blackjack.Game(1, 2, ["Nick", "Maddie"])
        myGame.playGame()

    

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()