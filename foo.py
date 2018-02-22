class Card(object):
    """ An object representation of a playing card.
        The "Card" has three instance attributes:
        @id is a unique identifier for each card
        @cardType is used to represent different kinds of cards
        @isTagged is used to mark card chosen by the player during each round """
    def __init__(self, idd, cardType, isTagged=False):
        self._id = idd
        self._cardType = cardType
        self._isTagged = isTagged
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
    deck = [Card(i, "Sashimi") for i in range(1, 15)]
    deck += [Card(i, "Tempura") for i in range(15, 29)]
    deck += [Card(i, "Dumpling") for i in range(29, 43)]
    deck += [Card(i, "MakiRollOne") for i in range(43, 49)]
    deck += [Card(i, "MakiRollTwo") for i in range(49, 61)]
    deck += [Card(i, "MakiRollThree") for i in range(61, 69)]
    deck += [Card(i, "Pudding") for i in range(69, 79)]
    deck += [Card(i, "Wasabi") for i in range(79, 85)]
    deck += [Card(i, "EggNigiri") for i in range(85, 90)]
    deck += [Card(i, "SalmonNigiri") for i in range(90, 100)]
    deck += [Card(i, "SquidNigiri") for i in range(100, 105)]
    return deck

def _toJSON(obj):
    """ Packs a python data structure into a JSON, to allow communication with
        JavaScript programs. """
    import json
    out = json.dumps(obj)
    return out

def _fromJSON(msg):
    """ Takes a JSON and unpacks it into a Python data structure, allowing
        communication with JavaScript. """
    import json
    out = json.loads(obj)
    return out

def prepareHand(hand):
    """ Takes a @hand, a list of "Card"s objects, and turns it into a dictionary.
        Packs the dictionary into a JSON so that it's ready to be send to a
        JavaScript program. """
    outHand = dict()
    for card in hand:
         outHand[card.getID()] = [card.getCardType(), card.getIsTagged()]
    outHand = _toJSON(outHand)
    return outHand

def prepareCards(hand):
    """ Takes a @hand, a JSON dictionary, unpacks the dictionary into a Python
        dictionary. Then extracts information from the dictionary and creates a
        list of "Card" objects to be used by the game logic. """
    outHand = []
    for k in hand:
        card = Card(k, hand[k][0], hand[k][1])
        outHand.append(card)
    return outHand


# Outdated code block, can be probably safely deleted.
# def main1():
#     lstCards = [Card(i, "Maki") for i in range(10)]
#     for x in lstCards:
#         print(x)

#     cards = dict()

#     for card in lstCards:
#         cards[card.getID()] = [card.getCardType(), card.getIsTagged()]

#     cards[3][1] = True

#     for k in cards:
#         v = cards[k]
#         print("ID: " + str(k) + " Card Type: " + str(v[0]) + " Tagged: " + str(v[1]))

#     import json

#     outmsg = json.dumps(cards)
#     inmsg = json.loads(outmsg)

#     if inmsg is dict:
#         for k in inmsg:
#             v = cards[k]
#             print("ID: " + str(k) + " Card Type: " + str(v[0]) + " Tagged: " + str(v[1]))

def main():
    """ Sample test block. It will autorun only if code is executed directly """
    deck1 = constructDeck()
    for card in deck1:
        print(card)

if __name__ == '__main__':
    main()