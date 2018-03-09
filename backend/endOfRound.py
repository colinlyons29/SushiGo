""" Takes in names of two shelves as arguments and uses information from those
    shelves to calculate the points that each player has at the end of the round. """

from pointCalc import *
from Player import *
from SelectedCards import *
from sys import argv
import shelve as shelve

class EndOfRoundCalculator(object):
#Takes in 4 players and the cards they selected. Calls the PointCalculator object's methods to
#get points that can be calculated without other players' data before comparing maki icons to see
#who scores points based on those.

    def __init__(self, plist, sclist):
        self._playerlst = plist
        self._scList = sclist
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
    #Checks if players are tying and acts accordingly based on game rules
    #makiLeaders is a list off all players that have the most amount of maki roll points
    #makiSeconds is a list of all players that have the second most amount of maki roll points
        makiMost = 0
        makiSecondAmount = 0
        makiLeaders = []
        makiSeconds = []

        for player in self._playerlst:
            if player.maki > 0:
                if player.maki > makiMost:
                    if makiLeaders:
                        makiSeconds = makiLeaders
                        makiSecondAmount = makiMost
                    makiLeaders = [player]
                    makiMost = player.maki

                elif player.maki == makiMost:
                    makiLeaders += [player]

                elif player.maki < makiMost:
                    if player.maki > makiSecondAmount:
                        makiSecondAmount = player.maki
                        makiSeconds = [player]

                    elif player.maki == makiSecondAmount:
                        makiSeconds += [player]

        if makiLeaders:
            for player in makiLeaders:
                player.addPoints(6 // len(makiLeaders))
            if makiSeconds:
                for player in makiSeconds:
                    player.addPoints(3 // len(makiSeconds))

    def printPlayers(self):
    #Just for testing purposes
        for player in self._playerlst:
            print(player)
        print("\n")

    def printReport(self):
    #Prints a report of player points earned to the console
        for i in range(4):
            print("Player " + str(i+1) + " at IP: " + self._playerlst[i].ip + " now has " + str(self._playerlst[i].points) + " points and collected " + str(self._playerlst[i].pudding) + " pudding!")
        print("\n")


pShelve = argv[1]
scShelve = argv[2]

plst = []
d = shelve.open(pShelve)
for k in d.keys():
    p = Player(k, d[k])
    plst.append(p)
d.close()

sclst = []
d = shelve.open(scShelve)
for k in d.keys():
    sc = SelectedCards()
    for c in d[k]:
        sc.SelectCard(c)
    sclst.append(sc)
d.close()

eor = EndOfRoundCalculator(plst, sclst)
