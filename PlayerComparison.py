################################
#Here we would take in the 4 players cards and calculate points based on that
#Right now I've made a shitty function to simulate that
from PremadeSelectedCards4 import *
from PointCalculator import *
from Player import *
cards = PremadeSelectedCards4()
lst = cards.returnSelectedCards()
scorelst = []
for i in range(4):
    calc = PointCalculator(lst[i])
    #scorelst += [calc.returnScores()]
    scorelst += [[6, 5, 1], [14, 3, 2], [3, 0, 3], [13, 5, 0]]

for i in range(4):
    print("Player " + str(i+1) + ": ", end = "")
    print(scorelst[i])

#################################

player1 = Player("192.168.2.4")
player2 = Player("192.168.2.5")
player3 = Player("192.168.2.6")
player4 = Player("192.168.2.7")
playerlst = [player1, player2, player3, player4]
for i in range(4):
    playerlst[i].takeInTotals(scorelst[i])
puddingMost = 0
puddingLeast = 0
puddingLeaders = []
puddingLosers = []
n = 1
print("\n")
for player in playerlst:
    print("\n")
    print("Player: ", n)
    n += 1
    if player.pudding > 0:
        print("Player pudding: ", player.pudding)
        print("Least amount: ", puddingLeast)
        print("Most amount: ", puddingMost)
        if player.pudding > puddingMost:
            print("Path: 1")
            if puddingLeaders:
                if puddingMost <= puddingLeast:
                    puddingLosers = puddingLeaders
                    puddingLeast = puddingMost
            else:
                puddingLeast = player.pudding
            puddingLeaders = [player]
            puddingMost = player.pudding

        elif player.pudding == puddingMost:
            print("Path: 2")
            puddingLeaders += [player]

        elif player.pudding < puddingLeast:
            print("Path: 3")
            if player.pudding < puddingLeast:
                puddingLeast = player.pudding
                puddingLosers = [player]

        elif player.pudding == puddingLeast:
            print("Path: 4")
            puddingLosers += [player]

    print("Leaders points = ", puddingMost)
    for player in puddingLeaders:
        print(player)

    print("Losers points = ", puddingLeast)
    for player in puddingLosers:
        print(player)

if puddingLeaders:
    for player in puddingLeaders:
        player.addPoints(6 // len(puddingLeaders))
    else:
        if puddingLosers:
            for player in puddingLosers:
                player.addPoints(-(6// len(puddingLosers)))

#print("\n")
#for player in playerlst:
  #  print(player)