from DeckConstructor import *
from queue import *

class SelectedCards(object):

    def __init__(self):
        self._cards = Queue()

    def selectCard(self, card):
        self._cards.put(card)

    def draw(self):
        return self._cards.get()

    def size(self):
        return self._cards.qsize()



