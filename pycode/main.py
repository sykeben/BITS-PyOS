import posgeneral as pg

pg.clear()
print "BITS-PyOS Console"
print "(C) 2018 Benjamin Sykes."
print ""
print "Loading libraries . . ."
print "- \"sleep\" from \"time\""
from time import sleep
print ""

print "### COUNTING UP DEMO ###"
print "There is no true kernel for PyOS yet, so this just shows that it works."
n = 0
while True:
    n += 1
    print str(n)
	sleep(1)