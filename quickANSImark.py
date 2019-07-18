import colorama
def dump(string : str):
    escaped = False
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
            continue
        if(escaped):
            print(char, end="")

        