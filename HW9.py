#Name:
#Class: 6th Hour
#Assignment: HW9
import random

#1. Print "Hello World!"
print("Hello World!")

#2. Create a list with three variables that each randomly generate a number between 1 and 100
m1 = random.randint (1, 100)
m2 = random.randint (1, 100)
m3 = random.randint (1, 100)

mardiList = [m1, m2, m3]

#3. Print the list.
print(mardiList)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if m1 >= m2 and m1 >= m3:
    print("m1 is the highest number")
elif m2 >= m1 and m2 >= m3:
    print("m2 is the highest number")
elif m3 >= m1 and m3 >= m2:
    print("m3 is the highest number")

#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(mardiList)
print(num)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0 :
   print("Num is divisible by 2")
elif num % 3 == 0 :
   print("Num is divisible by 3")
elif num % 2 and num % 3 == 0 :
   print("Num is divisible by both")
else :
   print("Num is not divisible by either.")
