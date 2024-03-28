# TASK 1 - WORDS WITH EVEN NUMBER OF VOWELS

# Write a python program that prompts the user to enter several words separated by spaces. 
# The program then creates a new lists to which it adds words from the entered list that contain 
# even number of vowels. Vowels are letters "a", "e", "i", "o", "u" .

ordlista = input('Skriv in flera ord, separerade med mellanslag.').split()
vokaler = 'aeiou'
ord_med_jämnt_antal_vokaler = []

for ord in ordlista:
    antal_vokaler_per_ord = 0
    for bokstav in ord:
        if bokstav in vokaler:
            antal_vokaler_per_ord += 1
    if antal_vokaler_per_ord % 2 == 0: 
        ord_med_jämnt_antal_vokaler.append(ord)

print(ord_med_jämnt_antal_vokaler)


# The following example shows a test run of the program

# $ python3 even_vowels.py
# Enter words separated by spaces: hello yes apple ananas aircraft
# [hello, apple]

# $ python3 even_vowels.py
# Enter words separated by spaces: confusion letter writer station kitten
# [confusion, letter, writer, kitten]