from SelectedCards import *

class PremadeSelectedCards4(object):

    def __init__(self):
        self._cards1 = SelectedCards()
        self._cards2 = SelectedCards()
        self._cards3 = SelectedCards()
        self._cards4 = SelectedCards()
        self._deck = DeckConstructor()
        for i in range(8):
            self._cards1.selectCard(self._deck.draw())

        for i in range(8):
            self._cards2.selectCard(self._deck.draw())

        for i in range(8):
            self._cards3.selectCard(self._deck.draw())

        for i in range(8):
            self._cards4.selectCard(self._deck.draw())

    def draw(self):
        return self._cards1.draw()

    def size(self):
        return self._cards1.size()

    def returnSelectedCards(self):
        return [self._cards1, self._cards2, self._cards3, self._cards4]




#hand = PremadeSelectedCards4()
#print(hand.size())
#hands = hand.returnSelectedCards()
#print(hands)
#for i in range(8):
#    print(hand.take())
