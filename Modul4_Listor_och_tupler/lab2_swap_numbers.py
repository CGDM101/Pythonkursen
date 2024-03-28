# TASK 2 - SWAP NUMBERS IN A LIST

# Write a python program that prompts the user enter a several integer numbers separated by spaces. 
# The program then prints this list where each evenly indexed element is swapped with its next oddly indexed neighbour.


heltalslista = [int(c) for c in input('Skriv in en serie heltal, separerade med mellanslag. ').split()]

for i in range(0, len(heltalslista), 2):
    if i + 1 < len(heltalslista):
        heltalslista[i], heltalslista[i+1] = heltalslista[i+1], heltalslista[i]

print(heltalslista)


# The following example shows a test run of the program

# $ python3 swap_numbers.py
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 
# [2, 1, 4, 3, 6, 5, 7]

# $ python3 swap_numbers.py
# Enter numbers separated by spaces: 15 9 24 100 31 68 71 95 
# [9, 15, 100, 24, 68, 31, 95, 71]