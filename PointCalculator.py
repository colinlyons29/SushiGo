from PremadeSelectedCards import *
from SelectedCards import *

class PointCalculator(object):

    def __init__(self, selectedCards):
        self._cards = selectedCards
        self._makiIcons = 0
        self._sashimiAmount = 0
        self._puddingAmount = 0
        self._tempuraAmount = 0
        self._wasabiPlaced = False
        self._dumplingAmount = 0
        self._points = 0
        self._dumplingScores = [0, 1, 3, 6, 10, 15]
        self.checkCards()
        self.calculatePoints()


    def checkCards(self):
        for i in range(8):
            card = self._cards.draw()
            #print(card)
            if card._cardType == "Sashimi":
                self._sashimiAmount += 1

            elif card._cardType == "Pudding":
                self._puddingAmount += 1

            elif card._cardType == "Tempura":
                self._tempuraAmount += 1

            elif card._cardType == "Wasabi":
                self._wasabiPlaced = True

            elif card._cardType == "Dumpling":
                self._dumplingAmount += 1

            elif card._cardType == "Maki Roll 1":
                self._makiIcons += 1

            elif card._cardType == "Maki Roll 2":
                self._makiIcons += 2

            elif card._cardType == "Maki Roll 3":
                self._makiIcons += 3


            elif card._cardType == "Nigiri 1":

                if self._wasabiPlaced:
                    self._points += 3
                    self._wasabiPlaced = False
                else:
                    self._points += 1

            elif card._cardType == "Nigiri 2":

                if self._wasabiPlaced:
                    self._points += 6
                    self._wasabiPlaced = False
                else:
                    self._points += 2

            elif card._cardType == "Nigiri 3":

                if self._wasabiPlaced:
                    self._points += 9
                    self._wasabiPlaced = False
                else:
                    self._points += 3

    def calculatePoints(self):

        self._points += ((self._sashimiAmount//3)*10)

        self._points += ((self._tempuraAmount//2)*5)

        if self._dumplingAmount > 5:
            self._points += 15
        else:
            self._points += self._dumplingScores[self._dumplingAmount]

    def returnScores(self):

        return [self._points, self._makiIcons, self._puddingAmount]



#cards = PremadeSelectedCards()
#scores = PointCalculator(cards)
#print(scores.returnScores())




