## source: https://stackoverflow.com/questions/65710302/writing-a-python-script-to-connect-to-a-port

import socket
import time
from colorama import init, Fore, Style

# Initialize colorama for terminal color support
init(autoreset=True)

# Sequência de portas do knockd (ajuste conforme sua configuração)
KNOCK_SEQUENCE = [1234, 5678, 9012]

def send_knock_sequence(target):
    """Envia a sequência de Port Knocking para liberar o SSH."""
    for port in KNOCK_SEQUENCE:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect_ex((target, port))  # Conexão rápida para o knock
            s.close()
            print(Fore.BLUE + f"Knock enviado na porta {port} de {target}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Erro ao bater na porta {port}: {e}" + Style.RESET_ALL)

def check_ssh_port():
    """Verifica se a porta SSH está aberta após o Port Knocking."""
    while True:
        target = input(Fore.RED + "Enter IP to scan for SSH port (or type 'q' to quit): " + Style.RESET_ALL)
        
        if target.lower() == 'q':
            print(Fore.RED + "Exiting SSH port check operation." + Style.RESET_ALL)
            return
        
        port = 22  # Porta do SSH
        
        # Enviar sequência de knocks antes de testar SSH
        print(Fore.CYAN + "Enviando sequência de Port Knocking..." + Style.RESET_ALL)
        send_knock_sequence(target)

        # Espera um tempo para permitir que o firewall processe os knocks
        time.sleep(15)

        try:
            # Cria o socket para conectar ao destino na porta SSH
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)

            print(Fore.YELLOW + f"Tentando conectar à porta SSH {port} em {target}..." + Style.RESET_ALL)
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(Fore.GREEN + f"SSH aberto em {target}! " + Style.RESET_ALL)
            else:
                print(Fore.RED + f"SSH ainda fechado em {target} " + Style.RESET_ALL)

            s.close()
        
        except Exception as e:
            print(Fore.RED + f"Erro inesperado: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    check_ssh_port()
