import math
import matplotlib.pyplot as plt

def d(num,size):
    return num*((size/2)+.5)

baseSP = [4,4,6,6,14,14,17,17,27,27,32,32,38,38,44,44,57,57,64,64]
print(baseSP)
arcSP = [4,4,9,10,19,20,24,25,36,37,43,44,51,52,59,60,74,75,83,84]
print(arcSP)
arcInfSP = [4,4,9,10,19,20,24,25,42,45,51,52,59,62,69,70,84,87,95,96]
print(arcInfSP)
arcCapSP = [4,4,9,10,19,20,24,25,42,45,51,52,59,62,80,81,95,99,107,108]
print(arcCapSP)
fullSP = [4,6,14,17,27,32,38,44,57,64,73,73,83,83,94,94,107,114,123,133]
print(fullSP)
sorcSP = [4,8,17,21,32,38,45,52,66,74,84,85,96,97,109,110,124,132,142,153]
print(sorcSP)

level = 5
mod = 5
targets = 2.5
arcDie = d(1,4)
#todo: levels 3-4. They important
def firebolt():
    if(level < 5):
        return d(1,10)
    if(level < 11):
        return d(2,10)
    if(level < 17):
        return d(3,10)
    return d(4,10)
def scorchingRay():
    return d(6,6)
def fireball():
    return d(8,6)

def calcArcDmg(): # uses arcSP OR arcInfSP
    global arcCapSP
    tempDamage = 0
    if(level < 9):
        if(arcCapSP[level-1] >= 3):
            #scorching ray
            tempDamage += scorchingRay() + (arcDie * 2) * targets
            arcCapSP[level-1] -= 3
        else:
            #cantrips
            tempDamage += firebolt()
    if(level < 13):
        if(arcCapSP[level-1] >= 5):
            #FIREBALL
            tempDamage += (fireball() + (arcDie * 3)) * targets
            arcCapSP[level-1] -= 5;
        if(arcCapSP[level-1] >= 3):
            #scorching ray
            tempDamage += scorchingRay() + (arcDie * 2) * targets
            arcCapSP[level-1] -= 3
        else:
            #cantrips
            tempDamage += firebolt()
    return tempDamage

def calcArtDmg(): # uses baseSP
    global baseSP
    tempDamage = 0
    if(level < 9):
        if(baseSP[level-1] < 3):
            #cantrips
            tempDamage += firebolt() + d(1,8)
        else:
            #scorching ray
            tempDamage += scorchingRay() + d(1,8)
            baseSP[level-1] -= 3
        #Eldritch Canon
        tempDamage += d(2,8) + mod
    if(level < 13):
        if(baseSP[level-1] >= 5):
            #fireball
            tempDamage += (fireball() + d(1,8))*targets
            baseSP[level-1] -= 5
        if(baseSP[level-1] >= 3):
            #scorching ray
            tempDamage += scorchingRay() + d(1,8)
            baseSP[level-1] -= 3
        else:
            #cantrips
            tempDamage += firebolt() + d(1,8)
        #Eldritch Canon
        tempDamage += d(3,8) + mod
    return tempDamage

for j in range(5,13):
    level = j
    artDamage = []
    totalArtDamage = []
    arcDamage = []
    totalArcDamage = []
    for i in range(0,15):
        artDamage.append(calcArtDmg())
        if(i == 0):
            totalArtDamage.append(artDamage[0])
        else:
            totalArtDamage.append(totalArtDamage[i-1]+artDamage[i])
        arcDamage.append(calcArcDmg())
        if(i == 0):
            totalArcDamage.append(arcDamage[0])
        else:
            totalArcDamage.append(totalArcDamage[i-1]+arcDamage[i])
    print("Level: "+str(level))
    print(" this art: "+str(artDamage))
    print(" this arc: "+str(arcDamage))
    print("total art: "+str(totalArtDamage))
    print("total arc: "+str(totalArcDamage))

    difDamage = []
    for i in range(0,15):
        difDamage.append(totalArcDamage[i]-totalArtDamage[i])
        #difDamage.append(arcDamage[i]-artDamage[i])
    x = range(1,16)
    plt.plot(x,difDamage, label = "level "+str(level))

#plt.ylim([0,100])

plt.title("Targets: "+str(targets)+", Die Size: "+str(int(((arcDie-.5)*2))))
plt.legend()
plt.show()
