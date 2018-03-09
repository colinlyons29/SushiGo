from queue import *

class SelectedCards(object):
#An class for storing all cards that a player has chosen in a round
#Inherits from the pyhton in built queue as order matters

    def __init__(self):
        self._cards = Queue()

    def selectCard(self, card):
        self._cards.put(card)

    def draw(self):
        return self._cards.get()

    def size(self):
        return self._cards.qsize()
