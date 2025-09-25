#Name:
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

enemyDict = {
    "Enemy1" : {
    "Name" : "Bryson",
    "Ability" : "Flying",
    "Damage" :10,
    "Health" :100,
},
    "Enemy2" : {
    "Name" : "Waylon",
    "Ability" : "Strength",
    "Damage" : 20,
    "Health" : 100,
    },
    "Enemy3" : {
    "Name" : "Ashton",
    "Ability" : "Invisibility",
    "Damage" : 5,
    "Health" : 100,
    },
    "Enemy4" : {
    "Name" : "Tucker",
    "Ability" : "Telekenisis",
    "Damage" : 10,
    "Health" : 100,
    },
    "Enemy5" : {
    "Name" : "Angel",
    "Ability" : "Time Traveler",
    "Damage" : 15,
    "Health" : 100,
    }
}
enemyDict["Enemy1"]["Damage"] = int(input("Bryson's Damage:"))
print(enemyDict["Enemy1"])
enemyDict["Enemy2"]["Damage"] = int(input("Waylon's Damage:"))
print(enemyDict["Enemy2"])
enemyDict["Enemy3"]["Damage"] = int(input("Ashton's Damage:"))
print(enemyDict["Enemy3"])
enemyDict["Enemy4"]["Damage"] = int(input("Tucker's Damage:"))
print(enemyDict["Enemy4"])
enemyDict["Enemy5"]["Damage"] = int(input("Angel's Damage:"))
print(enemyDict["Enemy5"])


