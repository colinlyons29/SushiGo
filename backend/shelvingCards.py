""" Takes in a json dictionary and the name of the shelve as arguments
    and stores the information from that dictionary in the named shelve. """

import shelve as shelve
import json
from sys import argv

jsonObj = argv[1]
tempD = json.loads(jsonObj)

shelveName = argv[2]
d = shelve.open(shelve)
for k in tempD:
    d[k] = tempD[k]
d.close()