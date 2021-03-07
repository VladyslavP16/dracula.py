# Деление
x = 10
y = 2.5
print(x//y)

# Деление без остатка
x = 10
y = 5
print(x//y)

# Zero Division Error
try:
    print(24/0)
except ZeroDivisionError as e:
    print(e)

a = 5.16
b = 20.4
try:
    print(a/b)
except:
    if b == 0:
        print('ZeroDivisionError: ', ZeroDivisionError)
    else:
        print('TypeError: ', TypeError)

some_dict = [
    {"brand": "ford", "model": "MusTAng Gt500", "year": 2018},
    {"brand": "ZAZ", "model": "Fortza", "year": 2001},
    {"brand": "VW", "model": "Golf GTI", "year": 1999}
]

cars_sorted_year = sorted(some_dict, key=lambda k: k['year'])
brand_title = some_dict[0]['brand'].title()
some_dict[0]['brand'] = brand_title
modification = some_dict[0]['model']
elements = some_dict[0]['model'].split(' ')
some_dict[0]['model'] = f'{elements[0].title()} {elements[1].upper()}'

print(cars_sorted_year)

# txt = some_dict[1]['model']
# x=txt.maketrans("t", " ")
# print(txt.translate(x))

