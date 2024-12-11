import re
import requests
from bs4 import BeautifulSoup

def find_hex_colors(text):
    """
    Находит все синтаксически корректные цвета в формате HEX в переданном тексте.
    Формат HEX: #rrggbb или #rgb, где r, g, b - шестнадцатеричные цифры.
    """
    hex_color_pattern = r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b"
    return re.findall(hex_color_pattern, text)

def find_hex_colors_in_url(url):
    """
    Находит все HEX-цвета на веб-странице по URL.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return find_hex_colors(text)
def find_hex_colors_in_file(file_path):
    """
    Находит все HEX-цвета в загруженном файле.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return find_hex_colors(text)

# C:/DDD/laba_3_pp/hcg.txt
#https://get-color.ru/
#https://habr.com/ru/articles/189766/
if __name__ == "__main__":
    print("Выберите источник для поиска HEX-цветов:")
    print("1. Ввести текст вручную")
    print("2. Указать URL веб-страницы")
    print("3. Указать путь к файлу")

    choice = input("Ваш выбор (1/2/3): ")

    if choice == '1':
        user_text = input("Введите текст: ")
        colors = find_hex_colors(user_text)
        print("Найденные HEX-цвета:", colors)

    elif choice == '2':
        url = input("Введите URL: ")
        try:
            colors = find_hex_colors_in_url(url)
            print("Найденные HEX-цвета:", colors)
        except requests.RequestException as e:
            print("Ошибка при запросе к URL:", e)

    elif choice == '3':
        file_path = input("Введите путь к файлу: ")
        try:
            colors = find_hex_colors_in_file(file_path)
            print("Найденные HEX-цвета:", colors)
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print("Ошибка при чтении файла:", e)

    else:
        print("Некорректный выбор.")
