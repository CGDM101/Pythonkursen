#### I den här repetitionen ska ni skapa en modul som innehåller två olika funktioner. Ni ska testa er kod i modulen och även skriva ett huvudprogram som anropar funktionerna från modulen.

### UPPGIFT 2 - HUVUDPROGRAM

# Skriv nu ett program som läser in ett antal tal samt ett sökt tal från användaren. Programmet ska använda funktionerna från modulen i förra uppgifterna för att skriva ut positionen för det minsta talet samt alla positioner för det givna talet. Spara programmet i en fil med namnet listprogram.py.

# $ python3 listprogram.py
# Ange ett par tal: 12 15 5 4 10 4 12 5 15
# Ange ett sökt tal: 5
# Det minsta talet finns på position 3.
# Talet 5 finns på positionerna [2, 7].

import rep_listfunktioner

x = input('Ange ett par tal: ').split()
talen = [int(tal) for tal in x]
talet = int(input('Ange ett sökt tal'))

minsta_talet = rep_listfunktioner.arg_min(talen)
minsta_talets_positioner = rep_listfunktioner.find_all_positions(talen, talet)

print(f'Det minsta talet finns på position {minsta_talet}.')
print(f'Talet {talet} finns på positionerna {minsta_talets_positioner}.')

