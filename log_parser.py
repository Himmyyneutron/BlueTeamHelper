import pandas as pd
from colorama import Fore, Style
import requests
from art import tprint

# Function to parse and analyze log files
def parse_logs(file_path):
    try:
        # Load logs into a DataFrame
        logs = pd.read_csv(file_path)
        print(Fore.GREEN + "Logs loaded successfully!" + Style.RESET_ALL)

        # Display available columns
        print(Fore.CYAN + "Columns in your logs: " + ", ".join(logs.columns) + Style.RESET_ALL)

        # Failed Logins
        if 'Keywords' in logs.columns:
            failed_logins = logs[logs['Keywords'].str.contains('Failed', na=False)]
            print(Fore.YELLOW + f"Failed login attempts: {len(failed_logins)}" + Style.RESET_ALL)
            failed_logins.to_csv("failed_logins.csv", index=False)
            print(Fore.GREEN + "Failed login events saved to 'failed_logins.csv'!" + Style.RESET_ALL)

        # Flagged IPs
        if 'Source' in logs.columns:
            flagged_ips = ['192.168.1.100', '10.0.0.1', '172.16.0.2']
            suspicious_ips = logs[logs['Source'].isin(flagged_ips)]
            print(Fore.RED + f"Connections from flagged IPs: {len(suspicious_ips)}" + Style.RESET_ALL)

            # Geolocate flagged IPs
            if not suspicious_ips.empty:
                suspicious_ips['Location'] = suspicious_ips['Source'].apply(geolocate_ip)
                suspicious_ips.to_csv("flagged_ips_with_location.csv", index=False)
                print(Fore.GREEN + "Flagged IPs with geolocation saved to 'flagged_ips_with_location.csv'!" + Style.RESET_ALL)

        # Events During Unusual Hours
        if 'Date and Time' in logs.columns:
            logs['Date and Time'] = pd.to_datetime(logs['Date and Time'], errors='coerce')
            unusual_times = logs[logs['Date and Time'].dt.hour.isin(range(0, 6))]
            print(Fore.MAGENTA + f"Events during unusual hours (midnight-6 AM): {len(unusual_times)}" + Style.RESET_ALL)
            unusual_times.to_csv("unusual_times.csv", index=False)
            print(Fore.GREEN + "Unusual hour events saved to 'unusual_times.csv'!" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)


# Function to geolocate IPs using ip-api
def geolocate_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            return f"{response['city']}, {response['country']}"
        else:
            return "Unknown"
    except Exception:
        return "Unknown"

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()  # Clear terminal at the start of the program

# Main function with ASCII Art and Menu
def main():
    tprint("P_a_r_s_e_r", font="epic")
    print(Fore.YELLOW + "Welcome to Blue Team Helper! This program was created by Joel Morales for the purposes of parsing windows securtiy logs." + Style.RESET_ALL)

    while True:
        print("\nMenu:")
        print("1. Analyze Logs")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            file_path = input("Enter the path to your log file: ").strip()
            parse_logs(file_path)
        elif choice == "2":
            print(Fore.CYAN + "Exiting Blue Team Helper. Stay secure!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
