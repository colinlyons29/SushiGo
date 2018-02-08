class Card(object):

    def __init__(self, id):
        self._id = 0
        self._numberInDeck = 0
        self._cardType = ""

    def getNumberInDeck(self):
        return self._numberInDeck

    def setNumberInDeck(self, number):
        self._numberInDeck = number

    def getCardType(self):
        return self._cardType

    def __str__(self):
        return self._cardType + "| ID = " + str(self._id)

    number = property(getNumberInDeck,setNumberInDeck)
    cardType = property(getCardType)

#==================================================================

class Sashimi(Card):
    #If you have 3 of these, you get 10 points
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 14
        self._cardType = "Sashimi"

#==================================================================

class Pudding(Card):
    #You get 6 points at the end of the game if you have the most of these
    #You get -6 if you have the least
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 10
        self._cardType = "Pudding"

#==================================================================

class Tempura(Card):
    #If you have 2 of these, you get 5 points
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 14
        self._cardType = "Tempura"

#==================================================================

class Wasabi(Card):
    #The next Nigiri card you play is multiplied by 3
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 6
        self._cardType = "Wasabii"

#==================================================================

class Dumpling(Card):
    #You get more points for each one of these you have (up to 5)
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 14
        self._cardType = "Dumpling"


#==================================================================


class MakiRoll(Card):
    #The player with the most Maki Roll Icons scores 6 points
    #The player with the second most scores 3
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 0
        self._cardType = "Maki Roll"
        self._makiRollIcons = 0

    def getMakiRollIcons(self):
        return self._makiRollIcons

    icons = property(getMakiRollIcons)

class MakiRollOne(MakiRoll):
    #Gives one Maki Roll Icon
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 6
        self._makiRollIcons = 1
        self._cardType = "Maki Roll 1"


class MakiRollTwo(MakiRoll):
    #Gives two Maki Roll Icons
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 12
        self._makiRollIcons = 2
        self._cardType = "Maki Roll 2"

class MakiRollThree(MakiRoll):
    #Gives three Maki Roll Icons
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 8
        self._makiRollIcons = 3
        self._cardType = "Maki Roll 3"


#==================================================================


class Nigiri(Card):
    #Scores a certain amount of points (1, 2, or 3) depending on its type
    #Can be multiplied by 3 if it is placed on top of a Wasabi card
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 5
        self._cardType = "Nigiri"
        self._defaultpoints = 0

    def getPoints(self):
        return self._defaultpoints

    points = property(getPoints)

class SquidNigiri(Nigiri):
    #Scores 3 points
    def __init__(self, id):
        self._id = id
        self._defaultpoints = 3
        self._cardType = "Nigiri 3"


class SalmonNigiri(Nigiri):
    # Scores 2 points
    def __init__(self, id):
        self._id = id
        self._numberInDeck = 10
        self._cardType = "Nigiri 2"
        self._defaultpoints = 2


class EggNigiri(Nigiri):
    # Scores 1 point
    def __init__(self, id):
        self._id = id
        self._cardType = "Nigiri 1"
        self._defaultpoints = 1


#card1 = Sashimi()
#print(card1.cardType)
#print(card1.number)

#card2 = MakiRollThree()
#print(card2.icons)