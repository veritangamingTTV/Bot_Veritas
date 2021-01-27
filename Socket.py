###
# This file handles any and all things network.
###

import socket

# Use keys from Settings file to make connection
from Settings import HOST, PORT, PASS, NICK, CHANNEL


# Create the connection
def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))

    # These three must be in order of PASS, NICK, CHANNEL for proper login
    s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
    s.send(bytes("NICK " + NICK + '\r\n', 'utf-8'))
    s.send(bytes("JOIN #" + CHANNEL + '\r\n', 'utf-8'))

    # Establish the socket by declaring a variable = openSocket()
    return s

# Process input for sending as message
def sendMsg(s, message):
    messageTemp = 'PRIVMSG #' + CHANNEL + ' :' + message
    # Send the appropriately formatted line
    s.send(bytes(messageTemp + '\r\n', 'utf-8'))
    # Log the message sent
    print('Sent: '+ messageTemp)
