#Name:
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
mardiDict = {
    "Name": "Mardi",
    "Age": "18",
    "Bday": [8, 17, 2007],
}

#3. Print the keys of the dictionary from #2.
print(mardiDict.keys())

#4. Print the values of the dictionary from #2
print(mardiDict.values())

#5. Print one of the three numbers from the list by itself
print(mardiDict["Bday"][0])

#6. Using the update function, add a fourth key to the dictionary and give it a value.
mardiDict.update({"Month" : "September"})

#7. Print the entire dictionary from #2 with the updated key and value.
print(mardiDict)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
fifthHourClass = {
   "Student 1": {
    "Name": "Waylon",
    "Age": "18",
   },
    "Student 2": {
        "Name": "Diana",
        "Age": "17",
    },
    "Student 3": {
        "Name": "Ashton",
        "Age": "16"
    }
}

#9. Print the names of all three classmates on the same line.
print(fifthHourClass.keys())

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
fifthHourClass.pop("Student 3")
print(fifthHourClass)