from pointCalc import *
from Player import *

class EndOfRoundCalculator(object):
#Takes in 4 players and the cards they selected. Calls the PointCalculator object's methods to
#get points that can be calculated without other players' data before comparing maki icons to see
#who scores points based on those.

    def __init__(self, pl1, pl2, pl3, pl4, sc1, sc2, sc3, sc4):
        self._playerlst = [pl1, pl2, pl3, pl4]
        self._scList = [sc1, sc2, sc3, sc4]
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
    #If we want to display scores during the game
    #we can edit this to send the wanted information
        for i in range(4):
            print("Player " + str(i+1) + " at IP: " + self._playerlst[i].ip + " now has " + str(self._playerlst[i].points) + " points and collected " + str(self._playerlst[i].pudding) + " pudding!")
        print("\n")

def main():
    from PremadeSelectedCards4 import *
    player1 = Player("192.168.2.4")
    player2 = Player("192.168.2.5")
    player3 = Player("192.168.2.6")
    player4 = Player("192.168.2.7")
    selectedcards = PremadeSelectedCards4()
    cards = selectedcards.returnSelectedCards()
    points = EndOfRoundCalculator(player1, player2, player3, player4, cards[0], cards[1], cards[2], cards[3])

if __name__ == '__main__':
    main()