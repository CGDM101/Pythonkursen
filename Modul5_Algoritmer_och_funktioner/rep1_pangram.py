# UPPGIFT 1 - PANGRAM

# Ett pangram är en mening som använder alfabetets alla bokstäver, minst en gång vardera. Sådana meningar används bland annat för att visa hur samtliga bokstäver i ett visst typsnitt ser ut. Skriv en funktion is_pangram som tar en text som argument och som avgör huruvida texten är ett pangram. Funktionen ska returnera ett värde av typen bool. Funktionen ska använda det engelska alfabetet och kunna hantera både små och stora bokstäver.

alfabetet = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(text):
    for i in range(len(alfabetet)):
        if alfabetet[i] not in text.lower():
            return False
    return True


# Testdata
text = 'The quick brown fox jumps over the lazy dog.'
if is_pangram(text):
    print('The text is a pangram.')      # This will be printed
else:
    print('The text is not a pangram.')

text = 'Pack my box with five dozen liquor jugs.'
if is_pangram(text):
    print('The text is a pangram.')      # This will be printed
else:
    print('The text is not a pangram.')

text = 'This is just any text.'
if is_pangram(text):
    print('The text is a pangram.')
else:
    print('The text is not a pangram.')   # This will be printed
