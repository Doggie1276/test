from random import randint
from time import sleep

a = int(input('Введите число от:'))
b = int(input('Введите число до:'))

result = randint(a, b)

print(f"Подбираем число в диапозоне от {a} до {b}...")
sleep(1)
print(f"Секунду...")
sleep(1)
print(f"Случайное число: {result}")
