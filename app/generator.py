from core.config import letters_data, symbols_data
import secrets


def password_generator(length):
    chars = (
        letters_data +
        [c.upper() for c in letters_data] +
        [str(i) for i in range(10)] +
        symbols_data
        )
    return''.join(secrets.choice(chars) for _ in range(length))
