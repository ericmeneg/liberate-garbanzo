#by ericmeneg
#This code simulates the effects of the algorythm used in the pokemon ultra sun and pokemon ultra moon games to determine random encounters in mount hokulani's first two fields at the foot of the mountain during the day, as listed on bulbapedia
import random
def species_det():
    species_check = random.randrange(0,101)
    held_item_type = 0
    held_item_odds = 0 
    held_item_type_two = 0
    held_item_odds_two = 0
    if species_check <=30:
        species = "Fearow"
        genderless = False
        held_item_odds = 5
        held_item_type = "Sharp Beak"
    elif 40>=species_check>30:
        species = "Ditto"
        held_item_odds = 5
        held_item_odds_two = 55
        held_item_type = "Metal Powder"
        held_item_type_two = "Quick Powder"
        genderless = True
    elif 50>=species_check>40:
        species = "Skarmory"
        held_item_odds = 5
        held_item_type = "Metal Coat"
        genderless = False
    elif 60>=species_check>50:
        species = "Elekid"
        held_item_odds = 5
        held_item_type = "Electririzer"
        genderless = False
    elif 70>=species_check>60:
        held_item_odds = 5
        held_item_type = "Metal Coat"
        species = "Beldum"
        genderless = True
    elif 90>=species_check>70:
        species = "Elgyem"
        held_item_odds = 0
        held_item_type = None
        genderless = False
    elif 100>=species_check>90:
        species = "Minior"
        genderless = True
    print(species)
    return genderless,held_item_odds,held_item_type,held_item_odds_two,held_item_type_two

def held_item(held_item_odds,held_item_type,held_item_odds_two,held_item_type_two):
    check = random.randrange(1,101)
    if check <= held_item_odds:
        print("The pokemon is holding a",held_item_type)
    elif check <= held_item_odds_two and held_item_odds_two != 0:
        print("The pokemon is holding a",held_item_type_two)

def gender_det(genderless):
    if genderless == True:
        gender = "Genderless"
    else:
        gender = random.randrange(1,3)
        if gender == 1:
            gender = "M"
        else:
            gender = "F"
    print(gender)

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
    affected_stat = random.randrange(1,7)
    if affected_stat == 1:
        affected_stat = "HP"
    elif affected_stat == 2:
        affected_stat = "Atk"
    elif affected_stat == 3:
        affected_stat = "Def"
    elif affected_stat == 4:
        affected_stat = "Sp. Atk"
    elif affected_stat == 5:
        affected_stat = "Sp. Def"
    elif affected_stat == 6:
        affected_stat = "Spe"
    return affected_stat

genderless,held_item_odds,held_item_type,held_item_odds_two,held_item_type_two = species_det()
level_det()
gender_det(genderless)
held_item(held_item_odds,held_item_type,held_item_odds_two,held_item_type_two)
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
    genderless,held_item_odds,held_item_type,held_item_odds_two,held_item_type_two = species_det()
    level_det()
    gender_det(genderless)
    held_item(held_item_odds,held_item_type,held_item_odds_two,held_item_type_two)
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

    if shiny == True:
        print("Shiny found after",count,"encounters")
        break'''