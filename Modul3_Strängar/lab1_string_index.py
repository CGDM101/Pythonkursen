# TASK 1 - PRINT A CHARACTER IN A GIVEN POSITION OF A STRING

# Write a python program that takes as input a string and an integer value and outputs the character found in the index position indicated by the integer value. If entered integer value represents a position outside of the valid index value for the string, the program must print a message prompting the user that the index is out of bounds.

string = input('Enter a string: ')
position = int(input('Enter position: '))
if position < len(string):
    print(string[position])
else:
    print('Index out of bounds')


# The following examples show test runs of the program

# Enter a string: This is a great day
# Enter position: 0
# T

# Enter a string: The sky is blue
# Enter position: 20
# Index out of bounds

# Enter a string: Red fox is hunting
# Enter position: 4
# f
