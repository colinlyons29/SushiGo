from PointCalculator import *
from Player import *
from PremadeSelectedCards16 import *
from EndOfGameCalculator import *

player1 = Player("192.168.2.4")
player2 = Player("192.168.2.5")
player3 = Player("192.168.2.6")
player4 = Player("192.168.2.7")

selectedcards = PremadeSelectedCards16()
cards = selectedcards.returnSelectedCards()
cards1 = cards[0]
cards2 = cards[1]
cards3 = cards[2]


print("Round 1:")
points = EndOfRoundCalculator(player1, player2, player3, player4, cards1[0], cards1[1], cards1[2], cards1[3])
print("Round 2:")
points = EndOfRoundCalculator(player1, player2, player3, player4, cards2[0], cards2[1], cards2[2], cards2[3])
print("Round 3:")
points = EndOfRoundCalculator(player1, player2, player3, player4, cards3[0], cards3[1], cards3[2], cards3[3])
print("Final Tally:")
puddings =  EndOfGameCalculator(player1, player2, player3, player4)
