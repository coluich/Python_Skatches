print('ciao')
def divisore():
    try:
        a = int(input("inserisci il valore di a: "))
        b = int(input("inserisci il valore di b: "))
        risultato = a ** b
        print("il risultato della divisione è: " + str(risultato))
    except ZeroDivisionError:
        print("non puoi effettuare una divisione per zero")
    except ValueError:
        print("hey, solo numeri grazie")

if True:
    divisore()