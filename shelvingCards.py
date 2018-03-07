""" Takes in a json dictionary as a command line argument and stores the
    information from that dictionary in a shelve. """

import shelve as shelve
import json

jsonObj = argv[1]
tempD = json.loads(jsonObj)

d = shelve.open()
for k in tempD:
    d[k] = tempD[k]
shelve.close()