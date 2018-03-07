""" Takes in the name of the shelve as an argument and loads the information from
    that shelve. The information is then stored in a json and passed to the 
    program that called this script. """

import shelve as shelve
import json
from sys import argv

shelveName = argv[2]
d = shelve.open(shelveName)
tempD = dict()

for k in d.keys():
    tempD[k] = d[k]

d.close()

jsonObj = json.dumps(tempD)
print(jsonObj)