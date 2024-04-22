#by ericmeneg
#This code takes the encounter odds for a pokemon species and simulates a shiny hunt at base 1/4096 odds in that area, counting every shiny of an undesired species found along the way
import random; import time
count=0
phases=0
odds = int(input("Type species encounter odds (in integer percentage, without %): "))

#weighted choices method
while True:
    count += 1
    valueshiny = random.randrange(1,4097)
    valuespecies = random.choices(["desired","undesired"], weights=[odds,(100-odds)], k=1)[0]
    if valueshiny == 4096 and valuespecies == "desired":
        print("Encounters:",count,"Phases:",phases,"*S*")
        break
    elif valueshiny == 4096 and valuespecies == "undesired":
        print(count,"S")
        phases += 1
        time.sleep(0.5)
    else:
        print(count,"N")

#<= randrange method
'''while True:
    count += 1
    valueshiny = random.randrange(1,4097)
    valuespecies = random.randrange(1,101)
    if valueshiny == 4096 and valuespecies <=odds:
        print("Encounters:",count,"Phases:",phases,"*S*")
        break
    elif valueshiny == 4096 and valuespecies>10:
        print(count,"S")
        phases += 1
    else:
        print(count,"N")'''

#no species consideration
'''count=0
shinies=0
totalcount=0
while True:
    count += 1
    valor = random.randrange(1,4097)
    if valor != 4096:
        print(count,"N")
    if valor == 4096:
        print(count,"S")
        shinies= shinies+1
        totalcount = totalcount+count
        count=0
    if shinies == 5:
        print("Encounters:",totalcount)
        break'''