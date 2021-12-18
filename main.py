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

def get_year(): #
    return random.randint(1001, 2022)

def get_pages():
    return random.randint(10,500)

def get_isbn13():
    return fake.isbn13()

def get_rating():
    return round(random.randint(0, 4) + random.random(), 1)

def get_price():
    return round(random.randint(10, 99) + random.random(), 2)

def get_author():
    return [fake.name() for _ in range(random.randint(1, 3))]

def get_item(pk=1):
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


if __name__ == "__main__":
    list_ = [next(get_item()) for _ in range(5)]
    print(list_)
    with open("output.json", "w", encoding="utf8") as f:

        f.write(json.dumps(list_))
        #


    # for _ in range(5):
    #     print(next(get_item()))

    # for _ in range(10):
    #     print(next(get_title()))
    #     print(get_year())
    #     print(get_pages())
    #     print(get_isbn13())
    #     print(get_rating())
    #     print(get_price())
    #     print(get_author())
    #     print("---------------------------")