import string
from Socket import sendMsg

# Display server messages on login
def joinRoom(s):
    readbuffer = ''
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode('UTF-8')
        temp = readbuffer.split('\n')
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMsg(s, 'Successfully joined chat!')
    
# Check for final line of server messages to determine successful connection
def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
    
