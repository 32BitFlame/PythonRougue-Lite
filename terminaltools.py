def clear():
    '''clears the terminal'''
    from os import system
    try:
        system("cls")
    except:
        system("clear")
    