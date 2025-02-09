# Ping script inspired by a subprocess implementation from DaniWeb.
# Reference: https://www.daniweb.com/programming/software-development/threads/483690

import subprocess
from colorama import Fore, Style

def ping():
    while True:
        ip_address = input(Fore.RED + "Enter IP address to ping (or type 'q' to quit): " + Style.RESET_ALL)
        
        if ip_address.lower() == 'q':
            print(Fore.RED + "Exiting ping operation." + Style.RESET_ALL)
            return  
        
        try:
            # Run the ping command with a continuous loop until manually stopped
            process = subprocess.Popen(["ping", "-c", "4", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Read output line by line
            for line in process.stdout:
                print(Fore.GREEN + line.strip() + Style.RESET_ALL)  # Print each line of output in green
            print("")

            # Check for any errors after the process finishes (wrong ip; letters..)
            errors = process.stderr.read()
            if errors:
                print(Fore.RED + f"Error: {errors}" + Style.RESET_ALL) 

        except TypeError as err:
            print(Fore.RED + f"An error occurred: {err}" + Style.RESET_ALL)
        except KeyboardInterrupt:
                print(Fore.YELLOW + print("\nInterrupted by user.") + Style.RESET_ALL)
                break
if __name__ == "__main__":
    ping()
