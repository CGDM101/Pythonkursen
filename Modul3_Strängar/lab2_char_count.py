# TASK 2 - COUNT ALPHABETICAL AND NUMERICAL CHARACTERS

# Write a python program that takes a string as input and outputs the number of alphabetical and numerical characters in it.

text = input('Enter a string: ').lower()
antal_bokstäver = 0
antal_siffror = 0
siffror = '0123456789'
bokstäver = 'abcdefghijklmnopqrstuvwxyz'

for tecken in text:
    if tecken in siffror:
        antal_siffror += 1
    if tecken in bokstäver:
        antal_bokstäver += 1

print(f'{antal_bokstäver} letters and {antal_siffror} decimals')


# The following examples show test runs of the program

# Enter a string: Churchill was born on the 30th of November 1874
# 33 letters and 6 decimals

# Enter a string: The coldest year on record occurred in 1904
# 32 letters and 4 decimals

# Enter a string: Santa Claus is coming to town
# 24 letters and 0 decimals
