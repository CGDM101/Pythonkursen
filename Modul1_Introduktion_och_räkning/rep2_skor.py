# UPPGIFT 2 - SKOR

# Alla mina skor har samma färg, storlek och modell. Varje högersko kan alltså
# paras ihop med vilken vänstersko som helst och vice versa. Skriv ett program
# som läser in antalet vänsterskor och antalet högerskor från användaren.

# Programmet ska skriva ut resultatet på följande format:
# "Det finns m par och n överblivna skor."
# med värden på m och n beroende på antalet höger- och vänsterskor som
# användaren angett.

# Läs in antal vänsterskor och gör om till heltal         13
# Läs in antal högerskor och gör om till heltal           9
# Beräkna antal kompletta par                             9
# Beräkna antal överblivna skor                           4
# Skriv ut resultatet                                     'Det finns 9 par och 4 överblivna skor.'

antal_vänsterskor = int(input('Skriv in antal vänsterskor: '))
antal_högerskor = int(input('Skriv in antal högerskor: '))

antal_kompletta_par = min(antal_vänsterskor, antal_högerskor)
antal_överblivna_skor = max(
    antal_vänsterskor, antal_högerskor) - antal_kompletta_par

print(f'Det finns {antal_kompletta_par} par och {antal_överblivna_skor} överblivna skor.')
