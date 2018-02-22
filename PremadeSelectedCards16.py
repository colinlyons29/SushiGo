from SelectedCards import *

class PremadeSelectedCards16(object):

    def __init__(self):
        self._cards1 = SelectedCards()
        self._cards2 = SelectedCards()
        self._cards3 = SelectedCards()
        self._cards4 = SelectedCards()
        self._cards5 = SelectedCards()
        self._cards6 = SelectedCards()
        self._cards7 = SelectedCards()
        self._cards8 = SelectedCards()
        self._cards9 = SelectedCards()
        self._cards10 = SelectedCards()
        self._cards11 = SelectedCards()
        self._cards12 = SelectedCards()
        self._cards13 = SelectedCards()
        self._cards14 = SelectedCards()
        self._cards15 = SelectedCards()
        self._cards16 = SelectedCards()
        self._deck = DeckConstructor()
        for i in range(8):
            self._cards1.selectCard(self._deck.draw())

        for i in range(8):
            self._cards2.selectCard(self._deck.draw())

        for i in range(8):
            self._cards3.selectCard(self._deck.draw())

        for i in range(8):
            self._cards4.selectCard(self._deck.draw())

        for i in range(8):
            self._cards5.selectCard(self._deck.draw())

        for i in range(8):
            self._cards6.selectCard(self._deck.draw())

        for i in range(8):
            self._cards7.selectCard(self._deck.draw())

        for i in range(8):
            self._cards8.selectCard(self._deck.draw())

        for i in range(8):
            self._cards9.selectCard(self._deck.draw())

        for i in range(8):
            self._cards10.selectCard(self._deck.draw())

        for i in range(8):
            self._cards11.selectCard(self._deck.draw())

        for i in range(8):
            self._cards12.selectCard(self._deck.draw())


    def draw(self):
        return self._cards1.draw()

    def size(self):
        return self._cards1.size()

    def returnSelectedCards(self):
        return [[self._cards1, self._cards2, self._cards3, self._cards4], [self._cards5, self._cards6, self._cards7, self._cards8], [self._cards9, self._cards10, self._cards11, self._cards12]]