class Card(object):

    def __init__(self, idd):
        self._id = idd
        self._numberInDeck = 0
        self._cardType = ""
        self._isTagged = False

    def getID(self):
        return self._id

    def getIsTagged(self):
        return self._isTagged

    def getNumberInDeck(self):
        return self._numberInDeck

    def setNumberInDeck(self, number):
        self._numberInDeck = number

    def getCardType(self):
        return self._cardType

    def __str__(self):
        return self._cardType + "| ID = " + str(self._id)

    #number = property(getNumberInDeck,setNumberInDeck)
    #cardType = property(getCardType)

lstCards = [Card(i) for i in range(10)]
for x in lstCards:
    print(x)

cards = dict()

for card in lstCards:
    cards[card.getID()] = [card.getNumberInDeck(), card.getCardType(), card.getIsTagged()]
    #cards[card.getID()].append(card.getNumberInDeck())
    #cards[card.getID()].append(card.getCardType())

cards[3][2] = True

for k in cards:
    v = cards[k]
    print("ID: " + str(k) + " Number in Deck: " + str(v[0]) + " Card Type: " + str(v[1]) + " Tagged: " + str(v[2]))

import json

outmsg = json.dumps(cards)
inmsg = json.loads(outmsg)

if inmsg is dict:
    for k in inmsg:
        v = cards[k]
        print("ID: " + str(k) + " Number in Deck: " + str(v[0]) + " Card Type: " + str(v[1]) + " Tagged: " + str(v[2]))
