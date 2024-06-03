from decimal import Decimal
import datetime


DATE_FORMAT = '%Y-%m-%d'

goods = {}

def add (items, title, amount, expiration_date=None):
    # преобразовываем строку в дату
    date_as_datetime = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date() if expiration_date else None
    if title in items:    # проверить есть ли title в словаре
        list.append(items[title], {'amount': amount, 'expiration_date' : date_as_datetime}) #добавляем значения для существующего ключа title
    else:
        items[title] = [{'amount': amount, 'expiration_date' : date_as_datetime}] # создаем новый элемент словаря, если товара нет


def add_by_note(items, note):
    note_list = str.split(note)           # разбиваем строку, получаем список характеристик товаров  
    if '-' in note_list[-1]:              # проверяем является последняя часть строки датой
        expiration_date = note_list[-1]
    else:
        expiration_date = None
    title = ''
    if expiration_date:                   # если дата есть, определяем amount как предпоследний элемент списка
        amount = Decimal(note_list[-2])
        for word in note_list[:-2]:       # и определяем название товара
            title += str(word) + ' '
        title = str.rstrip(title)         # убираем пробел в конце строки  
    else:                                 # если даты нет, определяем amount как последний элемент списка
        amount = Decimal(note_list[-1])
        for word in note_list[:-1]:       # и записываем название товара
            title += str(word) + ' '
        title = str.rstrip(title) 
    add(items, title, amount, expiration_date)          

add_by_note(goods, 'Яйца гусиные 4 2023-12-12') 
add_by_note(goods, 'Пельмени 8.2 2023-12-14')
add_by_note(goods, 'Пельмени 2')
print(goods)   

def find(items, needle):
    title_list = list(items.keys())
    find_titles = []
    needle_lower = str.lower(needle)
    for i in range(len(title_list)):
        title_lower = str.lower(title_list[i])
        if str.find(title_lower, needle_lower) != -1:
           list.append(find_titles, title_list[i])
    return find_titles

print(find(goods, 'льм'))
print(find(goods, 'про'))

def amount(items, needle):
    title_list = find(items, needle) # получим список подходящих товаров
    amount = Decimal(0)
    for title in title_list: # для каждого товара в списке
        parts = items[title] # создадим список, содержащий все характеристики каждого товара
        for part in parts:
            amount += Decimal(part['amount']) # посчитаем количество
    return amount

print(amount(goods, 'пел'))
print(amount(goods, 'мор'))
print(amount(goods, 'ца'))

def expire(items, in_advance_days=0):
    result = []
    today = datetime.date.today()
    date_in_advance = today + datetime.timedelta(days=in_advance_days)
    for title in items:
        parts = items[title]
        amount = 0
        for part in parts:
            if part['expiration_date'] != None and (part['expiration_date'] <= today or part['expiration_date'] <= date_in_advance):
                amount += Decimal(part['amount'])
        if amount > 0:
            list.append(result, (title, amount))
    return result

print(expire(goods))
print(expire(goods, 5))
