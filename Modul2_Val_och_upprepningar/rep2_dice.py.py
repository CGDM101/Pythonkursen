# UPPGIFT 2 - TÄRNING

# Tänk dig ett tärningsspel där man måste slå en sexa för att fortsätta. Använd
# modulen random för att simulera en serie kast med en rättvis, sexsidig
# tärning. Skriv ett program som skriver ut resultatet av kasten tills den
# första sexan slås. Programmet ska sedan skriva antalet kast det tog enligt
# exemplet nedan.

# 4
# 1
# 3
# 1
# 6
# Det tog 5 kast att få en 6:a.

import random
räknare = 0
kast = 0
while kast != 6:
    kast = random.randint(1, 6)
    print(kast)
    räknare += 1
    if kast == 6:
        break

print(f'Det tog {räknare} kast att få en 6:a.')
