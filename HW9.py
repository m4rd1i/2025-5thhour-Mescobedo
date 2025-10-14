#Name:
#Class: 6th Hour
#Assignment: HW9
import random
from selectors import SelectSelector

#1. Print "Hello World!"
print("Hello World!")

#2. Create a list with three variables that each randomly generate a number between 1 and 100
mardiList = [random.randint (1,100), random.randint (1,100), random.randint (1,100)]

#3. Print the list.
print(mardiList)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if mardiList[0] >= mardiList[1] and mardiList[0] >= mardiList[2]:
    print(f"{mardiList[0]} is the largest")
elif mardiList[1] >= mardiList [0] and mardiList [1] >=mardiList[2]:
    print(f"{mardiList[1]} is the largest")
    num = mardiList[1]
elif mardiList[2] >= mardiList[0] and mardiList[2] >= mardiList[1]:
    print(f"{mardiList[2]} is the largest")
    num = mardiList[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(mardiList)
print(num)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("Num is divisible by both")
    else:
        print("Num is divisible by 2, but not 3")
else :
  if num % 3 == 0:
        print("Num is divisible by 3, but not 2")
  else:
      print("Num is divisible by neither")
