while True:
    count = 0
    a = 0
    b = 1
    scelta = input('''
                   

    Scegli:
    1 = Numeri di fibonacci
    2 = Quale numero di fibonacci\n\n>>> ''')




    if scelta == '1':
        maximo = int(input('\nInserisci quanti numeri vuoi vedere:\n\n>>> '))
        while count < maximo:
            count += 1
            a = a + b
            print(f'\n{count} -- ' + str(a))
            if count < maximo:
                count += 1
                b = a + b
                print(f'\n{count} -- ' + str(b))

    if scelta == '2':
        sceltanumero = int(input('\nSegli il numero da controllare all\'interno della sequenza di fibonacci\n\n>>> '))
        
        while True:

            a = a + b
            if a > sceltanumero:
                print("\033[91m"+str(a)+"\033[0m")
                print('Purtroppo il tuo numero non esiste')
                break
            elif a == sceltanumero: 
                print("\033[92m"+str(a)+"\033[0m")
                print('Il tuo numero esiste!!!')
                break
            else:
                print(str(a))
            
            b = a + b
            if b > sceltanumero:
                print("\033[91m"+str(b)+"\033[0m"+"\n")
                print('Purtroppo il tuo numero non esiste')
                break
            elif b == sceltanumero: 
                print("\033[92m"+str(b)+"\033[0m"+"\n")
                print('Il tuo numero esiste!!!')
                break
            else:
                print(str(b))


    elif scelta != "1" and scelta != "2":
        print('Devi inserire o \'1\' o \'2\'')