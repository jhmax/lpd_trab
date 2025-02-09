## Network scan script inspired by techniques from NeuralNine.
# Reference: https://github.com/NeuralNine

import socket
import threading
import rsa
from colorama import Fore, Back, Style, init

# Inicializa o colorama
init(autoreset=True)

# Chaves RSA
public_key, private_key = rsa.newkeys(1024)
public_partner = None

def python_server():
    choice = input(Fore.YELLOW + "Do you want to host(1) or to connect(2): ")

    if choice == "1":
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
        server.bind(("192.168.0.21", 4444))  # Associar IP e porta
        server.listen()
        print(Fore.GREEN + "Server listening on 192.168.0.100:9999...")
        
        client, _ = server.accept()  # Aceitar a conexão do cliente
        client.send(public_key.save_pkcs1("PEM"))  # save in format PEM
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        print(Fore.CYAN + "Client connected.")

    elif choice == "2":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criar socket para o cliente
        client.connect(("192.168.0.21", 4444))  # Conectar ao servidor
        client.send(public_key.save_pkcs1("PEM"))  # save in format PEM
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        print(Fore.CYAN + f"Connected to server at 192.168.0.100:9999")

    else:
        print(Fore.RED + "Invalid choice, exiting...")
        exit()

    def sending_messages(c):
        while True:
            message = input(Fore.WHITE + "Your message: ")
            c.send(rsa.encrypt(message.encode(), public_partner))
            print(Fore.MAGENTA + "You: " + message)

    def receive_messages(c):
        while True:
            print(Fore.MAGENTA + "Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())

    # Iniciar as threads para enviar e receber mensagens
    threading.Thread(target=sending_messages, args=(client,)).start()
    threading.Thread(target=receive_messages, args=(client,)).start()

# Função principal
def py_server():
    try:
        python_server()
    except KeyboardInterrupt:
        print(Fore.RED + "\nServer/Client terminated by user (Ctrl + C).")
        exit(0)

# Este bloco assegura que a função main() seja executada apenas quando o script for executado diretamente
if __name__ == "__main__":
    py_server()
