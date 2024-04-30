#by ericmeneg
#This code simulates attempts at the dynamax lair in pokemon sword and shield, repeating until a shiny legendary pokemon is found (at odds of 1/100 for a shiny and 1/4 for that shiny to be the target)
import random; import time

count=0
phases=0

encounters = ["slot 1","slot 2","slot 3","legendary"]
while True:
    hasshiny = False
    hasshinylegend = False
    for x in encounters:
        encounter=x
        valueshiny = random.randrange(1,101)
        if valueshiny == 100 and encounter!="legendary":
            print("*S*")
            phases += 1
            hasshiny = True
        elif valueshiny == 100 and encounter == "legendary":
            print("*S*")
            hasshinylegend = True
        else:
            print("N")
    count += 1
    print("Attempts:",count)
    time.sleep(0.1)
    if hasshiny == True:
        time.sleep(1)
    if hasshinylegend == True:
        print("Phases:",phases)
        break