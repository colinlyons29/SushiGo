from PointCalculator import *
from Player import *
from PremadeSelectedCards4 import *

class EndOfRoundCalculator(object):

    def __init__(self, pl1, pl2, pl3, pl4, sc1, sc2, sc3, sc4):
        self._player1 = pl1
        self._player2 = pl2
        self._player3 = pl3
        self._player4 = pl4
        self._selectedCards1 = sc1
        self._selectedCards2 = sc2
        self._selectedCards3 = sc3
        self._selectedCards4 = sc4
        self._playerlst = [self._player1, self._player2, self._player3, self._player4]
        self._scList = [self._selectedCards1, self._selectedCards2, self._selectedCards3, self._selectedCards4]
        self.initialTotals()
        self.compareMaki()
        self.printReport()



    def initialTotals(self):
    #Calls the PointCalculator class to calculate the values of each and assign them to players
        for i in range(4):
            calc = PointCalculator(self._scList[i])
            self._playerlst[i].takeInTotals(calc.returnScores())

    def compareMaki(self):
    #Decides who to allocate points to based on their maki rolls
    #Doesn't seem like a complicated tasks but there needs to be rules for what happens when players tie
        makiMost = 0
        makiSecondAmount = 0
        makiLeaders = []
        makiSeconds = []

        for player in self._playerlst:
            if player.maki > 0:
                if player.maki > makiMost:
                    # print("1")

                    if makiLeaders:
                        makiSeconds = makiLeaders
                        makiSecondAmount = makiMost
                    makiLeaders = [player]
                    makiMost = player.maki

                elif player.maki == makiMost:
                    # print("2")
                    makiLeaders += [player]

                elif player.maki < makiMost:
                    # print("3")
                    # print("if " + str(player.maki) + " > " + str(makiSecondAmount))
                    if player.maki > makiSecondAmount:
                        makiSecondAmount = player.maki
                        makiSeconds = [player]

                    elif player.maki == makiSecondAmount:
                        # print("4")
                        makiSeconds += [player]

        if makiLeaders:
            for player in makiLeaders:
                player.addPoints(6 // len(makiLeaders))
            else:
                if makiSeconds:
                    for player in makiSeconds:
                        player.addPoints(3 // len(makiSeconds))

    def printPlayers(self):
    #Just for testing purposes
        for player in self._playerlst:
            print(player)
        print("\n")

    def printReport(self):
    #If we want to display scores during the game
    #we can edit this to send the wanted information
        for i in range(4):
            print("Player " + str(i+1) + " at IP: " + self._playerlst[i].ip + " now has " + str(self._playerlst[i].points) + " points and collected " + str(self._playerlst[i].pudding) + " pudding!")
        print("\n")

#
# player1 = Player("192.168.2.4")
# player2 = Player("192.168.2.5")
# player3 = Player("192.168.2.6")
# player4 = Player("192.168.2.7")
# selectedcards = PremadeSelectedCards4()
# cards = selectedcards.returnSelectedCards()
#
#
# points = EndOfRoundCalculator(player1, player2, player3, player4, cards[0], cards[1], cards[2], cards[3])