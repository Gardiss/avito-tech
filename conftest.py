from dotenv import load_dotenv


load_dotenv() #нужно, чтобы  переменные окружения, такие как логины/пароли/api tokens  не хранились в коде, а подгружались из файла .env

pytest_plugins = [
    'fixtures.page',
    'fixtures.user_auth'
]
