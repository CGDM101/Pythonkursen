# TASK 2 - SWAP NUMBERS IN A LIST


# Write a python program that prompts the user to enter a word. The program then uses a function called word_matrix that constructs a nested list of size N x N where N is the length of the word. Each element of the nested list is set to the underscore symbol "_" except for the diagonal elements (that is, elements with index (i, i) ) that are set to the ith letter of the word.

# The following example shows a test run of the program

# $ python3 word_to_matrix.py
# Enter a string: moon
# m___
# _o__
# __o_
# ___n

# $ python3 word_to_matrix.py
# Enter a string: Trollhattan
# T__________
# _r_________
# __o________
# ___l_______
# ____l______
# _____h_____
# ______a____
# _______t___
# ________t__
# _________a_
# __________n


def word_matrix(word):
    for i in range(len(word)):
        for j in range(len(word)):
            if i == j:
                print(word[i], end='')
            else:
                print('_', end='')
        print()

word_matrix(input('Enter a word: '))