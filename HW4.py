#Name: Maricella Escobedo
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.
mardisList = ["Mardi", "Waylon", "Diana", "Casandra", "Juliana"]

#2. Append a new name onto the Name List.
mardisList.append("Juliana")

#3. Print out the 4th name on the list.
print(mardisList[3])

#4. Create a list with 4 different integers in it.
maricellasList = [12, 9, 4, 21]

#5. Insert a new integer into the 2nd spot and print the new list.
maricellasList.insert(1,6)
print(maricellasList)

#6. Sort the list from lowest to highest and print the sorted list.
maricellasList.sort()
print(maricellasList)

#7. Add the 1st three numbers on the sorted list together and print the sum.
print(maricellasList[0] + maricellasList[1] + maricellasList[2])

#8. Create a list with two strings, two variables, and too boolean values.
everythingList = ["Cali", "Mae Mae", 9, 4, False, True]
print(everythingList)

#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(everythingList[int(input())])