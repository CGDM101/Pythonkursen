# TASK 1 - REVERSE LINE ORDER IN A TEXT FILE

# Write a python program that asks the user to enter name of a text file containing lines of text and rewrites the file with the same lines in reverse order.

# Red fox lives in the woods
# Rabbit lives in the hole
# Fish swims in the lake
# Birds fly in the sky

# After the program execution the file would contain following:

# Birds fly in the sky
# Fish swims in the lake
# Rabbit lives in the hole
# Red fox lives in the woods

filename = input(
    'Enter name of a text file containing lines of text ')  # fil.txt

with open(filename) as f:
    content = f.readlines()

reversed = content[::-1]

with open(filename, 'w') as f:
    f.writelines(reversed)


# print(reversed[0])
# for i in range(1, len(reversed)):
#     print(reversed[i], end='')
