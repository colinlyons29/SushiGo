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

    def __str__(self):
        """ String representation of the card object. """
        outstr = ""
        outstr += "CardID: " + str(self._id)
        outstr += " Card Type: " + str(self._cardType)
        outstr += " Tagged: " + str(self._isTagged)
        return outstr

    """ Getters are provided for all instance variables.
        Setter is provided only for the @isTagged as other instance variables
        are constants. """
    def getID(self):
        return self._id

    def getCardType(self):
        return self._cardType

    def getIsTagged(self):
        return self._isTagged

    def setIsTagged(self, isTagged):
        self._isTagged = isTagged

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

def _fromJSON(obj):
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
    hand = _fromJSON(hand)
    outHand = []
    for k in hand:
        card = Card(k, hand[k][0], hand[k][1])
        outHand.append(card)
    return outHand

def main():
    """ Sample test block. It will autorun only if code is executed directly """
    deck1 = constructDeck()
    for card in deck1:
        print(card)

if __name__ == '__main__':
    main()