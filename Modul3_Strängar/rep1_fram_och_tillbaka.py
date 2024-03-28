# UPPGIFT 1 - FRAM OCH TILLBAKA

# Skriv ett program som läser in ett ord från användaren. Programmet ska skriva ut det givna ordet framlänges och baklänges, vertikalt och sida vid sida. De två bokstäverna på varje rad ska skiljas åt av mellanslag och av ett bindestreck.

ordet = input('Ditt ord: ')
for i in range(len(ordet)):
    rev = ordet[::-1]
    print(f'{ordet[i]} - {rev[i]}')

# print(f'{ordet[i]} - {ordet[i-1]}') funkar inte, man måste ta rev! Annars växlas bara första bokstaven:
# h - n
# e - h
# j - e
# s - j
# a - s
# n - a




# Ange ett ord: väst
# v - t
# ä - s
# s - ä
# t - v

# Ange ett ord: sol
# s - l
# o - o
# l - s

# Ange ett ord: fågel
# f - l
# å - e
# g - g
# e - å
# l - f