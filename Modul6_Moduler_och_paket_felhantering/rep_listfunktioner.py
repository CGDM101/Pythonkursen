#### I den här repetitionen ska ni skapa en modul som innehåller två olika funktioner. Ni ska testa er kod i modulen och även skriva ett huvudprogram som anropar funktionerna från modulen.

### UPPGIFT 1 - LISTFUNKTIONER

# Python har många inbyggda funktioner som opererar på listor. Ibland kan man dock sakna en eller ett par specifika funktioner. Om de här funktionerna återkommer ofta i ett projekt kan det vara lämpligt att placera dem i en modul. Vi ska nu skriva två funktioner och placera dem i en modul med namnet "listfunktioner".

## 1 a) Hitta positionen för minsta värdet

# Den inbyggda funktionen min returnerar det minsta elementet i en lista. Skriv en funktion arg_min som istället returnerar positionen för listans minsta element. Om det minsta värdet förekommer mer än en gång ska funktionen returnera den första av dessa positioner. Om den angivna listan är tom ska ett ValueError kastas tillsammans med ett kortfattat felmeddelande som informerar användaren om att listan inte får vara tom. Meddelandet ska vara på svenska och innehålla orden "tom" och "lista".

# values = [6, 3, 4, 8, 1, 5]
# min_pos = arg_min(values)     # 4

# values = [14, 24, 10, 15, 10]
# min_pos = arg_min(values)     # 2

# values = []
# min_pos = arg_min(values) # ValueError

def arg_min(lst):
    min_pos = 0
    if len(lst) == 0:
        raise ValueError('Din lista är tom')
    for i in range(len(lst)):
        if lst[i] < lst[min_pos]:
            min_pos = i
    return min_pos

## 1 b) Hitta alla förekomster

# Listfunktionen index returnerar positionen för den första förekomsten av ett givet element i en lista. Skriv en funktion find_all_positions som returnerar en lista med positionerna för samtliga förekomster av ett givet element i en lista.

# values = [3, 3, 5, 2, 6, 5, 4, 5, 3, 2]
# min_pos = find_all_positions(values, 3) # [0, 1, 8]

# values = [3, 3, 5, 2, 6, 5, 4, 5, 3, 2]
# min_pos = find_all_positions(values, 8) # []

# values = []
# min_pos = find_all_positions(values, 5) # []


def find_all_positions(lst, tal):
    pos_lst = []
    for i, värde in enumerate(lst):
        if lst[i] == tal:
            pos_lst.append(i)
        # print('i:', i, end=' ')
        # print('värde:', värde)
    return pos_lst
