from colorama import Fore, Style, init
import os, datetime
init(autoreset=True)

# ===============================
# CLEAR SCREEN
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ===============================
# BANNER / WELCOME
# ===============================
def banner():
    clear()
    print(Fore.GREEN + "🌴  SaWiT OS - Nugra21")
    print(Fore.WHITE + "    Custom Terminal Operating System")
    print(Fore.CYAN + "    Linux-like • Python-based • CLI\n")

    print(Fore.WHITE + "    Ketik " + Fore.YELLOW + "BANTUAN" + Fore.WHITE + " untuk melihat semua command")
    print(Fore.WHITE + "    Ketik " + Fore.YELLOW + "NEOFETCH" + Fore.WHITE + " untuk info sistem\n")

# ===============================
# PROMPT TERMINAL
# ===============================
def prompt(user, role, path):
    role_tag = (
        Fore.RED + "PEJABAT"
        if role == "pejabat"
        else Fore.GREEN + "USER"
    )

    return (
        Fore.CYAN + user +
        Fore.WHITE + "@" +
        Fore.GREEN + "sawitos " +
        Fore.WHITE + "[" +
        Fore.YELLOW + path +
        Fore.WHITE + "] " +
        role_tag +
        Fore.WHITE + " ❯ " +
        Style.RESET_ALL
    )

# ===============================
# NEOFETCH (SYSTEM INFO)
# ===============================
def neofetch(system, user):
    print(Fore.GREEN + "🌴 SaWiT OS - Nugra21\n")

    print(Fore.CYAN + "OS        " + Fore.WHITE + ": " + system.get("os", "-"))
    print(Fore.CYAN + "Version   " + Fore.WHITE + ": " + system.get("version", "-"))
    print(Fore.CYAN + "Kernel    " + Fore.WHITE + ": " + system.get("kernel", "-"))
    print(Fore.CYAN + "Creator   " + Fore.WHITE + ": " + system.get("creator", "-"))
    print(Fore.CYAN + "User      " + Fore.WHITE + ": " + user)
    print(Fore.CYAN + "Shell     " + Fore.WHITE + ": SawitShell")
    print(Fore.CYAN + "Time      " + Fore.WHITE + ": " + str(datetime.datetime.now()))

    print(Fore.GREEN + "\n🌴  Keep planting code, keep harvesting skill 🌴\n")
