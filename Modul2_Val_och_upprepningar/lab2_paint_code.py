# TASK 2 - PAINT CODE

# Assume that a paint factory uses a code to denote color and finish for the manufactured paint. 
# In particular, the code contains three digits where the first two digits represent the color and 
# the last digit represents the finish. Further assume, that there are only five colours: 
# black, white, green, blue, and red represented by codes 00, 10, 20, 30, 40, respectively. 
# Also assume, that there are only two finishes: matt and glossy, represented by codes 0 and 1, respectively. 
# Thus, a black matt paint has code 000, while blue glossy paint has code 301.

# Write a python program that takes the paint code as input and returns the colour and the finish of the. 
# The program must detect incorrect code values by prompting "Color code unknown" and "Finish code unknown" 
# in cases where color or finish codes fall outside of the predefined values.


code = input('Enter paint code: ')

colour_code = f'{code[0]}{code[1]}'
finish_code = code[2]

colour = ''
finish = ''

match colour_code:
    case '00':
        colour = 'black'
    case '10':
        colour = 'white'
    case '20':
        colour = 'green'
    case '30':
        colour = 'blue'
    case '40':
        colour = 'red'
    case _:
        colour = 'Color code unknown'

match finish_code:
    case '0':
        finish = 'matt'
    case '1':
        finish = 'glossy'
    case _:
        finish = 'Finish code unknown'

print(f'Color: {colour}')
if finish == 'Finish code unknown':
    print(f'{finish}')
else:
    print(f'Finish: {finish}')



# $python3 paint_code.py
# Enter paint code: 000
# Color: black
# Finish: matt

# Enter paint code: 011
# Color: Color code unknown
# Finish: glossy

# Enter paint code: 409
# Color: red
# Finish code unknown

# Enter paint code: 200
# Color: green
# Finish: matt



# ALT:

if colour_code == '00':
    colour = 'black'
elif colour_code == '10':
    colour = 'white'
elif colour_code == '20':
    colour = 'green'
elif colour_code == '30':
    colour = 'blue'
elif colour_code == '40':
    colour = 'red'
elif colour_code != '00' or colour_code != '10' or colour_code != '20' or colour_code != '30' or colour_code != '40':
    colour = 'Color code unknown'

if finish_code == '0':
    finish = 'matt'
elif finish_code == '1':
    finish = 'glossy'
elif finish_code != '0' or finish_code != '1':
    finish = 'Finish code unknown'
