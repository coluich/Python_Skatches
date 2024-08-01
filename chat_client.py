import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except Exception as e:
            print(f"Errore nella ricezione del messaggio: {str(e)}")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.178.69', 5555))

    # Ricevi il messaggio di benvenuto e imposta lo pseudonimo
    welcome_message = client.recv(1024).decode('utf-8')
    print(welcome_message)
    pseudonym = input("Il tuo pseudonimo: ")
    client.send(pseudonym.encode('utf-8'))

    # Avvia un thread separato per la ricezione dei messaggi
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("Inserisci il messaggio: ")
        client.send(message.encode('utf-8'))

start_client()
