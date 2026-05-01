from ui.render import clear, print_logo, show_attempts, max_errors, print_password
from core.colors import colors
from app.generator import password_generator
from ui.cli import ask_password_length


def prompt_password_generation():
    attempts = 5
    print_logo()
    for attempt in range(1, attempts + 1):
        try:
            length = ask_password_length()
            if length < 10 or length > 128:
                print_logo()
                show_attempts(attempt, attempts)
                print(f"{colors.RED}[WARNING] Password length must be between 10 and 128{colors.RESET}")
            else:
                print_logo()
                password = password_generator(length)
                print(f"{colors.RED}Length: {length}{colors.RESET}")
                print_password(password)
                return length
        except ValueError:
            print_logo()
            show_attempts(attempt, attempts)
            print(f"{colors.RED}[WARNING] Input must be a number{colors.RESET}")
    print_logo()
    show_attempts(attempt, attempts)
    max_errors()