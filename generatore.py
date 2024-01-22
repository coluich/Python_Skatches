import itertools
import os
import string

def generate_passwords(length, include_characters):
    characters = ""
    
    if '1' in include_characters:
        characters += string.digits
    if '2' in include_characters:
        characters += string.ascii_letters
    if '3' in include_characters:
        characters += string.punctuation
    
    passwords = itertools.product(characters, repeat=length)
    passwords = [''.join(p) for p in passwords]
    return passwords

def main():
    length = int(input("Inserisci la lunghezza desiderata delle password: "))
    include_characters = input("Premi 1 per includere i numeri, 2 per includere le lettere, 3 per includere i caratteri speciali (es. 123): ")
    
    num_numbers = input("Quanti numeri ci saranno (o - per qualsiasi numero)? ")
    num_letters = input("Quante lettere ci saranno (o - per qualsiasi lettera)? ")
    num_special_chars = input("Quanti caratteri speciali ci saranno (o - per qualsiasi carattere)? ")
    
    exclude_chars = input("Inserisci eventuali caratteri da escludere: ")
    
    include_characters += exclude_chars
    
    passwords = generate_passwords(length, include_characters)
    
    default_path = os.path.join(os.getcwd(), "passwords.txt")
    save_path = input(f"Inserisci il percorso per il file (predefinito: {default_path}): ").strip()
    if not save_path:
        save_path = default_path
    
    with open(save_path, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    
    print(f"Le password sono state generate e salvate in {save_path}")

if __name__ == "__main__":main()
