import socket
import threading

clients = {}

def broadcast(message, sender_pseudonym):
    message = message.encode('utf-8')
    for client_socket, client_pseudonym in clients.values():
        if client_pseudonym != sender_pseudonym:
            try:
                client_socket.send(message)
            except Exception as e:
                print(f"Errore nell'invio del messaggio al client {client_pseudonym}: {str(e)}")

def handle_client(client_socket, pseudonym):
    clients[pseudonym] = (client_socket, pseudonym)

    broadcast(f"\n{pseudonym} si è unito alla chat.", pseudonym)

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = f"\n{pseudonym}: {data.decode('utf-8')}"
            print(message)
            broadcast(message, pseudonym)
        except:
            print(f"'{pseudonym}' ci ha lasciati")
            break

    del clients[pseudonym]
    broadcast(f"{pseudonym} ha lasciato la chat.", pseudonym)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.178.69', 5555))
    server.listen(5)

    print("Server in ascolto sulla porta 5555...")

    while True:
        client_sock, addr = server.accept()
        print(f"Connessione accettata da {addr[0]}:{addr[1]}")

        # Richiedi all'utente di inserire uno pseudonimo
        client_sock.send("Inserisci il tuo pseudonimo: ".encode('utf-8'))
        pseudonym = client_sock.recv(1024).decode('utf-8')

        client_handler = threading.Thread(target=handle_client, args=(client_sock, pseudonym))
        client_handler.start()

start_server()
