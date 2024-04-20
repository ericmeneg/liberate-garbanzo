#by ericmeneg
#This code simulates the effects of the algorythm used in the pokemon ultra sun and pokemon ultra moon games to determine random encounters in mount hokulani's first two fields at the foot of the mountain during the day, as listed on bulbapedia
import random
def species_det():
    genderless = False
    species_pool = ["Fearow","Ditto","Skarmory","Elekid","Beldum","Elgyem","Minior"]
    species = random.choices(species_pool, weights=(30,10,10,10,10,20,10), k=1)[0]
    if species == "Ditto" or species == "Beldum" or species == "Minior":
        genderless = True
    print(species)
    return species,genderless

def ability_def(species):
    ability_check = random.randrange(1,3)
    if species == "Fearow":
        ability = "Keen Eye"
    elif species == "Ditto":
        ability = "Limber"
    elif species == "Skarmory" and ability_check == 1:
        ability = "Keen Eye"
    elif species == "Skarmory" and ability_check == 2:
        ability = "Sturdy"
    elif species == "Elekid":
        ability = "Static"
    elif species == "Beldum":
        ability = "Clear body"
    elif species == "Elgyem" and ability_check == 1:
        ability = "Telepathy"
    elif species == "Elgyem" and ability_check == 2:
        ability = "Synchronize"
    elif species == "Minior":
        ability = "Shields down"
    print("It's ability is",ability)

def form_det():
    color_pool = ["red","orange","yellow","green","blue","violet"]
    color = random.choice(color_pool)
    print("It has a",color,"core")

def held_item(species):
    itemcheck = random.randrange(1,101)
    item = None
    if species == "Fearow" and itemcheck<=5:
        item = "Sharp Beak"
    if species == "Ditto":
        itempool = ["Quick Powder","Metal Powder", None]
        item = random.choices(itempool, weights=(50,5,45))
    if species == "Skarmory" and itemcheck<=5:
        item = "Metal Coat"
    if species == "Elekid" and itemcheck<=5:
        item = "Electirizer"
    if species == "Beldum" and itemcheck<=5:
        item = "Metal Coat"
    if species =="Minior" and itemcheck<=5:
        item = "Star Piece"
    if item != None:
        print("It's holding a",item)

def gender_det(genderless):
    if genderless == True:
        print("Genderless")
    else:
        genderpool = ["M","F"]
        print(random.choice(genderpool))

def level_det():
    print("Level",random.randrange(27,31))

def iv_gen(stat):
    iv = str(random.randrange(0,32))
    print(stat+":",iv)

def shininess_check():
    shiny_check = random.randrange(0,4097)
    if shiny_check == 4096:
        print("It's shiny form")
        shiny = True
    else:
        print("It's regular form")
        shiny = False
    return shiny

def nature_det():
    stats = ["HP","Atk","Def","Sp. Atk","Sp. Def","Spe"]
    affected_stat = random.choice(stats)
    return affected_stat

species,genderless = species_det()
level_det()
gender_det(genderless)
ability_def(species)
if species == "Minior":
    form_det()
held_item(species)
shininess_check()
iv_gen("HP")
iv_gen("Atk")
iv_gen("Def")
iv_gen("Sp. Atk")
iv_gen("Sp. Def")
iv_gen("Spe")
lowered_stat = nature_det()
raised_stat = nature_det()
if lowered_stat == raised_stat:
    print("The pokemon's nature will not affect it's stats")
else:
    print("The pokemon's nature will lower it's",lowered_stat,"and raise it's",raised_stat)

#If the following lines are habilitated then the code will run until a shiny pokemon is found, that can be used to simulate a shiny hunt:
'''count = 0
while True:
    count += 1
    species,genderless = species_det()
    level_det()
    gender_det(genderless)
    ability_def(species)
    if species == "Minior":
        form_det()
    held_item(species)
    shiny = shininess_check()
    iv_gen("HP")
    iv_gen("Atk")
    iv_gen("Def")
    iv_gen("Sp. Atk")
    iv_gen("Sp. Def")
    iv_gen("Spe")
    lowered_stat = nature_det()
    raised_stat = nature_det()
    if lowered_stat == raised_stat:
        print("The pokemon's nature will not affect it's stats")
    else:
        print("The pokemon's nature will lower it's",lowered_stat,"and raise it's",raised_stat)
    print("====================================================================")

    if shiny == True:
        print("Shiny found after",count,"encounters")
        break'''