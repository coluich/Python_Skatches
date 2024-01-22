

while True:
    
    print('''\n\n         -per effettuare un\'addizione  premere 1
         -per effettuare una sottrazione premere 2
         -per effettuare una moltiplicazione premere 3
         -per effettuare una divisione premere 4
         -per effettuare un calcolo esponenziale premere 5
         -per uscire digitare ESC''')
    print ('\nscegli:')

    scelta = input ('inserisci il numero:---------')

    if scelta == '1':
            print ('\nhai scelto addizione')
            num1 = float(input('inserisci il primo numero:'))
            num2 = float(input('inserisci il secondo numero:'))
            print('il risultato è: ' + str(num1 + num2))
    elif scelta == '2':
            print ('\nhai scelto sottrazione')
            num1 = float(input('inserisci il primo numero:'))
            num2 = float(input('inserisci il secondo numero:'))
            print('il risultato è: ' + str(num1 - num2))
    elif scelta == '3':
            print ('\nhai scelto moltiplcazione')
            num1 = float(input('inserisci il primo numero:'))
            num2 = float(input('inserisci il secondo numero:'))
            print('il risultato è: ' + str(num1 * num2))
    elif scelta == '4':
            print ('\nhai scelto divisione')
            num1 = float(input('inserisci il primo numero:'))
            num2 = float(input('inserisci il secondo numero:'))
            print('il risultato è: ' + str(num1 / num2))
    elif scelta == '5':
            print ('\nhai scelto calcolo esponenziale')
            num1 = float(input('inserisci il primo numero:'))
            num2 = float(input('inserisci il secondo numero:'))
            print('il risultato è: ' + str(num1 ** num2))
    elif scelta == 'ESC' or scelta == 'esc':
        break
