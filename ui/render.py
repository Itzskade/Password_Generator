import os
from ui.ascii import ascii_design
from core.colors import colors


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_logo():
    clear()
    print(colors.PURPLE + ascii_design + colors.RESET)


def show_attempts(attempts, max_attempts):
    bar = "●" * attempts + "○" * (max_attempts - attempts)
    print(f"Attempts: [{bar}]")


def abort():
    print_logo()
    print(f"\n{colors.RED}[✗] Process aborted successfully.{colors.RESET}\n")


def max_errors():
    print(f"\n{colors.RED}[✗] Maximum attempts reached. Exiting.{colors.RESET}\n")


def history_error():
    print_logo()
    print(f"\n{colors.RED}[✗] No password history yet{colors.RESET}\n")


def exiting():
    print_logo()
    print(f"""{colors.ROSE}
    ╔════════════════════════════╗
    ║          GOODBYE           ║
    ║      Process finished      ║
    ╚════════════════════════════╝
        {colors.RESET}""")


def print_password(password):
    print(f"\n{colors.GREEN}[✓] Your password: {password}{colors.RESET}\n")