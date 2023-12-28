import unittest
import deck
import blackjack

class TestBlackjackMethods(unittest.TestCase):

    def test_deck_shuffle(self):
        myDeck = deck.Deck()
        print(myDeck.cards)
        myDeck.shuffle(7)
        # print("shuffled: ", myDeck.cards)
        # print("card selection: ", myDeck.cards[5])
        

    def test_game(self):
        myGame = blackjack.Game(1, 2, ["Nick", "Maddie"])
        myGame.setupGame()

        for player in myGame.players:
            print(player.hand)

    

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()