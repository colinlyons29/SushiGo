class SelectedCards(object):

    def __init__(self, username):
        self._cards = []
        self._username = username

    def getUsername(self):
        return self._username

    def selectCard(self, card):
        self._cards.append(card)

    def draw(self):
        return self._cards.pop()

    def size(self):
        return len(self._cards)