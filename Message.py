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
    import gzip
    import pickle as pickle
    if not isinstance(msg, Message):
        return "Please only use Message object!"
    outmsg = "foo"
    return outmsg


def uncompressMessage(msg):
    import gzip
    import pickle as pickle

    outmsg = "bar"
    return outmsg

def main():
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