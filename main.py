import random
import string

def generate_password(length=12):
    """Rastgele bir şifre oluşturur."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test için
if __name__ == "__main__":
    print("Generated Password:", generate_password())
