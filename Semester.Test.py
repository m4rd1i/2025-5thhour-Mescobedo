#Name: Maricella Escobedo
#Class: 5th Hour
#Assignment: Semester Project 1

import random
import time

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HP" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).
heroRoll = random.randint(1,20)
enemyRoll = random.randint(1,20)
if heroRoll >= enemyRoll:
    print("Hero goes first.")
    heroRoll = True
else:
    print("Enemy goes first")
    enemyRoll = False

#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses
heroRollAttack = random.randint(1,20)
print(heroRollAttack)
while partyDict["LaeZel"]["HP"] > 0 and enemyDict["Mindflayer"]["HP"] > 0:
    if heroRoll == True:
        print("LaeZel goes first.")
        heroRollAttack = random.randint(1,20)
        if heroRollAttack == 20:
            enemyDict["Mindflayer"]["HP"] -= (partyDict["LaeZel"]["Damage"] * 2)
            print(f"LaeZel hits Mindflayer for {(partyDict["LaeZel"]["Damage"] * 2)}")
        elif heroRollAttack == 1:
            print("LaeZel misses the hit on the Mindflayer.")
        elif heroRollAttack + partyDict["LaeZel"]["AtkMod"] >= enemyDict["Mindflayer"]["AC"]:
            enemyDict["Mindflayer"]["HP"] -= (partyDict["LaeZel"]["Damage"] + 2)
            print(f"LaeZel hits Mindflayer for {(partyDict["LaeZel"]["Damage"])}")
        else:
            print("LaeZel missed their attack")

        enemyRollAttack = random.randint(1, 20)
        print(enemyRollAttack)
        if enemyRollAttack == 20:
            partyDict["LaeZel"]["HP"] -= (enemyDict["Mindflayer "]["Damage"] * 2)
            print(f"Mindflayer hits LaeZel for {(enemyDict["Mindflayer"]["Damage"] * 2)}")
        elif enemyRollAttack == 1:
            print("Mindflayer misses the hit on the LaeZel.")
        elif enemyRollAttack + enemyDict["Mindflayer"]["AtkMod"] >= partyDict["LaeZel"]["AC"]:
            partyDict["LaeZel"]["HP"] -= (enemyDict["Mindflayer"]["Damage"] + 2)
            print(f"Mindflayer hits LaeZel for {(enemyDict["Mindflayer"]["Damage"])}")
        else:
            print("Mindflayer missed their attack.")

    else:
        print("Mindflayer goes first")
        enemyRollAttack = random.randint(1, 20)
        print(enemyRollAttack)
        if enemyRollAttack == 20:
            partyDict["LaeZel"]["HP"] -= (enemyDict["Mindflayer"]["Damage"] * 2)
            print(f"Mindflayer hits LaeZel for {(enemyDict["Mindflayer"]["Damage"] * 2)}")
        elif enemyRollAttack == 1:
            print("Mindflayer misses the hit on the LaeZel.")
        elif enemyRollAttack + enemyDict["Mindflayer"]["AtkMod"] >= partyDict["LaeZel"]["AC"]:
            partyDict["LaeZel"]["HP"] -= (enemyDict["Mindflayer"]["Damage"] + 2)
            print(f"Mindflayer hits LaeZel for {(enemyDict["Mindflayer"]["Damage"])}")
        else:
            print("Mindflayer missed their attack.")

        heroRollAttack = random.randint(1,20)
        if heroRollAttack == 20:
            enemyDict["Mindflayer"]["HP"] -= (partyDict["LaeZel"]["Damage"] * 2)
            print(f"LaeZel hits Mindflayer for {(partyDict["LaeZel"]["Damage"] * 2)}")
        elif heroRollAttack == 1:
            print("LaeZel misses the hit on the Mindflayer.")
        elif heroRollAttack + partyDict["LaeZel"]["AtkMod"] >= enemyDict["Mindflayer"]["AC"]:
            enemyDict["Mindflayer"]["HP"] -= (partyDict["LaeZel"]["Damage"] + 2)
            print(f"LaeZel hits Mindflayer for {(partyDict["LaeZel"]["Damage"])}")
        else:
            print("LaeZel missed their attack")

#3. If the attack hits, roll damage and subtract it from the target's hit points.



#4. The second in initiative rolls to attack (and rolls damage) afterwards.



#5. Repeat steps 2-5 until one of the characters is dead.

