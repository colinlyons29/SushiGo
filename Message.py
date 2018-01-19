""" This file contains the Message class used to create Message objects that
    are the basis of communication between the server and the clients.
    The file also contains two methods: compressMessage() and uncompressMessage()
    as well as a unit test.
    Author: Jakub Piatek 115348936 """

class Message(object):
    """ The Message object used for exchanging information between the server
        and the clients. """
    def __init__(self, contents):
        self._contents = contents

    def __str__(self):
        """ String representation of the Message object. """
        outstr = ""
        outstr += self._contents
        return outstr

    def getContents(self):
        return self._contents

    def setContents(self, new):
        self._contents = new

def compressMessage(msg):
    """ Pickle and compress the Message object so that it can be sent across
        network. """
    import gzip
    import pickle as pickle

    if not isinstance(msg, Message):
        return "Please only use Message object!"

    outmsg = "foo"
    return outmsg


def uncompressMessage(msg):
    """ Uncompress and unpickle the Message object so that it can be processed
        by the receiver. """
    import gzip
    import pickle as pickle

    outmsg = "bar"
    return outmsg

#------------------------- Testing -------------------------

def main():
    """ Unit test for Message class, it's methods and the compressMessage() and
        uncompressMessage() functions. All methods of the Message class, excluding
        getters and setters, are tested. """
    msg1 = Message("Test Message")
    print(msg1)
    print("")
    cmsg = compressMessage(msg1)
    print(cmsg)
    print("")
    umsg = uncompressMessage(cmsg)
    print(umsg)
    print(cmsg)
    print("")
    ecmsg = compressMessage("foobar")
    print(ecmsg)
    print("")
    eumsg = uncompressMessage("foobar")
    print(ecmsg)
    print("")

if __name__ == '__main__':
    main()