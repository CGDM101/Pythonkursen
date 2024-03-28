# TASK 2 - THE MAIN PROGRAM

# Write a python program that uses the function from Task 1 by importing the file it was saved in as module. The program must prompt the use for arguments A, B, and L and output the list returned by the function.

from lab_funcs import in_range

a = int(input('Enter left value: '))
b = int(input('Enter right value: '))
l = input('Enter numbers separated by spaces: ').split()
ny = []
for item in l:
    ny.append(int(item))

result = in_range(a, b, ny)
print(result)


# Below is an example of the program execution usage

# Enter left value: 10
# Enter right value: 12
# Enter numbers separated by spaces: 56 -3 10 11 1098 12 2
# [2, 3, 5]



# Från testerna:

# 0
# 3
# -1 2 23 65 3 235 0
# [1, 4, 6]

# 10
# 15
# 1 43 7 11 94 4 10 14 5 15
# [3, 6, 7, 9]