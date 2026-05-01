from core.colors import colors


def get_menu_option():
    print(f"""{colors.YELLOW}1. Generate password by lenght\n2. Regenerate\n3. History\n4. Exit{colors.RESET}\n""")
    return int(input(f"{colors.BLUE}[➤ ] Select an option: {colors.RESET}"))


def ask_password_length():
    return int(input(f"\n{colors.BLUE}[➤ ] Please specify the desired password length: {colors.RESET}"))