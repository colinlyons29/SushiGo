from Player import *
from PremadeSelectedCards4 import *
from EndOfRoundCalculator import *
class EndOfGameCalculator(object):
#Takes in the 4 player objects and compares their pudding count.
#Currently calls print report to display these scores in the console

    def __init__(self, pl1, pl2, pl3, pl4):
        self._player1 = pl1
        self._player2 = pl2
        self._player3 = pl3
        self._player4 = pl4
        self._playerlst = [self._player1, self._player2, self._player3, self._player4]
        self.comparePudding()
        self.printReport()

    def comparePudding(self):
        # Decides who to allocate points to based on their pudding
        # Doesn't seem like a complicated tasks but there needs to be rules for what happens when players tie
        puddingMost = 0
        puddingLeast = 0
        puddingLeaders = []
        puddingLosers = []
        for player in self._playerlst:

            if player.pudding > puddingMost:
                if puddingLeaders:
                    if puddingMost <= puddingLeast:
                        puddingLosers = puddingLeaders
                        puddingLeast = puddingMost
                else:
                    puddingLeast = player.pudding
                puddingLeaders = [player]
                puddingMost = player.pudding

            elif player.pudding == puddingMost:
                puddingLeaders += [player]

            elif player.pudding < puddingLeast:
                if player.pudding < puddingLeast:
                    puddingLeast = player.pudding
                    puddingLosers = [player]

            elif player.pudding == puddingLeast:
                puddingLosers += [player]


        if puddingLeaders:
            for player in puddingLeaders:
                player.addPoints(6 // len(puddingLeaders))
            else:
                if puddingLosers:
                    for player in puddingLosers:
                        player.addPoints(-(6 // len(puddingLosers)))


    def printPlayers(self):
    #Just for testing purposes
        for player in self._playerlst:
            print(player)
        print("\n")

    def printReport(self):
        #This will be updated to return the output to the clients
        winner = None
        points = 0
        ith = 0
        for i in range(4):
            if self._playerlst[i].points > points:
                winner = self._playerlst[i]
                ith = i + 1
            print("Player " + str(i+1) + " at IP: " + self._playerlst[i].ip + " now has a final total " + str(self._playerlst[i].points) + " points and collected " + str(self._playerlst[i].pudding) + " pudding!")
        print("Player " + str(ith) + " at: " + self._playerlst[i].ip + " won!" )



# player1 = Player("192.168.2.4")
# player2 = Player("192.168.2.5")
# player3 = Player("192.168.2.6")
# player4 = Player("192.168.2.7")
# selectedcards = PremadeSelectedCards4()
# cards = selectedcards.returnSelectedCards()
# points = EndOfRoundCalculator(player1, player2, player3, player4, cards[0], cards[1], cards[2], cards[3])
# print("\n")
#
#
# puddings = EndOfGameCalculator(player1, player2, player3, player4)