import os
from colorama import Fore, Style, init
from banner import show_banner
from utils import log_activity, pause

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print(Fore.CYAN + "1. System Info")
    print(Fore.CYAN + "2. Write Log")
    print(Fore.CYAN + "3. View Logs")
    print(Fore.CYAN + "4. About App")
    print(Fore.RED  + "0. Exit")

def system_info():
    print(Fore.GREEN + "\nSystem Information")
    print("-" * 25)
    print(f"OS      : {os.name}")
    print(f"User    : {os.getenv('USERNAME') or os.getenv('USER')}")
    print(f"Path    : {os.getcwd()}")
    log_activity("Viewed system information")

def write_log():
    msg = input("Enter log message: ")
    log_activity(msg)
    print(Fore.YELLOW + "Log saved successfully.")

def view_logs():
    print(Fore.MAGENTA + "\nActivity Logs\n")
    try:
        with open("data/logs.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No logs found.")

def about():
    print(Fore.BLUE + """
Python Developer Lab
Version : 1.0.0
Author  : Open Source Learner

A simple but powerful terminal-based Python project.
""")

def main():
    while True:
        clear()
        show_banner()
        menu()
        choice = input("\nSelect option: ")

        if choice == "1":
            system_info()
        elif choice == "2":
            write_log()
        elif choice == "3":
            view_logs()
        elif choice == "4":
            about()
        elif choice == "0":
            log_activity("Exited application")
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

        pause()

if __name__ == "__main__":
    main()
