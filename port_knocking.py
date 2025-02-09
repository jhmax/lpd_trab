## source: https://stackoverflow.com/questions/65710302/writing-a-python-script-to-connect-to-a-port

import socket
from colorama import init, Fore, Style

# Initialize colorama for terminal color support
init(autoreset=True)

def check_ssh_port():
    while True:
        # Solicita o IP para escanear
        target = input(Fore.RED + "Enter IP to scan for SSH port (or type 'q' to quit): " + Style.RESET_ALL)
        
        if target.lower() == 'q':
            print(Fore.RED + "Exiting SSH port check operation." + Style.RESET_ALL)
            return
        
        port = 22  # Porta do SSH
        
        try:
            # Cria o socket para conectar ao destino na porta SSH
            s = socket.socket()
            s.settimeout(2)
            
            print(Fore.YELLOW + f"Attempting to connect to SSH port {port} on {target}..." + Style.RESET_ALL)
            s.connect((target, port))
            
            # Recebendo dados da resposta (pode ser um banner ou outro dado do serviço SSH)
            response = s.recv(1024)
            print(Fore.GREEN + f"Response received from {target}: {response.decode('utf-8', errors='ignore')}" + Style.RESET_ALL)
            
            # Fechando a conexão
            s.close()
        
        except socket.error as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    check_ssh_port()
