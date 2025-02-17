######################################################################

# Professor Armando Ventura
# Autor: João Maximino, 26713
# Mestrado em Engenharia Informática, 1º ano, Politécnico de Beja
# Disciplina: Linguas de Programação Dinâmicas

######################################################################
# Script: main.py
# Referência: https://github.com/jhmax
# Data: 08/02/2025
######################################################################

######################################################################(


import sys
import time
from colorama import init, Fore, Style


from ping_tool import ping  # Importing the ping function from ping_tool.py
from netdiscover_tool import netdiscover  # Importa a função netdiscover
from nmap_tool import nmap_scan
from udp_flood import udp_flood
from tcp_flood import tcp_flood
from log_files import  run_analysis, analyze_log_file, save_report, plot_suspicious_activity
from python_server import python_server
from port_knocking import check_ssh_port

# Initialize colorama for terminal color support
init(autoreset=True)


def banner():
    print(Fore.CYAN + r"""

 SSSSSS   EEEEEEE   CCCCCCC   PPPPP    YYY
 S        E         C         P   P   Y
 SSSSSS   EEEE      C         PPPP    Y
      S   E         C         P      Y
 SSSSSS   EEEEEEE   CCCCCCC   P      Y

    """ + Style.BRIGHT + Fore.GREEN + "          *** Welcome to SecPy ***")
    print(Fore.MAGENTA + "         Security and Networking Tool in Python")
    print(Fore.YELLOW + "---------------------------------------------------------")
    print(Fore.BLUE + "  João Maximino")
    print(Fore.BLUE + "  Version: 1.0")
    print(Fore.YELLOW + "---------------------------------------------------------\n")

def menu():
    banner()
    # Wait 1 second before showing the menu
    time.sleep(1)
    
    while True:
        print("\n\n")  # Two blank lines for spacing
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + "------ Main Menu ------")
        print("\n")
        print(Fore.CYAN + "[1]" + Fore.RESET + " Ping an IP address")
        print(Fore.CYAN + "[2]" + Fore.RESET + " Network discovery")
        print(Fore.CYAN + "[3]" + Fore.RESET + " Detect and list available network ports")
        print(Fore.CYAN + "[4]" + Fore.RESET + " Create a UDP flood")
        print(Fore.CYAN + "[5]" + Fore.RESET + " Create a SYN flood")
        print(Fore.CYAN + "[6]" + Fore.RESET + " Analyze and process log files")
        print(Fore.CYAN + "[7]" + Fore.RESET + " Secure message exchange between client and server")
        print(Fore.CYAN + "[8]" + Fore.RESET + " Client port knocking for SSH")
        print(Fore.CYAN + "[0]" + Fore.RESET + " Exit\n")
        
        choice = input(Fore.YELLOW + "SecPy > " + Fore.RESET)
        
        if choice == '1':
            ping()  
        elif choice == '2':
            netdiscover()  
        elif choice == '3':
            nmap_scan()
        elif choice == '4':
            udp_flood()
        elif choice == '5':
            tcp_flood()
        elif choice == '6':
            
            log_file = input(Fore.YELLOW + "Enter the path of the log file to analyze: " + Fore.RESET)
            run_analysis(log_file)
        elif choice == '7':
            python_server()
        elif choice == '8':
            check_ssh_port()
        elif choice == '0':
            print(Fore.RED + "Exiting... see you later!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option! Please choose a valid option.\n")

if __name__ == "__main__":
    menu()
