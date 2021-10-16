import random

ARRAY_SYMBOLS = ['0', '1', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
                 '@', '!']
# Получаем количкство символов в пороле.
COUNT_COUNT_SYMBOLS = 4

costom_count_symbols = int(input('Введите количество символов в пороле:'))
if costom_count_symbols > 0:
    count_symbols = costom_count_symbols
else:
    count_symbols = COUNT_COUNT_SYMBOLS

count_variant = len(ARRAY_SYMBOLS) ** count_symbols

def random_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]

password_array = [i for i in range(0, count_symbols)]

print(password_array)

print(f'Количество доступных вариантов: {len(ARRAY_SYMBOLS)}')

print(f'Количество доступных вариантов :{count_variant}')

print(count_symbols ** len(ARRAY_SYMBOLS))

print(ARRAY_SYMBOLS[random.randint(0, len(ARRAY_SYMBOLS) - 1)])

password = ''

for i in password_array:
    password = password + f'{random_symbols()}'

print(password)

with open('password.txt', 'a') as password_str:
    password_str.write('{}\n'.format(f'{[password]}'))