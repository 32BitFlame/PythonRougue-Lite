from terminaltools import *
import json
from readchar import readkey as readchar
import colorama
from quickANSImark import mparse
colorama.init()
def init():
    MAX_WIDTH = 100
    MAX_HEIGHT = 20
    MIN_WIDTH = 50
    MIN_HEIGHT = 10
    settings : dict = {}
    confsKeys = {
        "K_UP":None,
        "K_DOWN":None,
        "K_LEFT":None,
        "K_RIGHT":None,
        "K_INV":None,
        "K_ATTK":None,
        "K_ENTER":None
    }
    print("defaults initalized")
    print(confsKeys.keys())
    defaults = open("defaultskeys.json", "r")
    defaultsDict = json.loads(defaults.read())
    defaults.close()
    for key in confsKeys.keys():
        print("{0}: ".format(key))
        newVal = readchar()
        if(newVal != "\r"):
            confsKeys[key] = defaultsDict[key]
            continue
        confsKeys[key] = defaultsDict[key] 
    #Uncomment to overide defaults
    # f = open("defaultskeys.json", "w")
    # f.write(json.dumps(confsKeys))
    # f.close()
    dispWidth = MIN_WIDTH
    dispHeight = MIN_HEIGHT
    
    while True:
        clear()
        print("Press down to toggle height and right to toggle length(q to quit)")
        print("#"*dispWidth)
        for i in range(dispHeight-1): 
            print("#")
        inp = readchar()
        if(inp == "q"):
            break
        if(inp == confsKeys["K_DOWN"]):
            dispHeight+=1
        if(inp == confsKeys["K_UP"]):
            dispHeight-=1

        if(dispHeight > MAX_HEIGHT):
            dispHeight = MAX_HEIGHT
        elif(dispHeight < MIN_HEIGHT):
            dispHeight = MIN_HEIGHT
        
        if(inp == confsKeys["K_RIGHT"]):
            dispWidth+=1
        if(inp == confsKeys["K_LEFT"]):
            dispWidth-=1

        if(dispWidth > MAX_WIDTH):
            dispWidth = MAX_WIDTH
        elif(dispWidth < MIN_WIDTH):
            dispWidth = MIN_WIDTH
        
if(__name__ == "__main__"):
    init()