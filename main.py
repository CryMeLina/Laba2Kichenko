import re
import requests

URL_PATTERN = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s"\'<>]*)?'


def is_valid_url(url_string):
    match = re.fullmatch(URL_PATTERN, url_string.strip())
    return match is not None


def find_urls_in_text(text):
    return re.findall(URL_PATTERN, text)


def find_urls_from_web(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return find_urls_in_text(response.text)
    except requests.RequestException as error:
        print(f"Ошибка при загрузке страницы: {error}")
        return []


def find_urls_from_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            return find_urls_in_text(content)
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        return []
    except Exception as error:
        print(f"Ошибка при чтении файла: {error}")
        return []


def main():
    while True:
        print("\n--- Поиск и проверка гиперссылок ---")
        print("1. Проверить одну ссылку (ввод с клавиатуры)")
        print("2. Найти все ссылки в тексте (ввод с клавиатуры)")
        print("3. Найти все ссылки на веб-странице по URL")
        print("4. Найти все ссылки в локальном файле")
        print("0. Выход")

        choice = input("Выберите действие (0-4): ").strip()

        if choice == "1":
            user_url = input("Введите ссылку для проверки: ")
            if is_valid_url(user_url):
                print("Результат: Ссылка корректна!")
            else:
                print("Результат: Это НЕ корректная ссылка.")

        elif choice == "2":
            user_text = input("Введите HTML-код или текст со ссылками: ")
            urls = find_urls_in_text(user_text)
            print(f"Найдено ссылок ({len(urls)}):")
            for item in urls:
                print(f" - {item}")

        elif choice == "3":
            target_url = input("Введите адрес сайта (например, https://example.com): ").strip()
            urls = find_urls_from_web(target_url)
            print(f"Найдено ссылок на странице ({len(urls)}):")
            for item in urls:
                print(f" - {item}")

        elif choice == "4":
            path = input("Введите путь к файлу (например, index.html): ").strip()
            urls = find_urls_from_file(path)
            print(f"Найдено ссылок в файле ({len(urls)}):")
            for item in urls:
                print(f" - {item}")

        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 0 до 4.")


if __name__ == "__main__":
    main()