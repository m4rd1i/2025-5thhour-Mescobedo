#Name: Maricella Escobedo
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random

#2. print "Hello World!"
print("Hello World!")

#3. Create three different variables that each randomly generate an integer between 1 and 10
D10 = random.randint(1,10)
D20 = random.randint(1,10)
D100 = random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(D10, D20, D100)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
whatever = 2 + D10
hi = D20 - 4
what = D100 * 1.5

#6. Print each result from #5 on the same line.
print (whatever, hi, what)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
listOne = [random.randint (1, 6), random.randint (1, 6), random.randint (1, 6), random.randint (1, 6)]

#8. Sort the list in #7 and print it.
listOne.sort()
print(listOne)

#9. Add together the highest three numbers in the list from #7 and print the result.
print(listOne [1] + listOne[2] + listOne[3])

#10. Create a list with 5 names of other students in this class and print the list.
nameList = ["Diana", "Waylon", "Ashton", "Jazmine", "Casandra"]

print(nameList)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(nameList)
print(nameList)

#12. Print a random choice from the list of names from #10.
print(random.choice(nameList))