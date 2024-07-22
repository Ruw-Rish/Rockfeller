import random
import csv
import requests
from bs4 import BeautifulSoup
import os
import socket
import time
import string
from colorama import Fore, init
import subprocess

# Инициализация colorama
init(autoreset=True)

# Функция для создания градиентного текста
def create_gradient_text(text, start_color, end_color):
    def interpolate_color(start, end, factor):
        return round(start + (end - start) * factor)

    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    gradient_text = ""
    length = len(text)
    for i, char in enumerate(text):
        factor = i / length
        r = interpolate_color(start_color[0], end_color[0], factor)
        g = interpolate_color(start_color[1], end_color[1], factor)
        b = interpolate_color(start_color[2], end_color[2], factor)
        gradient_text += rgb_to_ansi(r, g, b) + char
    gradient_text += Fore.RESET
    return gradient_text

# Определение начального и конечного цветов (RGB)
start_color = (255, 0, 0)  # Красный
end_color = (0, 0, 255)    # Синий

# ASCII арт
ascii_art = """
  
██████╗  ██████╗  ██████╗██╗  ██╗███████╗███████╗███████╗██╗     ██╗     ███████╗██████╗ 
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔════╝██╔════╝██║     ██║     ██╔════╝██╔══██╗
██████╔╝██║   ██║██║     █████╔╝ █████╗  █████╗  █████╗  ██║     ██║     █████╗  ██████╔╝
██╔══██╗██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══╝  ██╔══╝  ██║     ██║     ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝╚██████╗██║  ██╗███████╗██║     ███████╗███████╗███████╗███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
       OWNER: @Susanoooooooo |Version 1.5                                       
 """

# Список цитат с указанием авторов
quotes = {
    "Albert Einstein": "Стремитесь не к успеху, а к ценностям, которые он дает.",
    "Steve Jobs": "Будьте голодными, будьте глупыми.",
    "Mark Twain": "Самый лучший способ начать делать - прекратить говорить и начать делать.",
    "Bill Gates": "Сложные задачи требуют терпения и настойчивости.",
    "Winston Churchill": "Успех - это способность идти от неудачи к неудаче, не потеряв энтузиазма.",
    "Arthur Rubinstein": "Путь к успеху - это пройти половину пути."
}

# Функция для выбора случайной цитаты из списка
def get_random_quote():
    author, quote = random.choice(list(quotes.items()))
    return quote

# Функция для чтения базы данных из CSV файла
def read_database():
    data = []
    with open('database.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Функция для получения WHOIS информации об IP-адресе
def get_whois_info(ip):
    url = 'https://whois.ru/'
    payload = {'domain': ip}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, params=payload, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлекаем информацию
    ip_info = soup.find('div', class_='row sn-whois-reginfo')

    if ip_info:
        ip_info_text = ip_info.find('pre').text
        return ip_info_text
    else:
        return "Информация не найдена"

# Функция для поиска по базе данных номеров телефонов
def search_phone(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 5:
            phone = data[1]
            if search_value in phone:
                id = data[0]
                username = data[2]
                first_name = data[3]
                last_name = data[4]
                print(f'''{Fore.RED}
                [+]ID пользователя: {id}
                [+]Username: {username}
                [+]Имя: {first_name}
                [+]Фамилия: {last_name}
                {Fore.GREEN}
                      ''')
                time.sleep(4)
                print("Ничего не найдено по базам данных.")

# Функция для очистки консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для выполнения файла number.py
def run_number_script():
    subprocess.run(['python', 'number.py'])

# Функция для выполнения swat.py
def run_swat_script():
    subprocess.run(['python', 'swat.py'])

# Функция для выполнения файла ip.py
def run_ip_script():
    subprocess.run(['python', 'ip.py'])

# Функция для выполнения файла DDos.py
def run_ddos_script():
    subprocess.run(['python', 'DDos.py'])

# Функция для обработки выбора пользователя
def choice_selected(choice, name):
    if choice == 1:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Пробив по базе данных:")
        phone = input(f'{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Номер телефона: {Fore.GREEN}')
        search_phone('database.csv', phone)
    elif choice == 2:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Запуск Поиска по IP")
        run_ip_script()
    elif choice == 3:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Пробив по номеру:")
        phone = input(f'{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Номер телефона: {Fore.GREEN}')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        try:
            response = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone, headers=headers)
            data = response.json()
            user_country = data['country']['english']
            user_id = data['country']['id']
            user_location = data['country']['location']
            user_city = data['capital']['english']
            user_lat = data['capital']['latitude']
            user_log = data['capital']['longitude']
            user_post = data['capital']['post']
            user_oper = data['0']['oper']
            uty = requests.get("https://api.whatsapp.com/send?phone="+phone, headers=headers)
            if uty.status_code == 200:
                utl2 = "https://api.whatsapp.com/send?phone="+phone
            else:
                utl2 = 'Not founded!'
            userr_all_info = f'{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Страна: {Fore.GREEN}{str(user_country)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] ID: {Fore.GREEN}{str(user_id)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Локация {Fore.GREEN}{str(user_location)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Город: {Fore.GREEN}{str(user_city)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Широта: {Fore.GREEN}{str(user_lat)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Долгота: {Fore.GREEN}{str(user_log)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Почтовый индекс: {Fore.GREEN}{str(user_post)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Оператор: {Fore.GREEN}{str(user_oper)}\n{Fore.CYAN}[{Fore.RED}*{Fore.CYAN}] Ссылка на WhatsApp: {Fore.GREEN}{str(utl2)}'
        except requests.exceptions.SSLError:
            print("An SSL error occurred while trying to connect to the website.")
        except Exception as e:
            print("An error occurred:", e)
    elif choice == 4:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Авторы: @Susanoooooooo")
    elif choice == 5:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("DDoS атака:")
        run_ddos_script()
    elif choice == 6:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Генерация ключей Mullvad:")
        KeyGenerator().main_menu()
    elif choice == 7:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Генерация токенов Discord:")
        num_keys = int(input("Введите количество ключей для генерации: "))
        token_length = 72
        keys = [generate_discord_key(token_length) for _ in range(num_keys)]
        filename = "token_discord.txt"
        save_keys_to_file(keys, filename)
        print(f"{num_keys} ключей было сгенерировано и сохранено в файл {filename}.")
    elif choice == 8:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Пробив по номеру (запуск скрипта number.py):")
        run_number_script()
    elif choice == 9:
        clear_console()
        print(create_gradient_text(ascii_art, start_color, end_color))
        print("Странный текст:")
        run_swat_script()
    elif choice == 99:
        print("До встречи, {}!".format(name))
        quit()
    else:
        print("Некорректный выбор. Пожалуйста, выберите существующий пункт из меню.")

# Класс для генерации ключей Mullvad
class KeyGenerator:
    def __init__(self):
        self.generated_count = 0

    def create_keys(self, count):
        for _ in range(count):
            key = ''.join(random.choice(string.digits) for _ in range(16))
            with open('generated_keys.txt', 'a') as file:
                file.write(key + '\n')
            self.generated_count += 1

    def main_menu(self):
        count = int(input('Сколько ключей сгенерировать?: '))
        self.create_keys(count)
        print(f'Успешно создано {count} ключей и сохранено в "generated_keys.txt"!')

# Функции для генерации токенов Discord и их сохранения
def generate_discord_key(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def save_keys_to_file(keys, filename):
    with open(filename, 'w') as file:
        for key in keys:
            file.write(key + '\n')

# Очистка экрана
clear_console()

# Проверка наличия файла с именем пользователя
if os.path.exists('username.txt'):
    with open('username.txt', 'r') as file:
        name = file.read().strip()
else:
    # Запрос имени пользователя
    name = input("Введите ваше имя: ")
    # Создание файла с именем пользователя
    with open('username.txt', 'w') as file:
        file.write(name)

# Вывод ASCII арта с градиентом
print(create_gradient_text(ascii_art, start_color, end_color))

# Вывод приветствия с рандомной цитатой из списка
print(f"\nПриветствую, {name}! \"{get_random_quote()}\"")

# Функция для форматирования меню в два столбца с равным расстоянием между ними
def format_menu(options):
    max_len = max(len(option) for option in options)
    formatted_menu = []
    for i in range(0, len(options), 2):
        left = options[i].ljust(max_len + 2)
        if i + 1 < len(options):
            right = options[i + 1].ljust(max_len + 2)
        else:
            right = ""
        formatted_menu.append(left + right)
    return "\n".join(formatted_menu)

# Основной цикл программы
while True:
    # Опции меню
    menu_options = [
        "[1]. Поиск по базе данных",
        "[2]. Поиск по IP",
        "[3]. Пробив по номеру",
        "[4]. Информация об авторах",
        "[5]. DDoS атака",
        "[6]. Генерация ключей Mullvad",
        "[7]. Генерация токенов Discord",
        "[8]. Пробив по номеру (2 больше инфы)",
        "[9]. Странный текст",
        "[99]. Выход"
    ]

    # Вывод меню выбора действий с градиентным текстом
    print("\nВыберите Функцию:")
    formatted_menu = format_menu(menu_options)
    print(create_gradient_text(formatted_menu, start_color, end_color))

    # Получение выбора пользователя
    choice = input("\n[?]Выберите опцию~> ")

    # Проверка выбора пользователя и выполнение соответствующего действия
    try:
        choice = int(choice)
        choice_selected(choice, name)
    except ValueError:
        print("Пожалуйста, введите число.")