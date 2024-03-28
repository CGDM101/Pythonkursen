# UPPGIFT 2 - HITTA NÄRMAST

# Skriv ett program som läser in en serie heltal och ett målvärde från användaren. Programmet skriva ut det tal i serien som ligger närmast det angivna målvärdet. Det sökta talet kan vara antingen större eller mindre än målvärdet. Om fler än ett heltal ligger lika nära målvärdet ska programmet skriva ut det första av dem.

strängar = input('Dina tal: ').split()
målvärde = int(input('Ditt målvärde: '))
talen = [int(sträng) for sträng in strängar]

x = enumerate(talen)
print(x)

for z, y in x:
    print(z, y)
    
# min_diff = 0
# difflista = []
# for tal in talen:
#     diff = abs(målvärde - tal)
#     if diff > min_diff:
#         min_diff = diff

# print(min_diff)
    # difflista.append(diff)

# print(difflista)

# Ange en serie heltal, åtskilda av mellanslag: 68 25 90 43 65 37 40 18
# Ange ett målvärde: 52
# Närmast: 43

# Ange en serie heltal, åtskilda av mellanslag: 5 7 3 14 2 18 13
# Ange ett målvärde: 10
# Närmast: 7

# Ange en serie heltal, åtskilda av mellanslag: 15 7 -2 -20 10 6
# Ange ett målvärde: 1
# Närmast: -2