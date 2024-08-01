import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from cryptography.fernet import Fernet
import re

# Credenziali statiche per l'esempio
USERNAME = "admin"
PASSWORD = "password"

def verifica_credenziali(username_input: str, password_input: str) -> bool:
    """Verifica se le credenziali inserite sono corrette."""
    return username_input == USERNAME and password_input == PASSWORD

# Funzioni per la gestione della chiave
def save_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()
# Genera e salva la chiave solo se non esiste già
if not os.path.exists('key.key'):
    key = Fernet.generate_key()
    save_key(key)
else:
    key = load_key()

cipher_suite = Fernet(key)

# Funzioni per criptare e decriptare
def encrypt_password(password: str) -> bytes:
    return cipher_suite.encrypt(password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    return cipher_suite.decrypt(encrypted_password).decode()

# Funzioni per salvare e recuperare le password
def save_password(service_name: str, password: str):
    encrypted_password = encrypt_password(password)  # Assicurati che questa funzione ritorni il risultato atteso
    with open("passwords.txt", "a") as file:
        file.write(f"{service_name}:{encrypted_password.decode('utf-8')}\n")  # Decodifica se necessario
def get_password(service_name: str) -> str:
    # Verifica se il file esiste prima di aprirlo
    if not os.path.exists('passwords.txt'):
        open('passwords.txt', 'w').close()  # Crea il file se non esiste
    with open("passwords.txt", "r") as file:
        for line in file:
            service, encrypted_password = line.strip().split(":")
            if service == service_name:
                return decrypt_password(encrypted_password.encode('utf-8'))
    return "Servizio non trovato."

# Funzione per la verifica dei requisiti della password
def verifica_password(password: str) -> bool:
    if len(password) < 8:
        print("La password deve essere lunga almeno 8 caratteri.")
        return False
    if not re.search("[A-Z]", password):
        print("La password deve contenere almeno una lettera maiuscola.")
        return False
    if not re.search("[a-z]", password):
        print("La password deve contenere almeno una lettera minuscola.")
        return False
    if not re.search("[0-9]", password):
        print("La password deve contenere almeno un numero.")
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        print("La password deve contenere almeno un carattere speciale.")
        return False
    return True

# Credenziali statiche per l'esempio
USERNAME = "admin"
PASSWORD = "password"

# Autenticazione utente
def login():
    username = entry_username.get()
    password = entry_password.get()
    if verifica_credenziali(username, password):
        login_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Login fallito", "Username o password errati")


# Aggiunta di una nuova password
def add_password():
    service = simpledialog.askstring("Aggiungi Password", "Nome del servizio:")
    if service is not None:
        password = simpledialog.askstring("Aggiungi Password", "Password:", show="*")
        if password and verifica_password(password):
            save_password(service, password)
            messagebox.showinfo("Successo", "Password salvata con successo.")
        else:
            messagebox.showerror("Errore", "La password non soddisfa i requisiti.")


# Recupero di una password esistente
def retrieve_password():
    service = simpledialog.askstring("Recupera Password", "Nome del servizio:")
    if service:
        password = get_password(service)
        if password:
            messagebox.showinfo("Password Recuperata", f"La password per '{service}' è: {password}")
        else:
            messagebox.showerror("Errore", "Password non trovata.")


# Mostra la finestra principale dopo il login
def show_main_window():
    main_window = tk.Tk()
    main_window.title("Gestore di Password")

    tk.Button(main_window, text="Aggiungi Password", command=add_password).pack(padx=50, pady=5)
    tk.Button(main_window, text="Recupera Password", command=retrieve_password).pack(padx=50, pady=5)
    tk.Button(main_window, text="Esci", command=lambda: main_window.destroy()).pack(padx=50, pady=5)

    main_window.mainloop()


# Finestra di login
login_window = tk.Tk()
login_window.title("Login Gestore di Password")

tk.Label(login_window, text="Username:").pack(padx=10, pady=5)
entry_username = tk.Entry(login_window)
entry_username.pack(padx=10, pady=5)

tk.Label(login_window, text="Password:").pack(padx=10, pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(padx=10, pady=5)

tk.Button(login_window, text="Login", command=login).pack(pady=10)

login_window.mainloop()
