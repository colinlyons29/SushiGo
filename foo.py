class Card(object):
    """ An object representation of a playing card.
        The "Card" has three instance attributes:
        @id is a unique identifier for each card
        @cardType is used to represent different kinds of cards
        @isTagged is used to mark card chosen by the player during each round """
    def __init__(self, idd, cardType):
        self._id = idd
        self._cardType = cardType
        self._isTagged = False
        #self._numberInDeck = 0

    def __str__(self):
        """ String representation of the card object. """
        outstr = ""
        outstr += "CardID: " + str(self._id)
        outstr += " Card Type: " + str(self._cardType)
        outstr += " Tagged: " + str(self._isTagged)
        return outstr

    def getID(self):
        return self._id

    def getCardType(self):
        return self._cardType

    def getIsTagged(self):
        return self._isTagged

    def setIsTagged(self, isTagged):
        self._isTagged = isTagged

    #def getNumberInDeck(self):
    #    return self._numberInDeck

    #def setNumberInDeck(self, number):
    #    self._numberInDeck = number

    #number = property(getNumberInDeck,setNumberInDeck)
    #cardType = property(getCardType)

def constructDeck():
    deck = []
    return deck

def main():
    """ Sample test block. Will autorun only if code executed directly """
    lstCards = [Card(i, "Maki") for i in range(10)]
    for x in lstCards:
        print(x)

    cards = dict()

    for card in lstCards:
        cards[card.getID()] = [card.getCardType(), card.getIsTagged()]

    cards[3][1] = True

    for k in cards:
        v = cards[k]
        print("ID: " + str(k) + " Card Type: " + str(v[0]) + " Tagged: " + str(v[1]))

    import json

    outmsg = json.dumps(cards)
    inmsg = json.loads(outmsg)

    if inmsg is dict:
        for k in inmsg:
            v = cards[k]
            print("ID: " + str(k) + " Card Type: " + str(v[0]) + " Tagged: " + str(v[1]))
