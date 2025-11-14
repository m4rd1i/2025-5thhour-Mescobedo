#Name: Maricella Escobedo
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

players = int(input("How many players do you have?: "))
ratings = []
for number in range(players):
    rate = int(input("Rating between 1 to 5: "))
    while rate < 1 or rate > 5 :
        print("The rating is out of range")
        rate = int(input("Rating between 1 to 5: "))
    else:
        ratings.append(rate)
sum = sum(ratings)
average = sum / players
print(average)