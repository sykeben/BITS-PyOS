import posgeneral as pg

pg.clear()
print "BITS-PyOS Console"
print "(C) 2018 Benjamin Sykes."
print ""
print "Loading libraries . . ."
print "- \"sleep\" from \"time\""
from time import sleep
print ""

print "There is no true kernel for PyOS yet,"
print "so the following demos show that it works."
print ""

print "### COUNTING UP DEMO ###"
print "This will count from 0 to 10."
for n in range(0, 10):
    n = n + 1
    print str(n)
    sleep(0.25)
print ""

print "### SYSTEM INFO DEMO ###"
print "Not implimented yet!"
print "Exiting in 3 seconds . . ."
sleep(3)