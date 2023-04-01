from datetime import time

def test_dark_theme():

    current_time = time(hour=23)
    is_dark_theme = None
    if time(22) <= current_time or current_time <= time(6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

    current_time = time(hour=16)
    dark_theme_enabled = True
    is_dark_theme = None
    if time(22) <= current_time or current_time <= time(6):
        is_dark_theme = True
    elif dark_theme_enabled == True:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
# ищем пользователя с именем Ольга
    suiable_user = None
    for user in users:
        if user['name'] == "Olga":
            suiable_user = user
    assert suiable_user == {"name": "Olga", "age": 45}

# ищем всех пользователей младше 20 лет
    suiable_users = None
    for user in users:
        if user['age'] < 20:
            suiable_users = [user for user in users if user['age'] < 20]
    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def make_readble_function(func_name, *args):
    return f"{func_name.__name__.replace('_', ' ').title()} [{', '.join(args)}]"

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = make_readble_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = make_readble_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = make_readble_function(find_registration_button_on_login_page, page_url,button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"