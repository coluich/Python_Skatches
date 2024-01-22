import os
from cryptography.fernet import Fernet

# Genera una chiave segreta per l'encryption
chiave = Fernet.generate_key()
cipher_suite = Fernet(chiave)

# Ottieni il percorso del file script Python corrente e della chiave segreta
percorso_script = os.path.abspath(__file__)
percorso_chiave_segreta = 'chiave_secreta.txt'  # Aggiorna con il percorso del file della chiave segreta

# Specifica la cartella da crittografare
cartella = os.getcwd()

# Cifra tutti i file nella cartella, escludendo lo script Python e il file della chiave segreta
for cartella_principale, _, files in os.walk(cartella):
    for nome_file in files:
        percorso_completo = os.path.join(cartella_principale, nome_file)
        # Controlla se il file è diverso dallo script Python e dalla chiave segreta
        if percorso_completo != percorso_script and percorso_completo != percorso_chiave_segreta:
            with open(percorso_completo, 'rb') as file:
                dati = file.read()
            dati_cifrati = cipher_suite.encrypt(dati)
            with open(percorso_completo, 'wb') as file:
                file.write(dati_cifrati)

# Scrivi la chiave segreta in un file
with open(percorso_chiave_segreta, 'wb') as file_chiave:
    file_chiave.write(chiave)

print(f"Tutti i file nella cartella '{cartella}' sono stati crittografati, escludendo lo script Python e il file della chiave segreta.")
