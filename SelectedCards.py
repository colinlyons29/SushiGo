from queue import *

class SelectedCards(object):

    def __init__(self, username):
        self._cards = Queue()
        self._username = username

    def getUsername(self):
        return self._username

    def selectCard(self, card):
        self._cards.put(card)

    def draw(self):
        return self._cards.get()

    def size(self):
        return self._cards.qsize()