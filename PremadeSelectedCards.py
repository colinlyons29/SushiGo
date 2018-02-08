from DeckConstructor import *
from queue import *
from SelectedCards import *

class PremadeSelectedCards(object):

    def __init__(self):
        self._cards = SelectedCards()
        self._deck = DeckConstructor()
        for i in range(8):
            self._cards.selectCard(self._deck.draw())

    def draw(self):
        return self._cards.draw()

    def size(self):
        return self._cards.size()




#hand = PremadeSelectedCards()
#print(hand.size())
#for i in range(8):
#    print(hand.take())
