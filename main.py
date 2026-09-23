from lib import password_strength


def main():
    """Запускає перевірку надійності пароля."""
    password = input("Введіть пароль: ")
    result = password_strength(password)
    print("Результат:", result)


if __name__ == "__main__":
    main()