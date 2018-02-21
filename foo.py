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
    """ Creates a full deck of cards. Each card is represented with a "Card"
        object. Takes no parameters and returns an array of "Card"s. """
    deck = [Card(i, "Sashimi") for i in range(1, 15)] +
            [Card(i, "Tempura") for i in range(15, 29)] +
            [Card(i, "Dumpling") for i in range(29, 43)] +
            [Card(i, "MakiRollOne") for i in range(43, 49)] +
            [Card(i, "MakiRollTwo") for i in range(49, 61)] +
            [Card(i, "MakiRollThree") for i in range(61, 69)] +
            [Card(i, "Pudding") for i in range(69, 79)] +
            [Card(i, "Wasabi") for i in range(79, 85)] +
            [Card(i, "EggNigiri") for i in range(85, 90)] +
            [Card(i, "SalmonNigiri") for i in range(90, 100)] +
            [Card(i) for i in range(15, 29)] +
    return deck

def main():
    """ Sample test block. It will autorun only if code is executed directly """
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
