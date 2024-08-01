# Installa la libreria con pip
# pip install braillelib

import braillelib as braille

# Converti il testo in Braille
braille_text = braille.textToBraille('ciao mondo')
print(braille_text)

# Converti il Braille in testo
text = braille.brailleToTextArray(braille_text)
print(text)
