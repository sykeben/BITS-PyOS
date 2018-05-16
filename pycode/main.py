print "BITS-PyOS Console"
print "(C) 2018 Benjamin Sykes."
print ""

print "Loading libraries . . ."
print "- input from bits"
from bits import input as binput
print "- sleep from time"
from time import sleep
print ""

print "Defining functions . . ."
print "- cls"
def cls():
    print "\n"*150
print ""

print "WARNING: This is a WIP."
sleep(2.5)

quitCall = False
current = "main"
while not quitCall:
    
    while current == "main":
        cls()
        print " ###### MAIN MENU ######"
        print " # [0] Quit            #"
        print " # [1] Applications    #"
        print " # [2] Information     #"
        print " #######################"
        print " Press a corrisponding key . . ."
        moveOn = False
        while not moveOn:
            key = str(binput.get_key().key)
            if key == "0":
                quitCall = True
                current = "quit"
                moveOn = True
            elif key == "1":
                current = "apps"
                moveOn = True
            elif key == "2":
                moveOn = True
                cls()
                print " ###### ERROR ######"
                print " # Feature not     #"
                print " # installed.      #"
                print " ###################"
                print " Closing in 3 seconds . . ."
                sleep(3)
    
    while current == "apps":
        cls()
        print " ###### APPLICATIONS ######"
        print " # [0] Back               #"
        print " ##########################"
        print " Press a corrisponding key . . ."
        moveOn = False
        while not moveOn:
            key = str(binput.get_key().key)
            if key == "0":
                current = "main"
                moveOn = True