import random
import time

asd = None
a = int(input('scegli un numero intero: '))
b = int(input('scegli un altro numero intero: '))
pippo = int(input('Quanti sbagli ti vuoi concedere? '))
numero = random.randint(a, b)

scelta = int(input('Che numero pensi che esca? '))
if scelta != numero:
    print('Errato')
    asd += 1
else:
    print('Bravo, hai indovinato')
    time.sleep(2)
if asd == pippo:
    print('Hai perso')

while True:
    scelta = int(input('Che numero pensi che esca? '))
    if scelta != numero:
        print('Errato')
        asd += 1

    if asd == pippo:
        print('Hai perso')
        break

    elif scelta == numero:
        print('Bravo, hai indovinato')
        break
