a = 2
b = 0.5
print(a + b)

name = 'ВВЕДИТЕ ВАШЕ ИМЯ'
print(name)
print('Привет, {names}!'.format(names=name.lower().capitalize()))

v = int(input('Введите число от 1 до 10: '))
print(v + 10)

name = str(input('Введите ваше имя: '))
print(f'Привет, {name}! Как дела?')

print(float('1')) #1.0
print(int('2.5')) # ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1)) #True
print(bool('')) #False
print(bool(0)) #False