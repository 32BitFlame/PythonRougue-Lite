import colorama
from termcolor import colored
colorama.init()
fgColors = [
    "white",
    "red",
    "green",
    "blue",
    "gray"
]
def mparse(string : str):
    escaped = False
    escapedContext = ""
    val : str = ""
    for char in string:
        if(char == "[" and not escaped):
            escaped = True
            continue
        if(char == "[" and escaped):
            val += "["
            continue
        if(escaped and char == "]"):
            escaped = False
            val += _handle(escapedContext)
            continue
        if(escaped):
            escapedContext += char
            continue
        val += char
    return val
def _handle(data : str):
    global fgColors
    colorContext = [None, None]
    uncoloredText= ""
    for i in range(len(data)):
        if(i == 0):
            colorContext[i] =  fgColors[int(data[i])]
            continue
        if(i == 1):
            try:
                colorContext[i] =  "on_" + fgColors[int(data[i])]
            except:
                colorContext[i] = None
            continue
        uncoloredText += data[i]
    return colored(uncoloredText, colorContext[0], colorContext[1])

if(__name__ == "__main__"):
    print(mparse(input("string: ")))