# UPPGIFT 2 - SÄTT MINSTA VÄRDE

# Skriv en funktion set_min_value som tar en lista av heltal och ett minsta värde. Funktionen ska ändra de av listans element som är mindre än det angivna värdet och sätta dem lika med detta värde. Funktionen ska inte returnera något.

def set_min_value(heltalslista, minsta_vaerde):
    for i in range(len(heltalslista)):
        if heltalslista[i] < minsta_vaerde:
            heltalslista[i] = minsta_vaerde


# Följande är ett exempel på hur funktionen kan användas
lst = [4, -2, 0, 3, 7]
set_min_value(lst, 2)
print(lst)              # [4, 2, 2, 3, 7]

lst = [-13, 5, -6, 9, 0]
set_min_value(lst, -3)
print(lst)              # [-3, 5, -3, 9, 0]

lst = [8, 9, 13, 6, 5]
set_min_value(lst, 1)
print(lst)              # [8, 9, 13, 6, 5]
