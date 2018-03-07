""" Creates four players and generates scores for them. Used for testing. """

import shelve as shelve
from Player import *
from SelectedCards import *
from Card import *

deck = Card.constructDeck()

d = shelve.open("playersDB")

p1 = Player("192.168.2.4", "p1")
d[p1.getUsername()] = p1.getIP()
p2 = Player("192.168.2.5", "p2")
d[p2.getUsername()] = p2.getIP()
p3 = Player("192.168.2.6", "p3")
d[p3.getUsername()] = p3.getIP()
p4 = Player("192.168.2.7", "p4")
d[p4.getUsername()] = p4.getIP()

d.close()

d = shelve.open("selectedCardsDB")

sc1 = SelectedCards("p1")
sc2 = SelectedCards("p1")
sc3 = SelectedCards("p1")
sc4 = SelectedCards("p1")

for i in range(8):
    sc1.selectCard(deck[i])
    sc2.selectCard(deck[i + 10])
    sc3.selectCard(deck[i + 20])
    sc4.selectCard(deck[i + 30])

d[sc1.getUsername()] = [sc1.draw() for i in range(8)]
d[sc2.getUsername()] = [sc2.draw() for i in range(8)]
d[sc3.getUsername()] = [sc3.draw() for i in range(8)]
d[sc4.getUsername()] = [sc4.draw() for i in range(8)]

d.close()