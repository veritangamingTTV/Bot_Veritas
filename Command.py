###
#  Bot will respond to commands listed in this file.
#  A dictionary file for specific lists will be added for
#  easier access and modification.
###

from Socket import sendMsg
import random

# Simple commands triggered by sending "!command"
comList =
{'build':
 'Ryzen 1500X (4.0GHz OC), Gigabyte AB350-M DS3-H, 16GB DDR4 2133MHz (2666MHz OC), EVGA GTX 960, 250GB SATA M.2, 1.5TB HDD',
 'hello':'Hallew!',
 'lurk':"Lurking's kinda my thing, too! Hope you're back soon!"}

# Commands requiring parameters "!command parameters"
paramList =
{'addquote':'Quote added!',
 'quote':'Fetching...'}

# List of quotes used by "!quote"
quotes =
['"Do or do not, there is no try." - Master Yoda',
 '"To infinity, and beyond!" - Buzz Lightyear',
 '"Please stand clear of the doors. Por favor mantengase alejado de las puertas." - WDW Monorail System']

def execute(command, user, param=None):
    
    # Check for simple command
    if command in comList:
        print(user+' triggered '+command+'!')
        response = str(comList.get(command))
        print('Respond with: '+ response)
        sendMsg(s, str(response))

    #Check for parameters
    elif command in paramList:
        print(user+' triggered '+command+'!')
        if command == 'addquote':
            quotes.add(param)
            
    # Reverse the parameter input !mirror hello "olleh"
    elif command == 'mirror':
        response = param[::-1]
        print(response)
        sendMsg(s, str(response))

    # return a quote from list
    elif command == 'quote':
        response = random.choice(quotes)
        index = quotes.index(response)
        sendMsg(s, 'Quote '+str(index)+': '+response)
