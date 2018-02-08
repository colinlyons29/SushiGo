from Cards import *
from random import shuffle
class DeckConstructor(object):
    #An object that creates a 'deck' of card objects

    def __init__(self):
        self._deck = []
        self.construct()

    def construct(self):
        id = 0
        for i in range(14):
            self._deck += [Sashimi(id)]
            id += 1
            self._deck += [Tempura(id)]
            id += 1
            self._deck += [Dumpling(id)]
            id += 1

        for i in range(12):
            self._deck += [MakiRollTwo(id)]
            id += 1

        for i in range(10):
            self._deck += [Pudding(id)]
            self._deck += [SalmonNigiri(id)]
            id += 1

        for i in range(8):
            self._deck += [MakiRollThree(id)]
            id += 1

        for i in range(6):
            self._deck += [Wasabi(id)]
            id += 1
            self._deck += [MakiRollOne(id)]
            id += 1

        for i in range(5):
            self._deck += [SquidNigiri(id)]
            id += 1
            self._deck += [EggNigiri(id)]
            id += 1

        shuffle(self._deck)

    def __str__(self):
        decklist = ""
        decklist += str(len(self._deck)) + "\n"
        for i in self._deck:
            decklist += i.cardType + "\n"
        return decklist

    def draw(self):
        return self._deck.pop()


