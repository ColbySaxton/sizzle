from server import *
import random
print(getEvents())
print(getHotspots())
n = 2.9
for i in range(10):
    geoTally(i,16+n*random.random(),16+n*random.random())
    geoTally(10+i,-1+n*random.random(),-1+n*random.random())
    geoTally(20+i,100+n*random.random(),1+n*random.random())
    geoTally(30+i,-30+n*random.random(),-30+n*random.random())
    geoTally(40+i,200+n*random.random(),200+n*random.random())


updateCounts()
print(getEvents())
print(getHotspots())
