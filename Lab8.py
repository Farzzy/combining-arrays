# Program Name: Lab8.py
# Course: IT1114/Section W02
# Student Name: Farzam Dizna
# Assignment Number: Lab8
# Due Date: 03/26/2023
# Purpose: This program will combine two integer arrays into one larger array and remove any duplicate values. Then it will sort and print out the final combined array. 
# Source1: https://www.w3schools.com/python/python_arrays.asp
# Source2: https://pynative.com/python-random-randrange/
# Source3: https://www.geeksforgeeks.org/sort-in-python/
# Source4: https://www.geeksforgeeks.org/python-set-method/
# Source5: https://www.datacamp.com/tutorial/sets-in-python
# Source6: https://realpython.com/sorting-algorithms-python/

import random

N = int(input("Enter a positive integer greater than 1: "))     # takes in the users input for N

array1 = [random.randint(0, 500) for _ in range(N)]             # creates the first array from 0 to 500 with N elements
array2 = [random.randint(0, 500) for _ in range(N)]             # creates the second array from 0 to 500 with N elements

array3 = array1 + array2                                        # adds the first and second arrays to create the third array
array3 = list(set(array3))                                      # lists and removes any duplicate values

for i in range(len(array3)):                                    # sorts the array using bubble sort
    for j in range(len(array3) - i - 1):                        
        if array3[j] > array3[j + 1]:                           # if the item we are looking at is greater than its adjacent value then we swap them
            array3[j], array3[j + 1] = array3[j + 1], array3[j]

for num in array3:                                              # prints the values from the final array
    print(num)