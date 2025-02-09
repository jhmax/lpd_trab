# Nmap tool to scan open ports technique from Alexandre Norman.
## reference: https://xael.org/pages/python-nmap-en.html

import subprocess
import nmap
from colorama import init, Fore, Style

# Initialize colorama for terminal color support
init(autoreset=True)

def nmap_scan():
    while True:
        # Solicita o IP ou domínio para escanear
        target = input(Fore.RED + "Enter IP or domain to scan (or type 'q' to quit): " + Style.RESET_ALL)
        
        if target.lower() == 'q':
            print(Fore.RED + "Exiting Nmap scan operation." + Style.RESET_ALL)
            return
        
        try:
            # Cria o objeto scanner do nmap
            nm = nmap.PortScanner()
            
            # Realiza o scan de portas do IP/dominio fornecido
            print(Fore.YELLOW + f"Scanning {target} for open ports..." + Style.RESET_ALL)
            nm.scan(hosts=target, arguments='-p 1-1024')  # Verifica as portas de 1 a 1024
            
            if nm.all_hosts():
                for host in nm.all_hosts():
                    print(Fore.GREEN + f"Host: {host}" + Style.RESET_ALL)
                    print(Fore.CYAN + "Open Ports:" + Style.RESET_ALL)
                    for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        for port in lport:
                            print(Fore.GREEN + f"Port {port} {nm[host][proto][port]['state']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"No hosts found for the IP or domain {target}." + Style.RESET_ALL)
            
        except nmap.nmap.PortScannerError as e:
            print(Fore.RED + f"Error in Nmap: {e}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    nmap_scan()
