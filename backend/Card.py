class Card(object):
    """ An object representation of a playing card.
        The "Card" has four instance attributes:
        @id is a unique identifier for each card
        @cardType is used to represent different kinds of cards
        @isTagged is used to mark card chosen by the player during each round 
        @playerID is used to distinguish between the player"""
    def __init__(self, idd, cardType, isTagged=False, playerID=None):
        self._id = idd
        self._cardType = cardType
        self._isTagged = isTagged
        self._playerID = playerID

    def __str__(self):
        """ String representation of the card object. """
        outstr = ""
        outstr += "CardID: " + str(self._id)
        outstr += " Card Type: " + str(self._cardType)
        outstr += " Tagged: " + str(self._isTagged)
        return outstr

    """ Getters are provided for all instance variables.
        Setter is provided only for the @isTagged and @playerID as other instance
        variables are constants. """
    def getID(self):
        return self._id

    def getCardType(self):
        return self._cardType

    def getIsTagged(self):
        return self._isTagged

    def setIsTagged(self, isTagged):
        self._isTagged = isTagged

    def getPlayerID(self):
        return self._playerID

    def setPlayerId(self, playerID):
        self._playerID = playerID

    def constructDeck():
        """ Creates a full deck of cards. Each card is represented with a "Card"
            object. Takes no parameters and returns an array of "Card"s. """
        deck = [Card(i, "Sashimi") for i in range(1, 15)]
        deck += [Card(i, "Tempura") for i in range(15, 29)]
        deck += [Card(i, "Dumpling") for i in range(29, 43)]
        deck += [Card(i, "Maki Roll 1") for i in range(43, 49)]
        deck += [Card(i, "Maki Roll 2") for i in range(49, 61)]
        deck += [Card(i, "Maki Roll 3") for i in range(61, 69)]
        deck += [Card(i, "Pudding") for i in range(69, 79)]
        deck += [Card(i, "Wasabi") for i in range(79, 85)]
        deck += [Card(i, "Nigiri 1") for i in range(85, 90)]
        deck += [Card(i, "Nigiri 2") for i in range(90, 100)]
        deck += [Card(i, "Nigiri 3") for i in range(100, 105)]
        deck.shuffle()
        return deck