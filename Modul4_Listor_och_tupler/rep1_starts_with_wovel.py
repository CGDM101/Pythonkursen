# UPPGIFT 1 - BÖRJAR MED VOKAL

# Skriv ett program som läser in en serie ord från användaren. Programmet skriva ut de ord i serien som börjar på vokal. Vokaler är bokstäverna aouåeiyäö. Orden ska skrivas ut på samma rad, åtskilda av mellanslag. Programmet ska kunna hantera små och stora bokstäver. Orden ska skrivas ut så som de skrivits av användaren.


vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
lista = []
orden = input('Dina ord: ').split()
for word in orden:
    if word[0] in vokaler:
        lista.append(word)
        print(word, end=' ')


# Ange en serie ord, åtskilda av mellanslag: Det var en gång En ENDA liten gång
# en En ENDA
        
# Ange en serie ord, åtskilda av mellanslag: Alla vägar bär till Rom även E45:an
# Alla även E45:an
        
# Ange en serie ord, åtskilda av mellanslag: alla ELEMENT i eN lista Är viktiga
# alla ELEMENT i eN Är
