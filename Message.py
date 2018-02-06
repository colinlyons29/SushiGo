""" This file contains the Message class used to create Message objects that
    are the basis of communication between the server and the clients.
    The file also contains two methods: encyptMessage() and decryptMessages()
    as well as a unit test.
    Planning to add encyption to messages.
    Planning to add gzip compression to encyptMessage() and decryptMessages()
    functions.
    Author: Jakub Piatek 115348936 """

#------------------------- Message Class -------------------------

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

#------------------------- Encryption Function -------------------------

def _encrypt(msg, shift, decrypt=False):
    """ Simple substitution encryption with a shift by "shift" number of letters. 
        Wraps around to prevent non existing characters."""
    outmsg = ""
    if shift < 1 or shift > 94:
        outmsg = "Please only use shift values between 1 and 94. "
    elif type(msg) is not str:
        outmsg = "Please only use string type values for encyption. "
    else:
        if not decrypt:
            for char in msg:
                newchar = ord(char)
                if newchar > 31:
                    newchar += shift
                    if newchar > 127:
                        newchar -= 94
                outmsg += chr(newchar)
        else:
            for char in msg:
                newchar = ord(char)
                if newchar > 31:
                    newchar -= shift
                    if newchar < 31:
                        newchar += 94
                outmsg += chr(newchar)
    return outmsg

#------------------------- Pickling Function -------------------------

def _convert(msg):
    """ Convert the Message object into a string form that can be send over the 
        sockets. """
    import pickle as pickle

    if type(msg) is str:
        outmsg = pickle.loads(msg)
    else:
        outmsg = pickle.dumps(msg)
    return outmsg

#------------------------- Functions -------------------------

def encryptMessage(msg):
    """ Pickle and encrypt the Message object so that it can be sent across
        network. """
    outmsg = ""
    return outmsg


def decryptMessages(msg):
    """ Decrypt and unpickle the Message object so that it can be processed
        by the receiver. """
    outmsg = ""
    return outmsg

#------------------------- Testing -------------------------

def main():
    """ Test block for Message class, it's methods and the encryptMessage() and
        decryptMessages() functions. All methods of the Message class, excluding
        getters and setters, are tested. """

    print('\n' + 50*'-' + '\n' + "Testing encryption function. " + '\n' + 50*'-' + '\n')
    print("The original text of the test message is: ")
    txt = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ac mattis 
nisi, bibendum suscipit libero. Cras euismod ut ex vitae pretium. Ut pharetra erat 
felis, venenatis vehicula nulla mattis quis. Nullam mollis sodales sapien, nec 
viverra elit hendrerit eget. Cras at lorem ultricies, blandit urna eu, laoreet ex. 
Aliquam ullamcorper a tortor vel rutrum. Aliquam rutrum euismod diam, quis vulputate 
tortor condimentum vitae. Aliquam erat lacus, aliquet id sapien sed, cursus 
consequat quam. Fusce euismod nisl purus. Phasellus quis velit turpis. Aenean non 
orci luctus, vehicula justo ac, laoreet nibh. Suspendisse vel luctus ex. Nulla ac 
dui mi. Sed finibus sapien a orci consequat, nec porta mi molestie. Donec mattis 
condimentum ex, vel auctor nisi fringilla et. Morbi maximus ante sed ultricies posuere. """
    print(txt)
    print("")
    print("The encrypted text, with shift 40, of the test message is: ")
    txt = _encrypt(txt, 40)
    print(txt)
    print("")
    print("The decrypted text of the test message is: ")
    txt = _encrypt(txt, 40, decrypt=True)
    print(txt)
    print("")
    print("Testing incorrect parameter detection: ")
    print("")
    print("Using shift parameter outside of range: ")
    txt = _encrypt(txt, 124)
    print(txt)
    print("")
    print("Using an object other than a string for msg parameter: ")
    txt = 21
    txt = _encrypt(txt, 40)
    print(txt)
    print("")

if __name__ == '__main__':
    main()