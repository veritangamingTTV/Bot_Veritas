import string

# Collect the username a message was sent by
def getUser(line):
    user = line.split(':', 2)[1].split('!',1)[0]
    return user

# Read server output
def getMsg(line, s):
    line = line.replace('\r','')
    msg = line
    # Check for server PING PONG [stay connected]
    if 'PING' in line.split(':',1)[0]:
        line = line.replace('PING','PONG')
        print(line)
        s.send(bytes('PONG :tmi.twitch.tv\r\n', 'utf-8'))
    # Read incoming message to log
    else:
        msg = line.split(':',2)[2]
    msg = msg.replace('\r','')
    return msg
