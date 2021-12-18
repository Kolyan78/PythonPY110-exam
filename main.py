from faker import Faker
import conf
import random
import json

fake = Faker()
Faker.seed(0)

def get_title(): # Функция-генератор, каждый раз при вызове выдающая случайное название книги
    # Выполнена в виде генератора, чтобы каждый раз не открывать файл.
    # Функция один раз открывает файл, создает список, каждый элмент которого строка из файл,
    # а далее при каждом вызове просто выдает случайный элемент списка
    with open("books.txt", encoding='utf8') as f:
        list_ = [x.rstrip() for x in f]
    while True:
        yield random.choice(list_)

def get_year(): # Функция выдает случайный год в заданном диапазоне от 1800 до текущего
    return random.randint(1800, 2021)

def get_pages(): # Функция выдает случайное количество страниц в книге от 10 до 500
    return random.randint(10,500)

def get_isbn13(): # Функция выдает фейковый ISBN13
    return fake.isbn13()

def get_rating(): # Функция выдает случайный рейтинг от 0 до 5 включительно, результат округляется до одного знака после запятой
    return round(random.randint(0, 4) + random.random(), 1)

def get_price(): # Функция выдает случайную стоимость книги в диапазоне от 10 до 99.99, результат округляется до двух знаков после запятой
    return round(random.randint(10, 99) + random.random(), 2)

def get_author(): # Функция для генерации фейкового автора, количество авторов выбрается случайным образом от 1 до 3
    return [fake.name() for _ in range(random.randint(1, 3))]

def get_item(pk = 1): # Функция генератор для создания словаря.
    # Пока не знаю как сделать параметр pk изменяющимся при каждом вызове.
    # Он всегда выдет одно и то же число
    while True:
        yield {
            "model": conf.MODEL,
            "pk": pk,
            "fields": {
                "title": next(get_title()),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn13(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_author()
            }
        }
        pk += 1

def func(i = 1):
    while True:
        yield i
        i += 1


if __name__ == "__main__":
    item = get_item()
    list_ = [next(item) for _ in range(100)]
    with open("output.json", "w", encoding="utf8") as f:
        f.write(json.dumps(list_, indent = 4, ensure_ascii=False))