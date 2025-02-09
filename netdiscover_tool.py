## NET DISCOVER script inspired by techniques from Noob Atbash.
# Reference: https://noob-atbash.github.io/blogs/Network-scan

import scapy.all as scapy
import netifaces
import time
from colorama import Fore, Style

def netdiscover():
    def get_local_ip():
        # Get the local IP address of the network interface
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                ip = addrs[netifaces.AF_INET][0]['addr']
                if not ip.startswith("127."):
                    return ip
        return None

    def get_subnet(ip):
        # Assume a standard subnet mask of 255.255.255.0 to calculate the network range
        subnet = ".".join(ip.split(".")[:-1]) + ".0/24"
        return subnet

    def scan(ip):
        # Create an ARP request to discover devices on the network
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request

        # Send the request and receive the responses
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        # List to store the discovered devices
        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)
        return clients_list

    def print_result(results_list):
        # Print the result in a user-friendly format
        print(Fore.CYAN + "IP\t\t\tMAC Address\n-------------------------------------------------------" + Style.RESET_ALL)
        for client in results_list:
            print(Fore.GREEN + client["ip"] + "\t\t" + client["mac"] + Style.RESET_ALL)

    local_ip = get_local_ip()
    if local_ip is None:
        print(Fore.RED + "Unable to determine the local IP address." + Style.RESET_ALL)
        return

    target_ip = get_subnet(local_ip)
    print(Fore.RED + f"Scanning: {target_ip}" + Style.RESET_ALL)
    
    try:
        while True:  # Keep scanning until the user decides to quit
            scan_result = scan(target_ip)
            print_result(scan_result)
            user_input = input(Fore.BLUE + "\nPress 'q' to quit or any key to scan again: " + Style.RESET_ALL)
            if user_input.lower() == 'q':
                print(Fore.RED + "\nExiting network discovery." + Style.RESET_ALL)
                break
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nInterrupted by user." + Style.RESET_ALL)

if __name__ == "__main__":
    netdiscover()
