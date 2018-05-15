import os

def clear():
    try:
        os.system('clear')
    except:
        try:
            os.sytem('cls')
        except:
            pass