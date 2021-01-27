from Socket import openSocket, sendMsg
from Initialize import joinRoom
from Settings import HOST
import string
import random
from Read import getUser, getMsg
from Command import execute, comList, quotes, paramList

# Establish connection
s = openSocket()
joinRoom(s)
readbuffer = ''
param = 'None'
reconTimer = 0

# When disconnected, make new connection
def reconnect():
    sleep(reconTimer)
    try:
        joinRoom(s)
        # On reconnect, reset attempt delay
        reconTimer = 0
    except:
        # On first reconnect failure, delay next attempt
        if reconTimer == 0:
            reconTimer = 2
            reconnect()
        # On subsequent failure, double delay timer
        else:
            reconTimer *= 2
            reconnect()

while True:
    # Recieve incoming data
    try:
        readbuffer = readbuffer + s.recv(1024).decode('UTF-8')
        temp = readbuffer.split('\n')
        readbuffer = temp.pop()
        # Display messages in log
        for line in temp:
                print(line)
                user = getUser(line)
                msg = getMsg(line, s)
                print(user + ' typed ' + msg)
                # Determine if message was a command
                if '!' in msg:
                    command = str(msg.split('!',1)[1])
                    # Log the command
                    print(str(user) +' used '+ command +' command!')
                    # Try with parameters
                    try:
                        param = str(command.split(' ',1)[1])
                        command = str(command.split(' ',1)[0])
                        print('With paramters: '+param)
                        print(user+' triggered '+command+'!')
                        if command == 'addquote':
                            print('Adding quote: '+param)
                            quotes.append(param)
                        elif command == 'mirror':
                            response = param[::-1]
                            print(response)
                            sendMsg(s, str(response))
                    # Error, no parameters
                    except:
                        print('Without parameters.')
                        print(user+' triggered '+command+'!')
                        if command in comList:
                            response = str(comList[command])
                            print('Respond with: '+ response)
                            sendMsg(s, str(response))
                        elif command == 'quote':
                            response = random.choice(quotes)
                            index = quotes.index(response) + 1
                            sendMsg(s, 'Quote '+str(index)+': '+response)
                        elif command == 'quotes':
                            for index, quote in enumerate(quotes):
                                index = index+1
                                print(index, quote)
                                response = 'Quote '+str(index)+': '+quote
                                sendMsg(s, response)
    # Failure to receive data, disconnected
    except:
        reconnect()
