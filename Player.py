class Player(object):
#Player object stores the players ip, their accumulated points and puddings, and their current maki icons
    def __init__(self, ip):
        self._ip = ip
        self._points = 0
        self._maki = 0
        self._pudding = 0

    def getMaki(self):
        return self._maki

    def getPudding(self):
        return self._pudding

    def getPoints(self):
        return self._points

    def getIP(self):
        return self._ip

    def takeInTotals(self, lst):
    #Points and puddings totals are increased while maki count resets as it doesn't persist
        self._points += lst[0]
        self._maki = lst[1]
        self._pudding += lst[2]

    def addPoints(self, num):
        self._points += num

    maki = property(getMaki)
    pudding = property(getPudding)
    ip = property(getIP)
    points = property(getPoints)


    def __str__(self):
        string = "["
        string += str(self._points)
        string += ", "
        string += str(self._maki)
        string += ", "
        string += str(self._pudding)
        string += "]"
        return string