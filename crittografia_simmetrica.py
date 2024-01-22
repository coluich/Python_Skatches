import rsa

asd = input('''1 o 2:
1. Decripta
2. Cripta
''')


if asd == '1':
    print('------------------Decrypta------------------')
    msgg = input('Inserisci il messaggio da decrittografare: ')
    msg = msgg.encode('utf8')
    bob_priv = input('Inserisci la chiave privata: ')
    mic = rsa.decrypt(msg, bob_priv)
    print(mic)
    input()

elif asd == '2':
    print('------------------Crypta------------------')
    msgg = input('inserisci il messaggio: ')
    msg = msgg.encode('utf8')
    bob_pub = input('Inserisci la chiave pubblica: ')
    mnic = rsa.encrypt(msg, bob_pub)
    print(mnic)
    input()
