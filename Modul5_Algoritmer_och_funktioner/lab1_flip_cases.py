# TASK 1 - FLIP CASES IN A STRING


# Write a python program that prompts the user to enter a string. The program then converts the string to a list of characters and passes it to a function named flip_case that changes lower case letters to upper case letters and upper case letters to lower case letters. The function must return the lens of the string. The program must print the output from the function as wells as the string with flipped cases to the user. HINT: to convert a list to string use following method: "".join(my_list)

# The following example shows a test run of the program

# $ python3 flip_cases.py
# Enter a string: oNCe THeRe WAS A dOG
# 20
# OncE thErE was a Dog

# $ python3 flip_cases.py
# Enter a string: PanCakes aRe gOOD wiTh JaM
# 26
# pANcAKES ArE Good WItH jAm



def flip_case(original_string):
    new_string = ''
    for i in range(len(original_string)):
        if original_string[i].islower():
            new_string +=original_string[i].upper()
        if original_string[i].isupper():
            new_string +=original_string[i].lower()
        if original_string[i] == ' ':
            new_string += ' '
    return new_string

print('Enter a string: ')
input_string = input()
returned = flip_case(input_string)
print(f'{len(returned)}\n{returned}')