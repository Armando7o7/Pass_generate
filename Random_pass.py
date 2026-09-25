import random


file_word = 'Пусть к словарю russian.txt'

translation_dict = {

    'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T',
    'Н': 'Y', 'Г': 'U', 'Ш': 'I', 'Щ': 'O', 'З': 'P',
    'Х': '[', 'Ъ': ']',
    'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F', 'П': 'G',
    'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L',
    'Ж': ';', 'Э': "'",
    'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V',
    'И': 'B', 'Т': 'N', 'Ь': 'M',
    'Б': ',', 'Ю': '.', 'Ё': '`',

    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't',
    'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'х': '[', 'ъ': ']',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g',
    'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
    'ж': ';', 'э': "'",
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v',
    'и': 'b', 'т': 'n', 'ь': 'm',
    'б': ',', 'ю': '.', 'ё': '`'
}

symbols = [".", ",", ";", ":", "?", "!", "—", "-", "–", "*"]


def load_words(file_word, cnt):

    with open(file_word, mode='r', encoding='UTF-8') as f:
        words = [
            line.strip()
            for line in f
            if len(line.strip()) >= cnt
        ]

    if not words:
        raise ValueError(
            f"В словаре нет слов длиной минимум {cnt} символов."
        )

    return words


def generate_password(n, cnt, words):
    selected_words = []
    password = ""

    for i in range(n):
        word = random.choice(words)
        selected_words.append(word)

        part = word[:cnt]

        password += part[0].upper() + part[1:]

    return password, selected_words


def translate(password):

    result = ""

    for char in password:
        result += translation_dict.get(char, char)

    return result


def generate_password_data(n, cnt, words):

    password, selected_words = generate_password(
        n,
        cnt,
        words
    )

    password = translate(password)

    number = random.randint(10, 100)
    symbol = random.choice(symbols)

    final_password = str(number) + symbol + password

    phrase = " ".join(selected_words)

    return final_password, phrase


def main():

    try:
        count = int(input("Количество паролей: "))
        n = int(input("Количество слов в одном пароле: "))
        cnt = int(input("Количество букв из каждого слова: "))

        if count <= 0:
            print("Количество паролей должно быть больше 0.")
            return

        if n <= 0:
            print("Количество слов должно быть больше 0.")
            return

        if cnt <= 0:
            print("Количество букв должно быть больше 0.")
            return

        words = load_words(file_word, cnt)

        for i in range(count):

            password, phrase = generate_password_data(
                n,
                cnt,
                words
            )

            print(f"Парольная фраза: {phrase}")
            print(f"Пароль:           {password}")

    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()