import secrets
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_password(length: int = 12) -> str:
    '''Generates a random passowrd with a minimum default length of 12 characters'''
    characters = ascii_letters + digits + punctuation
    if length < 12:
        raise ValueError("Password length must be at least 12 characters")
    try:
        list_password = list(
            "".join(
                secrets.choice(ascii_uppercase)
                + secrets.choice(ascii_lowercase)
                + secrets.choice(digits)
                + secrets.choice(punctuation)
            )
        )
        for _ in range(length - 4):
            list_password.append(secrets.choice(characters))
        secrets.SystemRandom().shuffle(list_password)
        return "".join(list_password)
    except Exception as e:
        print(f"An error occurred: {e} - Please try again.")


if __name__ == "__main__":
    print(generate_password())
