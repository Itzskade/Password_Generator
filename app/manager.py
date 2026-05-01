from ui.render import print_logo, abort, print_password, exiting, history_error
from app.controller import prompt_password_generation
from ui.cli import get_menu_option
from core.colors import colors
from app.generator import password_generator


def password_manager():
    print_logo()
    last_length = None
    history = []
    max_history = 10
    try:
        while True:
            choose = get_menu_option()
            if choose == 1:
                last_length = prompt_password_generation()
            elif choose == 2:
                print_logo()
                if last_length is None or not (10 <= last_length <= 128):
                    print(f"\n{colors.RED}[✗] Generate a password first.{colors.RESET}\n")
                else:
                    password = password_generator(last_length)
                    history.append(password)
                    history = history[-max_history:]
                    print(f"{colors.RED}Length: {last_length}{colors.RESET}")
                    print_password(password)
            elif choose == 3:
                print_logo()
                if len(history) == 0:
                    history_error()
                else:
                    print(f"{colors.BLUE}History{colors.RESET}\n" )
                    for item in history:
                        print(f"{colors.GREEN}{item}")
                    print(f"{colors.RESET}")
            elif choose == 4:
                return exiting()
            else:
                print_logo()
                print(f"\n{colors.RED}[✗] Please choose a number between 1 and 4.{colors.RESET}\n")

    except KeyboardInterrupt:
        abort()
    except EOFError:
        abort()
