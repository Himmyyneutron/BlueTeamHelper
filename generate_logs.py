import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
from art import tprint
from colorama import Fore, Style

# Initialize Faker for random data generation
fake = Faker()

# List of events and flagged IPs
event_types = ['Successful Login', 'Failed Login', 'File Access', 'Suspicious Activity']
task_categories = ['Authentication', 'File System', 'Network', 'Audit']
flagged_ips = ['192.168.1.100', '10.0.0.1', '172.16.0.2']

# Function to generate random logs
def generate_logs(file_name, num_logs=500):
    logs = []
    now = datetime.now()

    for _ in range(num_logs):
        event = random.choice(event_types)
        task_category = random.choice(task_categories)
        timestamp = now - timedelta(minutes=random.randint(0, 1440))  # Random time in the last 24 hours
        source_ip = fake.ipv4_private() if random.random() > 0.2 else random.choice(flagged_ips)
        keywords = event if event != 'Suspicious Activity' else 'Suspicious'
        
        log_entry = {
            'Keywords': keywords,
            'Date and Time': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Source': source_ip,
            'Event ID': random.randint(1000, 2000),
            'Task Category': task_category
        }
        logs.append(log_entry)

    # Save to CSV
    logs_df = pd.DataFrame(logs)
    logs_df.to_csv(file_name, index=False)
    print(Fore.GREEN + f"Generated {num_logs} logs and saved to {file_name}" + Style.RESET_ALL)

# Function to clear the terminal
def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function with a menu
def main():
    clear_terminal()
    tprint("Log Gen", font="block")
    print(Fore.YELLOW + "Welcome to the Log Generator UI!" + Style.RESET_ALL)

    while True:
        print("\nMenu:")
        print("1. Generate Logs")
        print("2. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Prompt user for file name and number of logs
            file_name = input("Enter the file name to save logs (e.g., logs.csv): ").strip()
            if not file_name.endswith(".csv"):
                file_name += ".csv"
            
            num_logs = input("Enter the number of logs to generate (default is 500): ").strip()
            if not num_logs.isdigit():
                num_logs = 500
            else:
                num_logs = int(num_logs)
            
            clear_terminal()
            tprint("Generating Logs", font="slant")
            generate_logs(file_name, num_logs)
        
        elif choice == "2":
            print(Fore.CYAN + "Exiting Log Generator. Stay secure!" + Style.RESET_ALL)
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

# Run the main function
if __name__ == "__main__":
    main()
