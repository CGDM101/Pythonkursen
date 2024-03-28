# UPPGIFT 2 - SVAMPBOB FYRKANT

# I ett meme från 2017 med SvampBob Fyrkant (Mocking SpongeBob) blandas små och stora bokstäver för att håna något eller någon. Skriv ett program som läser in ett ord från användaren och skriver ut ordet men med varannan bokstav liten och varannan bokstav stor. Den första bokstaven ska vara liten.

ordet = input('Ditt ord: ')
print(ordet[0].lower(), end='')
for i in range(1, len(ordet)):
    if i % 2 == 0:
        print(ordet[i].lower(), end='')
    elif i % 2 != 0:
        print(ordet[i].upper(), end='')

# Ange ett ord: meme
# mEmE

# Ange ett ord: SvampBob
# sVaMpBoB

# Ange ett ord: FYRKANT
# fYrKaNt