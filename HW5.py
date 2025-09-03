#Name:Maricella Escobedo
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
numList = [3, 6, 9, 12, 15, 18, 21, 24, 27]
#2. Sort the list from highest to lowest.
numList.sort(reverse=True)

#3. Create an empty list.
mardiList = []

#4. Remove the median number from the first list and add it to the second list.
numberFifteen = numList[4]
numList.pop(4)
mardiList.append(numberFifteen)

#5. Remove the first number from the first list and add it to the second list.
numberThree = numList[0]
numList.pop(0)
mardiList.append(numberThree)

#6. Print both lists.
print(mardiList)
print(numList)

#7. Add the two numbers in the second list together and print the result.
poopFartList = (mardiList[0] + mardiList[1])
print(poopFartList)

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
mardiList.pop(1)
mardiList.pop(0)

#9. Sort the first list from lowest to highest and print it.
numList.sort()
print(numList)