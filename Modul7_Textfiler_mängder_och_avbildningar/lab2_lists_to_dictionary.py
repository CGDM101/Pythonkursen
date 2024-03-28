# TASK 2 - CONVERT TWO LISTS INTO A DICTIONARY

# Write a python program that asks the user to enter two sequences of words separated by spaces. The program then constructs a dictionary where words in the first list are used as keys and words in the second sequence are used as values. If the sequences are of unequal lengths, the program must print following error message: "Lists are of unequal sizes".

# Exempel:
# Enter keys separated by spaces: one two three four five
# Enter values separated by spaces: red fox jumps over tree
# {'one': 'red', 'two': 'fox', 'three': 'jumps', 'four': 'over', 'five': 'tree'}

# Enter keys separated by spaces: I see sky of blue and trees of green
# Enter values separated by spaces: 9 8 7 6 5 4 3 2 1
# {'I': '9', 'see': '8', 'sky': '7', 'of': '2', 'blue': '5', 'and': '4', 'trees': '3', 'green': '1'}

keys = input('Enter keys separated by spaces: ').split()
values = input('Enter values separated by spaces: ').split()

dictionary = {}
if len(keys) == len(values):
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    print(dictionary)
else:
    print('Lists are of unequal sizes')
