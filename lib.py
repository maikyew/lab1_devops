def check_password_length(password):
    """Перевіряє, чи пароль містить не менше 8 символів."""
    return len(password) >= 8


def check_password_digit(password):
    """Перевіряє, чи містить пароль хоча б одну цифру."""
    return any(char.isdigit() for char in password)


def password_strength(password):
    """Визначає рівень надійності пароля."""
    if check_password_length(password) and check_password_digit(password):
        return "Надійний пароль"
    return "Слабкий пароль"