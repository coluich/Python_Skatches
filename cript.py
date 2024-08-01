from cryptography.fernet import Fernet
import os
import time
asd = True

os.system('cls' if os.name == 'nt' else 'clear')

if os.path.isfile('.\\chiave'):
    with open("chiave", 'r') as t:
        file_chiave_path = t.read()
        t.close
elif not os.path.isfile('.\\chiave'):
    file_chiave_path = "D:\\aes.pem"
else:
    print("Chiavi mancanti. Il programma verrà interrotto.")
    input()


def crittografa_file(chiave_fernet, nome_file):
    # Determina il nome del file crittografato
    nome_file_crittografato = nome_file + ".aes"
    input_path = os.path.join(cartella, nome_file)
    output_path = os.path.join(cartella, nome_file_crittografato)
    
    # Leggi il file originale
    with open(input_path, 'rb') as file_originale:
        dati_originale = file_originale.read()
    
    # Cifra il file originale
    dati_criptati = chiave_fernet.encrypt(dati_originale)
    
    # Salva il file cifrato
    with open(output_path, 'wb') as file_criptato:
        file_criptato.write(dati_criptati)
    
    print(f"File '{nome_file}' crittografato come '{nome_file_crittografato}'.")
    time.sleep(0.5)
    
    # Elimina il file originale
    os.remove(input_path)

def decrittografa_file(chiave_fernet, nome_file):
    # Determina il nome del file decrittografato
    nome_file_decrittografato = nome_file[:-4]  # Rimuovi l'estensione .aes
    input_path = os.path.join(cartella, nome_file)
    output_path = os.path.join(cartella, nome_file_decrittografato)
    
    # Leggi il file cifrato
    with open(input_path, 'rb') as file_criptato:
        dati_criptati = file_criptato.read()
    
    # Decifra il file cifrato
    try:
        dati_decrittati = chiave_fernet.decrypt(dati_criptati)
    except:
        print("\u001b[31mKey wrong\u001b[0m")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()


    # Salva il file decifrato
    with open(output_path, 'wb') as file_decrittato:
        file_decrittato.write(dati_decrittati)
    
    print(f"File '{nome_file}' decrittografato come '{nome_file_decrittografato}'.")
    time.sleep(0.5)
    
    # Elimina il file crittografato
    os.remove(input_path)

# Ottieni il percorso della directory corrente (dove si trova il tuo script Python)
cartella = os.path.dirname(os.path.abspath(__file__))

# Verifica se il file delle chiavi esiste
# file_chiave_path = "D:\\aes.pem"



if not os.path.exists(file_chiave_path):
    print("Chiavi mancanti. Il programma verrà interrotto.")
    input()
else:
    # Carica la chiave Fernet
    with open(file_chiave_path, "rb") as file_chiave:
        chiave_fernet = Fernet(file_chiave.read())

    # Usa il metodo listdir() del modulo os per ottenere una lista di tutti i file nella cartella
    # Il ciclo for itera su ciascun elemento nella lista e stampa i nomi dei file con i loro indici
    file_lista = os.listdir(cartella)

    print("Elenco dei file disponibili:")
    for indice, nome_file in enumerate(file_lista):
        if nome_file != os.path.basename(__file__) and nome_file != "chiave":  # Escludi il file Python corrente dall'elenco
            if nome_file.endswith(".aes"):
                print(f"\u001b[92m{indice} : {nome_file}\u001b[0m")
            else:
                print(f"\u001b[31m{indice} : {nome_file}\u001b[0m")


    # Chiedi all'utente di selezionare i file da crittografare/decrittografare
    
    indici_selezionati = input("-> ").split()
    
    if "q" in indici_selezionati or "Q" in indici_selezionati:
        exit()
        # print(indici_selezionati)
        pass





    for indice in range(len(indici_selezionati)):
        try:
            indice = int(indici_selezionati[indice])
            if indice >= 0 and indice < len(file_lista):
                nome_file_scelto = file_lista[indice]
                
                # Cifra o decifra il file a seconda dell'estensione
                if nome_file_scelto.endswith(".aes"):
                    decrittografa_file(chiave_fernet, nome_file_scelto)
                else:
                    crittografa_file(chiave_fernet, nome_file_scelto)
            else:
                print(f"Indice {indice} non valido. Ignorato.")
        except ValueError:
            print(f"Input non valido: {indici_selezionati[indice]}. Ignorato.")

    # Chiudi il programma
    print("Operazioni completate. Il programma si chiuderà.")
    os.system(f"{__file__}")