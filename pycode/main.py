version = "0.0.3"
copyrightYear = "2018"
copyrightHolder = "Benjamin Sykes"

print "BITS-PyOS Version {0}".format(version)
print "(C) {0} {1}.".format(copyrightYear, copyrightHolder)
print ""

print "Loading libraries . . ."
print "- input from bits"
from bits import input as binput
print "- sleep from time"
from time import sleep
print "- listdir from os"
from os import listdir as ld
print "- isfile and join from os.path"
from os.path import isfile, join
print ""

print "Defining functions . . ."
print "- cls"
def cls():
    print "\n"*150
print ""

print "WARNING: This is a WIP."
sleep(1)

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
                current = "info"
    
    while current == "apps":
        
        cls()
        print " ###### APPLICATIONS ######"
        print " # [0] Back               #"
        print " # [1] Other PyApp...     #"
        print " # [2] Test Application   #"
        print " ##########################"
        print " Press a corrisponding key . . ."
        
        moveOn = False
        currentApp = "none"
        while not moveOn:
            key = str(binput.get_key().key)
            if key == "0":
                current = "main"
                currentApp = "quit"
                moveOn = True
            if key == "1":
                currentApp = "other..."
                moveOn = True
            if key == "2":
                currentApp = "testapp"
                moveOn = True
        
        if currentApp == "other...":
        
            cls()
            print " Loading . . ."
            temp = range(1, 9)
            menuIDs = list()
            for i in temp:
                menuIDs.append(str(i))
            for i in list("abcdefghijklmnopqrstuvwxyz"):
                menuIDs.append(i)
            pyFiles = [f for f in ld("/pyos/apps") if isfile(join("/pyos/apps", f))]
            menuItems = list()
            itemCount = 0
            for i in pyFiles:
                itemCount = itemCount + 1
                menuItems.append(i)
            
            cls()
            print " ~##### OTHER . . . #####~"
            print " [0] Back"
            temp = -1
            for j in menuItems:
                temp = temp + 1
                print " [{0}] {1}".format(menuIDs[temp], j)
            print " ~## Press a key . . . ##~"
            
            moveOn = False
            while not moveOn:
                key = str(binput.get_key().key).lower()
                appToLaunch = "none"
                if key == "0":
                    moveOn = True
                temp = -1
                for j in menuIDs:
                    temp = temp + 1
                    if key == j:
                        if temp <= len(menuItems):
                            appToLaunch = menuItems[temp]
                            moveOn = True
            
            if appToLaunch != "none":
                cls()
                print " You selected: {0}".format(appToLaunch)
                binput.get_key()
        
        if currentApp == "testapp":
            
            cls()
            print " ~####### TEST APPLICATION #######~"
            print ""
            print " #     #\n #     # ###### #      #       ####\n #     # #      #      #      #    #\n ####### #####  #      #      #    #\n #     # #      #      #      #    # ###\n #     # #      #      #      #    # ###\n #     # ###### ###### ######  ####   #\n                                     #\n \n #     #                             ###\n #  #  #  ####  #####  #      #####  ###\n #  #  # #    # #    # #      #    # ###\n #  #  # #    # #    # #      #    #  #\n #  #  # #    # #####  #      #    #\n #  #  # #    # #   #  #      #    # ###\n  ## ##   ####  #    # ###### #####  ###"
            print ""
            print " ~###### Press any key . . . #####~"
            binput.get_key()
    
    while current == "info":
        
        cls()
        print " ~####### INFORMATION #######~"
        print ""
        print " BITS-PyOS Version: {0}".format(version)
        print " Copyright Year:    {0}".format(copyrightYear)
        print " Copyright Holder:  {0}".format(copyrightHolder)
        print ""
        print " ~### Press any key . . . ###~"
        binput.get_key()
        current = "main"