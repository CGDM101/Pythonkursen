# UPPGIFT 1 - STRUMPOR

# Alla mina strumpor har samma färg, storlek och modell. Varje strumpa kan alltså paras ihop med vilken annan strumpa som helst. 
# Skriv ett program som läser in antalet strumpor som användaren plockar ut ur tvättmaskinen. Programmet ska beräkna och skriva ut antalet hela par och antalet överblivna strumpor.

# Programmet ska skriva ut resultatet på följande format:
# "Det finns m par och n överbliven strumpa."
# med värden på m och n beroende på antalet strumpor som användaren angett.

# Läs in data från användaren och gör om till heltal  13
# Beräkna antalet kompletta par                       6
# Beräkna antalet överblivna strumpor                 1
# Skriv ut resultatet                                'Det finns 6 par och 1 överbliven strumpa.'

strumpor = int(input('Skriv in antal strumpor: '))
antal_par = strumpor // 2
antal_överblivna = strumpor % 2
print(f'Det finns {antal_par} par och {antal_överblivna} överbliven strumpa.')
